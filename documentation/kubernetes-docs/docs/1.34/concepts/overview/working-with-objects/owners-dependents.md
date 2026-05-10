# Owners and Dependents

In Kubernetes, some [objects](/docs/concepts/overview/working-with-objects/#kubernetes-objects "An entity in the Kubernetes system, representing part of the state of your cluster.") are
*owners* of other objects. For example, a
[ReplicaSet](/docs/concepts/workloads/controllers/replicaset/ "ReplicaSet ensures that a specified number of Pod replicas are running at one time") is the owner
of a set of Pods. These owned objects are *dependents* of their owner.

Ownership is different from the [labels and selectors](/docs/concepts/overview/working-with-objects/labels/)
mechanism that some resources also use. For example, consider a Service that
creates `EndpointSlice` objects. The Service uses [labels](/docs/concepts/overview/working-with-objects/labels "Tags objects with identifying attributes that are meaningful and relevant to users.") to allow the control plane to
determine which `EndpointSlice` objects are used for that Service. In addition
to the labels, each `EndpointSlice` that is managed on behalf of a Service has
an owner reference. Owner references help different parts of Kubernetes avoid
interfering with objects they don’t control.

## Owner references in object specifications

Dependent objects have a `metadata.ownerReferences` field that references their
owner object. A valid owner reference consists of the object name and a [UID](/docs/concepts/overview/working-with-objects/names "A Kubernetes systems-generated string to uniquely identify objects.")
within the same [namespace](/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster.") as the dependent object. Kubernetes sets the value of
this field automatically for objects that are dependents of other objects like
ReplicaSets, DaemonSets, Deployments, Jobs and CronJobs, and ReplicationControllers.
You can also configure these relationships manually by changing the value of
this field. However, you usually don't need to and can allow Kubernetes to
automatically manage the relationships.

Dependent objects also have an `ownerReferences.blockOwnerDeletion` field that
takes a boolean value and controls whether specific dependents can block garbage
collection from deleting their owner object. Kubernetes automatically sets this
field to `true` if a [controller](/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.")
(for example, the Deployment controller) sets the value of the
`metadata.ownerReferences` field. You can also set the value of the
`blockOwnerDeletion` field manually to control which dependents block garbage
collection.

A Kubernetes admission controller controls user access to change this field for
dependent resources, based on the delete permissions of the owner. This control
prevents unauthorized users from delaying owner object deletion.

> **Note:**
> Cross-namespace owner references are disallowed by design.
> Namespaced dependents can specify cluster-scoped or namespaced owners.
> A namespaced owner **must** exist in the same namespace as the dependent.
> If it does not, the owner reference is treated as absent, and the dependent
> is subject to deletion once all owners are verified absent.
>
> Cluster-scoped dependents can only specify cluster-scoped owners.
> In v1.20+, if a cluster-scoped dependent specifies a namespaced kind as an owner,
> it is treated as having an unresolvable owner reference, and is not able to be garbage collected.
>
> In v1.20+, if the garbage collector detects an invalid cross-namespace `ownerReference`,
> or a cluster-scoped dependent with an `ownerReference` referencing a namespaced kind, a warning Event
> with a reason of `OwnerRefInvalidNamespace` and an `involvedObject` of the invalid dependent is reported.
> You can check for that kind of Event by running
> `kubectl get events -A --field-selector=reason=OwnerRefInvalidNamespace`.

## Ownership and finalizers

When you tell Kubernetes to delete a resource, the API server allows the
managing controller to process any [finalizer rules](/docs/concepts/overview/working-with-objects/finalizers/)
for the resource. [Finalizers](/docs/concepts/overview/working-with-objects/finalizers/ "A namespaced key that tells Kubernetes to wait until specific conditions are met before it fully deletes an object marked for deletion.")
prevent accidental deletion of resources your cluster may still need to function
correctly. For example, if you try to delete a [PersistentVolume](/docs/concepts/storage/persistent-volumes/) that is still
in use by a Pod, the deletion does not happen immediately because the
`PersistentVolume` has the `kubernetes.io/pv-protection` finalizer on it.
Instead, the [volume](/docs/concepts/storage/volumes/) remains in the `Terminating` status until Kubernetes clears
the finalizer, which only happens after the `PersistentVolume` is no longer
bound to a Pod.

Kubernetes also adds finalizers to an owner resource when you use either
[foreground or orphan cascading deletion](/docs/concepts/architecture/garbage-collection/#cascading-deletion).
In foreground deletion, it adds the `foreground` finalizer so that the
controller must delete dependent resources that also have
`ownerReferences.blockOwnerDeletion=true` before it deletes the owner. If you
specify an orphan deletion policy, Kubernetes adds the `orphan` finalizer so
that the controller ignores dependent resources after it deletes the owner
object.

## What's next

* Learn more about [Kubernetes finalizers](/docs/concepts/overview/working-with-objects/finalizers/).
* Learn about [garbage collection](/docs/concepts/architecture/garbage-collection/).
* Read the API reference for [object metadata](/docs/reference/kubernetes-api/common-definitions/object-meta/#System).

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
