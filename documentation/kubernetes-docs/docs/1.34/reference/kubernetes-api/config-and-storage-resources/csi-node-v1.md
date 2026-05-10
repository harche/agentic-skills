# CSINode

CSINode holds information about all CSI drivers installed on a node.

`apiVersion: storage.k8s.io/v1`

`import "k8s.io/api/storage/v1"`

## CSINode

CSINode holds information about all CSI drivers installed on a node. CSI drivers do not need to create the CSINode object directly. As long as they use the node-driver-registrar sidecar container, the kubelet will automatically populate the CSINode object for the CSI driver as part of kubelet plugin registration. CSINode has the same name as a node. If the object is missing, it means either there are no CSI Drivers available on the node, or the Kubelet version is low enough that it doesn't create this object. CSINode has an OwnerReference that points to the corresponding node object.

---

* **apiVersion**: storage.k8s.io/v1
* **kind**: CSINode
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard object's metadata. metadata.name must be the Kubernetes node name.
* **spec** ([CSINodeSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/#CSINodeSpec)), required

  spec is the specification of CSINode

## CSINodeSpec

CSINodeSpec holds information about the specification of all CSI drivers installed on a node

---

* **drivers** ([]CSINodeDriver), required

  *Patch strategy: merge on key `name`*

  *Map: unique values on key name will be kept during a merge*

  drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty.

  *CSINodeDriver holds information about the specification of one CSI driver installed on a node*

  + **drivers.name** (string), required

    name represents the name of the CSI driver that this object refers to. This MUST be the same name returned by the CSI GetPluginName() call for that driver.
  + **drivers.nodeID** (string), required

    nodeID of the node from the driver point of view. This field enables Kubernetes to communicate with storage systems that do not share the same nomenclature for nodes. For example, Kubernetes may refer to a given node as "node1", but the storage system may refer to the same node as "nodeA". When Kubernetes issues a command to the storage system to attach a volume to a specific node, it can use this field to refer to the node name using the ID that the storage system will understand, e.g. "nodeA" instead of "node1". This field is required.
  + **drivers.allocatable** (VolumeNodeResources)

    allocatable represents the volume resources of a node that are available for scheduling. This field is beta.

    *VolumeNodeResources is a set of resource limits for scheduling of volumes.*

    - **drivers.allocatable.count** (int32)

      count indicates the maximum number of unique volumes managed by the CSI driver that can be used on a node. A volume that is both attached and mounted on a node is considered to be used once, not twice. The same rule applies for a unique volume that is shared among multiple pods on the same node. If this field is not specified, then the supported number of volumes on this node is unbounded.
  + **drivers.topologyKeys** ([]string)

    *Atomic: will be replaced during a merge*

    topologyKeys is the list of keys supported by the driver. When a driver is initialized on a cluster, it provides a set of topology keys that it understands (e.g. "company.com/zone", "company.com/region"). When a driver is initialized on a node, it provides the same topology keys along with values. Kubelet will expose these topology keys as labels on its own node object. When Kubernetes does topology aware provisioning, it can use this list to determine which labels it should retrieve from the node object and pass back to the driver. It is possible for different nodes to use different topology keys. This can be empty if driver does not support topology.

## CSINodeList

CSINodeList is a collection of CSINode objects.

---

* **apiVersion**: storage.k8s.io/v1
* **kind**: CSINodeList
* **metadata** ([ListMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/#ListMeta))

  Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **items** ([][CSINode](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/#CSINode)), required

  items is the list of CSINode

## Operations

---

### `get` read the specified CSINode

#### HTTP Request

GET /apis/storage.k8s.io/v1/csinodes/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the CSINode
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([CSINode](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/#CSINode)): OK

401: Unauthorized

### `list` list or watch objects of kind CSINode

#### HTTP Request

GET /apis/storage.k8s.io/v1/csinodes

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

200 ([CSINodeList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/#CSINodeList)): OK

401: Unauthorized

### `create` create a CSINode

#### HTTP Request

POST /apis/storage.k8s.io/v1/csinodes

#### Parameters

* **body**: [CSINode](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/#CSINode), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([CSINode](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/#CSINode)): OK

201 ([CSINode](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/#CSINode)): Created

202 ([CSINode](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/#CSINode)): Accepted

401: Unauthorized

### `update` replace the specified CSINode

#### HTTP Request

PUT /apis/storage.k8s.io/v1/csinodes/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the CSINode
* **body**: [CSINode](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/#CSINode), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([CSINode](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/#CSINode)): OK

201 ([CSINode](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/#CSINode)): Created

401: Unauthorized

### `patch` partially update the specified CSINode

#### HTTP Request

PATCH /apis/storage.k8s.io/v1/csinodes/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the CSINode
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

200 ([CSINode](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/#CSINode)): OK

201 ([CSINode](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/#CSINode)): Created

401: Unauthorized

### `delete` delete a CSINode

#### HTTP Request

DELETE /apis/storage.k8s.io/v1/csinodes/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the CSINode
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

200 ([CSINode](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/#CSINode)): OK

202 ([CSINode](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/#CSINode)): Accepted

401: Unauthorized

### `deletecollection` delete collection of CSINode

#### HTTP Request

DELETE /apis/storage.k8s.io/v1/csinodes

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
