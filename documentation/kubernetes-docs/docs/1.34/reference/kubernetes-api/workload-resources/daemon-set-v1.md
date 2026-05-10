# DaemonSet

DaemonSet represents the configuration of a daemon set.

`apiVersion: apps/v1`

`import "k8s.io/api/apps/v1"`

## DaemonSet

DaemonSet represents the configuration of a daemon set.

---

* **apiVersion**: apps/v1
* **kind**: DaemonSet
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard object's metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **spec** ([DaemonSetSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSetSpec))

  The desired behavior of this daemon set. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>
* **status** ([DaemonSetStatus](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSetStatus))

  The current status of this daemon set. This data may be out of date by some window of time. Populated by the system. Read-only. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>

## DaemonSetSpec

DaemonSetSpec is the specification of a daemon set.

---

* **selector** ([LabelSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/label-selector/#LabelSelector)), required

  A label query over pods that are managed by the daemon set. Must match in order to be controlled. It must match the pod template's labels. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors>
* **template** ([PodTemplateSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-template-v1/#PodTemplateSpec)), required

  An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). The only allowed template.spec.restartPolicy value is "Always". More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template>
* **minReadySeconds** (int32)

  The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready).
* **updateStrategy** (DaemonSetUpdateStrategy)

  An update strategy to replace existing DaemonSet pods with new pods.

  *DaemonSetUpdateStrategy is a struct used to control the update strategy for a DaemonSet.*

  + **updateStrategy.type** (string)

    Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is RollingUpdate.

    Possible enum values:

    - `"OnDelete"` Replace the old daemons only when it's killed
    - `"RollingUpdate"` Replace the old daemons by new ones using rolling update i.e replace them on each node one after the other.
  + **updateStrategy.rollingUpdate** (RollingUpdateDaemonSet)

    Rolling update config params. Present only if type = "RollingUpdate".

    *Spec to control the desired behavior of daemon set rolling update.*

    - **updateStrategy.rollingUpdate.maxSurge** (IntOrString)

      The maximum number of nodes with an existing available DaemonSet pod that can have an updated DaemonSet pod during during an update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up to a minimum of 1. Default value is 0. Example: when this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled) can have their a new pod created before the old pod is marked as deleted. The update starts by launching new pods on 30% of nodes. Once an updated pod is available (Ready for at least minReadySeconds) the old DaemonSet pod on that node is marked deleted. If the old pod becomes unavailable for any reason (Ready transitions to false, is evicted, or is drained) an updated pod is immediately created on that node without considering surge limits. Allowing surge implies the possibility that the resources consumed by the daemonset on any given node can double if the readiness check fails, and so resource intensive daemonsets should take into account that they may cause evictions during disruption.

      *IntOrString is a type that can hold an int32 or a string. When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type. This allows you to have, for example, a JSON field that can accept a name or number.*
    - **updateStrategy.rollingUpdate.maxUnavailable** (IntOrString)

      The maximum number of DaemonSet pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of total number of DaemonSet pods at the start of the update (ex: 10%). Absolute number is calculated from percentage by rounding up. This cannot be 0 if MaxSurge is 0 Default value is 1. Example: when this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled) can have their pods stopped for an update at any given time. The update starts by stopping at most 30% of those DaemonSet pods and then brings up new DaemonSet pods in their place. Once the new pods are available, it then proceeds onto other DaemonSet pods, thus ensuring that at least 70% of original number of DaemonSet pods are available at all times during the update.

      *IntOrString is a type that can hold an int32 or a string. When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type. This allows you to have, for example, a JSON field that can accept a name or number.*
* **revisionHistoryLimit** (int32)

  The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.

## DaemonSetStatus

DaemonSetStatus represents the current status of a daemon set.

---

* **numberReady** (int32), required

  numberReady is the number of nodes that should be running the daemon pod and have one or more of the daemon pod running with a Ready Condition.
* **numberAvailable** (int32)

  The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds)
* **numberUnavailable** (int32)

  The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds)
* **numberMisscheduled** (int32), required

  The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/>
* **desiredNumberScheduled** (int32), required

  The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: <https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/>
* **currentNumberScheduled** (int32), required

  The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/>
* **updatedNumberScheduled** (int32)

  The total number of nodes that are running updated daemon pod
* **collisionCount** (int32)

  Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.
* **conditions** ([]DaemonSetCondition)

  *Patch strategy: merge on key `type`*

  *Map: unique values on key type will be kept during a merge*

  Represents the latest available observations of a DaemonSet's current state.

  *DaemonSetCondition describes the state of a DaemonSet at a certain point.*

  + **conditions.status** (string), required

    Status of the condition, one of True, False, Unknown.
  + **conditions.type** (string), required

    Type of DaemonSet condition.
  + **conditions.lastTransitionTime** (Time)

    Last time the condition transitioned from one status to another.

    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
  + **conditions.message** (string)

    A human readable message indicating details about the transition.
  + **conditions.reason** (string)

    The reason for the condition's last transition.
* **observedGeneration** (int64)

  The most recent generation observed by the daemon set controller.

## DaemonSetList

DaemonSetList is a collection of daemon sets.

---

* **apiVersion**: apps/v1
* **kind**: DaemonSetList
* **metadata** ([ListMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/#ListMeta))

  Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **items** ([][DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet)), required

  A list of daemon sets.

## Operations

---

### `get` read the specified DaemonSet

#### HTTP Request

GET /apis/apps/v1/namespaces/{namespace}/daemonsets/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the DaemonSet
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet)): OK

401: Unauthorized

### `get` read status of the specified DaemonSet

#### HTTP Request

GET /apis/apps/v1/namespaces/{namespace}/daemonsets/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the DaemonSet
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet)): OK

401: Unauthorized

### `list` list or watch objects of kind DaemonSet

#### HTTP Request

GET /apis/apps/v1/namespaces/{namespace}/daemonsets

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

200 ([DaemonSetList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSetList)): OK

401: Unauthorized

### `list` list or watch objects of kind DaemonSet

#### HTTP Request

GET /apis/apps/v1/daemonsets

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

200 ([DaemonSetList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSetList)): OK

401: Unauthorized

### `create` create a DaemonSet

#### HTTP Request

POST /apis/apps/v1/namespaces/{namespace}/daemonsets

#### Parameters

* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet)): OK

201 ([DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet)): Created

202 ([DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet)): Accepted

401: Unauthorized

### `update` replace the specified DaemonSet

#### HTTP Request

PUT /apis/apps/v1/namespaces/{namespace}/daemonsets/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the DaemonSet
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet)): OK

201 ([DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet)): Created

401: Unauthorized

### `update` replace status of the specified DaemonSet

#### HTTP Request

PUT /apis/apps/v1/namespaces/{namespace}/daemonsets/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the DaemonSet
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet)): OK

201 ([DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet)): Created

401: Unauthorized

### `patch` partially update the specified DaemonSet

#### HTTP Request

PATCH /apis/apps/v1/namespaces/{namespace}/daemonsets/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the DaemonSet
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

200 ([DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet)): OK

201 ([DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet)): Created

401: Unauthorized

### `patch` partially update status of the specified DaemonSet

#### HTTP Request

PATCH /apis/apps/v1/namespaces/{namespace}/daemonsets/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the DaemonSet
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

200 ([DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet)): OK

201 ([DaemonSet](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSet)): Created

401: Unauthorized

### `delete` delete a DaemonSet

#### HTTP Request

DELETE /apis/apps/v1/namespaces/{namespace}/daemonsets/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the DaemonSet
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

### `deletecollection` delete collection of DaemonSet

#### HTTP Request

DELETE /apis/apps/v1/namespaces/{namespace}/daemonsets

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
