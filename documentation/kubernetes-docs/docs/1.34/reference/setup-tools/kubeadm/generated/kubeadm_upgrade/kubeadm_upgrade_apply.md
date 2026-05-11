#

### Synopsis

Upgrade your Kubernetes cluster to the specified version

The "apply [version]" command executes the following phases:

```
preflight        Run preflight checks before upgrade
control-plane    Upgrade the control plane
upload-config    Upload the kubeadm and kubelet configurations to ConfigMaps
  /kubeadm         Upload the kubeadm ClusterConfiguration to a ConfigMap
  /kubelet         Upload the kubelet configuration to a ConfigMap
kubelet-config   Upgrade the kubelet configuration for this node
bootstrap-token  Configures bootstrap token and cluster-info RBAC rules
addon            Upgrade the default kubeadm addons
  /coredns         Upgrade the CoreDNS addon
  /kube-proxy      Upgrade the kube-proxy addon
post-upgrade     Run post upgrade tasks
```

```
kubeadm upgrade apply [version]
```

### Options

|  |  |
| --- | --- |
| --allow-experimental-upgrades | |
|  | Show unstable versions of Kubernetes as an upgrade alternative and allow upgrading to an alpha/beta/release candidate versions of Kubernetes. |
| --allow-release-candidate-upgrades | |
|  | Show release candidate versions of Kubernetes as an upgrade alternative and allow upgrading to a release candidate versions of Kubernetes. |
| --certificate-renewal     Default: true | |
|  | Perform the renewal of certificates used by component changed during upgrades. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Do not change any state, just output what actions would be performed. |
| --etcd-upgrade     Default: true | |
|  | Perform the upgrade of etcd. |
| -f, --force | |
|  | Force upgrading although some requirements might not be met. This also implies non-interactive mode. |
| -h, --help | |
|  | help for apply |
| --ignore-preflight-errors strings | |
|  | A list of checks whose errors will be shown as warnings. Example: 'IsPrivilegedUser,Swap'. Value 'all' ignores errors from all checks. |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |
| --print-config | |
|  | Specifies whether the configuration file that will be used in the upgrade should be printed or not. |
| --skip-phases strings | |
|  | List of phases to be skipped |
| -y, --yes | |
|  | Perform the upgrade and do not prompt for confirmation (non-interactive mode). |

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
