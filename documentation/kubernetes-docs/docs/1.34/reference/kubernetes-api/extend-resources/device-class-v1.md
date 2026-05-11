# DeviceClass

DeviceClass is a vendor- or admin-provided resource that contains device configuration and selectors.

`apiVersion: resource.k8s.io/v1`

`import "k8s.io/api/resource/v1"`

## DeviceClass

DeviceClass is a vendor- or admin-provided resource that contains device configuration and selectors. It can be referenced in the device requests of a claim to apply these presets. Cluster scoped.

This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

---

* **apiVersion**: resource.k8s.io/v1
* **kind**: DeviceClass
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard object metadata
* **spec** ([DeviceClassSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/#DeviceClassSpec)), required

  Spec defines what can be allocated and how to configure it.

  This is mutable. Consumers have to be prepared for classes changing at any time, either because they get updated or replaced. Claim allocations are done once based on whatever was set in classes at the time of allocation.

  Changing the spec automatically increments the metadata.generation number.

## DeviceClassSpec

DeviceClassSpec is used in a [DeviceClass] to define what can be allocated and how to configure it.

---

* **config** ([]DeviceClassConfiguration)

  *Atomic: will be replaced during a merge*

  Config defines configuration parameters that apply to each device that is claimed via this class. Some classses may potentially be satisfied by multiple drivers, so each instance of a vendor configuration applies to exactly one driver.

  They are passed to the driver, but are not considered while allocating the claim.

  *DeviceClassConfiguration is used in DeviceClass.*

  + **config.opaque** (OpaqueDeviceConfiguration)

    Opaque provides driver-specific configuration parameters.

    *OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.*

    - **config.opaque.driver** (string), required

      Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.

      An admission policy provided by the driver developer could use this to decide whether it needs to validate them.

      Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver.
    - **config.opaque.parameters** (RawExtension), required

      Parameters can contain arbitrary data. It is the responsibility of the driver developer to handle validation and versioning. Typically this includes self-identification and a version ("kind" + "apiVersion" for Kubernetes types), with conversion between different versions.

      The length of the raw data must be smaller or equal to 10 Ki.

      *RawExtension is used to hold extensions in external versions.

      To use this, make a field which has RawExtension as its type in your external, versioned struct, and Object in your internal struct. You also need to register your various plugin types.

      // Internal package:

      type MyAPIObject struct {
      runtime.TypeMeta `json:",inline"`
      MyPlugin runtime.Object `json:"myPlugin"`
      }

      type PluginA struct {
      AOption string `json:"aOption"`
      }

      // External package:

      type MyAPIObject struct {
      runtime.TypeMeta `json:",inline"`
      MyPlugin runtime.RawExtension `json:"myPlugin"`
      }

      type PluginA struct {
      AOption string `json:"aOption"`
      }

      // On the wire, the JSON will look something like this:

      {
      "kind":"MyAPIObject",
      "apiVersion":"v1",
      "myPlugin": {
      "kind":"PluginA",
      "aOption":"foo",
      },
      }

      So what happens? Decode first uses json or yaml to unmarshal the serialized data into your external MyAPIObject. That causes the raw JSON to be stored, but not unpacked. The next step is to copy (using pkg/conversion) into the internal struct. The runtime package's DefaultScheme has conversion functions installed which will unpack the JSON stored in RawExtension, turning it into the correct object type, and storing it in the Object. (TODO: In the case where the object is of an unknown type, a runtime.Unknown object will be created and stored.)*
* **extendedResourceName** (string)

  ExtendedResourceName is the extended resource name for the devices of this class. The devices of this class can be used to satisfy a pod's extended resource requests. It has the same format as the name of a pod's extended resource. It should be unique among all the device classes in a cluster. If two device classes have the same name, then the class created later is picked to satisfy a pod's extended resource requests. If two classes are created at the same time, then the name of the class lexicographically sorted first is picked.

  This is an alpha field.
* **selectors** ([]DeviceSelector)

  *Atomic: will be replaced during a merge*

  Each selector must be satisfied by a device which is claimed via this class.

  *DeviceSelector must have exactly one field set.*

  + **selectors.cel** (CELDeviceSelector)

    CEL contains a CEL expression for selecting a device.

    *CELDeviceSelector contains a CEL expression for selecting a device.*

    - **selectors.cel.expression** (string), required

      Expression is a CEL expression which evaluates a single device. It must evaluate to true when the device under consideration satisfies the desired criteria, and false when it does not. Any other result is an error and causes allocation of devices to abort.

      The expression's input is an object named "device", which carries the following properties:

      * driver (string): the name of the driver which defines this device.
      * attributes (map[string]object): the device's attributes, grouped by prefix
        (e.g. device.attributes["dra.example.com"] evaluates to an object with all
        of the attributes which were prefixed by "dra.example.com".
      * capacity (map[string]object): the device's capacities, grouped by prefix.
      * allowMultipleAllocations (bool): the allowMultipleAllocations property of the device
        (v1.34+ with the DRAConsumableCapacity feature enabled).

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

## DeviceClassList

DeviceClassList is a collection of classes.

---

* **apiVersion**: resource.k8s.io/v1
* **kind**: DeviceClassList
* **metadata** ([ListMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/#ListMeta))

  Standard list metadata
* **items** ([][DeviceClass](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/#DeviceClass)), required

  Items is the list of resource classes.

## Operations

---

### `get` read the specified DeviceClass

#### HTTP Request

GET /apis/resource.k8s.io/v1/deviceclasses/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the DeviceClass
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([DeviceClass](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/#DeviceClass)): OK

401: Unauthorized

### `list` list or watch objects of kind DeviceClass

#### HTTP Request

GET /apis/resource.k8s.io/v1/deviceclasses

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

200 ([DeviceClassList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/#DeviceClassList)): OK

401: Unauthorized

### `create` create a DeviceClass

#### HTTP Request

POST /apis/resource.k8s.io/v1/deviceclasses

#### Parameters

* **body**: [DeviceClass](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/#DeviceClass), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([DeviceClass](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/#DeviceClass)): OK

201 ([DeviceClass](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/#DeviceClass)): Created

202 ([DeviceClass](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/#DeviceClass)): Accepted

401: Unauthorized

### `update` replace the specified DeviceClass

#### HTTP Request

PUT /apis/resource.k8s.io/v1/deviceclasses/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the DeviceClass
* **body**: [DeviceClass](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/#DeviceClass), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([DeviceClass](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/#DeviceClass)): OK

201 ([DeviceClass](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/#DeviceClass)): Created

401: Unauthorized

### `patch` partially update the specified DeviceClass

#### HTTP Request

PATCH /apis/resource.k8s.io/v1/deviceclasses/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the DeviceClass
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

200 ([DeviceClass](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/#DeviceClass)): OK

201 ([DeviceClass](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/#DeviceClass)): Created

401: Unauthorized

### `delete` delete a DeviceClass

#### HTTP Request

DELETE /apis/resource.k8s.io/v1/deviceclasses/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the DeviceClass
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

200 ([DeviceClass](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/#DeviceClass)): OK

202 ([DeviceClass](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/extend-resources/device-class-v1/#DeviceClass)): Accepted

401: Unauthorized

### `deletecollection` delete collection of DeviceClass

#### HTTP Request

DELETE /apis/resource.k8s.io/v1/deviceclasses

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
