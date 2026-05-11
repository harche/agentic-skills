# kubectl

## Synopsis

kubectl controls the Kubernetes cluster manager.

Find more information in [Command line tool](/docs/reference/kubectl/) (`kubectl`).

```
kubectl [flags]
```

## Options

|  |  |
| --- | --- |
| --add-dir-header | |
|  | If true, adds the file directory to the header of the log messages |
| --alsologtostderr | |
|  | log to standard error as well as files |
| --as string | |
|  | Username to impersonate for the operation |
| --as-group stringArray | |
|  | Group to impersonate for the operation, this flag can be repeated to specify multiple groups. |
| --azure-container-registry-config string | |
|  | Path to the file containing Azure container registry configuration information. |
| --cache-dir string     Default: "$HOME/.kube/cache" | |
|  | Default cache directory |
| --certificate-authority string | |
|  | Path to a cert file for the certificate authority |
| --client-certificate string | |
|  | Path to a client certificate file for TLS |
| --client-key string | |
|  | Path to a client key file for TLS |
| --cloud-provider-gce-l7lb-src-cidrs cidrs     Default: 130.211.0.0/22,35.191.0.0/16 | |
|  | CIDRs opened in GCE firewall for L7 LB traffic proxy & health checks |
| --cloud-provider-gce-lb-src-cidrs cidrs     Default: 130.211.0.0/22,209.85.152.0/22,209.85.204.0/22,35.191.0.0/16 | |
|  | CIDRs opened in GCE firewall for L4 LB traffic proxy & health checks |
| --cluster string | |
|  | The name of the kubeconfig cluster to use |
| --context string | |
|  | The name of the kubeconfig context to use |
| --default-not-ready-toleration-seconds int     Default: 300 | |
|  | Indicates the tolerationSeconds of the toleration for notReady:NoExecute that is added by default to every pod that does not already have such a toleration. |
| --default-unreachable-toleration-seconds int     Default: 300 | |
|  | Indicates the tolerationSeconds of the toleration for unreachable:NoExecute that is added by default to every pod that does not already have such a toleration. |
| -h, --help | |
|  | help for kubectl |
| --insecure-skip-tls-verify | |
|  | If true, the server's certificate will not be checked for validity. This will make your HTTPS connections insecure |
| --kubeconfig string | |
|  | Path to the kubeconfig file to use for CLI requests. |
| --log-backtrace-at traceLocation     Default: :0 | |
|  | when logging hits line file:N, emit a stack trace |
| --log-dir string | |
|  | If non-empty, write log files in this directory |
| --log-file string | |
|  | If non-empty, use this log file |
| --log-file-max-size uint     Default: 1800 | |
|  | Defines the maximum size a log file can grow to. Unit is megabytes. If the value is 0, the maximum file size is unlimited. |
| --log-flush-frequency duration     Default: 5s | |
|  | Maximum number of seconds between log flushes |
| --logtostderr     Default: true | |
|  | log to standard error instead of files |
| --match-server-version | |
|  | Require server version to match client version |
| -n, --namespace string | |
|  | If present, the namespace scope for this CLI request |
| --one-output | |
|  | If true, only write logs to their native severity level (vs also writing to each lower severity level) |
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
| --skip-headers | |
|  | If true, avoid header prefixes in the log messages |
| --skip-log-headers | |
|  | If true, avoid headers when opening log files |
| --stderrthreshold severity     Default: 2 | |
|  | logs at or above this threshold go to stderr |
| --tls-server-name string | |
|  | Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used |
| --token string | |
|  | Bearer token for authentication to the API server |
| --user string | |
|  | The name of the kubeconfig user to use |
| --username string | |
|  | Username for basic authentication to the API server |
| -v, --v Level | |
|  | number for the log level verbosity |
| --version version[=true] | |
|  | Print version information and quit |
| --vmodule moduleSpec | |
|  | comma-separated list of pattern=N settings for file-filtered logging |
| --warnings-as-errors | |
|  | Treat warnings received from the server as errors and exit with a non-zero exit code |

## Environment variables

|  |  |
| --- | --- |
| KUBECONFIG | |
|  | Path to the kubectl configuration ("kubeconfig") file. Default: "$HOME/.kube/config" |
| KUBECTL_COMMAND_HEADERS | |
|  | When set to false, turns off extra HTTP headers detailing invoked kubectl command (Kubernetes version v1.22 or later) |
| KUBECTL_EXPLAIN_OPENAPIV3 | |
|  | Toggles whether calls to `kubectl explain` use the new OpenAPIv3 data source available. OpenAPIV3 is enabled by default since Kubernetes 1.24. |
| KUBECTL_ENABLE_CMD_SHADOW | |
|  | When set to true, external plugins can be used as subcommands for builtin commands if subcommand does not exist. In alpha stage, this feature can only be used for create command(e.g. kubectl create networkpolicy). |
| KUBECTL_PORT_FORWARD_WEBSOCKETS | |
|  | When set to true, the kubectl port-forward command will attempt to stream using the websockets protocol. If the upgrade to websockets fails, the commands will fallback to use the current SPDY protocol. |
| KUBECTL_REMOTE_COMMAND_WEBSOCKETS | |
|  | When set to true, the kubectl exec, cp, and attach commands will attempt to stream using the websockets protocol. If the upgrade to websockets fails, the commands will fallback to use the current SPDY protocol. |
| KUBECTL_KUBERC | |
|  | When set to true, kuberc file is taken into account to define user specific preferences. |
| KUBECTL_KYAML | |
|  | When set to true, kubectl is capable of producing Kubernetes-specific dialect of YAML output format. |

## See Also

* [kubectl annotate](/docs/reference/kubectl/generated/kubectl_annotate/) - Update the annotations on a resource
* [kubectl api-resources](/docs/reference/kubectl/generated/kubectl_api-resources/) - Print the supported API resources on the server
* [kubectl api-versions](/docs/reference/kubectl/generated/kubectl_api-versions/) - Print the supported API versions on the server,
  in the form of "group/version"
* [kubectl apply](/docs/reference/kubectl/generated/kubectl_apply/) - Apply a configuration to a resource by filename or stdin
* [kubectl attach](/docs/reference/kubectl/generated/kubectl_attach/) - Attach to a running container
* [kubectl auth](/docs/reference/kubectl/generated/kubectl_auth/) - Inspect authorization
* [kubectl autoscale](/docs/reference/kubectl/generated/kubectl_autoscale/) - Auto-scale a Deployment, ReplicaSet, or ReplicationController
* [kubectl certificate](/docs/reference/kubectl/generated/kubectl_certificate/) - Modify certificate resources.
* [kubectl cluster-info](/docs/reference/kubectl/generated/kubectl_cluster-info/) - Display cluster info
* [kubectl completion](/docs/reference/kubectl/generated/kubectl_completion/) - Output shell completion code for the specified shell (bash or zsh)
* [kubectl config](/docs/reference/kubectl/generated/kubectl_config/) - Modify kubeconfig files
* [kubectl cordon](/docs/reference/kubectl/generated/kubectl_cordon/) - Mark node as unschedulable
* [kubectl cp](/docs/reference/kubectl/generated/kubectl_cp/) - Copy files and directories to and from containers.
* [kubectl create](/docs/reference/kubectl/generated/kubectl_create/) - Create a resource from a file or from stdin.
* [kubectl debug](/docs/reference/kubectl/generated/kubectl_debug/) - Create debugging sessions for troubleshooting workloads and nodes
* [kubectl delete](/docs/reference/kubectl/generated/kubectl_delete/) - Delete resources by filenames,
  stdin, resources and names, or by resources and label selector
* [kubectl describe](/docs/reference/kubectl/generated/kubectl_describe/) - Show details of a specific resource or group of resources
* [kubectl diff](/docs/reference/kubectl/generated/kubectl_diff/) - Diff live version against would-be applied version
* [kubectl drain](/docs/reference/kubectl/generated/kubectl_drain/) - Drain node in preparation for maintenance
* [kubectl edit](/docs/reference/kubectl/generated/kubectl_edit/) - Edit a resource on the server
* [kubectl events](/docs/reference/kubectl/generated/kubectl_events/) - List events
* [kubectl exec](/docs/reference/kubectl/generated/kubectl_exec/) - Execute a command in a container
* [kubectl explain](/docs/reference/kubectl/generated/kubectl_explain/) - Documentation of resources
* [kubectl expose](/docs/reference/kubectl/generated/kubectl_expose/) - Take a replication controller,
  service, deployment or pod and expose it as a new Kubernetes Service
* [kubectl get](/docs/reference/kubectl/generated/kubectl_get/) - Display one or many resources
* [kubectl kustomize](/docs/reference/kubectl/generated/kubectl_kustomize/) - Build a kustomization
  target from a directory or a remote url.
* [kubectl label](/docs/reference/kubectl/generated/kubectl_label/) - Update the labels on a resource
* [kubectl logs](/docs/reference/kubectl/generated/kubectl_logs/) - Print the logs for a container in a pod
* [kubectl options](/docs/reference/kubectl/generated/kubectl_options/) - Print the list of flags inherited by all commands
* [kubectl patch](/docs/reference/kubectl/generated/kubectl_patch/) - Update field(s) of a resource
* [kubectl plugin](/docs/reference/kubectl/generated/kubectl_plugin/) - Provides utilities for interacting with plugins.
* [kubectl port-forward](/docs/reference/kubectl/generated/kubectl_port-forward/) - Forward one or more local ports to a pod
* [kubectl proxy](/docs/reference/kubectl/generated/kubectl_proxy/) - Run a proxy to the Kubernetes API server
* [kubectl replace](/docs/reference/kubectl/generated/kubectl_replace/) - Replace a resource by filename or stdin
* [kubectl rollout](/docs/reference/kubectl/generated/kubectl_rollout/) - Manage the rollout of a resource
* [kubectl run](/docs/reference/kubectl/generated/kubectl_run/) - Run a particular image on the cluster
* [kubectl scale](/docs/reference/kubectl/generated/kubectl_scale/) - Set a new size for a Deployment, ReplicaSet or Replication Controller
* [kubectl set](/docs/reference/kubectl/generated/kubectl_set/) - Set specific features on objects
* [kubectl taint](/docs/reference/kubectl/generated/kubectl_taint/) - Update the taints on one or more nodes
* [kubectl top](/docs/reference/kubectl/generated/kubectl_top/) - Display Resource (CPU/Memory/Storage) usage.
* [kubectl uncordon](/docs/reference/kubectl/generated/kubectl_uncordon/) - Mark node as schedulable
* [kubectl version](/docs/reference/kubectl/generated/kubectl_version/) - Print the client and server version information
* [kubectl wait](/docs/reference/kubectl/generated/kubectl_wait/) - Experimental: Wait for a specific condition on one or many resources.

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
