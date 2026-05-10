# Share a Cluster with Namespaces

This page shows how to view, work in, and delete [namespaces](/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster.").
The page also shows how to use Kubernetes namespaces to subdivide your cluster.

## Before you begin

* Have an [existing Kubernetes cluster](/docs/setup/).
* You have a basic understanding of Kubernetes [Pods](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster."),
  [Services](/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service."), and
  [Deployments](/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster.").

## Viewing namespaces

List the current namespaces in a cluster using:

```
kubectl get namespaces
```

```
NAME              STATUS   AGE
default           Active   11d
kube-node-lease   Active   11d
kube-public       Active   11d
kube-system       Active   11d
```

Kubernetes starts with four initial namespaces:

* `default` The default namespace for objects with no other namespace
* `kube-node-lease` This namespace holds [Lease](/docs/concepts/architecture/leases/) objects associated with each node. Node leases allow the kubelet to send [heartbeats](/docs/concepts/architecture/nodes/#heartbeats) so that the control plane can detect node failure.
* `kube-public` This namespace is created automatically and is readable by all users
  (including those not authenticated). This namespace is mostly reserved for cluster usage,
  in case that some resources should be visible and readable publicly throughout the whole cluster.
  The public aspect of this namespace is only a convention, not a requirement.
* `kube-system` The namespace for objects created by the Kubernetes system

You can also get the summary of a specific namespace using:

```
kubectl get namespaces <name>
```

Or you can get detailed information with:

```
kubectl describe namespaces <name>
```

```
Name:           default
Labels:         <none>
Annotations:    <none>
Status:         Active

No resource quota.

Resource Limits
 Type       Resource    Min Max Default
 ----               --------    --- --- ---
 Container          cpu         -   -   100m
```

Note that these details show both resource quota (if present) as well as resource limit ranges.

Resource quota tracks aggregate usage of resources in the Namespace and allows cluster operators
to define *Hard* resource usage limits that a Namespace may consume.

A limit range defines min/max constraints on the amount of resources a single entity can consume in
a Namespace.

See [Admission control: Limit Range](https://git.k8s.io/design-proposals-archive/resource-management/admission_control_limit_range.md)

A namespace can be in one of two phases:

* `Active` the namespace is in use
* `Terminating` the namespace is being deleted, and can not be used for new objects

For more details, see [Namespace](/docs/reference/kubernetes-api/cluster-resources/namespace-v1/)
in the API reference.

## Creating a new namespace

> **Note:**
> Avoid creating namespace with prefix `kube-`, since it is reserved for Kubernetes system namespaces.

Create a new YAML file called `my-namespace.yaml` with the contents:

```
apiVersion: v1
kind: Namespace
metadata:
  name: <insert-namespace-name-here>
```

Then run:

```
kubectl create -f ./my-namespace.yaml
```

Alternatively, you can create namespace using below command:

```
kubectl create namespace <insert-namespace-name-here>
```

The name of your namespace must be a valid
[DNS label](/docs/concepts/overview/working-with-objects/names/#dns-label-names).

There's an optional field `finalizers`, which allows observables to purge resources whenever the
namespace is deleted. Keep in mind that if you specify a nonexistent finalizer, the namespace will
be created but will get stuck in the `Terminating` state if the user tries to delete it.

More information on `finalizers` can be found in the namespace
[design doc](https://git.k8s.io/design-proposals-archive/architecture/namespaces.md#finalizers).

## Deleting a namespace

Delete a namespace with

```
kubectl delete namespaces <insert-some-namespace-name>
```

> **Warning:**
> This deletes *everything* under the namespace!

This delete is asynchronous, so for a time you will see the namespace in the `Terminating` state.

## Subdividing your cluster using Kubernetes namespaces

By default, a Kubernetes cluster will instantiate a default namespace when provisioning the
cluster to hold the default set of Pods, Services, and Deployments used by the cluster.

Assuming you have a fresh cluster, you can introspect the available namespaces by doing the following:

```
kubectl get namespaces
```

```
NAME      STATUS    AGE
default   Active    13m
```

### Create new namespaces

For this exercise, we will create two additional Kubernetes namespaces to hold our content.

In a scenario where an organization is using a shared Kubernetes cluster for development and
production use cases:

* The development team would like to maintain a space in the cluster where they can get a view on
  the list of Pods, Services, and Deployments they use to build and run their application.
  In this space, Kubernetes resources come and go, and the restrictions on who can or cannot modify
  resources are relaxed to enable agile development.
* The operations team would like to maintain a space in the cluster where they can enforce strict
  procedures on who can or cannot manipulate the set of Pods, Services, and Deployments that run
  the production site.

One pattern this organization could follow is to partition the Kubernetes cluster into two
namespaces: `development` and `production`. Let's create two new namespaces to hold our work.

Create the `development` namespace using kubectl:

```
kubectl create -f https://k8s.io/examples/admin/namespace-dev.json
```

And then let's create the `production` namespace using kubectl:

```
kubectl create -f https://k8s.io/examples/admin/namespace-prod.json
```

To be sure things are right, list all of the namespaces in our cluster.

```
kubectl get namespaces --show-labels
```

```
NAME          STATUS    AGE       LABELS
default       Active    32m       <none>
development   Active    29s       name=development
production    Active    23s       name=production
```

### Create pods in each namespace

A Kubernetes namespace provides the scope for Pods, Services, and Deployments in the cluster.
Users interacting with one namespace do not see the content in another namespace.
To demonstrate this, let's spin up a simple Deployment and Pods in the `development` namespace.

```
kubectl create deployment snowflake \
  --image=registry.k8s.io/serve_hostname \
  -n=development --replicas=2
```

We have created a deployment whose replica size is 2 that is running the pod called `snowflake`
with a basic container that serves the hostname.

```
kubectl get deployment -n=development
```

```
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
snowflake    2/2     2            2           2m
```

```
kubectl get pods -l app=snowflake -n=development
```

```
NAME                         READY     STATUS    RESTARTS   AGE
snowflake-3968820950-9dgr8   1/1       Running   0          2m
snowflake-3968820950-vgc4n   1/1       Running   0          2m
```

And this is great, developers are able to do what they want, and they do not have to worry about
affecting content in the `production` namespace.

Let's switch to the `production` namespace and show how resources in one namespace are hidden from
the other. The `production` namespace should be empty, and the following commands should return nothing.

```
kubectl get deployment -n=production
kubectl get pods -n=production
```

Production likes to run cattle, so let's create some cattle pods.

```
kubectl create deployment cattle --image=registry.k8s.io/serve_hostname -n=production
kubectl scale deployment cattle --replicas=5 -n=production

kubectl get deployment -n=production
```

```
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
cattle       5/5     5            5           10s
```

```
kubectl get pods -l app=cattle -n=production
```

```
NAME                      READY     STATUS    RESTARTS   AGE
cattle-2263376956-41xy6   1/1       Running   0          34s
cattle-2263376956-kw466   1/1       Running   0          34s
cattle-2263376956-n4v97   1/1       Running   0          34s
cattle-2263376956-p5p3i   1/1       Running   0          34s
cattle-2263376956-sxpth   1/1       Running   0          34s
```

At this point, it should be clear that the resources users create in one namespace are hidden from
the other namespace.

As the policy support in Kubernetes evolves, we will extend this scenario to show how you can provide different
authorization rules for each namespace.

## Understanding the motivation for using namespaces

A single cluster should be able to satisfy the needs of multiple users or groups of users
(henceforth in this document a *user community*).

Kubernetes *namespaces* help different projects, teams, or customers to share a Kubernetes cluster.

It does this by providing the following:

1. A scope for [names](/docs/concepts/overview/working-with-objects/names/).
2. A mechanism to attach authorization and policy to a subsection of the cluster.

Use of multiple namespaces is optional.

Each user community wants to be able to work in isolation from other communities.
Each user community has its own:

1. resources (pods, services, replication controllers, etc.)
2. policies (who can or cannot perform actions in their community)
3. constraints (this community is allowed this much quota, etc.)

A cluster operator may create a Namespace for each unique user community.

The Namespace provides a unique scope for:

1. named resources (to avoid basic naming collisions)
2. delegated management authority to trusted users
3. ability to limit community resource consumption

Use cases include:

1. As a cluster operator, I want to support multiple user communities on a single cluster.
2. As a cluster operator, I want to delegate authority to partitions of the cluster to trusted
   users in those communities.
3. As a cluster operator, I want to limit the amount of resources each community can consume in
   order to limit the impact to other communities using the cluster.
4. As a cluster user, I want to interact with resources that are pertinent to my user community in
   isolation of what other user communities are doing on the cluster.

## Understanding namespaces and DNS

When you create a [Service](/docs/concepts/services-networking/service/), it creates a corresponding
[DNS entry](/docs/concepts/services-networking/dns-pod-service/).
This entry is of the form `<service-name>.<namespace-name>.svc.cluster.local`, which means
that if a container uses `<service-name>` it will resolve to the service which
is local to a namespace. This is useful for using the same configuration across
multiple namespaces such as Development, Staging and Production. If you want to reach
across namespaces, you need to use the fully qualified domain name (FQDN).

## What's next

* Learn more about [setting the namespace preference](/docs/concepts/overview/working-with-objects/namespaces/#setting-the-namespace-preference).
* Learn more about [setting the namespace for a request](/docs/concepts/overview/working-with-objects/namespaces/#setting-the-namespace-for-a-request)
* See [namespaces design](https://git.k8s.io/design-proposals-archive/architecture/namespaces.md).

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
