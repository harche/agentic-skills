# Overprovision Node Capacity For A Cluster

This page guides you through configuring [Node](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.")
overprovisioning in your Kubernetes cluster. Node overprovisioning is a strategy that proactively
reserves a portion of your cluster's compute resources. This reservation helps reduce the time
required to schedule new pods during scaling events, enhancing your cluster's responsiveness
to sudden spikes in traffic or workload demands.

By maintaining some unused capacity, you ensure that resources are immediately available when
new pods are created, preventing them from entering a pending state while the cluster scales up.

## Before you begin

* You need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with
  your cluster.
* You should already have a basic understanding of
  [Deployments](/docs/concepts/workloads/controllers/deployment/),
  Pod [priority](/docs/concepts/scheduling-eviction/pod-priority-preemption/#pod-priority "Pod Priority indicates the importance of a Pod relative to other Pods."),
  and [PriorityClasses](/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass "A mapping from a class name to the scheduling priority that a Pod should have.").
* Your cluster must be set up with an [autoscaler](/docs/concepts/cluster-administration/cluster-autoscaling/)
  that manages nodes based on demand.

## Create a PriorityClass

Begin by defining a PriorityClass for the placeholder Pods. First, create a PriorityClass with a
negative priority value, that you will shortly assign to the placeholder pods.
Later, you will set up a Deployment that uses this PriorityClass

[`priorityclass/low-priority-class.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/priorityclass/low-priority-class.yaml)![](/images/copycode.svg "Copy priorityclass/low-priority-class.yaml to clipboard")

```
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: placeholder # these Pods represent placeholder capacity
value: -1000
globalDefault: false
description: "Negative priority for placeholder pods to enable overprovisioning."
```

Then create the PriorityClass:

```
kubectl apply -f https://k8s.io/examples/priorityclass/low-priority-class.yaml
```

You will next define a Deployment that uses the negative-priority PriorityClass and runs a minimal container.
When you add this to your cluster, Kubernetes runs those placeholder pods to reserve capacity. Any time there
is a capacity shortage, the control plane will pick one these placeholder pods as the first candidate to
[preempt](/docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption "Preemption logic in Kubernetes helps a pending Pod to find a suitable Node by evicting low priority Pods existing on that Node.").

## Run Pods that request node capacity

Review the sample manifest:

[`deployments/deployment-with-capacity-reservation.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/deployments/deployment-with-capacity-reservation.yaml)![](/images/copycode.svg "Copy deployments/deployment-with-capacity-reservation.yaml to clipboard")

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: capacity-reservation
  # You should decide what namespace to deploy this into
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: capacity-placeholder
  template:
    metadata:
      labels:
        app.kubernetes.io/name: capacity-placeholder
      annotations:
        kubernetes.io/description: "Capacity reservation"
    spec:
      priorityClassName: placeholder
      affinity: # Try to place these overhead Pods on different nodes
                # if possible
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchLabels:
                  app.kubernetes.io/name: capacity-placeholder
              topologyKey: topology.kubernetes.io/hostname
      containers:
      - name: pause
        image: registry.k8s.io/pause:3.6
        resources:
          requests:
            cpu: "50m"
            memory: "512Mi"
          limits:
            memory: "512Mi"
```

### Pick a namespace for the placeholder pods

You should select, or create, a [namespace](/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster.")
that the placeholder Pods will go into.

### Create the placeholder deployment

Create a Deployment based on that manifest:

```
# Change the namespace name "example"
kubectl --namespace example apply -f https://k8s.io/examples/deployments/deployment-with-capacity-reservation.yaml
```

## Adjust placeholder resource requests

Configure the resource requests and limits for the placeholder pods to define the amount of overprovisioned resources you want to maintain. This reservation ensures that a specific amount of CPU and memory is kept available for new pods.

To edit the Deployment, modify the `resources` section in the Deployment manifest file
to set appropriate requests and limits. You can download that file locally and then edit it
with whichever text editor you prefer.

You can also edit the Deployment using kubectl:

```
kubectl edit deployment capacity-reservation
```

For example, to reserve a total of a 0.5 CPU and 1GiB of memory across 5 placeholder pods,
define the resource requests and limits for a single placeholder pod as follows:

```
  resources:
    requests:
      cpu: "100m"
      memory: "200Mi"
    limits:
      cpu: "100m"
```

## Set the desired replica count

### Calculate the total reserved resources

For example, with 5 replicas each reserving 0.1 CPU and 200MiB of memory:
Total CPU reserved: 5 × 0.1 = 0.5 (in the Pod specification, you'll write the quantity `500m`)
Total memory reserved: 5 × 200MiB = 1GiB (in the Pod specification, you'll write `1 Gi`)

To scale the Deployment, adjust the number of replicas based on your cluster's size and expected workload:

```
kubectl scale deployment capacity-reservation --replicas=5
```

Verify the scaling:

```
kubectl get deployment capacity-reservation
```

The output should reflect the updated number of replicas:

```
NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
capacity-reservation   5/5     5            5           2m
```

> **Note:**
> Some autoscalers, notably [Karpenter](/docs/concepts/cluster-administration/cluster-autoscaling/#autoscaler-karpenter),
> treat preferred affinity rules as hard rules when considering node scaling.
> If you use Karpenter or another node autoscaler that uses the same heuristic,
> the replica count you set here also sets a minimum node count for your cluster.

## What's next

* Learn more about [PriorityClasses](/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass) and how they affect pod scheduling.
* Explore [node autoscaling](/docs/concepts/cluster-administration/cluster-autoscaling/) to dynamically adjust your cluster's size based on workload demands.
* Understand [Pod preemption](/docs/concepts/scheduling-eviction/pod-priority-preemption/), a
  key mechanism for Kubernetes to handle resource contention. The same page covers *eviction*,
  which is less relevant to the placeholder Pod approach, but is also a mechanism for Kubernetes
  to react when resources are contended.

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
