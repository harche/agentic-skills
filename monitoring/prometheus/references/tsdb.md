# TSDB & Cardinality Reference

Analyze TSDB cardinality and server state via the status API. This is the go-to reference for diagnosing cardinality explosions and storage pressure.

## Table of Contents

1. [TSDB Cardinality Stats](#tsdb-cardinality-stats)
2. [Cardinality via PromQL](#cardinality-via-promql)
3. [Server Status](#server-status)
4. [Targets](#targets)

---

## TSDB Cardinality Stats

Head-block cardinality statistics: which metrics and labels have the most series.

```
GET /api/v1/status/tsdb
```

| Parameter | Default | Description |
|---|---|---|
| `limit` | 10 | Number of items per stat list |

**Note:** This endpoint is served by individual Prometheus instances, not aggregated by Thanos Querier. On OpenShift, query a Prometheus pod directly:

```bash
# Port-forward to a Prometheus instance
oc port-forward -n openshift-monitoring prometheus-k8s-0 9090:9090 &
PF_PID=$! && sleep 2 && \
curl -sk -H "Authorization: Bearer $TOKEN" \
  "http://localhost:9090/api/v1/status/tsdb" | jq '.data' && \
kill $PF_PID 2>/dev/null
```

### Output

```json
{
  "headStats": {
    "numSeries": 1234567,
    "numLabelPairs": 98765,
    "chunkCount": 2345678,
    "minTime": 1700000000000,
    "maxTime": 1700007200000
  },
  "seriesCountByMetricName":     [{"name": "apiserver_request_duration_seconds_bucket", "value": 50000}, ...],
  "labelValueCountByLabelName":  [{"name": "id", "value": 12000}, ...],
  "memoryInBytesByLabelName":    [{"name": "__name__", "value": 1048576}, ...],
  "seriesCountByLabelValuePair": [{"name": "namespace=openshift-monitoring", "value": 80000}, ...]
}
```

| Field | Diagnoses |
|---|---|
| `seriesCountByMetricName` | Which metrics have the most series — the usual cardinality culprits |
| `labelValueCountByLabelName` | Labels with the most unique values (e.g. `id`, `pod`, request IDs) |
| `seriesCountByLabelValuePair` | Which label pair contributes the most series |
| `headStats.numSeries` | Total active series — compare against instance memory |

```bash
# Top 20 metrics by series count
curl -s "http://localhost:9090/api/v1/status/tsdb?limit=20" \
  -H "Authorization: Bearer $TOKEN" | \
  jq -r '.data.seriesCountByMetricName[] | "\(.value)\t\(.name)"'
```

---

## Cardinality via PromQL

These work through Thanos Querier (no port-forward needed) and can be scoped with label selectors:

```bash
# Total active series (per Prometheus replica)
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=prometheus_tsdb_head_series' \
  "$PROM_URL/api/v1/query" | jq '.data.result'

# Top 15 metrics by series count
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=topk(15, count by (__name__)({__name__=~".+"}))' \
  "$PROM_URL/api/v1/query" | \
  jq -r '.data.result[] | "\(.value[1])\t\(.metric.__name__)"'

# Series count for one metric, by namespace
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=count by (namespace) (container_cpu_usage_seconds_total)' \
  "$PROM_URL/api/v1/query" | jq '.data.result'

# Ingestion rate (samples/sec)
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=rate(prometheus_tsdb_head_samples_appended_total[5m])' \
  "$PROM_URL/api/v1/query" | jq '.data.result'

# Series churn — new series created per second
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=rate(prometheus_tsdb_head_series_created_total[5m])' \
  "$PROM_URL/api/v1/query" | jq '.data.result'
```

**Warning:** `count by (__name__)({__name__=~".+"})` touches every series and is expensive on large clusters. Prefer the `/api/v1/status/tsdb` endpoint when possible, and scope with selectors (e.g. `{namespace="x"}`) when not.

---

## Server Status

Build, runtime, and configuration info for a Prometheus instance (direct access, not via Thanos):

```bash
# Version and build info
curl -s -H "Authorization: Bearer $TOKEN" "http://localhost:9090/api/v1/status/buildinfo" | jq '.data'

# Runtime info: storage retention, WAL corruptions, goroutines, last config reload
curl -s -H "Authorization: Bearer $TOKEN" "http://localhost:9090/api/v1/status/runtimeinfo" | jq '.data'

# Active configuration flags (retention, storage path, limits)
curl -s -H "Authorization: Bearer $TOKEN" "http://localhost:9090/api/v1/status/flags" | jq '.data'

# Full loaded prometheus.yml
curl -s -H "Authorization: Bearer $TOKEN" "http://localhost:9090/api/v1/status/config" | jq -r '.data.yaml'
```

Storage health is also exposed as metrics, queryable through Thanos:

```bash
# WAL corruptions, compaction failures, blocked storage
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query={__name__=~"prometheus_tsdb_(wal_corruptions_total|compactions_failed_total|head_truncations_failed_total)"}' \
  "$PROM_URL/api/v1/query" | jq '.data.result'
```

---

## Targets

Scrape target health — which exporters are up, down, or dropped.

```
GET /api/v1/targets
```

| Parameter | Default | Description |
|---|---|---|
| `state` | all | `active`, `dropped`, or `any` |
| `scrapePool` | all | Filter by scrape pool name |

```bash
# Down targets with their last error
curl -sk -G -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'state=active' \
  "$PROM_URL/api/v1/targets" | \
  jq '.data.activeTargets[] | select(.health != "up") | {job: .labels.job, instance: .labels.instance, lastError}'

# Scrape duration outliers
curl -sk -G -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'state=active' \
  "$PROM_URL/api/v1/targets" | \
  jq '.data.activeTargets | sort_by(.lastScrapeDuration) | reverse | .[:10] | .[] | {job: .labels.job, instance: .labels.instance, lastScrapeDuration}'
```
