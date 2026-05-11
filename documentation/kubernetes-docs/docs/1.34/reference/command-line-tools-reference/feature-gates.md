# Feature Gates

This page contains an overview of the various feature gates an administrator
can specify on different Kubernetes components.

See [feature stages](#feature-stages) for an explanation of the stages for a feature.

## Overview

Feature gates are a set of key=value pairs that describe Kubernetes features.
You can turn these features on or off using the `--feature-gates` command line flag
on each Kubernetes component.

## How to enable Feature Gates

To enable or disable a feature gate for a particular Kubernetes component, use the
`--feature-gates` flag.

This flag accepts a comma-separated list of key=value pairs, where each key is a
feature gate name and each value is either `true` (enable) or `false` (disable).

**Example usage:**

```
kube-apiserver --feature-gates=FeatureName1=true,FeatureName2=false
kubelet --feature-gates=GracefulNodeShutdown=true
```

Each Kubernetes component supports only the feature gates relevant to its functions.
Use `<component> -h` to list available feature gates for a specific component.

For detailed instructions on configuring feature gates in your cluster, see
[Configure Feature Gates](/docs/tasks/administer-cluster/configure-feature-gates/).

## Feature gates in Kubernetes

The following tables are a summary of the feature gates that you can set on
different Kubernetes components.

* The "Since" column contains the Kubernetes release when a feature is introduced
  or its release stage is changed.
* The "Until" column, if not empty, contains the last Kubernetes release in which
  you can still use a feature gate.
* If a feature is in the Alpha or Beta state, you can find the feature listed
  in the [Alpha/Beta feature gate table](#feature-gates-for-alpha-or-beta-features).
* If a feature is stable you can find all stages for that feature listed in the
  [Graduated/Deprecated feature gate table](#feature-gates-for-graduated-or-deprecated-features).
* The [Graduated/Deprecated feature gate table](#feature-gates-for-graduated-or-deprecated-features)
  also lists deprecated and withdrawn features.

> **Note:**
> For a reference to old feature gates that are removed, please refer to
> [feature gates removed](/docs/reference/command-line-tools-reference/feature-gates-removed/).

### Feature gates for Alpha or Beta features

Feature gates for features in Alpha or Beta states

| Feature | Default | Stage | Since | Until |
| --- | --- | --- | --- | --- |
| `AllowParsingUserUIDFromCertAuth` | `false` | Alpha | 1.33 | 1.33 |
| `AllowParsingUserUIDFromCertAuth` | `true` | Beta | 1.34 | – |
| `AllowUnsafeMalformedObjectDeletion` | `false` | Alpha | 1.32 | – |
| `APIResponseCompression` | `false` | Alpha | 1.7 | 1.15 |
| `APIResponseCompression` | `true` | Beta | 1.16 | – |
| `APIServerIdentity` | `false` | Alpha | 1.20 | 1.25 |
| `APIServerIdentity` | `true` | Beta | 1.26 | – |
| `APIServingWithRoutine` | `false` | Alpha | 1.30 | – |
| `CBORServingAndStorage` | `false` | Alpha | 1.32 | – |
| `ClearingNominatedNodeNameAfterBinding` | `false` | Alpha | 1.34 | 1.34 |
| `CloudControllerManagerWebhook` | `false` | Alpha | 1.27 | – |
| `ClusterTrustBundle` | `false` | Alpha | 1.27 | 1.32 |
| `ClusterTrustBundle` | `false` | Beta | 1.33 | – |
| `ClusterTrustBundleProjection` | `false` | Alpha | 1.29 | 1.32 |
| `ClusterTrustBundleProjection` | `false` | Beta | 1.33 | – |
| `ComponentFlagz` | `false` | Alpha | 1.32 | – |
| `ComponentStatusz` | `false` | Alpha | 1.32 | – |
| `ConcurrentWatchObjectDecode` | `false` | Beta | 1.31 | – |
| `ContainerCheckpoint` | `false` | Alpha | 1.25 | 1.29 |
| `ContainerCheckpoint` | `true` | Beta | 1.30 | – |
| `ContainerRestartRules` | `false` | Alpha | 1.34 | – |
| `ContainerStopSignals` | `false` | Alpha | 1.33 | – |
| `ContextualLogging` | `false` | Alpha | 1.24 | – |
| `ContextualLogging` | `true` | Beta | 1.30 | – |
| `CoordinatedLeaderElection` | `false` | Alpha | 1.31 | 1.32 |
| `CoordinatedLeaderElection` | `false` | Beta | 1.33 | – |
| `CPUManagerPolicyAlphaOptions` | `false` | Alpha | 1.23 | – |
| `CPUManagerPolicyBetaOptions` | `true` | Beta | 1.23 | – |
| `CrossNamespaceVolumeDataSource` | `false` | Alpha | 1.26 | – |
| `CSIVolumeHealth` | `false` | Alpha | 1.21 | – |
| `CustomCPUCFSQuotaPeriod` | `false` | Alpha | 1.12 | – |
| `DeclarativeValidation` | `true` | Beta | 1.33 | – |
| `DeclarativeValidationTakeover` | `false` | Beta | 1.33 | – |
| `DeploymentReplicaSetTerminatingReplicas` | `false` | Alpha | 1.33 | – |
| `DetectCacheInconsistency` | `true` | Beta | 1.34 | – |
| `DisableCPUQuotaWithExclusiveCPUs` | `true` | Beta | 1.33 | – |
| `DRAAdminAccess` | `false` | Alpha | 1.32 | 1.33 |
| `DRAAdminAccess` | `true` | Beta | 1.34 | – |
| `DRAConsumableCapacity` | `false` | Alpha | 1.34 | – |
| `DRADeviceBindingConditions` | `false` | Alpha | 1.34 | – |
| `DRADeviceTaints` | `false` | Alpha | 1.33 | – |
| `DRAExtendedResource` | `false` | Alpha | 1.34 | – |
| `DRAPartitionableDevices` | `false` | Alpha | 1.33 | – |
| `DRAPrioritizedList` | `false` | Alpha | 1.33 | 1.33 |
| `DRAPrioritizedList` | `true` | Beta | 1.34 | – |
| `DRAResourceClaimDeviceStatus` | `false` | Alpha | 1.32 | 1.32 |
| `DRAResourceClaimDeviceStatus` | `true` | Beta | 1.33 | – |
| `DRASchedulerFilterTimeout` | `false` | Alpha | 1.34 | – |
| `EnvFiles` | `false` | Alpha | 1.34 | – |
| `EventedPLEG` | `false` | Alpha | 1.26 | – |
| `ExternalServiceAccountTokenSigner` | `false` | Alpha | 1.32 | 1.33 |
| `ExternalServiceAccountTokenSigner` | `true` | Beta | 1.34 | – |
| `GracefulNodeShutdown` | `false` | Alpha | 1.20 | 1.20 |
| `GracefulNodeShutdown` | `true` | Beta | 1.21 | – |
| `GracefulNodeShutdownBasedOnPodPriority` | `false` | Alpha | 1.23 | 1.23 |
| `GracefulNodeShutdownBasedOnPodPriority` | `true` | Beta | 1.24 | – |
| `HostnameOverride` | `false` | Alpha | 1.34 | – |
| `HPAConfigurableTolerance` | `false` | Alpha | 1.33 | – |
| `HPAScaleToZero` | `false` | Alpha | 1.16 | – |
| `ImageMaximumGCAge` | `false` | Alpha | 1.29 | 1.29 |
| `ImageMaximumGCAge` | `true` | Beta | 1.30 | – |
| `ImageVolume` | `false` | Alpha | 1.31 | 1.32 |
| `ImageVolume` | `false` | Beta | 1.33 | – |
| `InformerResourceVersion` | `false` | Alpha | 1.30 | – |
| `InOrderInformers` | `true` | Alpha | 1.33 | 1.33 |
| `InOrderInformers` | `true` | Beta | 1.34 | – |
| `InPlacePodVerticalScaling` | `false` | Alpha | 1.27 | 1.32 |
| `InPlacePodVerticalScaling` | `true` | Beta | 1.33 | – |
| `InPlacePodVerticalScalingExclusiveCPUs` | `false` | Alpha | 1.32 | – |
| `InPlacePodVerticalScalingExclusiveMemory` | `false` | Alpha | 1.34 | – |
| `InTreePluginPortworxUnregister` | `false` | Alpha | 1.23 | – |
| `JobManagedBy` | `false` | Alpha | 1.30 | 1.31 |
| `JobManagedBy` | `true` | Beta | 1.32 | – |
| `KubeletCrashLoopBackOffMax` | `false` | Alpha | 1.32 | – |
| `KubeletEnsureSecretPulledImages` | `false` | Alpha | 1.33 | – |
| `KubeletFineGrainedAuthz` | `false` | Alpha | 1.32 | 1.32 |
| `KubeletFineGrainedAuthz` | `true` | Beta | 1.33 | – |
| `KubeletInUserNamespace` | `false` | Alpha | 1.22 | – |
| `KubeletPodResourcesDynamicResources` | `false` | Alpha | 1.27 | 1.33 |
| `KubeletPodResourcesDynamicResources` | `true` | Beta | 1.34 | – |
| `KubeletPodResourcesGet` | `false` | Alpha | 1.27 | 1.33 |
| `KubeletPodResourcesGet` | `true` | Beta | 1.34 | – |
| `KubeletPSI` | `false` | Alpha | 1.33 | 1.33 |
| `KubeletPSI` | `true` | Beta | 1.34 | – |
| `KubeletSeparateDiskGC` | `false` | Alpha | 1.29 | 1.30 |
| `KubeletSeparateDiskGC` | `true` | Beta | 1.31 | – |
| `KubeletServiceAccountTokenForCredentialProviders` | `false` | Alpha | 1.33 | 1.33 |
| `KubeletServiceAccountTokenForCredentialProviders` | `true` | Beta | 1.34 | – |
| `ListFromCacheSnapshot` | `false` | Alpha | 1.33 | 1.33 |
| `ListFromCacheSnapshot` | `true` | Beta | 1.34 | – |
| `LocalStorageCapacityIsolationFSQuotaMonitoring` | `false` | Alpha | 1.15 | 1.30 |
| `LocalStorageCapacityIsolationFSQuotaMonitoring` | `false` | Beta | 1.31 | – |
| `LoggingAlphaOptions` | `false` | Alpha | 1.24 | – |
| `LoggingBetaOptions` | `true` | Beta | 1.24 | – |
| `MatchLabelKeysInPodTopologySpread` | `false` | Alpha | 1.25 | 1.26 |
| `MatchLabelKeysInPodTopologySpread` | `true` | Beta | 1.27 | – |
| `MatchLabelKeysInPodTopologySpreadSelectorMerge` | `true` | Beta | 1.34 | – |
| `MaxUnavailableStatefulSet` | `false` | Alpha | 1.24 | – |
| `MemoryQoS` | `false` | Alpha | 1.22 | – |
| `MutableCSINodeAllocatableCount` | `false` | Alpha | 1.33 | 1.33 |
| `MutableCSINodeAllocatableCount` | `false` | Beta | 1.34 | – |
| `MutatingAdmissionPolicy` | `false` | Alpha | 1.30 | 1.33 |
| `MutatingAdmissionPolicy` | `false` | Beta | 1.34 | – |
| `NodeLogQuery` | `false` | Alpha | 1.27 | 1.29 |
| `NodeLogQuery` | `false` | Beta | 1.30 | – |
| `NominatedNodeNameForExpectation` | `false` | Alpha | 1.34 | – |
| `OpenAPIEnums` | `false` | Alpha | 1.23 | 1.23 |
| `OpenAPIEnums` | `true` | Beta | 1.24 | – |
| `PodAndContainerStatsFromCRI` | `false` | Alpha | 1.23 | – |
| `PodCertificateRequest` | `false` | Alpha | 1.34 | – |
| `PodDeletionCost` | `false` | Alpha | 1.21 | 1.21 |
| `PodDeletionCost` | `true` | Beta | 1.22 | – |
| `PodLevelResources` | `false` | Alpha | 1.32 | 1.33 |
| `PodLevelResources` | `true` | Beta | 1.34 | – |
| `PodLogsQuerySplitStreams` | `false` | Alpha | 1.32 | – |
| `PodObservedGenerationTracking` | `false` | Alpha | 1.33 | 1.33 |
| `PodObservedGenerationTracking` | `true` | Beta | 1.34 | – |
| `PodReadyToStartContainersCondition` | `false` | Alpha | 1.28 | 1.28 |
| `PodReadyToStartContainersCondition` | `true` | Beta | 1.29 | – |
| `PodTopologyLabelsAdmission` | `false` | Alpha | 1.33 | – |
| `PortForwardWebsockets` | `false` | Alpha | 1.30 | 1.30 |
| `PortForwardWebsockets` | `true` | Beta | 1.31 | – |
| `PreferSameTrafficDistribution` | `false` | Alpha | 1.33 | 1.33 |
| `PreferSameTrafficDistribution` | `true` | Beta | 1.34 | – |
| `PreventStaticPodAPIReferences` | `true` | Beta | 1.34 | – |
| `ProcMountType` | `false` | Alpha | 1.12 | 1.30 |
| `ProcMountType` | `false` | Beta | 1.31 | 1.32 |
| `ProcMountType` | `true` | Beta | 1.33 | – |
| `QOSReserved` | `false` | Alpha | 1.11 | – |
| `ReduceDefaultCrashLoopBackOffDecay` | `false` | Alpha | 1.33 | – |
| `RelaxedServiceNameValidation` | `false` | Alpha | 1.34 | – |
| `ReloadKubeletServerCertificateFile` | `true` | Beta | 1.31 | – |
| `RemoteRequestHeaderUID` | `false` | Alpha | 1.32 | – |
| `ResourceHealthStatus` | `false` | Alpha | 1.31 | – |
| `RotateKubeletServerCertificate` | `false` | Alpha | 1.7 | 1.11 |
| `RotateKubeletServerCertificate` | `true` | Beta | 1.12 | – |
| `RuntimeClassInImageCriApi` | `false` | Alpha | 1.29 | – |
| `SchedulerAsyncAPICalls` | `true` | Beta | 1.34 | – |
| `SchedulerAsyncPreemption` | `false` | Alpha | 1.32 | 1.32 |
| `SchedulerAsyncPreemption` | `true` | Beta | 1.33 | – |
| `SchedulerPopFromBackoffQ` | `true` | Beta | 1.33 | – |
| `SELinuxChangePolicy` | `false` | Alpha | 1.32 | 1.32 |
| `SELinuxChangePolicy` | `true` | Beta | 1.33 | – |
| `SELinuxMount` | `false` | Alpha | 1.30 | 1.32 |
| `SELinuxMount` | `false` | Beta | 1.33 | – |
| `SELinuxMountReadWriteOncePod` | `false` | Alpha | 1.25 | 1.26 |
| `SELinuxMountReadWriteOncePod` | `false` | Beta | 1.27 | 1.27 |
| `SELinuxMountReadWriteOncePod` | `true` | Beta | 1.28 | – |
| `ServiceAcccountNodeAudienceRestriction` | `false` | Beta | 1.32 | 1.32 |
| `ServiceAcccountNodeAudienceRestriction` | `true` | Beta | 1.33 | – |
| `SizeBasedListCostEstimate` | `true` | Beta | 1.34 | – |
| `StorageCapacityScoring` | `false` | Alpha | 1.33 | – |
| `StorageVersionAPI` | `false` | Alpha | 1.20 | – |
| `StorageVersionHash` | `false` | Alpha | 1.14 | 1.14 |
| `StorageVersionHash` | `true` | Beta | 1.15 | – |
| `StorageVersionMigrator` | `false` | Alpha | 1.30 | – |
| `StrictIPCIDRValidation` | `false` | Alpha | 1.33 | – |
| `StructuredAuthenticationConfigurationEgressSelector` | `true` | Beta | 1.34 | – |
| `SupplementalGroupsPolicy` | `false` | Alpha | 1.31 | 1.32 |
| `SupplementalGroupsPolicy` | `true` | Beta | 1.33 | – |
| `SystemdWatchdog` | `true` | Beta | 1.32 | – |
| `TokenRequestServiceAccountUIDValidation` | `true` | Beta | 1.34 | – |
| `TopologyManagerPolicyAlphaOptions` | `false` | Alpha | 1.26 | – |
| `TopologyManagerPolicyBetaOptions` | `false` | Beta | 1.26 | 1.27 |
| `TopologyManagerPolicyBetaOptions` | `true` | Beta | 1.28 | – |
| `TranslateStreamCloseWebsocketRequests` | `false` | Alpha | 1.29 | 1.29 |
| `TranslateStreamCloseWebsocketRequests` | `true` | Beta | 1.30 | – |
| `UnauthenticatedHTTP2DOSMitigation` | `false` | Beta | 1.28 | 1.28 |
| `UnauthenticatedHTTP2DOSMitigation` | `true` | Beta | 1.29 | – |
| `UnknownVersionInteroperabilityProxy` | `false` | Alpha | 1.28 | – |
| `UserNamespacesPodSecurityStandards` | `false` | Alpha | 1.29 | – |
| `UserNamespacesSupport` | `false` | Alpha | 1.28 | 1.29 |
| `UserNamespacesSupport` | `false` | Beta | 1.30 | 1.32 |
| `UserNamespacesSupport` | `true` | Beta | 1.33 | – |
| `WatchCacheInitializationPostStartHook` | `false` | Beta | 1.31 | – |
| `WatchList` | `false` | Alpha | 1.27 | 1.31 |
| `WatchList` | `true` | Beta | 1.32 | 1.32 |
| `WatchList` | `false` | Beta | 1.33 | 1.33 |
| `WatchList` | `true` | Beta | 1.34 | – |
| `WatchListClient` | `false` | Beta | 1.30 | – |
| `WindowsCPUAndMemoryAffinity` | `false` | Alpha | 1.32 | – |
| `WindowsGracefulNodeShutdown` | `false` | Alpha | 1.32 | 1.33 |
| `WindowsGracefulNodeShutdown` | `true` | Beta | 1.34 | – |

### Feature gates for graduated or deprecated features

Feature Gates for Graduated or Deprecated Features

| Feature | Default | Stage | Since | Until |
| --- | --- | --- | --- | --- |
| `AllowDNSOnlyNodeCSR` | `false` | Deprecated | 1.31 | – |
| `AllowInsecureKubeletCertificateSigningRequests` | `false` | Deprecated | 1.31 | – |
| `AllowServiceLBStatusOnNonLB` | `false` | Deprecated | 1.29 | – |
| `AnonymousAuthConfigurableEndpoints` | `false` | Alpha | 1.31 | 1.31 |
| `AnonymousAuthConfigurableEndpoints` | `true` | Beta | 1.32 | 1.33 |
| `AnonymousAuthConfigurableEndpoints` | `true` | GA | 1.34 | – |
| `AnyVolumeDataSource` | `false` | Alpha | 1.18 | 1.23 |
| `AnyVolumeDataSource` | `true` | Beta | 1.24 | 1.32 |
| `AnyVolumeDataSource` | `true` | GA | 1.33 | – |
| `APIServerTracing` | `false` | Alpha | 1.22 | 1.26 |
| `APIServerTracing` | `true` | Beta | 1.27 | 1.33 |
| `APIServerTracing` | `true` | GA | 1.34 | – |
| `AuthorizeNodeWithSelectors` | `false` | Alpha | 1.31 | 1.31 |
| `AuthorizeNodeWithSelectors` | `true` | Beta | 1.32 | 1.33 |
| `AuthorizeNodeWithSelectors` | `true` | GA | 1.34 | – |
| `AuthorizeWithSelectors` | `false` | Alpha | 1.31 | 1.31 |
| `AuthorizeWithSelectors` | `true` | Beta | 1.32 | 1.33 |
| `AuthorizeWithSelectors` | `true` | GA | 1.34 | – |
| `BtreeWatchCache` | `true` | Beta | 1.32 | 1.32 |
| `BtreeWatchCache` | `true` | GA | 1.33 | – |
| `ComponentSLIs` | `false` | Alpha | 1.26 | 1.26 |
| `ComponentSLIs` | `true` | Beta | 1.27 | 1.31 |
| `ComponentSLIs` | `true` | GA | 1.32 | – |
| `ConsistentListFromCache` | `false` | Alpha | 1.28 | 1.30 |
| `ConsistentListFromCache` | `true` | Beta | 1.31 | 1.33 |
| `ConsistentListFromCache` | `true` | GA | 1.34 | – |
| `CPUManagerPolicyOptions` | `false` | Alpha | 1.22 | 1.22 |
| `CPUManagerPolicyOptions` | `true` | Beta | 1.23 | 1.32 |
| `CPUManagerPolicyOptions` | `true` | GA | 1.33 | – |
| `CRDValidationRatcheting` | `false` | Alpha | 1.28 | 1.29 |
| `CRDValidationRatcheting` | `true` | Beta | 1.30 | 1.32 |
| `CRDValidationRatcheting` | `true` | GA | 1.33 | – |
| `CronJobsScheduledAnnotation` | `true` | Beta | 1.28 | 1.31 |
| `CronJobsScheduledAnnotation` | `true` | GA | 1.32 | – |
| `CSIMigrationPortworx` | `false` | Alpha | 1.23 | 1.24 |
| `CSIMigrationPortworx` | `false` | Beta | 1.25 | 1.30 |
| `CSIMigrationPortworx` | `true` | Beta | 1.31 | 1.32 |
| `CSIMigrationPortworx` | `true` | GA | 1.33 | – |
| `CustomResourceFieldSelectors` | `false` | Alpha | 1.30 | 1.30 |
| `CustomResourceFieldSelectors` | `true` | Beta | 1.31 | 1.31 |
| `CustomResourceFieldSelectors` | `true` | GA | 1.32 | – |
| `DisableAllocatorDualWrite` | `false` | Alpha | 1.31 | 1.32 |
| `DisableAllocatorDualWrite` | `false` | Beta | 1.33 | 1.33 |
| `DisableAllocatorDualWrite` | `true` | GA | 1.34 | – |
| `DisableNodeKubeProxyVersion` | `false` | Alpha | 1.29 | 1.30 |
| `DisableNodeKubeProxyVersion` | `true` | Beta | 1.31.0 | 1.31.0 |
| `DisableNodeKubeProxyVersion` | `false` | Deprecated | 1.31.1 | – |
| `DisableNodeKubeProxyVersion` | `false` | Deprecated | 1.32 | 1.32 |
| `DisableNodeKubeProxyVersion` | `true` | Deprecated | 1.33 | – |
| `DynamicResourceAllocation` | `false` | Alpha | 1.30 | 1.31 |
| `DynamicResourceAllocation` | `false` | Beta | 1.32 | 1.33 |
| `DynamicResourceAllocation` | `true` | GA | 1.34 | – |
| `ElasticIndexedJob` | `true` | Beta | 1.27 | 1.30 |
| `ElasticIndexedJob` | `true` | GA | 1.31 | – |
| `ExecProbeTimeout` | `true` | GA | 1.20 | – |
| `GitRepoVolumeDriver` | `false` | Deprecated | 1.33 | – |
| `HonorPVReclaimPolicy` | `false` | Alpha | 1.23 | 1.30 |
| `HonorPVReclaimPolicy` | `true` | Beta | 1.31 | 1.32 |
| `HonorPVReclaimPolicy` | `true` | GA | 1.33 | – |
| `InPlacePodVerticalScalingAllocatedStatus` | `false` | Alpha | 1.32 | 1.32 |
| `InPlacePodVerticalScalingAllocatedStatus` | `false` | Deprecated | 1.33 | – |
| `JobBackoffLimitPerIndex` | `false` | Alpha | 1.28 | 1.28 |
| `JobBackoffLimitPerIndex` | `true` | Beta | 1.29 | 1.32 |
| `JobBackoffLimitPerIndex` | `true` | GA | 1.33 | – |
| `JobPodReplacementPolicy` | `false` | Alpha | 1.28 | 1.28 |
| `JobPodReplacementPolicy` | `true` | Beta | 1.29 | 1.33 |
| `JobPodReplacementPolicy` | `true` | GA | 1.34 | – |
| `JobSuccessPolicy` | `false` | Alpha | 1.30 | 1.30 |
| `JobSuccessPolicy` | `true` | Beta | 1.31 | 1.32 |
| `JobSuccessPolicy` | `true` | GA | 1.33 | – |
| `KMSv1` | `true` | Deprecated | 1.28 | 1.28 |
| `KMSv1` | `false` | Deprecated | 1.29 | – |
| `KubeletCgroupDriverFromCRI` | `false` | Alpha | 1.28 | 1.30 |
| `KubeletCgroupDriverFromCRI` | `true` | Beta | 1.31 | – |
| `KubeletCgroupDriverFromCRI` | `true` | GA | 1.34 | – |
| `KubeletTracing` | `false` | Alpha | 1.25 | 1.26 |
| `KubeletTracing` | `true` | Beta | 1.27 | 1.33 |
| `KubeletTracing` | `true` | GA | 1.34 | – |
| `LoadBalancerIPMode` | `false` | Alpha | 1.29 | 1.30 |
| `LoadBalancerIPMode` | `true` | Beta | 1.30 | 1.31 |
| `LoadBalancerIPMode` | `true` | GA | 1.32 | – |
| `LogarithmicScaleDown` | `false` | Alpha | 1.21 | 1.21 |
| `LogarithmicScaleDown` | `true` | Beta | 1.22 | 1.30 |
| `LogarithmicScaleDown` | `true` | GA | 1.31 | – |
| `MatchLabelKeysInPodAffinity` | `false` | Alpha | 1.29 | 1.30 |
| `MatchLabelKeysInPodAffinity` | `true` | Beta | 1.31 | 1.32 |
| `MatchLabelKeysInPodAffinity` | `true` | GA | 1.33 | – |
| `MemoryManager` | `false` | Alpha | 1.21 | 1.21 |
| `MemoryManager` | `true` | Beta | 1.22 | 1.31 |
| `MemoryManager` | `true` | GA | 1.32 | – |
| `MultiCIDRServiceAllocator` | `false` | Alpha | 1.27 | 1.30 |
| `MultiCIDRServiceAllocator` | `false` | Beta | 1.31 | 1.32 |
| `MultiCIDRServiceAllocator` | `true` | GA | 1.33 | – |
| `NFTablesProxyMode` | `false` | Alpha | 1.29 | 1.30 |
| `NFTablesProxyMode` | `true` | Beta | 1.31 | 1.32 |
| `NFTablesProxyMode` | `true` | GA | 1.33 | – |
| `NodeInclusionPolicyInPodTopologySpread` | `false` | Alpha | 1.25 | 1.25 |
| `NodeInclusionPolicyInPodTopologySpread` | `true` | Beta | 1.26 | 1.32 |
| `NodeInclusionPolicyInPodTopologySpread` | `true` | GA | 1.33 | – |
| `NodeSwap` | `false` | Alpha | 1.22 | 1.27 |
| `NodeSwap` | `false` | Beta | 1.28 | 1.29 |
| `NodeSwap` | `true` | Beta | 1.30 | 1.33 |
| `NodeSwap` | `true` | GA | 1.34 | – |
| `OrderedNamespaceDeletion` | `false` | Beta | 1.30 | 1.32 |
| `OrderedNamespaceDeletion` | `true` | Beta | 1.33 | 1.33 |
| `OrderedNamespaceDeletion` | `true` | GA | 1.34 | – |
| `PodIndexLabel` | `true` | Beta | 1.28 | 1.31 |
| `PodIndexLabel` | `true` | GA | 1.32 | – |
| `PodLifecycleSleepAction` | `false` | Alpha | 1.29 | 1.29 |
| `PodLifecycleSleepAction` | `true` | Beta | 1.30 | 1.33 |
| `PodLifecycleSleepAction` | `true` | GA | 1.34 | – |
| `PodLifecycleSleepActionAllowZero` | `false` | Alpha | 1.32 | 1.32 |
| `PodLifecycleSleepActionAllowZero` | `true` | Beta | 1.33 | 1.33 |
| `PodLifecycleSleepActionAllowZero` | `true` | GA | 1.34 | – |
| `PodSchedulingReadiness` | `false` | Alpha | 1.26 | 1.26 |
| `PodSchedulingReadiness` | `true` | Beta | 1.27 | 1.29 |
| `PodSchedulingReadiness` | `true` | GA | 1.30 | – |
| `RecoverVolumeExpansionFailure` | `false` | Alpha | 1.23 | 1.31 |
| `RecoverVolumeExpansionFailure` | `true` | Beta | 1.32 | 1.33 |
| `RecoverVolumeExpansionFailure` | `true` | GA | 1.34 | – |
| `RecursiveReadOnlyMounts` | `false` | Alpha | 1.30 | 1.30 |
| `RecursiveReadOnlyMounts` | `true` | Beta | 1.31 | 1.32 |
| `RecursiveReadOnlyMounts` | `true` | GA | 1.33 | – |
| `RelaxedDNSSearchValidation` | `false` | Alpha | 1.32 | 1.32 |
| `RelaxedDNSSearchValidation` | `true` | Beta | 1.33 | 1.33 |
| `RelaxedDNSSearchValidation` | `true` | GA | 1.34 | – |
| `RelaxedEnvironmentVariableValidation` | `false` | Alpha | 1.30 | 1.31 |
| `RelaxedEnvironmentVariableValidation` | `true` | Beta | 1.32 | 1.33 |
| `RelaxedEnvironmentVariableValidation` | `true` | GA | 1.34 | – |
| `ResilientWatchCacheInitialization` | `true` | Beta | 1.31 | 1.33 |
| `ResilientWatchCacheInitialization` | `true` | GA | 1.34 | – |
| `RetryGenerateName` | `false` | Alpha | 1.30 | 1.30 |
| `RetryGenerateName` | `true` | Beta | 1.31 | 1.31 |
| `RetryGenerateName` | `true` | GA | 1.32 | – |
| `SchedulerQueueingHints` | `true` | Beta | 1.28 | 1.28 |
| `SchedulerQueueingHints` | `false` | Beta | 1.29 | 1.31 |
| `SchedulerQueueingHints` | `true` | Beta | 1.32 | 1.33 |
| `SchedulerQueueingHints` | `true` | GA | 1.34 | – |
| `SeparateCacheWatchRPC` | `true` | Beta | 1.28 | 1.32 |
| `SeparateCacheWatchRPC` | `false` | Deprecated | 1.33 | – |
| `SeparateTaintEvictionController` | `true` | Beta | 1.29 | 1.33 |
| `SeparateTaintEvictionController` | `true` | GA | 1.34 | – |
| `ServiceAccountTokenJTI` | `false` | Alpha | 1.29 | 1.29 |
| `ServiceAccountTokenJTI` | `true` | Beta | 1.30 | 1.31 |
| `ServiceAccountTokenJTI` | `true` | GA | 1.32 | – |
| `ServiceAccountTokenNodeBinding` | `false` | Alpha | 1.29 | 1.30 |
| `ServiceAccountTokenNodeBinding` | `true` | Beta | 1.31 | 1.32 |
| `ServiceAccountTokenNodeBinding` | `true` | GA | 1.33 | – |
| `ServiceAccountTokenNodeBindingValidation` | `false` | Alpha | 1.29 | 1.29 |
| `ServiceAccountTokenNodeBindingValidation` | `true` | Beta | 1.30 | 1.31 |
| `ServiceAccountTokenNodeBindingValidation` | `true` | GA | 1.32 | – |
| `ServiceAccountTokenPodNodeInfo` | `false` | Alpha | 1.29 | 1.29 |
| `ServiceAccountTokenPodNodeInfo` | `true` | Beta | 1.30 | 1.31 |
| `ServiceAccountTokenPodNodeInfo` | `true` | GA | 1.32 | – |
| `ServiceTrafficDistribution` | `false` | Alpha | 1.30 | 1.30 |
| `ServiceTrafficDistribution` | `true` | Beta | 1.31 | 1.32 |
| `ServiceTrafficDistribution` | `true` | GA | 1.33 | – |
| `SidecarContainers` | `false` | Alpha | 1.28 | 1.28 |
| `SidecarContainers` | `true` | Beta | 1.29 | 1.32 |
| `SidecarContainers` | `true` | GA | 1.33 | – |
| `SizeMemoryBackedVolumes` | `false` | Alpha | 1.20 | 1.21 |
| `SizeMemoryBackedVolumes` | `true` | Beta | 1.22 | 1.31 |
| `SizeMemoryBackedVolumes` | `true` | GA | 1.32 | – |
| `StatefulSetAutoDeletePVC` | `false` | Alpha | 1.23 | 1.26 |
| `StatefulSetAutoDeletePVC` | `true` | Beta | 1.27 | 1.31 |
| `StatefulSetAutoDeletePVC` | `true` | GA | 1.32 | – |
| `StatefulSetStartOrdinal` | `false` | Alpha | 1.26 | 1.26 |
| `StatefulSetStartOrdinal` | `true` | Beta | 1.27 | 1.30 |
| `StatefulSetStartOrdinal` | `true` | GA | 1.31 | – |
| `StorageNamespaceIndex` | `true` | Beta | 1.30 | 1.32 |
| `StorageNamespaceIndex` | `true` | Deprecated | 1.33 | – |
| `StreamingCollectionEncodingToJSON` | `true` | Beta | 1.33 | 1.33 |
| `StreamingCollectionEncodingToJSON` | `true` | GA | 1.34 | – |
| `StreamingCollectionEncodingToProtobuf` | `true` | Alpha | 1.33 | 1.33 |
| `StreamingCollectionEncodingToProtobuf` | `true` | GA | 1.34 | – |
| `StrictCostEnforcementForVAP` | `false` | Beta | 1.30 | 1.31 |
| `StrictCostEnforcementForVAP` | `true` | GA | 1.32 | – |
| `StrictCostEnforcementForWebhooks` | `false` | Beta | 1.31 | 1.31 |
| `StrictCostEnforcementForWebhooks` | `true` | GA | 1.32 | – |
| `StructuredAuthenticationConfiguration` | `false` | Alpha | 1.29 | 1.29 |
| `StructuredAuthenticationConfiguration` | `true` | Beta | 1.30 | 1.33 |
| `StructuredAuthenticationConfiguration` | `true` | GA | 1.34 | – |
| `StructuredAuthorizationConfiguration` | `false` | Alpha | 1.29 | 1.29 |
| `StructuredAuthorizationConfiguration` | `true` | Beta | 1.30 | 1.31 |
| `StructuredAuthorizationConfiguration` | `true` | GA | 1.32 | – |
| `TopologyAwareHints` | `false` | Alpha | 1.21 | 1.22 |
| `TopologyAwareHints` | `false` | Beta | 1.23 | 1.23 |
| `TopologyAwareHints` | `true` | Beta | 1.24 | 1.32 |
| `TopologyAwareHints` | `true` | GA | 1.33 | – |
| `TopologyManagerPolicyOptions` | `false` | Alpha | 1.26 | 1.27 |
| `TopologyManagerPolicyOptions` | `true` | Beta | 1.28 | 1.31 |
| `TopologyManagerPolicyOptions` | `true` | GA | 1.32 | – |
| `VolumeAttributesClass` | `false` | Alpha | 1.29 | 1.30 |
| `VolumeAttributesClass` | `false` | Beta | 1.31 | 1.33 |
| `VolumeAttributesClass` | `true` | GA | 1.34 | – |
| `WatchFromStorageWithoutResourceVersion` | `false` | Beta | 1.30 | 1.32 |
| `WatchFromStorageWithoutResourceVersion` | `false` | Deprecated | 1.33 | – |
| `WindowsHostNetwork` | `true` | Alpha | 1.26 | 1.32 |
| `WindowsHostNetwork` | `false` | Deprecated | 1.33 | – |
| `WinDSR` | `false` | Alpha | 1.14 | 1.32 |
| `WinDSR` | `true` | Beta | 1.33 | 1.33 |
| `WinDSR` | `true` | GA | 1.34 | – |
| `WinOverlay` | `false` | Alpha | 1.14 | 1.19 |
| `WinOverlay` | `true` | Beta | 1.20 | 1.33 |
| `WinOverlay` | `true` | GA | 1.34 | – |

## Using a feature

### Feature stages

A feature can be in *Alpha*, *Beta* or *GA* stage.
An *Alpha* feature means:

* Disabled by default.
* Might be buggy. Enabling the feature may expose bugs.
* Support for feature may be dropped at any time without notice.
* The API may change in incompatible ways in a later software release without notice.
* Recommended for use only in short-lived testing clusters, due to increased
  risk of bugs and lack of long-term support.

A *Beta* feature means:

* Usually enabled by default. Beta API groups are
  [disabled by default](https://github.com/kubernetes/enhancements/tree/master/keps/sig-architecture/3136-beta-apis-off-by-default).
* The feature is well tested. Enabling the feature is considered safe.
* Support for the overall feature will not be dropped, though details may change.
* The schema and/or semantics of objects may change in incompatible ways in a
  subsequent beta or stable release. When this happens, we will provide instructions
  for migrating to the next version. This may require deleting, editing, and
  re-creating API objects. The editing process may require some thought.
  This may require downtime for applications that rely on the feature.
* Recommended for only non-business-critical uses because of potential for
  incompatible changes in subsequent releases. If you have multiple clusters
  that can be upgraded independently, you may be able to relax this restriction.

> **Note:**
> Please do try *Beta* features and give feedback on them!
> After they exit beta, it may not be practical for us to make more changes.

A *General Availability* (GA) feature is also referred to as a *stable* feature. It means:

* The feature is always enabled; you cannot disable it.
* The corresponding feature gate is no longer needed.
* Stable versions of features will appear in released software for many subsequent versions.

## List of feature gates

Each feature gate is designed for enabling/disabling a specific feature.

`AllowDNSOnlyNodeCSR`
:   Allow kubelet to request a certificate without any Node IP available, only with DNS names.

`AllowInsecureKubeletCertificateSigningRequests`
:   Disable node admission validation of
    [CertificateSigningRequests](/docs/reference/access-authn-authz/certificate-signing-requests/#certificate-signing-requests)
    for kubelet signers. Unless you disable this feature gate, Kubernetes enforces that new
    kubelet certificates have a `commonName` matching `system:node:$nodeName`.

`AllowParsingUserUIDFromCertAuth`
:   When this feature is enabled, the subject name attribute `1.3.6.1.4.1.57683.2`
    in an X.509 certificate will be parsed as the user UID during certificate authentication.

`AllowServiceLBStatusOnNonLB`
:   Enables `.status.ingress.loadBalancer` to be set on Services of types other than `LoadBalancer`.

`AllowUnsafeMalformedObjectDeletion`
:   Enables the cluster operator to identify corrupt resource(s) using the **list**
    operation, and introduces an option `ignoreStoreReadErrorWithClusterBreakingPotential`
    that the operator can set to perform unsafe and force **delete** operation of
    such corrupt resource(s) using the Kubernetes API.

`AnonymousAuthConfigurableEndpoints`
:   Enable [configurable endpoints for anonymous auth](/docs/reference/access-authn-authz/authentication/#anonymous-authenticator-configuration)
    for the API server.

`AnyVolumeDataSource`
:   Enable use of any custom resource as the `DataSource` of a
    [PVC](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims "Claims storage resources defined in a PersistentVolume so that it can be mounted as a volume in a container.").

`APIResponseCompression`
:   Compress the API responses for `LIST` or `GET` requests.

`APIServerIdentity`
:   Assign each API server an ID in a cluster, using a [Lease](/docs/concepts/architecture/leases/).

`APIServerTracing`
:   Add support for distributed tracing in the API server.
    See [Traces for Kubernetes System Components](/docs/concepts/cluster-administration/system-traces/) for more details.

`APIServingWithRoutine`
:   This feature gate enables an API server performance improvement:
    the API server can use separate goroutines (lightweight threads managed by the Go runtime)
    to serve [**watch**](/docs/reference/using-api/api-concepts/#efficient-detection-of-changes)
    requests.

`AuthorizeNodeWithSelectors`
:   Make the [Node authorizer](/docs/reference/access-authn-authz/node/) use fine-grained selector authorization.

`AuthorizeWithSelectors`
:   Allows authorization to use field and label selectors.
    Enables `fieldSelector` and `labelSelector` fields in the [SubjectAccessReview API](/docs/reference/kubernetes-api/authorization-resources/subject-access-review-v1/),
    passes field and label selector information to [authorization webhooks](/docs/reference/access-authn-authz/webhook/),
    enables `fieldSelector` and `labelSelector` functions in the [authorizer CEL library](https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#AuthzSelectors),
    and enables checking `fieldSelector` and `labelSelector` fields in [authorization webhook `matchConditions`](/docs/reference/access-authn-authz/authorization/#using-configuration-file-for-authorization).

`BtreeWatchCache`
:   When enabled, the API server will replace the legacy HashMap-based *watch cache*
    with a BTree-based implementation. This replacement may bring performance improvements.

`CBORServingAndStorage`
:   Enables CBOR as a [supported encoding for requests and
    responses](/docs/reference/using-api/api-concepts/#cbor-encoding), and as the preferred storage
    encoding for custom resources.

`ClearingNominatedNodeNameAfterBinding`
:   Enable clearing `.status.nominatedNodeName` whenever Pods are bound to nodes.

`CloudControllerManagerWebhook`
:   Enable webhooks in cloud controller manager.

`ClusterTrustBundle`
:   Enable ClusterTrustBundle objects and kubelet integration.

`ClusterTrustBundleProjection`
:   [`clusterTrustBundle` projected volume sources](/docs/concepts/storage/projected-volumes/#clustertrustbundle).

`ComponentFlagz`
:   Enables the component's flagz endpoint.
    See [zpages](/docs/reference/instrumentation/zpages/) for more information.

`ComponentSLIs`
:   Enable the `/metrics/slis` endpoint on Kubernetes components like
    kubelet, kube-scheduler, kube-proxy, kube-controller-manager, cloud-controller-manager
    allowing you to scrape health check metrics.

`ComponentStatusz`
:   Enables the component's statusz endpoint.
    See [zpages](/docs/reference/instrumentation/zpages/) for more information.

`ConcurrentWatchObjectDecode`
:   Enable concurrent watch object decoding. This is to avoid starving the API server's
    watch cache when a conversion webhook is installed.

`ConsistentListFromCache`
:   Enhance Kubernetes API server performance by serving consistent **list** requests
    directly from its watch cache, improving scalability and response times.
    To consistent list from cache Kubernetes requires a newer etcd version (v3.4.31+ or v3.5.13+),
    that includes fixes to watch progress request feature.
    If older etcd version is provided Kubernetes will automatically detect it and fallback to serving consistent reads from etcd.
    Progress notifications ensure watch cache is consistent with etcd while reducing
    the need for resource-intensive quorum reads from etcd.

    See the Kubernetes documentation on [Semantics for **get** and **list**](/docs/reference/using-api/api-concepts/#semantics-for-get-and-list) for more details.

`ContainerCheckpoint`
:   Enables the kubelet `checkpoint` API.
    See [Kubelet Checkpoint API](/docs/reference/node/kubelet-checkpoint-api/) for more details.

`ContainerRestartRules`
:   Enables the ability to configure container-level restart policy and restart rules.
    See [Container Restart Policy and Rules](/docs/concepts/workloads/pods/pod-lifecycle/#container-restart-rules) for more details.

`ContainerStopSignals`
:   Enables usage of the StopSignal lifecycle for containers for configuring custom stop signals using which the containers would be stopped.

`ContextualLogging`
:   Enables extra details in log output of Kubernetes components that support
    contextual logging.

`CoordinatedLeaderElection`
:   Enables the behaviors supporting the LeaseCandidate API, and also enables
    coordinated leader election for the Kubernetes control plane, deterministically.

`CPUManagerPolicyAlphaOptions`
:   This allows fine-tuning of CPUManager policies,
    experimental, Alpha-quality options
    This feature gate guards *a group* of CPUManager options whose quality level is alpha.
    This feature gate will never graduate to beta or stable.

`CPUManagerPolicyBetaOptions`
:   This allows fine-tuning of CPUManager policies,
    experimental, Beta-quality options
    This feature gate guards *a group* of CPUManager options whose quality level is beta.
    This feature gate will never graduate to stable.

`CPUManagerPolicyOptions`
:   Allow fine-tuning of CPUManager policies.

`CRDValidationRatcheting`
:   Enable updates to custom resources to contain
    violations of their OpenAPI schema if the offending portions of the resource
    update did not change. See [Validation Ratcheting](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#validation-ratcheting) for more details.

`CronJobsScheduledAnnotation`
:   Set the scheduled job time as an
    [annotation](/docs/concepts/overview/working-with-objects/annotations "A key-value pair that is used to attach arbitrary non-identifying metadata to objects.") on Jobs that were created
    on behalf of a CronJob.

`CrossNamespaceVolumeDataSource`
:   Enable the usage of cross namespace volume data source
    to allow you to specify a source namespace in the `dataSourceRef` field of a
    PersistentVolumeClaim.

`CSIMigrationPortworx`
:   Enables shims and translation logic to route volume operations
    from the Portworx in-tree plugin to Portworx CSI plugin.
    Requires Portworx CSI driver to be installed and configured in the cluster.

`CSIVolumeHealth`
:   Enable support for CSI volume health monitoring on node.

`CustomCPUCFSQuotaPeriod`
:   Enable nodes to change `cpuCFSQuotaPeriod` in
    [kubelet config](/docs/tasks/administer-cluster/kubelet-config-file/).

`CustomResourceFieldSelectors`
:   Enable `selectableFields` in the
    [CustomResourceDefinition](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/ "Custom code that defines a resource to add to your Kubernetes API server without building a complete custom server.") API to allow filtering
    of custom resource **list**, **watch** and **deletecollection** requests.

`DeclarativeValidation`
:   Enables declarative validation of in-tree Kubernetes APIs. When enabled, APIs with declarative validation rules (defined using IDL tags in the Go code) will have both the generated declarative validation code and the original hand-written validation code executed. The results are compared, and any discrepancies are reported via the `declarative_validation_mismatch_total` metric. Only the hand-written validation result is returned to the user (eg: actually validates in the request path). The original hand-written validation are still the authoritative validations when this is enabled but this can be changed if the [DeclarativeValidationTakeover feature gate](/docs/reference/command-line-tools-reference/feature-gates/DeclarativeValidationTakeover.md) is enabled in addition to this gate. This feature gate only operates on the kube-apiserver.

`DeclarativeValidationTakeover`
:   When enabled, along with the [DeclarativeValidation](/docs/reference/command-line-tools-reference/feature-gates/DeclarativeValidation.md) feature gate, declarative validation errors are returned directly to the caller, replacing hand-written validation errors for rules that have declarative implementations. When disabled (and `DeclarativeValidation` is enabled), hand-written validation errors are always returned, effectively putting declarative validation in a **mismatch validation mode** that monitors but does not affect API responses. This **mismatch validation mode** allows for the monitoring of the `declarative_validation_mismatch_total` and `declarative_validation_panic_total` metrics which are implementation details for a safer rollout, average user shouldn't need to interact with it directly. This feature gate only operates on the kube-apiserver. Note: Although declarative validation aims for functional equivalence with hand-written validation, the exact description of error messages may differ between the two approaches.

`DeploymentReplicaSetTerminatingReplicas`
:   Enables a new status field `.status.terminatingReplicas` in Deployments and ReplicaSets to allow tracking of terminating pods.

`DetectCacheInconsistency`
:   Enable cache inconsistency detection in the API server.

`DisableAllocatorDualWrite`
:   You can enable the `MultiCIDRServiceAllocator` feature gate. The API server supports migration
    from the old bitmap ClusterIP allocators to the new IPAddress allocators.

    The API server performs a dual-write on both allocators. This feature gate disables the dual write
    on the new Cluster IP allocators; you can enable this feature gate if you have completed the
    relevant stage of the migration.

`DisableCPUQuotaWithExclusiveCPUs`
:   When the feature gate `DisableCPUQuotaWithExclusiveCPUs` is enabled (the default), then Kubernetes
    does **not** enforce CPU quota for Pods that use the [Guaranteed](/docs/concepts/workloads/pods/pod-qos/#guaranteed)
    [QoS class](/docs/concepts/workloads/pods/pod-qos/ "QoS Class (Quality of Service Class) provides a way for Kubernetes to classify pods within the cluster into several classes and make decisions about scheduling and eviction.").

    You can disable the `DisableCPUQuotaWithExclusiveCPUs` feature gate to restore the legacy behavior.

`DisableNodeKubeProxyVersion`
:   Disable setting the `kubeProxyVersion` field of the Node.

`DRAAdminAccess`
:   Enables support for requesting [admin access](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#admin-access)
    in a ResourceClaim or a ResourceClaimTemplate. Admin access grants access to
    in-use devices and may enable additional permissions when making the device
    available in a container. Starting with Kubernetes v1.33, only users authorized
    to create ResourceClaim or ResourceClaimTemplate objects in namespaces labeled
    with `resource.kubernetes.io/admin-access: "true"` (case-sensitive) can use the
    `adminAccess` field. This ensures that non-admin users cannot misuse the
    feature. Starting with Kubernetes v1.34, this label has been updated to `resource.kubernetes.io/admin-access: "true"`.

    This feature gate has no effect unless you also enable the `DynamicResourceAllocation` feature gate.

`DRAConsumableCapacity`
:   Enables device sharing across multiple ResourceClaims or requests.

    Additionally, if a device supports sharing, its resource (capacity) can be managed through a defined sharing policy.

`DRADeviceBindingConditions`
:   Enables support for DeviceBindingConditions in the DRA related fields.
    This allows for thorough device readiness checks and attachment processes before Bind phase.

`DRADeviceTaints`
:   Enables support for
    [tainting devices and selectively tolerating those taints](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#device-taints-and-tolerations)
    when using dynamic resource allocation to manage devices.

    This feature gate has no effect unless you also enable the `DynamicResourceAllocation` feature gate.

`DRAExtendedResource`
:   Enables support for the [Extended Resource allocation by DRA](/docs/concepts/configuration/manage-resources-containers/#extended-resources-allocation-by-dra) feature.
    It makes it possible to specify an extended resource name in a DeviceClass.

    This feature gate has no effect unless the `DynamicResourceAllocation` feature gate is enabled.

`DRAPartitionableDevices`
:   Enables support for requesting [Partitionable Devices](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#partitionable-devices)
    for DRA. This lets drivers advertise multiple devices that maps to the same resources
    of a physical device.

    This feature gate has no effect unless you also enable the `DynamicResourceAllocation` feature gate.

`DRAPrioritizedList`
:   Enables support for the [Prioritized List](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#prioritized-list)
    feature. It makes it possible to specify a prioritized list of subrequests for requests in a ResourceClaim.

    This feature gate has no effect unless you also enable the `DynamicResourceAllocation` feature gate.

`DRAResourceClaimDeviceStatus`
:   Enables support the ResourceClaim.status.devices field and for setting this
    status from DRA drivers. It requires the `DynamicResourceAllocation` feature
    gate to be enabled.

`DRASchedulerFilterTimeout`
:   Enables aborting the per-node filter operation in the scheduler after a certain
    time (10 seconds by default, configurable in the DynamicResources scheduler
    plugin configuration).

`DynamicResourceAllocation`
:   Enables support for resources with custom parameters and a lifecycle
    that is independent of a Pod. Allocation of resources is handled
    by the Kubernetes scheduler based on "structured parameters".

`ElasticIndexedJob`
:   Enables Indexed Jobs to be scaled up or down by mutating both
    `spec.completions` and `spec.parallelism` together such that `spec.completions == spec.parallelism`.
    See docs on [elastic Indexed Jobs](/docs/concepts/workloads/controllers/job/#elastic-indexed-jobs)
    for more details.

`EnvFiles`
:   Support defining container's Environment Variable Values via File.
    See [Define Environment Variable Values Using An Init Container](/docs/tasks/inject-data-application/define-environment-variable-via-file/) for more details.

`EventedPLEG`
:   Enable support for the kubelet to receive container life cycle events from the
    [container runtime](/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.") via
    an extension to [CRI](/docs/concepts/architecture/cri "Protocol for communication between the kubelet and the local container runtime.").
    (PLEG is an abbreviation for “Pod lifecycle event generator”).
    For this feature to be useful, you also need to enable support for container lifecycle events
    in each container runtime running in your cluster. If the container runtime does not announce
    support for container lifecycle events then the kubelet automatically switches to the legacy
    generic PLEG mechanism, even if you have this feature gate enabled.

`ExecProbeTimeout`
:   Ensure kubelet respects exec probe timeouts.
    This feature gate exists in case any of your existing workloads depend on a
    now-corrected fault where Kubernetes ignored exec probe timeouts. See
    [readiness probes](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#configure-probes).

`ExternalServiceAccountTokenSigner`
:   Enable setting `--service-account-signing-endpoint` to make the kube-apiserver use [external signer](/docs/reference/access-authn-authz/service-accounts-admin/#external-serviceaccount-token-signing-and-key-management) for token signing and token verifying key management.

`GitRepoVolumeDriver`
:   This controls if the `gitRepo` volume plugin is supported or not.
    The `gitRepo` volume plugin is disabled by default starting v1.33 release.
    This provides a way for users to enable it.

`GracefulNodeShutdown`
:   Enables support for graceful shutdown in kubelet.
    During a system shutdown, kubelet will attempt to detect the shutdown event
    and gracefully terminate pods running on the node. See
    [Graceful Node Shutdown](/docs/concepts/architecture/nodes/#graceful-node-shutdown)
    for more details.

`GracefulNodeShutdownBasedOnPodPriority`
:   Enables the kubelet to check Pod priorities
    when shutting down a node gracefully.

`HonorPVReclaimPolicy`
:   Honor persistent volume reclaim policy when it is `Delete` irrespective of PV-PVC deletion ordering.
    For more details, check the
    [PersistentVolume deletion protection finalizer](/docs/concepts/storage/persistent-volumes/#persistentvolume-deletion-protection-finalizer)
    documentation.

`HostnameOverride`
:   Allows setting any FQDN as the pod's hostname.

`HPAConfigurableTolerance`
:   Enables setting a [tolerance threshold](/docs/tasks/run-application/horizontal-pod-autoscale/#tolerance)
    for HorizontalPodAutoscaler metrics.

`HPAScaleToZero`
:   Enables setting `minReplicas` to 0 for `HorizontalPodAutoscaler`
    resources when using custom or external metrics.

`ImageMaximumGCAge`
:   Enables the kubelet configuration field `imageMaximumGCAge`, allowing an administrator to specify the age after which an image will be garbage collected.

`ImageVolume`
:   Allow using the [`image`](/docs/concepts/storage/volumes/) volume source in a Pod.
    This volume source lets you mount a container image as a read-only volume.

`InformerResourceVersion`
:   Enables the check over the last synced resource version using the informer.

`InOrderInformers`
:   Force the informers to deliver watch stream events in order instead of out of order.

`InPlacePodVerticalScaling`
:   Enables in-place Pod vertical scaling.

`InPlacePodVerticalScalingAllocatedStatus`
:   Enables the `allocatedResources` field in the container status.
    This feature requires the `InPlacePodVerticalScaling` gate be enabled as well.

`InPlacePodVerticalScalingExclusiveCPUs`
:   Enable resource resizing for containers in Guaranteed pods with integer CPU requests.
    It applies only in nodes with `InPlacePodVerticalScaling` and `CPUManager` features enabled,
    and the CPUManager policy set to `static`.

`InPlacePodVerticalScalingExclusiveMemory`
:   Allow resource resize for containers in Guaranteed Pods when the memory manager policy is set to `"Static"`.
    Applies only to nodes with `InPlacePodVerticalScaling` and memory manager features enabled.

`InTreePluginPortworxUnregister`
:   Stops registering the Portworx in-tree plugin in kubelet
    and volume controllers.

`JobBackoffLimitPerIndex`
:   Allows specifying the maximal number of pod
    retries per index in Indexed jobs.

`JobManagedBy`
:   Allows to delegate reconciliation of a Job object to an external controller.

`JobPodReplacementPolicy`
:   Allows you to specify pod replacement for terminating pods in a [Job](/docs/concepts/workloads/controllers/job/)

`JobSuccessPolicy`
:   Allow users to specify when a Job can be declared as succeeded based on the set of succeeded pods.

`KMSv1`
:   Enables KMS v1 API for encryption at rest. See
    [Using a KMS Provider for data encryption](/docs/tasks/administer-cluster/kms-provider/)
    for more details.

`KubeletCgroupDriverFromCRI`
:   Enable detection of the kubelet cgroup driver
    configuration option from the [CRI](/docs/concepts/architecture/cri "Protocol for communication between the kubelet and the local container runtime.").
    This feature gate is now on for all clusters. However, it only works on nodes
    where there is a CRI container runtime that supports the `RuntimeConfig`
    CRI call. If the CRI supports this feature, the kubelet ignores the
    `cgroupDriver` configuration setting (or deprecated `--cgroup-driver` command
    line argument). If the container runtime
    doesn't support it, the kubelet falls back to using the driver configured using
    the `cgroupDriver` configuration setting.
    The kubelet will stop falling back to this configuration in Kubernetes 1.36.
    Thus, users must upgrade their CRI container runtime to a version that supports
    the `RuntimeConfig` CRI call by then. Admins can use the metric
    `kubelet_cri_losing_support` to see if there are any nodes in their cluster that
    will lose support in 1.36. The following CRI versions support this CRI call:

    * containerd: Support was added in v2.0.0
    * CRI-O: Support was added in v1.28.0

    See [Configuring a cgroup driver](/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/)
    for more details.

`KubeletCrashLoopBackOffMax`
:   Enables support for configurable per-node backoff maximums for restarting
    containers in the `CrashLoopBackOff` state.
    For more details, check the `crashLoopBackOff.maxContainerRestartPeriod` field in the
    [kubelet config file](/docs/reference/config-api/kubelet-config.v1beta1/).

`KubeletEnsureSecretPulledImages`
:   Ensure that pods requesting an image are authorized to access the image
    with the provided credentials when the image is already present on the node.
    See [Ensure Image Pull Credential Verification](/docs/concepts/containers/images/#ensureimagepullcredentialverification).

`KubeletFineGrainedAuthz`
:   Enable [fine-grained authorization](/docs/reference/access-authn-authz/kubelet-authn-authz/#fine-grained-authorization)
    for the kubelet's HTTP(s) API.

`KubeletInUserNamespace`
:   Enables support for running kubelet in a
    [user namespace](https://man7.org/linux/man-pages/man7/user_namespaces.7.html "A Linux kernel feature to emulate superuser privilege for unprivileged users.").
    See [Running Kubernetes Node Components as a Non-root User](/docs/tasks/administer-cluster/kubelet-in-userns/).

`KubeletPodResourcesDynamicResources`
:   Extend the kubelet's
    [pod resources monitoring gRPC API](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
    endpoints List and Get to include resources allocated in ResourceClaims
    via [Dynamic Resource Allocation](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/).

`KubeletPodResourcesGet`
:   Enable the `Get` gRPC endpoint on kubelet's for Pod resources.
    This API augments the [resource allocation reporting](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#monitoring-device-plugin-resources).

`KubeletPSI`
:   Enable kubelet to surface Pressure Stall Information (PSI) metrics in the Summary API and Prometheus metrics.

`KubeletSeparateDiskGC`
:   The split image filesystem feature enables kubelet to perform garbage collection
    of images (read-only layers) and/or containers (writeable layers) deployed on
    separate filesystems.

`KubeletServiceAccountTokenForCredentialProviders`
:   Enable kubelet to send the service account token bound to the pod for which the image is being pulled to the credential provider plugin.

`KubeletTracing`
:   Add support for distributed tracing in the kubelet.
    When enabled, kubelet CRI interface and authenticated http servers are instrumented to generate
    OpenTelemetry trace spans.
    See [Traces for Kubernetes System Components](/docs/concepts/cluster-administration/system-traces/) for more details.

`ListFromCacheSnapshot`
:   Enables the API server to generate snapshots for the watch cache store and using them to serve LIST requests.

`LoadBalancerIPMode`
:   Allows setting `ipMode` for Services where `type` is set to `LoadBalancer`.
    See [Specifying IPMode of load balancer status](/docs/concepts/services-networking/service/#load-balancer-ip-mode)
    for more information.

`LocalStorageCapacityIsolationFSQuotaMonitoring`
:   When `LocalStorageCapacityIsolation`
    is enabled for
    [local ephemeral storage](/docs/concepts/configuration/manage-resources-containers/),
    the backing filesystem for [emptyDir volumes](/docs/concepts/storage/volumes/#emptydir) supports project quotas,
    and `UserNamespacesSupport` is enabled,
    project quotas are used to monitor `emptyDir` volume storage consumption rather than using filesystem walk, ensuring better performance and accuracy.

`LogarithmicScaleDown`
:   Enable semi-random selection of pods to evict on controller scaledown
    based on logarithmic bucketing of pod timestamps.

`LoggingAlphaOptions`
:   Allow fine-tuning of experimental, alpha-quality logging options.

`LoggingBetaOptions`
:   Allow fine-tuning of experimental, beta-quality logging options.

`MatchLabelKeysInPodAffinity`
:   Enable the `matchLabelKeys` and `mismatchLabelKeys` fields for
    [pod (anti)affinity](/docs/concepts/scheduling-eviction/assign-pod-node/).

`MatchLabelKeysInPodTopologySpread`
:   Enable the `matchLabelKeys` field for
    [Pod topology spread constraints](/docs/concepts/scheduling-eviction/topology-spread-constraints/).

`MatchLabelKeysInPodTopologySpreadSelectorMerge`
:   Enable merging of selectors built from `matchLabelKeys` into `labelSelector` of
    [Pod topology spread constraints](/docs/concepts/scheduling-eviction/topology-spread-constraints/).
    This feature gate can be enabled when `matchLabelKeys` feature is enabled with the `MatchLabelKeysInPodTopologySpread` feature flag.

`MaxUnavailableStatefulSet`
:   Enables setting the `maxUnavailable` field for the
    [rolling update strategy](/docs/concepts/workloads/controllers/statefulset/#rolling-updates)
    of a StatefulSet. The field specifies the maximum number of Pods
    that can be unavailable during the update.

`MemoryManager`
:   Allows setting memory affinity for a container based on
    NUMA topology.

`MemoryQoS`
:   Enable memory protection and usage throttle on pod / container using
    cgroup v2 memory controller.

`MultiCIDRServiceAllocator`
:   Track IP address allocations for Service cluster IPs using IPAddress objects.

`MutableCSINodeAllocatableCount`
:   When this feature gate is enabled, the `.spec.drivers[*].allocatable.count` field of a CSINode becomes mutable, and a new field, `nodeAllocatableUpdatePeriodSeconds`, is available in the CSIDriver object. This allows periodic updates to a node's reported allocatable volume capacity, preventing stateful pods from becoming stuck due to outdated information that the kube-scheduler relies on.

`MutatingAdmissionPolicy`
:   Enable [MutatingAdmissionPolicy](/docs/reference/access-authn-authz/mutating-admission-policy/) support, which allows
    [CEL](/docs/reference/using-api/cel/) mutations to
    be applied during admission control.

    For Kubernetes v1.30 and v1.31, this feature gate existed but had no effect.

`NFTablesProxyMode`
:   Allow running kube-proxy in [nftables mode](/docs/reference/networking/virtual-ips/#proxy-mode-nftables).

`NodeInclusionPolicyInPodTopologySpread`
:   Enable using `nodeAffinityPolicy` and `nodeTaintsPolicy` in
    [Pod topology spread constraints](/docs/concepts/scheduling-eviction/topology-spread-constraints/)
    when calculating pod topology spread skew.

`NodeLogQuery`
:   Enables querying logs of node services using the `/logs` endpoint.

`NodeSwap`
:   Enable the kubelet to allocate swap memory for Kubernetes workloads on a node.
    Must be used with `KubeletConfiguration.failSwapOn` set to false.
    For more details, please see [swap memory](/docs/concepts/architecture/nodes/#swap-memory)

`NominatedNodeNameForExpectation`
:   When enabled, the kube-scheduler uses `.status.nominatedNodeName` to express where a
    Pod is going to be bound.
    External components can also write to `.status.nominatedNodeName` for a Pod to provide
    a suggested placement.

`OpenAPIEnums`
:   Enables populating "enum" fields of OpenAPI schemas in the
    spec returned from the API server.

`OrderedNamespaceDeletion`
:   While deleting namespace, the pods resources is going to be deleted before the rest of resources.

`PodAndContainerStatsFromCRI`
:   Configure the kubelet to gather container and pod stats from the CRI container runtime rather than gathering them from cAdvisor.
    As of 1.26, this also includes gathering metrics from CRI and emitting them over `/metrics/cadvisor` (rather than having cAdvisor emit them directly).

`PodCertificateRequest`
:   Enable PodCertificateRequest objects and podCertificate projected volume
    sources.

`PodDeletionCost`
:   Enable the [Pod Deletion Cost](/docs/concepts/workloads/controllers/replicaset/#pod-deletion-cost)
    feature which allows users to influence ReplicaSet downscaling order.

`PodIndexLabel`
:   Enables the Job controller and StatefulSet controller to add the pod index as a label when creating new pods. See [Job completion mode docs](/docs/concepts/workloads/controllers/job/#completion-mode) and [StatefulSet pod index label docs](/docs/concepts/workloads/controllers/statefulset/#pod-index-label) for more details.

`PodLevelResources`
:   Enable *Pod level resources*: the ability to specify resource requests and limits
    at the Pod level, rather than only for specific containers.

`PodLifecycleSleepAction`
:   Enables the `sleep` action in Container lifecycle hooks (`preStop` and `postStart`).

`PodLifecycleSleepActionAllowZero`
:   Enables setting zero value for the `sleep` action in
    [container lifecycle hooks](/docs/concepts/containers/container-lifecycle-hooks/).

`PodLogsQuerySplitStreams`
:   Enable fetching specific log streams (either stdout or stderr) from a container's log streams, using the Pod API.

`PodObservedGenerationTracking`
:   Enables the kubelet to set `observedGeneration` in the Pod `.status`, and enables other components to set `observedGeneration` in pod conditions.
    This feature allows reflecting the `.metadata.generation` of the Pod at the time that the overall status, or some specific condition, was being recorded.
    Storing it helps avoid risks associated with *lost updates*.

`PodReadyToStartContainersCondition`
:   Enable the kubelet to mark the [PodReadyToStartContainers](/docs/concepts/workloads/pods/pod-lifecycle/#pod-has-network) condition on pods.

    This feature gate was previously known as `PodHasNetworkCondition`, and the associated condition was
    named `PodHasNetwork`.

`PodSchedulingReadiness`
:   Enable setting `schedulingGates` field to control a Pod's [scheduling readiness](/docs/concepts/scheduling-eviction/pod-scheduling-readiness/).

`PodTopologyLabelsAdmission`
:   Enables the `PodTopologyLabels` admission plugin.
    See [Pod Topology Labels](docs/reference/access-authn-authz/admission-controllers#podtopologylabels)
    for details.

`PortForwardWebsockets`
:   Allow WebSocket streaming of the
    portforward sub-protocol (`port-forward`) from clients requesting
    version v2 (`v2.portforward.k8s.io`) of the sub-protocol.

`PreferSameTrafficDistribution`
:   Allows usage of the values `PreferSameZone` and `PreferSameNode` in
    the Service [`trafficDistribution`](/docs/reference/networking/virtual-ips/#traffic-distribution)
    field.

`PreventStaticPodAPIReferences`
:   Denies Pod admission if static Pods reference other API objects.

`ProcMountType`
:   Enables control over the type proc mounts for containers
    by setting the `procMount` field of a Pod's `securityContext`.

`QOSReserved`
:   Allows resource reservations at the QoS level preventing pods
    at lower QoS levels from bursting into resources requested at higher QoS levels
    (memory only for now).

`RecoverVolumeExpansionFailure`
:   Enables users to edit their PVCs to smaller
    sizes so as they can recover from previously issued volume expansion failures.
    See [Recovering from Failure when Expanding Volumes](/docs/concepts/storage/persistent-volumes/#recovering-from-failure-when-expanding-volumes)
    for more details.

`RecursiveReadOnlyMounts`
:   Enables support for recursive read-only mounts.
    For more details, see [read-only mounts](/docs/concepts/storage/volumes/#read-only-mounts).

`ReduceDefaultCrashLoopBackOffDecay`
:   Enabled reduction of both the initial delay and the maximum delay accrued
    between container restarts for a node for containers in `CrashLoopBackOff`
    across the cluster to `1s` initial delay and `60s` maximum delay.

`RelaxedDNSSearchValidation`
:   Relax the server side validation for the DNS search string
    (`.spec.dnsConfig.searches`) for containers. For example,
    with this gate enabled, it is okay to include the `_` character
    in the DNS name search string.

`RelaxedEnvironmentVariableValidation`
:   Allow almost all printable ASCII characters in environment variables.

`RelaxedServiceNameValidation`
:   Enables relaxed validation for Service object names, allowing the use of [RFC 1123 label names](/docs/concepts/overview/working-with-objects/names/#dns-label-names) instead of [RFC 1035 label names](/docs/concepts/overview/working-with-objects/names/#rfc-1035-label-names).

    This feature allows Service object names to start with a digit.

`ReloadKubeletServerCertificateFile`
:   Enable the kubelet TLS server to update its certificate if the specified certificate file are changed.

    This feature is useful when specifying `tlsCertFile` and `tlsPrivateKeyFile` in kubelet configuration.
    The feature gate has no effect for other cases such as using TLS bootstrap.

`RemoteRequestHeaderUID`
:   Enable the API server to accept UIDs (user IDs) via request header authentication.
    This will also make the `kube-apiserver`'s API aggregator add UIDs via standard headers when
    forwarding requests to the servers serving the aggregated API.

`ResilientWatchCacheInitialization`
:   Enables resilient watchcache initialization to avoid controlplane overload.

`ResourceHealthStatus`
:   Enable the `allocatedResourcesStatus` field within the `.status` for a Pod. The field
    reports additional details for each container in the Pod,
    with the health information for each device assigned to the Pod.

    This feature applies to devices managed by both [Device Plugins](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-and-unhealthy-devices) and [Dynamic Resource Allocation](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#device-health-monitoring). See [Device plugin and unhealthy devices](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-and-unhealthy-devices) for more details.

`RetryGenerateName`
:   Enables retrying of object creation when the
    [API server](/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API.")
    is expected to generate a [name](/docs/concepts/overview/working-with-objects/names/#names).

    When this feature is enabled, requests using `generateName` are retried automatically in case the
    control plane detects a name conflict with an existing object, up to a limit of 8 total attempts.

`RotateKubeletServerCertificate`
:   Enable the rotation of the server TLS certificate on the kubelet.
    See [kubelet configuration](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/#kubelet-configuration)
    for more details.

`RuntimeClassInImageCriApi`
:   Enables images to be pulled based on the [runtime class](/docs/concepts/containers/runtime-class/)
    of the pods that reference them.

`SchedulerAsyncAPICalls`
:   Change the kube-scheduler to make the entire scheduling cycle free of blocking requests to the Kubernetes API server.
    Instead, interact with the Kubernetes API using asynchronous code.

`SchedulerAsyncPreemption`
:   Enable running some expensive operations within the scheduler, associated with
    [preemption](/docs/concepts/scheduling-eviction/pod-priority-preemption/), asynchronously.
    Asynchronous processing of preemption improves overall Pod scheduling latency.

`SchedulerPopFromBackoffQ`
:   Improves scheduling queue behavior by popping pods from the backoffQ when the activeQ is empty.
    This allows to process potentially schedulable pods ASAP, eliminating a penalty effect of the backoff queue.

`SchedulerQueueingHints`
:   Enables scheduler [queueing hints](/docs/concepts/scheduling-eviction/scheduling-framework/#queueinghint),
    which benefits to reduce the useless requeuing.
    The scheduler retries scheduling pods if something changes in the cluster that could make the pod scheduled.
    Queueing hints are internal signals that allow the scheduler to filter the changes in the cluster
    that are relevant to the unscheduled pod, based on previous scheduling attempts.

`SELinuxChangePolicy`
:   Enables `spec.securityContext.seLinuxChangePolicy` field.
    This field can be used to opt-out from applying the SELinux label to the pod
    volumes using mount options. This is required when a single volume that supports
    mounting with SELinux mount option is shared between Pods that have different
    SELinux labels, such as a privileged and unprivileged Pods.

    Enabling the `SELinuxChangePolicy` feature gate requires the feature gate `SELinuxMountReadWriteOncePod` to
    be enabled.

`SELinuxMount`
:   Speeds up container startup by allowing kubelet to mount volumes
    for a Pod directly with the correct SELinux label instead of changing each file on the volumes
    recursively.
    It widens the performance improvements behind the `SELinuxMountReadWriteOncePod`
    feature gate by extending the implementation to all volumes.

    Enabling the `SELinuxMount` feature gate requires the feature gates `SELinuxMountReadWriteOncePod`
    and `SELinuxChangePolicy` to be enabled.

`SELinuxMountReadWriteOncePod`
:   Speeds up container startup by allowing kubelet to mount volumes
    for a Pod directly with the correct SELinux label instead of changing each file on the volumes
    recursively. The initial implementation focused on ReadWriteOncePod volumes.

`SeparateCacheWatchRPC`
:   Allows the API server watch cache to create a watch on a dedicated RPC.
    This prevents watch cache from being starved by other watches.

`SeparateTaintEvictionController`
:   Enables running the *taint based eviction* controller,
    that performs [Taint-based Evictions](/docs/concepts/scheduling-eviction/taint-and-toleration/#taint-based-evictions),
    as a standalone controller (separate from the *node lifecycle* controller).

`ServiceAcccountNodeAudienceRestriction`
:   This gate is used to restrict the audience for which the kubelet can request a service account token for.

`ServiceAccountTokenJTI`
:   Controls whether JTIs (UUIDs) are embedded into generated service account tokens,
    and whether these JTIs are recorded into the Kubernetes audit log for future requests made by these tokens.

`ServiceAccountTokenNodeBinding`
:   Controls whether the API server allows binding service account tokens to Node objects.

`ServiceAccountTokenNodeBindingValidation`
:   Controls whether the apiserver will validate a Node reference in service account tokens.

`ServiceAccountTokenPodNodeInfo`
:   Controls whether the apiserver embeds the node name and uid
    for the associated node when issuing service account tokens bound to Pod objects.

`ServiceTrafficDistribution`
:   Allows usage of the optional `spec.trafficDistribution` field in Services. The
    field offers a way to express preferences for how traffic is distributed to
    Service endpoints.

`SidecarContainers`
:   Allow setting the `restartPolicy` of an init container to
    `Always` so that the container becomes a sidecar container (restartable init containers).
    See [Sidecar containers and restartPolicy](/docs/concepts/workloads/pods/sidecar-containers/)
    for more details.

`SizeBasedListCostEstimate`
:   Enables APF to use size of objects for estimating request cost.

`SizeMemoryBackedVolumes`
:   Enable kubelets to determine the size limit for
    memory-backed volumes (mainly `emptyDir` volumes).

`StatefulSetAutoDeletePVC`
:   Allows the use of the optional `.spec.persistentVolumeClaimRetentionPolicy` field,
    providing control over the deletion of PVCs in a StatefulSet's lifecycle.
    See
    [PersistentVolumeClaim retention](/docs/concepts/workloads/controllers/statefulset/#persistentvolumeclaim-retention)
    for more details.

`StatefulSetStartOrdinal`
:   Allow configuration of the start ordinal in a
    StatefulSet. See
    [Start ordinal](/docs/concepts/workloads/controllers/statefulset/#start-ordinal)
    for more details.

`StorageCapacityScoring`
:   The feature gate `VolumeCapacityPriority` was used in v1.32 to support storage that are
    statically provisioned. Starting from v1.33, the new feature gate `StorageCapacityScoring`
    replaces the old `VolumeCapacityPriority` gate with added support to dynamically provisioned storage.
    When `StorageCapacityScoring` is enabled, the VolumeBinding plugin in the kube-scheduler is extended
    to score Nodes based on the storage capacity on each of them.
    This feature is applicable to CSI volumes that supported [Storage Capacity](/docs/concepts/storage/storage-capacity/),
    including local storage backed by a CSI driver.

`StorageNamespaceIndex`
:   Enables a namespace indexer for namespace scoped resources
    in API server cache to accelerate list operations.

`StorageVersionAPI`
:   Enable the
    [storage version API](/docs/reference/generated/kubernetes-api/v1.34/#storageversion-v1alpha1-internal-apiserver-k8s-io).

`StorageVersionHash`
:   Allow API servers to expose the storage version hash in the
    discovery.

`StorageVersionMigrator`
:   Enables storage version migration. See [Migrate Kubernetes Objects Using Storage Version Migration](/docs/tasks/manage-kubernetes-objects/storage-version-migration/) for more details.

`StreamingCollectionEncodingToJSON`
:   Allow the API server JSON encoder to encode collections item by item, instead of all at once.

`StreamingCollectionEncodingToProtobuf`
:   Allow the API server Protobuf encoder to encode collections item by item, instead of all at once.

`StrictCostEnforcementForVAP`
:   Apply strict CEL cost validation for ValidatingAdmissionPolicies.

`StrictCostEnforcementForWebhooks`
:   Apply strict CEL cost validation for `matchConditions` within
    admission webhooks.

`StrictIPCIDRValidation`
:   Use stricter validation for fields containing IP addresses and CIDR values.

    In particular, with this feature gate enabled, octets within IPv4 addresses are
    not allowed to have any leading `0`s, and IPv4-mapped IPv6 values (e.g.
    `::ffff:192.168.0.1`) are forbidden. These sorts of values can potentially cause
    security problems when different components interpret the same string as
    referring to different IP addresses (as in CVE-2021-29923).

    This tightening applies only to fields in build-in API kinds, and not to
    custom resource kinds, values in Kubernetes configuration files, or
    command-line arguments.

`StructuredAuthenticationConfiguration`
:   Enable [structured authentication configuration](/docs/reference/access-authn-authz/authentication/#configuring-the-api-server)
    for the API server.

`StructuredAuthenticationConfigurationEgressSelector`
:   Enables Egress Selector in Structured Authentication Configuration.

`StructuredAuthorizationConfiguration`
:   Enable structured authorization configuration, so that cluster administrators
    can specify more than one [authorization webhook](/docs/reference/access-authn-authz/webhook/)
    in the API server handler chain.

`SupplementalGroupsPolicy`
:   Enables support for fine-grained SupplementalGroups control.
    For more details, see [Configure fine-grained SupplementalGroups control for a Pod](/content/en/docs/tasks/configure-pod-container/security-context/#supplementalgroupspolicy).

`SystemdWatchdog`
:   Allow using systemd watchdog to monitor the health status of kubelet.
    See [Kubelet Systemd Watchdog](/docs/reference/node/systemd-watchdog/)
    for more details.

`TokenRequestServiceAccountUIDValidation`
:   This is used to ensure that the UID provided in the TokenRequest matches
    the UID of the ServiceAccount for which the token is being requested.
    It helps prevent misuse of the TokenRequest API by ensuring that
    tokens are only issued for the correct ServiceAccount.

`TopologyAwareHints`
:   Enables topology aware routing based on topology hints
    in EndpointSlices. See [Topology Aware
    Hints](/docs/concepts/services-networking/topology-aware-routing/) for more
    details.

`TopologyManagerPolicyAlphaOptions`
:   Allow fine-tuning of topology manager policies,
    experimental, Alpha-quality options.
    This feature gate guards *a group* of topology manager options whose quality level is alpha.
    This feature gate will never graduate to beta or stable.

`TopologyManagerPolicyBetaOptions`
:   Allow fine-tuning of topology manager policies,
    experimental, Beta-quality options.
    This feature gate guards *a group* of topology manager options whose quality level is beta.
    This feature gate will never graduate to stable.

`TopologyManagerPolicyOptions`
:   Enable [fine-tuning](/docs/tasks/administer-cluster/topology-manager/#topology-manager-policy-options)
    of topology manager policies.

`TranslateStreamCloseWebsocketRequests`
:   Allow WebSocket streaming of the
    remote command sub-protocol (`exec`, `cp`, `attach`) from clients requesting
    version 5 (v5) of the sub-protocol.

`UnauthenticatedHTTP2DOSMitigation`
:   Enables HTTP/2 Denial of Service (DoS) mitigations for unauthenticated clients.
    Kubernetes v1.28.0 through v1.28.2 do not include this feature gate.

`UnknownVersionInteroperabilityProxy`
:   Proxy resource requests to the correct peer kube-apiserver when
    multiple kube-apiservers exist at varied versions.
    See [Mixed version proxy](/docs/concepts/architecture/mixed-version-proxy/) for more information.

`UserNamespacesPodSecurityStandards`
:   Enable Pod Security Standards policies relaxation for pods
    that run with namespaces. You must set the value of this feature gate consistently across all nodes in
    your cluster, and you must also enable `UserNamespacesSupport` to use this feature.

`UserNamespacesSupport`
:   Enable user namespace support for Pods.

`VolumeAttributesClass`
:   Enable support for VolumeAttributesClasses.
    See [Volume Attributes Classes](/docs/concepts/storage/volume-attributes-classes/)
    for more information.

`WatchCacheInitializationPostStartHook`
:   Enables post-start-hook for watchcache initialization to be part of readyz (with timeout).

`WatchFromStorageWithoutResourceVersion`
:   Enables watches without `resourceVersion` to be served from storage.

`WatchList`
:   Enable support for [streaming initial state of objects in watch requests](/docs/reference/using-api/api-concepts/#streaming-lists).

`WatchListClient`
:   Allows an API client to request a stream of data rather than fetching a full list.
    This functionality is available in `client-go` and requires the
    [WatchList](/docs/reference/command-line-tools-reference/feature-gates/)
    feature to be enabled on the server.
    If the `WatchList` is not supported on the server, the client will seamlessly fall back to a standard list request.

`WindowsCPUAndMemoryAffinity`
:   Add CPU and Memory Affinity support to Windows nodes with [CPUManager](/docs/tasks/administer-cluster/cpu-management-policies/#windows-support),
    [MemoryManager](/docs/tasks/administer-cluster/memory-manager/#windows-support)
    and topology manager.

`WindowsGracefulNodeShutdown`
:   Enables support for windows node graceful shutdown in kubelet.
    During a system shutdown, kubelet will attempt to detect the shutdown event
    and gracefully terminate pods running on the node. See
    [Graceful Node Shutdown](/docs/concepts/architecture/nodes/#graceful-node-shutdown)
    for more details.

`WindowsHostNetwork`
:   Enables support for joining Windows containers to a hosts' network namespace.

`WinDSR`
:   Allows kube-proxy to create DSR loadbalancers for Windows.

`WinOverlay`
:   Allows kube-proxy to run in overlay mode for Windows.

## What's next

* The [deprecation policy](/docs/reference/using-api/deprecation-policy/) for Kubernetes explains
  the project's approach to removing features and components.
* Since Kubernetes 1.24, new beta APIs are not enabled by default. When enabling a beta
  feature, you will also need to enable any associated API resources.
  For example, to enable a particular resource like
  `storage.k8s.io/v1beta1/csistoragecapacities`, set `--runtime-config=storage.k8s.io/v1beta1/csistoragecapacities`.
  See [API Versioning](/docs/reference/using-api/#api-versioning) for more details on the command line flags.
* See [Configure Feature Gates](/docs/tasks/administer-cluster/configure-feature-gates/)
  for step-by-step guidance on enabling feature gates.

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
