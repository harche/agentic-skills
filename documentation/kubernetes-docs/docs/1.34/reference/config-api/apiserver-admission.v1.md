# kube-apiserver Admission (v1)

## Resource Types

* [AdmissionReview](#admission-k8s-io-v1-AdmissionReview)

## `AdmissionReview`

AdmissionReview describes an admission review request/response.

| Field | Description |
| --- | --- |
| `apiVersion` string | `admission.k8s.io/v1` |
| `kind` string | `AdmissionReview` |
| `request`  [`AdmissionRequest`](#admission-k8s-io-v1-AdmissionRequest) | Request describes the attributes for the admission request. |
| `response`  [`AdmissionResponse`](#admission-k8s-io-v1-AdmissionResponse) | Response describes the attributes for the admission response. |

## `AdmissionRequest`

**Appears in:**

* [AdmissionReview](#admission-k8s-io-v1-AdmissionReview)

AdmissionRequest describes the admission.Attributes for the admission request.

| Field | Description |
| --- | --- |
| `uid` **[Required]**  [`k8s.io/apimachinery/pkg/types.UID`](https://pkg.go.dev/k8s.io/apimachinery/pkg/types#UID) | UID is an identifier for the individual request/response. It allows us to distinguish instances of requests which are otherwise identical (parallel requests, requests when earlier requests did not modify etc) The UID is meant to track the round trip (request/response) between the KAS and the WebHook, not the user request. It is suitable for correlating log entries between the webhook and apiserver, for either auditing or debugging. |
| `kind` **[Required]**  [`meta/v1.GroupVersionKind`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#GroupVersionKind) | Kind is the fully-qualified type of object being submitted (for example, v1.Pod or autoscaling.v1.Scale) |
| `resource` **[Required]**  [`meta/v1.GroupVersionResource`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#GroupVersionResource) | Resource is the fully-qualified resource being requested (for example, v1.pods) |
| `subResource`  `string` | SubResource is the subresource being requested, if any (for example, "status" or "scale") |
| `requestKind`  [`meta/v1.GroupVersionKind`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#GroupVersionKind) | RequestKind is the fully-qualified type of the original API request (for example, v1.Pod or autoscaling.v1.Scale). If this is specified and differs from the value in "kind", an equivalent match and conversion was performed.  For example, if deployments can be modified via apps/v1 and apps/v1beta1, and a webhook registered a rule of `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]` and `matchPolicy: Equivalent`, an API request to apps/v1beta1 deployments would be converted and sent to the webhook with `kind: {group:"apps", version:"v1", kind:"Deployment"}` (matching the rule the webhook registered for), and `requestKind: {group:"apps", version:"v1beta1", kind:"Deployment"}` (indicating the kind of the original API request).  See documentation for the "matchPolicy" field in the webhook configuration type for more details. |
| `requestResource`  [`meta/v1.GroupVersionResource`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#GroupVersionResource) | RequestResource is the fully-qualified resource of the original API request (for example, v1.pods). If this is specified and differs from the value in "resource", an equivalent match and conversion was performed.  For example, if deployments can be modified via apps/v1 and apps/v1beta1, and a webhook registered a rule of `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]` and `matchPolicy: Equivalent`, an API request to apps/v1beta1 deployments would be converted and sent to the webhook with `resource: {group:"apps", version:"v1", resource:"deployments"}` (matching the resource the webhook registered for), and `requestResource: {group:"apps", version:"v1beta1", resource:"deployments"}` (indicating the resource of the original API request).  See documentation for the "matchPolicy" field in the webhook configuration type. |
| `requestSubResource`  `string` | RequestSubResource is the name of the subresource of the original API request, if any (for example, "status" or "scale") If this is specified and differs from the value in "subResource", an equivalent match and conversion was performed. See documentation for the "matchPolicy" field in the webhook configuration type. |
| `name`  `string` | Name is the name of the object as presented in the request. On a CREATE operation, the client may omit name and rely on the server to generate the name. If that is the case, this field will contain an empty string. |
| `namespace`  `string` | Namespace is the namespace associated with the request (if any). |
| `operation` **[Required]**  [`Operation`](#admission-k8s-io-v1-Operation) | Operation is the operation being performed. This may be different than the operation requested. e.g. a patch can result in either a CREATE or UPDATE Operation. |
| `userInfo` **[Required]**  [`authentication/v1.UserInfo`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#userinfo-v1-authentication-k8s-io) | UserInfo is information about the requesting user |
| `object`  [`k8s.io/apimachinery/pkg/runtime.RawExtension`](https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime/#RawExtension) | Object is the object from the incoming request. |
| `oldObject`  [`k8s.io/apimachinery/pkg/runtime.RawExtension`](https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime/#RawExtension) | OldObject is the existing object. Only populated for DELETE and UPDATE requests. |
| `dryRun`  `bool` | DryRun indicates that modifications will definitely not be persisted for this request. Defaults to false. |
| `options`  [`k8s.io/apimachinery/pkg/runtime.RawExtension`](https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime/#RawExtension) | Options is the operation option structure of the operation being performed. e.g. `meta.k8s.io/v1.DeleteOptions` or `meta.k8s.io/v1.CreateOptions`. This may be different than the options the caller provided. e.g. for a patch request the performed Operation might be a CREATE, in which case the Options will a `meta.k8s.io/v1.CreateOptions` even though the caller provided `meta.k8s.io/v1.PatchOptions`. |

## `AdmissionResponse`

**Appears in:**

* [AdmissionReview](#admission-k8s-io-v1-AdmissionReview)

AdmissionResponse describes an admission response.

| Field | Description |
| --- | --- |
| `uid` **[Required]**  [`k8s.io/apimachinery/pkg/types.UID`](https://pkg.go.dev/k8s.io/apimachinery/pkg/types#UID) | UID is an identifier for the individual request/response. This must be copied over from the corresponding AdmissionRequest. |
| `allowed` **[Required]**  `bool` | Allowed indicates whether or not the admission request was permitted. |
| `status`  [`meta/v1.Status`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#status-v1-meta) | Result contains extra details into why an admission request was denied. This field IS NOT consulted in any way if "Allowed" is "true". |
| `patch`  `[]byte` | The patch body. Currently we only support "JSONPatch" which implements RFC 6902. |
| `patchType`  [`PatchType`](#admission-k8s-io-v1-PatchType) | The type of Patch. Currently we only allow "JSONPatch". |
| `auditAnnotations`  `map[string]string` | AuditAnnotations is an unstructured key value map set by remote admission controller (e.g. error=image-blacklisted). MutatingAdmissionWebhook and ValidatingAdmissionWebhook admission controller will prefix the keys with admission webhook name (e.g. imagepolicy.example.com/error=image-blacklisted). AuditAnnotations will be provided by the admission webhook to add additional context to the audit log for this request. |
| `warnings`  `[]string` | warnings is a list of warning messages to return to the requesting API client. Warning messages describe a problem the client making the API request should correct or be aware of. Limit warnings to 120 characters if possible. Warnings over 256 characters and large numbers of warnings may be truncated. |

## `Operation`

(Alias of `string`)

**Appears in:**

* [AdmissionRequest](#admission-k8s-io-v1-AdmissionRequest)

Operation is the type of resource operation being checked for admission control

## `PatchType`

(Alias of `string`)

**Appears in:**

* [AdmissionResponse](#admission-k8s-io-v1-AdmissionResponse)

PatchType is the type of patch being used to represent the mutated object

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
