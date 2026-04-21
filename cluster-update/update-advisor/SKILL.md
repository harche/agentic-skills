---
name: cluster-update-advisor
description: Assess OpenShift cluster update (upgrade) readiness and risk. Use when evaluating whether a cluster is safe to update, when an update is available, or when the user asks about update risks, prerequisites, blockers, or best practices.
---

# Cluster Update Advisor

## 1. Purpose

Assess cluster update readiness and produce a structured risk report with
actionable prerequisites, blockers, and recommendations.

The proposal request includes pre-collected cluster readiness data (JSON)
gathered by the Cluster Version Operator. Analyze this data, classify findings,
and produce a decision with evidence. Do not re-collect cluster data — it is
already in the request.

## 2. Inputs

The proposal request contains:
- Current and target version metadata
- Channel and update path information
- **Cluster readiness JSON** — cluster health checks with context relevant to preparing for the update

The readiness JSON is embedded in the request between ` ```json ` markers under
the "Cluster Readiness Data" heading. Parse it to begin analysis.

**Readiness JSON structure:**

```json
{
  "current_version": "4.21.5",
  "target_version": "4.21.8",
  "checks": {
    "cluster_conditions":    { "_status": "ok", "summary": {...}, ... },
    "operator_health":       { "_status": "ok", "summary": {...}, ... },
    "api_deprecations":      { "_status": "ok", "summary": {...}, ... },
    "node_capacity":         { "_status": "ok", "summary": {...}, ... },
    "pdb_drain":             { "_status": "ok", "summary": {...}, ... },
    "etcd_health":           { "_status": "ok", "summary": {...}, ... },
    "network":               { "_status": "ok", "summary": {...}, ... },
    "crd_compat":            { "_status": "ok", "summary": {...}, ... },
    "olm_operator_lifecycle": { "_status": "ok", "summary": {...}, ... }
  }
}
```

Each check contains `_status` (`ok` or `error`) and check-specific data
with a `summary` section for quick parsing.

## 3. Decision Policy

### 3.1 Workflow

```
Step 1: Parse readiness data
  Extract the JSON from the proposal request. Count checks
  with _status "ok" vs "error" for completeness.
                       │
Step 2: Verify data completeness
  Any check with _status "error" represents a gap in
  visibility. Note incomplete areas — they reduce confidence.
                       │
Step 3: Evaluate findings
  If the system prompt includes organization-specific policy
  (thresholds, scheduling preferences, risk tolerance), apply
  those constraints. Otherwise use sensible defaults.
  Walk through each check's summary and detail data:
  - Compare numeric thresholds (node headroom, etcd backup age)
  - Evaluate conditional update risks against cluster state
  - Identify compounding risks (e.g., paused MCP + cert expiry)
  - Estimate update duration (~10 min/node)
                       │
Step 4: Classify and decide
  Assign each finding a severity per the classification table
  in section 4.2. Then determine the overall assessment:
    recommend — all checks pass within acceptable thresholds
    caution   — findings exist but manageable with prerequisites
    block     — findings must be resolved before update
    escalate  — insufficient data for confident assessment
                       │
Step 5: Investigate (as needed)
  Use prometheus, platform-docs, redhat-support, or
  product-lifecycle skills for deeper analysis.
                       │
                       ▼
               Produce structured risk report
```

### 3.2 Blocker Classification

| Severity | Criteria | Action |
|---|---|---|
| **Blocker** | Update will fail or cause data loss | `decision: block` |
| **Warning** | Update may cause disruption | `decision: caution` |
| **Info** | Noteworthy but non-blocking | Include for awareness |

Classification rules:

| Check | Blocker if... | Warning if... |
|---|---|---|
| Cluster conditions | Upgradeable=False (non-z-stream) | Update already in progress |
| API deprecations | Workloads use APIs **removed** in target | Workloads use **deprecated** APIs |
| Operator health | Any operator has Upgradeable=False | Any operator is Degraded=True |
| MachineConfigPool | Any MCP paused or degraded | MCP updating or not all machines ready |
| Node capacity | Headroom < 20% | Headroom < 40% |
| PDB config | PDB blocks ALL replicas from draining | PDB has maxUnavailable: 0 |
| etcd health | Any member unhealthy | No recent backup (within 24h) |
| Network plugin | SDN in use and target requires OVN (4.17+) | Using deprecated SDN (< 4.17) |
| CRD compatibility | Stored version not served; operator maxOpenShiftVersion < target | Deprecated versions still served |
| OLM operator lifecycle | Installed operator incompatible with target OCP; operator product EOL | Operator has pending update; operator product in Maintenance Support |

### 3.3 Decision Matrix

| Blockers | Warnings | Decision |
|---|---|---|
| 0 | 0 | `recommend` |
| 0 | 1+ | `caution` |
| 1+ | any | `block` |
| Unable to assess | any | `escalate` |

### 3.4 Output

The output schema is enforced by the OlsAgent CR's `outputSchema` field —
the operator handles structured output compliance via the LLM API.

## 4. Failure Modes — What NOT to Do

1. **Never recommend updating without analyzing the readiness data.** The JSON
   in the request is the source of truth.

2. **Never dismiss conditional update risks.** If the update path is conditional,
   evaluate each risk against the cluster.

3. **Never skip the API deprecation check.** Workloads using removed APIs will
   break after the update.

4. **Never assume etcd is healthy.** Always check member health in the readiness data.

5. **Never fabricate Jira issue keys, KB article IDs, or CVE numbers.** Use the
   `redhat-support` skill to get real data.

6. **Never recommend skipping an update version** unless the readiness data shows
   that path exists.

7. **Never recommend force-updating.** If the standard path is blocked, report it.

## 5. Using Other Skills

- **`openshift-docs`** — Read official OpenShift update docs for version-specific
  procedures and breaking changes.

- **`prometheus`** — Query cluster metrics for trend analysis (etcd latency,
  CPU headroom, firing alerts).

- **`jira`** — Search Red Hat Jira for bugs and known issues affecting the target version.

- **`product-lifecycle`** — Query Red Hat Product Life Cycle API to check
  support status and OCP compatibility for installed operators. Use the operator's
  `package` name from OLM readiness data to look up entries via the `package`
  field (exact match). Flag operators whose product version is End of life or whose
  `openshift_compatibility` does not include the target OCP version.
