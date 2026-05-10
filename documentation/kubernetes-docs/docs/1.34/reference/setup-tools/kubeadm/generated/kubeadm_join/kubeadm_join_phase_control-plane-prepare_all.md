#

### Synopsis

Prepare the machine for serving a control plane

```
kubeadm join phase control-plane-prepare all [api-server-endpoint] [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | If the node should host a new control plane instance, the IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-bind-port int32     Default: 6443 | |
|  | If the node should host a new control plane instance, the port for the API Server to bind to. |
| --certificate-key string | |
|  | Use this key to decrypt the certificate secrets uploaded by init. The certificate key is a hex encoded string that is an AES key of size 32 bytes. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane | |
|  | Create a new control plane instance on this node |
| --discovery-file string | |
|  | For file-based discovery, a file or URL from which to load cluster information. |
| --discovery-token string | |
|  | For token-based discovery, the token used to validate cluster information fetched from the API server. |
| --discovery-token-ca-cert-hash strings | |
|  | For token-based discovery, validate that the root CA public key matches this hash (format: "<type>:<value>"). |
| --discovery-token-unsafe-skip-ca-verification | |
|  | For token-based discovery, allow joining without --discovery-token-ca-cert-hash pinning. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for all |
| --node-name string | |
|  | Specify the node name. |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |
| --tls-bootstrap-token string | |
|  | Specify the token used to temporarily authenticate with the Kubernetes Control Plane while joining the node. |
| --token string | |
|  | Use this token for both discovery-token and tls-bootstrap-token when those values are not provided. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

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
