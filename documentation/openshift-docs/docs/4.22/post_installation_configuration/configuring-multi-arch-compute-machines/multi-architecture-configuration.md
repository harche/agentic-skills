<div wrapper="1" role="_abstract">

An OpenShift Container Platform cluster with multi-architecture compute machines is a cluster that supports compute machines with different architectures.

</div>

Configuring multi-architecture compute machines involves some additional considerations:

- When there are nodes with multiple architectures in your cluster, the architecture of the container image that you deploy to a node must be consistent with the architecture of that node. You need to ensure that the pod is assigned to the node with the appropriate architecture and that it matches the container image architecture. For more information on assigning pods to nodes, see [Assigning pods to nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/).

- In installer-provisioned installations, you are restricted to using the infrastructure provided by a single cloud provider. Adding external nodes, regardless of their architecture, to these clusters is not supported.

- Clusters that are installed with the platform type `none` are unable to use some features, such as managing compute machines with the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that would normally support the feature. This parameter cannot be changed after installation.

  > [!IMPORTANT]
  > Review the information in the [guidelines for deploying OpenShift Container Platform on non-tested platforms](https://access.redhat.com/articles/4207611) before you attempt to install an OpenShift Container Platform cluster in virtualized or cloud environments.

- The Cluster Samples Operator is not supported on clusters with multi-architecture compute machines. Your cluster can be created without this capability. For more information, see [Cluster capabilities](../../installing/overview/cluster-capabilities.xml#cluster-capabilities).

- For information on migrating your single-architecture cluster to a cluster that supports multi-architecture compute machines, see [Migrating to a cluster with multi-architecture compute machines](../../updating/updating_a_cluster/migrating-to-multi-payload.xml#migrating-to-multi-payload).

# Configuring your cluster with multi-architecture compute machines

To create a cluster with multi-architecture compute machines with different installation options and platforms, you can use the documentation in the following table:

<table>
<caption>Cluster with multi-architecture compute machine installation options</caption>
<colgroup>
<col style="width: 37%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Documentation section</th>
<th style="text-align: left;">Platform</th>
<th style="text-align: left;">User-provisioned installation</th>
<th style="text-align: left;">Installer-provisioned installation</th>
<th style="text-align: left;">Control Plane</th>
<th style="text-align: left;">Compute node</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><a href="../../post_installation_configuration/configuring-multi-arch-compute-machines/creating-multi-arch-compute-nodes-azure.xml#creating-multi-arch-compute-nodes-azure">Creating a cluster with multi-architecture compute machines on Azure</a></p></td>
<td style="text-align: left;"><p>Microsoft Azure</p></td>
<td style="text-align: left;"><p>✓</p></td>
<td style="text-align: left;"><p>✓</p></td>
<td style="text-align: left;"><p><code>aarch64</code> or <code>x86_64</code></p></td>
<td style="text-align: left;"><p><code>aarch64</code>, <code>x86_64</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../../post_installation_configuration/configuring-multi-arch-compute-machines/creating-multi-arch-compute-nodes-aws.xml#creating-multi-arch-compute-nodes-aws">Creating a cluster with multi-architecture compute machines on AWS</a></p></td>
<td style="text-align: left;"><p>Amazon Web Services (AWS)</p></td>
<td style="text-align: left;"><p>✓</p></td>
<td style="text-align: left;"><p>✓</p></td>
<td style="text-align: left;"><p><code>aarch64</code> or <code>x86_64</code></p></td>
<td style="text-align: left;"><p><code>aarch64</code>, <code>x86_64</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../../post_installation_configuration/configuring-multi-arch-compute-machines/creating-multi-arch-compute-nodes-google-cloud.xml#creating-multi-arch-compute-nodes-google-cloud">Creating a cluster with multi-architecture compute machines on Google Cloud</a></p></td>
<td style="text-align: left;"><p>Google Cloud</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>✓</p></td>
<td style="text-align: left;"><p><code>aarch64</code> or <code>x86_64</code></p></td>
<td style="text-align: left;"><p><code>aarch64</code>, <code>x86_64</code></p></td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;"><p><a href="../../post_installation_configuration/configuring-multi-arch-compute-machines/creating-multi-arch-compute-nodes-bare-metal.xml#creating-multi-arch-compute-nodes-bare-metal">Creating a cluster with multi-architecture compute machines on bare metal, IBM Power, or IBM Z</a></p></td>
<td style="text-align: left;"><p>Bare metal</p></td>
<td style="text-align: left;"><p>✓</p></td>
<td style="text-align: left;"><p>✓</p></td>
<td style="text-align: left;"><p><code>aarch64</code> or <code>x86_64</code></p></td>
<td style="text-align: left;"><p><code>aarch64</code>, <code>x86_64</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>IBM Power</p></td>
<td style="text-align: left;"><p>✓</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p><code>x86_64</code> or <code>ppc64le</code></p></td>
<td style="text-align: left;"><p><code>x86_64</code>, <code>ppc64le</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>IBM Z</p></td>
<td style="text-align: left;"><p>✓</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p><code>x86_64</code> or <code>s390x</code></p></td>
<td style="text-align: left;"><p><code>x86_64</code>, <code>s390x</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../../post_installation_configuration/configuring-multi-arch-compute-machines/creating-multi-arch-compute-nodes-ibm-z.xml#creating-multi-arch-compute-nodes-ibm-z">Creating a cluster with multi-architecture compute machines on IBM Z® and IBM® LinuxONE with z/VM</a></p></td>
<td style="text-align: left;"><p>IBM Z® and IBM® LinuxONE</p></td>
<td style="text-align: left;"><p>✓</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p><code>x86_64</code></p></td>
<td style="text-align: left;"><p><code>x86_64</code>, <code>s390x</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../../post_installation_configuration/configuring-multi-arch-compute-machines/creating-multi-arch-compute-nodes-ibm-z-kvm.xml#creating-multi-arch-compute-nodes-ibm-z-kvm">Creating a cluster with multi-architecture compute machines on IBM Z® and IBM® LinuxONE with RHEL KVM</a></p></td>
<td style="text-align: left;"><p>IBM Z® and IBM® LinuxONE</p></td>
<td style="text-align: left;"><p>✓</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p><code>x86_64</code></p></td>
<td style="text-align: left;"><p><code>x86_64</code>, <code>s390x</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../../post_installation_configuration/configuring-multi-arch-compute-machines/creating-multi-arch-compute-nodes-ibm-power.xml#creating-multi-arch-compute-nodes-ibm-power">Creating a cluster with multi-architecture compute machines on IBM Power®</a></p></td>
<td style="text-align: left;"><p>IBM Power®</p></td>
<td style="text-align: left;"><p>✓</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p><code>x86_64</code></p></td>
<td style="text-align: left;"><p><code>x86_64</code>, <code>ppc64le</code></p></td>
</tr>
</tbody>
</table>

# Verifying cluster compatibility

Before you can start adding compute nodes of different architectures to your cluster, you must verify that your cluster is multi-architecture compatible.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

- IBM Power only: Ensure that you meet the following prerequisites:

  - When using multiple architectures, hosts for OpenShift Container Platform nodes must share the same storage layer. If they do not have the same storage layer, use a storage provider such as `nfs-provisioner`.

  - You should limit the number of network hops between the compute and control plane as much as possible.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI (`oc`).

2.  You can check that your cluster uses the architecture payload by running the following command:

    ``` terminal
    $ oc adm release info -o jsonpath="{ .metadata.metadata}"
    ```

</div>

<div>

<div class="title">

Verification

</div>

- If you see the following output, your cluster is using the multi-architecture payload:

  ``` terminal
  {
   "release.openshift.io/architecture": "multi",
   "url": "https://access.redhat.com/errata/<errata_version>"
  }
  ```

  You can then begin adding multi-arch compute nodes to your cluster.

- If you see the following output, your cluster is not using the multi-architecture payload:

  ``` terminal
  {
   "url": "https://access.redhat.com/errata/<errata_version>"
  }
  ```

  > [!IMPORTANT]
  > To migrate your cluster so the cluster supports multi-architecture compute machines, follow the procedure in [Migrating to a cluster with multi-architecture compute machines](../../updating/updating_a_cluster/migrating-to-multi-payload.xml#migrating-to-multi-payload).

</div>
