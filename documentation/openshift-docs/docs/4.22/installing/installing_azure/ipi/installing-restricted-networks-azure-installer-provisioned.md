In OpenShift Container Platform version 4.17, you can install a cluster on Microsoft Azure in a restricted network by creating an internal mirror of the installation release content on an existing Azure Virtual Network (VNet).

> [!IMPORTANT]
> You can install an OpenShift Container Platform cluster by using mirrored installation release content, but your cluster requires internet access to use the Azure APIs.

# Prerequisites

- You [mirrored the images for a disconnected installation](../../../disconnected/installing-mirroring-installation-images.xml#installation-about-mirror-registry_installing-mirroring-installation-images) to your registry and obtained the `imageContentSources` data for your version of OpenShift Container Platform.

  > [!IMPORTANT]
  > Because the installation media is on the mirror host, you can use that computer to complete all installation steps.

- You have an existing VNet in Azure. While installing a cluster in a restricted network that uses installer-provisioned infrastructure, you cannot use the installer-provisioned VNet. You must use a user-provisioned VNet that satisfies one of the following requirements:

  - The VNet contains the mirror registry.

  - The VNet has firewall rules or a peering connection to access the mirror registry hosted elsewhere.

# About installations in restricted networks

In OpenShift Container Platform 4.17, you can perform an installation that does not require an active connection to the internet to obtain software components. Restricted network installations can be completed using installer-provisioned infrastructure or user-provisioned infrastructure, depending on the cloud platform to which you are installing the cluster.

If you choose to perform a restricted network installation on a cloud platform, you still require access to its cloud APIs. Some cloud functions, like Amazon Web Service’s Route 53 DNS and IAM services, require internet access. Depending on your network, you might require less internet access for an installation on bare metal hardware, Nutanix, or on VMware vSphere.

To complete a restricted network installation, you must create a registry that mirrors the contents of the OpenShift image registry and contains the installation media. You can create this registry on a mirror host, which can access both the internet and your closed network, or by using other methods that meet your restrictions.

## Additional limits

Clusters in restricted networks have the following additional limitations and restrictions:

- The `ClusterVersion` status includes an `Unable to retrieve available updates` error.

- By default, you cannot use the contents of the Developer Catalog because you cannot access the required image stream tags.

## User-defined outbound routing

In OpenShift Container Platform, you can choose your own outbound routing for a cluster to connect to the internet. This allows you to skip the creation of public IP addresses and the public load balancer.

You can configure user-defined routing by modifying parameters in the `install-config.yaml` file before installing your cluster. A pre-existing VNet is required to use outbound routing when installing a cluster; the installation program is not responsible for configuring this.

When configuring a cluster to use user-defined routing, the installation program does not create the following resources:

- Outbound rules for access to the internet.

- Public IPs for the public load balancer.

- Kubernetes Service object to add the cluster machines to the public load balancer for outbound requests.

You must ensure the following items are available before setting user-defined routing:

- Egress to the internet is possible to pull container images, unless using an OpenShift image registry mirror.

- The cluster can access Azure APIs.

- Various allowlist endpoints are configured. You can reference these endpoints in the *Configuring your firewall* section.

There are several pre-existing networking setups that are supported for internet access using user-defined routing.

### Restricted cluster with Azure Firewall

You can use Azure Firewall to restrict the outbound routing for the Virtual Network (VNet) that is used to install the OpenShift Container Platform cluster. For more information, see [providing user-defined routing with Azure Firewall](https://learn.microsoft.com/en-us/azure/aks/egress-outboundtype#deploy-a-cluster-with-outbound-type-of-udr-and-azure-firewall). You can create a OpenShift Container Platform cluster in a restricted network by using VNet with Azure Firewall and configuring the user-defined routing.

> [!IMPORTANT]
> If you are using Azure Firewall for restricting internet access, you must set the `publish` field to `Internal` in the `install-config.yaml` file. This is because [Azure Firewall does not work properly with Azure public load balancers](https://learn.microsoft.com/en-us/azure/firewall/integrate-lb).

# About reusing a VNet for your OpenShift Container Platform cluster

In OpenShift Container Platform 4.17, you can deploy a cluster into an existing Azure Virtual Network (VNet) in Microsoft Azure. If you do, you must also use existing subnets within the VNet and routing rules.

By deploying OpenShift Container Platform into an existing Azure VNet, you might be able to avoid service limit constraints in new accounts or more easily abide by the operational constraints that your company’s guidelines set. This is a good option to use if you cannot obtain the infrastructure creation permissions that are required to create the VNet.

## Requirements for using your VNet

When you deploy a cluster by using an existing VNet, you must perform additional network configuration before you install the cluster. In installer-provisioned infrastructure clusters, the installer usually creates the following components, but it does not create them when you install into an existing VNet:

- Subnets

- Route tables

- VNets

- Network Security Groups

> [!NOTE]
> The installation program requires that you use the cloud-provided DNS server. Using a custom DNS server is not supported and causes the installation to fail.

If you use a custom VNet, you must correctly configure it and its subnets for the installation program and the cluster to use. The installation program cannot subdivide network ranges for the cluster to use, set route tables for the subnets, or set VNet options like DHCP, so you must do so before you install the cluster.

The cluster must be able to access the resource group that contains the existing VNet and subnets. While all of the resources that the cluster creates are placed in a separate resource group that it creates, some network resources are used from a separate group. Some cluster Operators must be able to access resources in both resource groups. For example, the Machine API controller attaches NICS for the virtual machines that it creates to subnets from the networking resource group.

Your VNet must meet the following characteristics:

- The VNet’s CIDR block must contain the `Networking.MachineCIDR` range, which is the IP address pool for cluster machines.

- The VNet and its subnets must belong to the same resource group, and the subnets must be configured to use Azure-assigned DHCP IP addresses instead of static IP addresses.

You must provide two subnets within your VNet, one for the control plane machines and one for the compute machines. Because Azure distributes machines in different availability zones within the region that you specify, your cluster will have high availability by default.

> [!NOTE]
> By default, if you specify availability zones in the `install-config.yaml` file, the installation program distributes the control plane machines and the compute machines across [these availability zones](https://azure.microsoft.com/en-us/global-infrastructure/availability-zones/) within [a region](https://azure.microsoft.com/en-us/global-infrastructure/regions). To ensure high availability for your cluster, select a region with at least three availability zones. If your region contains fewer than three availability zones, the installation program places more than one control plane machine in the available zones.

To ensure that the subnets that you provide are suitable, the installation program confirms the following data:

- All the specified subnets exist.

- There are two private subnets, one for the control plane machines and one for the compute machines.

- The subnet CIDRs belong to the machine CIDR that you specified. Machines are not provisioned in availability zones that you do not provide private subnets for. If required, the installation program creates public load balancers that manage the control plane and worker nodes, and Azure allocates a public IP address to them.

> [!NOTE]
> If you destroy a cluster that uses an existing VNet, the VNet is not deleted.

### Network security group requirements

The network security groups for the subnets that host the compute and control plane machines require specific access to ensure that the cluster communication is correct. You must create rules to allow access to the required cluster communication ports.

> [!IMPORTANT]
> The network security group rules must be in place before you install the cluster. If you attempt to install a cluster without the required access, the installation program cannot reach the Azure APIs, and installation fails.

| Port | Description | Control plane | Compute |
|----|----|----|----|
| `80` | Allows HTTP traffic |  | x |
| `443` | Allows HTTPS traffic |  | x |
| `6443` | Allows communication to the control plane machines | x |  |
| `22623` | Allows internal communication to the machine config server for provisioning machines | x |  |
| `*` | Allows connections to Azure APIs. You must set a Destination Service Tag to `AzureCloud`. <sup>\[1\]</sup> | x | x |
| `*` | Denies connections to the internet. You must set a Destination Service Tag to `Internet`. <sup>\[1\]</sup> | x | x |

Required ports

<div wrapper="1" role="small">

1.  If you are using Azure Firewall to restrict the internet access, then you can configure Azure Firewall to allow the Azure APIs. A network security group rule is not needed. For more information, see "Configuring your firewall" in "Additional resources".

</div>

> [!IMPORTANT]
> Currently, there is no supported way to block or restrict the machine config server endpoint. The machine config server must be exposed to the network so that newly-provisioned machines, which have no existing configuration or state, are able to fetch their configuration. In this model, the root of trust is the certificate signing requests (CSR) endpoint, which is where the kubelet sends its certificate signing request for approval to join the cluster. Because of this, machine configs should not be used to distribute sensitive information, such as secrets and certificates.
>
> To ensure that the machine config server endpoints, ports 22623 and 22624, are secured in bare metal scenarios, customers must configure proper network policies.

Because cluster components do not modify the user-provided network security groups, which the Kubernetes controllers update, a pseudo-network security group is created for the Kubernetes controller to modify without impacting the rest of the environment.

<table>
<caption>Ports used for all-machine to all-machine communications</caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 22%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Protocol</th>
<th style="text-align: left;">Port</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>ICMP</p></td>
<td style="text-align: left;"><p>N/A</p></td>
<td style="text-align: left;"><p>Network reachability tests</p></td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;"><p>TCP</p></td>
<td style="text-align: left;"><p><code>1936</code></p></td>
<td style="text-align: left;"><p>Metrics</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>9000</code>-<code>9999</code></p></td>
<td style="text-align: left;"><p>Host level services, including the node exporter on ports <code>9100</code>-<code>9101</code> and the Cluster Version Operator on port <code>9099</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>10250</code>-<code>10259</code></p></td>
<td style="text-align: left;"><p>The default ports that Kubernetes reserves</p></td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;"><p>UDP</p></td>
<td style="text-align: left;"><p><code>6081</code></p></td>
<td style="text-align: left;"><p>Geneve</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>9000</code>-<code>9999</code></p></td>
<td style="text-align: left;"><p>Host level services, including the node exporter on ports <code>9100</code>-<code>9101</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>500</code></p></td>
<td style="text-align: left;"><p>IPsec IKE packets</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>4500</code></p></td>
<td style="text-align: left;"><p>IPsec NAT-T packets</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>123</code></p></td>
<td style="text-align: left;"><p>Network Time Protocol (NTP) on UDP port <code>123</code>. If you configure an external NTP time server, you must open UDP port <code>123</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>TCP/UDP</p></td>
<td style="text-align: left;"><p><code>30000</code>-<code>32767</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Kubernetes node port</p></td>
<td style="text-align: left;"><p>ESP</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
</tbody>
</table>

| Protocol | Port          | Description                |
|----------|---------------|----------------------------|
| TCP      | `2379`-`2380` | etcd server and peer ports |

Ports used for control plane machine to control plane machine communications

## Division of permissions

Starting with OpenShift Container Platform 4.3, you do not need all of the permissions that are required for an installation program-provisioned infrastructure cluster to deploy a cluster. This change mimics the division of permissions that you might have at your company: some individuals can create different resources in your clouds than others. For example, you might be able to create application-specific items, like instances, storage, and load balancers, but not networking-related components such as VNets, subnet, or ingress rules.

The Azure credentials that you use when you create your cluster do not need the networking permissions that are required to make VNets and core networking components within the VNet, such as subnets, routing tables, internet gateways, NAT, and VPN. You still need permission to make the application resources that the machines within the cluster require, such as load balancers, security groups, storage accounts, and nodes.

## Isolation between clusters

Because the cluster is unable to modify network security groups in an existing subnet, there is no way to isolate clusters from each other on the VNet.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [About the OVN-Kubernetes network plugin](../../../networking/ovn_kubernetes_network_provider/about-ovn-kubernetes.xml#about-ovn-kubernetes)

- [Configuring your firewall](../../../installing/install_config/configuring-firewall.xml#configuring-firewall)

</div>

# Creating the installation configuration file

<div wrapper="1" role="_abstract">

You can customize the OpenShift Container Platform cluster you install on Microsoft Azure.

</div>

> [!IMPORTANT]
> Do not specify `windows`, `microsoft`, or other variants of these words in the `metadata.name` parameter of the `install-config.yaml` file. Specifying one of these words for the cluster name causes the installation program to generate an error message like the following example message:
>
> ``` terminal
> The resource name 'windows-xxxx-identity' or a part of the name is a trademarked or reserved word.
> ```
>
> Additionally, specifying `login` at the beginning of the name in the `metadata.name` parameter of the `install-config.yaml` file results in the generation of an error message. You can specify `login` in the middle or end of the name.

<div>

<div class="title">

Prerequisites

</div>

- You have the OpenShift Container Platform installation program and the pull secret for your cluster. For a restricted network installation, these files are on your mirror host.

- You have the `imageContentSources` values that were generated during mirror registry creation.

- You have obtained the contents of the certificate for your mirror registry.

- You have retrieved a Red Hat Enterprise Linux CoreOS (RHCOS) image and uploaded it to an accessible location.

- You have an Azure subscription ID and tenant ID.

- If you are installing the cluster using a service principal, you have its application ID and password.

- If you are installing the cluster using a system-assigned managed identity, you have enabled it on the virtual machine that you will run the installation program from.

- If you are installing the cluster using a user-assigned managed identity, you have met these prerequisites:

  - You have its client ID.

  - You have assigned it to the virtual machine that you will run the installation program from.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Optional: If you have run the installation program on this computer before, and want to use an alternative service principal or managed identity, go to the `~/.azure/` directory and delete the `osServicePrincipal.json` configuration file.

    Deleting this file prevents the installation program from automatically reusing subscription and authentication values from a previous installation.

2.  Create the `install-config.yaml` file.

    1.  Change to the directory that contains the installation program and run the following command:

        ``` terminal
        $ ./openshift-install create install-config --dir <installation_directory>
        ```

        - `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates.

          When specifying the directory:

        - Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.

        - Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.

    2.  At the prompts, provide the configuration details for your cloud:

        1.  Optional: Select an SSH key to use to access your cluster machines.

            > [!NOTE]
            > For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

        2.  Select **azure** as the platform to target.

            If the installation program cannot locate the `osServicePrincipal.json` configuration file from a previous installation, you are prompted for Azure subscription and authentication values.

        3.  Enter the following Azure parameter values for your subscription:

            - **azure subscription id**: Enter the subscription ID to use for the cluster.

            - **azure tenant id**: Enter the tenant ID.

        4.  Depending on the Azure identity you are using to deploy the cluster, do one of the following when prompted for the **azure service principal client id**:

            - If you are using a service principal, enter its application ID.

            - If you are using a system-assigned managed identity, leave this value blank.

            - If you are using a user-assigned managed identity, specify its client ID.

        5.  Depending on the Azure identity you are using to deploy the cluster, do one of the following when prompted for the **azure service principal client secret**:

            - If you are using a service principal, enter its password.

            - If you are using a system-assigned managed identity, leave this value blank.

            - If you are using a user-assigned managed identity, leave this value blank.

        6.  Select the region to deploy the cluster to.

        7.  Select the base domain to deploy the cluster to. The base domain corresponds to the Azure DNS Zone that you created for your cluster.

        8.  Enter a descriptive name for your cluster.

            > [!IMPORTANT]
            > All Azure resources that are available through public endpoints are subject to resource name restrictions, and you cannot create resources that use certain terms. For a list of terms that Azure restricts, see [Resolve reserved resource name errors](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-reserved-resource-name) in the Azure documentation.

        9.  Paste the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret).

3.  Edit the `install-config.yaml` file to give the additional information that is required for an installation in a restricted network.

    1.  Update the `pullSecret` value to contain the authentication information for your registry:

        ``` yaml
        pullSecret: '{"auths":{"<mirror_host_name>:5000": {"auth": "<credentials>","email": "you@example.com"}}}'
        ```

        For `<mirror_host_name>`, specify the registry domain name that you specified in the certificate for your mirror registry, and for `<credentials>`, specify the base64-encoded user name and password for your mirror registry.

    2.  Add the `additionalTrustBundle` parameter and value.

        ``` yaml
        additionalTrustBundle: |
          -----BEGIN CERTIFICATE-----
          ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
          -----END CERTIFICATE-----
        ```

        The value must be the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority, or the self-signed certificate that you generated for the mirror registry.

    3.  Define the network and subnets for the VNet to install the cluster under the `platform.azure` field:

        ``` yaml
        networkResourceGroupName: <vnet_resource_group>
        virtualNetwork: <vnet>
        controlPlaneSubnet: <control_plane_subnet>
        computeSubnet: <compute_subnet>
        ```

        where:

        `<vnet_resource_group>`
        Specifies the resource group name that contains the existing virtual network (VNet).

        `<vnet>`
        Specifies the existing virtual network name.

        `<control_plane_subnet>`
        Specifies the existing subnet name to deploy the control plane machines.

        `<compute_subnet>`
        Specifies the existing subnet name to deploy compute machines.

    4.  Add the image content resources, which resemble the following YAML excerpt:

        ``` yaml
        imageContentSources:
        - mirrors:
          - <mirror_host_name>:5000/<repo_name>/release
          source: quay.io/openshift-release-dev/ocp-release
        - mirrors:
          - <mirror_host_name>:5000/<repo_name>/release
          source: registry.redhat.io/ocp/release
        ```

        For these values, use the `imageContentSources` that you recorded during mirror registry creation.

    5.  Optionally, set the publishing strategy to `Internal`:

        ``` yaml
        publish: Internal
        ```

        By setting this option, you create an internal Ingress Controller and a private load balancer.

        > [!IMPORTANT]
        > Azure Firewall [does not work seamlessly](https://learn.microsoft.com/en-us/azure/firewall/integrate-lb) with Azure Public Load balancers. Thus, when using Azure Firewall for restricting internet access, the `publish` field in `install-config.yaml` should be set to `Internal`.

4.  Make any other modifications to the `install-config.yaml` file that you require.

    For more information about the parameters, see "Installation configuration parameters".

5.  Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

    > [!IMPORTANT]
    > The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

    If previously not detected, the installation program creates an `osServicePrincipal.json` configuration file and stores this file in the `~/.azure/` directory on your computer. This ensures that the installation program can load the profile when it is creating an OpenShift Container Platform cluster on the target platform.

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Installation configuration parameters for Azure](../../../installing/installing_azure/installation-config-parameters-azure.xml#installation-config-parameters-azure)

</div>

## Minimum resource requirements for cluster installation

<div wrapper="1" role="_abstract">

Each created cluster must meet minimum requirements so that the cluster runs as expected.

</div>

| Machine | Operating System | vCPU <sup>\[1\]</sup> | Virtual RAM | Storage | Input/Output Per Second (IOPS)<sup>\[2\]</sup> |
|----|----|----|----|----|----|
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Minimum resource requirements

<div wrapper="1" role="small">

1.  One vCPU is equivalent to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs.

2.  OpenShift Container Platform and Kubernetes are sensitive to disk performance, and faster storage is recommended, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. Note that on many cloud platforms, storage size and IOPS scale together, so you might need to over-allocate storage volume to obtain sufficient performance.

3.  As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. Use of RHEL 7 compute machines is deprecated and has been removed in OpenShift Container Platform 4.10 and later.

</div>

> [!NOTE]
> For OpenShift Container Platform version 4.19, RHCOS is based on RHEL version 9.6, which updates the micro-architecture requirements. The following list contains the minimum instruction set architectures (ISA) that each architecture requires:
>
> - x86-64 architecture requires x86-64-v2 ISA
>
> - ARM64 architecture requires ARMv8.0-A ISA
>
> - IBM Power architecture requires Power 9 ISA
>
> - s390x architecture requires z14 ISA
>
> For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.2_release_notes/index#architectures) (RHEL documentation).

> [!IMPORTANT]
> You are required to use Azure virtual machines that have the `premiumIO` parameter set to `true`.

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

## Tested instance types for Azure

The following Microsoft Azure instance types have been tested with OpenShift Container Platform.

<div class="example">

<div class="title">

Machine types based on 64-bit x86 architecture

</div>

<https://raw.githubusercontent.com/openshift/installer/release-4.21/docs/user/azure/tested_instance_types_x86_64.md>

</div>

## Tested instance types for Azure on 64-bit ARM infrastructures

The following Microsoft Azure ARM64 instance types have been tested with OpenShift Container Platform.

<div class="example">

<div class="title">

Machine types based on 64-bit ARM architecture

</div>

<https://raw.githubusercontent.com/openshift/installer/release-4.21/docs/user/azure/tested_instance_types_aarch64.md>

</div>

## Enabling trusted launch for Azure VMs

You can enable two trusted launch features when installing your cluster on Azure: [secure boot](https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch#secure-boot) and [virtualized Trusted Platform Modules](https://learn.microsoft.com/en-us/windows/security/hardware-security/tpm/trusted-platform-module-overview).

For more information about the sizes of virtual machines that support the trusted launch features, see [Virtual machine sizes](https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch#virtual-machines-sizes).

> [!IMPORTANT]
> Trusted launch is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You have created an `install-config.yaml` file.

</div>

<div>

<div class="title">

Procedure

</div>

- Edit the `install-config.yaml` file before deploying your cluster:

  - Enable trusted launch only on control plane by adding the following stanza:

    ``` yaml
    controlPlane:
      platform:
        azure:
          settings:
            securityType: TrustedLaunch
            trustedLaunch:
              uefiSettings:
                secureBoot: Enabled
                virtualizedTrustedPlatformModule: Enabled
    ```

  - Enable trusted launch only on compute node by adding the following stanza:

    ``` yaml
    compute:
      platform:
        azure:
          settings:
            securityType: TrustedLaunch
            trustedLaunch:
              uefiSettings:
                secureBoot: Enabled
                virtualizedTrustedPlatformModule: Enabled
    ```

  - Enable trusted launch on all nodes by adding the following stanza:

    ``` yaml
    platform:
      azure:
        settings:
          securityType: TrustedLaunch
          trustedLaunch:
            uefiSettings:
              secureBoot: Enabled
              virtualizedTrustedPlatformModule: Enabled
    ```

</div>

## Enabling confidential VMs

You can enable confidential VMs when installing your cluster. You can enable confidential VMs for compute nodes, control plane nodes, or all nodes.

You can use confidential VMs with the following VM sizes:

- DCasv5-series

- DCadsv5-series

- ECasv5-series

- ECadsv5-series

- DCesv5-series

- DCedsv5-series

- ECesv5-series

- ECedsv5-series

- NCCads_H100_v5

> [!IMPORTANT]
> Confidential VMs are currently not supported on 64-bit ARM architectures.

<div>

<div class="title">

Prerequisites

</div>

- You have created an `install-config.yaml` file.

</div>

<div>

<div class="title">

Procedure

</div>

- Edit the `install-config.yaml` file before deploying your cluster:

  - Enable confidential VMs only on control plane by adding the following stanza:

    ``` yaml
    controlPlane:
      platform:
        azure:
          settings:
            securityType: ConfidentialVM
            confidentialVM:
              uefiSettings:
                secureBoot: Enabled
                virtualizedTrustedPlatformModule: Enabled
          osDisk:
            securityProfile:
              securityEncryptionType: VMGuestStateOnly
    ```

  - Enable confidential VMs only on compute nodes by adding the following stanza:

    ``` yaml
    compute:
      platform:
        azure:
          settings:
            securityType: ConfidentialVM
            confidentialVM:
              uefiSettings:
                secureBoot: Enabled
                virtualizedTrustedPlatformModule: Enabled
          osDisk:
            securityProfile:
              securityEncryptionType: VMGuestStateOnly
    ```

  - Enable confidential VMs on all nodes by adding the following stanza:

    ``` yaml
    platform:
      azure:
        defaultMachinePlatform:
          settings:
            securityType: ConfidentialVM
            confidentialVM:
              uefiSettings:
                secureBoot: Enabled
                virtualizedTrustedPlatformModule: Enabled
          osDisk:
            securityProfile:
              securityEncryptionType: VMGuestStateOnly
    ```

</div>

## Configuring a dedicated disk for etcd

You can install your OpenShift Container Platform cluster on Microsoft Azure with a dedicated data disk for `etcd`. This configuration attaches a separate managed disk to each control plane node and uses it only for `etcd` data, which can improve cluster performance and stability.

> [!IMPORTANT]
> Dedicated disk for etcd is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You have created an `install-config.yaml` file.

</div>

<div>

<div class="title">

Procedure

</div>

- To configure a dedicated `etcd` disk, edit the `install-config.yaml` file and add the `diskSetup` and `dataDisks` parameters to the `controlPlane` stanza:

  ``` yaml
  # ...
  controlPlane:
    architecture: amd64
    hyperthreading: Enabled
    name: master
    platform:
      azure:
        type: Standard_D4s_v5
        dataDisks:
        - nameSuffix: etcddisk
          cachingType: None
          diskSizeGB: 20
          lun: 0
    diskSetup:
    - type: etcd
      etcd:
        platformDiskID: etcddisk
    replicas: 3
  # ...
  ```

</div>

- Specify the same value you defined for `platformDiskID`.

- Specify `None`. Other caching requirements are not currently supported.

- Specify a disk size in GB. This value can be any integer greater than `0`.

  > [!NOTE]
  > A minimum of 20 GB ensures enough space is available for defragmentation operations.

- Specify a logical unit number (LUN). This can be any integer from `0` through `63` that is not used by another disk.

- Specify `etcd`. This identifies `etcd` as the node component type to receive a dedicated disk.

- Specify a name to identify the disk. This value must not exceed 12 characters.

## Enabling a user-managed DNS

<div wrapper="1" role="_abstract">

You can install a cluster with a domain name server (DNS) solution that you manage instead of the default cluster-provisioned DNS solution. As a result, you can manage the API and Ingress DNS records in your own system rather than adding the records to the DNS of the cloud. For example, your organization’s security policies might not allow the use of public DNS services such as Microsoft Azure. In such scenarios, you can use your own DNS service to bypass the public DNS service and manage your own DNS for the IP addresses of the API and Ingress services.

</div>

If you enable user-managed DNS during installation, the installation program provisions DNS records for the API and Ingress services only within the cluster. To ensure access from outside the cluster, you must provision the DNS records in an external DNS service of your choice for the API and Ingress services after installation.

<div>

<div class="title">

Prerequisites

</div>

- You installed the `jq` package.

</div>

<div>

<div class="title">

Procedure

</div>

- Before you deploy your cluster, use a text editor to open the `install-config.yaml` file and add the following stanza:

  - To enable user-managed DNS:

    ``` yaml
    # ...

    platform:
      azure:
        userProvisionedDNS: Enabled
    ```

    where:

    `userProvisionedDNS`
    Enables user-provisioned DNS management.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

For information about provisioning your DNS records for the API server and the Ingress services, see "Provisioning your own DNS records".

</div>

## Sample customized install-config.yaml file for Azure

<div wrapper="1" role="_abstract">

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters.

</div>

> [!IMPORTANT]
> This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it. For a full list and description of all installation configuration parameters, see *Installation configuration parameters for Azure*.

<div class="formalpara">

<div class="title">

Sample `install-config.yaml` file for Azure

</div>

``` yaml
apiVersion: v1
baseDomain: example.com
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
metadata:
  name: example-cluster
controlPlane:
  hyperthreading: Enabled
  name: master
  platform:
    azure:
      type: Standard_D8s_v3
  replicas: 3
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    azure:
      type: Standard_D2s_v3
  replicas: 3
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
platform:
  azure:
    baseDomainResourceGroupName: example-basedomain-resourcegroup-name
    region: centralus
```

</div>

where:

`controlPlane`
Specifies parameters that apply to control plane machines.

`compute`
Specifies parameters that apply to compute machines.

`networking`
Specifies parameters that apply to the cluster networking configuration. If you do not provide networking values, the installation program provides default values.

`platform`
Specifies parameters that apply to the infrastructure platform that hosts the cluster.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Installation configuration parameters for Azure](../../../installing/installing_azure/installation-config-parameters-azure.xml#installation-config-parameters-azure)

</div>

## Configuring the cluster-wide proxy during installation

<div wrapper="1" role="_abstract">

To enable internet access in environments that deny direct connections, configure a cluster-wide proxy in the `install-config.yaml` file. This configuration ensures that the new OpenShift Container Platform cluster routes traffic through the specified HTTP or HTTPS proxy.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You have an existing `install-config.yaml` file.

- You have reviewed the sites that your cluster requires access to and determined whether any of them need to bypass the proxy. By default, all cluster egress traffic is proxied, including calls to hosting cloud provider APIs. You added sites to the `Proxy` object’s `spec.noProxy` field to bypass the proxy if necessary.

  > [!NOTE]
  > The `Proxy` object `status.noProxy` field is populated with the values of the `networking.machineNetwork[].cidr`, `networking.clusterNetwork[].cidr`, and `networking.serviceNetwork[]` fields from your installation configuration.
  >
  > For installations on Amazon Web Services (AWS), Google Cloud, Microsoft Azure, and Red Hat OpenStack Platform (RHOSP), the `Proxy` object `status.noProxy` field is also populated with the instance metadata endpoint (`169.254.169.254`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit your `install-config.yaml` file and add the proxy settings. For example:

    ``` yaml
    apiVersion: v1
    baseDomain: my.domain.com
    proxy:
      httpProxy: http://<username>:<pswd>@<ip>:<port>
      httpsProxy: https://<username>:<pswd>@<ip>:<port>
      noProxy: example.com
    additionalTrustBundle: |
        -----BEGIN CERTIFICATE-----
        <MY_TRUSTED_CA_CERT>
        -----END CERTIFICATE-----
    additionalTrustBundlePolicy: <policy_to_add_additionalTrustBundle>
    # ...
    ```

    where:

    `proxy.httpProxy`
    Specifies a proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be `http`.

    `proxy.httpsProxy`
    Specifies a proxy URL to use for creating HTTPS connections outside the cluster.

    `proxy.noProxy`
    Specifies a comma-separated list of destination domain names, IP addresses, or other network CIDRs to exclude from proxying. Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass the proxy for all destinations.

    `additionalTrustBundle`
    If provided, the installation program generates a config map that is named `user-ca-bundle` in the `openshift-config` namespace to hold the additional CA certificates. If you provide `additionalTrustBundle` and at least one proxy setting, the `Proxy` object is configured to reference the `user-ca-bundle` config map in the `trustedCA` field. The Cluster Network Operator then creates a `trusted-ca-bundle` config map that merges the contents specified for the `trustedCA` parameter with the RHCOS trust bundle. The `additionalTrustBundle` field is required unless the proxy’s identity certificate is signed by an authority from the RHCOS trust bundle.

    `additionalTrustBundlePolicy`
    Specifies the policy that determines the configuration of the `Proxy` object to reference the `user-ca-bundle` config map in the `trustedCA` field. The allowed values are `Proxyonly` and `Always`. Use `Proxyonly` to reference the `user-ca-bundle` config map only when `http/https` proxy is configured. Use `Always` to always reference the `user-ca-bundle` config map. The default value is `Proxyonly`. Optional parameter.

    > [!NOTE]
    > The installation program does not support the proxy `readinessEndpoints` field.

    > [!NOTE]
    > If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example:
    >
    > ``` terminal
    > $ ./openshift-install wait-for install-complete --log-level debug
    > ```

2.  Save the file and reference it when installing OpenShift Container Platform.

    The installation program creates a cluster-wide proxy that is named `cluster` that uses the proxy settings in the provided `install-config.yaml` file. If no proxy settings are provided, a `cluster` `Proxy` object is still created, but it will have a nil `spec`.

    > [!NOTE]
    > Only the `Proxy` object named `cluster` is supported, and no additional proxies can be created.

</div>

# Alternatives to storing administrator-level secrets in the kube-system project

By default, administrator secrets are stored in the `kube-system` project. If you configured the `credentialsMode` parameter in the `install-config.yaml` file to `Manual`, you must use one of the following alternatives:

- To manage long-term cloud credentials manually, follow the procedure in [Manually creating long-term credentials](../../../installing/installing_azure/ipi/installing-restricted-networks-azure-installer-provisioned.xml#manually-create-iam_installing-restricted-networks-azure-installer-provisioned).

- To implement short-term credentials that are managed outside the cluster for individual components, follow the procedures in [Configuring an Azure cluster to use short-term credentials](../../../installing/installing_azure/ipi/installing-restricted-networks-azure-installer-provisioned.xml#installing-azure-with-short-term-creds_installing-restricted-networks-azure-installer-provisioned).

## Manually creating long-term credentials

The Cloud Credential Operator (CCO) can be put into manual mode prior to installation in environments where the cloud identity and access management (IAM) APIs are not reachable, or the administrator prefers not to store an administrator-level credential secret in the cluster `kube-system` namespace.

<div>

<div class="title">

Procedure

</div>

1.  If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

    <div class="formalpara">

    <div class="title">

    Sample configuration file snippet

    </div>

    ``` yaml
    apiVersion: v1
    baseDomain: example.com
    credentialsMode: Manual
    # ...
    ```

    </div>

2.  If you have not previously created installation manifest files, do so by running the following command:

    ``` terminal
    $ openshift-install create manifests --dir <installation_directory>
    ```

    where `<installation_directory>` is the directory in which the installation program creates files.

3.  Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

    ``` terminal
    $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
    ```

4.  Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ oc adm release extract \
      --from=$RELEASE_IMAGE \
      --credentials-requests \
      --included \
      --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
      --to=<path_to_directory_for_credentials_requests>
    ```

    - The `--included` parameter includes only the manifests that your specific cluster configuration requires.

    - Specify the location of the `install-config.yaml` file.

    - Specify the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

      This command creates a YAML file for each `CredentialsRequest` object.

      <div class="formalpara">

      <div class="title">

      Sample `CredentialsRequest` object

      </div>

      ``` yaml
      apiVersion: cloudcredential.openshift.io/v1
      kind: CredentialsRequest
      metadata:
        name: <component_credentials_request>
        namespace: openshift-cloud-credential-operator
        ...
      spec:
        providerSpec:
          apiVersion: cloudcredential.openshift.io/v1
          kind: AzureProviderSpec
          roleBindings:
          - role: Contributor
        ...
      ```

      </div>

5.  Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object.

    <div class="formalpara">

    <div class="title">

    Sample `CredentialsRequest` object with secrets

    </div>

    ``` yaml
    apiVersion: cloudcredential.openshift.io/v1
    kind: CredentialsRequest
    metadata:
      name: <component_credentials_request>
      namespace: openshift-cloud-credential-operator
      ...
    spec:
      providerSpec:
        apiVersion: cloudcredential.openshift.io/v1
        kind: AzureProviderSpec
        roleBindings:
        - role: Contributor
          ...
      secretRef:
        name: <component_secret>
        namespace: <component_namespace>
      ...
    ```

    </div>

    <div class="formalpara">

    <div class="title">

    Sample `Secret` object

    </div>

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: <component_secret>
      namespace: <component_namespace>
    data:
      azure_subscription_id: <base64_encoded_azure_subscription_id>
      azure_client_id: <base64_encoded_azure_client_id>
      azure_client_secret: <base64_encoded_azure_client_secret>
      azure_tenant_id: <base64_encoded_azure_tenant_id>
      azure_resource_prefix: <base64_encoded_azure_resource_prefix>
      azure_resourcegroup: <base64_encoded_azure_resourcegroup>
      azure_region: <base64_encoded_azure_region>
    ```

    </div>

</div>

> [!IMPORTANT]
> Before upgrading a cluster that uses manually maintained credentials, you must ensure that the CCO is in an upgradeable state.

## Configuring an Azure cluster to use short-term credentials

To install a cluster that uses Microsoft Entra Workload ID, you must configure the Cloud Credential Operator utility and create the required Azure resources for your cluster.

### Configuring the Cloud Credential Operator utility

To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary.

> [!NOTE]
> The `ccoctl` utility is a Linux binary that must run in a Linux environment.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform account with cluster administrator access.

- You have installed the OpenShift CLI (`oc`).

</div>

- You have created a global Azure account for the `ccoctl` utility to use with the following permissions:

  - `Microsoft.Resources/subscriptions/resourceGroups/read`

  - `Microsoft.Resources/subscriptions/resourceGroups/write`

  - `Microsoft.Resources/subscriptions/resourceGroups/delete`

  - `Microsoft.Authorization/roleAssignments/read`

  - `Microsoft.Authorization/roleAssignments/delete`

  - `Microsoft.Authorization/roleAssignments/write`

  - `Microsoft.Authorization/roleDefinitions/read`

  - `Microsoft.Authorization/roleDefinitions/write`

  - `Microsoft.Authorization/roleDefinitions/delete`

  - `Microsoft.Storage/storageAccounts/listkeys/action`

  - `Microsoft.Storage/storageAccounts/delete`

  - `Microsoft.Storage/storageAccounts/read`

  - `Microsoft.Storage/storageAccounts/write`

  - `Microsoft.Storage/storageAccounts/blobServices/containers/delete`

  - `Microsoft.Storage/storageAccounts/blobServices/containers/read`

  - `Microsoft.Storage/storageAccounts/blobServices/containers/write`

  - `Microsoft.ManagedIdentity/userAssignedIdentities/delete`

  - `Microsoft.ManagedIdentity/userAssignedIdentities/read`

  - `Microsoft.ManagedIdentity/userAssignedIdentities/write`

  - `Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdentityCredentials/read`

  - `Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdentityCredentials/write`

  - `Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdentityCredentials/delete`

  - `Microsoft.Storage/register/action`

  - `Microsoft.ManagedIdentity/register/action`

<div>

<div class="title">

Procedure

</div>

1.  Set a variable for the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
    ```

2.  Obtain the CCO container image from the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
    ```

    > [!NOTE]
    > Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool.

3.  Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ oc image extract $CCO_IMAGE \
      --file="/usr/bin/ccoctl.<rhel_version>" \
      -a ~/.pull-secret
    ```

    - For `<rhel_version>`, specify the value that corresponds to the version of Red Hat Enterprise Linux (RHEL) that the host uses. If no value is specified, `ccoctl.rhel8` is used by default. The following values are valid:

      - `rhel8`: Specify this value for hosts that use RHEL 8.

      - `rhel9`: Specify this value for hosts that use RHEL 9.

    > [!NOTE]
    > The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`.

4.  Change the permissions to make `ccoctl` executable by running the following command:

    ``` terminal
    $ chmod 775 ccoctl
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example:

  ``` terminal
  $ ./ccoctl
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  OpenShift credentials provisioning tool

  Usage:
    ccoctl [command]

  Available Commands:
    aws          Manage credentials objects for AWS cloud
    azure        Manage credentials objects for Azure
    gcp          Manage credentials objects for Google cloud
    help         Help about any command
    ibmcloud     Manage credentials objects for IBM Cloud
    nutanix      Manage credentials objects for Nutanix

  Flags:
    -h, --help   help for ccoctl

  Use "ccoctl [command] --help" for more information about a command.
  ```

  </div>

</div>

### Creating Azure resources with the Cloud Credential Operator utility

<div wrapper="1" role="_abstract">

You can use the `ccoctl azure create-all` command to automate the creation of Azure resources.

</div>

> [!NOTE]
> By default, `ccoctl` creates objects in the directory in which the commands are run. To create the objects in a different directory, use the `--output-dir` flag. This procedure uses `<path_to_ccoctl_output_dir>` to refer to this directory.

<div class="formalpara">

<div class="title">

Prerequisites

</div>

You must have:

</div>

- Extracted and prepared the `ccoctl` binary.

- Access to your Microsoft Azure account by using the Azure CLI.

<div>

<div class="title">

Procedure

</div>

1.  Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

    ``` terminal
    $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
    ```

2.  Extract the list of `CredentialsRequest` objects from the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ oc adm release extract \
      --from=$RELEASE_IMAGE \
      --credentials-requests \
      --included \
      --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
      --to=<path_to_directory_for_credentials_requests>
    ```

    - The `--included` parameter includes only the manifests that your specific cluster configuration requires.

    - Specify the location of the `install-config.yaml` file.

    - Specify the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

      > [!NOTE]
      > This command might take a few moments to run.

3.  To enable the `ccoctl` utility to detect your Azure credentials automatically, log in to the Azure CLI by running the following command:

    ``` terminal
    $ az login
    ```

4.  Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the following command:

    ``` terminal
    $ ccoctl azure create-all \
      --name=<azure_infra_name> \
      --output-dir=<ccoctl_output_dir> \
      --region=<azure_region> \
      --subscription-id=<azure_subscription_id> \
      --credentials-requests-dir=<path_to_credentials_requests_directory> \
      --dnszone-resource-group-name=<azure_dns_zone_resource_group_name> \
      --tenant-id=<azure_tenant_id> \
      --network-resource-group-name <azure_resource_group> \
      --preserve-existing-roles
    ```

    - Specify the user-defined name for all created Azure resources used for tracking.

    - Optional: Specify the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which the commands are run.

    - Specify the Azure region in which cloud resources will be created.

    - Specify the Azure subscription ID to use.

    - Specify the directory containing the files for the component `CredentialsRequest` objects.

    - Specify the name of the resource group containing the cluster’s base domain Azure DNS zone.

    - Specify the Azure tenant ID to use.

    - Optional: Specify the virtual network resource group if it is different from the cluster resource group.

    - Optional: Specify this flag to ensure that any custom role assignments you define on managed identities are not removed during OpenShift Container Platform updates.

      > [!NOTE]
      > If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.
      >
      > To see additional optional parameters and explanations of how to use them, run the `azure create-all --help` command.

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the OpenShift Container Platform secrets are created, list the files in the `<path_to_ccoctl_output_dir>/manifests` directory:

  ``` terminal
  $ ls <path_to_ccoctl_output_dir>/manifests
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` text
  azure-ad-pod-identity-webhook-config.yaml
  cluster-authentication-02-config.yaml
  openshift-cloud-controller-manager-azure-cloud-credentials-credentials.yaml
  openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
  openshift-cluster-api-capz-manager-bootstrap-credentials-credentials.yaml
  openshift-cluster-csi-drivers-azure-disk-credentials-credentials.yaml
  openshift-cluster-csi-drivers-azure-file-credentials-credentials.yaml
  openshift-image-registry-installer-cloud-credentials-credentials.yaml
  openshift-ingress-operator-cloud-credentials-credentials.yaml
  openshift-machine-api-azure-cloud-credentials-credentials.yaml
  ```

  </div>

  You can verify that the Microsoft Entra ID service accounts are created by querying Azure. For more information, refer to Azure documentation on listing Entra ID service accounts.

</div>

### Incorporating the Cloud Credential Operator utility manifests

To implement short-term security credentials managed outside the cluster for individual components, you must move the manifest files that the Cloud Credential Operator utility (`ccoctl`) created to the correct directories for the installation program.

<div>

<div class="title">

Prerequisites

</div>

- You have configured an account with the cloud platform that hosts your cluster.

- You have configured the Cloud Credential Operator utility (`ccoctl`).

- You have created the cloud provider resources that are required for your cluster with the `ccoctl` utility.

</div>

<div>

<div class="title">

Procedure

</div>

1.  If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

    <div class="formalpara">

    <div class="title">

    Sample configuration file snippet

    </div>

    ``` yaml
    apiVersion: v1
    baseDomain: example.com
    credentialsMode: Manual
    # ...
    ```

    </div>

2.  If you used the `ccoctl` utility to create a new Azure resource group instead of using an existing resource group, modify the `resourceGroupName` parameter in the `install-config.yaml` as shown:

    <div class="formalpara">

    <div class="title">

    Sample configuration file snippet

    </div>

    ``` yaml
    apiVersion: v1
    baseDomain: example.com
    # ...
    platform:
      azure:
        resourceGroupName: <azure_infra_name>
    # ...
    ```

    </div>

    - This value must match the user-defined name for Azure resources that was specified with the `--name` argument of the `ccoctl azure create-all` command.

3.  If you have not previously created installation manifest files, do so by running the following command:

    ``` terminal
    $ openshift-install create manifests --dir <installation_directory>
    ```

    where `<installation_directory>` is the directory in which the installation program creates files.

4.  Copy the manifests that the `ccoctl` utility generated to the `manifests` directory that the installation program created by running the following command:

    ``` terminal
    $ cp /<path_to_ccoctl_output_dir>/manifests/* ./manifests/
    ```

5.  Copy the `tls` directory that contains the private key to the installation directory:

    ``` terminal
    $ cp -a /<path_to_ccoctl_output_dir>/tls .
    ```

</div>

# Deploying the cluster

You can install OpenShift Container Platform on a compatible cloud platform.

> [!IMPORTANT]
> You can run the `create cluster` command of the installation program only once, during initial installation.

<div>

<div class="title">

Prerequisites

</div>

- You have configured an account with the cloud platform that hosts your cluster.

- You have the OpenShift Container Platform installation program and the pull secret for your cluster.

- You have an Azure subscription ID and tenant ID.

</div>

<div>

<div class="title">

Procedure

</div>

- In the directory that contains the installation program, initialize the cluster deployment by running the following command:

  ``` terminal
  $ ./openshift-install create cluster --dir <installation_directory> \
      --log-level=info
  ```

  - For `<installation_directory>`, specify the location of your customized `./install-config.yaml` file.

  - To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

When the cluster deployment completes successfully:

</div>

- The terminal displays directions for accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user.

- Credential information also outputs to `<installation_directory>/.openshift_install.log`.

> [!IMPORTANT]
> Do not delete the installation program or the files that the installation program creates. Both are required to delete the cluster.

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
...
INFO Install complete!
INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
INFO Login to the console with user: "kubeadmin", and password: "password"
INFO Time elapsed: 36m22s
```

</div>

> [!IMPORTANT]
> - The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
>
> - It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

# Provisioning your own DNS records

<div wrapper="1" role="_abstract">

Use the IP address of the API server to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain. Use the IP address of the Ingress service to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

</div>

<div>

<div class="title">

Prerequisite

</div>

- You have installed the Azure CLI client `(az)`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Add the `userProvisionedDNS` parameter to the `install-config.yaml` file and enable the parameter. For more information, see "Enabling a user-managed DNS".

2.  Install your cluster.

3.  If you are installing a private cluster, set the `lb_name` variable by running the following command:

    ``` terminal
    $ lb_name="${infra_id}-internal"
    ```

    1.  Set the `frontendipconfig_id` variable by running the following command:

        ``` terminal
        $ frontendipconfig_id=$(az network lb show -n ${lb_name} -g ${cluster_resource_group_name} -ojson | jq -r ".loadBalancingRules[] | select(.frontendPort == 6443) | .frontendIPConfiguration.id")
        ```

    2.  Set the `frontendipconfig_name` variable by running the following command:

        ``` terminal
        $ frontendipconfig_name=${frontendipconfig_id##*/}
        ```

    3.  To retrieve the IP address of the API service, run the following command:

        ``` terminal
        $ az network lb frontend-ip show -n ${frontendipconfig_name} --lb-name ${lb_name} -g ${cluster_resource_group_name} --query "privateIPAddress" -otsv
        ```

4.  If you are installing a public cluster, set the `lb_name` variable by running the following command:

    ``` terminal
    $ lb_name="${infra_id}"
    ```

    1.  Set the `frontendipconfig_id` variable by running the following command:

        ``` terminal
        $ frontendipconfig_id=$(az network lb show -n ${lb_name} -g ${cluster_resource_group_name} -ojson | jq -r ".loadBalancingRules[] | select(.frontendPort == 6443) | .frontendIPConfiguration.id")
        ```

    2.  Set the `frontendipconfig_name` variable by running the following command:

        ``` terminal
        $ frontendipconfig_name=${frontendipconfig_id##*/}
        ```

    3.  Set the `frontendpublicip_id` variable by running the following command:

        ``` terminal
        $ frontendpublicip_id=$(az network lb frontend-ip show -n ${frontendipconfig_name} --lb-name ${lb_name} -g ${cluster_resource_group_name} --query "publicIPAddress.id" -otsv)
        ```

    4.  To retrieve the IP address of the API service, run the following command:

        ``` terminal
        $ az network public-ip show --ids ${frontendpublicip_id} --query 'ipAddress' -otsv
        ```

5.  Use the IP address and your cluster name and base cluster domain to configure your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname.

6.  If you are installing a private cluster, set the `lb_name` variable by running the following command:

    ``` terminal
    $ lb_name="${infra_id}-internal"
    ```

    1.  Set the `frontendipconfig_id` variable by running the following command:

        ``` terminal
        $ frontendipconfig_id=$(az network lb show -n ${lb_name} -g ${cluster_resource_group_name} -ojson | jq -r ".loadBalancingRules[] | select(.frontendPort == 443) | .frontendIPConfiguration.id")
        ```

    2.  Set the `frontendipconfig_name` variable by running the following command:

        ``` terminal
        $ frontendipconfig_name=${frontendipconfig_id##*/}
        ```

    3.  To retrieve the IP address of the Ingress service, run the following command:

        ``` terminal
        $ az network lb frontend-ip show -n ${frontendipconfig_name} --lb-name ${lb_name} -g ${cluster_resource_group_name} --query "privateIPAddress" -otsv
        ```

7.  If you are installing a public cluster, set the `lb_name` variable by running the following command:

    ``` terminal
    $ lb_name="${infra_id}"
    ```

    1.  Set the `frontendipconfig_id` variable by running the following command:

        ``` terminal
        $ frontendipconfig_id=$(az network lb show -n ${lb_name} -g ${cluster_resource_group_name} -ojson | jq -r ".loadBalancingRules[] | select(.frontendPort == 443) | .frontendIPConfiguration.id")
        ```

    2.  Set the `frontendipconfig_name` variable by running the following command:

        ``` terminal
        $ frontendipconfig_name=${frontendipconfig_id##*/}
        ```

    3.  Set the `frontendpublicip_id` variable by running the following command:

        ``` terminal
        $ frontendpublicip_id=$(az network lb frontend-ip show -n ${frontendipconfig_name} --lb-name ${lb_name} -g ${cluster_resource_group_name} --query "publicIPAddress.id" -otsv)
        ```

    4.  To retrieve the IP address of the Ingress service, run the following command:

        ``` terminal
        $ az network public-ip show --ids ${frontendpublicip_id} --query 'ipAddress' -otsv
        ```

8.  Use the IP address and your cluster name and base cluster domain to configure your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname.

</div>

# Logging in to the cluster by using the CLI

<div wrapper="1" role="_abstract">

To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation.

</div>

The `kubeconfig` file is specific to a cluster and is created during OpenShift Container Platform installation.

<div>

<div class="title">

Prerequisites

</div>

- You deployed an OpenShift Container Platform cluster.

- You installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Export the `kubeadmin` credentials by running the following command:

    ``` terminal
    $ export KUBECONFIG=<installation_directory>/auth/kubeconfig
    ```

    where:

    `<installation_directory>`
    Specifies the path to the directory that stores the installation files.

2.  Verify you can run `oc` commands successfully using the exported configuration by running the following command:

    ``` terminal
    $ oc whoami
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    system:admin
    ```

    </div>

</div>

# Next steps

- [Customize your cluster](../../../post_installation_configuration/cluster-tasks.xml#available_cluster_customizations).

- If necessary, you can [Remote health reporting](../../../support/remote_health_monitoring/remote-health-reporting.xml#remote-health-reporting).
