# Feature Gates (removed)

This page contains list of feature gates that have been removed. The information on this page is for reference.
A removed feature gate is different from a GA'ed or deprecated one in that a removed one is
no longer recognized as a valid feature gate.
However, a GA'ed or a deprecated feature gate is still recognized by the corresponding Kubernetes
components although they are unable to cause any behavior differences in a cluster.

For feature gates that are still recognized by the Kubernetes components, please refer to
the [Alpha/Beta feature gate table](/docs/reference/command-line-tools-reference/feature-gates/#feature-gates-for-alpha-or-beta-features)
or the [Graduated/Deprecated feature gate table](/docs/reference/command-line-tools-reference/feature-gates/#feature-gates-for-graduated-or-deprecated-features)

### Feature gates that are removed

In the following table:

* The "From" column contains the Kubernetes release when a feature is introduced
  or its release stage is changed.
* The "To" column, if not empty, contains the last Kubernetes release in which
  you can still use a feature gate. If the feature stage is either "Deprecated"
  or "GA", the "To" column is the Kubernetes release when the feature is removed.

Feature Gates Removed

| Feature | Default | Stage | From | To |
| --- | --- | --- | --- | --- |
| `Accelerators` | `false` | Alpha | 1.6 | 1.10 |
| `Accelerators` | – | Deprecated | 1.11 | 1.11 |
| `AdmissionWebhookMatchConditions` | `false` | Alpha | 1.27 | 1.27 |
| `AdmissionWebhookMatchConditions` | `true` | Beta | 1.28 | 1.29 |
| `AdmissionWebhookMatchConditions` | `true` | GA | 1.30 | 1.32 |
| `AdvancedAuditing` | `false` | Alpha | 1.7 | 1.7 |
| `AdvancedAuditing` | `true` | Beta | 1.8 | 1.11 |
| `AdvancedAuditing` | `true` | GA | 1.12 | 1.27 |
| `AffinityInAnnotations` | `false` | Alpha | 1.6 | 1.7 |
| `AffinityInAnnotations` | – | Deprecated | 1.8 | 1.8 |
| `AggregatedDiscoveryEndpoint` | `false` | Alpha | 1.26 | 1.26 |
| `AggregatedDiscoveryEndpoint` | `true` | Beta | 1.27 | 1.29 |
| `AggregatedDiscoveryEndpoint` | `true` | GA | 1.30 | 1.32 |
| `AllowExtTrafficLocalEndpoints` | `false` | Beta | 1.4 | 1.6 |
| `AllowExtTrafficLocalEndpoints` | `true` | GA | 1.7 | 1.9 |
| `AllowInsecureBackendProxy` | `true` | Beta | 1.17 | 1.20 |
| `AllowInsecureBackendProxy` | `true` | GA | 1.21 | 1.25 |
| `APIListChunking` | `false` | Alpha | 1.8 | 1.8 |
| `APIListChunking` | `true` | Beta | 1.9 | 1.28 |
| `APIListChunking` | `true` | GA | 1.29 | 1.32 |
| `APIPriorityAndFairness` | `false` | Alpha | 1.18 | 1.19 |
| `APIPriorityAndFairness` | `true` | Beta | 1.20 | 1.28 |
| `APIPriorityAndFairness` | `true` | GA | 1.29 | 1.30 |
| `APISelfSubjectReview` | `false` | Alpha | 1.26 | 1.26 |
| `APISelfSubjectReview` | `true` | Beta | 1.27 | 1.27 |
| `APISelfSubjectReview` | `true` | GA | 1.28 | 1.29 |
| `AppArmor` | `true` | Beta | 1.4 | 1.30 |
| `AppArmor` | `true` | GA | 1.31 | 1.32 |
| `AppArmorFields` | `true` | Beta | 1.30 | 1.30 |
| `AppArmorFields` | `true` | GA | 1.31 | 1.32 |
| `AttachVolumeLimit` | `false` | Alpha | 1.11 | 1.11 |
| `AttachVolumeLimit` | `true` | Beta | 1.12 | 1.16 |
| `AttachVolumeLimit` | `true` | GA | 1.17 | 1.21 |
| `BalanceAttachedNodeVolumes` | `false` | Alpha | 1.11 | 1.21 |
| `BalanceAttachedNodeVolumes` | `false` | Deprecated | 1.22 | 1.22 |
| `BlockVolume` | `false` | Alpha | 1.9 | 1.12 |
| `BlockVolume` | `true` | Beta | 1.13 | 1.17 |
| `BlockVolume` | `true` | GA | 1.18 | 1.21 |
| `BoundServiceAccountTokenVolume` | `false` | Alpha | 1.13 | 1.20 |
| `BoundServiceAccountTokenVolume` | `true` | Beta | 1.21 | 1.21 |
| `BoundServiceAccountTokenVolume` | `true` | GA | 1.22 | 1.23 |
| `CloudDualStackNodeIPs` | `false` | Alpha | 1.27 | 1.28 |
| `CloudDualStackNodeIPs` | `true` | Beta | 1.29 | 1.29 |
| `CloudDualStackNodeIPs` | `true` | GA | 1.30 | 1.31 |
| `ConfigurableFSGroupPolicy` | `false` | Alpha | 1.18 | 1.19 |
| `ConfigurableFSGroupPolicy` | `true` | Beta | 1.20 | 1.22 |
| `ConfigurableFSGroupPolicy` | `true` | GA | 1.23 | 1.25 |
| `ConsistentHTTPGetHandlers` | `true` | GA | 1.25 | 1.30 |
| `ControllerManagerLeaderMigration` | `false` | Alpha | 1.21 | 1.21 |
| `ControllerManagerLeaderMigration` | `true` | Beta | 1.22 | 1.23 |
| `ControllerManagerLeaderMigration` | `true` | GA | 1.24 | 1.26 |
| `CPUManager` | `false` | Alpha | 1.8 | 1.9 |
| `CPUManager` | `true` | Beta | 1.10 | 1.25 |
| `CPUManager` | `true` | GA | 1.26 | 1.32 |
| `CRIContainerLogRotation` | `false` | Alpha | 1.10 | 1.10 |
| `CRIContainerLogRotation` | `true` | Beta | 1.11 | 1.20 |
| `CRIContainerLogRotation` | `true` | GA | 1.21 | 1.22 |
| `CronJobControllerV2` | `false` | Alpha | 1.20 | 1.20 |
| `CronJobControllerV2` | `true` | Beta | 1.21 | 1.21 |
| `CronJobControllerV2` | `true` | GA | 1.22 | 1.23 |
| `CronJobTimeZone` | `false` | Alpha | 1.24 | 1.24 |
| `CronJobTimeZone` | `true` | Beta | 1.25 | 1.26 |
| `CronJobTimeZone` | `true` | GA | 1.27 | 1.28 |
| `CSIBlockVolume` | `false` | Alpha | 1.11 | 1.13 |
| `CSIBlockVolume` | `true` | Beta | 1.14 | 1.17 |
| `CSIBlockVolume` | `true` | GA | 1.18 | 1.21 |
| `CSIDriverRegistry` | `false` | Alpha | 1.12 | 1.13 |
| `CSIDriverRegistry` | `true` | Beta | 1.14 | 1.17 |
| `CSIDriverRegistry` | `true` | GA | 1.18 | 1.21 |
| `CSIInlineVolume` | `false` | Alpha | 1.15 | 1.15 |
| `CSIInlineVolume` | `true` | Beta | 1.16 | 1.24 |
| `CSIInlineVolume` | `true` | GA | 1.25 | 1.26 |
| `CSIMigration` | `false` | Alpha | 1.14 | 1.16 |
| `CSIMigration` | `true` | Beta | 1.17 | 1.24 |
| `CSIMigration` | `true` | GA | 1.25 | 1.26 |
| `CSIMigrationAWS` | `false` | Alpha | 1.14 | 1.16 |
| `CSIMigrationAWS` | `false` | Beta | 1.17 | 1.22 |
| `CSIMigrationAWS` | `true` | Beta | 1.23 | 1.24 |
| `CSIMigrationAWS` | `true` | GA | 1.25 | 1.26 |
| `CSIMigrationAWSComplete` | `false` | Alpha | 1.17 | 1.20 |
| `CSIMigrationAWSComplete` | – | Deprecated | 1.21 | 1.21 |
| `CSIMigrationAzureDisk` | `false` | Alpha | 1.15 | 1.18 |
| `CSIMigrationAzureDisk` | `false` | Beta | 1.19 | 1.22 |
| `CSIMigrationAzureDisk` | `true` | Beta | 1.23 | 1.23 |
| `CSIMigrationAzureDisk` | `true` | GA | 1.24 | 1.26 |
| `CSIMigrationAzureDiskComplete` | `false` | Alpha | 1.17 | 1.20 |
| `CSIMigrationAzureDiskComplete` | – | Deprecated | 1.21 | 1.21 |
| `CSIMigrationAzureFile` | `false` | Alpha | 1.15 | 1.20 |
| `CSIMigrationAzureFile` | `false` | Beta | 1.21 | 1.23 |
| `CSIMigrationAzureFile` | `true` | Beta | 1.24 | 1.25 |
| `CSIMigrationAzureFile` | `true` | GA | 1.26 | 1.29 |
| `CSIMigrationAzureFileComplete` | `false` | Alpha | 1.17 | 1.20 |
| `CSIMigrationAzureFileComplete` | – | Deprecated | 1.21 | 1.21 |
| `CSIMigrationGCE` | `false` | Alpha | 1.14 | 1.16 |
| `CSIMigrationGCE` | `false` | Beta | 1.17 | 1.22 |
| `CSIMigrationGCE` | `true` | Beta | 1.23 | 1.24 |
| `CSIMigrationGCE` | `true` | GA | 1.25 | 1.27 |
| `CSIMigrationGCEComplete` | `false` | Alpha | 1.17 | 1.20 |
| `CSIMigrationGCEComplete` | – | Deprecated | 1.21 | 1.21 |
| `CSIMigrationOpenStack` | `false` | Alpha | 1.14 | 1.17 |
| `CSIMigrationOpenStack` | `true` | Beta | 1.18 | 1.23 |
| `CSIMigrationOpenStack` | `true` | GA | 1.24 | 1.25 |
| `CSIMigrationOpenStackComplete` | `false` | Alpha | 1.17 | 1.20 |
| `CSIMigrationOpenStackComplete` | – | Deprecated | 1.21 | 1.21 |
| `CSIMigrationRBD` | `false` | Alpha | 1.23 | 1.27 |
| `CSIMigrationRBD` | `false` | Deprecated | 1.28 | 1.30 |
| `CSIMigrationvSphere` | `false` | Alpha | 1.18 | 1.18 |
| `CSIMigrationvSphere` | `false` | Beta | 1.19 | 1.24 |
| `CSIMigrationvSphere` | `true` | Beta | 1.25 | 1.25 |
| `CSIMigrationvSphere` | `true` | GA | 1.26 | 1.28 |
| `CSIMigrationvSphereComplete` | `false` | Beta | 1.19 | 1.21 |
| `CSIMigrationvSphereComplete` | – | Deprecated | 1.22 | 1.22 |
| `CSINodeExpandSecret` | `false` | Alpha | 1.25 | 1.26 |
| `CSINodeExpandSecret` | `true` | Beta | 1.27 | 1.28 |
| `CSINodeExpandSecret` | `true` | GA | 1.29 | 1.30 |
| `CSINodeInfo` | `false` | Alpha | 1.12 | 1.13 |
| `CSINodeInfo` | `true` | Beta | 1.14 | 1.16 |
| `CSINodeInfo` | `true` | GA | 1.17 | 1.22 |
| `CSIPersistentVolume` | `false` | Alpha | 1.9 | 1.9 |
| `CSIPersistentVolume` | `true` | Beta | 1.10 | 1.12 |
| `CSIPersistentVolume` | `true` | GA | 1.13 | 1.16 |
| `CSIServiceAccountToken` | `false` | Alpha | 1.20 | 1.20 |
| `CSIServiceAccountToken` | `true` | Beta | 1.21 | 1.21 |
| `CSIServiceAccountToken` | `true` | GA | 1.22 | 1.24 |
| `CSIStorageCapacity` | `false` | Alpha | 1.19 | 1.20 |
| `CSIStorageCapacity` | `true` | Beta | 1.21 | 1.23 |
| `CSIStorageCapacity` | `true` | GA | 1.24 | 1.27 |
| `CSIVolumeFSGroupPolicy` | `false` | Alpha | 1.19 | 1.19 |
| `CSIVolumeFSGroupPolicy` | `true` | Beta | 1.20 | 1.22 |
| `CSIVolumeFSGroupPolicy` | `true` | GA | 1.23 | 1.25 |
| `CSRDuration` | `true` | Beta | 1.22 | 1.23 |
| `CSRDuration` | `true` | GA | 1.24 | 1.25 |
| `CustomPodDNS` | `false` | Alpha | 1.9 | 1.9 |
| `CustomPodDNS` | `true` | Beta | 1.10 | 1.13 |
| `CustomPodDNS` | `true` | GA | 1.14 | 1.16 |
| `CustomResourceDefaulting` | `false` | Alpha | 1.15 | 1.15 |
| `CustomResourceDefaulting` | `true` | Beta | 1.16 | 1.16 |
| `CustomResourceDefaulting` | `true` | GA | 1.17 | 1.18 |
| `CustomResourcePublishOpenAPI` | `false` | Alpha | 1.14 | 1.14 |
| `CustomResourcePublishOpenAPI` | `true` | Beta | 1.15 | 1.15 |
| `CustomResourcePublishOpenAPI` | `true` | GA | 1.16 | 1.18 |
| `CustomResourceSubresources` | `false` | Alpha | 1.10 | 1.10 |
| `CustomResourceSubresources` | `true` | Beta | 1.11 | 1.15 |
| `CustomResourceSubresources` | `true` | GA | 1.16 | 1.18 |
| `CustomResourceValidation` | `false` | Alpha | 1.8 | 1.8 |
| `CustomResourceValidation` | `true` | Beta | 1.9 | 1.15 |
| `CustomResourceValidation` | `true` | GA | 1.16 | 1.18 |
| `CustomResourceValidationExpressions` | `false` | Alpha | 1.23 | 1.24 |
| `CustomResourceValidationExpressions` | `true` | Beta | 1.25 | 1.28 |
| `CustomResourceValidationExpressions` | `true` | GA | 1.29 | 1.30 |
| `CustomResourceWebhookConversion` | `false` | Alpha | 1.13 | 1.14 |
| `CustomResourceWebhookConversion` | `true` | Beta | 1.15 | 1.15 |
| `CustomResourceWebhookConversion` | `true` | GA | 1.16 | 1.18 |
| `DaemonSetUpdateSurge` | `false` | Alpha | 1.21 | 1.21 |
| `DaemonSetUpdateSurge` | `true` | Beta | 1.22 | 1.24 |
| `DaemonSetUpdateSurge` | `true` | GA | 1.25 | 1.26 |
| `DefaultHostNetworkHostPortsInPodTemplates` | `false` | Deprecated | 1.28 | 1.30 |
| `DefaultPodTopologySpread` | `false` | Alpha | 1.19 | 1.19 |
| `DefaultPodTopologySpread` | `true` | Beta | 1.20 | 1.23 |
| `DefaultPodTopologySpread` | `true` | GA | 1.24 | 1.25 |
| `DelegateFSGroupToCSIDriver` | `false` | Alpha | 1.22 | 1.22 |
| `DelegateFSGroupToCSIDriver` | `true` | Beta | 1.23 | 1.25 |
| `DelegateFSGroupToCSIDriver` | `true` | GA | 1.26 | 1.27 |
| `DevicePluginCDIDevices` | `false` | Alpha | 1.28 | 1.28 |
| `DevicePluginCDIDevices` | `true` | Beta | 1.29 | 1.30 |
| `DevicePluginCDIDevices` | `true` | GA | 1.31 | 1.33 |
| `DevicePlugins` | `false` | Alpha | 1.8 | 1.9 |
| `DevicePlugins` | `true` | Beta | 1.10 | 1.25 |
| `DevicePlugins` | `true` | GA | 1.26 | 1.27 |
| `DisableAcceleratorUsageMetrics` | `false` | Alpha | 1.19 | 1.19 |
| `DisableAcceleratorUsageMetrics` | `true` | Beta | 1.20 | 1.24 |
| `DisableAcceleratorUsageMetrics` | `true` | GA | 1.25 | 1.27 |
| `DisableCloudProviders` | `false` | Alpha | 1.22 | 1.28 |
| `DisableCloudProviders` | `true` | Beta | 1.29 | 1.30 |
| `DisableCloudProviders` | `true` | GA | 1.31 | 1.32 |
| `DisableKubeletCloudCredentialProviders` | `false` | Alpha | 1.23 | 1.28 |
| `DisableKubeletCloudCredentialProviders` | `true` | Beta | 1.29 | 1.30 |
| `DisableKubeletCloudCredentialProviders` | `true` | GA | 1.31 | 1.32 |
| `DownwardAPIHugePages` | `false` | Alpha | 1.20 | 1.20 |
| `DownwardAPIHugePages` | `false` | Beta | 1.21 | 1.21 |
| `DownwardAPIHugePages` | `true` | Beta | 1.22 | 1.26 |
| `DownwardAPIHugePages` | `true` | GA | 1.27 | 1.28 |
| `DRAControlPlaneController` | `false` | Alpha | 1.26 | 1.31 |
| `DryRun` | `false` | Alpha | 1.12 | 1.12 |
| `DryRun` | `true` | Beta | 1.13 | 1.18 |
| `DryRun` | `true` | GA | 1.19 | 1.27 |
| `DynamicAuditing` | `false` | Alpha | 1.13 | 1.18 |
| `DynamicAuditing` | – | Deprecated | 1.19 | 1.19 |
| `DynamicKubeletConfig` | `false` | Alpha | 1.4 | 1.10 |
| `DynamicKubeletConfig` | `true` | Beta | 1.11 | 1.21 |
| `DynamicKubeletConfig` | `false` | Deprecated | 1.22 | 1.25 |
| `DynamicProvisioningScheduling` | `false` | Alpha | 1.11 | 1.11 |
| `DynamicProvisioningScheduling` | – | Deprecated | 1.12 | – |
| `DynamicVolumeProvisioning` | `true` | Alpha | 1.3 | 1.7 |
| `DynamicVolumeProvisioning` | `true` | GA | 1.8 | 1.12 |
| `EfficientWatchResumption` | `false` | Alpha | 1.20 | 1.20 |
| `EfficientWatchResumption` | `true` | Beta | 1.21 | 1.23 |
| `EfficientWatchResumption` | `true` | GA | 1.24 | 1.32 |
| `EnableAggregatedDiscoveryTimeout` | `true` | Deprecated | 1.16 | 1.17 |
| `EnableEquivalenceClassCache` | `false` | Alpha | 1.8 | 1.12 |
| `EnableEquivalenceClassCache` | – | Deprecated | 1.13 | 1.23 |
| `EndpointSlice` | `false` | Alpha | 1.16 | 1.16 |
| `EndpointSlice` | `false` | Beta | 1.17 | 1.17 |
| `EndpointSlice` | `true` | Beta | 1.18 | 1.20 |
| `EndpointSlice` | `true` | GA | 1.21 | 1.24 |
| `EndpointSliceNodeName` | `false` | Alpha | 1.20 | 1.20 |
| `EndpointSliceNodeName` | `true` | GA | 1.21 | 1.24 |
| `EndpointSliceProxying` | `false` | Alpha | 1.18 | 1.18 |
| `EndpointSliceProxying` | `true` | Beta | 1.19 | 1.21 |
| `EndpointSliceProxying` | `true` | GA | 1.22 | 1.24 |
| `EndpointSliceTerminatingCondition` | `false` | Alpha | 1.20 | 1.21 |
| `EndpointSliceTerminatingCondition` | `true` | Beta | 1.22 | 1.25 |
| `EndpointSliceTerminatingCondition` | `true` | GA | 1.26 | 1.27 |
| `EphemeralContainers` | `false` | Alpha | 1.16 | 1.22 |
| `EphemeralContainers` | `true` | Beta | 1.23 | 1.24 |
| `EphemeralContainers` | `true` | GA | 1.25 | 1.26 |
| `EvenPodsSpread` | `false` | Alpha | 1.16 | 1.17 |
| `EvenPodsSpread` | `true` | Beta | 1.18 | 1.18 |
| `EvenPodsSpread` | `true` | GA | 1.19 | 1.21 |
| `ExpandCSIVolumes` | `false` | Alpha | 1.14 | 1.15 |
| `ExpandCSIVolumes` | `true` | Beta | 1.16 | 1.23 |
| `ExpandCSIVolumes` | `true` | GA | 1.24 | 1.26 |
| `ExpandedDNSConfig` | `false` | Alpha | 1.22 | 1.25 |
| `ExpandedDNSConfig` | `true` | Beta | 1.26 | 1.27 |
| `ExpandedDNSConfig` | `true` | GA | 1.28 | 1.29 |
| `ExpandInUsePersistentVolumes` | `false` | Alpha | 1.11 | 1.14 |
| `ExpandInUsePersistentVolumes` | `true` | Beta | 1.15 | 1.23 |
| `ExpandInUsePersistentVolumes` | `true` | GA | 1.24 | 1.26 |
| `ExpandPersistentVolumes` | `false` | Alpha | 1.8 | 1.10 |
| `ExpandPersistentVolumes` | `true` | Beta | 1.11 | 1.23 |
| `ExpandPersistentVolumes` | `true` | GA | 1.24 | 1.26 |
| `ExperimentalCriticalPodAnnotation` | `false` | Alpha | 1.5 | 1.12 |
| `ExperimentalCriticalPodAnnotation` | `false` | Deprecated | 1.13 | 1.16 |
| `ExperimentalHostUserNamespaceDefaulting` | `false` | Beta | 1.5 | 1.27 |
| `ExperimentalHostUserNamespaceDefaulting` | `false` | Deprecated | 1.28 | 1.29 |
| `ExternalPolicyForExternalIP` | `true` | GA | 1.18 | 1.22 |
| `GCERegionalPersistentDisk` | `true` | Beta | 1.10 | 1.12 |
| `GCERegionalPersistentDisk` | `true` | GA | 1.13 | 1.16 |
| `GenericEphemeralVolume` | `false` | Alpha | 1.19 | 1.20 |
| `GenericEphemeralVolume` | `true` | Beta | 1.21 | 1.22 |
| `GenericEphemeralVolume` | `true` | GA | 1.23 | 1.24 |
| `GRPCContainerProbe` | `false` | Alpha | 1.23 | 1.23 |
| `GRPCContainerProbe` | `true` | Beta | 1.24 | 1.26 |
| `GRPCContainerProbe` | `true` | GA | 1.27 | 1.28 |
| `HPAContainerMetrics` | `false` | Alpha | 1.20 | 1.26 |
| `HPAContainerMetrics` | `true` | Beta | 1.27 | 1.29 |
| `HPAContainerMetrics` | `true` | GA | 1.30 | 1.31 |
| `HugePages` | `false` | Alpha | 1.8 | 1.9 |
| `HugePages` | `true` | Beta | 1.10 | 1.13 |
| `HugePages` | `true` | GA | 1.14 | 1.16 |
| `HugePageStorageMediumSize` | `false` | Alpha | 1.18 | 1.18 |
| `HugePageStorageMediumSize` | `true` | Beta | 1.19 | 1.21 |
| `HugePageStorageMediumSize` | `true` | GA | 1.22 | 1.24 |
| `HyperVContainer` | `false` | Alpha | 1.10 | 1.19 |
| `HyperVContainer` | `false` | Deprecated | 1.20 | 1.20 |
| `IdentifyPodOS` | `false` | Alpha | 1.23 | 1.23 |
| `IdentifyPodOS` | `true` | Beta | 1.24 | 1.24 |
| `IdentifyPodOS` | `true` | GA | 1.25 | 1.26 |
| `ImmutableEphemeralVolumes` | `false` | Alpha | 1.18 | 1.18 |
| `ImmutableEphemeralVolumes` | `true` | Beta | 1.19 | 1.20 |
| `ImmutableEphemeralVolumes` | `true` | GA | 1.21 | 1.24 |
| `IndexedJob` | `false` | Alpha | 1.21 | 1.21 |
| `IndexedJob` | `true` | Beta | 1.22 | 1.23 |
| `IndexedJob` | `true` | GA | 1.24 | 1.25 |
| `IngressClassNamespacedParams` | `false` | Alpha | 1.21 | 1.21 |
| `IngressClassNamespacedParams` | `true` | Beta | 1.22 | 1.22 |
| `IngressClassNamespacedParams` | `true` | GA | 1.23 | 1.24 |
| `Initializers` | `false` | Alpha | 1.7 | 1.13 |
| `Initializers` | – | Deprecated | 1.14 | 1.14 |
| `InTreePluginAWSUnregister` | `false` | Alpha | 1.21 | 1.30 |
| `InTreePluginAzureDiskUnregister` | `false` | Alpha | 1.21 | 1.30 |
| `InTreePluginAzureFileUnregister` | `false` | Alpha | 1.21 | 1.30 |
| `InTreePluginGCEUnregister` | `false` | Alpha | 1.21 | 1.30 |
| `InTreePluginOpenStackUnregister` | `false` | Alpha | 1.21 | 1.30 |
| `InTreePluginRBDUnregister` | `false` | Alpha | 1.23 | 1.27 |
| `InTreePluginRBDUnregister` | `false` | Deprecated | 1.28 | 1.30 |
| `InTreePluginvSphereUnregister` | `false` | Alpha | 1.21 | 1.30 |
| `IPTablesOwnershipCleanup` | `false` | Alpha | 1.25 | 1.26 |
| `IPTablesOwnershipCleanup` | `true` | Beta | 1.27 | 1.27 |
| `IPTablesOwnershipCleanup` | `true` | GA | 1.28 | 1.29 |
| `IPv6DualStack` | `false` | Alpha | 1.15 | 1.20 |
| `IPv6DualStack` | `true` | Beta | 1.21 | 1.22 |
| `IPv6DualStack` | `true` | GA | 1.23 | 1.24 |
| `JobMutableNodeSchedulingDirectives` | `true` | Beta | 1.23 | 1.26 |
| `JobMutableNodeSchedulingDirectives` | `true` | GA | 1.27 | 1.28 |
| `JobPodFailurePolicy` | `false` | Alpha | 1.25 | 1.25 |
| `JobPodFailurePolicy` | `true` | Beta | 1.26 | 1.30 |
| `JobPodFailurePolicy` | `true` | GA | 1.31 | 1.32 |
| `JobReadyPods` | `false` | Alpha | 1.23 | 1.23 |
| `JobReadyPods` | `true` | Beta | 1.24 | 1.28 |
| `JobReadyPods` | `true` | GA | 1.29 | 1.30 |
| `JobTrackingWithFinalizers` | `false` | Alpha | 1.22 | 1.22 |
| `JobTrackingWithFinalizers` | `false` | Beta | 1.23 | 1.24 |
| `JobTrackingWithFinalizers` | `true` | Beta | 1.25 | 1.25 |
| `JobTrackingWithFinalizers` | `true` | GA | 1.26 | 1.28 |
| `KMSv2` | `false` | Alpha | 1.25 | 1.26 |
| `KMSv2` | `true` | Beta | 1.27 | 1.28 |
| `KMSv2` | `true` | GA | 1.29 | 1.31 |
| `KMSv2KDF` | `false` | Beta | 1.28 | 1.28 |
| `KMSv2KDF` | `true` | GA | 1.29 | 1.31 |
| `KubeletConfigFile` | `false` | Alpha | 1.8 | 1.9 |
| `KubeletConfigFile` | – | Deprecated | 1.10 | 1.10 |
| `KubeletCredentialProviders` | `false` | Alpha | 1.20 | 1.23 |
| `KubeletCredentialProviders` | `true` | Beta | 1.24 | 1.25 |
| `KubeletCredentialProviders` | `true` | GA | 1.26 | 1.28 |
| `KubeletPluginsWatcher` | `false` | Alpha | 1.11 | 1.11 |
| `KubeletPluginsWatcher` | `true` | Beta | 1.12 | 1.12 |
| `KubeletPluginsWatcher` | `true` | GA | 1.13 | 1.16 |
| `KubeletPodResources` | `false` | Alpha | 1.13 | 1.14 |
| `KubeletPodResources` | `true` | Beta | 1.15 | 1.27 |
| `KubeletPodResources` | `true` | GA | 1.28 | 1.29 |
| `KubeletPodResourcesGetAllocatable` | `false` | Alpha | 1.21 | 1.22 |
| `KubeletPodResourcesGetAllocatable` | `true` | Beta | 1.23 | 1.27 |
| `KubeletPodResourcesGetAllocatable` | `true` | GA | 1.28 | 1.29 |
| `KubeProxyDrainingTerminatingNodes` | `false` | Alpha | 1.28 | 1.30 |
| `KubeProxyDrainingTerminatingNodes` | `true` | Beta | 1.30 | 1.30 |
| `KubeProxyDrainingTerminatingNodes` | `true` | GA | 1.31 | 1.32 |
| `LegacyNodeRoleBehavior` | `false` | Alpha | 1.16 | 1.18 |
| `LegacyNodeRoleBehavior` | `true` | Beta | 1.19 | 1.20 |
| `LegacyNodeRoleBehavior` | `false` | GA | 1.21 | 1.22 |
| `LegacyServiceAccountTokenCleanUp` | `false` | Alpha | 1.28 | 1.28 |
| `LegacyServiceAccountTokenCleanUp` | `true` | Beta | 1.29 | 1.29 |
| `LegacyServiceAccountTokenCleanUp` | `true` | GA | 1.30 | 1.31 |
| `LegacyServiceAccountTokenNoAutoGeneration` | `true` | Beta | 1.24 | 1.25 |
| `LegacyServiceAccountTokenNoAutoGeneration` | `true` | GA | 1.26 | 1.28 |
| `LegacyServiceAccountTokenTracking` | `false` | Alpha | 1.26 | 1.26 |
| `LegacyServiceAccountTokenTracking` | `true` | Beta | 1.27 | 1.27 |
| `LegacyServiceAccountTokenTracking` | `true` | GA | 1.28 | 1.29 |
| `LocalStorageCapacityIsolation` | `false` | Alpha | 1.7 | 1.9 |
| `LocalStorageCapacityIsolation` | `true` | Beta | 1.10 | 1.24 |
| `LocalStorageCapacityIsolation` | `true` | GA | 1.25 | 1.26 |
| `MinDomainsInPodTopologySpread` | `false` | Alpha | 1.24 | 1.24 |
| `MinDomainsInPodTopologySpread` | `false` | Beta | 1.25 | 1.26 |
| `MinDomainsInPodTopologySpread` | `true` | Beta | 1.27 | 1.29 |
| `MinDomainsInPodTopologySpread` | `true` | GA | 1.30 | 1.31 |
| `MinimizeIPTablesRestore` | `false` | Alpha | 1.26 | 1.26 |
| `MinimizeIPTablesRestore` | `true` | Beta | 1.27 | 1.27 |
| `MinimizeIPTablesRestore` | `true` | GA | 1.28 | 1.29 |
| `MixedProtocolLBService` | `false` | Alpha | 1.20 | 1.23 |
| `MixedProtocolLBService` | `true` | Beta | 1.24 | 1.25 |
| `MixedProtocolLBService` | `true` | GA | 1.26 | 1.27 |
| `MountContainers` | `false` | Alpha | 1.9 | 1.16 |
| `MountContainers` | `false` | Deprecated | 1.17 | 1.17 |
| `MountPropagation` | `false` | Alpha | 1.8 | 1.9 |
| `MountPropagation` | `true` | Beta | 1.10 | 1.11 |
| `MountPropagation` | `true` | GA | 1.12 | 1.14 |
| `MultiCIDRRangeAllocator` | `false` | Alpha | 1.25 | 1.28 |
| `NamespaceDefaultLabelName` | `true` | Beta | 1.21 | 1.21 |
| `NamespaceDefaultLabelName` | `true` | GA | 1.22 | 1.23 |
| `NetworkPolicyEndPort` | `false` | Alpha | 1.21 | 1.21 |
| `NetworkPolicyEndPort` | `true` | Beta | 1.22 | 1.24 |
| `NetworkPolicyEndPort` | `true` | GA | 1.25 | 1.26 |
| `NetworkPolicyStatus` | `false` | Alpha | 1.24 | 1.27 |
| `NewVolumeManagerReconstruction` | `false` | Alpha | 1.25 | 1.26 |
| `NewVolumeManagerReconstruction` | `true` | Beta | 1.27 | 1.29 |
| `NewVolumeManagerReconstruction` | `true` | GA | 1.30 | 1.31 |
| `NodeDisruptionExclusion` | `false` | Alpha | 1.16 | 1.18 |
| `NodeDisruptionExclusion` | `true` | Beta | 1.19 | 1.20 |
| `NodeDisruptionExclusion` | `true` | GA | 1.21 | 1.22 |
| `NodeLease` | `false` | Alpha | 1.12 | 1.13 |
| `NodeLease` | `true` | Beta | 1.14 | 1.16 |
| `NodeLease` | `true` | GA | 1.17 | 1.23 |
| `NodeOutOfServiceVolumeDetach` | `false` | Alpha | 1.24 | 1.25 |
| `NodeOutOfServiceVolumeDetach` | `true` | Beta | 1.26 | 1.27 |
| `NodeOutOfServiceVolumeDetach` | `true` | GA | 1.28 | 1.31 |
| `NonPreemptingPriority` | `false` | Alpha | 1.15 | 1.18 |
| `NonPreemptingPriority` | `true` | Beta | 1.19 | 1.23 |
| `NonPreemptingPriority` | `true` | GA | 1.24 | 1.25 |
| `OpenAPIV3` | `false` | Alpha | 1.23 | 1.23 |
| `OpenAPIV3` | `true` | Beta | 1.24 | 1.26 |
| `OpenAPIV3` | `true` | GA | 1.27 | 1.28 |
| `PDBUnhealthyPodEvictionPolicy` | `false` | Alpha | 1.26 | 1.26 |
| `PDBUnhealthyPodEvictionPolicy` | `true` | Beta | 1.27 | 1.30 |
| `PDBUnhealthyPodEvictionPolicy` | `true` | GA | 1.31 | 1.32 |
| `PersistentLocalVolumes` | `false` | Alpha | 1.7 | 1.9 |
| `PersistentLocalVolumes` | `true` | Beta | 1.10 | 1.13 |
| `PersistentLocalVolumes` | `true` | GA | 1.14 | 1.16 |
| `PersistentVolumeLastPhaseTransitionTime` | `false` | Alpha | 1.28 | 1.28 |
| `PersistentVolumeLastPhaseTransitionTime` | `true` | Beta | 1.29 | 1.30 |
| `PersistentVolumeLastPhaseTransitionTime` | `true` | GA | 1.31 | 1.32 |
| `PodAffinityNamespaceSelector` | `false` | Alpha | 1.21 | 1.21 |
| `PodAffinityNamespaceSelector` | `true` | Beta | 1.22 | 1.23 |
| `PodAffinityNamespaceSelector` | `true` | GA | 1.24 | 1.25 |
| `PodDisruptionBudget` | `false` | Alpha | 1.3 | 1.4 |
| `PodDisruptionBudget` | `true` | Beta | 1.5 | 1.20 |
| `PodDisruptionBudget` | `true` | GA | 1.21 | 1.25 |
| `PodDisruptionConditions` | `false` | Alpha | 1.25 | 1.25 |
| `PodDisruptionConditions` | `true` | Beta | 1.26 | 1.30 |
| `PodDisruptionConditions` | `true` | GA | 1.31 | 1.33 |
| `PodHasNetworkCondition` | `false` | Alpha | 1.25 | 1.27 |
| `PodHostIPs` | `false` | Alpha | 1.28 | 1.28 |
| `PodHostIPs` | `true` | Beta | 1.29 | 1.30 |
| `PodHostIPs` | `true` | GA | 1.30 | 1.31 |
| `PodOverhead` | `false` | Alpha | 1.16 | 1.17 |
| `PodOverhead` | `true` | Beta | 1.18 | 1.23 |
| `PodOverhead` | `true` | GA | 1.24 | 1.25 |
| `PodPriority` | `false` | Alpha | 1.8 | 1.10 |
| `PodPriority` | `true` | Beta | 1.11 | 1.13 |
| `PodPriority` | `true` | GA | 1.14 | 1.18 |
| `PodReadinessGates` | `false` | Alpha | 1.11 | 1.11 |
| `PodReadinessGates` | `true` | Beta | 1.12 | 1.13 |
| `PodReadinessGates` | `true` | GA | 1.14 | 1.16 |
| `PodSecurity` | `false` | Alpha | 1.22 | 1.22 |
| `PodSecurity` | `true` | Beta | 1.23 | 1.24 |
| `PodSecurity` | `true` | GA | 1.25 | 1.27 |
| `PodShareProcessNamespace` | `false` | Alpha | 1.10 | 1.11 |
| `PodShareProcessNamespace` | `true` | Beta | 1.12 | 1.16 |
| `PodShareProcessNamespace` | `true` | GA | 1.17 | 1.19 |
| `PreferNominatedNode` | `false` | Alpha | 1.21 | 1.21 |
| `PreferNominatedNode` | `true` | Beta | 1.22 | 1.23 |
| `PreferNominatedNode` | `true` | GA | 1.24 | 1.25 |
| `ProbeTerminationGracePeriod` | `false` | Alpha | 1.21 | 1.21 |
| `ProbeTerminationGracePeriod` | `false` | Beta | 1.22 | 1.24 |
| `ProbeTerminationGracePeriod` | `true` | Beta | 1.25 | 1.27 |
| `ProbeTerminationGracePeriod` | `true` | GA | 1.28 | 1.28 |
| `ProxyTerminatingEndpoints` | `false` | Alpha | 1.22 | 1.25 |
| `ProxyTerminatingEndpoints` | `true` | Beta | 1.26 | 1.27 |
| `ProxyTerminatingEndpoints` | `true` | GA | 1.28 | 1.29 |
| `PVCProtection` | `false` | Alpha | 1.9 | 1.9 |
| `PVCProtection` | – | Deprecated | 1.10 | 1.10 |
| `ReadOnlyAPIDataVolumes` | `true` | Beta | 1.8 | 1.9 |
| `ReadOnlyAPIDataVolumes` | – | GA | 1.10 | 1.10 |
| `ReadWriteOncePod` | `false` | Alpha | 1.22 | 1.26 |
| `ReadWriteOncePod` | `true` | Beta | 1.27 | 1.28 |
| `ReadWriteOncePod` | `true` | GA | 1.29 | 1.30 |
| `RemainingItemCount` | `false` | Alpha | 1.15 | 1.15 |
| `RemainingItemCount` | `true` | Beta | 1.16 | 1.28 |
| `RemainingItemCount` | `true` | GA | 1.29 | 1.32 |
| `RemoveSelfLink` | `false` | Alpha | 1.16 | 1.19 |
| `RemoveSelfLink` | `true` | Beta | 1.20 | 1.23 |
| `RemoveSelfLink` | `true` | GA | 1.24 | 1.29 |
| `RequestManagement` | `false` | Alpha | 1.15 | 1.16 |
| `RequestManagement` | – | Deprecated | 1.17 | 1.17 |
| `ResourceLimitsPriorityFunction` | `false` | Alpha | 1.9 | 1.18 |
| `ResourceLimitsPriorityFunction` | – | Deprecated | 1.19 | 1.19 |
| `ResourceQuotaScopeSelectors` | `false` | Alpha | 1.11 | 1.11 |
| `ResourceQuotaScopeSelectors` | `true` | Beta | 1.12 | 1.16 |
| `ResourceQuotaScopeSelectors` | `true` | GA | 1.17 | 1.18 |
| `RetroactiveDefaultStorageClass` | `false` | Alpha | 1.25 | 1.25 |
| `RetroactiveDefaultStorageClass` | `true` | Beta | 1.26 | 1.27 |
| `RetroactiveDefaultStorageClass` | `true` | GA | 1.28 | 1.28 |
| `RootCAConfigMap` | `false` | Alpha | 1.13 | 1.19 |
| `RootCAConfigMap` | `true` | Beta | 1.20 | 1.20 |
| `RootCAConfigMap` | `true` | GA | 1.21 | 1.22 |
| `RotateKubeletClientCertificate` | `true` | Beta | 1.8 | 1.18 |
| `RotateKubeletClientCertificate` | `true` | GA | 1.19 | 1.21 |
| `RunAsGroup` | `true` | Beta | 1.14 | 1.20 |
| `RunAsGroup` | `true` | GA | 1.21 | 1.22 |
| `RuntimeClass` | `false` | Alpha | 1.12 | 1.13 |
| `RuntimeClass` | `true` | Beta | 1.14 | 1.19 |
| `RuntimeClass` | `true` | GA | 1.20 | 1.24 |
| `ScheduleDaemonSetPods` | `false` | Alpha | 1.11 | 1.11 |
| `ScheduleDaemonSetPods` | `true` | Beta | 1.12 | 1.16 |
| `ScheduleDaemonSetPods` | `true` | GA | 1.17 | 1.18 |
| `SCTPSupport` | `false` | Alpha | 1.12 | 1.18 |
| `SCTPSupport` | `true` | Beta | 1.19 | 1.19 |
| `SCTPSupport` | `true` | GA | 1.20 | 1.22 |
| `SeccompDefault` | `false` | Alpha | 1.22 | 1.24 |
| `SeccompDefault` | `true` | Beta | 1.25 | 1.26 |
| `SeccompDefault` | `true` | GA | 1.27 | 1.28 |
| `SecurityContextDeny` | `false` | Alpha | 1.27 | 1.29 |
| `SelectorIndex` | `false` | Alpha | 1.18 | 1.18 |
| `SelectorIndex` | `true` | Beta | 1.19 | 1.19 |
| `SelectorIndex` | `true` | GA | 1.20 | 1.25 |
| `ServerSideApply` | `false` | Alpha | 1.14 | 1.15 |
| `ServerSideApply` | `true` | Beta | 1.16 | 1.21 |
| `ServerSideApply` | `true` | GA | 1.22 | 1.31 |
| `ServerSideFieldValidation` | `false` | Alpha | 1.23 | 1.24 |
| `ServerSideFieldValidation` | `true` | Beta | 1.25 | 1.26 |
| `ServerSideFieldValidation` | `true` | GA | 1.27 | 1.31 |
| `ServiceAccountIssuerDiscovery` | `false` | Alpha | 1.18 | 1.19 |
| `ServiceAccountIssuerDiscovery` | `true` | Beta | 1.20 | 1.20 |
| `ServiceAccountIssuerDiscovery` | `true` | GA | 1.21 | 1.23 |
| `ServiceAppProtocol` | `false` | Alpha | 1.18 | 1.18 |
| `ServiceAppProtocol` | `true` | Beta | 1.19 | 1.19 |
| `ServiceAppProtocol` | `true` | GA | 1.20 | 1.22 |
| `ServiceInternalTrafficPolicy` | `false` | Alpha | 1.21 | 1.21 |
| `ServiceInternalTrafficPolicy` | `true` | Beta | 1.22 | 1.25 |
| `ServiceInternalTrafficPolicy` | `true` | GA | 1.26 | 1.27 |
| `ServiceIPStaticSubrange` | `false` | Alpha | 1.24 | 1.24 |
| `ServiceIPStaticSubrange` | `true` | Beta | 1.25 | 1.25 |
| `ServiceIPStaticSubrange` | `true` | GA | 1.26 | 1.27 |
| `ServiceLBNodePortControl` | `false` | Alpha | 1.20 | 1.21 |
| `ServiceLBNodePortControl` | `true` | Beta | 1.22 | 1.23 |
| `ServiceLBNodePortControl` | `true` | GA | 1.24 | 1.25 |
| `ServiceLoadBalancerClass` | `false` | Alpha | 1.21 | 1.21 |
| `ServiceLoadBalancerClass` | `true` | Beta | 1.22 | 1.23 |
| `ServiceLoadBalancerClass` | `true` | GA | 1.24 | 1.25 |
| `ServiceLoadBalancerFinalizer` | `false` | Alpha | 1.15 | 1.15 |
| `ServiceLoadBalancerFinalizer` | `true` | Beta | 1.16 | 1.16 |
| `ServiceLoadBalancerFinalizer` | `true` | GA | 1.17 | 1.20 |
| `ServiceNodeExclusion` | `false` | Alpha | 1.8 | 1.18 |
| `ServiceNodeExclusion` | `true` | Beta | 1.19 | 1.20 |
| `ServiceNodeExclusion` | `true` | GA | 1.21 | 1.22 |
| `ServiceNodePortStaticSubrange` | `false` | Alpha | 1.27 | 1.27 |
| `ServiceNodePortStaticSubrange` | `true` | Beta | 1.28 | 1.28 |
| `ServiceNodePortStaticSubrange` | `true` | GA | 1.29 | 1.30 |
| `ServiceTopology` | `false` | Alpha | 1.17 | 1.19 |
| `ServiceTopology` | `false` | Deprecated | 1.20 | 1.22 |
| `SetHostnameAsFQDN` | `false` | Alpha | 1.19 | 1.19 |
| `SetHostnameAsFQDN` | `true` | Beta | 1.20 | 1.21 |
| `SetHostnameAsFQDN` | `true` | GA | 1.22 | 1.24 |
| `SkipReadOnlyValidationGCE` | `false` | Alpha | 1.28 | 1.28 |
| `SkipReadOnlyValidationGCE` | `true` | Deprecated | 1.29 | 1.30 |
| `StableLoadBalancerNodeSet` | `true` | Beta | 1.27 | 1.29 |
| `StableLoadBalancerNodeSet` | `true` | GA | 1.30 | 1.31 |
| `StartupProbe` | `false` | Alpha | 1.16 | 1.17 |
| `StartupProbe` | `true` | Beta | 1.18 | 1.19 |
| `StartupProbe` | `true` | GA | 1.20 | 1.23 |
| `StatefulSetMinReadySeconds` | `false` | Alpha | 1.22 | 1.22 |
| `StatefulSetMinReadySeconds` | `true` | Beta | 1.23 | 1.24 |
| `StatefulSetMinReadySeconds` | `true` | GA | 1.25 | 1.26 |
| `StorageObjectInUseProtection` | `true` | Beta | 1.10 | 1.10 |
| `StorageObjectInUseProtection` | `true` | GA | 1.11 | 1.24 |
| `StreamingProxyRedirects` | `false` | Beta | 1.5 | 1.5 |
| `StreamingProxyRedirects` | `true` | Beta | 1.6 | 1.17 |
| `StreamingProxyRedirects` | `true` | Deprecated | 1.18 | 1.21 |
| `StreamingProxyRedirects` | `false` | Deprecated | 1.22 | 1.24 |
| `SupportIPVSProxyMode` | `false` | Alpha | 1.8 | 1.8 |
| `SupportIPVSProxyMode` | `false` | Beta | 1.9 | 1.9 |
| `SupportIPVSProxyMode` | `true` | Beta | 1.10 | 1.10 |
| `SupportIPVSProxyMode` | `true` | GA | 1.11 | 1.20 |
| `SupportNodePidsLimit` | `false` | Alpha | 1.14 | 1.14 |
| `SupportNodePidsLimit` | `true` | Beta | 1.15 | 1.19 |
| `SupportNodePidsLimit` | `true` | GA | 1.20 | 1.23 |
| `SupportPodPidsLimit` | `false` | Alpha | 1.10 | 1.13 |
| `SupportPodPidsLimit` | `true` | Beta | 1.14 | 1.19 |
| `SupportPodPidsLimit` | `true` | GA | 1.20 | 1.23 |
| `SuspendJob` | `false` | Alpha | 1.21 | 1.21 |
| `SuspendJob` | `true` | Beta | 1.22 | 1.23 |
| `SuspendJob` | `true` | GA | 1.24 | 1.25 |
| `Sysctls` | `true` | Beta | 1.11 | 1.20 |
| `Sysctls` | `true` | GA | 1.21 | 1.22 |
| `TaintBasedEvictions` | `false` | Alpha | 1.6 | 1.12 |
| `TaintBasedEvictions` | `true` | Beta | 1.13 | 1.17 |
| `TaintBasedEvictions` | `true` | GA | 1.18 | 1.20 |
| `TaintNodesByCondition` | `false` | Alpha | 1.8 | 1.11 |
| `TaintNodesByCondition` | `true` | Beta | 1.12 | 1.16 |
| `TaintNodesByCondition` | `true` | GA | 1.17 | 1.18 |
| `TokenRequest` | `false` | Alpha | 1.10 | 1.11 |
| `TokenRequest` | `true` | Beta | 1.12 | 1.19 |
| `TokenRequest` | `true` | GA | 1.20 | 1.21 |
| `TokenRequestProjection` | `false` | Alpha | 1.11 | 1.11 |
| `TokenRequestProjection` | `true` | Beta | 1.12 | 1.19 |
| `TokenRequestProjection` | `true` | GA | 1.20 | 1.21 |
| `TopologyManager` | `false` | Alpha | 1.16 | 1.17 |
| `TopologyManager` | `true` | Beta | 1.18 | 1.26 |
| `TopologyManager` | `true` | GA | 1.27 | 1.28 |
| `TTLAfterFinished` | `false` | Alpha | 1.12 | 1.20 |
| `TTLAfterFinished` | `true` | Beta | 1.21 | 1.22 |
| `TTLAfterFinished` | `true` | GA | 1.23 | 1.24 |
| `UserNamespacesStatelessPodsSupport` | `false` | Alpha | 1.25 | 1.27 |
| `ValidateProxyRedirects` | `false` | Alpha | 1.12 | 1.13 |
| `ValidateProxyRedirects` | `true` | Beta | 1.14 | 1.21 |
| `ValidateProxyRedirects` | `true` | Deprecated | 1.22 | 1.24 |
| `ValidatingAdmissionPolicy` | `false` | Alpha | 1.26 | 1.27 |
| `ValidatingAdmissionPolicy` | `false` | Beta | 1.28 | 1.29 |
| `ValidatingAdmissionPolicy` | `true` | GA | 1.30 | 1.31 |
| `VolumeCapacityPriority` | `false` | Alpha | 1.21 | 1.32 |
| `VolumePVCDataSource` | `false` | Alpha | 1.15 | 1.15 |
| `VolumePVCDataSource` | `true` | Beta | 1.16 | 1.17 |
| `VolumePVCDataSource` | `true` | GA | 1.18 | 1.21 |
| `VolumeScheduling` | `false` | Alpha | 1.9 | 1.9 |
| `VolumeScheduling` | `true` | Beta | 1.10 | 1.12 |
| `VolumeScheduling` | `true` | GA | 1.13 | 1.16 |
| `VolumeSnapshotDataSource` | `false` | Alpha | 1.12 | 1.16 |
| `VolumeSnapshotDataSource` | `true` | Beta | 1.17 | 1.19 |
| `VolumeSnapshotDataSource` | `true` | GA | 1.20 | 1.22 |
| `VolumeSubpath` | `true` | GA | 1.10 | 1.24 |
| `VolumeSubpathEnvExpansion` | `false` | Alpha | 1.14 | 1.14 |
| `VolumeSubpathEnvExpansion` | `true` | Beta | 1.15 | 1.16 |
| `VolumeSubpathEnvExpansion` | `true` | GA | 1.17 | 1.24 |
| `WarningHeaders` | `true` | Beta | 1.19 | 1.21 |
| `WarningHeaders` | `true` | GA | 1.22 | 1.24 |
| `WatchBookmark` | `false` | Alpha | 1.15 | 1.15 |
| `WatchBookmark` | `true` | Beta | 1.16 | 1.16 |
| `WatchBookmark` | `true` | GA | 1.17 | 1.32 |
| `WindowsEndpointSliceProxying` | `false` | Alpha | 1.19 | 1.20 |
| `WindowsEndpointSliceProxying` | `true` | Beta | 1.21 | 1.21 |
| `WindowsEndpointSliceProxying` | `true` | GA | 1.22 | 1.24 |
| `WindowsGMSA` | `false` | Alpha | 1.14 | 1.15 |
| `WindowsGMSA` | `true` | Beta | 1.16 | 1.17 |
| `WindowsGMSA` | `true` | GA | 1.18 | 1.18 |
| `WindowsHostProcessContainers` | `false` | Alpha | 1.22 | 1.22 |
| `WindowsHostProcessContainers` | `true` | Beta | 1.23 | 1.25 |
| `WindowsHostProcessContainers` | `true` | GA | 1.26 | 1.27 |
| `WindowsRunAsUserName` | `false` | Alpha | 1.16 | 1.16 |
| `WindowsRunAsUserName` | `true` | Beta | 1.17 | 1.17 |
| `WindowsRunAsUserName` | `true` | GA | 1.18 | 1.20 |
| `ZeroLimitedNominalConcurrencyShares` | `false` | Beta | 1.29 | 1.29 |
| `ZeroLimitedNominalConcurrencyShares` | `true` | GA | 1.30 | 1.31 |

## Descriptions for removed feature gates

`Accelerators`
:   Provided an early form of plugin to enable Nvidia GPU support when using
    Docker Engine; no longer available. See
    [Device Plugins](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) for
    an alternative.

`AdmissionWebhookMatchConditions`
:   Enable [match conditions](/docs/reference/access-authn-authz/extensible-admission-controllers/#matching-requests-matchconditions)
    on mutating & validating admission webhooks.

`AdvancedAuditing`
:   Enable [advanced auditing](/docs/tasks/debug/debug-cluster/audit/#advanced-audit)

`AffinityInAnnotations`
:   Enable setting
    [Pod affinity or anti-affinity](/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity).

`AggregatedDiscoveryEndpoint`
:   Enable a single HTTP endpoint `/discovery/<version>` which
    supports native HTTP caching with ETags containing all APIResources known to the API server.

`AllowExtTrafficLocalEndpoints`
:   Enable a service to route external requests to node local endpoints.

`AllowInsecureBackendProxy`
:   Enable the users to skip TLS verification of
    kubelets on Pod log requests.

`APIListChunking`
:   Enable the API clients to retrieve (`LIST` or `GET`)
    resources from API server in chunks.

`APIPriorityAndFairness`
:   Enable managing request concurrency with
    prioritization and fairness at each server. (Renamed from `RequestManagement`)

`APISelfSubjectReview`
:   Activate the `SelfSubjectReview` API which allows users
    to see the requesting subject's authentication information.
    See [API access to authentication information for a client](/docs/reference/access-authn-authz/authentication/#self-subject-review)
    for more details.

`AppArmor`
:   Enable use of AppArmor mandatory access control for Pods running on Linux nodes.
    See [AppArmor Tutorial](/docs/tutorials/security/apparmor/) for more details.

`AppArmorFields`
:   Enable AppArmor related security context settings.

    For more information about AppArmor and Kubernetes, read the
    [AppArmor](/docs/concepts/security/linux-kernel-security-constraints/#apparmor) section
    within
    [security features in the Linux kernel](/docs/concepts/security/linux-kernel-security-constraints/#linux-security-features).

`AttachVolumeLimit`
:   Enable volume plugins to report limits on number of volumes
    that can be attached to a node.
    See [dynamic volume limits](/docs/concepts/storage/storage-limits/#dynamic-volume-limits)
    for more details.

`BalanceAttachedNodeVolumes`
:   Include volume count on node to be considered for
    balanced resource allocation while scheduling. A node which has closer CPU,
    memory utilization, and volume count is favored by the scheduler while making decisions.

`BlockVolume`
:   Enable the definition and consumption of raw block devices in Pods.
    See [Raw Block Volume Support](/docs/concepts/storage/persistent-volumes/#raw-block-volume-support)
    for more details.

`BoundServiceAccountTokenVolume`
:   Migrate ServiceAccount volumes to use a projected volume
    consisting of a ServiceAccountTokenVolumeProjection. Cluster admins can use metric
    `serviceaccount_stale_tokens_total` to monitor workloads that are depending on the extended
    tokens. If there are no such workloads, turn off extended tokens by starting `kube-apiserver` with
    flag `--service-account-extend-token-expiration=false`.

    Check [Bound Service Account Tokens](https://github.com/kubernetes/enhancements/blob/master/keps/sig-auth/1205-bound-service-account-tokens/README.md)
    for more details.

`CloudDualStackNodeIPs`
:   Enables dual-stack `kubelet --node-ip` with external cloud providers.
    See [Configure IPv4/IPv6 dual-stack](/docs/concepts/services-networking/dual-stack/#configure-ipv4-ipv6-dual-stack)
    for more details.

`ConfigurableFSGroupPolicy`
:   Allows user to configure volume permission change policy
    for fsGroups when mounting a volume in a Pod. See
    [Configure volume permission and ownership change policy for Pods](/docs/tasks/configure-pod-container/security-context/#configure-volume-permission-and-ownership-change-policy-for-pods)
    for more details.

`ConsistentHTTPGetHandlers`
:   Normalize HTTP get URL and Header passing for lifecycle
    handlers with probers.

`ControllerManagerLeaderMigration`
:   Enables Leader Migration for
    [kube-controller-manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/#initial-leader-migration-configuration) and
    [cloud-controller-manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/#deploy-cloud-controller-manager)
    which allows a cluster operator to live migrate
    controllers from the kube-controller-manager into an external controller-manager
    (e.g. the cloud-controller-manager) in an HA cluster without downtime.

`CPUManager`
:   Enable container level CPU affinity support, see
    [CPU Management Policies](/docs/tasks/administer-cluster/cpu-management-policies/).

`CRIContainerLogRotation`
:   Enable container log rotation for CRI container runtime.
    The default max size of a log file is 10MB and the default max number of
    log files allowed for a container is 5.
    These values can be configured in the kubelet config.
    See [logging at node level](/docs/concepts/cluster-administration/logging/#logging-at-the-node-level)
    for more details.

`CronJobControllerV2`
:   Use an alternative implementation of the
    [CronJob](/docs/concepts/workloads/controllers/cron-jobs/ "A repeating task (a Job) that runs on a regular schedule.") controller. Otherwise,
    version 1 of the same controller is selected.

`CronJobTimeZone`
:   Allow the use of the `timeZone` optional field in [CronJobs](/docs/concepts/workloads/controllers/cron-jobs/)

`CSIBlockVolume`
:   Enable external CSI volume drivers to support block storage.
    See [`csi` raw block volume support](/docs/concepts/storage/volumes/#csi-raw-block-volume-support)
    for more details.

`CSIDriverRegistry`
:   Enable all logic related to the CSIDriver API object in
    `csi.storage.k8s.io`.

`CSIInlineVolume`
:   Enable CSI Inline volumes support for pods.

`CSIMigration`
:   Enables shims and translation logic to route volume
    operations from in-tree plugins to corresponding pre-installed CSI plugins

`CSIMigrationAWS`
:   Enables shims and translation logic to route volume
    operations from the AWS-EBS in-tree plugin to EBS CSI plugin. Supports
    falling back to in-tree EBS plugin for mount operations to nodes that have
    the feature disabled or that do not have EBS CSI plugin installed and
    configured. Does not support falling back for provision operations, for those
    the CSI plugin must be installed and configured.

`CSIMigrationAWSComplete`
:   Stops registering the EBS in-tree plugin in
    kubelet and volume controllers and enables shims and translation logic to
    route volume operations from the AWS-EBS in-tree plugin to EBS CSI plugin.
    Requires CSIMigration and CSIMigrationAWS feature flags enabled and EBS CSI
    plugin installed and configured on all nodes in the cluster. This flag has
    been deprecated in favor of the `InTreePluginAWSUnregister` feature flag
    which prevents the registration of in-tree EBS plugin.

`CSIMigrationAzureDisk`
:   Enables shims and translation logic to route volume
    operations from the Azure-Disk in-tree plugin to AzureDisk CSI plugin.
    Supports falling back to in-tree AzureDisk plugin for mount operations to
    nodes that have the feature disabled or that do not have AzureDisk CSI plugin
    installed and configured. Does not support falling back for provision
    operations, for those the CSI plugin must be installed and configured.
    Requires CSIMigration feature flag enabled.

`CSIMigrationAzureDiskComplete`
:   Stops registering the Azure-Disk in-tree
    plugin in kubelet and volume controllers and enables shims and translation
    logic to route volume operations from the Azure-Disk in-tree plugin to
    AzureDisk CSI plugin. Requires CSIMigration and CSIMigrationAzureDisk feature
    flags enabled and AzureDisk CSI plugin installed and configured on all nodes
    in the cluster. This flag has been deprecated in favor of the
    `InTreePluginAzureDiskUnregister` feature flag which prevents the registration
    of in-tree AzureDisk plugin.

`CSIMigrationAzureFile`
:   Enables shims and translation logic to route volume
    operations from the Azure-File in-tree plugin to AzureFile CSI plugin.
    Supports falling back to in-tree AzureFile plugin for mount operations to
    nodes that have the feature disabled or that do not have AzureFile CSI plugin
    installed and configured. Does not support falling back for provision
    operations, for those the CSI plugin must be installed and configured.
    Requires CSIMigration feature flag enabled.

`CSIMigrationAzureFileComplete`
:   Stops registering the Azure-File in-tree
    plugin in kubelet and volume controllers and enables shims and translation
    logic to route volume operations from the Azure-File in-tree plugin to
    AzureFile CSI plugin. Requires CSIMigration and CSIMigrationAzureFile feature
    flags enabled and AzureFile CSI plugin installed and configured on all nodes
    in the cluster. This flag has been deprecated in favor of the
    `InTreePluginAzureFileUnregister` feature flag which prevents the registration
    of in-tree AzureFile plugin.

`CSIMigrationGCE`
:   Enables shims and translation logic to route volume
    operations from the GCE-PD in-tree plugin to PD CSI plugin. Supports falling
    back to in-tree GCE plugin for mount operations to nodes that have the
    feature disabled or that do not have PD CSI plugin installed and configured.
    Does not support falling back for provision operations, for those the CSI
    plugin must be installed and configured. Requires CSIMigration feature flag
    enabled.

`CSIMigrationGCEComplete`
:   Stops registering the GCE-PD in-tree plugin in
    kubelet and volume controllers and enables shims and translation logic to
    route volume operations from the GCE-PD in-tree plugin to PD CSI plugin.
    Requires CSIMigration and CSIMigrationGCE feature flags enabled and PD CSI
    plugin installed and configured on all nodes in the cluster. This flag has
    been deprecated in favor of the `InTreePluginGCEUnregister` feature flag which
    prevents the registration of in-tree GCE PD plugin.

`CSIMigrationOpenStack`
:   Enables shims and translation logic to route volume
    operations from the Cinder in-tree plugin to Cinder CSI plugin. Supports
    falling back to in-tree Cinder plugin for mount operations to nodes that have
    the feature disabled or that do not have Cinder CSI plugin installed and
    configured. Does not support falling back for provision operations, for those
    the CSI plugin must be installed and configured. Requires CSIMigration
    feature flag enabled.

`CSIMigrationOpenStackComplete`
:   Stops registering the Cinder in-tree plugin in
    kubelet and volume controllers and enables shims and translation logic to route
    volume operations from the Cinder in-tree plugin to Cinder CSI plugin.
    Requires CSIMigration and CSIMigrationOpenStack feature flags enabled and Cinder
    CSI plugin installed and configured on all nodes in the cluster. This flag has
    been deprecated in favor of the `InTreePluginOpenStackUnregister` feature flag
    which prevents the registration of in-tree openstack cinder plugin.

`CSIMigrationRBD`
:   Enables shims and translation logic to route volume
    operations from the RBD in-tree plugin to Ceph RBD CSI plugin. Requires
    CSIMigration and csiMigrationRBD feature flags enabled and Ceph CSI plugin
    installed and configured in the cluster.

    This feature gate was deprecated in favor of the `InTreePluginRBDUnregister` feature gate,
    which prevents the registration of in-tree RBD plugin.

`CSIMigrationvSphere`
:   Enables shims and translation logic to route volume operations
    from the vSphere in-tree plugin to vSphere CSI plugin. Supports falling back
    to in-tree vSphere plugin for mount operations to nodes that have the feature
    disabled or that do not have vSphere CSI plugin installed and configured.
    Does not support falling back for provision operations, for those the CSI
    plugin must be installed and configured. Requires CSIMigration feature flag
    enabled.

`CSIMigrationvSphereComplete`
:   Stops registering the vSphere in-tree plugin in kubelet
    and volume controllers and enables shims and translation logic to route volume operations
    from the vSphere in-tree plugin to vSphere CSI plugin. Requires CSIMigration and
    CSIMigrationvSphere feature flags enabled and vSphere CSI plugin installed and
    configured on all nodes in the cluster. This flag has been deprecated in favor
    of the `InTreePluginvSphereUnregister` feature flag which prevents the
    registration of in-tree vsphere plugin.

`CSINodeExpandSecret`
:   Enable passing secret authentication data to a CSI driver for use
    during a `NodeExpandVolume` CSI operation.

`CSINodeInfo`
:   Enable all logic related to the CSINodeInfo API object in `csi.storage.k8s.io`.

`CSIPersistentVolume`
:   Enable discovering and mounting volumes provisioned through a
    [CSI (Container Storage Interface)](https://git.k8s.io/design-proposals-archive/storage/container-storage-interface.md)
    compatible volume plugin.

`CSIServiceAccountToken`
:   Enable CSI drivers to receive the pods' service account token
    that they mount volumes for. See
    [Token Requests](https://kubernetes-csi.github.io/docs/token-requests.html).

`CSIStorageCapacity`
:   Enables CSI drivers to publish storage capacity information
    and the Kubernetes scheduler to use that information when scheduling pods. See
    [Storage Capacity](/docs/concepts/storage/storage-capacity/).
    Check the [`csi` volume type](/docs/concepts/storage/volumes/#csi) documentation for more details.

`CSIVolumeFSGroupPolicy`
:   Allows CSIDrivers to use the `fsGroupPolicy` field.
    This field controls whether volumes created by a CSIDriver support volume ownership
    and permission modifications when these volumes are mounted.

`CSRDuration`
:   Allows clients to request a duration for certificates issued
    via the Kubernetes CSR API.

`CustomPodDNS`
:   Enable customizing the DNS settings for a Pod using its `dnsConfig` property.
    Check [Pod's DNS Config](/docs/concepts/services-networking/dns-pod-service/#pod-dns-config)
    for more details.

`CustomResourceDefaulting`
:   Enable CRD support for default values in OpenAPI v3 validation schemas.

`CustomResourcePublishOpenAPI`
:   Enables publishing of CRD OpenAPI specs.

`CustomResourceSubresources`
:   Enable `/status` and `/scale` subresources
    on resources created from [CustomResourceDefinition](/docs/concepts/extend-kubernetes/api-extension/custom-resources/).

`CustomResourceValidation`
:   Enable schema based validation on resources created from
    [CustomResourceDefinition](/docs/concepts/extend-kubernetes/api-extension/custom-resources/).

`CustomResourceValidationExpressions`
:   Enable expression language validation in CRD
    which will validate customer resource based on validation rules written in
    the `x-kubernetes-validations` extension.

`CustomResourceWebhookConversion`
:   Enable webhook-based conversion
    on resources created from [CustomResourceDefinition](/docs/concepts/extend-kubernetes/api-extension/custom-resources/).

`DaemonSetUpdateSurge`
:   Enables the DaemonSet workloads to maintain
    availability during update per node.
    See [Perform a Rolling Update on a DaemonSet](/docs/tasks/manage-daemon/update-daemon-set/).

`DefaultHostNetworkHostPortsInPodTemplates`
:   This feature gate controls the point at which a default value for
    `.spec.containers[*].ports[*].hostPort`
    is assigned, for Pods using `hostNetwork: true`. The default since Kubernetes v1.28 is to only set a default
    value in Pods.

    Enabling this means a default will be assigned even to the `.spec` of an embedded
    [PodTemplate](/docs/concepts/workloads/pods/#pod-templates) (for example, in a Deployment),
    which is the way that older releases of Kubernetes worked.
    You should migrate your code so that it does not rely on the legacy behavior.

`DefaultPodTopologySpread`
:   Enables the use of `PodTopologySpread` scheduling plugin to do
    [default spreading](/docs/concepts/scheduling-eviction/topology-spread-constraints/#internal-default-constraints).

`DelegateFSGroupToCSIDriver`
:   If supported by the CSI driver, delegates the
    role of applying `fsGroup` from a Pod's `securityContext` to the driver by
    passing `fsGroup` through the NodeStageVolume and NodePublishVolume CSI calls.

`DevicePluginCDIDevices`
:   Enable support to CDI device IDs in the
    [Device Plugin](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) API.

`DevicePlugins`
:   Enable the [device-plugins](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
    based resource provisioning on nodes.

`DisableAcceleratorUsageMetrics`
:   [Disable accelerator metrics collected by the kubelet](/docs/concepts/cluster-administration/system-metrics/#disable-accelerator-metrics).

`DisableCloudProviders`
:   Enabling this feature gate deactivated functionality in `kube-apiserver`,
    `kube-controller-manager` and `kubelet` that related to the `--cloud-provider`
    command line argument.

    In Kubernetes v1.31 and later, the only valid values for `--cloud-provider`
    are the empty string (no cloud provider integration), or "external"
    (integration via a separate cloud-controller-manager).

`DisableKubeletCloudCredentialProviders`
:   Enabling the feature gate deactivated the legacy in-tree functionality within the
    kubelet, that allowed the kubelet to to authenticate to a cloud provider container registry
    for container image pulls.

`DownwardAPIHugePages`
:   Enables usage of hugepages in
    [downward API](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/).

`DRAControlPlaneController`
:   Enables support for resources with custom parameters and a lifecycle
    that is independent of a Pod. Allocation of resources is handled
    by a resource driver's control plane controller.

`DryRun`
:   Enable server-side [dry run](/docs/reference/using-api/api-concepts/#dry-run) requests
    so that validation, merging, and mutation can be tested without committing.

`DynamicAuditing`
:   Used to enable dynamic auditing before v1.19.

`DynamicKubeletConfig`
:   Enable the dynamic configuration of kubelet. The
    feature is no longer supported outside of supported skew policy. The feature
    gate was removed from kubelet in 1.24.

`DynamicProvisioningScheduling`
:   Extend the default scheduler to be aware of
    volume topology and handle PV provisioning.
    This feature was superseded by the `VolumeScheduling` feature in v1.12.

`DynamicVolumeProvisioning`
:   Enable the
    [dynamic provisioning](/docs/concepts/storage/dynamic-provisioning/) of persistent volumes to Pods.

`EfficientWatchResumption`
:   Allows for storage-originated bookmark (progress
    notify) events to be delivered to the users. This is only applied to watch operations.

`EnableAggregatedDiscoveryTimeout`
:   Enable the five second
    timeout on aggregated discovery calls.

`EnableEquivalenceClassCache`
:   Enable the scheduler to cache equivalence of
    nodes when scheduling Pods.

`EndpointSlice`
:   Enables EndpointSlices for more scalable and extensible
    network endpoints. See [Enabling EndpointSlices](/docs/concepts/services-networking/endpoint-slices/).

`EndpointSliceNodeName`
:   Enables EndpointSlice `nodeName` field.

`EndpointSliceProxying`
:   When enabled, kube-proxy running
    on Linux will use EndpointSlices as the primary data source instead of
    Endpoints, enabling scalability and performance improvements. See
    [Enabling Endpoint Slices](/docs/concepts/services-networking/endpoint-slices/).

`EndpointSliceTerminatingCondition`
:   Enables EndpointSlice `terminating` and `serving`
    condition fields.

`EphemeralContainers`
:   Enable the ability to add
    [ephemeral containers](/docs/concepts/workloads/pods/ephemeral-containers/ "A type of container type that you can temporarily run inside a Pod")
    to running Pods.

`EvenPodsSpread`
:   Enable pods to be scheduled evenly across topology domains. See
    [Pod Topology Spread Constraints](/docs/concepts/scheduling-eviction/topology-spread-constraints/).

`ExpandCSIVolumes`
:   Enable the expanding of CSI volumes.

`ExpandedDNSConfig`
:   Enable kubelet and kube-apiserver to allow more DNS
    search paths and longer list of DNS search paths. This feature requires container
    runtime support(Containerd: v1.5.6 or higher, CRI-O: v1.22 or higher). See
    [Expanded DNS Configuration](/docs/concepts/services-networking/dns-pod-service/#expanded-dns-configuration).

`ExpandInUsePersistentVolumes`
:   Enable expanding in-use PVCs. See
    [Resizing an in-use PersistentVolumeClaim](/docs/concepts/storage/persistent-volumes/#resizing-an-in-use-persistentvolumeclaim).

`ExpandPersistentVolumes`
:   Enable the expanding of persistent volumes. See
    [Expanding Persistent Volumes Claims](/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims).

`ExperimentalCriticalPodAnnotation`
:   Enable annotating specific pods as *critical*
    so that their [scheduling is guaranteed](/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/).
    This feature is deprecated by Pod Priority and Preemption as of v1.13.

`ExperimentalHostUserNamespaceDefaulting`
:   Enabling the defaulting user
    namespace to host. This is for containers that are using other host namespaces,
    host mounts, or containers that are privileged or using specific non-namespaced
    capabilities (e.g. `MKNODE`, `SYS_MODULE` etc.). This should only be enabled
    if user namespace remapping is enabled in the Docker daemon.

`ExternalPolicyForExternalIP`
:   Fix a bug where ExternalTrafficPolicy is not
    applied to Service ExternalIPs.

`GCERegionalPersistentDisk`
:   Enable the regional PD feature on GCE.

`GenericEphemeralVolume`
:   Enables ephemeral, inline volumes that support all features
    of normal volumes (can be provided by third-party storage vendors, storage capacity tracking,
    restore from snapshot, etc.).
    See [Ephemeral Volumes](/docs/concepts/storage/ephemeral-volumes/).

`GRPCContainerProbe`
:   Enables the gRPC probe method for {Liveness,Readiness,Startup}Probe.
    See [Configure Liveness, Readiness and Startup Probes](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-grpc-liveness-probe).

`HPAContainerMetrics`
:   Allow [HorizontalPodAutoscalers](/docs/tasks/run-application/horizontal-pod-autoscale/ "Object that automatically scales the number of pod replicas based on targeted resource utilization or custom metric targets.")
    to scale based on metrics from individual containers within target pods.

`HugePages`
:   Enable the allocation and consumption of pre-allocated
    [huge pages](/docs/tasks/manage-hugepages/scheduling-hugepages/).

`HugePageStorageMediumSize`
:   Enable support for multiple sizes pre-allocated
    [huge pages](/docs/tasks/manage-hugepages/scheduling-hugepages/).

`HyperVContainer`
:   Enable
    [Hyper-V isolation](https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/hyperv-container)
    for Windows containers.

`IdentifyPodOS`
:   Allows the Pod OS field to be specified. This helps in identifying
    the OS of the pod authoritatively during the API server admission time.

`ImmutableEphemeralVolumes`
:   Allows for marking individual Secrets and ConfigMaps as
    immutable for better safety and performance.

`IndexedJob`
:   Allows the [Job](/docs/concepts/workloads/controllers/job/)
    controller to manage Pod completions per completion index.

`IngressClassNamespacedParams`
:   Allow namespace-scoped parameters reference in
    `IngressClass` resource. This feature adds two fields - `Scope` and `Namespace`
    to `IngressClass.spec.parameters`.

`Initializers`
:   Allow asynchronous coordination of object creation using the
    Initializers admission plugin.

`InTreePluginAWSUnregister`
:   Stops registering the aws-ebs in-tree plugin in kubelet
    and volume controllers.

`InTreePluginAzureDiskUnregister`
:   Stops registering the azuredisk in-tree plugin in kubelet
    and volume controllers.

`InTreePluginAzureFileUnregister`
:   Stops registering the azurefile in-tree plugin in kubelet
    and volume controllers.

`InTreePluginGCEUnregister`
:   Stops registering the gce-pd in-tree plugin in kubelet
    and volume controllers.

`InTreePluginOpenStackUnregister`
:   Stops registering the OpenStack cinder in-tree plugin in kubelet
    and volume controllers.

`InTreePluginRBDUnregister`
:   Stops registering the RBD in-tree plugin within kubelet and volume controllers.

`InTreePluginvSphereUnregister`
:   Stops registering the vSphere in-tree plugin in kubelet
    and volume controllers.

`IPTablesOwnershipCleanup`
:   This causes kubelet to no longer create legacy iptables rules.

`IPv6DualStack`
:   Enable [dual stack](/docs/concepts/services-networking/dual-stack/)
    support for IPv6.

`JobMutableNodeSchedulingDirectives`
:   Allows updating node scheduling directives in
    the pod template of [Job](/docs/concepts/workloads/controllers/job/).

`JobPodFailurePolicy`
:   Allow users to specify handling of pod failures based on container
    exit codes and pod conditions.

`JobReadyPods`
:   Enables tracking the number of Pods that have a `Ready`
    [condition](/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions).
    The count of `Ready` pods is recorded in the
    [status](/docs/reference/kubernetes-api/workload-resources/job-v1/#JobStatus)
    of a [Job](/docs/concepts/workloads/controllers/job/) status.

`JobTrackingWithFinalizers`
:   Enables tracking [Job](/docs/concepts/workloads/controllers/job/)
    completions without relying on Pods remaining in the cluster indefinitely.
    The Job controller uses Pod finalizers and a field in the Job status to keep
    track of the finished Pods to count towards completion.

`KMSv2`
:   Enables KMS v2 API for encryption at rest. See
    [Using a KMS Provider for data encryption](/docs/tasks/administer-cluster/kms-provider/)
    for more details.

`KMSv2KDF`
:   Enables KMS v2 to generate single use data encryption keys.
    See [Using a KMS Provider for data encryption](/docs/tasks/administer-cluster/kms-provider/) for more details.
    If the `KMSv2` feature gate is not enabled in your cluster, the value of the `KMSv2KDF` feature gate has no effect.

`KubeletConfigFile`
:   Enable loading kubelet configuration from
    a file specified using a config file.
    See [setting kubelet parameters via a config file](/docs/tasks/administer-cluster/kubelet-config-file/)
    for more details.

`KubeletCredentialProviders`
:   Enable kubelet exec credential providers for
    image pull credentials.

`KubeletPluginsWatcher`
:   Enable probe-based plugin watcher utility to enable kubelet
    to discover plugins such as [CSI volume drivers](/docs/concepts/storage/volumes/#csi).

`KubeletPodResources`
:   Enable the kubelet's pod resources gRPC endpoint. See
    [Support Device Monitoring](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/606-compute-device-assignment/README.md)
    for more details.

`KubeletPodResourcesGetAllocatable`
:   Enable the kubelet's pod resources
    `GetAllocatableResources` functionality. This API augments the
    [resource allocation reporting](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#monitoring-device-plugin-resources)

`KubeProxyDrainingTerminatingNodes`
:   Implement connection draining for
    terminating nodes for `externalTrafficPolicy: Cluster` services.

`LegacyNodeRoleBehavior`
:   When disabled, legacy behavior in service load balancers and
    node disruption will ignore the `node-role.kubernetes.io/master` label in favor of the
    feature-specific labels provided by `NodeDisruptionExclusion` and `ServiceNodeExclusion`.

`LegacyServiceAccountTokenCleanUp`
:   Enable cleaning up Secret-based
    [service account tokens](/docs/concepts/security/service-accounts/#get-a-token)
    when they are not used in a specified time (default to be one year).

`LegacyServiceAccountTokenNoAutoGeneration`
:   Stop auto-generation of Secret-based
    [service account tokens](/docs/concepts/security/service-accounts/#get-a-token).

`LegacyServiceAccountTokenTracking`
:   Track usage of Secret-based
    [service account tokens](/docs/concepts/security/service-accounts/#get-a-token).

`LocalStorageCapacityIsolation`
:   Enable the consumption of
    [local ephemeral storage](/docs/concepts/configuration/manage-resources-containers/)
    and also the `sizeLimit` property of an
    [emptyDir volume](/docs/concepts/storage/volumes/#emptydir).

`MinDomainsInPodTopologySpread`
:   Enable `minDomains` in
    [Pod topology spread constraints](/docs/concepts/scheduling-eviction/topology-spread-constraints/).

`MinimizeIPTablesRestore`
:   Enables new performance improvement logics
    in the kube-proxy iptables mode.

`MixedProtocolLBService`
:   Enable using different protocols in the same `LoadBalancer` type
    Service instance.

`MountContainers`
:   Enable using utility containers on host as the volume mounter.

`MountPropagation`
:   Enable sharing volume mounted by one container to other containers or pods.
    For more details, please see [mount propagation](/docs/concepts/storage/volumes/#mount-propagation).

`MultiCIDRRangeAllocator`
:   Enables the MultiCIDR range allocator.

`NamespaceDefaultLabelName`
:   Configure the API Server to set an immutable
    [label](/docs/concepts/overview/working-with-objects/labels "Tags objects with identifying attributes that are meaningful and relevant to users.") `kubernetes.io/metadata.name`
    on all namespaces, containing the namespace name.

`NetworkPolicyEndPort`
:   Allows you to define ports in a
    [NetworkPolicy](/docs/concepts/services-networking/network-policies/)
    rule as a range of port numbers.

`NetworkPolicyStatus`
:   Enable the `status` subresource for NetworkPolicy objects.

`NewVolumeManagerReconstruction`
:   Enables improved discovery of mounted volumes during kubelet
    startup. Since the associated code had been significantly refactored, Kubernetes versions 1.25 to 1.29
    allowed you to opt-out in case the kubelet got stuck at the startup, or did not unmount volumes
    from terminated Pods.

    This refactoring was behind the `SELinuxMountReadWriteOncePod` feature gate in Kubernetes
    releases 1.25 and 1.26.

`NodeDisruptionExclusion`
:   Enable use of the Node label `node.kubernetes.io/exclude-disruption`
    which prevents nodes from being evacuated during zone failures.

`NodeLease`
:   Enable the new Lease API to report node heartbeats, which could be used as a node health signal.

`NodeOutOfServiceVolumeDetach`
:   When a Node is marked out-of-service using the
    `node.kubernetes.io/out-of-service` taint, Pods on the node will be forcefully deleted
    if they can not tolerate this taint, and the volume detach operations for Pods terminating
    on the node will happen immediately. The deleted Pods can recover quickly on different nodes.

`NonPreemptingPriority`
:   Enable `preemptionPolicy` field for PriorityClass and Pod.

`OpenAPIV3`
:   Enables the API server to publish OpenAPI v3.

`PDBUnhealthyPodEvictionPolicy`
:   Enables the `unhealthyPodEvictionPolicy` field of a `PodDisruptionBudget`. This specifies
    when unhealthy pods should be considered for eviction. Please see [Unhealthy Pod Eviction Policy](/docs/tasks/run-application/configure-pdb/#unhealthy-pod-eviction-policy)
    for more details.

`PersistentLocalVolumes`
:   Enable the usage of `local` volume type in Pods.
    Pod affinity has to be specified if requesting a `local` volume.

`PersistentVolumeLastPhaseTransitionTime`
:   Adds a new field to PersistentVolume
    which holds a timestamp of when the volume last transitioned its phase.

`PodAffinityNamespaceSelector`
:   Enable the
    [Pod Affinity Namespace Selector](/docs/concepts/scheduling-eviction/assign-pod-node/#namespace-selector)
    and [CrossNamespacePodAffinity](/docs/concepts/policy/resource-quotas/#cross-namespace-pod-affinity-quota)
    quota scope features.

`PodDisruptionBudget`
:   Enable the [PodDisruptionBudget](/docs/tasks/run-application/configure-pdb/) feature.

`PodDisruptionConditions`
:   Enabled support for appending a dedicated pod condition indicating that the pod is being deleted due to a disruption.

`PodHasNetworkCondition`
:   Enable the kubelet to mark the [PodHasNetwork](/docs/concepts/workloads/pods/pod-lifecycle/#pod-has-network)
    condition on pods. This was renamed to `PodReadyToStartContainersCondition` in 1.28.

`PodHostIPs`
:   Enable the `status.hostIPs` field for pods and the [downward API](/docs/concepts/workloads/pods/downward-api/ "A mechanism to expose Pod and container field values to code running in a container.").
    The field lets you expose host IP addresses to workloads.

`PodOverhead`
:   Enable the [PodOverhead](/docs/concepts/scheduling-eviction/pod-overhead/)
    feature to account for pod overheads.

`PodPriority`
:   Enable the descheduling and preemption of Pods based on their
    [priorities](/docs/concepts/scheduling-eviction/pod-priority-preemption/).

`PodReadinessGates`
:   Enable the setting of `PodReadinessGate` field for extending
    Pod readiness evaluation. See [Pod readiness gate](/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate)
    for more details.

`PodSecurity`
:   Enables the `PodSecurity` admission plugin.

`PodShareProcessNamespace`
:   Enable the setting of `shareProcessNamespace` in a Pod for sharing
    a single process namespace between containers running in a pod. More details can be found in
    [Share Process Namespace between Containers in a Pod](/docs/tasks/configure-pod-container/share-process-namespace/).

`PreferNominatedNode`
:   This flag tells the scheduler whether the nominated
    nodes will be checked first before looping through all the other nodes in
    the cluster.

`ProbeTerminationGracePeriod`
:   Enable [setting probe-level
    `terminationGracePeriodSeconds`](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#probe-level-terminationgraceperiodseconds)
    on pods. See the [enhancement proposal](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/2238-liveness-probe-grace-period)
    for more details.

`ProxyTerminatingEndpoints`
:   Enable the kube-proxy to handle terminating
    endpoints when `ExternalTrafficPolicy=Local`.

`PVCProtection`
:   Enable the prevention of a PersistentVolumeClaim (PVC) from
    being deleted when it is still used by any Pod.

`ReadOnlyAPIDataVolumes`
:   Set [`configMap`](/docs/concepts/storage/volumes/#configmap),
    [`secret`](/docs/concepts/storage/volumes/#secret),
    [`downwardAPI`](/docs/concepts/storage/volumes/#downwardapi) and
    [`projected`](/docs/concepts/storage/volumes/#projected)
    [volumes](/docs/concepts/storage/volumes/ "A directory containing data, accessible to the containers in a pod.") to be mounted read-only.

    Since Kubernetes v1.10, these volume types are always read-only and you cannot opt out.

`ReadWriteOncePod`
:   Enables the usage of `ReadWriteOncePod` PersistentVolume
    access mode.

`RemainingItemCount`
:   Allow the API servers to show a count of remaining
    items in the response to a
    [chunking list request](/docs/reference/using-api/api-concepts/#retrieving-large-results-sets-in-chunks).

`RemoveSelfLink`
:   Sets the `.metadata.selfLink` field to blank (empty string) for all
    objects and collections. This field has been deprecated since the Kubernetes v1.16
    release. When this feature is enabled, the `.metadata.selfLink` field remains part of
    the Kubernetes API, but is always unset.

`RequestManagement`
:   Enables managing request concurrency with prioritization and fairness
    at each API server. Deprecated by `APIPriorityAndFairness` since 1.17.

`ResourceLimitsPriorityFunction`
:   Enable a scheduler priority function that
    assigns a lowest possible score of 1 to a node that satisfies at least one of
    the input Pod's cpu and memory limits. The intent is to break ties between
    nodes with same scores.

`ResourceQuotaScopeSelectors`
:   Enable resource quota scope selectors.

`RetroactiveDefaultStorageClass`
:   Allow assigning StorageClass to unbound PVCs retroactively.

`RootCAConfigMap`
:   Configure the `kube-controller-manager` to publish a
    [ConfigMap](/docs/concepts/configuration/configmap/ "An API object used to store non-confidential data in key-value pairs. Can be consumed as environment variables, command-line arguments, or configuration files in a volume.") named `kube-root-ca.crt`
    to every namespace. This ConfigMap contains a CA bundle used for verifying connections
    to the kube-apiserver. See
    [Bound Service Account Tokens](https://github.com/kubernetes/enhancements/blob/master/keps/sig-auth/1205-bound-service-account-tokens/README.md)
    for more details.

`RotateKubeletClientCertificate`
:   Enable the rotation of the client TLS certificate on the kubelet.
    See [kubelet configuration](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/#kubelet-configuration)
    for more details.

`RunAsGroup`
:   Enable control over the primary group ID set on the init processes of containers.

`RuntimeClass`
:   Enable the [RuntimeClass](/docs/concepts/containers/runtime-class/) feature for
    selecting container runtime configurations.

`ScheduleDaemonSetPods`
:   Enable DaemonSet Pods to be scheduled by the default scheduler instead
    of the DaemonSet controller.

`SCTPSupport`
:   Enables the *SCTP* `protocol` value in Pod, Service, Endpoints, EndpointSlice,
    and NetworkPolicy definitions.

`SeccompDefault`
:   Enables the use of `RuntimeDefault` as the default seccomp profile
    for all workloads.
    The seccomp profile is specified in the `securityContext` of a Pod and/or a Container.

`SecurityContextDeny`
:   This gate signals that the `SecurityContextDeny` admission controller is deprecated.

`SelectorIndex`
:   Allows label and field based indexes in API server watch cache to accelerate
    list operations.

`ServerSideApply`
:   Enables the [Sever Side Apply (SSA)](/docs/reference/using-api/server-side-apply/)
    feature on the API Server.

`ServerSideFieldValidation`
:   Enables server-side field validation. This means the validation
    of resource schema is performed at the API server side rather than the client side
    (for example, the `kubectl create` or `kubectl apply` command line).

`ServiceAccountIssuerDiscovery`
:   Enable OIDC discovery endpoints (issuer and JWKS URLs) for the
    service account issuer in the API server. See
    [Configure Service Accounts for Pods](/docs/tasks/configure-pod-container/configure-service-account/#service-account-issuer-discovery)
    for more details.

`ServiceAppProtocol`
:   Enables the `appProtocol` field on Services and Endpoints.

`ServiceInternalTrafficPolicy`
:   Enables the `internalTrafficPolicy` field on Services

`ServiceIPStaticSubrange`
:   Enables a strategy for Services ClusterIP allocations, whereby the
    ClusterIP range is subdivided. Dynamic allocated ClusterIP addresses will be allocated preferently
    from the upper range allowing users to assign static ClusterIPs from the lower range with a low
    risk of collision. See
    [Avoiding collisions](/docs/reference/networking/virtual-ips/#avoiding-collisions)
    for more details.

`ServiceLBNodePortControl`
:   Enables the `allocateLoadBalancerNodePorts` field on Services.

`ServiceLoadBalancerClass`
:   Enables the `loadBalancerClass` field on Services. See
    [Specifying class of load balancer implementation](/docs/concepts/services-networking/service/#load-balancer-class)
    for more details.

`ServiceLoadBalancerFinalizer`
:   Enable finalizer protection for Service load balancers.

`ServiceNodeExclusion`
:   Enable the exclusion of nodes from load balancers created by a cloud provider.
    A node is eligible for exclusion if labelled with "`node.kubernetes.io/exclude-from-external-load-balancers`".

`ServiceNodePortStaticSubrange`
:   Enables the use of different port allocation
    strategies for NodePort Services. For more details, see
    [reserve NodePort ranges to avoid collisions](/docs/concepts/services-networking/service/#avoid-nodeport-collisions).

`ServiceTopology`
:   Enable service to route traffic based upon the Node topology of the cluster.

`SetHostnameAsFQDN`
:   Enable the ability of setting Fully Qualified Domain Name(FQDN) as the
    hostname of a pod. See
    [Pod's `setHostnameAsFQDN` field](/docs/concepts/services-networking/dns-pod-service/#pod-sethostnameasfqdn-field).

`SkipReadOnlyValidationGCE`
:   Skip validation that GCE PersistentDisk volumes are in read-only mode.

`StableLoadBalancerNodeSet`
:   Enables less load balancer re-configurations by
    the service controller (KCCM) as an effect of changing node state.

`StartupProbe`
:   Enable the [startup](/docs/concepts/workloads/pods/pod-lifecycle/#when-should-you-use-a-startup-probe)
    probe in the kubelet.

`StatefulSetMinReadySeconds`
:   Allows `minReadySeconds` to be respected by
    the StatefulSet controller.

`StorageObjectInUseProtection`
:   Postpone the deletion of PersistentVolume or
    PersistentVolumeClaim objects if they are still being used.

`StreamingProxyRedirects`
:   Instructs the API server to intercept (and follow) redirects from the
    backend (kubelet) for streaming requests. Examples of streaming requests include the `exec`,
    `attach` and `port-forward` requests.

`SupportIPVSProxyMode`
:   Enable providing in-cluster service load balancing using IPVS.
    See [service proxies](/docs/reference/networking/virtual-ips/) for more details.

`SupportNodePidsLimit`
:   Enable the support to limiting PIDs on the Node. The parameter
    `pid=<number>` in the `--system-reserved` and `--kube-reserved` options can be specified to
    ensure that the specified number of process IDs will be reserved for the system as a whole and for
    Kubernetes system daemons respectively.

`SupportPodPidsLimit`
:   Enable the support to limiting PIDs in Pods.

`SuspendJob`
:   Enable support to suspend and resume Jobs. For more details, see
    [the Jobs docs](/docs/concepts/workloads/controllers/job/).

`Sysctls`
:   Enable support for namespaced kernel parameters (sysctls) that can be set for each pod.
    See [sysctls](/docs/tasks/administer-cluster/sysctl-cluster/) for more details.

`TaintBasedEvictions`
:   Enable evicting pods from nodes based on taints on Nodes and tolerations
    on Pods. See [taints and tolerations](/docs/concepts/scheduling-eviction/taint-and-toleration/)
    for more details.

`TaintNodesByCondition`
:   Enable automatic tainting nodes based on
    [node conditions](/docs/concepts/architecture/nodes/#condition).

`TokenRequest`
:   Enable the `TokenRequest` endpoint on service account resources.

`TokenRequestProjection`
:   Enable the injection of service account tokens into a Pod through a
    [`projected` volume](/docs/concepts/storage/volumes/#projected).

`TopologyManager`
:   Enable a mechanism to coordinate fine-grained hardware resource
    assignments for different components in Kubernetes. See
    [Control Topology Management Policies on a node](/docs/tasks/administer-cluster/topology-manager/).

`TTLAfterFinished`
:   Allow a [TTL controller](/docs/concepts/workloads/controllers/ttlafterfinished/)
    to clean up resources after they finish execution.

`UserNamespacesStatelessPodsSupport`
:   Enable user namespace support for stateless Pods. This feature gate was superseded
    by the `UserNamespacesSupport` feature gate in the Kubernetes v1.28 release.

`ValidateProxyRedirects`
:   This flag controls whether the API server should validate that redirects
    are only followed to the same host. Only used if the `StreamingProxyRedirects` flag is enabled.

`ValidatingAdmissionPolicy`
:   Enable [ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/) support for CEL validations be used in Admission Control.

`VolumeCapacityPriority`
:   Enable support for prioritizing nodes in different
    topologies based on available PV capacity.
    This feature is renamed to `StorageCapacityScoring` in v1.33.

`VolumePVCDataSource`
:   Enable support for specifying an existing PVC as a DataSource.

`VolumeScheduling`
:   Enable volume topology aware scheduling and make the PersistentVolumeClaim
    (PVC) binding aware of scheduling decisions. It also enables the usage of
    [`local`](/docs/concepts/storage/volumes/#local) volume type when used together with the
    `PersistentLocalVolumes` feature gate.

`VolumeSnapshotDataSource`
:   Enable volume snapshot data source support.

`VolumeSubpath`
:   Allow mounting a subpath of a volume in a container.

`VolumeSubpathEnvExpansion`
:   Enable `subPathExpr` field for expanding environment
    variables into a `subPath`.

`WarningHeaders`
:   Allow sending warning headers in API responses.

`WatchBookmark`
:   Enable support for watch bookmark events.

`WindowsEndpointSliceProxying`
:   When enabled, kube-proxy running on Windows will use
    EndpointSlices as the primary data source instead of Endpoints, enabling scalability and
    performance improvements. See
    [Enabling Endpoint Slices](/docs/concepts/services-networking/endpoint-slices/).

`WindowsGMSA`
:   Enables passing of GMSA credential specs from pods to container runtimes.

`WindowsHostProcessContainers`
:   Enables support for Windows HostProcess containers.

`WindowsRunAsUserName`
:   Enable support for running applications in Windows containers with as a
    non-default user. See [Configuring RunAsUserName](/docs/tasks/configure-pod-container/configure-runasusername/)
    for more details.

`ZeroLimitedNominalConcurrencyShares`
:   Allow [priority & fairness](/docs/concepts/cluster-administration/flow-control/)
    in the API server to use a zero value for the `nominalConcurrencyShares` field of
    the `limited` section of a priority level.

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
