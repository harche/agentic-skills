# kubectl create

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

This page is automatically generated.

If you plan to report an issue with this page, mention that the page is auto-generated in your issue description. The fix may need to happen elsewhere in the Kubernetes project.

## Feedback

Was this page helpful?

Yes
No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on
[Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes).
Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to
[report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io)
or
[suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

const yes = document.querySelector('.feedback--yes');
const no = document.querySelector('.feedback--no');
document.querySelectorAll('.feedback--link').forEach(link => {
link.href = link.href + window.location.pathname;
});
const sendFeedback = (value) => {
if (!gtag) { console.log('!gtag'); }
gtag('event', 'click', {
'event_category': 'Helpful',
'event_label': window.location.pathname,
value
});
};
const disableButtons = () => {
yes.disabled = true;
yes.classList.add('feedback--button__disabled');
no.disabled = true;
no.classList.add('feedback--button__disabled');
};
yes.addEventListener('click', () => {
sendFeedback(1);
disableButtons();
document.querySelector('.feedback--response').classList.remove('feedback--response__hidden');
});
no.addEventListener('click', () => {
sendFeedback(0);
disableButtons();
document.querySelector('.feedback--response').classList.remove('feedback--response__hidden');
});

Last modified April 23, 2026 at 2:12 AM PST: [Merge pull request #55450 from sayanchowdhury/update-release-1.34-hugo.toml (d1f313a)](https://github.com/kubernetes/website/commit/d1f313a65f45bd4882d05fe9b6bea162fa2fdc16)
