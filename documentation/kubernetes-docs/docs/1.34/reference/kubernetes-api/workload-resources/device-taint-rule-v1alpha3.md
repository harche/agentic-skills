# DeviceTaintRule v1alpha3

DeviceTaintRule adds one taint to all devices which match the selector.

`apiVersion: resource.k8s.io/v1alpha3`

`import "k8s.io/api/resource/v1alpha3"`

## DeviceTaintRule

DeviceTaintRule adds one taint to all devices which match the selector. This has the same effect as if the taint was specified directly in the ResourceSlice by the DRA driver.

---

* **apiVersion**: resource.k8s.io/v1alpha3
* **kind**: DeviceTaintRule
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard object metadata
* **spec** ([DeviceTaintRuleSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/#DeviceTaintRuleSpec)), required

  Spec specifies the selector and one taint.

  Changing the spec automatically increments the metadata.generation number.

## DeviceTaintRuleSpec

DeviceTaintRuleSpec specifies the selector and one taint.

---

* **taint** (DeviceTaint), required

  The taint that gets applied to matching devices.

  *The device this taint is attached to has the "effect" on any claim which does not tolerate the taint and, through the claim, to pods using the claim.*

  + **taint.effect** (string), required

    The effect of the taint on claims that do not tolerate the taint and through such claims on the pods using them. Valid effects are NoSchedule and NoExecute. PreferNoSchedule as used for nodes is not valid here.

    Possible enum values:

    - `"NoExecute"` Evict any already-running pods that do not tolerate the device taint.
    - `"NoSchedule"` Do not allow new pods to schedule which use a tainted device unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running.
  + **taint.key** (string), required

    The taint key to be applied to a device. Must be a label name.
  + **taint.timeAdded** (Time)

    TimeAdded represents the time at which the taint was added. Added automatically during create or update if not set.

    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
  + **taint.value** (string)

    The taint value corresponding to the taint key. Must be a label value.
* **deviceSelector** (DeviceTaintSelector)

  DeviceSelector defines which device(s) the taint is applied to. All selector criteria must be satified for a device to match. The empty selector matches all devices. Without a selector, no devices are matches.

  *DeviceTaintSelector defines which device(s) a DeviceTaintRule applies to. The empty selector matches all devices. Without a selector, no devices are matched.*

  + **deviceSelector.device** (string)

    If device is set, only devices with that name are selected. This field corresponds to slice.spec.devices[].name.

    Setting also driver and pool may be required to avoid ambiguity, but is not required.
  + **deviceSelector.deviceClassName** (string)

    If DeviceClassName is set, the selectors defined there must be satisfied by a device to be selected. This field corresponds to class.metadata.name.
  + **deviceSelector.driver** (string)

    If driver is set, only devices from that driver are selected. This fields corresponds to slice.spec.driver.
  + **deviceSelector.pool** (string)

    If pool is set, only devices in that pool are selected.

    Also setting the driver name may be useful to avoid ambiguity when different drivers use the same pool name, but this is not required because selecting pools from different drivers may also be useful, for example when drivers with node-local devices use the node name as their pool name.
  + **deviceSelector.selectors** ([]DeviceSelector)

    *Atomic: will be replaced during a merge*

    Selectors contains the same selection criteria as a ResourceClaim. Currently, CEL expressions are supported. All of these selectors must be satisfied.

    *DeviceSelector must have exactly one field set.*

    - **deviceSelector.selectors.cel** (CELDeviceSelector)

      CEL contains a CEL expression for selecting a device.

      *CELDeviceSelector contains a CEL expression for selecting a device.*

      * **deviceSelector.selectors.cel.expression** (string), required

        Expression is a CEL expression which evaluates a single device. It must evaluate to true when the device under consideration satisfies the desired criteria, and false when it does not. Any other result is an error and causes allocation of devices to abort.

        The expression's input is an object named "device", which carries the following properties:

        + driver (string): the name of the driver which defines this device.
        + attributes (map[string]object): the device's attributes, grouped by prefix
          (e.g. device.attributes["dra.example.com"] evaluates to an object with all
          of the attributes which were prefixed by "dra.example.com".
        + capacity (map[string]object): the device's capacities, grouped by prefix.

        Example: Consider a device with driver="dra.example.com", which exposes two attributes named "model" and "ext.example.com/family" and which exposes one capacity named "modules". This input to this expression would have the following fields:

        ```
        device.driver
        device.attributes["dra.example.com"].model
        device.attributes["ext.example.com"].family
        device.capacity["dra.example.com"].modules
        ```

        The device.driver field can be used to check for a specific driver, either as a high-level precondition (i.e. you only want to consider devices from this driver) or as part of a multi-clause expression that is meant to consider devices from different drivers.

        The value type of each attribute is defined by the device definition, and users who write these expressions must consult the documentation for their specific drivers. The value type of each capacity is Quantity.

        If an unknown prefix is used as a lookup in either device.attributes or device.capacity, an empty map will be returned. Any reference to an unknown field will cause an evaluation error and allocation to abort.

        A robust expression should check for the existence of attributes before referencing them.

        For ease of use, the cel.bind() function is enabled, and can be used to simplify expressions that access multiple attributes with the same domain. For example:

        ```
        cel.bind(dra, device.attributes["dra.example.com"], dra.someBool && dra.anotherBool)
        ```

        The length of the expression must be smaller or equal to 10 Ki. The cost of evaluating it is also limited based on the estimated number of logical steps.

## DeviceTaintRuleList

DeviceTaintRuleList is a collection of DeviceTaintRules.

---

* **apiVersion**: resource.k8s.io/v1alpha3
* **kind**: DeviceTaintRuleList
* **metadata** ([ListMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/#ListMeta))

  Standard list metadata
* **items** ([][DeviceTaintRule](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/#DeviceTaintRule)), required

  Items is the list of DeviceTaintRules.

## Operations

---

### `get` read the specified DeviceTaintRule

#### HTTP Request

GET /apis/resource.k8s.io/v1alpha3/devicetaintrules/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the DeviceTaintRule
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([DeviceTaintRule](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/#DeviceTaintRule)): OK

401: Unauthorized

### `list` list or watch objects of kind DeviceTaintRule

#### HTTP Request

GET /apis/resource.k8s.io/v1alpha3/devicetaintrules

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

200 ([DeviceTaintRuleList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/#DeviceTaintRuleList)): OK

401: Unauthorized

### `create` create a DeviceTaintRule

#### HTTP Request

POST /apis/resource.k8s.io/v1alpha3/devicetaintrules

#### Parameters

* **body**: [DeviceTaintRule](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/#DeviceTaintRule), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([DeviceTaintRule](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/#DeviceTaintRule)): OK

201 ([DeviceTaintRule](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/#DeviceTaintRule)): Created

202 ([DeviceTaintRule](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/#DeviceTaintRule)): Accepted

401: Unauthorized

### `update` replace the specified DeviceTaintRule

#### HTTP Request

PUT /apis/resource.k8s.io/v1alpha3/devicetaintrules/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the DeviceTaintRule
* **body**: [DeviceTaintRule](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/#DeviceTaintRule), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([DeviceTaintRule](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/#DeviceTaintRule)): OK

201 ([DeviceTaintRule](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/#DeviceTaintRule)): Created

401: Unauthorized

### `patch` partially update the specified DeviceTaintRule

#### HTTP Request

PATCH /apis/resource.k8s.io/v1alpha3/devicetaintrules/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the DeviceTaintRule
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

200 ([DeviceTaintRule](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/#DeviceTaintRule)): OK

201 ([DeviceTaintRule](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/#DeviceTaintRule)): Created

401: Unauthorized

### `delete` delete a DeviceTaintRule

#### HTTP Request

DELETE /apis/resource.k8s.io/v1alpha3/devicetaintrules/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the DeviceTaintRule
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

200 ([DeviceTaintRule](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/#DeviceTaintRule)): OK

202 ([DeviceTaintRule](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1alpha3/#DeviceTaintRule)): Accepted

401: Unauthorized

### `deletecollection` delete collection of DeviceTaintRule

#### HTTP Request

DELETE /apis/resource.k8s.io/v1alpha3/devicetaintrules

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
