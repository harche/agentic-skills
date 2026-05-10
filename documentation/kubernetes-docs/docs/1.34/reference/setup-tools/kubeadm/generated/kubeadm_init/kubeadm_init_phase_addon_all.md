#

### Synopsis

Install all the addons

```
kubeadm init phase addon all [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | The IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-bind-port int32     Default: 6443 | |
|  | Port for the API Server to bind to. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane-endpoint string | |
|  | Specify a stable IP address or DNS name for the control plane. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| --feature-gates string | |
|  | A set of key=value pairs that describe feature gates for various features. Options are: ControlPlaneKubeletLocalMode=true|false (BETA - default=true) NodeLocalCRISocket=true|false (BETA - default=true) PublicKeysECDSA=true|false (DEPRECATED - default=false) RootlessControlPlane=true|false (ALPHA - default=false) WaitForAllControlPlaneComponents=true|false (default=true) |
| -h, --help | |
|  | help for all |
| --image-repository string     Default: "registry.k8s.io" | |
|  | Choose a container registry to pull control plane images from |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |
| --pod-network-cidr string | |
|  | Specify range of IP addresses for the pod network. If set, the control plane will automatically allocate CIDRs for every node. |
| --service-cidr string     Default: "10.96.0.0/12" | |
|  | Use alternative range of IP address for service VIPs. |
| --service-dns-domain string     Default: "cluster.local" | |
|  | Use alternative domain for services, e.g. "myorg.internal". |

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
