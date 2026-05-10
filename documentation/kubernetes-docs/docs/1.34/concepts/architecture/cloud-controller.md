# Cloud Controller Manager

FEATURE STATE:
`Kubernetes v1.11 [beta]`

Cloud infrastructure technologies let you run Kubernetes on public, private, and hybrid clouds.
Kubernetes believes in automated, API-driven infrastructure without tight coupling between
components.

The cloud-controller-manager is a Kubernetes [control plane](/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.") component
that embeds cloud-specific control logic. The cloud controller manager lets you link your
cluster into your cloud provider's API, and separates out the components that interact
with that cloud platform from components that only interact with your cluster.

By decoupling the interoperability logic between Kubernetes and the underlying cloud
infrastructure, the cloud-controller-manager component enables cloud providers to release
features at a different pace compared to the main Kubernetes project.

The cloud-controller-manager is structured using a plugin
mechanism that allows different cloud providers to integrate their platforms with Kubernetes.

## Design

![Kubernetes components](/images/docs/components-of-kubernetes.svg)

The cloud controller manager runs in the control plane as a replicated set of processes
(usually, these are containers in Pods). Each cloud-controller-manager implements
multiple [controllers](/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") in a single
process.

> **Note:**
> You can also run the cloud controller manager as a Kubernetes
> [addon](/docs/concepts/cluster-administration/addons/ "Resources that extend the functionality of Kubernetes.") rather than as part
> of the control plane.

## Cloud controller manager functions

The controllers inside the cloud controller manager include:

### Node controller

The node controller is responsible for updating [Node](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") objects
when new servers are created in your cloud infrastructure. The node controller obtains information about the
hosts running inside your tenancy with the cloud provider. The node controller performs the following functions:

1. Update a Node object with the corresponding server's unique identifier obtained from the cloud provider API.
2. Annotating and labelling the Node object with cloud-specific information, such as the region the node
   is deployed into and the resources (CPU, memory, etc) that it has available.
3. Obtain the node's hostname and network addresses.
4. Verifying the node's health. In case a node becomes unresponsive, this controller checks with
   your cloud provider's API to see if the server has been deactivated / deleted / terminated.
   If the node has been deleted from the cloud, the controller deletes the Node object from your Kubernetes
   cluster.

Some cloud provider implementations split this into a node controller and a separate node
lifecycle controller.

### Route controller

The route controller is responsible for configuring routes in the cloud
appropriately so that containers on different nodes in your Kubernetes
cluster can communicate with each other.

Depending on the cloud provider, the route controller might also allocate blocks
of IP addresses for the Pod network.

### Service controller

[Services](/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.") integrate with cloud
infrastructure components such as managed load balancers, IP addresses, network
packet filtering, and target health checking. The service controller interacts with your
cloud provider's APIs to set up load balancers and other infrastructure components
when you declare a Service resource that requires them.

## Authorization

This section breaks down the access that the cloud controller manager requires
on various API objects, in order to perform its operations.

### Node controller

The Node controller only works with Node objects. It requires full access
to read and modify Node objects.

`v1/Node`:

* get
* list
* create
* update
* patch
* watch
* delete

### Route controller

The route controller listens to Node object creation and configures
routes appropriately. It requires Get access to Node objects.

`v1/Node`:

* get

### Service controller

The service controller watches for Service object **create**, **update** and **delete** events and then
configures load balancers for those Services appropriately.

To access Services, it requires **list**, and **watch** access. To update Services, it requires
**patch** and **update** access to the `status` subresource.

`v1/Service`:

* list
* get
* watch
* patch
* update

### Others

The implementation of the core of the cloud controller manager requires access to create Event
objects, and to ensure secure operation, it requires access to create ServiceAccounts.

`v1/Event`:

* create
* patch
* update

`v1/ServiceAccount`:

* create

The [RBAC](/docs/reference/access-authn-authz/rbac/ "Manages authorization decisions, allowing admins to dynamically configure access policies through the Kubernetes API.") ClusterRole for the cloud
controller manager looks like:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cloud-controller-manager
rules:
- apiGroups:
  - ""
  resources:
  - events
  verbs:
  - create
  - patch
  - update
- apiGroups:
  - ""
  resources:
  - nodes
  verbs:
  - '*'
- apiGroups:
  - ""
  resources:
  - nodes/status
  verbs:
  - patch
- apiGroups:
  - ""
  resources:
  - services
  verbs:
  - list
  - watch
- apiGroups:
  - ""
  resources:
  - services/status
  verbs:
  - patch
  - update
- apiGroups:
  - ""
  resources:
  - serviceaccounts
  verbs:
  - create
- apiGroups:
  - ""
  resources:
  - persistentvolumes
  verbs:
  - get
  - list
  - update
  - watch
```

## What's next

* [Cloud Controller Manager Administration](/docs/tasks/administer-cluster/running-cloud-controller/#cloud-controller-manager)
  has instructions on running and managing the cloud controller manager.
* To upgrade a HA control plane to use the cloud controller manager, see
  [Migrate Replicated Control Plane To Use Cloud Controller Manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/).
* Want to know how to implement your own cloud controller manager, or extend an existing project?

  + The cloud controller manager uses Go interfaces, specifically, `CloudProvider` interface defined in
    [`cloud.go`](https://github.com/kubernetes/cloud-provider/blob/release-1.21/cloud.go#L42-L69)
    from [kubernetes/cloud-provider](https://github.com/kubernetes/cloud-provider) to allow
    implementations from any cloud to be plugged in.
  + The implementation of the shared controllers highlighted in this document (Node, Route, and Service),
    and some scaffolding along with the shared cloudprovider interface, is part of the Kubernetes core.
    Implementations specific to cloud providers are outside the core of Kubernetes and implement
    the `CloudProvider` interface.
  + For more information about developing plugins,
    see [Developing Cloud Controller Manager](/docs/tasks/administer-cluster/developing-cloud-controller-manager/).

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
