# kubectl port-forward

## Synopsis

Forward one or more local ports to a pod.

Use resource type/name such as deployment/mydeployment to select a pod. Resource type defaults to 'pod' if omitted.

If there are multiple pods matching the criteria, a pod will be selected automatically. The forwarding session ends when the selected pod terminates, and a rerun of the command is needed to resume forwarding.

```
kubectl port-forward TYPE/NAME [options] [LOCAL_PORT:]REMOTE_PORT [...[LOCAL_PORT_N:]REMOTE_PORT_N]
```

## Examples

```
  # Listen on ports 5000 and 6000 locally, forwarding data to/from ports 5000 and 6000 in the pod
  kubectl port-forward pod/mypod 5000 6000

  # Listen on ports 5000 and 6000 locally, forwarding data to/from ports 5000 and 6000 in a pod selected by the deployment
  kubectl port-forward deployment/mydeployment 5000 6000

  # Listen on port 8443 locally, forwarding to the targetPort of the service's port named "https" in a pod selected by the service
  kubectl port-forward service/myservice 8443:https

  # Listen on port 8888 locally, forwarding to 5000 in the pod
  kubectl port-forward pod/mypod 8888:5000

  # Listen on port 8888 on all addresses, forwarding to 5000 in the pod
  kubectl port-forward --address 0.0.0.0 pod/mypod 8888:5000

  # Listen on port 8888 on localhost and selected IP, forwarding to 5000 in the pod
  kubectl port-forward --address localhost,10.19.21.23 pod/mypod 8888:5000

  # Listen on a random port locally, forwarding to 5000 in the pod
  kubectl port-forward pod/mypod :5000
```

## Options

|  |  |
| --- | --- |
| --address strings     Default: "localhost" | |
|  | Addresses to listen on (comma separated). Only accepts IP addresses or localhost as a value. When localhost is supplied, kubectl will try to bind on both 127.0.0.1 and ::1 and will fail if neither of these addresses are available to bind. |
| -h, --help | |
|  | help for port-forward |
| --pod-running-timeout duration     Default: 1m0s | |
|  | The length of time (like 5s, 2m, or 3h, higher than zero) to wait until at least one pod is running |

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
