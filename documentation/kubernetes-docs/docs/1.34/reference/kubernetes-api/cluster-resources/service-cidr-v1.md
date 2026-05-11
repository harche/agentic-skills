# ServiceCIDR

ServiceCIDR defines a range of IP addresses using CIDR format (e.

`apiVersion: networking.k8s.io/v1`

`import "k8s.io/api/networking/v1"`

## ServiceCIDR

ServiceCIDR defines a range of IP addresses using CIDR format (e.g. 192.168.0.0/24 or 2001:db2::/64). This range is used to allocate ClusterIPs to Service objects.

---

* **apiVersion**: networking.k8s.io/v1
* **kind**: ServiceCIDR
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard object's metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **spec** ([ServiceCIDRSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDRSpec))

  spec is the desired state of the ServiceCIDR. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>
* **status** ([ServiceCIDRStatus](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDRStatus))

  status represents the current state of the ServiceCIDR. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>

## ServiceCIDRSpec

ServiceCIDRSpec define the CIDRs the user wants to use for allocating ClusterIPs for Services.

---

* **cidrs** ([]string)

  *Atomic: will be replaced during a merge*

  CIDRs defines the IP blocks in CIDR notation (e.g. "192.168.0.0/24" or "2001:db8::/64") from which to assign service cluster IPs. Max of two CIDRs is allowed, one of each IP family. This field is immutable.

## ServiceCIDRStatus

ServiceCIDRStatus describes the current state of the ServiceCIDR.

---

* **conditions** ([]Condition)

  *Patch strategy: merge on key `type`*

  *Map: unique values on key type will be kept during a merge*

  conditions holds an array of metav1.Condition that describe the state of the ServiceCIDR. Current service state

  *Condition contains details for one aspect of the current state of this API Resource.*

  + **conditions.lastTransitionTime** (Time), required

    lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.

    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
  + **conditions.message** (string), required

    message is a human readable message indicating details about the transition. This may be an empty string.
  + **conditions.reason** (string), required

    reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.
  + **conditions.status** (string), required

    status of the condition, one of True, False, Unknown.
  + **conditions.type** (string), required

    type of condition in CamelCase or in foo.example.com/CamelCase.
  + **conditions.observedGeneration** (int64)

    observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.

## ServiceCIDRList

ServiceCIDRList contains a list of ServiceCIDR objects.

---

* **apiVersion**: networking.k8s.io/v1
* **kind**: ServiceCIDRList
* **metadata** ([ListMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/#ListMeta))

  Standard object's metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **items** ([][ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR)), required

  items is the list of ServiceCIDRs.

## Operations

---

### `get` read the specified ServiceCIDR

#### HTTP Request

GET /apis/networking.k8s.io/v1/servicecidrs/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the ServiceCIDR
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR)): OK

401: Unauthorized

### `get` read status of the specified ServiceCIDR

#### HTTP Request

GET /apis/networking.k8s.io/v1/servicecidrs/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the ServiceCIDR
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR)): OK

401: Unauthorized

### `list` list or watch objects of kind ServiceCIDR

#### HTTP Request

GET /apis/networking.k8s.io/v1/servicecidrs

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

200 ([ServiceCIDRList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDRList)): OK

401: Unauthorized

### `create` create a ServiceCIDR

#### HTTP Request

POST /apis/networking.k8s.io/v1/servicecidrs

#### Parameters

* **body**: [ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR)): OK

201 ([ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR)): Created

202 ([ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR)): Accepted

401: Unauthorized

### `update` replace the specified ServiceCIDR

#### HTTP Request

PUT /apis/networking.k8s.io/v1/servicecidrs/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the ServiceCIDR
* **body**: [ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR)): OK

201 ([ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR)): Created

401: Unauthorized

### `update` replace status of the specified ServiceCIDR

#### HTTP Request

PUT /apis/networking.k8s.io/v1/servicecidrs/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the ServiceCIDR
* **body**: [ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR)): OK

201 ([ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR)): Created

401: Unauthorized

### `patch` partially update the specified ServiceCIDR

#### HTTP Request

PATCH /apis/networking.k8s.io/v1/servicecidrs/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the ServiceCIDR
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

200 ([ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR)): OK

201 ([ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR)): Created

401: Unauthorized

### `patch` partially update status of the specified ServiceCIDR

#### HTTP Request

PATCH /apis/networking.k8s.io/v1/servicecidrs/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the ServiceCIDR
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

200 ([ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR)): OK

201 ([ServiceCIDR](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/#ServiceCIDR)): Created

401: Unauthorized

### `delete` delete a ServiceCIDR

#### HTTP Request

DELETE /apis/networking.k8s.io/v1/servicecidrs/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the ServiceCIDR
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

200 ([Status](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/status/#Status)): OK

202 ([Status](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/status/#Status)): Accepted

401: Unauthorized

### `deletecollection` delete collection of ServiceCIDR

#### HTTP Request

DELETE /apis/networking.k8s.io/v1/servicecidrs

#### Parameters

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
