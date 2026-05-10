# kubeadm upgrade

`kubeadm upgrade` is a user-friendly command that wraps complex upgrading logic
behind one command, with support for both planning an upgrade and actually performing it.

## kubeadm upgrade guidance

The steps for performing an upgrade using kubeadm are outlined in [this document](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/).
For older versions of kubeadm, please refer to older documentation sets of the Kubernetes website.

You can use `kubeadm upgrade diff` to see the changes that would be applied to static pod manifests.

In Kubernetes v1.15.0 and later, `kubeadm upgrade apply` and `kubeadm upgrade node` will also
automatically renew the kubeadm managed certificates on this node, including those stored in kubeconfig files.
To opt-out, it is possible to pass the flag `--certificate-renewal=false`. For more details about certificate
renewal see the [certificate management documentation](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/).

> **Note:**
> The commands `kubeadm upgrade apply` and `kubeadm upgrade plan` have a legacy `--config`
> flag which makes it possible to reconfigure the cluster, while performing planning or upgrade of that particular
> control-plane node. Please be aware that the upgrade workflow was not designed for this scenario and there are
> reports of unexpected results.

## kubeadm upgrade plan

### Synopsis

Check which versions are available to upgrade to and validate whether your current cluster is upgradeable. This command can only run on the control plane nodes where the kubeconfig file "admin.conf" exists. To skip the internet check, pass in the optional [version] parameter.

```
kubeadm upgrade plan [version] [flags]
```

### Options

|  |  |
| --- | --- |
| --allow-experimental-upgrades | |
|  | Show unstable versions of Kubernetes as an upgrade alternative and allow upgrading to an alpha/beta/release candidate versions of Kubernetes. |
| --allow-missing-template-keys     Default: true | |
|  | If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats. |
| --allow-release-candidate-upgrades | |
|  | Show release candidate versions of Kubernetes as an upgrade alternative and allow upgrading to a release candidate versions of Kubernetes. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --etcd-upgrade     Default: true | |
|  | Perform the upgrade of etcd. |
| -h, --help | |
|  | help for plan |
| --ignore-preflight-errors strings | |
|  | A list of checks whose errors will be shown as warnings. Example: 'IsPrivilegedUser,Swap'. Value 'all' ignores errors from all checks. |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| -o, --output string     Default: "text" | |
|  | Output format. One of: text|json|yaml|go-template|go-template-file|template|templatefile|jsonpath|jsonpath-as-json|jsonpath-file. |
| --print-config | |
|  | Specifies whether the configuration file that will be used in the upgrade should be printed or not. |
| --show-managed-fields | |
|  | If true, keep the managedFields when printing objects in JSON or YAML format. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm upgrade apply

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

## kubeadm upgrade diff

### Synopsis

Show what differences would be applied to existing static pod manifests. See also: kubeadm upgrade apply --dry-run

```
kubeadm upgrade diff [version] [flags]
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -c, --context-lines int     Default: 3 | |
|  | How many lines of context in the diff |
| -h, --help | |
|  | help for diff |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm upgrade node

### Synopsis

Upgrade commands for a node in the cluster

The "node" command executes the following phases:

```
preflight       Run upgrade node pre-flight checks
control-plane   Upgrade the control plane instance deployed on this node, if any
kubelet-config  Upgrade the kubelet configuration for this node
addon           Upgrade the default kubeadm addons
  /coredns        Upgrade the CoreDNS addon
  /kube-proxy     Upgrade the kube-proxy addon
post-upgrade    Run post upgrade tasks
```

```
kubeadm upgrade node [flags]
```

### Options

|  |  |
| --- | --- |
| --certificate-renewal     Default: true | |
|  | Perform the renewal of certificates used by component changed during upgrades. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Do not change any state, just output the actions that would be performed. |
| --etcd-upgrade     Default: true | |
|  | Perform the upgrade of etcd. |
| -h, --help | |
|  | help for node |
| --ignore-preflight-errors strings | |
|  | A list of checks whose errors will be shown as warnings. Example: 'IsPrivilegedUser,Swap'. Value 'all' ignores errors from all checks. |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |
| --skip-phases strings | |
|  | List of phases to be skipped |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## What's next

* [kubeadm config](/docs/reference/setup-tools/kubeadm/kubeadm-config/) if you initialized your cluster using kubeadm v1.7.x or lower, to configure your cluster for `kubeadm upgrade`

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
