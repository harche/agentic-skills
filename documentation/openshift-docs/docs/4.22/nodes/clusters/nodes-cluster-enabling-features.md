<div wrapper="1" role="_abstract">

As an administrator, you can use feature gates to enable features that are not part of the default set of features so that you can use these non-default features in your cluster.

</div>

# Understanding feature gates

<div wrapper="1" role="_abstract">

You can use the `FeatureGate` custom resource (CR) to enable specific feature sets so that you can use specific non-default features in your cluster.

</div>

A feature set is a collection of OpenShift Container Platform features that are not enabled by default.

You can activate the following feature set by using the `FeatureGate` CR:

- `TechPreviewNoUpgrade`. This feature set is a subset of the current Technology Preview features. This feature set allows you to enable these Technology Preview features on test clusters, where you can fully test them, while leaving the features disabled on production clusters.

  > [!WARNING]
  > Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. You should not enable this feature set on production clusters.

  The following Technology Preview features are enabled by this feature set:

  - `AdditionalRoutingCapabilities`

  - `AdminNetworkPolicy`

  - `AlibabaPlatform`

  - `AutomatedEtcdBackup`

  - `AWSClusterHostedDNS`

  - `AWSClusterHostedDNSInstall`

  - `AWSDedicatedHosts`

  - `AWSDualStackInstall`

  - `AWSServiceLBNetworkSecurityGroup`

  - `AzureClusterHostedDNSInstall`

  - `AzureDedicatedHosts`

  - `AzureDualStackInstall`

  - `AzureMultiDisk`

  - `AzureWorkloadIdentity`

  - `BootcNodeManagement`

  - `BootImageSkewEnforcement`

  - `BuildCSIVolumes`

  - `CBORServingAndStorage`

  - `ClientsPreferCBOR`

  - `ClusterAPIInstallIBMCloud`

  - `ClusterAPIMachineManagement`

  - `ClusterMonitoringConfig`

  - `ClusterVersionOperatorConfiguration`

  - `ConsolePluginContentSecurityPolicy`

  - `CPMSMachineNamePrefix`

  - `CRDCompatibilityRequirementOperator`

  - `DNSNameResolver`

  - `DualReplica`

  - `DyanmicServiceEndpointIBMCloud`

  - `EtcdBackendQuota`

  - `EventTTL`

  - `Example`

  - `ExternalOIDC`

  - `ExternalOIDCWithUIDAndExtraClaimMappings`

  - `GatewayAPI`

  - `GatewayAPIController`

  - `GCPClusterHostedDNS`

  - `GCPClusterHostedDNSInstall`

  - `GCPDualStackInstall`

  - `GCPCustomAPIEndpoints`

  - `GCPCustomAPIEndpointsInstall`

  - `HighlyAvailableArbiter`

  - `HyperShiftOnlyDynamicResourceAllocation`

  - `ImageModeStatusReporting`

  - `ImageStreamImportMode`

  - `ImageVolume`

  - `InsightsConfig`

  - `InsightsOnDemandDataGather`

  - `IrreconcilableMachineConfig`

  - `KMSEncryptionProvider`

  - `KMSv1`

  - `MachineAPIMigration`

  - `MachineConfigNodes`

  - `ManagedBootImages`

  - `ManagedBootImagesAWS`

  - `ManagedBootImagesAzure`

  - `ManagedBootImagesCPMS`

  - `ManagedBootImagesvSphere`

  - `MaxUnavailableStatefulSet`

  - `MetricsCollectionProfiles`

  - `MinimumKubeletVersion`

  - `MixedCPUsAllocation`

  - `MultiDiskSetup`

  - `MutableCSINodeAllocatableCount`

  - `MutatingAdmissionPolicy`

  - `NetworkDiagnosticsConfig`

  - `NetworkLiveMigration`

  - `NetworkSegmentation`

  - `NewOLM`

  - `NewOLMCatalogdAPIV1Metas`

  - `NewOLMOwnSingleNamespace`

  - `NewOLMPreflightPermissionChecks`

  - `NewOLMWebhookProviderOpenshiftServiceCA`

  - `NoRegistryClusterInstall`

  - `NutanixMultiSubnets`

  - `OnPremDNSRecords`

  - `OpenShiftPodSecurityAdmission`

  - `OSStreams`

  - `OVNObservability`

  - `PinnedImages`

  - `PreconfiguredUDNAddresses`

  - `ProcMountType`

  - `RouteAdvertisements`

  - `RouteExternalCertificate`

  - `SELinuxMount`

  - `ServiceAccountTokenNodeBinding`

  - `SignatureStores`

  - `SigstoreImageVerification`

  - `SigstoreImageVerificationPKI`

  - `StoragePerformantSecurityPolicy`

  - `TranslateStreamCloseWebsocketRequests`

  - `UpgradeStatus`

  - `UserNamespacesPodSecurityStandards`

  - `UserNamespacesSupport`

  - `VolumeAttributesClass`

  - `VolumeGroupSnapshot`

  - `VSphereConfigurableMaxAllowedBlockVolumesPerNode`

  - `VSphereHostVMGroupZonal`

  - `VSphereMixedNodeEnv`

  - `VSphereMultiDisk`

  - `VSphereMultiNetworks`

See the *Additional resources* sections for information on some of these features.

# Enabling feature sets at installation

<div wrapper="1" role="_abstract">

You can enable feature sets for all nodes in the cluster by editing the `install-config.yaml` file before you deploy the cluster. This allows you to use non-default features in your cluster.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You have an `install-config.yaml` file.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Use the `featureSet` parameter to specify the name of the feature set you want to enable, such as `TechPreviewNoUpgrade`:

    > [!WARNING]
    > Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. You should not enable this feature set on production clusters.

    <div class="formalpara">

    <div class="title">

    Sample `install-config.yaml` file with an enabled feature set

    </div>

    ``` yaml
    compute:
    - hyperthreading: Enabled
      name: worker
      platform:
        aws:
          rootVolume:
            iops: 2000
            size: 500
            type: io1
          metadataService:
            authentication: Optional
          type: c5.4xlarge
          zones:
          - us-west-2c
      replicas: 3
    featureSet: TechPreviewNoUpgrade
    ```

    </div>

2.  Save the file and reference it when using the installation program to deploy the cluster.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

You can verify that the feature gates are enabled by looking at the `kubelet.conf` file on a node after the nodes return to the ready state.

</div>

1.  From the **Administrator** perspective in the web console, navigate to **Compute** → **Nodes**.

2.  Select a node.

3.  In the **Node details** page, click **Terminal**.

4.  In the terminal window, change your root directory to `/host`:

    ``` terminal
    sh-4.2# chroot /host
    ```

5.  View the `kubelet.conf` file:

    ``` terminal
    sh-4.2# cat /etc/kubernetes/kubelet.conf
    ```

    <div class="formalpara">

    <div class="title">

    Sample output

    </div>

    ``` terminal
    # ...
    featureGates:
      InsightsOperatorPullingSCA: true,
      LegacyNodeRoleBehavior: false
    # ...
    ```

    </div>

    The features that are listed as `true` are enabled on your cluster.

    > [!NOTE]
    > The features listed vary depending upon the OpenShift Container Platform version.

# Enabling feature sets using the web console

<div wrapper="1" role="_abstract">

You can use the OpenShift Container Platform web console to enable feature sets for all of the nodes in a cluster by editing the `FeatureGate` custom resource (CR). Completing this task enables non-default features in your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, switch to the **Administration** → **Custom Resource Definitions** page.

2.  On the **Custom Resource Definitions** page, click **FeatureGate**.

3.  On the **Custom Resource Definition Details** page, click the **Instances** tab.

4.  Click the **cluster** feature gate, then click the **YAML** tab.

5.  Edit the **cluster** instance to add specific feature sets:

    > [!WARNING]
    > Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. You should not enable this feature set on production clusters.

    <div class="formalpara">

    <div class="title">

    Sample Feature Gate custom resource

    </div>

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: FeatureGate
    metadata:
      name: cluster
    # ...
    spec:
      featureSet: TechPreviewNoUpgrade
    ```

    </div>

    where:

    `metadata.name`
    Specifies the name of the `FeatureGate` CR. You must specify `cluster` for the name.

    `spec.featureSet`
    Specifies the feature set that you want to enable:

    - `TechPreviewNoUpgrade` enables specific Technology Preview features.

    After you save the changes, new machine configs are created, the machine config pools are updated, and scheduling on each node is disabled while the change is being applied.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

You can verify that the feature gates are enabled by looking at the `kubelet.conf` file on a node after the nodes return to the ready state.

</div>

1.  From the **Administrator** perspective in the web console, navigate to **Compute** → **Nodes**.

2.  Select a node.

3.  In the **Node details** page, click **Terminal**.

4.  In the terminal window, change your root directory to `/host`:

    ``` terminal
    sh-4.2# chroot /host
    ```

5.  View the `kubelet.conf` file:

    ``` terminal
    sh-4.2# cat /etc/kubernetes/kubelet.conf
    ```

    <div class="formalpara">

    <div class="title">

    Sample output

    </div>

    ``` terminal
    # ...
    featureGates:
      InsightsOperatorPullingSCA: true,
      LegacyNodeRoleBehavior: false
    # ...
    ```

    </div>

    The features that are listed as `true` are enabled on your cluster.

    > [!NOTE]
    > The features listed vary depending upon the OpenShift Container Platform version.

# Enabling feature sets using the CLI

<div wrapper="1" role="_abstract">

You can use the OpenShift CLI (`oc`) to enable feature sets for all of the nodes in a cluster by editing the `FeatureGate` custom resource (CR). Completing this task enables non-default features in your cluster.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- Edit the `FeatureGate` CR named `cluster`:

  ``` terminal
  $ oc edit featuregate cluster
  ```

  > [!WARNING]
  > Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. You should not enable this feature set on production clusters.

  <div class="formalpara">

  <div class="title">

  Sample FeatureGate custom resource

  </div>

  ``` yaml
  apiVersion: config.openshift.io/v1
  kind: FeatureGate
  metadata:
    name: cluster
  # ...
  spec:
    featureSet: TechPreviewNoUpgrade
  ```

  </div>

  where:

  `metadata.name`
  Specifies the name of the `FeatureGate` CR. This must be `cluster`.

  `spec.featureSet`
  Specifies the feature set that you want to enable:

  - `TechPreviewNoUpgrade` enables specific Technology Preview features.

  After you save the changes, new machine configs are created, the machine config pools are updated, and scheduling on each node is disabled while the change is being applied.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

You can verify that the feature gates are enabled by looking at the `kubelet.conf` file on a node after the nodes return to the ready state.

</div>

1.  From the **Administrator** perspective in the web console, navigate to **Compute** → **Nodes**.

2.  Select a node.

3.  In the **Node details** page, click **Terminal**.

4.  In the terminal window, change your root directory to `/host`:

    ``` terminal
    sh-4.2# chroot /host
    ```

5.  View the `kubelet.conf` file:

    ``` terminal
    sh-4.2# cat /etc/kubernetes/kubelet.conf
    ```

    <div class="formalpara">

    <div class="title">

    Sample output

    </div>

    ``` terminal
    # ...
    featureGates:
      InsightsOperatorPullingSCA: true,
      LegacyNodeRoleBehavior: false
    # ...
    ```

    </div>

    The features that are listed as `true` are enabled on your cluster.

    > [!NOTE]
    > The features listed vary depending upon the OpenShift Container Platform version.

# Additional resources

- [Shared Resources CSI Driver and Build CSI Volumes in OpenShift Builds](../../cicd/builds/running-entitled-builds.xml#builds-running-entitled-builds-with-sharedsecret-objects_running-entitled-builds)

- [CSI inline ephemeral volumes](../../storage/container_storage_interface/ephemeral-storage-csi-inline.xml#ephemeral-storage-csi-inline)

- [Managing machines with the Cluster API](../../machine_management/cluster_api_machine_management/cluster-api-about.xml#cluster-api-about)

- [Disabling the Insights Operator gather operations](../../support/remote_health_monitoring/using-insights-operator.xml#disabling-insights-operator-gather_using-insights-operator)

- [Enabling the Insights Operator gather operations](../../support/remote_health_monitoring/using-insights-operator.xml#enabling-insights-operator-gather_using-insights-operator)

- [Running an Insights Operator gather operation](../../support/remote_health_monitoring/using-insights-operator.xml#running-insights-operator-gather_using-insights-operator)

- [Managing the default storage class](../../storage/container_storage_interface/persistent-storage-csi-sc-manage.xml#persistent-storage-csi-sc-manage)

- [Pod security admission enforcement](../../authentication/understanding-and-managing-pod-security-admission.xml#understanding-and-managing-pod-security-admission)
