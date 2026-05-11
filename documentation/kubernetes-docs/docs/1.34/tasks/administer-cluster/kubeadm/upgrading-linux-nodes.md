# Upgrading Linux nodes

This page explains how to upgrade a Linux Worker Nodes created with kubeadm.

## Before you begin

You need to have shell access to all the nodes, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial
on a cluster with at least two nodes that are not acting as control plane hosts.

To check the version, enter `kubectl version`.

* Familiarize yourself with [the process for upgrading the rest of your kubeadm
  cluster](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/). You will want to
  upgrade the control plane nodes before upgrading your Linux Worker nodes.

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

## Upgrading worker nodes

### Upgrade kubeadm

Upgrade kubeadm:

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

### Call "kubeadm upgrade"

For worker nodes this upgrades the local kubelet configuration:

```
sudo kubeadm upgrade node
```

### Drain the node

Prepare the node for maintenance by marking it unschedulable and evicting the workloads:

```
# execute this command on a control plane node
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
# execute this command on a control plane node
# replace <node-to-uncordon> with the name of your node
kubectl uncordon <node-to-uncordon>
```

## What's next

* See how to [Upgrade Windows nodes](/docs/tasks/administer-cluster/kubeadm/upgrading-windows-nodes/).

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
