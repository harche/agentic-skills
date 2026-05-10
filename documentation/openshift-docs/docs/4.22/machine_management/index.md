<div wrapper="1" role="_abstract">

You can use machine management to flexibly work with underlying infrastructure such as Amazon Web Services (AWS), Microsoft Azure, Google Cloud, Red Hat OpenStack Platform (RHOSP), and VMware vSphere to manage the OpenShift Container Platform cluster. You can control the cluster and perform auto-scaling, such as scaling up and down the cluster based on specific workload policies.

</div>

It is important to have a cluster that adapts to changing workloads. The OpenShift Container Platform cluster can horizontally scale up and down when the load increases or decreases.

Machine management is implemented as a custom resource definition (CRD). A CRD object defines a new unique object `Kind` in the cluster and enables the Kubernetes API server to handle the object’s entire lifecycle.

The Machine API Operator provisions the following resources:

- `MachineSet`

- `Machine`

- `ClusterAutoscaler`

- `MachineAutoscaler`

- `MachineHealthCheck`

# Machine API overview

<div wrapper="1" role="_abstract">

The Machine API performs all node host provisioning management actions after the cluster installation finishes. Because of this system, OpenShift Container Platform offers an elastic, dynamic provisioning method on top of public or private cloud infrastructure.

</div>

The Machine API is a combination of primary resources that are based on the upstream Cluster API project and custom OpenShift Container Platform resources.

The two primary resources are:

Machines
A fundamental unit that describes the host for a node. A machine has a `providerSpec` specification, which describes the types of compute nodes that are offered for different cloud platforms. For example, a machine type for a compute node might define a specific machine type and required metadata.

Machine sets
`MachineSet` resources are groups of compute machines. Compute machine sets are to compute machines as replica sets are to pods. If you need more compute machines or must scale them down, you change the `replicas` field on the `MachineSet` resource to meet your compute need.

> [!WARNING]
> Control plane machines cannot be managed by compute machine sets.
>
> Control plane machine sets provide management capabilities for supported control plane machines that are similar to what compute machine sets provide for compute machines.
>
> For more information, see “Managing control plane machines".

The following custom resources add more capabilities to your cluster:

Machine autoscaler
The `MachineAutoscaler` resource automatically scales compute machines in a cloud. You can set the minimum and maximum scaling boundaries for nodes in a specified compute machine set, and the machine autoscaler maintains that range of nodes.

The `MachineAutoscaler` object takes effect after a `ClusterAutoscaler` object exists. Both `ClusterAutoscaler` and `MachineAutoscaler` resources are made available by the `ClusterAutoscalerOperator` object.

Cluster autoscaler
This resource is based on the upstream cluster autoscaler project. In the OpenShift Container Platform implementation, it is integrated with the Machine API by extending the compute machine set API. You can use the cluster autoscaler to manage your cluster in the following ways:

- Set cluster-wide scaling limits for resources such as cores, nodes, memory, and GPU

- Set the priority so that the cluster prioritizes pods and new nodes are not brought online for less important pods

- Set the scaling policy so that you can scale up nodes but not scale them down

Machine health check
The `MachineHealthCheck` resource detects when a machine is unhealthy, deletes it, and, on supported platforms, makes a new machine.

In OpenShift Container Platform version 3.11, you could not roll out a multi-zone architecture easily because the cluster did not manage machine provisioning. Beginning with OpenShift Container Platform version 4.1, this process is easier. Each compute machine set is scoped to a single zone, so the installation program sends out compute machine sets across availability zones on your behalf. And then because your compute is dynamic, and in the face of a zone failure, you always have a zone for when you must rebalance your machines. In global Azure regions that do not have multiple availability zones, you can use availability sets to ensure high availability. The autoscaler provides best-effort balancing over the life of a cluster.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Machine phases and lifecycle](../machine_management/machine-phases-lifecycle.xml#machine-phases-lifecycle)

</div>

# Compute machine management

<div wrapper="1" role="_abstract">

As a cluster administrator, you can manage the compute machines in your OpenShift Container Platform cluster.

</div>

For example, you can perform the following actions:

- Create a compute machine set for the following cloud providers:

  - [AWS](../machine_management/creating_machinesets/creating-machineset-aws.xml#creating-machineset-aws)

  - [Azure](../machine_management/creating_machinesets/creating-machineset-azure.xml#creating-machineset-azure)

  - [Azure Stack Hub](../machine_management/creating_machinesets/creating-machineset-azure-stack-hub.xml#creating-machineset-azure-stack-hub)

  - [Google Cloud](../machine_management/creating_machinesets/creating-machineset-gcp.xml#creating-machineset-gcp)

  - [IBM Cloud](../machine_management/creating_machinesets/creating-machineset-ibm-cloud.xml#creating-machineset-ibm-cloud)

  - [IBM Power Virtual Server](../machine_management/creating_machinesets/creating-machineset-ibm-power-vs.xml#creating-machineset-ibm-power-vs)

  - [Nutanix](../machine_management/creating_machinesets/creating-machineset-nutanix.xml#creating-machineset-nutanix)

  - [RHOSP](../machine_management/creating_machinesets/creating-machineset-osp.xml#creating-machineset-osp)

  - [vSphere](../machine_management/creating_machinesets/creating-machineset-vsphere.xml#creating-machineset-vsphere)

- Create a machine set for a bare metal deployment: [Creating a compute machine set on bare metal](../machine_management/creating_machinesets/creating-machineset-bare-metal.xml#creating-machineset-bare-metal)

- [Manually scale a compute machine set](../machine_management/manually-scaling-machineset.xml#manually-scaling-machineset) by adding or removing a machine from the compute machine set.

- [Modify a compute machine set](../machine_management/modifying-machineset.xml#modifying-machineset) through the `MachineSet` YAML configuration file.

- [Delete](../machine_management/deleting-machine.xml#deleting-machine) a machine.

- [Create infrastructure compute machine sets](../machine_management/creating-infrastructure-machinesets.xml#creating-infrastructure-machinesets).

- Configure and deploy a [machine health check](../machine_management/deploying-machine-health-checks.xml#deploying-machine-health-checks) to automatically fix damaged machines in a machine pool.

# Control plane machine management

<div wrapper="1" role="_abstract">

As a cluster administrator, you can manage the control plane machines in your OpenShift Container Platform cluster.

</div>

For example, you can perform the following actions:

- [Update your control plane configuration](../machine_management/control_plane_machine_management/cpmso-managing-machines.xml#cpmso-feat-config-update_cpmso-managing-machines) with a control plane machine set for the following cloud providers:

  - [Amazon Web Services](../machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.xml#cpmso-config-options-aws)

  - [Google Cloud](../machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-gcp.xml#cpmso-config-options-gcp)

  - [Microsoft Azure](../machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.xml#cpmso-config-options-azure)

  - [Nutanix](../machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-nutanix.xml#cpmso-config-options-nutanix)

  - [Red Hat OpenStack Platform (RHOSP)](../machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-openstack.xml#cpmso-config-options-openstack)

  - [VMware vSphere](../machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-vsphere.xml#cpmso-config-options-vsphere)

- Configure and deploy a [machine health check](../machine_management/deploying-machine-health-checks.xml#deploying-machine-health-checks) to automatically recover unhealthy control plane machines.

# Cluster autoscaling

<div wrapper="1" role="_abstract">

You can automatically scale your OpenShift Container Platform cluster to ensure flexibility for changing workloads.

</div>

To [autoscale](../machine_management/applying-autoscaling.xml#applying-autoscaling) your cluster, you must first deploy a cluster autoscaler, and then deploy a machine autoscaler for each compute machine set.

- The [*cluster autoscaler*](../machine_management/applying-autoscaling.xml#cluster-autoscaler-about_applying-autoscaling) increases and decreases the size of the cluster based on deployment needs.

- The [*machine autoscaler*](../machine_management/applying-autoscaling.xml#machine-autoscaler-about_applying-autoscaling) adjusts the number of machines in the compute machine sets that you deploy in your OpenShift Container Platform cluster.

# Compute machine creation on user-provisioned infrastructure

<div wrapper="1" role="_abstract">

User-provisioned infrastructure is an environment where you can deploy infrastructure such as compute, network, and storage resources that host the OpenShift Container Platform. You can add compute machines to a cluster on user-provisioned infrastructure during or after the installation process.

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Adding compute machines to clusters with user-provisioned infrastructure manually](../machine_management/user_infra/adding-compute-user-infra-general.xml#adding-compute-user-infra-general)

</div>
