# Workload Resources

---

##### [Pod](/docs/reference/kubernetes-api/workload-resources/pod-v1/)

Pod is a collection of containers that can run on a host.

##### [Binding](/docs/reference/kubernetes-api/workload-resources/binding-v1/)

Binding ties one object to another; for example, a pod is bound to a node by a scheduler.

##### [PodTemplate](/docs/reference/kubernetes-api/workload-resources/pod-template-v1/)

PodTemplate describes a template for creating copies of a predefined pod.

##### [ReplicationController](/docs/reference/kubernetes-api/workload-resources/replication-controller-v1/)

ReplicationController represents the configuration of a replication controller.

##### [ReplicaSet](/docs/reference/kubernetes-api/workload-resources/replica-set-v1/)

ReplicaSet ensures that a specified number of pod replicas are running at any given time.

##### [Deployment](/docs/reference/kubernetes-api/workload-resources/deployment-v1/)

Deployment enables declarative updates for Pods and ReplicaSets.

##### [StatefulSet](/docs/reference/kubernetes-api/workload-resources/stateful-set-v1/)

StatefulSet represents a set of pods with consistent identities.

##### [ControllerRevision](/docs/reference/kubernetes-api/workload-resources/controller-revision-v1/)

ControllerRevision implements an immutable snapshot of state data.

##### [DaemonSet](/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/)

DaemonSet represents the configuration of a daemon set.

##### [Job](/docs/reference/kubernetes-api/workload-resources/job-v1/)

Job represents the configuration of a single job.

##### [CronJob](/docs/reference/kubernetes-api/workload-resources/cron-job-v1/)

CronJob represents the configuration of a single cron job.

##### [HorizontalPodAutoscaler](/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/)

configuration of a horizontal pod autoscaler.

##### [HorizontalPodAutoscaler](/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2/)

HorizontalPodAutoscaler is the configuration for a horizontal pod autoscaler, which automatically manages the replica count of any resource implementing the scale subresource based on the metrics specified.

##### [PriorityClass](/docs/reference/kubernetes-api/workload-resources/priority-class-v1/)

PriorityClass defines mapping from a priority class name to the priority integer value.

##### [DeviceTaintRule v1alpha3](/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/)

DeviceTaintRule adds one taint to all devices which match the selector.

##### [ResourceClaim](/docs/reference/kubernetes-api/workload-resources/resource-claim-v1/)

ResourceClaim describes a request for access to resources in the cluster, for use by workloads.

##### [ResourceClaimTemplate](/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/)

ResourceClaimTemplate is used to produce ResourceClaim objects.

##### [ResourceSlice](/docs/reference/kubernetes-api/workload-resources/resource-slice-v1/)

ResourceSlice represents one or more resources in a pool of similar resources, managed by a common driver.

This page is automatically generated.

If you plan to report an issue with this page, mention that the page is auto-generated in your issue description. The fix may need to happen elsewhere in the Kubernetes project.

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
