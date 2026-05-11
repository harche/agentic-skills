This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/concepts/workloads/controllers/).

# Workload Management

* 1: [Deployments](#pg-a2dc0393e0c4079e1c504b6429844e86)
* 2: [ReplicaSet](#pg-d459b930218774655fa7fd1620625539)
* 3: [StatefulSets](#pg-6d72299952c37ca8cc61b416e5bdbcd4)
* 4: [DaemonSet](#pg-41600eb8b6631c88848156f381e9d588)
* 5: [Jobs](#pg-cc7cc3c4907039d9f863162e20bfbbef)
* 6: [Automatic Cleanup for Finished Jobs](#pg-4de50a37ebb6f2340484192126cb7a04)
* 7: [CronJob](#pg-2e4cec01c525b45eccd6010e21cc76d9)
* 8: [ReplicationController](#pg-27f1331d515d95f76aa1156088b4ad91)

Kubernetes provides several built-in APIs for declarative management of your
[workloads](/docs/concepts/workloads/ "A workload is an application running on Kubernetes.")
and the components of those workloads.

Ultimately, your applications run as containers inside
[Pods](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster."); however, managing individual
Pods would be a lot of effort. For example, if a Pod fails, you probably want to
run a new Pod to replace it. Kubernetes can do that for you.

You use the Kubernetes API to create a workload
[object](/docs/concepts/overview/working-with-objects/#kubernetes-objects "An entity in the Kubernetes system, representing part of the state of your cluster.") that represents a higher abstraction level
than a Pod, and then the Kubernetes
[control plane](/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.") automatically manages
Pod objects on your behalf, based on the specification for the workload object you defined.

The built-in APIs for managing workloads are:

[Deployment](/docs/concepts/workloads/controllers/deployment/) (and, indirectly, [ReplicaSet](/docs/concepts/workloads/controllers/replicaset/)),
the most common way to run an application on your cluster.
Deployment is a good fit for managing a stateless application workload on your cluster, where
any Pod in the Deployment is interchangeable and can be replaced if needed.
(Deployments are a replacement for the legacy
[ReplicationController](/docs/reference/glossary/?all=true#term-replication-controller "A (deprecated) API object that manages a replicated application.") API).

A [StatefulSet](/docs/concepts/workloads/controllers/statefulset/) lets you
manage one or more Pods – all running the same application code – where the Pods rely
on having a distinct identity. This is different from a Deployment where the Pods are
expected to be interchangeable.
The most common use for a StatefulSet is to be able to make a link between its Pods and
their persistent storage. For example, you can run a StatefulSet that associates each Pod
with a [PersistentVolume](/docs/concepts/storage/persistent-volumes/). If one of the Pods
in the StatefulSet fails, Kubernetes makes a replacement Pod that is connected to the
same PersistentVolume.

A [DaemonSet](/docs/concepts/workloads/controllers/daemonset/) defines Pods that provide
facilities that are local to a specific [node](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.");
for example, a driver that lets containers on that node access a storage system. You use a DaemonSet
when the driver, or other node-level service, has to run on the node where it's useful.
Each Pod in a DaemonSet performs a role similar to a system daemon on a classic Unix / POSIX
server.
A DaemonSet might be fundamental to the operation of your cluster,
such as a plugin to let that node access
[cluster networking](/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-network-model),
it might help you to manage the node,
or it could provide less essential facilities that enhance the container platform you are running.
You can run DaemonSets (and their pods) across every node in your cluster, or across just a subset (for example,
only install the GPU accelerator driver on nodes that have a GPU installed).

You can use a [Job](/docs/concepts/workloads/controllers/job/) and / or
a [CronJob](/docs/concepts/workloads/controllers/cron-jobs/) to
define tasks that run to completion and then stop. A Job represents a one-off task,
whereas each CronJob repeats according to a schedule.

Other topics in this section:
