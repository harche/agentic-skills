# Downward API

There are two ways to expose Pod and container fields to a running container: environment variables, and as files that are populated by a special volume type. Together, these two ways of exposing Pod and container fields are called the downward API.

It is sometimes useful for a container to have information about itself, without
being overly coupled to Kubernetes. The *downward API* allows containers to consume
information about themselves or the cluster without using the Kubernetes client
or API server.

An example is an existing application that assumes a particular well-known
environment variable holds a unique identifier. One possibility is to wrap the
application, but that is tedious and error-prone, and it violates the goal of low
coupling. A better option would be to use the Pod's name as an identifier, and
inject the Pod's name into the well-known environment variable.

In Kubernetes, there are two ways to expose Pod and container fields to a running container:

* as [environment variables](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)
* as [files in a `downwardAPI` volume](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)

Together, these two ways of exposing Pod and container fields are called the
*downward API*.

## Available fields

Only some Kubernetes API fields are available through the downward API. This
section lists which fields you can make available.

You can pass information from available Pod-level fields using `fieldRef`.
At the API level, the `spec` for a Pod always defines at least one
[Container](/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container).
You can pass information from available Container-level fields using
`resourceFieldRef`.

### Information available via `fieldRef`

For some Pod-level fields, you can provide them to a container either as
an environment variable or using a `downwardAPI` volume. The fields available
via either mechanism are:

`metadata.name`
:   the pod's name

`metadata.namespace`
:   the pod's [namespace](/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster.")

`metadata.uid`
:   the pod's unique ID

`metadata.annotations['<KEY>']`
:   the value of the pod's [annotation](/docs/concepts/overview/working-with-objects/annotations "A key-value pair that is used to attach arbitrary non-identifying metadata to objects.") named `<KEY>` (for example, `metadata.annotations['myannotation']`)

`metadata.labels['<KEY>']`
:   the text value of the pod's [label](/docs/concepts/overview/working-with-objects/labels "Tags objects with identifying attributes that are meaningful and relevant to users.") named `<KEY>` (for example, `metadata.labels['mylabel']`)

The following information is available through environment variables
**but not as a downwardAPI volume fieldRef**:

`spec.serviceAccountName`
:   the name of the pod's [service account](/docs/tasks/configure-pod-container/configure-service-account/ "Provides an identity for processes that run in a Pod.")

`spec.nodeName`
:   the name of the [node](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") where the Pod is executing

`status.hostIP`
:   the primary IP address of the node to which the Pod is assigned

`status.hostIPs`
:   the IP addresses is a dual-stack version of `status.hostIP`, the first is always the same as `status.hostIP`.

`status.podIP`
:   the pod's primary IP address (usually, its IPv4 address)

`status.podIPs`
:   the IP addresses is a dual-stack version of `status.podIP`, the first is always the same as `status.podIP`

The following information is available through a `downwardAPI` volume
`fieldRef`, **but not as environment variables**:

`metadata.labels`
:   all of the pod's labels, formatted as `label-key="escaped-label-value"` with one label per line

`metadata.annotations`
:   all of the pod's annotations, formatted as `annotation-key="escaped-annotation-value"` with one annotation per line

### Information available via `resourceFieldRef`

These container-level fields allow you to provide information about
[requests and limits](/docs/concepts/configuration/manage-resources-containers/#requests-and-limits)
for resources such as CPU and memory.

> **Note:**
> FEATURE STATE:
> `Kubernetes v1.33 [beta]`(enabled by default)
>
> Container CPU and memory resources can be resized while the container is running.
> If this happens, a downward API volume will be updated,
> but environment variables will not be updated unless the container restarts.
> See [Resize CPU and Memory Resources assigned to Containers](/docs/tasks/configure-pod-container/resize-container-resources/)
> for more details.

`resource: limits.cpu`
:   A container's CPU limit

`resource: requests.cpu`
:   A container's CPU request

`resource: limits.memory`
:   A container's memory limit

`resource: requests.memory`
:   A container's memory request

`resource: limits.hugepages-*`
:   A container's hugepages limit

`resource: requests.hugepages-*`
:   A container's hugepages request

`resource: limits.ephemeral-storage`
:   A container's ephemeral-storage limit

`resource: requests.ephemeral-storage`
:   A container's ephemeral-storage request

#### Fallback information for resource limits

If CPU and memory limits are not specified for a container, and you use the
downward API to try to expose that information, then the
kubelet defaults to exposing the maximum allocatable value for CPU and memory
based on the [node allocatable](/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable)
calculation.

## What's next

You can read about [`downwardAPI` volumes](/docs/concepts/storage/volumes/#downwardapi).

You can try using the downward API to expose container- or Pod-level information:

* as [environment variables](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)
* as [files in `downwardAPI` volume](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)

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
