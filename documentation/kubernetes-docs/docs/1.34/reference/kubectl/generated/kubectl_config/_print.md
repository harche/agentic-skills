This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/reference/kubectl/generated/kubectl_config/).

# kubectl config

* 1: [kubectl config current-context](#pg-5014b54facef233a63885234ce91c3aa)
* 2: [kubectl config delete-cluster](#pg-aecc079c7de2d3be561601daf1d6684c)
* 3: [kubectl config delete-context](#pg-b5f24b4e3009ebba0a0f4ad35af0d4ab)
* 4: [kubectl config delete-user](#pg-d77b4cbd068f250f86cff5c2e75dabda)
* 5: [kubectl config get-clusters](#pg-1176518e0a720b52609f27e88abef8eb)
* 6: [kubectl config get-contexts](#pg-f96682991dc356384f3888c21b013cd6)
* 7: [kubectl config get-users](#pg-3a4916efcdffdb896b4619a1a5cbd87b)
* 8: [kubectl config rename-context](#pg-4f49ec6f9e1def05f72cfd83d8e26f34)
* 9: [kubectl config set](#pg-fddfa538835c3f9a09666f6713f07278)
* 10: [kubectl config set-cluster](#pg-c6f09b5a087eb07fce8acb3d3db38e22)
* 11: [kubectl config set-context](#pg-2500189be627eaffa4b161af5dd9a178)
* 12: [kubectl config set-credentials](#pg-b3b6ccdb55698e26fcd43bf215002c58)
* 13: [kubectl config unset](#pg-f82900d692231ec20a5fc6465c06e298)
* 14: [kubectl config use-context](#pg-f6ec7b5627422d529c65ee106681fea2)
* 15: [kubectl config view](#pg-3bfacbe2914206676749a842aa0d00f2)

## Synopsis

Modify kubeconfig files using subcommands like "kubectl config set current-context my-context".

The loading order follows these rules:

1. If the --kubeconfig flag is set, then only that file is loaded. The flag may only be set once and no merging takes place.
2. If $KUBECONFIG environment variable is set, then it is used as a list of paths (normal path delimiting rules for your system). These paths are merged. When a value is modified, it is modified in the file that defines the stanza. When a value is created, it is created in the first file that exists. If no files in the chain exist, then it creates the last file in the list.
3. Otherwise, ${HOME}/.kube/config is used and no merging takes place.

```
kubectl config SUBCOMMAND
```

## Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for config |
| --kubeconfig string | |
|  | use a particular kubeconfig file |

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
* [kubectl config current-context](kubectl_config_current-context/) - Display the current-context
* [kubectl config delete-cluster](kubectl_config_delete-cluster/) - Delete the specified cluster from the kubeconfig
* [kubectl config delete-context](kubectl_config_delete-context/) - Delete the specified context from the kubeconfig
* [kubectl config delete-user](kubectl_config_delete-user/) - Delete the specified user from the kubeconfig
* [kubectl config get-clusters](kubectl_config_get-clusters/) - Display clusters defined in the kubeconfig
* [kubectl config get-contexts](kubectl_config_get-contexts/) - Describe one or many contexts
* [kubectl config get-users](kubectl_config_get-users/) - Display users defined in the kubeconfig
* [kubectl config rename-context](kubectl_config_rename-context/) - Rename a context from the kubeconfig file
* [kubectl config set](kubectl_config_set/) - Set an individual value in a kubeconfig file
* [kubectl config set-cluster](kubectl_config_set-cluster/) - Set a cluster entry in kubeconfig
* [kubectl config set-context](kubectl_config_set-context/) - Set a context entry in kubeconfig
* [kubectl config set-credentials](kubectl_config_set-credentials/) - Set a user entry in kubeconfig
* [kubectl config unset](kubectl_config_unset/) - Unset an individual value in a kubeconfig file
* [kubectl config use-context](kubectl_config_use-context/) - Set the current-context in a kubeconfig file
* [kubectl config view](kubectl_config_view/) - Display merged kubeconfig settings or a specified kubeconfig file
