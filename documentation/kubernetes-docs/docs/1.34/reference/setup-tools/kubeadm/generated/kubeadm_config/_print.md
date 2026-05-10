This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/reference/setup-tools/kubeadm/generated/kubeadm_config/).

#

* 1:
* 2:
* 3:
* 4:
* 5:
* 6:
* 7:
* 8:
* 9:
* 10:

Manage configuration for a kubeadm cluster persisted in a ConfigMap in the cluster

### Synopsis

There is a ConfigMap in the kube-system namespace called "kubeadm-config" that kubeadm uses to store internal configuration about the
cluster. kubeadm CLI v1.8.0+ automatically creates this ConfigMap with the config used with 'kubeadm init', but if you
initialized your cluster using kubeadm v1.7.x or lower, you must use the 'kubeadm init phase upload-config' command to
create this ConfigMap. This is required so that 'kubeadm upgrade' can configure your upgraded cluster correctly.

```
kubeadm config [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for config |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |
