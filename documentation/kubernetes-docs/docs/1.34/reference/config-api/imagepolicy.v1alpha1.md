# Image Policy API (v1alpha1)

## Resource Types

* [ImageReview](#imagepolicy-k8s-io-v1alpha1-ImageReview)

## `ImageReview`

ImageReview checks if the set of images in a pod are allowed.

| Field | Description |
| --- | --- |
| `apiVersion` string | `imagepolicy.k8s.io/v1alpha1` |
| `kind` string | `ImageReview` |
| `metadata`  [`meta/v1.ObjectMeta`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#objectmeta-v1-meta) | Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec` **[Required]**  [`ImageReviewSpec`](#imagepolicy-k8s-io-v1alpha1-ImageReviewSpec) | Spec holds information about the pod being evaluated |
| `status`  [`ImageReviewStatus`](#imagepolicy-k8s-io-v1alpha1-ImageReviewStatus) | Status is filled in by the backend and indicates whether the pod should be allowed. |

## `ImageReviewContainerSpec`

**Appears in:**

* [ImageReviewSpec](#imagepolicy-k8s-io-v1alpha1-ImageReviewSpec)

ImageReviewContainerSpec is a description of a container within the pod creation request.

| Field | Description |
| --- | --- |
| `image`  `string` | This can be in the form image:tag or image@SHA:012345679abcdef. |

## `ImageReviewSpec`

**Appears in:**

* [ImageReview](#imagepolicy-k8s-io-v1alpha1-ImageReview)

ImageReviewSpec is a description of the pod creation request.

| Field | Description |
| --- | --- |
| `containers`  [`[]ImageReviewContainerSpec`](#imagepolicy-k8s-io-v1alpha1-ImageReviewContainerSpec) | Containers is a list of a subset of the information in each container of the Pod being created. |
| `annotations`  `map[string]string` | Annotations is a list of key-value pairs extracted from the Pod's annotations. It only includes keys which match the pattern `*.image-policy.k8s.io/*`. It is up to each webhook backend to determine how to interpret these annotations, if at all. |
| `namespace`  `string` | Namespace is the namespace the pod is being created in. |

## `ImageReviewStatus`

**Appears in:**

* [ImageReview](#imagepolicy-k8s-io-v1alpha1-ImageReview)

ImageReviewStatus is the result of the review for the pod creation request.

| Field | Description |
| --- | --- |
| `allowed` **[Required]**  `bool` | Allowed indicates that all images were allowed to be run. |
| `reason`  `string` | Reason should be empty unless Allowed is false in which case it may contain a short description of what is wrong. Kubernetes may truncate excessively long errors when displaying to the user. |
| `auditAnnotations`  `map[string]string` | AuditAnnotations will be added to the attributes object of the admission controller request using 'AddAnnotation'. The keys should be prefix-less (i.e., the admission controller will add an appropriate prefix). |

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
