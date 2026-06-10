# Rules, Alerts & PromQL Validation Reference

Inspect alerting/recording rules loaded in the cluster, view active alerts, and validate PromQL expressions — all via the HTTP API.

## Table of Contents

1. [Loaded Rules](#loaded-rules)
2. [Active Alerts](#active-alerts)
3. [Validating PromQL](#validating-promql)
4. [Alertmanager](#alertmanager)
5. [What Requires promtool](#what-requires-promtool)

---

## Loaded Rules

List all alerting and recording rules currently loaded, with health and evaluation state.

```
GET /api/v1/rules
```

| Parameter | Default | Description |
|---|---|---|
| `type` | all | `alert` or `record` |
| `rule_name[]` | | Filter by rule name (repeatable) |
| `rule_group[]` | | Filter by group name (repeatable) |
| `file[]` | | Filter by rule file path (repeatable) |

### Examples

```bash
# All alerting rules — name, state, query
curl -sk -G -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'type=alert' \
  "$PROM_URL/api/v1/rules" | \
  jq -r '.data.groups[].rules[] | "\(.state)\t\(.name)"' | sort | uniq -c

# Firing rules only, with their PromQL
curl -sk -G -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'type=alert' \
  "$PROM_URL/api/v1/rules" | \
  jq '.data.groups[].rules[] | select(.state == "firing") | {name, query, duration, labels}'

# Find a specific rule definition
curl -sk -G -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'rule_name[]=KubePodCrashLooping' \
  "$PROM_URL/api/v1/rules" | jq '.data.groups[].rules[]'

# Rules with evaluation errors (unhealthy rules)
curl -sk -H "Authorization: Bearer $TOKEN" \
  "$PROM_URL/api/v1/rules" | \
  jq '.data.groups[].rules[] | select(.health != "ok") | {name, health, lastError}'

# Recording rules
curl -sk -G -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'type=record' \
  "$PROM_URL/api/v1/rules" | jq -r '.data.groups[].rules[].name'
```

---

## Active Alerts

List currently pending/firing alerts as Prometheus sees them.

```
GET /api/v1/alerts
```

### Examples

```bash
# All active alerts — name, state, severity
curl -sk -H "Authorization: Bearer $TOKEN" \
  "$PROM_URL/api/v1/alerts" | \
  jq -r '.data.alerts[] | "\(.state)\t\(.labels.severity // "-")\t\(.labels.alertname)"' | sort | uniq -c | sort -rn

# Firing alerts with full labels and annotations
curl -sk -H "Authorization: Bearer $TOKEN" \
  "$PROM_URL/api/v1/alerts" | \
  jq '.data.alerts[] | select(.state == "firing") | {labels, annotations, activeAt}'

# Alerts for a specific namespace
curl -sk -H "Authorization: Bearer $TOKEN" \
  "$PROM_URL/api/v1/alerts" | \
  jq '.data.alerts[] | select(.labels.namespace == "openshift-etcd")'
```

The `ALERTS` metric is also queryable like any other series, which is useful for alert history:

```bash
# When did this alert fire over the last 24h?
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=ALERTS{alertname="TargetDown"}[24h:5m]' \
  "$PROM_URL/api/v1/query" | jq '.data.result'
```

---

## Validating PromQL

A PromQL expression can be syntax-checked by evaluating it — a parse error returns `status: error` with the parser message, without side effects:

```bash
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=sum(rate(foo[5m]) by (ns)' \
  "$PROM_URL/api/v1/query" | \
  jq -r 'if .status == "success" then "VALID (\(.data.result | length) series)" else "INVALID: \(.error)" end'
```

Distinguish the failure modes:

- **Parse error** (`errorType: bad_data`) — the expression is syntactically invalid.
- **Valid but empty result** (`status: success`, `result: []`) — syntax is fine, but no series match. Check metric names and label selectors via the discovery endpoints (see querying.md).

Prometheus 3.x also exposes `POST /api/v1/format_query` (pretty-printing) and `POST /api/v1/parse_query` (AST) — note these may not be available on Thanos Querier; fall back to the evaluate-to-validate pattern above.

---

## Alertmanager

On OpenShift, Alertmanager has its own route and API (`/api/v2/`):

```bash
AM_HOST=$(oc -n openshift-monitoring get route alertmanager-main -o jsonpath='{.status.ingress[].host}') && \
# Active alerts as Alertmanager sees them (post-silencing, post-grouping)
curl -sk -H "Authorization: Bearer $TOKEN" "https://$AM_HOST/api/v2/alerts" | \
  jq -r '.[] | "\(.status.state)\t\(.labels.alertname)"'

# Current silences
curl -sk -H "Authorization: Bearer $TOKEN" "https://$AM_HOST/api/v2/silences" | \
  jq '.[] | select(.status.state == "active") | {comment, matchers, endsAt}'
```

Use this to answer "why am I not receiving this alert?" — the alert may be silenced or inhibited in Alertmanager even though Prometheus shows it firing.

---

## What Requires promtool

These operations work on local files and have no API equivalent. They are out of scope for in-cluster analysis; mention them only if the user is authoring rules in a repo:

- `promtool check rules <file>` — static validation of rule files before applying
- `promtool test rules <test-file>` — unit-testing rules against synthetic series
- `promtool check config <file>` — validating a prometheus.yml

For rules already deployed to the cluster, the `/api/v1/rules` endpoint's `health` and `lastError` fields (above) provide the equivalent feedback.
