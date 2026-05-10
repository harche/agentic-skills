This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/concepts/scheduling-eviction/).

# Scheduling, Preemption and Eviction

* 1: [Kubernetes Scheduler](#pg-598f36d691ab197f9d995784574b0a12)
* 2: [Assigning Pods to Nodes](#pg-21169f516071aea5d16734a4c27789a5)
* 3: [Pod Overhead](#pg-da22fe2278df236f71efbe672f392677)
* 4: [Pod Scheduling Readiness](#pg-d9483841860fd8701aee18ffb0759aef)
* 5: [Pod Topology Spread Constraints](#pg-6b8c85a6a88f4a81e6b79e197c293c31)
* 6: [Taints and Tolerations](#pg-ede4960b56a3529ee0bfe7c8fe2d09a5)
* 7: [Scheduling Framework](#pg-602208c95fe7b1f1170310ce993f5814)
* 8: [Dynamic Resource Allocation](#pg-132fdff5faea3a27f280f3acdf4f8b7d)
* 9: [Scheduler Performance Tuning](#pg-d9574a30fcbc631b0d2a57850e161e89)
* 10: [Resource Bin Packing](#pg-961126cd43559012893979e568396a49)
* 11: [Pod Priority and Preemption](#pg-60e5a2861609e0848d58ce8bf99c4a31)
* 12: [Node-pressure Eviction](#pg-78e0431b4b7516092662a7c289cbb304)
* 13: [API-initiated Eviction](#pg-b87723bf81b079042860f0ebd37b0a64)

In Kubernetes, scheduling refers to making sure that [Pods](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.")
are matched to [Nodes](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") so that the
[kubelet](/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") can run them. Preemption
is the process of terminating Pods with lower [Priority](/docs/concepts/scheduling-eviction/pod-priority-preemption/#pod-priority "Pod Priority indicates the importance of a Pod relative to other Pods.")
so that Pods with higher Priority can schedule on Nodes. Eviction is the process
of terminating one or more Pods on Nodes.

## Scheduling

* [Kubernetes Scheduler](/docs/concepts/scheduling-eviction/kube-scheduler/)
* [Assigning Pods to Nodes](/docs/concepts/scheduling-eviction/assign-pod-node/)
* [Pod Overhead](/docs/concepts/scheduling-eviction/pod-overhead/)
* [Pod Topology Spread Constraints](/docs/concepts/scheduling-eviction/topology-spread-constraints/)
* [Taints and Tolerations](/docs/concepts/scheduling-eviction/taint-and-toleration/)
* [Scheduling Framework](/docs/concepts/scheduling-eviction/scheduling-framework/)
* [Dynamic Resource Allocation](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)
* [Scheduler Performance Tuning](/docs/concepts/scheduling-eviction/scheduler-perf-tuning/)
* [Resource Bin Packing for Extended Resources](/docs/concepts/scheduling-eviction/resource-bin-packing/)
* [Pod Scheduling Readiness](/docs/concepts/scheduling-eviction/pod-scheduling-readiness/)
* [Descheduler](https://github.com/kubernetes-sigs/descheduler#descheduler-for-kubernetes)

## Pod Disruption

[Pod disruption](/docs/concepts/workloads/pods/disruptions/) is the process by which
Pods on Nodes are terminated either voluntarily or involuntarily.

Voluntary disruptions are started intentionally by application owners or cluster
administrators. Involuntary disruptions are unintentional and can be triggered by
unavoidable issues like Nodes running out of [resources](/docs/reference/glossary/?all=true#term-infrastructure-resource "A defined amount of infrastructure available for consumption (CPU, memory, etc)."),
or by accidental deletions.

* [Pod Priority and Preemption](/docs/concepts/scheduling-eviction/pod-priority-preemption/)
* [Node-pressure Eviction](/docs/concepts/scheduling-eviction/node-pressure-eviction/)
* [API-initiated Eviction](/docs/concepts/scheduling-eviction/api-eviction/)
