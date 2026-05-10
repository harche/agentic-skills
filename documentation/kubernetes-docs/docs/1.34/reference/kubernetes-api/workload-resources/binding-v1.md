# Binding

Binding ties one object to another; for example, a pod is bound to a node by a scheduler.

`apiVersion: v1`

`import "k8s.io/api/core/v1"`

## Binding

Binding ties one object to another; for example, a pod is bound to a node by a scheduler.

---

* **apiVersion**: v1
* **kind**: Binding
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard object's metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **target** ([ObjectReference](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-reference/#ObjectReference)), required

  The target object that you want to bind to the standard object.

## Operations

---

### `create` create a Binding

#### HTTP Request

POST /api/v1/namespaces/{namespace}/bindings

#### Parameters

* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [Binding](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/binding-v1/#Binding), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([Binding](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/binding-v1/#Binding)): OK

201 ([Binding](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/binding-v1/#Binding)): Created

202 ([Binding](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/binding-v1/#Binding)): Accepted

401: Unauthorized

### `create` create binding of a Pod

#### HTTP Request

POST /api/v1/namespaces/{namespace}/pods/{name}/binding

#### Parameters

* **name** (*in path*): string, required

  name of the Binding
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [Binding](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/binding-v1/#Binding), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([Binding](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/binding-v1/#Binding)): OK

201 ([Binding](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/binding-v1/#Binding)): Created

202 ([Binding](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/binding-v1/#Binding)): Accepted

401: Unauthorized

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
