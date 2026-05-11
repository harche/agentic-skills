# Cluster Resources

---

##### [APIService](/docs/reference/kubernetes-api/cluster-resources/api-service-v1/)

APIService represents a server for a particular GroupVersion.

##### [ComponentStatus](/docs/reference/kubernetes-api/cluster-resources/component-status-v1/)

ComponentStatus (and ComponentStatusList) holds the cluster validation info.

##### [Event](/docs/reference/kubernetes-api/cluster-resources/event-v1/)

Event is a report of an event somewhere in the cluster.

##### [IPAddress](/docs/reference/kubernetes-api/cluster-resources/ip-address-v1/)

IPAddress represents a single IP of a single IP Family.

##### [Lease](/docs/reference/kubernetes-api/cluster-resources/lease-v1/)

Lease defines a lease concept.

##### [LeaseCandidate v1beta1](/docs/reference/kubernetes-api/cluster-resources/lease-candidate-v1beta1/)

LeaseCandidate defines a candidate for a Lease object.

##### [Namespace](/docs/reference/kubernetes-api/cluster-resources/namespace-v1/)

Namespace provides a scope for Names.

##### [Node](/docs/reference/kubernetes-api/cluster-resources/node-v1/)

Node is a worker node in Kubernetes.

##### [RuntimeClass](/docs/reference/kubernetes-api/cluster-resources/runtime-class-v1/)

RuntimeClass defines a class of container runtime supported in the cluster.

##### [ServiceCIDR](/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/)

ServiceCIDR defines a range of IP addresses using CIDR format (e.

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
