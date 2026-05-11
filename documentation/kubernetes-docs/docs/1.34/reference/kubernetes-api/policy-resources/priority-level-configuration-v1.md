# PriorityLevelConfiguration

PriorityLevelConfiguration represents the configuration of a priority level.

`apiVersion: flowcontrol.apiserver.k8s.io/v1`

`import "k8s.io/api/flowcontrol/v1"`

## PriorityLevelConfiguration

PriorityLevelConfiguration represents the configuration of a priority level.

---

* **apiVersion**: flowcontrol.apiserver.k8s.io/v1
* **kind**: PriorityLevelConfiguration
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  `metadata` is the standard object's metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **spec** ([PriorityLevelConfigurationSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfigurationSpec))

  `spec` is the specification of the desired behavior of a "request-priority". More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>
* **status** ([PriorityLevelConfigurationStatus](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfigurationStatus))

  `status` is the current status of a "request-priority". More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>

## PriorityLevelConfigurationSpec

PriorityLevelConfigurationSpec specifies the configuration of a priority level.

---

* **exempt** (ExemptPriorityLevelConfiguration)

  `exempt` specifies how requests are handled for an exempt priority level. This field MUST be empty if `type` is `"Limited"`. This field MAY be non-empty if `type` is `"Exempt"`. If empty and `type` is `"Exempt"` then the default values for `ExemptPriorityLevelConfiguration` apply.

  *ExemptPriorityLevelConfiguration describes the configurable aspects of the handling of exempt requests. In the mandatory exempt configuration object the values in the fields here can be modified by authorized users, unlike the rest of the `spec`.*

  + **exempt.lendablePercent** (int32)

    `lendablePercent` prescribes the fraction of the level's NominalCL that can be borrowed by other priority levels. This value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level's LendableConcurrencyLimit (LendableCL), is defined as follows.

    LendableCL(i) = round( NominalCL(i) * lendablePercent(i)/100.0 )
  + **exempt.nominalConcurrencyShares** (int32)

    `nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats nominally reserved for this priority level. This DOES NOT limit the dispatching from this priority level but affects the other priority levels through the borrowing mechanism. The server's concurrency limit (ServerCL) is divided among all the priority levels in proportion to their NCS values:

    NominalCL(i) = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k] NCS(k)

    Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level. This field has a default value of zero.
* **limited** (LimitedPriorityLevelConfiguration)

  `limited` specifies how requests are handled for a Limited priority level. This field must be non-empty if and only if `type` is `"Limited"`.

  *LimitedPriorityLevelConfiguration specifies how to handle requests that are subject to limits. It addresses two issues:

  + How are requests for this priority level limited?
  + What should be done with requests that exceed the limit?*
  + **limited.borrowingLimitPercent** (int32)

    `borrowingLimitPercent`, if present, configures a limit on how many seats this priority level can borrow from other priority levels. The limit is known as this level's BorrowingConcurrencyLimit (BorrowingCL) and is a limit on the total number of seats that this level may borrow at any one time. This field holds the ratio of that limit to the level's nominal concurrency limit. When this field is non-nil, it must hold a non-negative integer and the limit is calculated as follows.

    BorrowingCL(i) = round( NominalCL(i) * borrowingLimitPercent(i)/100.0 )

    The value of this field can be more than 100, implying that this priority level can borrow a number of seats that is greater than its own nominal concurrency limit (NominalCL). When this field is left `nil`, the limit is effectively infinite.
  + **limited.lendablePercent** (int32)

    `lendablePercent` prescribes the fraction of the level's NominalCL that can be borrowed by other priority levels. The value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level's LendableConcurrencyLimit (LendableCL), is defined as follows.

    LendableCL(i) = round( NominalCL(i) * lendablePercent(i)/100.0 )
  + **limited.limitResponse** (LimitResponse)

    `limitResponse` indicates what to do with requests that can not be executed right now

    *LimitResponse defines how to handle requests that can not be executed right now.*

    - **limited.limitResponse.type** (string), required

      `type` is "Queue" or "Reject". "Queue" means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. "Reject" means that requests that can not be executed upon arrival are rejected. Required.
    - **limited.limitResponse.queuing** (QueuingConfiguration)

      `queuing` holds the configuration parameters for queuing. This field may be non-empty only if `type` is `"Queue"`.

      *QueuingConfiguration holds the configuration parameters for queuing*

      * **limited.limitResponse.queuing.handSize** (int32)

        `handSize` is a small positive number that configures the shuffle sharding of requests into queues. When enqueuing a request at this priority level the request's flow identifier (a string pair) is hashed and the hash value is used to shuffle the list of queues and deal a hand of the size specified here. The request is put into one of the shortest queues in that hand. `handSize` must be no larger than `queues`, and should be significantly smaller (so that a few heavy flows do not saturate most of the queues). See the user-facing documentation for more extensive guidance on setting this field. This field has a default value of 8.
      * **limited.limitResponse.queuing.queueLengthLimit** (int32)

        `queueLengthLimit` is the maximum number of requests allowed to be waiting in a given queue of this priority level at a time; excess requests are rejected. This value must be positive. If not specified, it will be defaulted to 50.
      * **limited.limitResponse.queuing.queues** (int32)

        `queues` is the number of queues for this priority level. The queues exist independently at each apiserver. The value must be positive. Setting it to 1 effectively precludes shufflesharding and thus makes the distinguisher method of associated flow schemas irrelevant. This field has a default value of 64.
  + **limited.nominalConcurrencyShares** (int32)

    `nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats available at this priority level. This is used both for requests dispatched from this priority level as well as requests dispatched from other priority levels borrowing seats from this level. The server's concurrency limit (ServerCL) is divided among the Limited priority levels in proportion to their NCS values:

    NominalCL(i) = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k] NCS(k)

    Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level.

    If not specified, this field defaults to a value of 30.

    Setting this field to zero supports the construction of a "jail" for this priority level that is used to hold some request(s)
* **type** (string), required

  `type` indicates whether this priority level is subject to limitation on request execution. A value of `"Exempt"` means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels. A value of `"Limited"` means that (a) requests of this priority level *are* subject to limits and (b) some of the server's limited capacity is made available exclusively to this priority level. Required.

## PriorityLevelConfigurationStatus

PriorityLevelConfigurationStatus represents the current state of a "request-priority".

---

* **conditions** ([]PriorityLevelConfigurationCondition)

  *Patch strategy: merge on key `type`*

  *Map: unique values on key type will be kept during a merge*

  `conditions` is the current state of "request-priority".

  *PriorityLevelConfigurationCondition defines the condition of priority level.*

  + **conditions.lastTransitionTime** (Time)

    `lastTransitionTime` is the last time the condition transitioned from one status to another.

    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
  + **conditions.message** (string)

    `message` is a human-readable message indicating details about last transition.
  + **conditions.reason** (string)

    `reason` is a unique, one-word, CamelCase reason for the condition's last transition.
  + **conditions.status** (string)

    `status` is the status of the condition. Can be True, False, Unknown. Required.
  + **conditions.type** (string)

    `type` is the type of the condition. Required.

## PriorityLevelConfigurationList

PriorityLevelConfigurationList is a list of PriorityLevelConfiguration objects.

---

* **apiVersion**: flowcontrol.apiserver.k8s.io/v1
* **kind**: PriorityLevelConfigurationList
* **metadata** ([ListMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/#ListMeta))

  `metadata` is the standard object's metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **items** ([][PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration)), required

  `items` is a list of request-priorities.

## Operations

---

### `get` read the specified PriorityLevelConfiguration

#### HTTP Request

GET /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the PriorityLevelConfiguration
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration)): OK

401: Unauthorized

### `get` read status of the specified PriorityLevelConfiguration

#### HTTP Request

GET /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the PriorityLevelConfiguration
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration)): OK

401: Unauthorized

### `list` list or watch objects of kind PriorityLevelConfiguration

#### HTTP Request

GET /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations

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

200 ([PriorityLevelConfigurationList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfigurationList)): OK

401: Unauthorized

### `create` create a PriorityLevelConfiguration

#### HTTP Request

POST /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations

#### Parameters

* **body**: [PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration)): OK

201 ([PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration)): Created

202 ([PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration)): Accepted

401: Unauthorized

### `update` replace the specified PriorityLevelConfiguration

#### HTTP Request

PUT /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the PriorityLevelConfiguration
* **body**: [PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration)): OK

201 ([PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration)): Created

401: Unauthorized

### `update` replace status of the specified PriorityLevelConfiguration

#### HTTP Request

PUT /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the PriorityLevelConfiguration
* **body**: [PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration)): OK

201 ([PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration)): Created

401: Unauthorized

### `patch` partially update the specified PriorityLevelConfiguration

#### HTTP Request

PATCH /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the PriorityLevelConfiguration
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

200 ([PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration)): OK

201 ([PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration)): Created

401: Unauthorized

### `patch` partially update status of the specified PriorityLevelConfiguration

#### HTTP Request

PATCH /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the PriorityLevelConfiguration
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

200 ([PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration)): OK

201 ([PriorityLevelConfiguration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/#PriorityLevelConfiguration)): Created

401: Unauthorized

### `delete` delete a PriorityLevelConfiguration

#### HTTP Request

DELETE /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the PriorityLevelConfiguration
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

### `deletecollection` delete collection of PriorityLevelConfiguration

#### HTTP Request

DELETE /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations

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
