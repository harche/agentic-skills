# kubeadm upgrade phases

## kubeadm upgrade apply phase

Using the phases of `kubeadm upgrade apply`, you can choose to execute the separate steps of the initial upgrade
of a control plane node.

* phase
  * preflight
    * control-plane
      * upload-config
        * kubelet-config
          * bootstrap-token
            * addon
              * post-upgrade

### Synopsis

Use this command to invoke single phase of the "apply" workflow

```
kubeadm upgrade apply phase [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for phase |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Run preflight checks before upgrade

```
kubeadm upgrade apply phase preflight [flags]
```

### Options

|  |  |
| --- | --- |
| --allow-experimental-upgrades | |
|  | Show unstable versions of Kubernetes as an upgrade alternative and allow upgrading to an alpha/beta/release candidate versions of Kubernetes. |
| --allow-release-candidate-upgrades | |
|  | Show release candidate versions of Kubernetes as an upgrade alternative and allow upgrading to a release candidate versions of Kubernetes. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Do not change any state, just output what actions would be performed. |
| -f, --force | |
|  | Force upgrading although some requirements might not be met. This also implies non-interactive mode. |
| -h, --help | |
|  | help for preflight |
| --ignore-preflight-errors strings | |
|  | A list of checks whose errors will be shown as warnings. Example: 'IsPrivilegedUser,Swap'. Value 'all' ignores errors from all checks. |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| -y, --yes | |
|  | Perform the upgrade and do not prompt for confirmation (non-interactive mode). |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Upgrade the control plane

```
kubeadm upgrade apply phase control-plane [flags]
```

### Options

|  |  |
| --- | --- |
| --certificate-renewal     Default: true | |
|  | Perform the renewal of certificates used by component changed during upgrades. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Do not change any state, just output what actions would be performed. |
| --etcd-upgrade     Default: true | |
|  | Perform the upgrade of etcd. |
| -h, --help | |
|  | help for control-plane |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Upload the kubeadm and kubelet configurations to ConfigMaps

```
kubeadm upgrade apply phase upload-config [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for upload-config |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Upgrade the kubelet configuration for this node by downloading it from the kubelet-config ConfigMap stored in the cluster

```
kubeadm upgrade apply phase kubelet-config [flags]
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Do not change any state, just output what actions would be performed. |
| -h, --help | |
|  | help for kubelet-config |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Configures bootstrap token and cluster-info RBAC rules

```
kubeadm upgrade apply phase bootstrap-token [flags]
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Do not change any state, just output what actions would be performed. |
| -h, --help | |
|  | help for bootstrap-token |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Upgrade the default kubeadm addons

```
kubeadm upgrade apply phase addon [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for addon |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Run post upgrade tasks

```
kubeadm upgrade apply phase post-upgrade [flags]
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Do not change any state, just output what actions would be performed. |
| -h, --help | |
|  | help for post-upgrade |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm upgrade node phase

Using the phases of `kubeadm upgrade node` you can choose to execute the separate steps of the upgrade of
secondary control-plane or worker nodes.

* phase
  * preflight
    * control-plane
      * kubelet-config
        * addon
          * post-upgrade

### Synopsis

Use this command to invoke single phase of the "node" workflow

```
kubeadm upgrade node phase [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for phase |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

Run upgrade node pre-flight checks

### Synopsis

Run pre-flight checks for kubeadm upgrade node.

```
kubeadm upgrade node phase preflight [flags]
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for preflight |
| --ignore-preflight-errors strings | |
|  | A list of checks whose errors will be shown as warnings. Example: 'IsPrivilegedUser,Swap'. Value 'all' ignores errors from all checks. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Upgrade the control plane instance deployed on this node, if any

```
kubeadm upgrade node phase control-plane [flags]
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
|  | help for control-plane |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Upgrade the kubelet configuration for this node by downloading it from the kubelet-config ConfigMap stored in the cluster

```
kubeadm upgrade node phase kubelet-config [flags]
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Do not change any state, just output the actions that would be performed. |
| -h, --help | |
|  | help for kubelet-config |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Upgrade the default kubeadm addons

```
kubeadm upgrade node phase addon [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for addon |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Run post upgrade tasks

```
kubeadm upgrade node phase post-upgrade [flags]
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Do not change any state, just output the actions that would be performed. |
| -h, --help | |
|  | help for post-upgrade |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## What's next

* [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) to bootstrap a Kubernetes control-plane node
* [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) to connect a node to the cluster
* [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) to revert any changes made to this host by `kubeadm init` or `kubeadm join`
* [kubeadm upgrade](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/) to upgrade a kubeadm node
* [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha/) to try experimental functionality

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
