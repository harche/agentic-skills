<div wrapper="1" role="_abstract">

Placing a node into maintenance mode marks the node as unschedulable, and removes all the VMs and pods from it. Nodes can be placed into maintenance mode by using the `oc adm` utility or `NodeMaintenance` custom resources (CRs).

</div>

> [!IMPORTANT]
> Virtual machines (VMs) must have a persistent volume claim (PVC) with a shared `ReadWriteMany` (RWX) access mode to be live migrated.

# Maintaining bare-metal nodes

<div wrapper="1" role="_abstract">

When you deploy OpenShift Container Platform on bare metal infrastructure, there are additional considerations that must be taken into account compared to deploying on cloud infrastructure.

</div>

Unlike in cloud environments where the cluster nodes are considered ephemeral, re-provisioning a bare-metal node requires significantly more time and effort for maintenance tasks.

When a bare-metal node fails, for example, if a an unrecoverable kernel error happens or a NIC card hardware failure occurs, workloads on the failed node need to be restarted elsewhere else on the cluster while the problem node is repaired or replaced. Node maintenance mode allows cluster administrators to gracefully power down nodes, moving workloads to other parts of the cluster and ensuring workloads do not get interrupted. Detailed progress and node status details are provided during maintenance.

# About the Node Maintenance Operator

<div wrapper="1" role="_abstract">

The Node Maintenance Operator watches for new or deleted `NodeMaintenance` custom resources (CRs). When a new `NodeMaintenance` CR is detected, no new workloads are scheduled, and the node is cordoned off from the rest of the cluster. All pods that can be evicted are evicted from the node. When a `NodeMaintenance` CR is deleted, the node that is referenced in the CR is made available for new workloads.

</div>

Using a `NodeMaintenance` CR for node maintenance tasks achieves the same results as the `oc adm cordon` and `oc adm drain` commands using standard OpenShift Container Platform custom resource processing.

> [!NOTE]
> The `node-maintenance-operator` (NMO) is no longer shipped with OpenShift Virtualization. It is deployed as a standalone Operator from the software catalog in the OpenShift Container Platform web console or by using the OpenShift CLI (`oc`).

# Additional resources

- [About live migration](../../virt/live_migration/virt-about-live-migration.xml#virt-about-live-migration)

- [About node remediation, fencing, and maintenance](https://docs.redhat.com/en/documentation/workload_availability_for_red_hat_openshift/26.2/html-single/remediation_fencing_and_maintenance/index#about-remediation-fencing-maintenance)
