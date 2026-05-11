<div wrapper="1" role="_abstract">

Explore OpenShift Virtualization by taking guided tours, installing the Operator, and configuring a basic environment. Learn how to migrate from your current platform, then learn more about how to deploy and manage virtual machines (VMs) by following the additional resources links.

</div>

> [!NOTE]
> Cluster configuration procedures require `cluster-admin` privileges.

# Getting started tour

<div wrapper="1" role="_abstract">

The **Getting started** tour introduces several key aspects of using OpenShift Virtualization. There are two ways to start the tour.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform web console.

</div>

<div>

<div class="title">

Procedure

</div>

- If you see the **Welcome to OpenShift Virtualization** dialog, click **Start Tour**.

- Otherwise, go to **Virtualization** → **Overview** → **Settings** → **User** → **Getting started resources** → **Guided tour**.

</div>

# Quick start tours

<div wrapper="1" role="_abstract">

You can explore several OpenShift Virtualization capabilities by taking quick start tours in the web console.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform web console.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Click the **Help** icon **?** in the menu bar on the header of the OpenShift Container Platform web console.

2.  Select **Quick Starts**. You can filter the list of tours by entering the keyword `virtual` in the **Filter** field.

</div>

# Migrating to OpenShift Virtualization

<div wrapper="1" role="_abstract">

To migrate virtual machines from an external provider such as VMware vSphere, Red Hat OpenStack Platform (RHOSP), Red Hat Virtualization, or another OpenShift Container Platform cluster, use the Migration Toolkit for Virtualization (MTV). You can also migrate Open Virtual Appliance (OVA) files created by VMware vSphere.

</div>

> [!NOTE]
> Migration Toolkit for Virtualization is not part of OpenShift Virtualization and requires separate installation. For this reason, all links in this procedure lead outside of OpenShift Virtualization documentation.

<div>

<div class="title">

Prerequisites

</div>

- The Migration Toolkit for Virtualization Operator [is installed](https://docs.redhat.com/en/documentation/migration_toolkit_for_virtualization/2.8/html/installing_and_using_the_migration_toolkit_for_virtualization/installing-the-operator_mtv#installing-the-operator_mtv).

</div>

<div>

<div class="title">

Procedure

</div>

- [Migrate virtual machines from VMware vSphere](https://docs.redhat.com/en/documentation/migration_toolkit_for_virtualization/2.8/html/installing_and_using_the_migration_toolkit_for_virtualization/migrating-vmware#adding-source-provider_vmware).

- [Migrate virtual machines from Red Hat OpenStack Platform (RHOSP)](https://docs.redhat.com/en/documentation/migration_toolkit_for_virtualization/2.8/html/installing_and_using_the_migration_toolkit_for_virtualization/migrating-osp_ostack#adding-source-provider_ostack).

- [Migrate virtual machines from Red Hat Virtualization](https://docs.redhat.com/en/documentation/migration_toolkit_for_virtualization/2.8/html/installing_and_using_the_migration_toolkit_for_virtualization/migrating-rhv_rhv#adding-source-provider_rhv).

- [Migrate virtual machines from OpenShift Virtualization](https://docs.redhat.com/en/documentation/migration_toolkit_for_virtualization/2.8/html/installing_and_using_the_migration_toolkit_for_virtualization/migrating-virt_cnv#adding-source-provider_cnv).

- [Migrate virtual machines from OVA files created by VMware vSphere](https://docs.redhat.com/en/documentation/migration_toolkit_for_virtualization/2.8/html/installing_and_using_the_migration_toolkit_for_virtualization/migrating-ova_ova#adding-source-provider_ova).

</div>

# Additional resources

- [Plan your bare-metal cluster for OpenShift Virtualization](../../installing/installing_bare_metal/preparing-to-install-on-bare-metal.xml#virt-planning-bare-metal-cluster-for-ocp-virt_preparing-to-install-on-bare-metal)

- [Prepare your cluster for OpenShift Virtualization](../../virt/install/preparing-cluster-for-virt.xml#preparing-cluster-for-virt)

- [Learn about storage volumes for VM disks](../../virt/install/preparing-cluster-for-virt.xml#virt-about-storage-volumes-for-vm-disks_virt-requirements)

- [Use a CSI-enabled storage provider](../../storage/container_storage_interface/persistent-storage-csi.xml#persistent-storage-csi)

- [Configure local storage for virtual machines](../../virt/storage/virt-configuring-local-storage-with-hpp.xml#virt-configuring-local-storage-with-hpp)

- [Install the OpenShift Virtualization Operator](../../virt/install/installing-virt.xml#virt-installing-virt-operator_installing-virt)

- [Install the Kubernetes NMState Operator](../../networking/networking_operators/k8s-nmstate-about-the-k8s-nmstate-operator.xml#installing-the-kubernetes-nmstate-operator-cli)

- [Specify nodes for virtual machines](../../virt/managing_vms/advanced_vm_management/virt-specifying-nodes-for-vms.xml#virt-specifying-nodes-for-vms)

- [Install and use the `virtctl` command-line interface (CLI) tool](../../virt/getting_started/virt-using-the-cli-tools.xml#virt-using-the-cli-tools)

- [Create a VM from a Red Hat image](../../virt/creating_vms_advanced/virt-creating-vms-from-rh-images-overview.xml#virt-creating-vms-from-rh-images-overview)

- [Create a VM from an instance type](../../virt/creating_vm/virt-creating-vms-from-instance-types.xml#virt-creating-vms-from-instance-types)

- [Import a custom image from a web page](../../virt/creating_vms_advanced/virt-creating-vms-from-web-images.xml#virt-creating-vms-from-web-images)

- [Upload an image from your local machine](../../virt/creating_vms_advanced/virt-creating-vms-uploading-images.xml#virt-creating-vms-uploading-images)

- [Clone a persistent volume claim (PVC)](../../virt/creating_vms_advanced/virt-creating-vms-by-cloning-pvcs.xml#virt-creating-vms-by-cloning-pvcs)

- [Connect a VM to a Linux bridge network](../../virt/vm_networking/virt-connecting-vm-to-linux-bridge.xml#virt-connecting-vm-to-linux-bridge)

- [Connect a VM to an Open Virtual Network (OVN)-Kubernetes secondary network](../../virt/vm_networking/virt-connecting-vm-to-ovn-secondary-network.xml#virt-connecting-vm-to-ovn-secondary-network)

- [Connect a VM to a Single Root I/O Virtualization (SR-IOV) network](../../virt/vm_networking/virt-connecting-vm-to-sriov.xml#virt-connecting-vm-to-sriov)

- [Connect to a virtual machine console](../../virt/managing_vms/virt-accessing-vm-consoles.xml#virt-accessing-vm-consoles)

- [Connect to a VM by using SSH](../../virt/managing_vms/virt-accessing-vm-ssh.xml#virt-accessing-vm-ssh)

- [Connect to the desktop viewer by using the web console](../../virt/managing_vms/virt-accessing-vm-consoles.xml#virt-connecting-desktop-viewer-web_virt-accessing-vm-consoles)

- [Manage a VM by using the web console](../../virt/managing_vms/virt-controlling-vm-states.xml#virt-controlling-vm-states)

- [Export a VM](../../virt/managing_vms/virt-exporting-vms.xml#virt-accessing-exported-vm-manifests_virt-exporting-vms)

- [Review post-installation configuration options](../../virt/post_installation_configuration/virt-post-install-config.xml#virt-post-install-config)

- [Configure storage options and automatic boot source updates](../../virt/storage/virt-storage-config-overview.xml#virt-storage-config-overview)

- [Learn about monitoring and health checks](../../virt/monitoring/virt-monitoring-overview.xml#virt-monitoring-overview)

- [Learn about live migration](../../virt/live_migration/virt-about-live-migration.xml#virt-about-live-migration)

- [Back up and restore VMs by using the OpenShift API for Data Protection (OADP)](../../backup_and_restore/application_backup_and_restore/installing/installing-oadp-kubevirt.xml#installing-oadp-kubevirt)

- [Tune and scale your cluster](https://access.redhat.com/articles/6994974)
