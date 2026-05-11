This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/reference/kubectl/generated/kubectl_create/).

# kubectl create

* 1: [kubectl create clusterrole](#pg-bc9f354d308d4b7b92bd1e2c199dd4d1)
* 2: [kubectl create clusterrolebinding](#pg-b580bc796e16cf5c330344854759b767)
* 3: [kubectl create configmap](#pg-d7a078683e8028884681580d3da9c355)
* 4: [kubectl create cronjob](#pg-8623e760bcd816213276f920925c7c9f)
* 5: [kubectl create deployment](#pg-85938a5e506af5d05edc154a7ba45ee7)
* 6: [kubectl create ingress](#pg-454f37b7a4a10acbcb73ee1faefe7ba6)
* 7: [kubectl create job](#pg-962e637e4ac9ca350d8717c056c77268)
* 8: [kubectl create namespace](#pg-8b99d360d189a763d8828d8dad70db8a)
* 9: [kubectl create poddisruptionbudget](#pg-1e27a1c88d08b9addd57196b0559c087)
* 10: [kubectl create priorityclass](#pg-ba25e70aa569d978cd2bec9f32ce0dba)
* 11: [kubectl create quota](#pg-e28159f2e6cb8aa3120d1e88a2e3e404)
* 12: [kubectl create role](#pg-01fc591ca5a786b8d3ed390ef6b72ad5)
* 13: [kubectl create rolebinding](#pg-df4b1aa40a6f6a6f8645261cacb35972)
* 14: [kubectl create secret](#pg-de61418fe2b7a032a7336d6c27fb27be)
* 15: [kubectl create secret docker-registry](#pg-76970ddfe96bc2cf910756946387250e)
* 16: [kubectl create secret generic](#pg-68b32a259fda3582817081388caa0330)
* 17: [kubectl create secret tls](#pg-4033b20aaa417f9e2081d96419a6ee45)
* 18: [kubectl create service](#pg-e0cf2bf7674d167398f315e6a67e1379)
* 19: [kubectl create service clusterip](#pg-8b94cb3a05077a406591bf6b1886edc2)
* 20: [kubectl create service externalname](#pg-d5f597b1de53f09bf2bea1855a981247)
* 21: [kubectl create service loadbalancer](#pg-a1edd453dd57d18385eb35c8e33431a4)
* 22: [kubectl create service nodeport](#pg-a0df1e98366de5c5261e1414770c68f9)
* 23: [kubectl create serviceaccount](#pg-811bd5ff9c057c6c3e7755acabbc824a)
* 24: [kubectl create token](#pg-ee534c7541a0919bdd14e6411d8067b8)

## Synopsis

Create a resource from a file or from stdin.

JSON and YAML formats are accepted.

```
kubectl create -f FILENAME
```

## Examples

```
  # Create a pod using the data in pod.json
  kubectl create -f ./pod.json

  # Create a pod based on the JSON passed into stdin
  cat pod.json | kubectl create -f -

  # Edit the data in registry.yaml in JSON then create the resource using the edited data
  kubectl create -f registry.yaml --edit -o json
```

## Options

|  |  |
| --- | --- |
| --allow-missing-template-keys     Default: true | |
|  | If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats. |
| --dry-run string[="unchanged"]     Default: "none" | |
|  | Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource. |
| --edit | |
|  | Edit the API resource before creating |
| --field-manager string     Default: "kubectl-create" | |
|  | Name of the manager used to track field ownership. |
| -f, --filename strings | |
|  | Filename, directory, or URL to files to use to create the resource |
| -h, --help | |
|  | help for create |
| -k, --kustomize string | |
|  | Process the kustomization directory. This flag can't be used together with -f or -R. |
| -o, --output string | |
|  | Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file). |
| --raw string | |
|  | Raw URI to POST to the server. Uses the transport specified by the kubeconfig file. |
| -R, --recursive | |
|  | Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory. |
| --save-config | |
|  | If true, the configuration of current object will be saved in its annotation. Otherwise, the annotation will be unchanged. This flag is useful when you want to perform kubectl apply on this object in the future. |
| -l, --selector string | |
|  | Selector (label query) to filter on, supports '=', '==', '!=', 'in', 'notin'.(e.g. -l key1=value1,key2=value2,key3 in (value3)). Matching objects must satisfy all of the specified label constraints. |
| --show-managed-fields | |
|  | If true, keep the managedFields when printing objects in JSON or YAML format. |
| --template string | |
|  | Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview]. |
| --validate string[="strict"]     Default: "strict" | |
|  | Must be one of: strict (or true), warn, ignore (or false). "true" or "strict" will use a schema to validate the input and fail the request if invalid. It will perform server side validation if ServerSideFieldValidation is enabled on the api-server, but will fall back to less reliable client-side validation if not. "warn" will warn about unknown or duplicate fields without blocking the request if server-side field validation is enabled on the API server, and behave as "ignore" otherwise. "false" or "ignore" will not perform any schema validation, silently dropping any unknown or duplicate fields. |
| --windows-line-endings | |
|  | Only relevant if --edit=true. Defaults to the line ending native to your platform. |

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
* [kubectl create clusterrole](kubectl_create_clusterrole/) - Create a cluster role
* [kubectl create clusterrolebinding](kubectl_create_clusterrolebinding/) - Create a cluster role binding for a particular cluster role
* [kubectl create configmap](kubectl_create_configmap/) - Create a config map from a local file, directory or literal value
* [kubectl create cronjob](kubectl_create_cronjob/) - Create a cron job with the specified name
* [kubectl create deployment](kubectl_create_deployment/) - Create a deployment with the specified name
* [kubectl create ingress](kubectl_create_ingress/) - Create an ingress with the specified name
* [kubectl create job](kubectl_create_job/) - Create a job with the specified name
* [kubectl create namespace](kubectl_create_namespace/) - Create a namespace with the specified name
* [kubectl create poddisruptionbudget](kubectl_create_poddisruptionbudget/) - Create a pod disruption budget with the specified name
* [kubectl create priorityclass](kubectl_create_priorityclass/) - Create a priority class with the specified name
* [kubectl create quota](kubectl_create_quota/) - Create a quota with the specified name
* [kubectl create role](kubectl_create_role/) - Create a role with single rule
* [kubectl create rolebinding](kubectl_create_rolebinding/) - Create a role binding for a particular role or cluster role
* [kubectl create secret](kubectl_create_secret/) - Create a secret using a specified subcommand
* [kubectl create service](kubectl_create_service/) - Create a service using a specified subcommand
* [kubectl create serviceaccount](kubectl_create_serviceaccount/) - Create a service account with the specified name
* [kubectl create token](kubectl_create_token/) - Request a service account token
