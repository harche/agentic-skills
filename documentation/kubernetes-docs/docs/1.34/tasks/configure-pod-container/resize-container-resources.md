# Resize CPU and Memory Resources assigned to Containers

FEATURE STATE:
`Kubernetes v1.33 [beta]`(enabled by default)

This page explains how to change the CPU and memory resource requests and limits
assigned to a container *without recreating the Pod*.

Traditionally, changing a Pod's resource requirements necessitated deleting the existing Pod
and creating a replacement, often managed by a [workload controller](/docs/concepts/workloads/controllers/).
In-place Pod Resize allows changing the CPU/memory allocation of container(s) within a running Pod
while potentially avoiding application disruption.

**Key Concepts:**

* **Desired Resources:** A container's `spec.containers[*].resources` represent
  the *desired* resources for the container, and are mutable for CPU and memory.
* **Actual Resources:** The `status.containerStatuses[*].resources` field
  reflects the resources *currently configured* for a running container.
  For containers that haven't started or were restarted,
  it reflects the resources allocated upon their next start.
* **Triggering a Resize:** You can request a resize by updating the desired `requests`
  and `limits` in the Pod's specification.
  This is typically done using `kubectl patch`, `kubectl apply`, or `kubectl edit`
  targeting the Pod's `resize` subresource.
  When the desired resources don't match the allocated resources,
  the Kubelet will attempt to resize the container.
* **Allocated Resources (Advanced):**
  The `status.containerStatuses[*].allocatedResources` field tracks resource values
  confirmed by the Kubelet, primarily used for internal scheduling logic.
  For most monitoring and validation purposes, focus on `status.containerStatuses[*].resources`.

If a node has pods with a pending or incomplete resize (see [Pod Resize Status](#pod-resize-status) below),
the [scheduler](/docs/reference/command-line-tools-reference/kube-scheduler/ "Control plane component that watches for newly created pods with no assigned node, and selects a node for them to run on.") uses
the *maximum* of a container's desired requests, allocated requests,
and actual requests from the status when making scheduling decisions.

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

Your Kubernetes server must be at or later than version 1.33.

To check the version, enter `kubectl version`.

The `InPlacePodVerticalScaling` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/)
must be enabled
for your control plane and for all nodes in your cluster.

The `kubectl` client version must be at least v1.32 to use the `--subresource=resize` flag.

## Pod resize status

The Kubelet updates the Pod's status conditions to indicate the state of a resize request:

* `type: PodResizePending`: The Kubelet cannot immediately grant the request.
  The `message` field provides an explanation of why.
  + `reason: Infeasible`: The requested resize is impossible on the current node
    (for example, requesting more resources than the node has).
  + `reason: Deferred`: The requested resize is currently not possible,
    but might become feasible later (for example if another pod is removed).
    The Kubelet will retry the resize.
* `type: PodResizeInProgress`: The Kubelet has accepted the resize and allocated resources,
  but the changes are still being applied.
  This is usually brief but might take longer depending on the resource type and runtime behavior.
  Any errors during actuation are reported in the `message` field (along with `reason: Error`).

### How kubelet retries Deferred resizes

If the requested resize is *Deferred*, the kubelet will periodically re-attempt the resize,
for example when another pod is removed or scaled down. If there are multiple deferred
resizes, they are retried according to the following priority:

* Pods with a higher Priority (based on PriorityClass) will have their resize request retried first.
* If two pods have the same Priority, resize of guaranteed pods will be retried before the resize of burstable pods.
* If all else is the same, pods that have been in the Deferred state longer will be prioritized.

A higher priority resize being marked as pending will not block the remaining pending resizes from being attempted;
all remaining pending resizes will still be retried even if a higher-priority resize gets deferred again.

### Leveraging `observedGeneration` Fields

FEATURE STATE:
`Kubernetes v1.34 [beta]`(enabled by default)

* The top-level `status.observedGeneration` field shows the `metadata.generation` corresponding to the latest pod specification that the kubelet has acknowledged. You can use this to determine the most recent resize request the kubelet has processed.
* In the `PodResizeInProgress` condition, the `conditions[].observedGeneration` field indicates the `metadata.generation` of the podSpec when the current in-progress resize was initiated.
* In the `PodResizePending` condition, the `conditions[].observedGeneration` field indicates the `metadata.generation` of the podSpec when the pending resize's allocation was last attempted.

## Container resize policies

You can control whether a container should be restarted when resizing
by setting `resizePolicy` in the container specification.
This allows fine-grained control based on resource type (CPU or memory).

```
    resizePolicy:
    - resourceName: cpu
      restartPolicy: NotRequired
    - resourceName: memory
      restartPolicy: RestartContainer
```

* `NotRequired`: (Default) Apply the resource change to the running container without restarting it.
* `RestartContainer`: Restart the container to apply the new resource values.
  This is often necessary for memory changes because many applications
  and runtimes cannot adjust their memory allocation dynamically.

If `resizePolicy[*].restartPolicy` is not specified for a resource, it defaults to `NotRequired`.

> **Note:**
> If a Pod's overall `restartPolicy` is `Never`, then any container `resizePolicy` must be `NotRequired` for all resources.
> You cannot configure a resize policy that would require a restart in such Pods.

**Example Scenario:**

Consider a container configured with `restartPolicy: NotRequired` for CPU and `restartPolicy: RestartContainer` for memory.

* If only CPU resources are changed, the container is resized in-place.
* If only memory resources are changed, the container is restarted.
* If *both* CPU and memory resources are changed simultaneously, the container is restarted (due to the memory policy).

## Limitations

For Kubernetes 1.34, resizing pod resources in-place has the following limitations:

* **Resource Types:** Only CPU and memory resources can be resized.
* **Memory Decrease:** If the memory resize restart policy is `NotRequired` (or unspecified), the kubelet will make a
  best-effort attempt to prevent oom-kills when decreasing memory limits, but doesn't provide any guarantees.
  Before decreasing container memory limits, if memory usage exceeds the requested limit, the resize will be skipped
  and the status will remain in an "In Progress" state. This is considered best-effort because it is still subject
  to a race condition where memory usage may spike right after the check is performed.
* **QoS Class:** The Pod's original [Quality of Service (QoS) class](/docs/concepts/workloads/pods/pod-qos/)
  (Guaranteed, Burstable, or BestEffort) is determined at creation and **cannot** be changed by a resize.
  The resized resource values must still adhere to the rules of the original QoS class:
  + *Guaranteed*: Requests must continue to equal limits for both CPU and memory after resizing.
  + *Burstable*: Requests and limits cannot become equal for *both* CPU and memory simultaneously
    (as this would change it to Guaranteed).
  + *BestEffort*: Resource requirements (`requests` or `limits`) cannot be added
    (as this would change it to Burstable or Guaranteed).
* **Container Types:** Non-restartable [init containers](/docs/concepts/workloads/pods/init-containers/ "One or more initialization containers that must run to completion before any app containers run.") and
  [ephemeral containers](/docs/concepts/workloads/pods/ephemeral-containers/ "A type of container type that you can temporarily run inside a Pod") cannot be resized.
  [Sidecar containers](/docs/concepts/workloads/pods/sidecar-containers/) can be resized.
* **Resource Removal:** Resource requests and limits cannot be entirely removed once set;
  they can only be changed to different values.
* **Operating System:** Windows pods do not support in-place resize.
* **Node Policies:** Pods managed by [static CPU or Memory manager policies](/docs/tasks/administer-cluster/cpu-management-policies/)
  cannot be resized in-place.
* **Swap:** Pods utilizing [swap memory](/docs/concepts/architecture/nodes/#swap-memory) cannot resize memory requests
  unless the `resizePolicy` for memory is `RestartContainer`.

These restrictions might be relaxed in future Kubernetes versions.

## Example 1: Resizing CPU without restart

First, create a Pod designed for in-place CPU resize and restart-required memory resize.

[`pods/resource/pod-resize.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/resource/pod-resize.yaml)![](/images/copycode.svg "Copy pods/resource/pod-resize.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: resize-demo
spec:
  containers:
  - name: pause
    image: registry.k8s.io/pause:3.8
    resizePolicy:
    - resourceName: cpu
      restartPolicy: NotRequired # Default, but explicit here
    - resourceName: memory
      restartPolicy: RestartContainer
    resources:
      limits:
        memory: "200Mi"
        cpu: "700m"
      requests:
        memory: "200Mi"
        cpu: "700m"
```

Create the pod:

```
kubectl create -f pod-resize.yaml
```

This pod starts in the Guaranteed QoS class. Verify its initial state:

```
# Wait a moment for the pod to be running
kubectl get pod resize-demo --output=yaml
```

Observe the `spec.containers[0].resources` and `status.containerStatuses[0].resources`.
They should match the manifest (700m CPU, 200Mi memory). Note the `status.containerStatuses[0].restartCount` (should be 0).

Now, increase the CPU request and limit to `800m`. You use `kubectl patch` with the `--subresource resize` command line argument.

```
kubectl patch pod resize-demo --subresource resize --patch \
  '{"spec":{"containers":[{"name":"pause", "resources":{"requests":{"cpu":"800m"}, "limits":{"cpu":"800m"}}}]}}'

# Alternative methods:
# kubectl -n qos-example edit pod resize-demo --subresource resize
# kubectl -n qos-example apply -f <updated-manifest> --subresource resize --server-side
```

> **Note:**
> The `--subresource resize` command line argument requires `kubectl` client version v1.32.0 or later.
> Older versions will report an `invalid subresource` error.

Check the pod status again after patching:

```
kubectl get pod resize-demo --output=yaml --namespace=qos-example
```

You should see:

* `spec.containers[0].resources` now shows `cpu: 800m`.
* `status.containerStatuses[0].resources` also shows `cpu: 800m`, indicating the resize was successful on the node.
* `status.containerStatuses[0].restartCount` remains `0`, because the CPU `resizePolicy` was `NotRequired`.

## Example 2: Resizing memory with restart

Now, resize the memory for the *same* pod by increasing it to `300Mi`.
Since the memory `resizePolicy` is `RestartContainer`, the container is expected to restart.

```
kubectl patch pod resize-demo --subresource resize --patch \
  '{"spec":{"containers":[{"name":"pause", "resources":{"requests":{"memory":"300Mi"}, "limits":{"memory":"300Mi"}}}]}}'
```

Check the pod status shortly after patching:

```
kubectl get pod resize-demo --output=yaml
```

You should now observe:

* `spec.containers[0].resources` shows `memory: 300Mi`.
* `status.containerStatuses[0].resources` also shows `memory: 300Mi`.
* `status.containerStatuses[0].restartCount` has increased to `1` (or more, if restarts happened previously),
  indicating the container was restarted to apply the memory change.

## Troubleshooting: Infeasible resize request

Next, try requesting an unreasonable amount of CPU, such as 1000 full cores (written as `"1000"` instead of `"1000m"` for millicores), which likely exceeds node capacity.

```
# Attempt to patch with an excessively large CPU request
kubectl patch pod resize-demo --subresource resize --patch \
  '{"spec":{"containers":[{"name":"pause", "resources":{"requests":{"cpu":"1000"}, "limits":{"cpu":"1000"}}}]}}'
```

Query the Pod's details:

```
kubectl get pod resize-demo --output=yaml
```

You'll see changes indicating the problem:

* The `spec.containers[0].resources` reflects the *desired* state (`cpu: "1000"`).
* A condition with `type: PodResizePending` and `reason: Infeasible` was added to the Pod.
* The condition's `message` will explain why (`Node didn't have enough capacity: cpu, requested: 800000, capacity: ...`)
* Crucially, `status.containerStatuses[0].resources` will *still show the previous values* (`cpu: 800m`, `memory: 300Mi`),
  because the infeasible resize was not applied by the Kubelet.
* The `restartCount` will not have changed due to this failed attempt.

To fix this, you would need to patch the pod again with feasible resource values.

## Clean up

Delete the pod:

```
kubectl delete pod resize-demo
```

## What's next

### For application developers

* [Assign Memory Resources to Containers and Pods](/docs/tasks/configure-pod-container/assign-memory-resource/)
* [Assign CPU Resources to Containers and Pods](/docs/tasks/configure-pod-container/assign-cpu-resource/)
* [Assign Pod-level CPU and memory resources](/docs/tasks/configure-pod-container/assign-pod-level-resources/)

### For cluster administrators

* [Configure Default Memory Requests and Limits for a Namespace](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)
* [Configure Default CPU Requests and Limits for a Namespace](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)
* [Configure Minimum and Maximum Memory Constraints for a Namespace](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)
* [Configure Minimum and Maximum CPU Constraints for a Namespace](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)
* [Configure Memory and CPU Quotas for a Namespace](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)

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
