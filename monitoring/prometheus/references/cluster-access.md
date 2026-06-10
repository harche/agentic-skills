# Cluster Access Reference

How to discover, authenticate to, and connect to Prometheus on Kubernetes and OpenShift clusters with `curl`.

## Table of Contents

1. [OpenShift Clusters](#openshift-clusters)
2. [Kubernetes Clusters](#kubernetes-clusters)
3. [Authentication Patterns](#authentication-patterns)
4. [Troubleshooting](#troubleshooting)

---

## OpenShift Clusters

OpenShift ships a managed monitoring stack with Prometheus behind a Thanos Querier front-end.

### Discover the Thanos Querier Endpoint

**From inside a cluster pod** (preferred when cluster DNS works):
```bash
PROM_URL="https://thanos-querier.openshift-monitoring.svc:9091"
```

**Via the external route:**
```bash
# List monitoring routes
oc get route -n openshift-monitoring

# Extract the Thanos Querier host
HOST=$(oc -n openshift-monitoring get route thanos-querier -o jsonpath='{.status.ingress[].host}')
PROM_URL="https://$HOST"
```

### Get Bearer Token

**Inside a pod — use the mounted SA token first:**
```bash
TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token 2>/dev/null || true)
```

**Current user token (outside a pod):**
```bash
TOKEN=$(oc whoami -t 2>/dev/null)
```

If this returns empty, the kubeconfig uses client certificate auth instead of a session token. Create a service account token:

**Service account token (for client cert kubeconfigs or automation):**
```bash
oc -n openshift-monitoring create sa prometheus-reader 2>/dev/null
oc adm policy add-cluster-role-to-user cluster-monitoring-view -z prometheus-reader -n openshift-monitoring 2>/dev/null

# OCP 4.11+ / Kubernetes 1.24+ (TokenRequest API)
TOKEN=$(oc create token prometheus-reader -n openshift-monitoring --duration=1h)
```

### Verify Connection

```bash
curl -sk -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'query=up' \
  "$PROM_URL/api/v1/query" | jq '.status'
```

Expect `"success"`. Do **not** probe `/-/healthy` or `/-/ready` — Thanos Querier returns 503 on those.

### Required RBAC

The requesting account needs the `cluster-monitoring-view` cluster role. Current user (`oc whoami -t`) typically has this if they have cluster-reader or admin access.

---

## Kubernetes Clusters

Prometheus on vanilla Kubernetes is typically installed via kube-prometheus-stack (Helm) or the Prometheus Operator.

### Discover Prometheus

```bash
# Search for Prometheus services across all namespaces
kubectl get svc -A | grep -iE 'prometheus|thanos'

# Common namespaces
kubectl get svc -n monitoring
kubectl get svc -n prometheus
kubectl get svc -n kube-prometheus-stack
kubectl get svc -n observability

# Check for Prometheus CRDs (operator-based installs)
kubectl get prometheus -A 2>/dev/null
```

Common service names (varies by Helm release):

| Component | Typical Service Name | Port |
|---|---|---|
| Prometheus | `prometheus-kube-prometheus-prometheus` | 9090 |
| Alertmanager | `prometheus-kube-prometheus-alertmanager` | 9093 |
| Thanos Sidecar | `prometheus-kube-prometheus-thanos-discovery` | 10901 |

### Port-Forward

```bash
# Port-forward to the Prometheus service
PROM_NS="monitoring"  # adjust to actual namespace
PROM_SVC="prometheus-kube-prometheus-prometheus"  # adjust to actual service name

kubectl port-forward -n "$PROM_NS" "svc/$PROM_SVC" 9090:9090 &
PF_PID=$!
sleep 2  # wait for port-forward to establish

PROM_URL="http://localhost:9090"
```

If the service name isn't obvious, find the pod by label:
```bash
kubectl port-forward -n "$PROM_NS" \
  $(kubectl get pods -n "$PROM_NS" -l app.kubernetes.io/name=prometheus -o jsonpath='{.items[0].metadata.name}') \
  9090:9090 &
PF_PID=$!
```

### Verify and Clean Up

Port-forwarded connections usually don't require auth:

```bash
# Verify
curl -s --data-urlencode 'query=up' "$PROM_URL/api/v1/query" | jq '.status'

# When done
kill $PF_PID 2>/dev/null
```

If auth is required, extract the token from kubeconfig (see below) and add the `Authorization` header.

---

## Authentication Patterns

### Curl Auth Flags

| Scenario | Flags |
|---|---|
| Bearer token (most common for K8s/OCP) | `-H "Authorization: Bearer $TOKEN"` |
| Basic auth | `-u 'username:password'` |
| TLS client certificates (mTLS) | `--cert /path/to/client.crt --key /path/to/client.key` |
| Custom CA | `--cacert /path/to/ca.crt` |
| Skip TLS verification (last resort) | `-k` |

Prefer `--cacert` over `-k` when a CA bundle is available. Inside an OpenShift pod, the service CA for in-cluster endpoints is typically at `/var/run/secrets/kubernetes.io/serviceaccount/service-ca.crt` (if mounted) — fall back to `-k` for route endpoints with cluster-default certs.

### Token Extraction from Kubeconfig

```bash
# Direct token in kubeconfig
kubectl config view --minify --raw -o jsonpath='{.users[0].user.token}'

# OpenShift
oc whoami -t

# Create a short-lived token (K8s 1.24+)
kubectl create token <service-account> -n <namespace> --duration=1h
```

---

## Troubleshooting

### "connection refused" on port-forward
The port-forward process may have died. Check `jobs` and restart it.

### "401 Unauthorized" on OpenShift route
Token may have expired. Refresh with `oc whoami -t` (requires `oc login` session) or create a new SA token.

### "certificate signed by unknown authority"
Use `-k`, or provide the CA cert via `--cacert`.

### 503 from Thanos on `/-/healthy` or `/-/ready`
Expected — Thanos Querier doesn't implement Prometheus's health endpoints. Use a `query=up` request to verify connectivity.

### "could not find Prometheus service"
Try broader searches:
```bash
kubectl get svc -A | grep -iE '9090|prom|thanos|monitor'
kubectl get pods -A | grep -iE 'prom|thanos'
```

### In-cluster service unreachable from the pod
Some sandboxed pods use external DNS and cannot resolve `*.svc` names. Fall back to the external route discovered via `oc get route -n openshift-monitoring thanos-querier`.
