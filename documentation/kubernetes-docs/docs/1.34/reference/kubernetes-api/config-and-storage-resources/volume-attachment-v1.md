# VolumeAttachment

VolumeAttachment captures the intent to attach or detach the specified volume to/from the specified node.

`apiVersion: storage.k8s.io/v1`

`import "k8s.io/api/storage/v1"`

## VolumeAttachment

VolumeAttachment captures the intent to attach or detach the specified volume to/from the specified node.

VolumeAttachment objects are non-namespaced.

---

* **apiVersion**: storage.k8s.io/v1
* **kind**: VolumeAttachment
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard object metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **spec** ([VolumeAttachmentSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachmentSpec)), required

  spec represents specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.
* **status** ([VolumeAttachmentStatus](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachmentStatus))

  status represents status of the VolumeAttachment request. Populated by the entity completing the attach or detach operation, i.e. the external-attacher.

## VolumeAttachmentSpec

VolumeAttachmentSpec is the specification of a VolumeAttachment request.

---

* **attacher** (string), required

  attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().
* **nodeName** (string), required

  nodeName represents the node that the volume should be attached to.
* **source** (VolumeAttachmentSource), required

  source represents the volume that should be attached.

  *VolumeAttachmentSource represents a volume that should be attached. Right now only PersistentVolumes can be attached via external attacher, in the future we may allow also inline volumes in pods. Exactly one member can be set.*

  + **source.inlineVolumeSpec** ([PersistentVolumeSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/#PersistentVolumeSpec))

    inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is beta-level and is only honored by servers that enabled the CSIMigration feature.
  + **source.persistentVolumeName** (string)

    persistentVolumeName represents the name of the persistent volume to attach.

## VolumeAttachmentStatus

VolumeAttachmentStatus is the status of a VolumeAttachment request.

---

* **attached** (boolean), required

  attached indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
* **attachError** (VolumeError)

  attachError represents the last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.

  *VolumeError captures an error encountered during a volume operation.*

  + **attachError.errorCode** (int32)

    errorCode is a numeric gRPC code representing the error encountered during Attach or Detach operations.

    This is an optional, beta field that requires the MutableCSINodeAllocatableCount feature gate being enabled to be set.
  + **attachError.message** (string)

    message represents the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.
  + **attachError.time** (Time)

    time represents the time the error was encountered.

    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
* **attachmentMetadata** (map[string]string)

  attachmentMetadata is populated with any information returned by the attach operation, upon successful attach, that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
* **detachError** (VolumeError)

  detachError represents the last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher.

  *VolumeError captures an error encountered during a volume operation.*

  + **detachError.errorCode** (int32)

    errorCode is a numeric gRPC code representing the error encountered during Attach or Detach operations.

    This is an optional, beta field that requires the MutableCSINodeAllocatableCount feature gate being enabled to be set.
  + **detachError.message** (string)

    message represents the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.
  + **detachError.time** (Time)

    time represents the time the error was encountered.

    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*

## VolumeAttachmentList

VolumeAttachmentList is a collection of VolumeAttachment objects.

---

* **apiVersion**: storage.k8s.io/v1
* **kind**: VolumeAttachmentList
* **metadata** ([ListMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/#ListMeta))

  Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **items** ([][VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)), required

  items is the list of VolumeAttachments

## Operations

---

### `get` read the specified VolumeAttachment

#### HTTP Request

GET /apis/storage.k8s.io/v1/volumeattachments/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the VolumeAttachment
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)): OK

401: Unauthorized

### `get` read status of the specified VolumeAttachment

#### HTTP Request

GET /apis/storage.k8s.io/v1/volumeattachments/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the VolumeAttachment
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)): OK

401: Unauthorized

### `list` list or watch objects of kind VolumeAttachment

#### HTTP Request

GET /apis/storage.k8s.io/v1/volumeattachments

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

200 ([VolumeAttachmentList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachmentList)): OK

401: Unauthorized

### `create` create a VolumeAttachment

#### HTTP Request

POST /apis/storage.k8s.io/v1/volumeattachments

#### Parameters

* **body**: [VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)): OK

201 ([VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)): Created

202 ([VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)): Accepted

401: Unauthorized

### `update` replace the specified VolumeAttachment

#### HTTP Request

PUT /apis/storage.k8s.io/v1/volumeattachments/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the VolumeAttachment
* **body**: [VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)): OK

201 ([VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)): Created

401: Unauthorized

### `update` replace status of the specified VolumeAttachment

#### HTTP Request

PUT /apis/storage.k8s.io/v1/volumeattachments/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the VolumeAttachment
* **body**: [VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)): OK

201 ([VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)): Created

401: Unauthorized

### `patch` partially update the specified VolumeAttachment

#### HTTP Request

PATCH /apis/storage.k8s.io/v1/volumeattachments/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the VolumeAttachment
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

200 ([VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)): OK

201 ([VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)): Created

401: Unauthorized

### `patch` partially update status of the specified VolumeAttachment

#### HTTP Request

PATCH /apis/storage.k8s.io/v1/volumeattachments/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the VolumeAttachment
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

200 ([VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)): OK

201 ([VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)): Created

401: Unauthorized

### `delete` delete a VolumeAttachment

#### HTTP Request

DELETE /apis/storage.k8s.io/v1/volumeattachments/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the VolumeAttachment
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

200 ([VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)): OK

202 ([VolumeAttachment](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/#VolumeAttachment)): Accepted

401: Unauthorized

### `deletecollection` delete collection of VolumeAttachment

#### HTTP Request

DELETE /apis/storage.k8s.io/v1/volumeattachments

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
