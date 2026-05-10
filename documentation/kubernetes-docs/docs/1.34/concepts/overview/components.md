# Kubernetes Components

An overview of the key components that make up a Kubernetes cluster.

This page provides a high-level overview of the essential components that make up a Kubernetes cluster.

![Components of Kubernetes](/images/docs/components-of-kubernetes.svg)

The components of a Kubernetes cluster

## Core Components

A Kubernetes cluster consists of a control plane and one or more worker nodes.
Here's a brief overview of the main components:

### Control Plane Components

Manage the overall state of the cluster:

[kube-apiserver](/docs/concepts/architecture/#kube-apiserver)
:   The core component server that exposes the Kubernetes HTTP API.

[etcd](/docs/concepts/architecture/#etcd)
:   Consistent and highly-available key value store for all API server data.

[kube-scheduler](/docs/concepts/architecture/#kube-scheduler)
:   Looks for Pods not yet bound to a node, and assigns each Pod to a suitable node.

[kube-controller-manager](/docs/concepts/architecture/#kube-controller-manager)
:   Runs [controllers](/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") to implement Kubernetes API behavior.

[cloud-controller-manager](/docs/concepts/architecture/#cloud-controller-manager) (optional)
:   Integrates with underlying cloud provider(s).

### Node Components

Run on every node, maintaining running pods and providing the Kubernetes runtime environment:

[kubelet](/docs/concepts/architecture/#kubelet)
:   Ensures that Pods are running, including their containers.

[kube-proxy](/docs/concepts/architecture/#kube-proxy) (optional)
:   Maintains network rules on nodes to implement [Services](/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.").

[Container runtime](/docs/concepts/architecture/#container-runtime)
:   Software responsible for running containers. Read
    [Container Runtimes](/docs/setup/production-environment/container-runtimes/) to learn more.

> **Note:**
> 🛇 This item links to a third party project or product that is not part of Kubernetes itself. [More information](#third-party-content-disclaimer)

Your cluster may require additional software on each node; for example, you might also
run [systemd](https://systemd.io/) on a Linux node to supervise local components.

## Addons

Addons extend the functionality of Kubernetes. A few important examples include:

[DNS](/docs/concepts/architecture/#dns)
:   For cluster-wide DNS resolution.

[Web UI](/docs/concepts/architecture/#web-ui-dashboard) (Dashboard)
:   For cluster management via a web interface.

[Container Resource Monitoring](/docs/concepts/architecture/#container-resource-monitoring)
:   For collecting and storing container metrics.

[Cluster-level Logging](/docs/concepts/architecture/#cluster-level-logging)
:   For saving container logs to a central log store.

## Flexibility in Architecture

Kubernetes allows for flexibility in how these components are deployed and managed.
The architecture can be adapted to various needs, from small development environments
to large-scale production deployments.

For more detailed information about each component and various ways to configure your
cluster architecture, see the [Cluster Architecture](/docs/concepts/architecture/) page.

Items on this page refer to third party products or projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for those third-party products or projects. See the [CNCF website guidelines](https://github.com/cncf/foundation/blob/master/website-guidelines.md) for more details.

You should read the [content guide](/docs/contribute/style/content-guide/#third-party-content) before proposing a change that adds an extra third-party link.

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
