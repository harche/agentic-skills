This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/reference/kubectl/generated/kubectl_rollout/).

# kubectl rollout

* 1: [kubectl rollout history](#pg-feee355d0921a2dae193326b4569c1c4)
* 2: [kubectl rollout pause](#pg-a45554a76bb1970815575b0d0eb8eb78)
* 3: [kubectl rollout restart](#pg-dff2e5df7176c0f397625767a6624bf4)
* 4: [kubectl rollout resume](#pg-a2718a937a9d531c87d0c31ba738c112)
* 5: [kubectl rollout status](#pg-5162a0abebfda06de0129978dff33fa3)
* 6: [kubectl rollout undo](#pg-decea050af73d7440fc036efb9ff569f)

## Synopsis

Manage the rollout of one or many resources.

Valid resource types include:

* deployments
* daemonsets
* statefulsets

```
kubectl rollout SUBCOMMAND
```

## Examples

```
  # Rollback to the previous deployment
  kubectl rollout undo deployment/abc

  # Check the rollout status of a daemonset
  kubectl rollout status daemonset/foo

  # Restart a deployment
  kubectl rollout restart deployment/abc

  # Restart deployments with the 'app=nginx' label
  kubectl rollout restart deployment --selector=app=nginx
```

## Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for rollout |

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
* [kubectl rollout history](kubectl_rollout_history/) - View rollout history
* [kubectl rollout pause](kubectl_rollout_pause/) - Mark the provided resource as paused
* [kubectl rollout restart](kubectl_rollout_restart/) - Restart a resource
* [kubectl rollout resume](kubectl_rollout_resume/) - Resume a paused resource
* [kubectl rollout status](kubectl_rollout_status/) - Show the status of the rollout
* [kubectl rollout undo](kubectl_rollout_undo/) - Undo a previous rollout
