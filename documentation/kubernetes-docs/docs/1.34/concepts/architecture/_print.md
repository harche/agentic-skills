This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/concepts/architecture/).

# Cluster Architecture

The architectural concepts behind Kubernetes.

* 1: [Nodes](#pg-9ef2890698e773b6c0d24fd2c20146f5)
* 2: [Communication between Nodes and the Control Plane](#pg-c0251def6da29b30afebfb04549f1703)
* 3: [Controllers](#pg-ca8819042a505291540e831283da66df)
* 4: [Leases](#pg-d5e64235fa89f107957072cd8a39e4c5)
* 5: [Cloud Controller Manager](#pg-bc804b02614d67025b4c788f1ca87fbc)
* 6: [About cgroup v2](#pg-c20ec7d296cc2c8668bb204c2af31180)
* 7: [Kubernetes Self-Healing](#pg-f992b9b0f5b827e6fe522de5dde184cc)
* 8: [Garbage Collection](#pg-44a2e2e592af0846101e970aff9243e5)
* 9: [Mixed Version Proxy](#pg-93721154dcdc5837b4ff286b4d4202ea)

A Kubernetes cluster consists of a control plane plus a set of worker machines, called nodes,
that run containerized applications. Every cluster needs at least one worker node in order to run Pods.

The worker node(s) host the Pods that are the components of the application workload.
The control plane manages the worker nodes and the Pods in the cluster. In production
environments, the control plane usually runs across multiple computers and a cluster
usually runs multiple nodes, providing fault-tolerance and high availability.

This document outlines the various components you need to have for a complete and working Kubernetes cluster.

![The control plane (kube-apiserver, etcd, kube-controller-manager, kube-scheduler) and several nodes. Each node is running a kubelet and kube-proxy.](/images/docs/kubernetes-cluster-architecture.svg)

Figure 1. Kubernetes cluster components.

About this architecture

The diagram in Figure 1 presents an example reference architecture for a Kubernetes cluster.
The actual distribution of components can vary based on specific cluster setups and requirements.

In the diagram, each node runs the [`kube-proxy`](#kube-proxy) component. You need a
network proxy component on each node to ensure that the
[Service](/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.") API and associated behaviors
are available on your cluster network. However, some network plugins provide their own,
third party implementation of proxying. When you use that kind of network plugin,
the node does not need to run `kube-proxy`.

## Control plane components

The control plane's components make global decisions about the cluster (for example, scheduling),
as well as detecting and responding to cluster events (for example, starting up a new
[pod](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") when a Deployment's
`replicas` field is unsatisfied).

Control plane components can be run on any machine in the cluster. However, for simplicity, setup scripts
typically start all control plane components on the same machine, and do not run user containers on this machine.
See [Creating Highly Available clusters with kubeadm](/docs/setup/production-environment/tools/kubeadm/high-availability/)
for an example control plane setup that runs across multiple machines.

### kube-apiserver

The API server is a component of the Kubernetes
[control plane](/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.") that exposes the Kubernetes API.
The API server is the front end for the Kubernetes control plane.

The main implementation of a Kubernetes API server is [kube-apiserver](/docs/reference/generated/kube-apiserver/).
kube-apiserver is designed to scale horizontally—that is, it scales by deploying more instances.
You can run several instances of kube-apiserver and balance traffic between those instances.

### etcd

Consistent and highly-available key value store used as Kubernetes' backing store for all cluster data.

If your Kubernetes cluster uses etcd as its backing store, make sure you have a
[back up](/docs/tasks/administer-cluster/configure-upgrade-etcd/#backing-up-an-etcd-cluster) plan
for the data.

You can find in-depth information about etcd in the official [documentation](https://etcd.io/docs/).

### kube-scheduler

Control plane component that watches for newly created
[Pods](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") with no assigned
[node](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes."), and selects a node for them
to run on.

Factors taken into account for scheduling decisions include:
individual and collective [resource](/docs/reference/glossary/?all=true#term-infrastructure-resource "A defined amount of infrastructure available for consumption (CPU, memory, etc).")
requirements, hardware/software/policy constraints, affinity and anti-affinity specifications,
data locality, inter-workload interference, and deadlines.

### kube-controller-manager

Control plane component that runs [controller](/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") processes.

Logically, each [controller](/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") is a separate process, but to reduce complexity, they are all compiled into a single binary and run in a single process.

There are many different types of controllers. Some examples of them are:

* Node controller: Responsible for noticing and responding when nodes go down.
* Job controller: Watches for Job objects that represent one-off tasks, then creates Pods to run those tasks to completion.
* EndpointSlice controller: Populates EndpointSlice objects (to provide a link between Services and Pods).
* ServiceAccount controller: Create default ServiceAccounts for new namespaces.

The above is not an exhaustive list.

### cloud-controller-manager

A Kubernetes [control plane](/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.") component
that embeds cloud-specific control logic. The cloud controller manager lets you link your
cluster into your cloud provider's API, and separates out the components that interact
with that cloud platform from components that only interact with your cluster.

The cloud-controller-manager only runs controllers that are specific to your cloud provider.
If you are running Kubernetes on your own premises, or in a learning environment inside your
own PC, the cluster does not have a cloud controller manager.

As with the kube-controller-manager, the cloud-controller-manager combines several logically
independent control loops into a single binary that you run as a single process. You can scale
horizontally (run more than one copy) to improve performance or to help tolerate failures.

The following controllers can have cloud provider dependencies:

* Node controller: For checking the cloud provider to determine if a node has been
  deleted in the cloud after it stops responding
* Route controller: For setting up routes in the underlying cloud infrastructure
* Service controller: For creating, updating and deleting cloud provider load balancers

---

## Node components

Node components run on every node, maintaining running pods and providing the Kubernetes runtime environment.

### kubelet

An agent that runs on each [node](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") in the cluster. It makes sure that [containers](/docs/concepts/containers/ "A lightweight and portable executable image that contains software and all of its dependencies.") are running in a [Pod](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.").

The [kubelet](/docs/reference/command-line-tools-reference/kubelet/) takes a set of PodSpecs that
are provided through various mechanisms and ensures that the containers described in those
PodSpecs are running and healthy. The kubelet doesn't manage containers which were not created by
Kubernetes.

### kube-proxy (optional)

kube-proxy is a network proxy that runs on each
[node](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") in your cluster,
implementing part of the Kubernetes
[Service](/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.") concept.

[kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/)
maintains network rules on nodes. These network rules allow network
communication to your Pods from network sessions inside or outside of
your cluster.

kube-proxy uses the operating system packet filtering layer if there is one
and it's available. Otherwise, kube-proxy forwards the traffic itself.

If you use a [network plugin](#network-plugins) that implements packet forwarding for Services
by itself, and providing equivalent behavior to kube-proxy, then you do not need to run
kube-proxy on the nodes in your cluster.

### Container runtime

A fundamental component that empowers Kubernetes to run containers effectively.
It is responsible for managing the execution and lifecycle of containers within the Kubernetes environment.

Kubernetes supports container runtimes such as
[containerd](https://containerd.io/docs/ "A container runtime with an emphasis on simplicity, robustness and portability"), [CRI-O](https://cri-o.io/#what-is-cri-o "A lightweight container runtime specifically for Kubernetes"),
and any other implementation of the [Kubernetes CRI (Container Runtime
Interface)](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/container-runtime-interface.md).

## Addons

Addons use Kubernetes resources ([DaemonSet](/docs/concepts/workloads/controllers/daemonset "Ensures a copy of a Pod is running across a set of nodes in a cluster."),
[Deployment](/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster."), etc) to implement cluster features.
Because these are providing cluster-level features, namespaced resources for
addons belong within the `kube-system` namespace.

Selected addons are described below; for an extended list of available addons,
please see [Addons](/docs/concepts/cluster-administration/addons/).

### DNS

While the other addons are not strictly required, all Kubernetes clusters should have
[cluster DNS](/docs/concepts/services-networking/dns-pod-service/), as many examples rely on it.

Cluster DNS is a DNS server, in addition to the other DNS server(s) in your environment,
which serves DNS records for Kubernetes services.

Containers started by Kubernetes automatically include this DNS server in their DNS searches.

### Web UI (Dashboard)

[Dashboard](/docs/tasks/access-application-cluster/web-ui-dashboard/) is a general purpose,
web-based UI for Kubernetes clusters. It allows users to manage and troubleshoot applications
running in the cluster, as well as the cluster itself.

### Container resource monitoring

[Container Resource Monitoring](/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)
records generic time-series metrics about containers in a central database, and provides a UI for browsing that data.

### Cluster-level Logging

A [cluster-level logging](/docs/concepts/cluster-administration/logging/) mechanism is responsible
for saving container logs to a central log store with a search/browsing interface.

### Network plugins

[Network plugins](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
are software components that implement the container network interface (CNI) specification.
They are responsible for allocating IP addresses to pods and enabling them to communicate
with each other within the cluster.

## Architecture variations

While the core components of Kubernetes remain consistent, the way they are deployed and
managed can vary. Understanding these variations is crucial for designing and maintaining
Kubernetes clusters that meet specific operational needs.

### Control plane deployment options

The control plane components can be deployed in several ways:

Traditional deployment
:   Control plane components run directly on dedicated machines or VMs, often managed as systemd services.

Static Pods
:   Control plane components are deployed as static Pods, managed by the kubelet on specific nodes.
    This is a common approach used by tools like kubeadm.

Self-hosted
:   The control plane runs as Pods within the Kubernetes cluster itself, managed by Deployments
    and StatefulSets or other Kubernetes primitives.

Managed Kubernetes services
:   Cloud providers often abstract away the control plane, managing its components as part of their service offering.

### Workload placement considerations

The placement of workloads, including the control plane components, can vary based on cluster size,
performance requirements, and operational policies:

* In smaller or development clusters, control plane components and user workloads might run on the same nodes.
* Larger production clusters often dedicate specific nodes to control plane components,
  separating them from user workloads.
* Some organizations run critical add-ons or monitoring tools on control plane nodes.

### Cluster management tools

Tools like kubeadm, kops, and Kubespray offer different approaches to deploying and managing clusters,
each with its own method of component layout and management.

### Customization and extensibility

Kubernetes architecture allows for significant customization:

* Custom schedulers can be deployed to work alongside the default Kubernetes scheduler or to replace it entirely.
* API servers can be extended with CustomResourceDefinitions and API Aggregation.
* Cloud providers can integrate deeply with Kubernetes using the cloud-controller-manager.

The flexibility of Kubernetes architecture allows organizations to tailor their clusters to specific needs,
balancing factors such as operational complexity, performance, and management overhead.

## What's next

Learn more about the following:

* [Nodes](/docs/concepts/architecture/nodes/) and
  [their communication](/docs/concepts/architecture/control-plane-node-communication/)
  with the control plane.
* Kubernetes [controllers](/docs/concepts/architecture/controller/).
* [kube-scheduler](/docs/concepts/scheduling-eviction/kube-scheduler/) which is the default scheduler for Kubernetes.
* Etcd's official [documentation](https://etcd.io/docs/).
* Several [container runtimes](/docs/setup/production-environment/container-runtimes/) in Kubernetes.
* Integrating with cloud providers using [cloud-controller-manager](/docs/concepts/architecture/cloud-controller/).
* [kubectl](/docs/reference/generated/kubectl/kubectl-commands) commands.
