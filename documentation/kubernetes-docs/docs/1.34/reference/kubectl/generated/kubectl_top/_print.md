This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/reference/kubectl/generated/kubectl_top/).

# kubectl top

* 1: [kubectl top node](#pg-24aaff2b409245e171479e8dd8790013)
* 2: [kubectl top pod](#pg-765f5bf8510a311aaa87e1027328a2ef)

## Synopsis

Display resource (CPU/memory) usage.

This command provides a view of recent resource consumption for nodes and pods. It fetches metrics from the Metrics Server, which aggregates this data from the kubelet on each node. The Metrics Server must be installed and running in the cluster for this command to work.

The metrics shown are specifically optimized for Kubernetes autoscaling decisions, such as those made by the Horizontal Pod Autoscaler (HPA) and Vertical Pod Autoscaler (VPA). Because of this, the values may not match those from standard OS tools like 'top', as the metrics are designed to provide a stable signal for autoscalers rather than for pinpoint accuracy.

When to use this command:

* For on-the-fly spot-checks of resource usage (e.g. identify which pods are consuming the most resources at a glance, or get a quick sense of the load on your nodes)
* Understand current resource consumption patterns
* Validate the behavior of your HPA or VPA configurations by seeing the metrics they use for scaling decisions.

It is not intended to be a replacement for full-featured monitoring solutions. Its primary design goal is to provide a low-overhead signal for autoscalers, not to be a perfectly accurate monitoring tool. For high-accuracy reporting, historical analysis, dashboarding, or alerting, you should use a dedicated monitoring solution.

```
kubectl top [flags]
```

## Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for top |

## Parent Options Inherited

|  |  |
| --- | --- |
| --as string | |
|  | Username to impersonate for the operation. User could be a regular user or a service account in a namespace. |
| --as-group strings | |
|  | Group to impersonate for the operation, this flag can be repeated to specify multiple groups. |
| --as-uid string | |
|  | UID to impersonate for the operation. |
| --cache-dir string     Default: "$HOME/.kube/cache" | |
|  | Default cache directory |
| --certificate-authority string | |
|  | Path to a cert file for the certificate authority |
| --client-certificate string | |
|  | Path to a client certificate file for TLS |
| --client-key string | |
|  | Path to a client key file for TLS |
| --cluster string | |
|  | The name of the kubeconfig cluster to use |
| --context string | |
|  | The name of the kubeconfig context to use |
| --disable-compression | |
|  | If true, opt-out of response compression for all requests to the server |
| --insecure-skip-tls-verify | |
|  | If true, the server's certificate will not be checked for validity. This will make your HTTPS connections insecure |
| --kubeconfig string | |
|  | Path to the kubeconfig file to use for CLI requests. |
| --kuberc string | |
|  | Path to the kuberc file to use for preferences. This can be disabled by exporting KUBECTL_KUBERC=false feature gate or turning off the feature KUBERC=off. |
| --match-server-version | |
|  | Require server version to match client version |
| -n, --namespace string | |
|  | If present, the namespace scope for this CLI request |
| --password string | |
|  | Password for basic authentication to the API server |
| --profile string     Default: "none" | |
|  | Name of profile to capture. One of (none|cpu|heap|goroutine|threadcreate|block|mutex) |
| --profile-output string     Default: "profile.pprof" | |
|  | Name of the file to write the profile to |
| --request-timeout string     Default: "0" | |
|  | The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don't timeout requests. |
| -s, --server string | |
|  | The address and port of the Kubernetes API server |
| --storage-driver-buffer-duration duration     Default: 1m0s | |
|  | Writes in the storage driver will be buffered for this duration, and committed to the non memory backends as a single transaction |
| --storage-driver-db string     Default: "cadvisor" | |
|  | database name |
| --storage-driver-host string     Default: "localhost:8086" | |
|  | database host:port |
| --storage-driver-password string     Default: "root" | |
|  | database password |
| --storage-driver-secure | |
|  | use secure connection with database |
| --storage-driver-table string     Default: "stats" | |
|  | table name |
| --storage-driver-user string     Default: "root" | |
|  | database username |
| --tls-server-name string | |
|  | Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used |
| --token string | |
|  | Bearer token for authentication to the API server |
| --user string | |
|  | The name of the kubeconfig user to use |
| --username string | |
|  | Username for basic authentication to the API server |
| --version version[=true] | |
|  | --version, --version=raw prints version information and quits; --version=vX.Y.Z... sets the reported version |
| --warnings-as-errors | |
|  | Treat warnings received from the server as errors and exit with a non-zero exit code |

## See Also

* [kubectl](../kubectl/) - kubectl controls the Kubernetes cluster manager
* [kubectl top node](kubectl_top_node/) - Display resource (CPU/memory) usage of nodes
* [kubectl top pod](kubectl_top_pod/) - Display resource (CPU/memory) usage of pods
