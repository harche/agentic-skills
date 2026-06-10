---
name: prometheus
description: Query and analyze Prometheus metrics on Kubernetes and OpenShift clusters via the Prometheus HTTP API using curl. Use when the user asks about Prometheus metrics, PromQL queries, metric analysis, alerting rules, recording rules, TSDB cardinality, or anything related to Prometheus monitoring — even if they just say "check metrics" or "why is CPU high on the cluster". Also trigger when the user mentions promtool, Thanos, or wants to inspect Prometheus rules or alerts.
---

# Prometheus Metrics Analysis via the HTTP API

Query and analyze Prometheus metrics on Kubernetes and OpenShift clusters using `curl` and `jq` against the Prometheus (or Thanos Querier) HTTP API. Everything `promtool query` does is a thin wrapper over this API, so no extra tooling is required.

## Prerequisites

- `curl` and `jq`
- `kubectl` or `oc` CLI with a valid kubeconfig pointing to the target cluster

## Critical Rules

These rules exist because they caused real failures during testing. Follow them exactly.

1. **Run setup + queries in a single bash call.** Shell variables (`$PROM_URL`, `$TOKEN`) do not persist across separate bash invocations. Combine setup and queries into one command using `&&`.

2. **Always pass PromQL via `--data-urlencode`.** Never hand-build URL query strings — PromQL is full of characters (`{`, `}`, `+`, `[`, `]`, `!`, `"`) that break unencoded URLs. `curl -s --data-urlencode 'query=...'` sends a POST with proper encoding; the Prometheus API accepts POST on all query endpoints.

3. **Check `.status` before parsing results.** Every API response is `{"status":"success|error", "data":{...}}`. A failed query still returns HTTP 400 with a JSON body — surface `.error` instead of silently parsing an empty result:
   ```bash
   ... | jq -r 'if .status == "success" then .data.result else "ERROR: \(.errorType): \(.error)" end'
   ```

4. **Token acquisition priority.** Inside a pod, use the mounted SA token first: `TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token 2>/dev/null || true)`. Only fall back to `oc whoami -t` when running outside a pod. The SA must have the `cluster-monitoring-view` ClusterRole bound for Prometheus/Thanos access on OpenShift.

5. **Thanos Querier returns 503 on `/-/healthy`.** This is expected — Thanos doesn't expose Prometheus's health endpoints. Verify connectivity by querying `up` instead.

6. **Sample values are JSON strings, not numbers.** A result value is `[<unix-ts>, "<value-as-string>"]`. Convert with `tonumber` in jq before doing math.

7. **Kill port-forwards when done.** If you started `kubectl port-forward ... & PF_PID=$!`, always `kill $PF_PID 2>/dev/null` at the end of the same bash call.

## Setup + Query (Single Bash Call)

Every session should follow this pattern in one bash command. Adapt the query section as needed.

### OpenShift

```bash
TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token 2>/dev/null || true) && \
if [ -z "$TOKEN" ]; then TOKEN=$(oc whoami -t 2>/dev/null || true); fi && \
if [ -z "$TOKEN" ]; then echo "ERROR: No token available"; exit 1; fi && \
HOST=$(oc -n openshift-monitoring get route thanos-querier -o jsonpath='{.status.ingress[].host}') && \
PROM_URL="https://$HOST" && \
# --- queries go here, chained with && ---
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=up' \
  "$PROM_URL/api/v1/query" | jq '.data.result | length'
```

### Kubernetes

```bash
export KUBECONFIG=<path-to-kubeconfig> && \
PROM_NS="monitoring" && \
PROM_SVC=$(kubectl get svc -n "$PROM_NS" -o jsonpath='{.items[?(@.spec.ports[*].port==9090)].metadata.name}') && \
kubectl port-forward -n "$PROM_NS" "svc/$PROM_SVC" 9090:9090 &
PF_PID=$! && sleep 2 && \
PROM_URL="http://localhost:9090" && \
# --- queries go here, chained with && ---
curl -s --data-urlencode 'query=up' "$PROM_URL/api/v1/query" | jq '.data.result | length' && \
# --- clean up ---
kill $PF_PID 2>/dev/null
```

## Query Examples

All examples assume `$PROM_URL` and `$TOKEN` are set (from the setup block above) and use `AUTH` as shorthand for `-H "Authorization: Bearer $TOKEN"`. Chain them in the same bash call.

```bash
# Instant query
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=up' \
  "$PROM_URL/api/v1/query" | jq '.data.result'

# Aggregated query — extract label and value
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=sum(rate(container_cpu_usage_seconds_total{container!=""}[5m])) by (namespace)' \
  "$PROM_URL/api/v1/query" | \
  jq -r '.data.result[] | "\(.metric.namespace): \(.value[1] | tonumber * 1000 | round / 1000) cores"'

# Range query (last hour, 1-minute steps)
# macOS: date -u -v-1H    Linux: date -u -d '1 hour ago'
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=node_memory_MemAvailable_bytes' \
  --data-urlencode "start=$(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -v-1H +%Y-%m-%dT%H:%M:%SZ)" \
  --data-urlencode "end=$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --data-urlencode 'step=1m' \
  "$PROM_URL/api/v1/query_range" | jq '.data.result'

# Discover all metric names
curl -sk -H "Authorization: Bearer $TOKEN" \
  "$PROM_URL/api/v1/label/__name__/values" | jq -r '.data[]'

# Find series matching a selector
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'match[]=container_cpu_usage_seconds_total{namespace="default"}' \
  "$PROM_URL/api/v1/series" | jq '.data'
```

## References

Detailed API references — read on demand when you need specifics:

|references/cluster-access.md — Discovery, auth, and port-forward setup for OpenShift and Kubernetes
|references/querying.md — Instant, range, series, label, and metadata endpoints with jq recipes
|references/rules-alerts.md — Inspect loaded alerting/recording rules, active alerts, and validate PromQL
|references/tsdb.md — Cardinality analysis and TSDB statistics via the status API

## Common PromQL Patterns

Useful starting points when the user asks broad questions:

| Question | PromQL |
|---|---|
| Which targets are down? | `up == 0` |
| CPU usage by namespace | `sum(rate(container_cpu_usage_seconds_total[5m])) by (namespace)` |
| Memory usage by pod | `container_memory_working_set_bytes{container!=""}` |
| Disk pressure | `node_filesystem_avail_bytes / node_filesystem_size_bytes < 0.1` |
| API server request rate | `sum(rate(apiserver_request_total[5m])) by (verb, resource)` |
| API server error rate | `sum(rate(apiserver_request_total{code=~"5.."}[5m])) by (resource)` |
| Pod restart count | `increase(kube_pod_container_status_restarts_total[1h]) > 0` |
| Node CPU saturation | `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) by (instance)` |
| etcd leader changes | `increase(etcd_server_leader_changes_seen_total[1h])` |
| Scrape duration | `scrape_duration_seconds` |

## Important

- For OpenShift, always query the Thanos Querier — it aggregates data from all Prometheus instances. From inside a cluster pod, prefer the in-cluster service `https://thanos-querier.openshift-monitoring.svc:9091` when cluster DNS is available; fall back to the route otherwise.
- Discover before querying: list metric names (`/api/v1/label/__name__/values`) and metadata (`/api/v1/metadata`) before writing PromQL against unfamiliar metrics.
- **Cross-platform date**: Use `date -u -d '1 hour ago' +FMT 2>/dev/null || date -u -v-1H +FMT` to work on both Linux (GNU date) and macOS (BSD date).
