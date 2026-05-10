# kubeadm reset

Performs a best effort revert of changes made by `kubeadm init` or `kubeadm join`.

### Synopsis

Performs a best effort revert of changes made to this host by 'kubeadm init' or 'kubeadm join'

The "reset" command executes the following phases:

```
preflight           Run reset pre-flight checks
remove-etcd-member  Remove a local etcd member.
cleanup-node        Run cleanup node.
```

```
kubeadm reset [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path to the directory where the certificates are stored. If specified, clean this directory. |
| --cleanup-tmp-dir | |
|  | Cleanup the "/etc/kubernetes/tmp" directory |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --cri-socket string | |
|  | Path to the CRI socket to connect. If empty kubeadm will try to auto-detect this value; use this option only if you have more than one CRI installed or if you have non-standard CRI socket. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -f, --force | |
|  | Reset the node without prompting for confirmation. |
| -h, --help | |
|  | help for reset |
| --ignore-preflight-errors strings | |
|  | A list of checks whose errors will be shown as warnings. Example: 'IsPrivilegedUser,Swap'. Value 'all' ignores errors from all checks. |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --skip-phases strings | |
|  | List of phases to be skipped |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Reset workflow

`kubeadm reset` is responsible for cleaning up a node local file system from files that were created using
the `kubeadm init` or `kubeadm join` commands. For control-plane nodes `reset` also removes the local stacked
etcd member of this node from the etcd cluster.

`kubeadm reset phase` can be used to execute the separate phases of the above workflow.
To skip a list of phases you can use the `--skip-phases` flag, which works in a similar way to
the `kubeadm join` and `kubeadm init` phase runners.

`kubeadm reset` also supports the `--config` flag for passing
a [`ResetConfiguration` structure](/docs/reference/config-api/kubeadm-config.v1beta4/).

### Cleanup of external etcd members

`kubeadm reset` will not delete any etcd data if external etcd is used. This means that if you run `kubeadm init` again using the same etcd endpoints, you will see state from previous clusters.

To wipe etcd data it is recommended you use a client like etcdctl, such as:

```
etcdctl del "" --prefix
```

See the [etcd documentation](https://github.com/coreos/etcd/tree/master/etcdctl) for more information.

### Cleanup of CNI configuration

CNI plugins use the directory `/etc/cni/net.d` to store their configuration.
The `kubeadm reset` command does not cleanup that directory. Leaving the configuration
of a CNI plugin on a host can be problematic if the same host is later used
as a new Kubernetes node and a different CNI plugin happens to be deployed in that cluster.
It can result in a configuration conflict between CNI plugins.

To cleanup the directory, backup its contents if needed and then execute
the following command:

```
sudo rm -rf /etc/cni/net.d
```

### Cleanup of network traffic rules

The `kubeadm reset` command does not clean any iptables, nftables or IPVS rules applied
to the host by kube-proxy. A control loop in kube-proxy ensures that the rules on each node
host are synchronized. For additional details please see
[Virtual IPs and Service Proxies](/docs/reference/networking/virtual-ips/).

Leaving the rules without cleanup should not cause any issues if the host is
later reused as a Kubernetes node or if it will serve a different purpose.

If you wish to perform this cleanup, you can use the same kube-proxy container
which was used in your cluster and the `--cleanup` flag of the
`kube-proxy` binary:

```
docker run --privileged --rm registry.k8s.io/kube-proxy:v1.34.0 sh -c "kube-proxy --cleanup && echo DONE"
```

The output of the above command should print `DONE` at the end.
Instead of Docker, you can use your preferred container runtime to start the container.

### Cleanup of $HOME/.kube

The `$HOME/.kube` directory typically contains configuration files and kubectl cache.
While not cleaning the contents of `$HOME/.kube/cache` is not an issue, there is one important
file in the directory. That is `$HOME/.kube/config` and it is used by kubectl to authenticate
to the Kubernetes API server. After `kubeadm init` finishes, the user is instructed to copy the
`/etc/kubernetes/admin.conf` file to the `$HOME/.kube/config` location and grant the current
user access to it.

The `kubeadm reset` command does not clean any of the contents of the `$HOME/.kube` directory.
Leaving the `$HOME/.kube/config` file without deleting it, can be problematic depending
on who will have access to this host after `kubeadm reset` was called.
If the same cluster continues to exist, it is highly recommended to delete the file,
as the admin credentials stored in it will continue to be valid.

To cleanup the directory, examine its contents, perform backup if needed and execute
the following command:

```
rm -rf $HOME/.kube
```

### Graceful kube-apiserver shutdown

If you have your `kube-apiserver` configured with the `--shutdown-delay-duration` flag,
you can run the following commands to attempt a graceful shutdown for the running API server Pod,
before you run `kubeadm reset`:

```
yq eval -i '.spec.containers[0].command = []' /etc/kubernetes/manifests/kube-apiserver.yaml
timeout 60 sh -c 'while pgrep kube-apiserver >/dev/null; do sleep 1; done' || true
```

## What's next

* [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) to bootstrap a Kubernetes control-plane node
* [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) to bootstrap a Kubernetes worker node and join it to the cluster

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
