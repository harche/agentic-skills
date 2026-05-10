# ReplicaSet

ReplicaSet ensures that a specified number of pod replicas are running at any given time.

`apiVersion: apps/v1`

`import "k8s.io/api/apps/v1"`

## ReplicaSet

ReplicaSet ensures that a specified number of pod replicas are running at any given time.

---

* **apiVersion**: apps/v1
* **kind**: ReplicaSet
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  If the Labels of a ReplicaSet are empty, they are defaulted to be the same as the Pod(s) that the ReplicaSet manages. Standard object's metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **spec** ([ReplicaSetSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSetSpec))

  Spec defines the specification of the desired behavior of the ReplicaSet. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>
* **status** ([ReplicaSetStatus](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSetStatus))

  Status is the most recently observed status of the ReplicaSet. This data may be out of date by some window of time. Populated by the system. Read-only. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>

## ReplicaSetSpec

ReplicaSetSpec is the specification of a ReplicaSet.

---

* **selector** ([LabelSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/label-selector/#LabelSelector)), required

  Selector is a label query over pods that should match the replica count. Label keys and values that must match in order to be controlled by this replica set. It must match the pod template's labels. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors>
* **template** ([PodTemplateSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-template-v1/#PodTemplateSpec))

  Template is the object that describes the pod that will be created if insufficient replicas are detected. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/#pod-template>
* **replicas** (int32)

  Replicas is the number of desired pods. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicaset>
* **minReadySeconds** (int32)

  Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)

## ReplicaSetStatus

ReplicaSetStatus represents the current status of a ReplicaSet.

---

* **replicas** (int32), required

  Replicas is the most recently observed number of non-terminating pods. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicaset>
* **availableReplicas** (int32)

  The number of available non-terminating pods (ready for at least minReadySeconds) for this replica set.
* **readyReplicas** (int32)

  The number of non-terminating pods targeted by this ReplicaSet with a Ready Condition.
* **terminatingReplicas** (int32)

  The number of terminating pods for this replica set. Terminating pods have a non-null .metadata.deletionTimestamp and have not yet reached the Failed or Succeeded .status.phase.

  This is an alpha field. Enable DeploymentReplicaSetTerminatingReplicas to be able to use this field.
* **fullyLabeledReplicas** (int32)

  The number of non-terminating pods that have labels matching the labels of the pod template of the replicaset.
* **conditions** ([]ReplicaSetCondition)

  *Patch strategy: merge on key `type`*

  *Map: unique values on key type will be kept during a merge*

  Represents the latest available observations of a replica set's current state.

  *ReplicaSetCondition describes the state of a replica set at a certain point.*

  + **conditions.status** (string), required

    Status of the condition, one of True, False, Unknown.
  + **conditions.type** (string), required

    Type of replica set condition.
  + **conditions.lastTransitionTime** (Time)

    The last time the condition transitioned from one status to another.

    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
  + **conditions.message** (string)

    A human readable message indicating details about the transition.
  + **conditions.reason** (string)

    The reason for the condition's last transition.
* **observedGeneration** (int64)

  ObservedGeneration reflects the generation of the most recently observed ReplicaSet.

## ReplicaSetList

ReplicaSetList is a collection of ReplicaSets.

---

* **apiVersion**: apps/v1
* **kind**: ReplicaSetList
* **metadata** ([ListMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/#ListMeta))

  Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>
* **items** ([][ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet)), required

  List of ReplicaSets. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicaset>

## Operations

---

### `get` read the specified ReplicaSet

#### HTTP Request

GET /apis/apps/v1/namespaces/{namespace}/replicasets/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the ReplicaSet
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet)): OK

401: Unauthorized

### `get` read status of the specified ReplicaSet

#### HTTP Request

GET /apis/apps/v1/namespaces/{namespace}/replicasets/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the ReplicaSet
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet)): OK

401: Unauthorized

### `list` list or watch objects of kind ReplicaSet

#### HTTP Request

GET /apis/apps/v1/namespaces/{namespace}/replicasets

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

200 ([ReplicaSetList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSetList)): OK

401: Unauthorized

### `list` list or watch objects of kind ReplicaSet

#### HTTP Request

GET /apis/apps/v1/replicasets

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

200 ([ReplicaSetList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSetList)): OK

401: Unauthorized

### `create` create a ReplicaSet

#### HTTP Request

POST /apis/apps/v1/namespaces/{namespace}/replicasets

#### Parameters

* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet)): OK

201 ([ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet)): Created

202 ([ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet)): Accepted

401: Unauthorized

### `update` replace the specified ReplicaSet

#### HTTP Request

PUT /apis/apps/v1/namespaces/{namespace}/replicasets/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the ReplicaSet
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet)): OK

201 ([ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet)): Created

401: Unauthorized

### `update` replace status of the specified ReplicaSet

#### HTTP Request

PUT /apis/apps/v1/namespaces/{namespace}/replicasets/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the ReplicaSet
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet)): OK

201 ([ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet)): Created

401: Unauthorized

### `patch` partially update the specified ReplicaSet

#### HTTP Request

PATCH /apis/apps/v1/namespaces/{namespace}/replicasets/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the ReplicaSet
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

200 ([ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet)): OK

201 ([ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet)): Created

401: Unauthorized

### `patch` partially update status of the specified ReplicaSet

#### HTTP Request

PATCH /apis/apps/v1/namespaces/{namespace}/replicasets/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the ReplicaSet
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

200 ([ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet)): OK

201 ([ReplicaSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/#ReplicaSet)): Created

401: Unauthorized

### `delete` delete a ReplicaSet

#### HTTP Request

DELETE /apis/apps/v1/namespaces/{namespace}/replicasets/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the ReplicaSet
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

200 ([Status](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/status/#Status)): OK

202 ([Status](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/status/#Status)): Accepted

401: Unauthorized

### `deletecollection` delete collection of ReplicaSet

#### HTTP Request

DELETE /apis/apps/v1/namespaces/{namespace}/replicasets

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
