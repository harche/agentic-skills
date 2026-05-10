# Namespace

Namespace provides a scope for Names.

`apiVersion: v1`

`import "k8s.io/api/core/v1"`

## Namespace

Namespace provides a scope for Names. Use of multiple namespaces is optional.

---

* **apiVersion**: v1
* **kind**: Namespace
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard object's metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **spec** ([NamespaceSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#NamespaceSpec))

  Spec defines the behavior of the Namespace. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>
* **status** ([NamespaceStatus](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#NamespaceStatus))

  Status describes the current status of a Namespace. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>

## NamespaceSpec

NamespaceSpec describes the attributes on a Namespace.

---

* **finalizers** ([]string)

  *Atomic: will be replaced during a merge*

  Finalizers is an opaque list of values that must be empty to permanently remove object from storage. More info: <https://kubernetes.io/docs/tasks/administer-cluster/namespaces/>

## NamespaceStatus

NamespaceStatus is information about the current status of a Namespace.

---

* **conditions** ([]NamespaceCondition)

  *Patch strategy: merge on key `type`*

  *Map: unique values on key type will be kept during a merge*

  Represents the latest available observations of a namespace's current state.

  *NamespaceCondition contains details about state of namespace.*

  + **conditions.status** (string), required

    Status of the condition, one of True, False, Unknown.
  + **conditions.type** (string), required

    Type of namespace controller condition.
  + **conditions.lastTransitionTime** (Time)

    Last time the condition transitioned from one status to another.

    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
  + **conditions.message** (string)

    Human-readable message indicating details about last transition.
  + **conditions.reason** (string)

    Unique, one-word, CamelCase reason for the condition's last transition.
* **phase** (string)

  Phase is the current lifecycle phase of the namespace. More info: <https://kubernetes.io/docs/tasks/administer-cluster/namespaces/>

  Possible enum values:

  + `"Active"` means the namespace is available for use in the system
  + `"Terminating"` means the namespace is undergoing graceful termination

## NamespaceList

NamespaceList is a list of Namespaces.

---

* **apiVersion**: v1
* **kind**: NamespaceList
* **metadata** ([ListMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/#ListMeta))

  Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>
* **items** ([][Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)), required

  Items is the list of Namespace objects in the list. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>

## Operations

---

### `get` read the specified Namespace

#### HTTP Request

GET /api/v1/namespaces/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the Namespace
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)): OK

401: Unauthorized

### `get` read status of the specified Namespace

#### HTTP Request

GET /api/v1/namespaces/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the Namespace
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)): OK

401: Unauthorized

### `list` list or watch objects of kind Namespace

#### HTTP Request

GET /api/v1/namespaces

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

200 ([NamespaceList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#NamespaceList)): OK

401: Unauthorized

### `create` create a Namespace

#### HTTP Request

POST /api/v1/namespaces

#### Parameters

* **body**: [Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)): OK

201 ([Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)): Created

202 ([Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)): Accepted

401: Unauthorized

### `update` replace the specified Namespace

#### HTTP Request

PUT /api/v1/namespaces/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the Namespace
* **body**: [Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)): OK

201 ([Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)): Created

401: Unauthorized

### `update` replace finalize of the specified Namespace

#### HTTP Request

PUT /api/v1/namespaces/{name}/finalize

#### Parameters

* **name** (*in path*): string, required

  name of the Namespace
* **body**: [Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)): OK

201 ([Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)): Created

401: Unauthorized

### `update` replace status of the specified Namespace

#### HTTP Request

PUT /api/v1/namespaces/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the Namespace
* **body**: [Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)): OK

201 ([Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)): Created

401: Unauthorized

### `patch` partially update the specified Namespace

#### HTTP Request

PATCH /api/v1/namespaces/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the Namespace
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

200 ([Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)): OK

201 ([Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)): Created

401: Unauthorized

### `patch` partially update status of the specified Namespace

#### HTTP Request

PATCH /api/v1/namespaces/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the Namespace
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

200 ([Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)): OK

201 ([Namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/#Namespace)): Created

401: Unauthorized

### `delete` delete a Namespace

#### HTTP Request

DELETE /api/v1/namespaces/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the Namespace
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
