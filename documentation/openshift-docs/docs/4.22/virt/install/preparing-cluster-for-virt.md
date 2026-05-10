<div wrapper="1" role="_abstract">

Review platform compatibility information before you install OpenShift Virtualization. For detailed system requirements, see "Hardware, software, and operational requirements" in the Additional resources section.

</div>

# Compatible platforms

<div wrapper="1" role="_abstract">

OpenShift Virtualization supports bare-metal servers, ARM64-based systems, and IBM Z® or IBM® LinuxONE systems in logical partitions.

</div>

Compatible platforms
- On-premise bare-metal servers. For more information, see "Planning a bare-metal cluster for OpenShift Virtualization" in the Additional resources section.

- Bare-metal clusters installed on ARM64-based (`arm64`, also known as `aarch64`) systems.

- IBM Z® or IBM® LinuxONE (s390x architecture) systems where an OpenShift Container Platform cluster is installed in logical partitions (LPARs). For more information, see "Preparing to install on IBM Z and IBM LinuxONE" in the Additional resources section.

# Cloud platforms

<div wrapper="1" role="_abstract">

OpenShift Virtualization is compatible with various public cloud platforms, each with specific storage options and support levels.

</div>

> [!IMPORTANT]
> Installing OpenShift Virtualization on certain cloud platforms is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Vendor</th>
<th style="text-align: left;">Status</th>
<th style="text-align: left;">Storage</th>
<th style="text-align: left;">Resources</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Amazon Web Services (AWS)</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><ul>
<li><p>Elastic Block Store (EBS)</p></li>
<li><p>Red Hat OpenShift Data Foundation (ODF)</p></li>
<li><p>Portworx</p></li>
<li><p>FSx (NetApp)</p></li>
</ul></td>
<td style="text-align: left;"><p>For more information, see "Installing a cluster on AWS with customizations" in the Additional resources section.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Red Hat OpenShift Service on AWS (ROSA)</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><ul>
<li><p>EBS</p></li>
<li><p>Portworx</p></li>
<li><p>FSx (Q3)</p></li>
<li><p>ODF</p></li>
</ul></td>
<td style="text-align: left;"><ul>
<li><p><a href="https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/virtualization/index">OpenShift Virtualization</a> in the Red Hat OpenShift Service on AWS documentation</p></li>
<li><p><a href="https://docs.aws.amazon.com/rosa/latest/userguide/what-is-rosa.html">What is Red Hat OpenShift Service on AWS?</a> in the AWS documentation</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>Oracle Cloud Infrastructure (OCI)</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><ul>
<li><p>OCI native storage</p></li>
</ul></td>
<td style="text-align: left;"><ul>
<li><p><a href="https://access.redhat.com/articles/7118050">OpenShift Virtualization and Oracle Cloud Infrastructure (OCI) known issues and limitations</a> in the Red Hat Knowledgebase</p></li>
<li><p><a href="https://github.com/oracle-quickstart/oci-openshift/blob/main/docs/openshift-virtualization.md">Installing OpenShift Virtualization on OCI</a> in the <code>oracle-quickstart/oci-openshift</code> GitHub repository</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>Azure Red Hat OpenShift (ARO)</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><ul>
<li><p>ODF</p></li>
</ul></td>
<td style="text-align: left;"><ul>
<li><p><a href="https://learn.microsoft.com/en-us/azure/openshift/howto-create-openshift-virtualization">OpenShift Virtualization for Azure Red Hat OpenShift (preview)</a> in the Microsoft documentation</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>Google Cloud</p></td>
<td style="text-align: left;"><p>GA, as of OpenShift Virtualization 4.21.1</p></td>
<td style="text-align: left;"><ul>
<li><p>Google Cloud native storage</p></li>
<li><p>Google Cloud NetApp Volumes (GCNV); requires OpenShift Virtualization 4.21.2 or later</p></li>
</ul></td>
<td style="text-align: left;"><ul>
<li><p><a href="https://access.redhat.com/articles/7139046">Storage configuration for OpenShift Virtualization 4.17.x on Google Cloud</a> in the Red Hat Knowledgebase</p></li>
<li><p><a href="https://access.redhat.com/articles/7139682">OpenShift Virtualization on Google Cloud: Known issues and limitations</a> in the Red Hat Knowledgebase</p></li>
<li><p><a href="https://access.redhat.com/articles/7141472">Storage configuration for OpenShift Virtualization with GCNV</a> in the Red Hat Knowledgebase</p></li>
<li><p><a href="https://access.redhat.com/articles/7141471">OpenShift Virtualization with GCNV: Known errors and limitations</a> in the Red Hat Knowledgebase</p></li>
</ul></td>
</tr>
</tbody>
</table>

Bare-metal instances or servers offered by other cloud providers are not supported.

> [!TIP]
> For platform-specific networking information, see "Networking overview" in the Additional resources section.

# OpenShift Virtualization on AWS bare metal

<div wrapper="1" role="_abstract">

You can run OpenShift Virtualization on an Amazon Web Services (AWS) bare metal OpenShift Container Platform cluster.

</div>

> [!NOTE]
> OpenShift Virtualization is also supported on Red Hat OpenShift Service on AWS (ROSA) Classic clusters, which have the same configuration requirements as AWS bare-metal clusters.

# ARM64 compatibility

<div wrapper="1" role="_abstract">

OpenShift Virtualization on ARM64 systems is generally available (GA) with specific limitations for operating systems and live migration.

</div>

Before using OpenShift Virtualization on an ARM64-based system, consider the following limitations:

Operating system
- Only Linux-based guest operating systems are supported.

- All virtualization limitations for RHEL also apply to OpenShift Virtualization. For more information, see [How virtualization on ARM64 differs from AMD64 and Intel 64](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_virtualization/assembly_feature-support-and-limitations-in-rhel-9-virtualization_configuring-and-managing-virtualization#how-virtualization-on-arm-64-differs-from-amd64-and-intel64_feature-support-and-limitations-in-rhel-9-virtualization) in the RHEL documentation.

Live migration
- Live migration is **not supported** on ARM64-based OpenShift Container Platform clusters.

- Hotplug is not supported on ARM64-based clusters because it depends on live migration.

VM creation
- RHEL 10 supports instance types and preferences, but not templates.

- RHEL 9 supports templates, instance types, and preferences.

# IBM Z and IBM LinuxONE compatibility

<div wrapper="1" role="_abstract">

You can use OpenShift Virtualization in an OpenShift Container Platform cluster that is installed in logical partitions (LPARs) on an IBM Z® or IBM® LinuxONE (`s390x` architecture) system.

</div>

Some features are not currently available on `s390x` architecture, while others require workarounds or procedural changes. These lists are subject to change.

Currently unavailable features
The following features are currently not available on `s390x` architecture:

- Memory hot plugging and hot unplugging

- Node Health Check Operator

- SR-IOV Operator

- PCI passthrough

- OpenShift Virtualization cluster checkup framework

- OpenShift Virtualization on a cluster installed in FIPS mode

- IPv6

- IBM® Storage scale

- Hosted control planes for OpenShift Virtualization

- VM pages using HugePages

  The following features are not applicable on `s390x` architecture:

- virtual Trusted Platform Module (vTPM) devices

- UEFI mode for VMs

- USB host passthrough

- Configuring virtual GPUs

- Creating and managing Windows VMs

- Hyper-V

Functionality differences
The following features are available for use on s390x architecture but function differently or require procedural changes:

- When deleting a virtual machine by using the web console, the **grace period** option is ignored. For more information, see "Deleting a virtual machine by using the web console" in the Additional resources section.

- When configuring the default CPU model, the `spec.defaultCPUModel` value is `"gen15b"` for an IBM Z cluster. For more information, see "Configuring the default CPU model" in the Additional resources section.

- When configuring a downward metrics device, if you use a VM preference, the `spec.preference.name` value must be set to `rhel.9.s390x` or another available preference with the format `*.s390x`. For more information, see "Configuring a downward metrics device" in the Additional resources section.

- When creating virtual machines from instance types, you are not allowed to set `spec.domain.memory.maxGuest` because memory hot plugging is not supported on IBM Z®. For more information, see "Creating virtual machines from instance types" in the Additional resources section.

- Prometheus queries for VM guests could have inconsistent outcome in comparison to `x86`.

# Important considerations for any platform

<div wrapper="1" role="_abstract">

Before installing OpenShift Virtualization, note key considerations about installation methods, storage, IPv6, and FIPS mode.

</div>

Installation method considerations
You can use any installation method, including user-provisioned, installer-provisioned, or Assisted Installer, to deploy OpenShift Container Platform. However, the installation method and the cluster topology might affect OpenShift Virtualization functionality, such as snapshots or live migration. For more information about live migration, see "Hardware, software, and operational requirements" in the Additional resources section.

Red Hat OpenShift Data Foundation
If you deploy OpenShift Virtualization with Red Hat OpenShift Data Foundation, you must create a dedicated storage class for Windows virtual machine disks. For more information, see "Optimizing ODF PersistentVolumes for Windows VMs" in the Additional resources section.

IPv6
OpenShift Virtualization support for single-stack IPv6 clusters is limited to the OVN-Kubernetes localnet and Linux bridge Container Network Interface (CNI) plugins.

> [!IMPORTANT]
> Installing OpenShift Virtualization on certain cloud platforms is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

FIPS mode
If you install your cluster in FIPS mode, no additional setup is required for OpenShift Virtualization. For more information, see "Installing a FIPS-compliant cluster" in the Additional resources section.

# Object maximums

<div wrapper="1" role="_abstract">

Consider tested object maximums for both OpenShift Container Platform and OpenShift Virtualization when planning your cluster.

</div>

OpenShift Container Platform
See "OpenShift Container Platform object maximums" in the Additional resources section.

OpenShift Virtualization
See "OpenShift Virtualization supported limits" in the Additional resources section.

# Additional resources

- [Hardware, software, and operational requirements](../../virt/install/virt-requirements.xml#virt-requirements)

- [Planning a bare-metal cluster for OpenShift Virtualization](../../installing/installing_bare_metal/preparing-to-install-on-bare-metal.xml#virt-planning-bare-metal-cluster-for-ocp-virt_preparing-to-install-on-bare-metal)

- [Preparing to install on IBM Z and IBM LinuxONE](../../installing/installing_ibm_z/preparing-to-install-on-ibm-z.xml#preparing-to-install-on-ibm-z_preparing-to-install-on-ibm-z)

- [Installing a cluster on AWS with customizations](../../installing/installing_aws/ipi/installing-aws-customizations.xml#installing-aws-customizations)

- [OpenShift Container Platform object maximums](../../scalability_and_performance/planning-your-environment-according-to-object-maximums.xml#planning-your-environment-according-to-object-maximums)

- [OpenShift Virtualization supported limits](../../virt/about_virt/virt-supported-limits.xml#virt-supported-limits)

- [Installing a FIPS-compliant cluster](../../installing/overview/installing-fips.xml#installing-fips-mode_installing-fips)

- [Configuring the default CPU model](../../virt/managing_vms/advanced_vm_management/virt-configuring-default-cpu-model.xml#virt-configuring-default-cpu-model)

- [Deleting a virtual machine by using the web console](../../virt/managing_vms/virt-delete-vms.xml#virt-delete-vm-web_virt-delete-vms)

- [Configuring a downward metrics device](../../virt/monitoring/virt-exposing-downward-metrics.xml#virt-configuring-downward-metrics_virt-exposing-downward-metrics)

- [Creating virtual machines from instance types](../../virt/creating_vm/virt-creating-vms-from-instance-types.xml#virt-creating-vms-from-instance-types)

- [Networking overview](../../virt/vm_networking/virt-networking-overview.xml#virt-networking)

- [Connecting a virtual machine to an OVN-Kubernetes secondary network](../../virt/vm_networking/virt-connecting-vm-to-ovn-secondary-network.xml#virt-connecting-vm-to-ovn-secondary-network)

- [Exposing a virtual machine by using a service](../../virt/vm_networking/virt-exposing-vm-with-service.xml#virt-exposing-vm-with-service)

- [Optimizing ODF PersistentVolumes for Windows VMs](https://access.redhat.com/articles/6978371)

- [GCNV service levels](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels)

- [Glossary of common terms for OpenShift Container Platform storage](../../storage/index.xml#openshift-storage-common-terms_storage-overview)
