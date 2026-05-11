<div wrapper="1" role="_abstract">

The following procedures are typically performed after you install OpenShift Virtualization. You can configure the components that are relevant for your environment:

</div>

- As a cluster administrator, you can run a self validation checkup to verify that the environment is fully functional and self-sustained before you deploy production workloads.

- The hostpath provisioner is a local storage provisioner designed for OpenShift Virtualization. If you want to configure local storage for virtual machines, you must enable the hostpath provisioner first.

- [Node placement rules for OpenShift Virtualization Operators, workloads, and controllers](../../virt/post_installation_configuration/virt-node-placement-virt-components.xml#virt-node-placement-virt-components)

- [Network configuration](../../virt/post_installation_configuration/virt-post-install-network-config.xml#virt-post-install-network-config):

  - Installing the Kubernetes NMState and SR-IOV Operators

  - Configuring a Linux bridge network for external access to virtual machines (VMs)

  - Configuring a dedicated secondary network for live migration

  - Configuring an SR-IOV network

  - Enabling the creation of load balancer services by using the OpenShift Container Platform web console

- [Storage configuration](../../virt/post_installation_configuration/virt-post-install-storage-config.xml#virt-post-install-storage-config):

  - Defining a default storage class for the Container Storage Interface (CSI)

  - Configuring local storage by using the Hostpath Provisioner (HPP)
