# Upgrading kubeadm clusters

This page explains how to upgrade a Kubernetes cluster created with kubeadm from version
1.33.x to version 1.34.x, and from version
1.34.x to 1.34.y (where `y > x`). Skipping MINOR versions
when upgrading is unsupported. For more details, please visit [Version Skew Policy](/releases/version-skew-policy/).

To see information about upgrading clusters created using older versions of kubeadm,
please refer to following pages instead:

* [Upgrading a kubeadm cluster from 1.32 to 1.33](https://v1-33.docs.kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
* [Upgrading a kubeadm cluster from 1.31 to 1.32](https://v1-32.docs.kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
* [Upgrading a kubeadm cluster from 1.30 to 1.31](https://v1-31.docs.kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
* [Upgrading a kubeadm cluster from 1.29 to 1.30](https://v1-30.docs.kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)

The Kubernetes project recommends upgrading to the latest patch releases promptly, and
to ensure that you are running a supported minor release of Kubernetes.
Following this recommendation helps you to stay secure.

The upgrade workflow at high level is the following:

1. Upgrade a primary control plane node.
2. Upgrade additional control plane nodes.
3. Upgrade worker nodes.

## Before you begin

* Make sure you read the [release notes](https://git.k8s.io/kubernetes/CHANGELOG) carefully.
* The cluster should use a static control plane and etcd pods or external etcd.
* Make sure to back up any important components, such as app-level state stored in a database.
  `kubeadm upgrade` does not touch your workloads, only components internal to Kubernetes, but backups are always a best practice.
* [Swap must be disabled](https://serverfault.com/questions/684771/best-way-to-disable-swap-in-linux).

### Additional information

* The instructions below outline when to drain each node during the upgrade process.
  If you are performing a **minor** version upgrade for any kubelet, you **must**
  first drain the node (or nodes) that you are upgrading. In the case of control plane nodes,
  they could be running CoreDNS Pods or other critical workloads. For more information see
  [Draining nodes](/docs/tasks/administer-cluster/safely-drain-node/).
* The Kubernetes project recommends that you match your kubelet and kubeadm versions.
  You can instead use a version of kubelet that is older than kubeadm, provided it is within the
  range of supported versions.
  For more details, please visit [kubeadm's skew against the kubelet](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#kubeadm-s-skew-against-the-kubelet).
* All containers are restarted after upgrade, because the container spec hash value is changed.
* To verify that the kubelet service has successfully restarted after the kubelet has been upgraded,
  you can execute `systemctl status kubelet` or view the service logs with `journalctl -xeu kubelet`.
* `kubeadm upgrade` supports `--config` with a
  [`UpgradeConfiguration` API type](/docs/reference/config-api/kubeadm-config.v1beta4/) which can
  be used to configure the upgrade process.
* `kubeadm upgrade` does not support reconfiguration of an existing cluster. Follow the steps in
  [Reconfiguring a kubeadm cluster](/docs/tasks/administer-cluster/kubeadm/kubeadm-reconfigure/) instead.

### Considerations when upgrading etcd

Because the `kube-apiserver` static pod is running at all times (even if you
have drained the node), when you perform a kubeadm upgrade which includes an
etcd upgrade, in-flight requests to the server will stall while the new etcd
static pod is restarting. As a workaround, it is possible to actively stop the
`kube-apiserver` process a few seconds before starting the `kubeadm upgrade apply` command. This permits to complete in-flight requests and close existing
connections, and minimizes the consequence of the etcd downtime. This can be
done as follows on control plane nodes:

```
killall -s SIGTERM kube-apiserver # trigger a graceful kube-apiserver shutdown
sleep 20 # wait a little bit to permit completing in-flight requests
kubeadm upgrade ... # execute a kubeadm upgrade command
```

## Changing the package repository

If you're using the community-owned package repositories (`pkgs.k8s.io`), you need to
enable the package repository for the desired Kubernetes minor release. This is explained in
[Changing the Kubernetes package repository](/docs/tasks/administer-cluster/kubeadm/change-package-repository/)
document.

> **Note:**
> **Note:** The legacy package repositories (`apt.kubernetes.io` and `yum.kubernetes.io`) have been
> [deprecated and frozen starting from September 13, 2023](/blog/2023/08/31/legacy-package-repository-deprecation/).
> **Using the [new package repositories hosted at `pkgs.k8s.io`](/blog/2023/08/15/pkgs-k8s-io-introduction/)
> is strongly recommended and required in order to install Kubernetes versions released after September 13, 2023.**
> The deprecated legacy repositories, and their contents, might be removed at any time in the future and without
> a further notice period. The new package repositories provide downloads for Kubernetes versions starting with v1.24.0.

## Determine which version to upgrade to

Find the latest patch release for Kubernetes 1.34 using the OS package manager:

* Ubuntu, Debian or HypriotOS
  * CentOS, RHEL or Fedora

```
# Find the latest 1.34 version in the list.
# It should look like 1.34.x-*, where x is the latest patch.
sudo apt update
sudo apt-cache madison kubeadm
```

For systems with DNF:

```
# Find the latest 1.34 version in the list.
# It should look like 1.34.x-*, where x is the latest patch.
sudo yum list --showduplicates kubeadm --disableexcludes=kubernetes
```

For systems with DNF5:

```
# Find the latest 1.34 version in the list.
# It should look like 1.34.x-*, where x is the latest patch.
sudo yum list --showduplicates kubeadm --setopt=disable_excludes=kubernetes
```

If you don't see the version you expect to upgrade to, [verify if the Kubernetes package repositories are used.](/docs/tasks/administer-cluster/kubeadm/change-package-repository/#verifying-if-the-kubernetes-package-repositories-are-used)

## Upgrading control plane nodes

The upgrade procedure on control plane nodes should be executed one node at a time.
Pick a control plane node that you wish to upgrade first. It must have the `/etc/kubernetes/admin.conf` file.

### Call "kubeadm upgrade"

**For the first control plane node**

1. Upgrade kubeadm:

   * Ubuntu, Debian or HypriotOS
     * CentOS, RHEL or Fedora

   ```
   # replace x in 1.34.x-* with the latest patch version
   sudo apt-mark unhold kubeadm && \
   sudo apt-get update && sudo apt-get install -y kubeadm='1.34.x-*' && \
   sudo apt-mark hold kubeadm
   ```

   For systems with DNF:

   ```
   # replace x in 1.34.x-* with the latest patch version
   sudo yum install -y kubeadm-'1.34.x-*' --disableexcludes=kubernetes
   ```

   For systems with DNF5:

   ```
   # replace x in 1.34.x-* with the latest patch version
   sudo yum install -y kubeadm-'1.34.x-*' --setopt=disable_excludes=kubernetes
   ```
2. Verify that the download works and has the expected version:

   ```
   kubeadm version
   ```
3. Verify the upgrade plan:

   ```
   sudo kubeadm upgrade plan
   ```

   This command checks that your cluster can be upgraded, and fetches the versions you can upgrade to.
   It also shows a table with the component config version states.

   > **Note:**
   > `kubeadm upgrade` also automatically renews the certificates that it manages on this node.
   > To opt-out of certificate renewal the flag `--certificate-renewal=false` can be used.
   > For more information see the [certificate management guide](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/).
4. Choose a version to upgrade to, and run the appropriate command. For example:

   ```
   # replace x with the patch version you picked for this upgrade
   sudo kubeadm upgrade apply v1.34.x
   ```

   Once the command finishes you should see:

   ```
   [upgrade/successful] SUCCESS! Your cluster was upgraded to "v1.34.x". Enjoy!

   [upgrade/kubelet] Now that your control plane is upgraded, please proceed with upgrading your kubelets if you haven't already done so.
   ```

   > **Note:**
   > For versions earlier than v1.28, kubeadm defaulted to a mode that upgrades the addons (including CoreDNS and kube-proxy)
   > immediately during `kubeadm upgrade apply`, regardless of whether there are other control plane instances that have not
   > been upgraded. This may cause compatibility problems. Since v1.28, kubeadm defaults to a mode that checks whether all
   > the control plane instances have been upgraded before starting to upgrade the addons. You must perform control plane
   > instances upgrade sequentially or at least ensure that the last control plane instance upgrade is not started until all
   > the other control plane instances have been upgraded completely, and the addons upgrade will be performed after the last
   > control plane instance is upgraded.
5. Manually upgrade your CNI provider plugin.

   Your Container Network Interface (CNI) provider may have its own upgrade instructions to follow.
   Check the [addons](/docs/concepts/cluster-administration/addons/) page to
   find your CNI provider and see whether additional upgrade steps are required.

   This step is not required on additional control plane nodes if the CNI provider runs as a DaemonSet.

**For the other control plane nodes**

Same as the first control plane node but use:

```
sudo kubeadm upgrade node
```

instead of:

```
sudo kubeadm upgrade apply
```

Also calling `kubeadm upgrade plan` and upgrading the CNI provider plugin is no longer needed.

### Drain the node

Prepare the node for maintenance by marking it unschedulable and evicting the workloads:

```
# replace <node-to-drain> with the name of your node you are draining
kubectl drain <node-to-drain> --ignore-daemonsets
```

### Upgrade kubelet and kubectl

1. Upgrade the kubelet and kubectl:

   * Ubuntu, Debian or HypriotOS
     * CentOS, RHEL or Fedora

   ```
   # replace x in 1.34.x-* with the latest patch version
   sudo apt-mark unhold kubelet kubectl && \
   sudo apt-get update && sudo apt-get install -y kubelet='1.34.x-*' kubectl='1.34.x-*' && \
   sudo apt-mark hold kubelet kubectl
   ```

   For systems with DNF:

   ```
   # replace x in 1.34.x-* with the latest patch version
   sudo yum install -y kubelet-'1.34.x-*' kubectl-'1.34.x-*' --disableexcludes=kubernetes
   ```

   For systems with DNF5:

   ```
   # replace x in 1.34.x-* with the latest patch version
   sudo yum install -y kubelet-'1.34.x-*' kubectl-'1.34.x-*' --setopt=disable_excludes=kubernetes
   ```
2. Restart the kubelet:

   ```
   sudo systemctl daemon-reload
   sudo systemctl restart kubelet
   ```

### Uncordon the node

Bring the node back online by marking it schedulable:

```
# replace <node-to-uncordon> with the name of your node
kubectl uncordon <node-to-uncordon>
```

## Upgrade worker nodes

The upgrade procedure on worker nodes should be executed one node at a time or few nodes at a time,
without compromising the minimum required capacity for running your workloads.

The following pages show how to upgrade Linux and Windows worker nodes:

* [Upgrade Linux nodes](/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes/)
* [Upgrade Windows nodes](/docs/tasks/administer-cluster/kubeadm/upgrading-windows-nodes/)

## Verify the status of the cluster

After the kubelet is upgraded on all nodes verify that all nodes are available again by running
the following command from anywhere kubectl can access the cluster:

```
kubectl get nodes
```

The `STATUS` column should show `Ready` for all your nodes, and the version number should be updated.

## Recovering from a failure state

If `kubeadm upgrade` fails and does not roll back, for example because of an unexpected shutdown during execution, you can run `kubeadm upgrade` again.
This command is idempotent and eventually makes sure that the actual state is the desired state you declare.

To recover from a bad state, you can also run `sudo kubeadm upgrade apply --force` without changing the version that your cluster is running.

During upgrade kubeadm writes the following backup folders under `/etc/kubernetes/tmp`:

* `kubeadm-backup-etcd-<date>-<time>`
* `kubeadm-backup-manifests-<date>-<time>`

`kubeadm-backup-etcd` contains a backup of the local etcd member data for this control plane Node.
In case of an etcd upgrade failure and if the automatic rollback does not work, the contents of this folder
can be manually restored in `/var/lib/etcd`. In case external etcd is used this backup folder will be empty.

`kubeadm-backup-manifests` contains a backup of the static Pod manifest files for this control plane Node.
In case of a upgrade failure and if the automatic rollback does not work, the contents of this folder can be
manually restored in `/etc/kubernetes/manifests`. If for some reason there is no difference between a pre-upgrade
and post-upgrade manifest file for a certain component, a backup file for it will not be written.

> **Note:**
> After the cluster upgrade using kubeadm, the backup directory `/etc/kubernetes/tmp` will remain and
> these backup files will need to be cleared manually.

## How it works

`kubeadm upgrade apply` does the following:

* Checks that your cluster is in an upgradeable state:
  + The API server is reachable
  + All nodes are in the `Ready` state
  + The control plane is healthy
* Enforces the version skew policies.
* Makes sure the control plane images are available or available to pull to the machine.
* Generates replacements and/or uses user supplied overwrites if component configs require version upgrades.
* Upgrades the control plane components or rollbacks if any of them fails to come up.
* Applies the new `CoreDNS` and `kube-proxy` manifests and makes sure that all necessary RBAC rules are created.
* Creates new certificate and key files of the API server and backs up old files if they're about to expire in 180 days.

`kubeadm upgrade node` does the following on additional control plane nodes:

* Fetches the kubeadm `ClusterConfiguration` from the cluster.
* Optionally backups the kube-apiserver certificate.
* Upgrades the static Pod manifests for the control plane components.
* Upgrades the kubelet configuration for this node.

`kubeadm upgrade node` does the following on worker nodes:

* Fetches the kubeadm `ClusterConfiguration` from the cluster.
* Upgrades the kubelet configuration for this node.

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
