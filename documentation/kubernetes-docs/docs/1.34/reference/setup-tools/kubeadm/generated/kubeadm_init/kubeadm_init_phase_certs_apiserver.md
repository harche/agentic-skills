#

### Synopsis

Generate the certificate for serving the Kubernetes API, and save them into apiserver.crt and apiserver.key files.

If both files already exist, kubeadm skips the generation step and existing files will be used.

```
kubeadm init phase certs apiserver [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | The IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-cert-extra-sans strings | |
|  | Optional extra Subject Alternative Names (SANs) to use for the API Server serving certificate. Can be both IP addresses and DNS names. |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane-endpoint string | |
|  | Specify a stable IP address or DNS name for the control plane. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for apiserver |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |
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
