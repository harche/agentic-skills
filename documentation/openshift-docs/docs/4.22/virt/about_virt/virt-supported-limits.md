<div wrapper="1" role="_abstract">

You can refer to tested object maximums when planning your OpenShift Container Platform environment for OpenShift Virtualization. However, approaching the maximum values can reduce performance and increase latency. Ensure that you plan for your specific use case and consider all factors that can impact cluster scaling.

</div>

For more information about cluster configuration and options that impact performance, see the [OpenShift Virtualization - Tuning & Scaling Guide](https://access.redhat.com/articles/6994974) in the Red Hat Knowledgebase.

# Tested maximums for OpenShift Virtualization

<div wrapper="1" role="_abstract">

The following limits apply to a large-scale OpenShift Virtualization 4.x environment. They are based on a single cluster of the largest possible size. When you plan an environment, remember that multiple smaller clusters might be the best option for your use case.

</div>

## Virtual machine maximums

The following maximums apply to virtual machines (VMs) running on OpenShift Virtualization. These values are subject to the limits specified in [Virtualization limits for Red Hat Enterprise Linux with KVM](https://access.redhat.com/articles/rhel-kvm-limits).

| Objective (per VM)  | Tested limit | Theoretical limit |
|---------------------|--------------|-------------------|
| Virtual CPUs        | 216 vCPUs    | 255 vCPUs         |
| Memory              | 6 TB         | 16 TB             |
| Single disk size    | 20 TB        | 100 TB            |
| Hot-pluggable disks | 255 disks    | N/A               |

> [!NOTE]
> Each VM must have at least 512 MB of memory.

## Host maximums

The following maximums apply to the OpenShift Container Platform hosts used for OpenShift Virtualization.

| Objective (per host) | Tested limit | Theoretical limit |
|----|----|----|
| Logical CPU cores or threads | Same as Red Hat Enterprise Linux (RHEL) | N/A |
| RAM | Same as RHEL | N/A |
| Simultaneous live migrations | Defaults to 2 outbound migrations per node, and 5 concurrent migrations per cluster | Depends on NIC bandwidth |
| Live migration bandwidth | No default limit | Depends on NIC bandwidth |

## Cluster maximums

The following maximums apply to objects defined in OpenShift Virtualization.

| Objective (per cluster) | Tested limit | Theoretical limit |
|----|----|----|
| Number of attached PVs per node | N/A | CSI storage provider dependent |
| Maximum PV size | N/A | CSI storage provider dependent |
| Hosts | 500 hosts (100 or fewer recommended) <sup>\[1\]</sup> | Same as OpenShift Container Platform |
| Defined VMs | 10,000 VMs <sup>\[2\]</sup> | Same as OpenShift Container Platform |

1.  If you use more than 100 nodes, consider using Red Hat Advanced Cluster Management (RHACM) to manage multiple clusters instead of scaling out a single control plane. Larger clusters add complexity, require longer updates, and depending on node size and total object density, they can increase control plane stress.

    Using multiple clusters can be beneficial in areas like per-cluster isolation and high availability.

2.  The maximum number of VMs per node depends on the host hardware and resource capacity. It is also limited by the following parameters:

    - Settings that limit the number of pods that can be scheduled to a node. For example: `maxPods`.

    - The default number of KVM devices. For example: `devices.kubevirt.io/kvm: 1k`.

# Additional resources

- [OpenShift Virtualization - Tuning & Scaling Guide](https://access.redhat.com/articles/6994974)

- [Planning your environment according to object maximums](../../scalability_and_performance/planning-your-environment-according-to-object-maximums.xml#planning-your-environment-according-to-object-maximums)

- [Managing the maximum number of pods per node](../../nodes/nodes/nodes-nodes-managing-max-pods.xml#nodes-nodes-managing-max-pods)

- [Red Hat Advanced Cluster Management documentation](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes)
