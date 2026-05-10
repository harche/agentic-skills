# Configure Default CPU Requests and Limits for a Namespace

Define a default CPU resource limits for a namespace, so that every new Pod in that namespace has a CPU resource limit configured.

This page shows how to configure default CPU requests and limits for a
[namespace](/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster.").

A Kubernetes cluster can be divided into namespaces. If you create a Pod within a
namespace that has a default CPU
[limit](/docs/concepts/configuration/manage-resources-containers/#requests-and-limits), and any container in that Pod does not specify
its own CPU limit, then the
[control plane](/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.") assigns the default
CPU limit to that container.

Kubernetes assigns a default CPU
[request](/docs/concepts/configuration/manage-resources-containers/#requests-and-limits),
but only under certain conditions that are explained later in this page.

## Before you begin

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [KodeKloud](https://kodekloud.com/public-playgrounds)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)

You must have access to create namespaces in your cluster.

If you're not already familiar with what Kubernetes means by 1.0 CPU,
read [meaning of CPU](/docs/concepts/configuration/manage-resources-containers/#meaning-of-cpu).

## Create a namespace

Create a namespace so that the resources you create in this exercise are
isolated from the rest of your cluster.

```
kubectl create namespace default-cpu-example
```

## Create a LimitRange and a Pod

Here's a manifest for an example [LimitRange](/docs/concepts/policy/limit-range/ "Provides constraints to limit resource consumption per Containers or Pods in a namespace.").
The manifest specifies a default CPU request and a default CPU limit.

[`admin/resource/cpu-defaults.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/admin/resource/cpu-defaults.yaml)![](/images/copycode.svg "Copy admin/resource/cpu-defaults.yaml to clipboard")

```
apiVersion: v1
kind: LimitRange
metadata:
  name: cpu-limit-range
spec:
  limits:
  - default:
      cpu: 1
    defaultRequest:
      cpu: 0.5
    type: Container
```

Create the LimitRange in the default-cpu-example namespace:

```
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults.yaml --namespace=default-cpu-example
```

Now if you create a Pod in the default-cpu-example namespace, and any container
in that Pod does not specify its own values for CPU request and CPU limit,
then the control plane applies default values: a CPU request of 0.5 and a default
CPU limit of 1.

Here's a manifest for a Pod that has one container. The container
does not specify a CPU request and limit.

[`admin/resource/cpu-defaults-pod.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/admin/resource/cpu-defaults-pod.yaml)![](/images/copycode.svg "Copy admin/resource/cpu-defaults-pod.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: default-cpu-demo
spec:
  containers:
  - name: default-cpu-demo-ctr
    image: nginx
```

Create the Pod.

```
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults-pod.yaml --namespace=default-cpu-example
```

View the Pod's specification:

```
kubectl get pod default-cpu-demo --output=yaml --namespace=default-cpu-example
```

The output shows that the Pod's only container has a CPU request of 500m `cpu`
(which you can read as “500 millicpu”), and a CPU limit of 1 `cpu`.
These are the default values specified by the LimitRange.

```
containers:
- image: nginx
  imagePullPolicy: Always
  name: default-cpu-demo-ctr
  resources:
    limits:
      cpu: "1"
    requests:
      cpu: 500m
```

## What if you specify a container's limit, but not its request?

Here's a manifest for a Pod that has one container. The container
specifies a CPU limit, but not a request:

[`admin/resource/cpu-defaults-pod-2.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/admin/resource/cpu-defaults-pod-2.yaml)![](/images/copycode.svg "Copy admin/resource/cpu-defaults-pod-2.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: default-cpu-demo-2
spec:
  containers:
  - name: default-cpu-demo-2-ctr
    image: nginx
    resources:
      limits:
        cpu: "1"
```

Create the Pod:

```
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults-pod-2.yaml --namespace=default-cpu-example
```

View the [specification](/docs/concepts/overview/working-with-objects/#object-spec-and-status)
of the Pod that you created:

```
kubectl get pod default-cpu-demo-2 --output=yaml --namespace=default-cpu-example
```

The output shows that the container's CPU request is set to match its CPU limit.
Notice that the container was not assigned the default CPU request value of 0.5 `cpu`:

```
resources:
  limits:
    cpu: "1"
  requests:
    cpu: "1"
```

## What if you specify a container's request, but not its limit?

Here's an example manifest for a Pod that has one container. The container
specifies a CPU request, but not a limit:

[`admin/resource/cpu-defaults-pod-3.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/admin/resource/cpu-defaults-pod-3.yaml)![](/images/copycode.svg "Copy admin/resource/cpu-defaults-pod-3.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: default-cpu-demo-3
spec:
  containers:
  - name: default-cpu-demo-3-ctr
    image: nginx
    resources:
      requests:
        cpu: "0.75"
```

Create the Pod:

```
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults-pod-3.yaml --namespace=default-cpu-example
```

View the specification of the Pod that you created:

```
kubectl get pod default-cpu-demo-3 --output=yaml --namespace=default-cpu-example
```

The output shows that the container's CPU request is set to the value you specified at
the time you created the Pod (in other words: it matches the manifest).
However, the same container's CPU limit is set to 1 `cpu`, which is the default CPU limit
for that namespace.

```
resources:
  limits:
    cpu: "1"
  requests:
    cpu: 750m
```

## Motivation for default CPU limits and requests

If your namespace has a CPU [resource quota](/docs/concepts/policy/resource-quotas/ "Provides constraints that limit aggregate resource consumption per namespace.")
configured,
it is helpful to have a default value in place for CPU limit.
Here are two of the restrictions that a CPU resource quota imposes on a namespace:

* For every Pod that runs in the namespace, each of its containers must have a CPU limit.
* CPU limits apply a resource reservation on the node where the Pod in question is scheduled.
  The total amount of CPU that is reserved for use by all Pods in the namespace must not
  exceed a specified limit.

When you add a LimitRange:

If any Pod in that namespace that includes a container does not specify its own CPU limit,
the control plane applies the default CPU limit to that container, and the Pod can be
allowed to run in a namespace that is restricted by a CPU ResourceQuota.

## Clean up

Delete your namespace:

```
kubectl delete namespace default-cpu-example
```

## What's next

### For cluster administrators

* [Configure Default Memory Requests and Limits for a Namespace](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)
* [Configure Minimum and Maximum Memory Constraints for a Namespace](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)
* [Configure Minimum and Maximum CPU Constraints for a Namespace](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)
* [Configure Memory and CPU Quotas for a Namespace](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)
* [Configure a Pod Quota for a Namespace](/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)
* [Configure Quotas for API Objects](/docs/tasks/administer-cluster/quota-api-object/)

### For app developers

* [Assign Memory Resources to Containers and Pods](/docs/tasks/configure-pod-container/assign-memory-resource/)
* [Assign CPU Resources to Containers and Pods](/docs/tasks/configure-pod-container/assign-cpu-resource/)
* [Assign Pod-level CPU and memory resources](/docs/tasks/configure-pod-container/assign-pod-level-resources/)
* [Configure Quality of Service for Pods](/docs/tasks/configure-pod-container/quality-service-pod/)

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
