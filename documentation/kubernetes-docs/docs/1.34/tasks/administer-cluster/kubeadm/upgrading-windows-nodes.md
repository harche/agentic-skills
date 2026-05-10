# Upgrading Windows nodes

FEATURE STATE:
`Kubernetes v1.18 [beta]`

This page explains how to upgrade a Windows node created with kubeadm.

## Before you begin

You need to have shell access to all the nodes, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial
on a cluster with at least two nodes that are not acting as control plane hosts.

Your Kubernetes server must be at or later than version 1.17.

To check the version, enter `kubectl version`.

* Familiarize yourself with [the process for upgrading the rest of your kubeadm
  cluster](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/). You will want to
  upgrade the control plane nodes before upgrading your Windows nodes.

## Upgrading worker nodes

### Upgrade kubeadm

1. From the Windows node, upgrade kubeadm:

   ```
   # replace 1.34.0 with your desired version
   curl.exe -Lo <path-to-kubeadm.exe>  "https://dl.k8s.io/v1.34.0/bin/windows/amd64/kubeadm.exe"
   ```

### Drain the node

1. From a machine with access to the Kubernetes API,
   prepare the node for maintenance by marking it unschedulable and evicting the workloads:

   ```
   # replace <node-to-drain> with the name of your node you are draining
   kubectl drain <node-to-drain> --ignore-daemonsets
   ```

   You should see output similar to this:

   ```
   node/ip-172-31-85-18 cordoned
   node/ip-172-31-85-18 drained
   ```

### Upgrade the kubelet configuration

1. From the Windows node, call the following command to sync new kubelet configuration:

   ```
   kubeadm upgrade node
   ```

### Upgrade kubelet and kube-proxy

1. From the Windows node, upgrade and restart the kubelet:

   ```
   stop-service kubelet
   curl.exe -Lo <path-to-kubelet.exe> "https://dl.k8s.io/v1.34.0/bin/windows/amd64/kubelet.exe"
   restart-service kubelet
   ```
2. From the Windows node, upgrade and restart the kube-proxy.

   ```
   stop-service kube-proxy
   curl.exe -Lo <path-to-kube-proxy.exe> "https://dl.k8s.io/v1.34.0/bin/windows/amd64/kube-proxy.exe"
   restart-service kube-proxy
   ```

> **Note:**
> If you are running kube-proxy in a HostProcess container within a Pod, and not as a Windows Service,
> you can upgrade kube-proxy by applying a newer version of your kube-proxy manifests.

### Uncordon the node

1. From a machine with access to the Kubernetes API,
   bring the node back online by marking it schedulable:

   ```
   # replace <node-to-drain> with the name of your node
   kubectl uncordon <node-to-drain>
   ```

## What's next

* See how to [Upgrade Linux nodes](/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes/).

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
