# API-initiated Eviction

API-initiated eviction is the process by which you use the [Eviction API](/docs/reference/generated/kubernetes-api/v1.34/#create-eviction-pod-v1-core)
to create an `Eviction` object that triggers graceful pod termination.

You can request eviction by calling the Eviction API directly, or programmatically
using a client of the [API server](/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API."), like the `kubectl drain` command. This
creates an `Eviction` object, which causes the API server to terminate the Pod.

API-initiated evictions respect your configured [`PodDisruptionBudgets`](/docs/tasks/run-application/configure-pdb/)
and [`terminationGracePeriodSeconds`](/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination).

Using the API to create an Eviction object for a Pod is like performing a
policy-controlled [`DELETE` operation](/docs/reference/kubernetes-api/workload-resources/pod-v1/#delete-delete-a-pod)
on the Pod.

## Calling the Eviction API

You can use a [Kubernetes language client](/docs/tasks/administer-cluster/access-cluster-api/#programmatic-access-to-the-api)
to access the Kubernetes API and create an `Eviction` object. To do this, you
POST the attempted operation, similar to the following example:

* policy/v1
  * policy/v1beta1

> **Note:**
> `policy/v1` Eviction is available in v1.22+. Use `policy/v1beta1` with prior releases.

```
{
  "apiVersion": "policy/v1",
  "kind": "Eviction",
  "metadata": {
    "name": "quux",
    "namespace": "default"
  }
}
```

> **Note:**
> Deprecated in v1.22 in favor of `policy/v1`

```
{
  "apiVersion": "policy/v1beta1",
  "kind": "Eviction",
  "metadata": {
    "name": "quux",
    "namespace": "default"
  }
}
```

Alternatively, you can attempt an eviction operation by accessing the API using
`curl` or `wget`, similar to the following example:

```
curl -v -H 'Content-type: application/json' https://your-cluster-api-endpoint.example/api/v1/namespaces/default/pods/quux/eviction -d @eviction.json
```

## How API-initiated eviction works

When you request an eviction using the API, the API server performs admission
checks and responds in one of the following ways:

* `200 OK`: the eviction is allowed, the `Eviction` subresource is created, and
  the Pod is deleted, similar to sending a `DELETE` request to the Pod URL.
* `429 Too Many Requests`: the eviction is not currently allowed because of the
  configured [PodDisruptionBudget](/docs/reference/glossary/?all=true#term-pod-disruption-budget "An object that limits the number of Pods of a replicated application that are down simultaneously from voluntary disruptions.").
  You may be able to attempt the eviction again later. You might also see this
  response because of API rate limiting.
* `500 Internal Server Error`: the eviction is not allowed because there is a
  misconfiguration, like if multiple PodDisruptionBudgets reference the same Pod.

If the Pod you want to evict isn't part of a workload that has a
PodDisruptionBudget, the API server always returns `200 OK` and allows the
eviction.

If the API server allows the eviction, the Pod is deleted as follows:

1. The `Pod` resource in the API server is updated with a deletion timestamp,
   after which the API server considers the `Pod` resource to be terminated. The
   `Pod` resource is also marked with the configured grace period.
2. The [kubelet](/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") on the node where the local Pod is running notices that the `Pod`
   resource is marked for termination and starts to gracefully shut down the
   local Pod.
3. While the kubelet is shutting the Pod down, the control plane removes the Pod
   from [EndpointSlice](/docs/concepts/services-networking/endpoint-slices/ "EndpointSlices track the IP addresses of Pods for Services.")
   objects. As a result, controllers no longer consider the Pod as a valid object.
4. After the grace period for the Pod expires, the kubelet forcefully terminates
   the local Pod.
5. The kubelet tells the API server to remove the `Pod` resource.
6. The API server deletes the `Pod` resource.

## Troubleshooting stuck evictions

In some cases, your applications may enter a broken state, where the Eviction
API will only return `429` or `500` responses until you intervene. This can
happen if, for example, a ReplicaSet creates pods for your application but new
pods do not enter a `Ready` state. You may also notice this behavior in cases
where the last evicted Pod had a long termination grace period.

If you notice stuck evictions, try one of the following solutions:

* Abort or pause the automated operation causing the issue. Investigate the stuck
  application before you restart the operation.
* Wait a while, then directly delete the Pod from your cluster control plane
  instead of using the Eviction API.

## What's next

* Learn how to protect your applications with a [Pod Disruption Budget](/docs/tasks/run-application/configure-pdb/).
* Learn about [Node-pressure Eviction](/docs/concepts/scheduling-eviction/node-pressure-eviction/).
* Learn about [Pod Priority and Preemption](/docs/concepts/scheduling-eviction/pod-priority-preemption/).

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
