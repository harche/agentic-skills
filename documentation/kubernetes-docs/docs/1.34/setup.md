# Getting started

This section lists the different ways to set up and run Kubernetes.
When you install Kubernetes, choose an installation type based on: ease of maintenance, security,
control, available resources, and expertise required to operate and manage a cluster.

You can [download Kubernetes](/releases/download/) to deploy a Kubernetes cluster
on a local machine, into the cloud, or for your own datacenter.

Several [Kubernetes components](/docs/concepts/overview/components/) such as [kube-apiserver](/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API.") or [kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/ "kube-proxy is a network proxy that runs on each node in the cluster.") can also be
deployed as [container images](/releases/download/#container-images) within the cluster.

It is **recommended** to run Kubernetes components as container images wherever
that is possible, and to have Kubernetes manage those components.
Components that run containers - notably, the kubelet - can't be included in this category.

If you don't want to manage a Kubernetes cluster yourself, you could pick a managed service, including
[certified platforms](/docs/setup/production-environment/turnkey-solutions/).
There are also other standardized and custom solutions across a wide range of cloud and
bare metal environments.

## Learning environment

If you're learning Kubernetes, use the tools supported by the Kubernetes community,
or tools in the ecosystem to set up a Kubernetes cluster on a local machine.
See [Install tools](/docs/tasks/tools/).

## Production environment

When evaluating a solution for a
[production environment](/docs/setup/production-environment/), consider which aspects of
operating a Kubernetes cluster (or *abstractions*) you want to manage yourself and which you
prefer to hand off to a provider.

For a cluster you're managing yourself, the officially supported tool
for deploying Kubernetes is [kubeadm](/docs/setup/production-environment/tools/kubeadm/).

## What's next

* [Download Kubernetes](/releases/download/)
* Download and [install tools](/docs/tasks/tools/) including `kubectl`
* Select a [container runtime](/docs/setup/production-environment/container-runtimes/) for your new cluster
* Learn about [best practices](/docs/setup/best-practices/) for cluster setup

Kubernetes is designed for its [control plane](/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.") to
run on Linux. Within your cluster you can run applications on Linux or other operating systems, including
Windows.

* Learn to [set up clusters with Windows nodes](/docs/concepts/windows/)

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
