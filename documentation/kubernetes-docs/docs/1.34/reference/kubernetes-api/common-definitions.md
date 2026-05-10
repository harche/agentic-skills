# Common Definitions

---

##### [DeleteOptions](/docs/reference/kubernetes-api/common-definitions/delete-options/)

DeleteOptions may be provided when deleting an API object.

##### [LabelSelector](/docs/reference/kubernetes-api/common-definitions/label-selector/)

A label selector is a label query over a set of resources.

##### [ListMeta](/docs/reference/kubernetes-api/common-definitions/list-meta/)

ListMeta describes metadata that synthetic resources must have, including lists and various status objects.

##### [LocalObjectReference](/docs/reference/kubernetes-api/common-definitions/local-object-reference/)

LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

##### [NodeSelectorRequirement](/docs/reference/kubernetes-api/common-definitions/node-selector-requirement/)

A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

##### [ObjectFieldSelector](/docs/reference/kubernetes-api/common-definitions/object-field-selector/)

ObjectFieldSelector selects an APIVersioned field of an object.

##### [ObjectMeta](/docs/reference/kubernetes-api/common-definitions/object-meta/)

ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.

##### [ObjectReference](/docs/reference/kubernetes-api/common-definitions/object-reference/)

ObjectReference contains enough information to let you inspect or modify the referred object.

##### [Patch](/docs/reference/kubernetes-api/common-definitions/patch/)

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

##### [Quantity](/docs/reference/kubernetes-api/common-definitions/quantity/)

Quantity is a fixed-point representation of a number.

##### [ResourceFieldSelector](/docs/reference/kubernetes-api/common-definitions/resource-field-selector/)

ResourceFieldSelector represents container resources (cpu, memory) and their output format.

##### [Status](/docs/reference/kubernetes-api/common-definitions/status/)

Status is a return value for calls that don't return other objects.

##### [TypedLocalObjectReference](/docs/reference/kubernetes-api/common-definitions/typed-local-object-reference/)

TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.

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
