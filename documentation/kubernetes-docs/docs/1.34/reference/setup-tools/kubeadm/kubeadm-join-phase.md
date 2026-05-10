# kubeadm join phase

`kubeadm join phase` enables you to invoke atomic steps of the join process.
Hence, you can let kubeadm do some of the work and you can fill in the gaps
if you wish to apply customization.

`kubeadm join phase` is consistent with the [kubeadm join workflow](/docs/reference/setup-tools/kubeadm/kubeadm-join/#join-workflow),
and behind the scene both use the same code.

## kubeadm join phase

* phase

### Synopsis

Use this command to invoke single phase of the "join" workflow

```
kubeadm join phase [flags]
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

## kubeadm join phase preflight

Using this phase you can execute preflight checks on a joining node.

* preflight

Run join pre-flight checks

### Synopsis

Run pre-flight checks for kubeadm join.

```
kubeadm join phase preflight [api-server-endpoint] [flags]
```

### Examples

```
  # Run join pre-flight checks using a config file.
  kubeadm join phase preflight --config kubeadm-config.yaml
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
| --cri-socket string | |
|  | Path to the CRI socket to connect. If empty kubeadm will try to auto-detect this value; use this option only if you have more than one CRI installed or if you have non-standard CRI socket. |
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
|  | help for preflight |
| --ignore-preflight-errors strings | |
|  | A list of checks whose errors will be shown as warnings. Example: 'IsPrivilegedUser,Swap'. Value 'all' ignores errors from all checks. |
| --node-name string | |
|  | Specify the node name. |
| --tls-bootstrap-token string | |
|  | Specify the token used to temporarily authenticate with the Kubernetes Control Plane while joining the node. |
| --token string | |
|  | Use this token for both discovery-token and tls-bootstrap-token when those values are not provided. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm join phase control-plane-prepare

Using this phase you can prepare a node for serving a control-plane.

* control-plane-prepare
  * all
    * download-certs
      * certs
        * kubeconfig
          * control-plane

### Synopsis

Prepare the machine for serving a control plane

```
kubeadm join phase control-plane-prepare [flags]
```

### Examples

```
  # Prepares the machine for serving a control plane
  kubeadm join phase control-plane-prepare all
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for control-plane-prepare |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

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

### Synopsis

Download certificates shared among control-plane nodes from the kubeadm-certs Secret

```
kubeadm join phase control-plane-prepare download-certs [api-server-endpoint] [flags]
```

### Options

|  |  |
| --- | --- |
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
|  | help for download-certs |
| --tls-bootstrap-token string | |
|  | Specify the token used to temporarily authenticate with the Kubernetes Control Plane while joining the node. |
| --token string | |
|  | Use this token for both discovery-token and tls-bootstrap-token when those values are not provided. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate the certificates for the new control plane components

```
kubeadm join phase control-plane-prepare certs [api-server-endpoint] [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | If the node should host a new control plane instance, the IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
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
|  | help for certs |
| --node-name string | |
|  | Specify the node name. |
| --tls-bootstrap-token string | |
|  | Specify the token used to temporarily authenticate with the Kubernetes Control Plane while joining the node. |
| --token string | |
|  | Use this token for both discovery-token and tls-bootstrap-token when those values are not provided. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate the kubeconfig for the new control plane components

```
kubeadm join phase control-plane-prepare kubeconfig [api-server-endpoint] [flags]
```

### Options

|  |  |
| --- | --- |
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
|  | help for kubeconfig |
| --tls-bootstrap-token string | |
|  | Specify the token used to temporarily authenticate with the Kubernetes Control Plane while joining the node. |
| --token string | |
|  | Use this token for both discovery-token and tls-bootstrap-token when those values are not provided. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate the manifests for the new control plane components

```
kubeadm join phase control-plane-prepare control-plane [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | If the node should host a new control plane instance, the IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-bind-port int32     Default: 6443 | |
|  | If the node should host a new control plane instance, the port for the API Server to bind to. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane | |
|  | Create a new control plane instance on this node |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for control-plane |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm join phase kubelet-start

Using this phase you can write the kubelet settings, certificates and (re)start the kubelet.

* kubelet-start

Write kubelet settings, certificates and (re)start the kubelet

### Synopsis

Write a file with KubeletConfiguration and an environment file with node specific kubelet settings, and then (re)start kubelet.

```
kubeadm join phase kubelet-start [api-server-endpoint] [flags]
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --cri-socket string | |
|  | Path to the CRI socket to connect. If empty kubeadm will try to auto-detect this value; use this option only if you have more than one CRI installed or if you have non-standard CRI socket. |
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
|  | help for kubelet-start |
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

## kubeadm join phase control-plane-join

Using this phase you can join a node as a control-plane instance.

* control-plane-join
  * all
    * etcd
      * mark-control-plane

### Synopsis

Join a machine as a control plane instance

```
kubeadm join phase control-plane-join [flags]
```

### Examples

```
  # Joins a machine as a control plane instance
  kubeadm join phase control-plane-join all
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for control-plane-join |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Join a machine as a control plane instance

```
kubeadm join phase control-plane-join all [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | If the node should host a new control plane instance, the IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane | |
|  | Create a new control plane instance on this node |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for all |
| --node-name string | |
|  | Specify the node name. |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Add a new local etcd member

```
kubeadm join phase control-plane-join etcd [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | If the node should host a new control plane instance, the IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane | |
|  | Create a new control plane instance on this node |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for etcd |
| --node-name string | |
|  | Specify the node name. |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Mark a node as a control-plane

```
kubeadm join phase control-plane-join mark-control-plane [flags]
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane | |
|  | Create a new control plane instance on this node |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for mark-control-plane |
| --node-name string | |
|  | Specify the node name. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## What's next

* [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) to bootstrap a Kubernetes control-plane node
* [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) to connect a node to the cluster
* [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) to revert any changes made to this host by `kubeadm init` or `kubeadm join`
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
