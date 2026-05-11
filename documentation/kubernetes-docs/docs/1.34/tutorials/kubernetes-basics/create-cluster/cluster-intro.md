# Using Minikube to Create a Cluster

## Objectives

* Learn what a Kubernetes cluster is.
* Learn what Minikube is.
* Start a Kubernetes cluster on your computer.

## Kubernetes Clusters

> **Note:**
> *Kubernetes is a production-grade, open-source platform that orchestrates
> the placement (scheduling) and execution of application containers
> within and across computer clusters.*

**Kubernetes coordinates a highly available cluster of computers that are connected
to work as a single unit.** The abstractions in Kubernetes allow you to deploy
containerized applications to a cluster without tying them specifically to individual
machines. To make use of this new model of deployment, applications need to be packaged
in a way that decouples them from individual hosts: they need to be containerized.
Containerized applications are more flexible and available than in past deployment models,
where applications were installed directly onto specific machines as packages deeply
integrated into the host. **Kubernetes automates the distribution and scheduling of
application containers across a cluster in a more efficient way.** Kubernetes is an
open-source platform and is production-ready.

A Kubernetes cluster consists of two types of resources:

* The **Control Plane** coordinates the cluster
* **Nodes** are the workers that run applications

### Cluster Diagram

![](/docs/tutorials/kubernetes-basics/public/images/module_01_cluster.svg)

**The Control Plane is responsible for managing the cluster.** The Control Plane
coordinates all activities in your cluster, such as scheduling applications, maintaining
applications' desired state, scaling applications, and rolling out new updates.

> **Note:**
> *Control Planes manage the cluster and the nodes that are used to host the running
> applications.*

**A node is a VM or a physical computer that serves as a worker machine in a Kubernetes
cluster.** Each node has a Kubelet, which is an agent for managing the node and
communicating with the Kubernetes control plane. The node should also have tools for
handling container operations, such as [containerd](https://containerd.io/docs/ "A container runtime with an emphasis on simplicity, robustness and portability")
or [CRI-O](https://cri-o.io/#what-is-cri-o "A lightweight container runtime specifically for Kubernetes"). A Kubernetes cluster that handles production
traffic should have a minimum of three nodes because if one node goes down, both an
[etcd](/docs/concepts/architecture/#etcd) member and a control plane instance are lost,
and redundancy is compromised. You can mitigate this risk by adding more control plane nodes.

When you deploy applications on Kubernetes, you tell the control plane to start
the application containers. The control plane schedules the containers to run on
the cluster's nodes. **Node-level components, such as the kubelet, communicate
with the control plane using the [Kubernetes API](/docs/concepts/overview/kubernetes-api/)**,
which the control plane exposes. End users can also use the Kubernetes API directly
to interact with the cluster.

A Kubernetes cluster can be deployed on either physical or virtual machines. To
get started with Kubernetes development, you can use Minikube. Minikube is a lightweight
Kubernetes implementation that creates a VM on your local machine and deploys a
simple cluster containing only one node. Minikube is available for Linux, macOS,
and Windows systems. The Minikube CLI provides basic bootstrapping operations for
working with your cluster, including start, stop, status, and delete.

## What's next

* Tutorial [Hello Minikube](/docs/tutorials/hello-minikube/).
* Learn more about [Cluster Architecture](/docs/concepts/architecture/).

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
