# ResourceClaimTemplate

ResourceClaimTemplate is used to produce ResourceClaim objects.

`apiVersion: resource.k8s.io/v1`

`import "k8s.io/api/resource/v1"`

## ResourceClaimTemplate

ResourceClaimTemplate is used to produce ResourceClaim objects.

This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

---

* **apiVersion**: resource.k8s.io/v1
* **kind**: ResourceClaimTemplate
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard object metadata
* **spec** ([ResourceClaimTemplateSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplateSpec)), required

  Describes the ResourceClaim that is to be generated.

  This field is immutable. A ResourceClaim will get created by the control plane for a Pod when needed and then not get updated anymore.

## ResourceClaimTemplateSpec

ResourceClaimTemplateSpec contains the metadata and fields for a ResourceClaim.

---

* **spec** ([ResourceClaimSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-v1/#ResourceClaimSpec)), required

  Spec for the ResourceClaim. The entire content is copied unchanged into the ResourceClaim that gets created from this template. The same fields as in a ResourceClaim are also valid here.
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  ObjectMeta may contain labels and annotations that will be copied into the ResourceClaim when creating it. No other fields are allowed and will be rejected during validation.

## ResourceClaimTemplateList

ResourceClaimTemplateList is a collection of claim templates.

---

* **apiVersion**: resource.k8s.io/v1
* **kind**: ResourceClaimTemplateList
* **metadata** ([ListMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/#ListMeta))

  Standard list metadata
* **items** ([][ResourceClaimTemplate](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplate)), required

  Items is the list of resource claim templates.

## Operations

---

### `get` read the specified ResourceClaimTemplate

#### HTTP Request

GET /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaimtemplates/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the ResourceClaimTemplate
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([ResourceClaimTemplate](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplate)): OK

401: Unauthorized

### `list` list or watch objects of kind ResourceClaimTemplate

#### HTTP Request

GET /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaimtemplates

#### Parameters

* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **allowWatchBookmarks** (*in query*): boolean

  [allowWatchBookmarks](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#allowWatchBookmarks)
* **continue** (*in query*): string

  [continue](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#continue)
* **fieldSelector** (*in query*): string

  [fieldSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldSelector)
* **labelSelector** (*in query*): string

  [labelSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#labelSelector)
* **limit** (*in query*): integer

  [limit](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#limit)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)
* **resourceVersion** (*in query*): string

  [resourceVersion](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#resourceVersion)
* **resourceVersionMatch** (*in query*): string

  [resourceVersionMatch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#resourceVersionMatch)
* **sendInitialEvents** (*in query*): boolean

  [sendInitialEvents](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#sendInitialEvents)
* **timeoutSeconds** (*in query*): integer

  [timeoutSeconds](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#timeoutSeconds)
* **watch** (*in query*): boolean

  [watch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#watch)

#### Response

200 ([ResourceClaimTemplateList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplateList)): OK

401: Unauthorized

### `list` list or watch objects of kind ResourceClaimTemplate

#### HTTP Request

GET /apis/resource.k8s.io/v1/resourceclaimtemplates

#### Parameters

* **allowWatchBookmarks** (*in query*): boolean

  [allowWatchBookmarks](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#allowWatchBookmarks)
* **continue** (*in query*): string

  [continue](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#continue)
* **fieldSelector** (*in query*): string

  [fieldSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldSelector)
* **labelSelector** (*in query*): string

  [labelSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#labelSelector)
* **limit** (*in query*): integer

  [limit](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#limit)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)
* **resourceVersion** (*in query*): string

  [resourceVersion](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#resourceVersion)
* **resourceVersionMatch** (*in query*): string

  [resourceVersionMatch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#resourceVersionMatch)
* **sendInitialEvents** (*in query*): boolean

  [sendInitialEvents](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#sendInitialEvents)
* **timeoutSeconds** (*in query*): integer

  [timeoutSeconds](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#timeoutSeconds)
* **watch** (*in query*): boolean

  [watch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#watch)

#### Response

200 ([ResourceClaimTemplateList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplateList)): OK

401: Unauthorized

### `create` create a ResourceClaimTemplate

#### HTTP Request

POST /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaimtemplates

#### Parameters

* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [ResourceClaimTemplate](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplate), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([ResourceClaimTemplate](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplate)): OK

201 ([ResourceClaimTemplate](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplate)): Created

202 ([ResourceClaimTemplate](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplate)): Accepted

401: Unauthorized

### `update` replace the specified ResourceClaimTemplate

#### HTTP Request

PUT /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaimtemplates/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the ResourceClaimTemplate
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [ResourceClaimTemplate](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplate), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([ResourceClaimTemplate](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplate)): OK

201 ([ResourceClaimTemplate](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplate)): Created

401: Unauthorized

### `patch` partially update the specified ResourceClaimTemplate

#### HTTP Request

PATCH /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaimtemplates/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the ResourceClaimTemplate
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [Patch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/patch/#Patch), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **force** (*in query*): boolean

  [force](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#force)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([ResourceClaimTemplate](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplate)): OK

201 ([ResourceClaimTemplate](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplate)): Created

401: Unauthorized

### `delete` delete a ResourceClaimTemplate

#### HTTP Request

DELETE /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaimtemplates/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the ResourceClaimTemplate
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [DeleteOptions](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/delete-options/#DeleteOptions)
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **gracePeriodSeconds** (*in query*): integer

  [gracePeriodSeconds](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#gracePeriodSeconds)
* **ignoreStoreReadErrorWithClusterBreakingPotential** (*in query*): boolean

  [ignoreStoreReadErrorWithClusterBreakingPotential](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#ignoreStoreReadErrorWithClusterBreakingPotential)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)
* **propagationPolicy** (*in query*): string

  [propagationPolicy](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#propagationPolicy)

#### Response

200 ([ResourceClaimTemplate](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplate)): OK

202 ([ResourceClaimTemplate](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/#ResourceClaimTemplate)): Accepted

401: Unauthorized

### `deletecollection` delete collection of ResourceClaimTemplate

#### HTTP Request

DELETE /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaimtemplates

#### Parameters

* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [DeleteOptions](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/delete-options/#DeleteOptions)
* **continue** (*in query*): string

  [continue](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#continue)
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldSelector** (*in query*): string

  [fieldSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldSelector)
* **gracePeriodSeconds** (*in query*): integer

  [gracePeriodSeconds](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#gracePeriodSeconds)
* **ignoreStoreReadErrorWithClusterBreakingPotential** (*in query*): boolean

  [ignoreStoreReadErrorWithClusterBreakingPotential](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#ignoreStoreReadErrorWithClusterBreakingPotential)
* **labelSelector** (*in query*): string

  [labelSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#labelSelector)
* **limit** (*in query*): integer

  [limit](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#limit)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)
* **propagationPolicy** (*in query*): string

  [propagationPolicy](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#propagationPolicy)
* **resourceVersion** (*in query*): string

  [resourceVersion](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#resourceVersion)
* **resourceVersionMatch** (*in query*): string

  [resourceVersionMatch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#resourceVersionMatch)
* **sendInitialEvents** (*in query*): boolean

  [sendInitialEvents](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#sendInitialEvents)
* **timeoutSeconds** (*in query*): integer

  [timeoutSeconds](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#timeoutSeconds)

#### Response

200 ([Status](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/status/#Status)): OK

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
