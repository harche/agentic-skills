# Policy Resources

---

##### [FlowSchema](/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/)

FlowSchema defines the schema of a group of flows.

##### [LimitRange](/docs/reference/kubernetes-api/policy-resources/limit-range-v1/)

LimitRange sets resource usage limits for each kind of resource in a Namespace.

##### [ResourceQuota](/docs/reference/kubernetes-api/policy-resources/resource-quota-v1/)

ResourceQuota sets aggregate quota restrictions enforced per namespace.

##### [NetworkPolicy](/docs/reference/kubernetes-api/policy-resources/network-policy-v1/)

NetworkPolicy describes what network traffic is allowed for a set of Pods.

##### [PodDisruptionBudget](/docs/reference/kubernetes-api/policy-resources/pod-disruption-budget-v1/)

PodDisruptionBudget is an object to define the max disruption that can be caused to a collection of pods.

##### [PriorityLevelConfiguration](/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/)

PriorityLevelConfiguration represents the configuration of a priority level.

##### [ValidatingAdmissionPolicy](/docs/reference/kubernetes-api/policy-resources/validating-admission-policy-v1/)

ValidatingAdmissionPolicy describes the definition of an admission validation policy that accepts or rejects an object without changing it.

##### [ValidatingAdmissionPolicyBinding](/docs/reference/kubernetes-api/policy-resources/validating-admission-policy-binding-v1/)

ValidatingAdmissionPolicyBinding binds the ValidatingAdmissionPolicy with paramerized resources.

##### [MutatingAdmissionPolicy v1beta1](/docs/reference/kubernetes-api/policy-resources/mutating-admission-policy-v1beta1/)

MutatingAdmissionPolicy describes the definition of an admission mutation policy that mutates the object coming into admission chain.

##### [MutatingAdmissionPolicyBinding v1alpha1](/docs/reference/kubernetes-api/policy-resources/mutating-admission-policy-binding-v1alpha1/)

MutatingAdmissionPolicyBinding binds the MutatingAdmissionPolicy with parametrized resources.

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
