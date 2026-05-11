This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/concepts/workloads/).

# Workloads

Understand Pods, the smallest deployable compute object in Kubernetes, and the higher-level abstractions that help you to run them.

* 1: [Pods](#pg-4d68b0ccf9c683e6368ffdcc40c838d4)

+ 1.1: [Pod Lifecycle](#pg-c3c2b9cf30915ec9d46c147201da3332)
+ 1.2: [Init Containers](#pg-1ccbd4eeded6ab138d98b59175bd557e)
+ 1.3: [Sidecar Containers](#pg-31b32aaff870448be05e247a95c17a57)
+ 1.4: [Ephemeral Containers](#pg-53a1005011e1bda2ce81819aad7c8b32)
+ 1.5: [Disruptions](#pg-4aaf43c715cd764bc8ed4436f3537e68)
+ 1.6: [Pod Hostname](#pg-268190c91963ce121c0de5a4894db118)
+ 1.7: [Pod Quality of Service Classes](#pg-a77cbc10142789b7e0f78a222546ed1e)
+ 1.8: [User Namespaces](#pg-868be91dc02aab6dc768102e4abf5eff)
+ 1.9: [Downward API](#pg-420713565efe2f940e277f6b4824ad9a)

* 2: [Workload Management](#pg-89637410cacae45a36ab1cc278c482eb)

+ 2.1: [Deployments](#pg-a2dc0393e0c4079e1c504b6429844e86)
+ 2.2: [ReplicaSet](#pg-d459b930218774655fa7fd1620625539)
+ 2.3: [StatefulSets](#pg-6d72299952c37ca8cc61b416e5bdbcd4)
+ 2.4: [DaemonSet](#pg-41600eb8b6631c88848156f381e9d588)
+ 2.5: [Jobs](#pg-cc7cc3c4907039d9f863162e20bfbbef)
+ 2.6: [Automatic Cleanup for Finished Jobs](#pg-4de50a37ebb6f2340484192126cb7a04)
+ 2.7: [CronJob](#pg-2e4cec01c525b45eccd6010e21cc76d9)
+ 2.8: [ReplicationController](#pg-27f1331d515d95f76aa1156088b4ad91)

* 3: [Autoscaling Workloads](#pg-57dc30ff77a6b2871e15ed60c0bf61f0)
* 4: [Managing Workloads](#pg-5921bd285837eed0aec7451e57f03654)
* 5: [Vertical Pod Autoscaling](#pg-9452c7522847e65b263c3433561ab637)

A workload is an application running on Kubernetes.
Whether your workload is a single component or several that work together, on Kubernetes you run
it inside a set of [*pods*](/docs/concepts/workloads/pods/).
In Kubernetes, a Pod represents a set of running
[containers](/docs/concepts/containers/ "A lightweight and portable executable image that contains software and all of its dependencies.") on your cluster.

Kubernetes pods have a [defined lifecycle](/docs/concepts/workloads/pods/pod-lifecycle/).
For example, once a pod is running in your cluster then a critical fault on the
[node](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") where that pod is running means that
all the pods on that node fail. Kubernetes treats that level of failure as final: you
would need to create a new Pod to recover, even if the node later becomes healthy.

However, to make life considerably easier, you don't need to manage each Pod directly.
Instead, you can use *workload resources* that manage a set of pods on your behalf.
These resources configure [controllers](/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.")
that make sure the right number of the right kind of pod are running, to match the state
you specified.

Kubernetes provides several built-in workload resources:

* [Deployment](/docs/concepts/workloads/controllers/deployment/) and [ReplicaSet](/docs/concepts/workloads/controllers/replicaset/)
  (replacing the legacy resource
  [ReplicationController](/docs/reference/glossary/?all=true#term-replication-controller "A (deprecated) API object that manages a replicated application.")).
  Deployment is a good fit for managing a stateless application workload on your cluster,
  where any Pod in the Deployment is interchangeable and can be replaced if needed.
* [StatefulSet](/docs/concepts/workloads/controllers/statefulset/) lets you
  run one or more related Pods that do track state somehow. For example, if your workload
  records data persistently, you can run a StatefulSet that matches each Pod with a
  [PersistentVolume](/docs/concepts/storage/persistent-volumes/). Your code, running in the
  Pods for that StatefulSet, can replicate data to other Pods in the same StatefulSet
  to improve overall resilience.
* [DaemonSet](/docs/concepts/workloads/controllers/daemonset/) defines Pods that provide
  facilities that are local to nodes.
  Every time you add a node to your cluster that matches the specification in a DaemonSet,
  the control plane schedules a Pod for that DaemonSet onto the new node.
  Each pod in a DaemonSet performs a job similar to a system daemon on a classic Unix / POSIX
  server. A DaemonSet might be fundamental to the operation of your cluster, such as
  a plugin to run [cluster networking](/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-network-model),
  it might help you to manage the node,
  or it could provide optional behavior that enhances the container platform you are running.
* [Job](/docs/concepts/workloads/controllers/job/) and
  [CronJob](/docs/concepts/workloads/controllers/cron-jobs/) provide different ways to
  define tasks that run to completion and then stop.
  You can use a [Job](/docs/concepts/workloads/controllers/job/) to
  define a task that runs to completion, just once. You can use a
  [CronJob](/docs/concepts/workloads/controllers/cron-jobs/) to run
  the same Job multiple times according a schedule.

In the wider Kubernetes ecosystem, you can find third-party workload resources that provide
additional behaviors. Using a
[custom resource definition](/docs/concepts/extend-kubernetes/api-extension/custom-resources/),
you can add in a third-party workload resource if you want a specific behavior that's not part
of Kubernetes' core. For example, if you wanted to run a group of Pods for your application but
stop work unless *all* the Pods are available (perhaps for some high-throughput distributed task),
then you can implement or install an extension that does provide that feature.

## What's next

As well as reading about each API kind for workload management, you can read how to
do specific tasks:

* [Run a stateless application using a Deployment](/docs/tasks/run-application/run-stateless-application-deployment/)
* Run a stateful application either as a [single instance](/docs/tasks/run-application/run-single-instance-stateful-application/)
  or as a [replicated set](/docs/tasks/run-application/run-replicated-stateful-application/)
* [Run automated tasks with a CronJob](/docs/tasks/job/automated-tasks-with-cron-jobs/)

To learn about Kubernetes' mechanisms for separating code from configuration,
visit [Configuration](/docs/concepts/configuration/).

There are two supporting concepts that provide backgrounds about how Kubernetes manages pods
for applications:

* [Garbage collection](/docs/concepts/architecture/garbage-collection/) tidies up objects
  from your cluster after their *owning resource* has been removed.
* The [*time-to-live after finished* controller](/docs/concepts/workloads/controllers/ttlafterfinished/)
  removes Jobs once a defined time has passed since they completed.

Once your application is running, you might want to make it available on the internet as
a [Service](/docs/concepts/services-networking/service/) or, for web application only,
using an [Ingress](/docs/concepts/services-networking/ingress/).
