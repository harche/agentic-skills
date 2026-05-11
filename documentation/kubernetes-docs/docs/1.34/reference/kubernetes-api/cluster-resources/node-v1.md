# Node

Node is a worker node in Kubernetes.

`apiVersion: v1`

`import "k8s.io/api/core/v1"`

## Node

Node is a worker node in Kubernetes. Each node will have a unique identifier in the cache (i.e. in etcd).

---

* **apiVersion**: v1
* **kind**: Node
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard object's metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **spec** ([NodeSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#NodeSpec))

  Spec defines the behavior of a node. <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>
* **status** ([NodeStatus](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#NodeStatus))

  Most recently observed status of the node. Populated by the system. Read-only. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>

## NodeSpec

NodeSpec describes the attributes that a node is created with.

---

* **configSource** (NodeConfigSource)

  Deprecated: Previously used to specify the source of the node's configuration for the DynamicKubeletConfig feature. This feature is removed.

  *NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22*

  + **configSource.configMap** (ConfigMapNodeConfigSource)

    ConfigMap is a reference to a Node's ConfigMap

    *ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: <https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration>*

    - **configSource.configMap.kubeletConfigKey** (string), required

      KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.
    - **configSource.configMap.name** (string), required

      Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.
    - **configSource.configMap.namespace** (string), required

      Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.
    - **configSource.configMap.resourceVersion** (string)

      ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.
    - **configSource.configMap.uid** (string)

      UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.
* **externalID** (string)

  Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: <https://issues.k8s.io/61966>
* **podCIDR** (string)

  PodCIDR represents the pod IP range assigned to the node.
* **podCIDRs** ([]string)

  *Set: unique values will be kept during a merge*

  podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6.
* **providerID** (string)

  ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>
* **taints** ([]Taint)

  *Atomic: will be replaced during a merge*

  If specified, the node's taints.

  *The node this Taint is attached to has the "effect" on any pod that does not tolerate the Taint.*

  + **taints.effect** (string), required

    Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.

    Possible enum values:

    - `"NoExecute"` Evict any already-running pods that do not tolerate the taint. Currently enforced by NodeController.
    - `"NoSchedule"` Do not allow new pods to schedule onto the node unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. Enforced by the scheduler.
    - `"PreferNoSchedule"` Like TaintEffectNoSchedule, but the scheduler tries not to schedule new pods onto the node, rather than prohibiting new pods from scheduling onto the node entirely. Enforced by the scheduler.
  + **taints.key** (string), required

    Required. The taint key to be applied to a node.
  + **taints.timeAdded** (Time)

    TimeAdded represents the time at which the taint was added.

    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
  + **taints.value** (string)

    The taint value corresponding to the taint key.
* **unschedulable** (boolean)

  Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: <https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration>

## NodeStatus

NodeStatus is information about the current status of a node.

---

* **addresses** ([]NodeAddress)

  *Patch strategy: merge on key `type`*

  *Map: unique values on key type will be kept during a merge*

  List of addresses reachable to the node. Queried from cloud provider, if available. More info: <https://kubernetes.io/docs/reference/node/node-status/#addresses> Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See <https://pr.k8s.io/79391> for an example. Consumers should assume that addresses can change during the lifetime of a Node. However, there are some exceptions where this may not be possible, such as Pods that inherit a Node's address in its own status or consumers of the downward API (status.hostIP).

  *NodeAddress contains information for the node's address.*

  + **addresses.address** (string), required

    The node address.
  + **addresses.type** (string), required

    Node address type, one of Hostname, ExternalIP or InternalIP.
* **allocatable** (map[string][Quantity](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/quantity/#Quantity))

  Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity.
* **capacity** (map[string][Quantity](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/quantity/#Quantity))

  Capacity represents the total resources of a node. More info: <https://kubernetes.io/docs/reference/node/node-status/#capacity>
* **conditions** ([]NodeCondition)

  *Patch strategy: merge on key `type`*

  *Map: unique values on key type will be kept during a merge*

  Conditions is an array of current observed node conditions. More info: <https://kubernetes.io/docs/reference/node/node-status/#condition>

  *NodeCondition contains condition information for a node.*

  + **conditions.status** (string), required

    Status of the condition, one of True, False, Unknown.
  + **conditions.type** (string), required

    Type of node condition.
  + **conditions.lastHeartbeatTime** (Time)

    Last time we got an update on a given condition.

    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
  + **conditions.lastTransitionTime** (Time)

    Last time the condition transit from one status to another.

    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
  + **conditions.message** (string)

    Human readable message indicating details about last transition.
  + **conditions.reason** (string)

    (brief) reason for the condition's last transition.
* **config** (NodeConfigStatus)

  Status of the config assigned to the node via the dynamic Kubelet config feature.

  *NodeConfigStatus describes the status of the config assigned by Node.Spec.ConfigSource.*

  + **config.active** (NodeConfigSource)

    Active reports the checkpointed config the node is actively using. Active will represent either the current version of the Assigned config, or the current LastKnownGood config, depending on whether attempting to use the Assigned config results in an error.

    *NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22*

    - **config.active.configMap** (ConfigMapNodeConfigSource)

      ConfigMap is a reference to a Node's ConfigMap

      *ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: <https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration>*

      * **config.active.configMap.kubeletConfigKey** (string), required

        KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.
      * **config.active.configMap.name** (string), required

        Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.
      * **config.active.configMap.namespace** (string), required

        Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.
      * **config.active.configMap.resourceVersion** (string)

        ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.
      * **config.active.configMap.uid** (string)

        UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.
  + **config.assigned** (NodeConfigSource)

    Assigned reports the checkpointed config the node will try to use. When Node.Spec.ConfigSource is updated, the node checkpoints the associated config payload to local disk, along with a record indicating intended config. The node refers to this record to choose its config checkpoint, and reports this record in Assigned. Assigned only updates in the status after the record has been checkpointed to disk. When the Kubelet is restarted, it tries to make the Assigned config the Active config by loading and validating the checkpointed payload identified by Assigned.

    *NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22*

    - **config.assigned.configMap** (ConfigMapNodeConfigSource)

      ConfigMap is a reference to a Node's ConfigMap

      *ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: <https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration>*

      * **config.assigned.configMap.kubeletConfigKey** (string), required

        KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.
      * **config.assigned.configMap.name** (string), required

        Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.
      * **config.assigned.configMap.namespace** (string), required

        Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.
      * **config.assigned.configMap.resourceVersion** (string)

        ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.
      * **config.assigned.configMap.uid** (string)

        UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.
  + **config.error** (string)

    Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors may occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned record, attempting to checkpoint the payload associated with Spec.ConfigSource, attempting to load or validate the Assigned config, etc. Errors may occur at different points while syncing config. Earlier errors (e.g. download or checkpointing errors) will not result in a rollback to LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g. loading or validating a checkpointed config) will result in a rollback to LastKnownGood. In the latter case, it is usually possible to resolve the error by fixing the config assigned in Spec.ConfigSource. You can find additional information for debugging by searching the error message in the Kubelet log. Error is a human-readable description of the error state; machines can check whether or not Error is empty, but should not rely on the stability of the Error text across Kubelet versions.
  + **config.lastKnownGood** (NodeConfigSource)

    LastKnownGood reports the checkpointed config the node will fall back to when it encounters an error attempting to use the Assigned config. The Assigned config becomes the LastKnownGood config when the node determines that the Assigned config is stable and correct. This is currently implemented as a 10-minute soak period starting when the local record of Assigned config is updated. If the Assigned config is Active at the end of this period, it becomes the LastKnownGood. Note that if Spec.ConfigSource is reset to nil (use local defaults), the LastKnownGood is also immediately reset to nil, because the local default config is always assumed good. You should not make assumptions about the node's method of determining config stability and correctness, as this may change or become configurable in the future.

    *NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22*

    - **config.lastKnownGood.configMap** (ConfigMapNodeConfigSource)

      ConfigMap is a reference to a Node's ConfigMap

      *ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: <https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration>*

      * **config.lastKnownGood.configMap.kubeletConfigKey** (string), required

        KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.
      * **config.lastKnownGood.configMap.name** (string), required

        Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.
      * **config.lastKnownGood.configMap.namespace** (string), required

        Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.
      * **config.lastKnownGood.configMap.resourceVersion** (string)

        ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.
      * **config.lastKnownGood.configMap.uid** (string)

        UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.
* **daemonEndpoints** (NodeDaemonEndpoints)

  Endpoints of daemons running on the Node.

  *NodeDaemonEndpoints lists ports opened by daemons running on the Node.*

  + **daemonEndpoints.kubeletEndpoint** (DaemonEndpoint)

    Endpoint on which Kubelet is listening.

    *DaemonEndpoint contains information about a single Daemon endpoint.*

    - **daemonEndpoints.kubeletEndpoint.Port** (int32), required

      Port number of the given endpoint.
* **features** (NodeFeatures)

  Features describes the set of features implemented by the CRI implementation.

  *NodeFeatures describes the set of features implemented by the CRI implementation. The features contained in the NodeFeatures should depend only on the cri implementation independent of runtime handlers.*

  + **features.supplementalGroupsPolicy** (boolean)

    SupplementalGroupsPolicy is set to true if the runtime supports SupplementalGroupsPolicy and ContainerUser.
* **images** ([]ContainerImage)

  *Atomic: will be replaced during a merge*

  List of container images on this node

  *Describe a container image*

  + **images.names** ([]string)

    *Atomic: will be replaced during a merge*

    Names by which this image is known. e.g. ["kubernetes.example/hyperkube:v1.0.7", "cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7"]
  + **images.sizeBytes** (int64)

    The size of the image in bytes.
* **nodeInfo** (NodeSystemInfo)

  Set of ids/uuids to uniquely identify the node. More info: <https://kubernetes.io/docs/reference/node/node-status/#info>

  *NodeSystemInfo is a set of ids/uuids to uniquely identify the node.*

  + **nodeInfo.architecture** (string), required

    The Architecture reported by the node
  + **nodeInfo.bootID** (string), required

    Boot ID reported by the node.
  + **nodeInfo.containerRuntimeVersion** (string), required

    ContainerRuntime Version reported by the node through runtime remote API (e.g. containerd://1.4.2).
  + **nodeInfo.kernelVersion** (string), required

    Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).
  + **nodeInfo.kubeProxyVersion** (string), required

    Deprecated: KubeProxy Version reported by the node.
  + **nodeInfo.kubeletVersion** (string), required

    Kubelet Version reported by the node.
  + **nodeInfo.machineID** (string), required

    MachineID reported by the node. For unique machine identification in the cluster this field is preferred. Learn more from man(5) machine-id: <http://man7.org/linux/man-pages/man5/machine-id.5.html>
  + **nodeInfo.operatingSystem** (string), required

    The Operating System reported by the node
  + **nodeInfo.osImage** (string), required

    OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).
  + **nodeInfo.systemUUID** (string), required

    SystemUUID reported by the node. For unique machine identification MachineID is preferred. This field is specific to Red Hat hosts <https://access.redhat.com/documentation/en-us/red_hat_subscription_management/1/html/rhsm/uuid>
  + **nodeInfo.swap** (NodeSwapStatus)

    Swap Info reported by the node.

    *NodeSwapStatus represents swap memory information.*

    - **nodeInfo.swap.capacity** (int64)

      Total amount of swap memory in bytes.
* **phase** (string)

  NodePhase is the recently observed lifecycle phase of the node. More info: <https://kubernetes.io/docs/concepts/nodes/node/#phase> The field is never populated, and now is deprecated.

  Possible enum values:

  + `"Pending"` means the node has been created/added by the system, but not configured.
  + `"Running"` means the node has been configured and has Kubernetes components running.
  + `"Terminated"` means the node has been removed from the cluster.
* **runtimeHandlers** ([]NodeRuntimeHandler)

  *Atomic: will be replaced during a merge*

  The available runtime handlers.

  *NodeRuntimeHandler is a set of runtime handler information.*

  + **runtimeHandlers.features** (NodeRuntimeHandlerFeatures)

    Supported features.

    *NodeRuntimeHandlerFeatures is a set of features implemented by the runtime handler.*

    - **runtimeHandlers.features.recursiveReadOnlyMounts** (boolean)

      RecursiveReadOnlyMounts is set to true if the runtime handler supports RecursiveReadOnlyMounts.
    - **runtimeHandlers.features.userNamespaces** (boolean)

      UserNamespaces is set to true if the runtime handler supports UserNamespaces, including for volumes.
  + **runtimeHandlers.name** (string)

    Runtime handler name. Empty for the default runtime handler.
* **volumesAttached** ([]AttachedVolume)

  *Atomic: will be replaced during a merge*

  List of volumes that are attached to the node.

  *AttachedVolume describes a volume attached to a node*

  + **volumesAttached.devicePath** (string), required

    DevicePath represents the device path where the volume should be available
  + **volumesAttached.name** (string), required

    Name of the attached volume
* **volumesInUse** ([]string)

  *Atomic: will be replaced during a merge*

  List of attachable volumes in use (mounted) by the node.

## NodeList

NodeList is the whole list of all Nodes which have been registered with master.

---

* **apiVersion**: v1
* **kind**: NodeList
* **metadata** ([ListMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/#ListMeta))

  Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>
* **items** ([][Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node)), required

  List of nodes

## Operations

---

### `get` read the specified Node

#### HTTP Request

GET /api/v1/nodes/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the Node
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node)): OK

401: Unauthorized

### `get` read status of the specified Node

#### HTTP Request

GET /api/v1/nodes/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the Node
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node)): OK

401: Unauthorized

### `list` list or watch objects of kind Node

#### HTTP Request

GET /api/v1/nodes

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

200 ([NodeList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#NodeList)): OK

401: Unauthorized

### `create` create a Node

#### HTTP Request

POST /api/v1/nodes

#### Parameters

* **body**: [Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node)): OK

201 ([Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node)): Created

202 ([Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node)): Accepted

401: Unauthorized

### `update` replace the specified Node

#### HTTP Request

PUT /api/v1/nodes/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the Node
* **body**: [Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node)): OK

201 ([Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node)): Created

401: Unauthorized

### `update` replace status of the specified Node

#### HTTP Request

PUT /api/v1/nodes/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the Node
* **body**: [Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node)): OK

201 ([Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node)): Created

401: Unauthorized

### `patch` partially update the specified Node

#### HTTP Request

PATCH /api/v1/nodes/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the Node
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

200 ([Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node)): OK

201 ([Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node)): Created

401: Unauthorized

### `patch` partially update status of the specified Node

#### HTTP Request

PATCH /api/v1/nodes/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the Node
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

200 ([Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node)): OK

201 ([Node](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/#Node)): Created

401: Unauthorized

### `delete` delete a Node

#### HTTP Request

DELETE /api/v1/nodes/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the Node
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

### `deletecollection` delete collection of Node

#### HTTP Request

DELETE /api/v1/nodes

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
