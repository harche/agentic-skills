# About dynamic provisioning

The `StorageClass` resource object describes and classifies storage that can be requested, as well as provides a means for passing parameters for dynamically provisioned storage on demand. `StorageClass` objects can also serve as a management mechanism for controlling different levels of storage and access to the storage. Cluster Administrators (`cluster-admin`) or Storage Administrators (`storage-admin`) define and create the `StorageClass` objects that users can request without needing any detailed knowledge about the underlying storage volume sources.

The OpenShift Container Platform persistent volume framework enables this functionality and allows administrators to provision a cluster with persistent storage. The framework also gives users a way to request those resources without having any knowledge of the underlying infrastructure.

Many storage types are available for use as persistent volumes in OpenShift Container Platform. While all of them can be statically provisioned by an administrator, some types of storage are created dynamically using the built-in provider and plugin APIs.

# Available dynamic provisioning plugins

OpenShift Container Platform provides the following provisioner plugins, which have generic implementations for dynamic provisioning that use the cluster’s configured provider’s API to create new storage resources:

| Storage type | Provisioner plugin name | Notes |
|----|----|----|
| Red Hat OpenStack Platform (RHOSP) Cinder | `kubernetes.io/cinder` |  |
| RHOSP Manila Container Storage Interface (CSI) | `manila.csi.openstack.org` | Once installed, the OpenStack Manila CSI Driver Operator and ManilaDriver automatically create the required storage classes for all available Manila share types needed for dynamic provisioning. |
| Amazon Elastic Block Store (Amazon EBS) | `ebs.csi.aws.com` | For dynamic provisioning when using multiple clusters in different zones, tag each node with `Key=kubernetes.io/cluster/<cluster_name>,Value=<cluster_id>` where `<cluster_name>` and `<cluster_id>` are unique per cluster. |
| Azure Disk | `kubernetes.io/azure-disk` |  |
| Azure File | `kubernetes.io/azure-file` | The `persistent-volume-binder` service account requires permissions to create and get secrets to store the Azure storage account and keys. |
| GCE Persistent Disk (gcePD) | `kubernetes.io/gce-pd` | In multi-zone configurations, it is advisable to run one OpenShift Container Platform cluster per GCE project to avoid PVs from being created in zones where no node in the current cluster exists. |
| IBM Power® Virtual Server Block | `powervs.csi.ibm.com` | After installation, the IBM Power® Virtual Server Block CSI Driver Operator and IBM Power® Virtual Server Block CSI Driver automatically create the required storage classes for dynamic provisioning. |
| [VMware vSphere](https://www.vmware.com/support/vsphere.html) | `kubernetes.io/vsphere-volume` |  |

> [!IMPORTANT]
> Any chosen provisioner plugin also requires configuration for the relevant cloud, host, or third-party provider as per the relevant documentation.

# Defining a storage class

`StorageClass` objects are currently a globally scoped object and must be created by `cluster-admin` or `storage-admin` users.

> [!IMPORTANT]
> The Cluster Storage Operator might install a default storage class depending on the platform in use. This storage class is owned and controlled by the Operator. It cannot be deleted or modified beyond defining annotations and labels. If different behavior is desired, you must define a custom storage class.

The following sections describe the basic definition for a `StorageClass` object and specific examples for each of the supported plugin types.

## Basic StorageClass object definition

The following resource shows the parameters and default values that you use to configure a storage class. This example uses the AWS ElasticBlockStore (EBS) object definition.

<div class="formalpara">

<div class="title">

Sample `StorageClass` definition

</div>

``` yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: <storage-class-name>
  annotations:
    storageclass.kubernetes.io/is-default-class: 'true'
    ...
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp3
...
```

</div>

- (required) The API object type.

- (required) The current apiVersion.

- (required) The name of the storage class.

- (optional) Annotations for the storage class.

- (required) The type of provisioner associated with this storage class.

- (optional) The parameters required for the specific provisioner, this will change from plug-in to plug-in.

## Storage class annotations

To set a storage class as the cluster-wide default, add the following annotation to your storage class metadata:

``` yaml
storageclass.kubernetes.io/is-default-class: "true"
```

For example:

``` yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
...
```

This enables any persistent volume claim (PVC) that does not specify a specific storage class to automatically be provisioned through the default storage class. However, your cluster can have more than one storage class, but only one of them can be the default storage class.

> [!NOTE]
> The beta annotation `storageclass.beta.kubernetes.io/is-default-class` is still working; however, it will be removed in a future release.

To set a storage class description, add the following annotation to your storage class metadata:

``` yaml
kubernetes.io/description: My Storage Class Description
```

For example:

``` yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  annotations:
    kubernetes.io/description: My Storage Class Description
...
```

## RHOSP Cinder object definition

<div class="formalpara">

<div class="title">

cinder-storageclass.yaml

</div>

``` yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: <storage-class-name>
provisioner: kubernetes.io/cinder
parameters:
  type: fast
  availability: nova
  fsType: ext4
```

</div>

- Name of the storage class. The persistent volume claim uses this storage class for provisioning the associated persistent volumes.

- Volume type created in Cinder. Default is empty.

- Availability Zone. If not specified, volumes are generally round-robined across all active zones where the OpenShift Container Platform cluster has a node.

- File system that is created on dynamically provisioned volumes. This value is copied to the `fsType` field of dynamically provisioned persistent volumes and the file system is created when the volume is mounted for the first time. The default value is `ext4`.

## RHOSP Manila Container Storage Interface (CSI) object definition

Once installed, the OpenStack Manila CSI Driver Operator and ManilaDriver automatically create the required storage classes for all available Manila share types needed for dynamic provisioning.

## AWS Elastic Block Store (EBS) object definition

<div class="formalpara">

<div class="title">

aws-ebs-storageclass.yaml

</div>

``` yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: <storage-class-name>
provisioner: ebs.csi.aws.com
parameters:
  type: io1
  iopsPerGB: "10"
  encrypted: "true"
  kmsKeyId: keyvalue
  fsType: ext4
```

</div>

- (required) Name of the storage class. The persistent volume claim uses this storage class for provisioning the associated persistent volumes.

- (required) Select from `io1`, `gp3`, `sc1`, `st1`. The default is `gp3`. See the [AWS documentation](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) for valid Amazon Resource Name (ARN) values.

- Optional: Only for **io1** volumes. I/O operations per second per GiB. The AWS volume plugin multiplies this with the size of the requested volume to compute IOPS of the volume. The value cap is 20,000 IOPS, which is the maximum supported by AWS. See the [AWS documentation](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) for further details.

- Optional: Denotes whether to encrypt the EBS volume. Valid values are `true` or `false`.

- Optional: The full ARN of the key to use when encrypting the volume. If none is supplied, but `encypted` is set to `true`, then AWS generates a key. See the [AWS documentation](http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) for a valid ARN value.

- Optional: File system that is created on dynamically provisioned volumes. This value is copied to the `fsType` field of dynamically provisioned persistent volumes and the file system is created when the volume is mounted for the first time. The default value is `ext4`.

## Azure Disk object definition

<div class="formalpara">

<div class="title">

azure-advanced-disk-storageclass.yaml

</div>

``` yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: <storage-class-name>
provisioner: kubernetes.io/azure-disk
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
parameters:
  kind: Managed
  storageaccounttype: Premium_LRS
reclaimPolicy: Delete
```

</div>

- Name of the storage class. The persistent volume claim uses this storage class for provisioning the associated persistent volumes.

- Using `WaitForFirstConsumer` is strongly recommended. This provisions the volume while allowing enough storage to schedule the pod on a free worker node from an available zone.

- Possible values are `Shared` (default), `Managed`, and `Dedicated`.

  > [!IMPORTANT]
  > Red Hat only supports the use of `kind: Managed` in the storage class.
  >
  > With `Shared` and `Dedicated`, Azure creates unmanaged disks, while OpenShift Container Platform creates a managed disk for machine OS (root) disks. But because Azure Disk does not allow the use of both managed and unmanaged disks on a node, unmanaged disks created with `Shared` or `Dedicated` cannot be attached to OpenShift Container Platform nodes.

- Azure storage account SKU tier. Default is empty. Note that Premium VMs can attach both `Standard_LRS` and `Premium_LRS` disks, Standard VMs can only attach `Standard_LRS` disks, Managed VMs can only attach managed disks, and unmanaged VMs can only attach unmanaged disks.

  1.  If `kind` is set to `Shared`, Azure creates all unmanaged disks in a few shared storage accounts in the same resource group as the cluster.

  2.  If `kind` is set to `Managed`, Azure creates new managed disks.

  3.  If `kind` is set to `Dedicated` and a `storageAccount` is specified, Azure uses the specified storage account for the new unmanaged disk in the same resource group as the cluster. For this to work:

      - The specified storage account must be in the same region.

      - Azure Cloud Provider must have write access to the storage account.

  4.  If `kind` is set to `Dedicated` and a `storageAccount` is not specified, Azure creates a new dedicated storage account for the new unmanaged disk in the same resource group as the cluster.

## Azure File object definition

The Azure File storage class uses secrets to store the Azure storage account name and the storage account key that are required to create an Azure Files share. These permissions are created as part of the following procedure.

<div>

<div class="title">

Procedure

</div>

1.  Define a `ClusterRole` object that allows access to create and view secrets:

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
    #  name: system:azure-cloud-provider
      name: <persistent-volume-binder-role>
    rules:
    - apiGroups: ['']
      resources: ['secrets']
      verbs:     ['get','create']
    ```

    - The name of the cluster role to view and create secrets.

2.  Add the cluster role to the service account:

    ``` terminal
    $ oc adm policy add-cluster-role-to-user <persistent-volume-binder-role> system:serviceaccount:kube-system:persistent-volume-binder
    ```

3.  Create the Azure File `StorageClass` object:

    ``` yaml
    kind: StorageClass
    apiVersion: storage.k8s.io/v1
    metadata:
      name: <azure-file>
    provisioner: kubernetes.io/azure-file
    parameters:
      location: eastus
      skuName: Standard_LRS
      storageAccount: <storage-account>
    reclaimPolicy: Delete
    volumeBindingMode: Immediate
    ```

    - Name of the storage class. The persistent volume claim uses this storage class for provisioning the associated persistent volumes.

    - Location of the Azure storage account, such as `eastus`. Default is empty, meaning that a new Azure storage account will be created in the OpenShift Container Platform cluster’s location.

    - SKU tier of the Azure storage account, such as `Standard_LRS`. Default is empty, meaning that a new Azure storage account will be created with the `Standard_LRS` SKU.

    - Name of the Azure storage account. If a storage account is provided, then `skuName` and `location` are ignored. If no storage account is provided, then the storage class searches for any storage account that is associated with the resource group for any accounts that match the defined `skuName` and `location`.

</div>

### Considerations when using Azure File

The following file system features are not supported by the default Azure File storage class:

- Symlinks

- Hard links

- Extended attributes

- Sparse files

- Named pipes

Additionally, the owner user identifier (UID) of the Azure File mounted directory is different from the process UID of the container. The `uid` mount option can be specified in the `StorageClass` object to define a specific user identifier to use for the mounted directory.

The following `StorageClass` object demonstrates modifying the user and group identifier, along with enabling symlinks for the mounted directory.

``` yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: azure-file
mountOptions:
  - uid=1500
  - gid=1500
  - mfsymlinks
provisioner: kubernetes.io/azure-file
parameters:
  location: eastus
  skuName: Standard_LRS
reclaimPolicy: Delete
volumeBindingMode: Immediate
```

- Specifies the user identifier to use for the mounted directory.

- Specifies the group identifier to use for the mounted directory.

- Enables symlinks.

## GCE PersistentDisk (gcePD) object definition

<div class="formalpara">

<div class="title">

gce-pd-storageclass.yaml

</div>

``` yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: <storage-class-name>
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-ssd
  replication-type: none
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
reclaimPolicy: Delete
```

</div>

- Name of the storage class. The persistent volume claim uses this storage class for provisioning the associated persistent volumes.

- Select `pd-ssd`, `pd-standard`, or `hyperdisk-balanced`. The default is `pd-ssd`.

## VMware vSphere object definition

<div class="formalpara">

<div class="title">

vsphere-storageclass.yaml

</div>

``` yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: <storage-class-name>
provisioner: csi.vsphere.vmware.com
```

</div>

- Name of the storage class. The persistent volume claim uses this storage class for provisioning the associated persistent volumes.

- For more information about using VMware vSphere CSI with OpenShift Container Platform, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/storage/volumes/#vsphere-csi-migration).

# Changing the default storage class

Use the following procedure to change the default storage class.

For example, if you have two defined storage classes, `gp3` and `standard`, and you want to change the default storage class from `gp3` to `standard`.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster with cluster-admin privileges.

</div>

<div class="formalpara">

<div class="title">

Procedure

</div>

To change the default storage class:

</div>

1.  List the storage classes:

    ``` terminal
    $ oc get storageclass
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                 TYPE
    gp3 (default)        ebs.csi.aws.com
    standard             ebs.csi.aws.com
    ```

    </div>

    - `(default)` indicates the default storage class.

2.  Make the desired storage class the default.

    For the desired storage class, set the `storageclass.kubernetes.io/is-default-class` annotation to `true` by running the following command:

    ``` terminal
    $ oc patch storageclass standard -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "true"}}}'
    ```

    > [!NOTE]
    > You can have multiple default storage classes for a short time. However, you should ensure that only one default storage class exists eventually.
    >
    > With multiple default storage classes present, any persistent volume claim (PVC) requesting the default storage class (`pvc.spec.storageClassName`=nil) gets the most recently created default storage class, regardless of the default status of that storage class, and the administrator receives an alert in the alerts dashboard that there are multiple default storage classes, `MultipleDefaultStorageClasses`.

3.  Remove the default storage class setting from the old default storage class.

    For the old default storage class, change the value of the `storageclass.kubernetes.io/is-default-class` annotation to `false` by running the following command:

    ``` terminal
    $ oc patch storageclass gp3 -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "false"}}}'
    ```

4.  Verify the changes:

    ``` terminal
    $ oc get storageclass
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                 TYPE
    gp3                  ebs.csi.aws.com
    standard (default)   ebs.csi.aws.com
    ```

    </div>
