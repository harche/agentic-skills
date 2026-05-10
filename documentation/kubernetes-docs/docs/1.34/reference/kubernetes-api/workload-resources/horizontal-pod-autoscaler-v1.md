# HorizontalPodAutoscaler

configuration of a horizontal pod autoscaler.

`apiVersion: autoscaling/v1`

`import "k8s.io/api/autoscaling/v1"`

## HorizontalPodAutoscaler

configuration of a horizontal pod autoscaler.

---

* **apiVersion**: autoscaling/v1
* **kind**: HorizontalPodAutoscaler
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard object metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **spec** ([HorizontalPodAutoscalerSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscalerSpec))

  spec defines the behaviour of autoscaler. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>.
* **status** ([HorizontalPodAutoscalerStatus](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscalerStatus))

  status is the current information about the autoscaler.

## HorizontalPodAutoscalerSpec

specification of a horizontal pod autoscaler.

---

* **maxReplicas** (int32), required

  maxReplicas is the upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.
* **scaleTargetRef** (CrossVersionObjectReference), required

  reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource.

  *CrossVersionObjectReference contains enough information to let you identify the referred resource.*

  + **scaleTargetRef.kind** (string), required

    kind is the kind of the referent; More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>
  + **scaleTargetRef.name** (string), required

    name is the name of the referent; More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>
  + **scaleTargetRef.apiVersion** (string)

    apiVersion is the API version of the referent
* **minReplicas** (int32)

  minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down. It defaults to 1 pod. minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured. Scaling is active as long as at least one metric value is available.
* **targetCPUUtilizationPercentage** (int32)

  targetCPUUtilizationPercentage is the target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used.

## HorizontalPodAutoscalerStatus

current status of a horizontal pod autoscaler

---

* **currentReplicas** (int32), required

  currentReplicas is the current number of replicas of pods managed by this autoscaler.
* **desiredReplicas** (int32), required

  desiredReplicas is the desired number of replicas of pods managed by this autoscaler.
* **currentCPUUtilizationPercentage** (int32)

  currentCPUUtilizationPercentage is the current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU.
* **lastScaleTime** (Time)

  lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed.

  *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
* **observedGeneration** (int64)

  observedGeneration is the most recent generation observed by this autoscaler.

## HorizontalPodAutoscalerList

list of horizontal pod autoscaler objects.

---

* **apiVersion**: autoscaling/v1
* **kind**: HorizontalPodAutoscalerList
* **metadata** ([ListMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/#ListMeta))

  Standard list metadata.
* **items** ([][HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler)), required

  items is the list of horizontal pod autoscaler objects.

## Operations

---

### `get` read the specified HorizontalPodAutoscaler

#### HTTP Request

GET /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the HorizontalPodAutoscaler
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler)): OK

401: Unauthorized

### `get` read status of the specified HorizontalPodAutoscaler

#### HTTP Request

GET /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the HorizontalPodAutoscaler
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler)): OK

401: Unauthorized

### `list` list or watch objects of kind HorizontalPodAutoscaler

#### HTTP Request

GET /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers

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

200 ([HorizontalPodAutoscalerList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscalerList)): OK

401: Unauthorized

### `list` list or watch objects of kind HorizontalPodAutoscaler

#### HTTP Request

GET /apis/autoscaling/v1/horizontalpodautoscalers

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

200 ([HorizontalPodAutoscalerList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscalerList)): OK

401: Unauthorized

### `create` create a HorizontalPodAutoscaler

#### HTTP Request

POST /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers

#### Parameters

* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler)): OK

201 ([HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler)): Created

202 ([HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler)): Accepted

401: Unauthorized

### `update` replace the specified HorizontalPodAutoscaler

#### HTTP Request

PUT /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the HorizontalPodAutoscaler
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler)): OK

201 ([HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler)): Created

401: Unauthorized

### `update` replace status of the specified HorizontalPodAutoscaler

#### HTTP Request

PUT /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the HorizontalPodAutoscaler
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler)): OK

201 ([HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler)): Created

401: Unauthorized

### `patch` partially update the specified HorizontalPodAutoscaler

#### HTTP Request

PATCH /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the HorizontalPodAutoscaler
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

200 ([HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler)): OK

201 ([HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler)): Created

401: Unauthorized

### `patch` partially update status of the specified HorizontalPodAutoscaler

#### HTTP Request

PATCH /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the HorizontalPodAutoscaler
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

200 ([HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler)): OK

201 ([HorizontalPodAutoscaler](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/#HorizontalPodAutoscaler)): Created

401: Unauthorized

### `delete` delete a HorizontalPodAutoscaler

#### HTTP Request

DELETE /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the HorizontalPodAutoscaler
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

### `deletecollection` delete collection of HorizontalPodAutoscaler

#### HTTP Request

DELETE /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers

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
