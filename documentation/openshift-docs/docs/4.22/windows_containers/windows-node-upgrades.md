You can ensure your Windows nodes have the latest updates by updating the Windows Machine Config Operator (WMCO).

You can update the WMCO in any of the following scenarios:

- Within the current version. for example, from \<10.y.z\> to \<10.y.z+1\>.

- To a new, contiguous version. For example, from \<10.y\> to \<10.y+1\>.

- From an EUS version to another EUS version by using a Control Plane Only update. For example, from \<10.y\> to \<10.y+2\>.

# Windows Machine Config Operator updates

When a new version of the Windows Machine Config Operator (WMCO) is released that is compatible with the current cluster version, the Operator is updated based on the update channel and subscription approval strategy it was installed with when using the Operator Lifecycle Manager (OLM). The WMCO update results in the Kubernetes components in the Windows machine being updated.

> [!NOTE]
> If you are updating to a new version of the WMCO and want to use cluster monitoring, you must have the `openshift.io/cluster-monitoring=true` label present in the WMCO namespace. If you add the label to a pre-existing WMCO namespace, and there are already Windows nodes configured, restart the WMCO pod to allow monitoring graphs to display.

For a non-disruptive update, the WMCO terminates the Windows machines configured by the previous version of the WMCO and recreates them using the current version. This is done by deleting the `Machine` object, which results in the drain and deletion of the Windows node. To facilitate an update, the WMCO adds a version annotation to all the configured nodes. During an update, a mismatch in version annotation results in the deletion and recreation of a Windows machine. To have minimal service disruptions during an update, the WMCO only updates one Windows machine at a time.

After the update, it is recommended that you set the `spec.os.name.windows` parameter in your workload pods. The WMCO uses this field to authoritatively identify the pod operating system for validation and is used to enforce Windows-specific pod security context constraints (SCCs).

> [!IMPORTANT]
> The WMCO is only responsible for updating Kubernetes components, not for Windows operating system updates. You provide the Windows image when creating the VMs; therefore, you are responsible for providing an updated image. You can provide an updated Windows image by changing the image configuration in the `MachineSet` spec.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Updating installed Operators](../operators/admin/olm-upgrading-operators.xml#olm-upgrading-operators).

</div>

# Windows Machine Config Operator Control Plane Only update

OpenShift Container Platform and Windows Machine Config Operator (WMCO) support updating from one EUS version to another EUS version of OpenShift Container Platform, in a process called a **Control Plane Only** update. After upgrading the cluster, the Windows nodes are updated from the starting EUS version to the new EUS version while keeping the Windows workloads in a healthy state with no disruptions.

> [!IMPORTANT]
> This update was previously known as an **EUS-to-EUS** update and is now referred to as a **Control Plane Only** update. These updates are only viable between **even-numbered minor versions** of OpenShift Container Platform.

## WMCO Control Plane Only update by using the web console

You can use the OpenShift Container Platform web console to perform a Control Plane Only update of the Windows Machine Config Operator (WMCO).

<div>

<div class="title">

Prerequisites

</div>

- The cluster must be running on a supported EUS version of OpenShift Container Platform.

- All Windows nodes must be in a healthy state.

- All Windows nodes must be running on the same version of the WMCO.

- All the of the prerequisites of the Control Plane Only update are met, as described in "Performing a Control Plane Only update."

</div>

<div>

<div class="title">

Procedure

</div>

1.  Uninstall WMCO operator by using the following the steps:

    > [!IMPORTANT]
    > Delete the Operator only. Do not delete the Windows namespace or any Windows workloads.

    1.  Log in to the OpenShift Container Platform web console.

    2.  Navigate to **Ecosystem** → **Software Catalog**.

    3.  Use the **Filter by keyword** box to search for `Red Hat Windows Machine Config Operator`.

    4.  Click the **Red Hat Windows Machine Config Operator** tile. The Operator tile indicates it is installed.

    5.  In the **Windows Machine Config Operator** descriptor page, click **Uninstall**.

2.  Update OpenShift Container Platform by following the steps in "Performing a Control Plane Only update."

3.  Install the new WMCO version by following the steps in "Installing the Windows Machine Config Operator using the web console."

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Performing a Control Plane Only update](../updating/updating_a_cluster/control-plane-only-update.xml#control-plane-only-update)

- [Installing the Windows Machine Config Operator using the web console](../windows_containers/enabling-windows-container-workloads.xml#installing-wmco-using-web-console_enabling-windows-container-workloads)

</div>

## WMCO Control Plane Only update by using the CLI

You can use the OpenShift CLI (`oc`) to perform a Control Plane Only update of the Windows Machine Config Operator (WMCO).

<div>

<div class="title">

Prerequisites

</div>

- The cluster must be running on a supported EUS version of OpenShift Container Platform.

- All Windows nodes must be in a healthy state.

- All Windows nodes must be running on the same version of the WMCO.

- All the of the prerequisites of the Control Plane Only update are met, as described in "Performing a Control Plane Only update."

</div>

<div>

<div class="title">

Procedure

</div>

1.  Uninstall the WMCO Operator from the cluster by following the steps in "Deleting Operators from a cluster using the CLI."

    > [!IMPORTANT]
    > Delete the Operator only. Do not delete the Windows namespace or any Windows workloads.

2.  Update OpenShift Container Platform by following the steps in "Performing a Control Plane Only update."

3.  Install the new WMCO version by following the steps in "Installing the Windows Machine Config Operator using the CLI."

</div>

<div>

<div class="title">

Verification

</div>

- On the Verify that the **Status** shows **Succeeded** to confirm successful installation of the WMCO.

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Deleting Operators from a cluster using the CLI](../operators/admin/olm-deleting-operators-from-cluster.xml#olm-deleting-operator-from-a-cluster-using-cli_olm-deleting-operators-from-a-cluster)

- [Performing a Control Plane Only update](../updating/updating_a_cluster/control-plane-only-update.xml#control-plane-only-update)

- [Installing the Windows Machine Config Operator using the CLI](../windows_containers/enabling-windows-container-workloads.xml#installing-wmco-using-cli_enabling-windows-container-workloads)

</div>
