# Upgrade A Cluster

This page provides an overview of the steps you should follow to upgrade a
Kubernetes cluster.

The Kubernetes project recommends upgrading to the latest patch releases promptly, and
to ensure that you are running a supported minor release of Kubernetes.
Following this recommendation helps you to stay secure.

The way that you upgrade a cluster depends on how you initially deployed it
and on any subsequent changes.

At a high level, the steps you perform are:

* Upgrade the [control plane](/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.")
* Upgrade the nodes in your cluster
* Upgrade clients such as [kubectl](/docs/reference/kubectl/ "A command line tool for communicating with a Kubernetes cluster.")
* Adjust manifests and other resources based on the API changes that accompany the
  new Kubernetes version

## Before you begin

You must have an existing cluster. This page is about upgrading from Kubernetes
1.33 to Kubernetes 1.34. If your cluster
is not currently running Kubernetes 1.33 then please check
the documentation for the version of Kubernetes that you plan to upgrade to.

## Upgrade approaches

### kubeadm

If your cluster was deployed using the `kubeadm` tool, refer to
[Upgrading kubeadm clusters](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
for detailed information on how to upgrade the cluster.

Once you have upgraded the cluster, remember to
[install the latest version of `kubectl`](/docs/tasks/tools/).

### Manual deployments

> **Caution:**
> These steps do not account for third-party extensions such as network and storage
> plugins.

You should manually update the control plane following this sequence:

* etcd (all instances)
* kube-apiserver (all control plane hosts)
* kube-controller-manager
* kube-scheduler
* cloud controller manager, if you use one

At this point you should
[install the latest version of `kubectl`](/docs/tasks/tools/).

For each node in your cluster, [drain](/docs/tasks/administer-cluster/safely-drain-node/)
that node and then either replace it with a new node that uses the 1.34
kubelet, or upgrade the kubelet on that node and bring the node back into service.

> **Caution:**
> Draining nodes before upgrading kubelet ensures that pods are re-admitted and containers are
> re-created, which may be necessary to resolve some security issues or other important bugs.

### Other deployments

Refer to the documentation for your cluster deployment tool to learn the recommended set
up steps for maintenance.

## Post-upgrade tasks

### Switch your cluster's storage API version

The objects that are serialized into etcd for a cluster's internal
representation of the Kubernetes resources active in the cluster are
written using a particular version of the API.

When the supported API changes, these objects may need to be rewritten
in the newer API. Failure to do this will eventually result in resources
that are no longer decodable or usable by the Kubernetes API server.

For each affected object, fetch it using the latest supported API and then
write it back also using the latest supported API.

### Update manifests

Upgrading to a new Kubernetes version can provide new APIs.

You can use `kubectl convert` command to convert manifests between different API versions.
For example:

```
kubectl convert -f pod.yaml --output-version v1
```

The `kubectl` tool replaces the contents of `pod.yaml` with a manifest that sets `kind` to
Pod (unchanged), but with a revised `apiVersion`.

### Device Plugins

If your cluster is running device plugins and the node needs to be upgraded to a Kubernetes
release with a newer device plugin API version, device plugins must be upgraded to support
both version before the node is upgraded in order to guarantee that device allocations
continue to complete successfully during the upgrade.

Refer to [API compatibility](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#api-compatibility) and [Kubelet Device Manager API Versions](/docs/reference/node/device-plugin-api-versions/) for more details.

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
