# Querying Reference

The Prometheus HTTP API endpoints for querying a Prometheus or Thanos Querier server.

Every command below assumes:
- `$PROM_URL` — server base URL (see cluster-access.md)
- `$TOKEN` — bearer token; omit the `Authorization` header for unauthenticated port-forwards

All query endpoints accept both GET and POST. Always use `--data-urlencode` (which implies POST) so PromQL special characters are encoded correctly.

## Response Envelope

Every endpoint returns:

```json
{"status": "success", "data": { ... }}
```

or on failure (HTTP 4xx with a body — always check):

```json
{"status": "error", "errorType": "bad_data", "error": "parse error: ..."}
```

Guard with jq:

```bash
... | jq -r 'if .status == "success" then .data else "ERROR: \(.errorType): \(.error)" end'
```

For query results, `.data.resultType` is `vector` (instant), `matrix` (range), or `scalar`. Sample values are `[<unix-ts>, "<string>"]` — convert with `tonumber`.

## Table of Contents

1. [Instant Query](#instant-query)
2. [Range Query](#range-query)
3. [Series Discovery](#series-discovery)
4. [Label Discovery](#label-discovery)
5. [Metric Metadata](#metric-metadata)

---

## Instant Query

Evaluate a PromQL expression at a single point in time.

```
POST /api/v1/query
```

| Parameter | Default | Description |
|---|---|---|
| `query` | | PromQL expression (required) |
| `time` | now | Evaluation time (RFC3339 or Unix timestamp) |
| `timeout` | server default | Evaluation timeout (e.g. `30s`) |

### Examples

```bash
# Basic query
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=up' \
  "$PROM_URL/api/v1/query" | jq '.data.result'

# Query at a specific time
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=up' \
  --data-urlencode 'time=2024-01-15T10:00:00Z' \
  "$PROM_URL/api/v1/query" | jq '.data.result'

# Aggregated query — extract namespace and value
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=sum(rate(container_cpu_usage_seconds_total[5m])) by (namespace)' \
  "$PROM_URL/api/v1/query" | \
  jq '.data.result[] | {namespace: .metric.namespace, value: .value[1]}'

# Top 10 memory consumers
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=topk(10, container_memory_working_set_bytes{container!=""})' \
  "$PROM_URL/api/v1/query" | \
  jq '.data.result[] | {pod: .metric.pod, namespace: .metric.namespace, bytes: .value[1]}'

# Sort results numerically by value
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=sum(rate(container_cpu_usage_seconds_total[5m])) by (namespace)' \
  "$PROM_URL/api/v1/query" | \
  jq '.data.result | sort_by(.value[1] | tonumber) | reverse'
```

---

## Range Query

Evaluate a PromQL expression over a time range.

```
POST /api/v1/query_range
```

| Parameter | Default | Description |
|---|---|---|
| `query` | | PromQL expression (required) |
| `start` | | Start time (RFC3339 or Unix timestamp, required) |
| `end` | | End time (RFC3339 or Unix timestamp, required) |
| `step` | | Resolution step (duration like `1m`, `5m`, `1h`, required) |

Result type is `matrix`: each series has `values: [[ts, "val"], ...]` instead of a single `value`.

### Examples

```bash
# Last hour, 1-minute resolution (cross-platform: tries GNU date first, falls back to BSD)
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=node_memory_MemAvailable_bytes' \
  --data-urlencode "start=$(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -v-1H +%Y-%m-%dT%H:%M:%SZ)" \
  --data-urlencode "end=$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --data-urlencode 'step=1m' \
  "$PROM_URL/api/v1/query_range" | jq '.data.result'

# Last 24 hours, 5-minute resolution — min/max/last per instance
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) by (instance)' \
  --data-urlencode "start=$(date -u -d '1 day ago' +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -v-1d +%Y-%m-%dT%H:%M:%SZ)" \
  --data-urlencode "end=$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --data-urlencode 'step=5m' \
  "$PROM_URL/api/v1/query_range" | \
  jq '.data.result[] | {instance: .metric.instance,
       min: ([.values[][1] | tonumber] | min),
       max: ([.values[][1] | tonumber] | max),
       last: (.values[-1][1])}'
```

### Choosing Step Size

- **1m** — fine-grained, last 1-2 hours
- **5m** — standard, last 6-24 hours
- **15m** — daily overview
- **1h** — weekly/monthly trends

Rule of thumb: aim for 100-500 data points per series. Servers reject ranges exceeding ~11,000 points per series.

---

## Series Discovery

Find time series matching label selectors.

```
POST /api/v1/series
```

| Parameter | Default | Description |
|---|---|---|
| `match[]` | | Series selector (required, repeatable) |
| `start` | | Start time |
| `end` | | End time |

### Examples

```bash
# All series for a metric
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'match[]=container_cpu_usage_seconds_total' \
  "$PROM_URL/api/v1/series" | jq '.data'

# Series in a specific namespace
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'match[]=container_cpu_usage_seconds_total{namespace="kube-system"}' \
  "$PROM_URL/api/v1/series" | jq '.data'

# Multiple selectors (OR)
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'match[]=up' \
  --data-urlencode 'match[]=scrape_duration_seconds' \
  "$PROM_URL/api/v1/series" | jq '.data'
```

---

## Label Discovery

List label names or label values.

```
POST /api/v1/labels                 # all label names
GET  /api/v1/label/<name>/values    # values for one label
```

| Parameter | Default | Description |
|---|---|---|
| `match[]` | | Restrict to series matching selector (repeatable) |
| `start` | | Start time |
| `end` | | End time |

### Examples

```bash
# List all metric names (the __name__ label)
curl -sk -H "Authorization: Bearer $TOKEN" \
  "$PROM_URL/api/v1/label/__name__/values" | jq -r '.data[]'

# Grep for metrics related to a topic
curl -sk -H "Authorization: Bearer $TOKEN" \
  "$PROM_URL/api/v1/label/__name__/values" | jq -r '.data[]' | grep -i etcd

# List all namespaces that have metrics
curl -sk -H "Authorization: Bearer $TOKEN" \
  "$PROM_URL/api/v1/label/namespace/values" | jq -r '.data[]'

# List pods for a specific metric
curl -sk -G -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'match[]=container_cpu_usage_seconds_total' \
  "$PROM_URL/api/v1/label/pod/values" | jq -r '.data[]'

# List all label names
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'match[]=up' \
  "$PROM_URL/api/v1/labels" | jq -r '.data[]'
```

Note the `-G` on the `label/<name>/values` example: that endpoint is GET-only on some servers, and `-G` converts `--data-urlencode` parameters into the URL query string.

---

## Metric Metadata

Discover metric types and help strings — do this before writing PromQL against unfamiliar metrics.

```
GET /api/v1/metadata
```

| Parameter | Default | Description |
|---|---|---|
| `metric` | all | Restrict to one metric name |
| `limit` | | Max number of metrics returned |

### Examples

```bash
# Type and help for one metric
curl -sk -G -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'metric=apiserver_request_duration_seconds' \
  "$PROM_URL/api/v1/metadata" | jq '.data'

# Sample of all metadata (type, help) — large response, use limit
curl -sk -G -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'limit=100' \
  "$PROM_URL/api/v1/metadata" | jq '.data'
```

Knowing the type matters: counters need `rate()`/`increase()`, gauges are used directly, histograms are queried via their `_bucket`/`_sum`/`_count` series with `histogram_quantile()`.
