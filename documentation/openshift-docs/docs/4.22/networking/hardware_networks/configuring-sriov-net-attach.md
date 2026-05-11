<div wrapper="1" role="_abstract">

You can configure an Ethernet network attachment for an Single Root I/O Virtualization (SR-IOV) device in the cluster.

</div>

Before you perform any tasks in the following documentation, ensure that you installed the SR-IOV Network Operator.

# Ethernet device configuration object

You can configure an Ethernet network device by defining an `SriovNetwork` object.

The following YAML describes an `SriovNetwork` object:

``` yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: <name>
  namespace: openshift-sriov-network-operator
spec:
  resourceName: <sriov_resource_name>
  networkNamespace: <target_namespace>
  vlan: <vlan>
  spoofChk: "<spoof_check>"
  ipam: |-
    {}
  linkState: <link_state>
  maxTxRate: <max_tx_rate>
  minTxRate: <min_tx_rate>
  vlanQoS: <vlan_qos>
  trust: "<trust_vf>"
  capabilities: <capabilities>
```

- A name for the object. The SR-IOV Network Operator creates a `NetworkAttachmentDefinition` object with same name.

- The namespace where the SR-IOV Network Operator is installed. You can also install the SR-IOV Network Operator in any namespace.

- The value for the `spec.resourceName` parameter from the `SriovNetworkNodePolicy` object that defines the SR-IOV hardware for this additional network.

- The target namespace for the SriovNetwork object. Only pods in the target namespace can attach to the additional network. When installing the SR-IOV Network Operator in a namespace other than `openshift-sriov-network-operator`, you must not configure this field..

- Optional: Specifies the VLAN ID to assign to an additional network. The default value of `0` means that an additional network has no VLAN ID tag. Supported VLAN ID values range from `1` to `4094`.

- Optional: The spoof check mode of the VF. The allowed values are the strings `"on"` and `"off"`.

  > [!IMPORTANT]
  > You must enclose the value you specify in quotes or the object is rejected by the SR-IOV Network Operator.

- A configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition.

- Optional: The link state of virtual function (VF). Allowed value are `enable`, `disable` and `auto`.

- Optional: A maximum transmission rate, in Mbps, for the VF.

- Optional: A minimum transmission rate, in Mbps, for the VF. This value must be less than or equal to the maximum transmission rate.

  > [!NOTE]
  > Intel NICs do not support the `minTxRate` parameter. For more information, see [BZ#1772847](https://bugzilla.redhat.com/show_bug.cgi?id=1772847).

- Optional: An IEEE 802.1p priority level for the VF. The default value is `0`.

- Optional: The trust mode of the VF. The allowed values are the strings `"on"` and `"off"`.

  > [!IMPORTANT]
  > You must enclose the value that you specify in quotes, or the SR-IOV Network Operator rejects the object.

- Optional: The capabilities to configure for this additional network. You can specify `'{ "ips": true }'` to enable IP address support or `'{ "mac": true }'` to enable MAC address support.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Installing the SR-IOV Network Operator](../../networking/networking_operators/sr-iov-operator/installing-sriov-operator.xml#installing-sriov-operator)

- [Configuring namespaced SR-IOV resources](../../networking/hardware_networks/configuring-namespaced-sriov-resources.xml#introduction-to-namespaced-sriovnetwork-resources_configuring-namespaced-sriov-resources)

</div>

## Creating a configuration for assignment of dual-stack IP addresses dynamically

<div wrapper="1" role="_abstract">

You can dynamically assign dual-stack IP addresses to a secondary network so that pods can communicate over both IPv4 and IPv6 addresses.

</div>

You can configure the following IP address assignment types in the `ipRanges` parameter:

- IPv4 addresses

- IPv6 addresses

- multiple IP address assignment

<div>

<div class="title">

Procedure

</div>

1.  Set `type` to `whereabouts`.

2.  Use `ipRanges` to allocate IP addresses as shown in the following example:

    ``` yaml
    cniVersion: operator.openshift.io/v1
    kind: Network
    metadata:
      name: cluster
    spec:
      additionalNetworks:
      - name: whereabouts-shim
        namespace: default
        type: Raw
        rawCNIConfig: |-
          {
           "name": "whereabouts-dual-stack",
           "cniVersion": "0.3.1,
           "type": "bridge",
           "ipam": {
             "type": "whereabouts",
             "ipRanges": [
                      {"range": "192.168.10.0/24"},
                      {"range": "2001:db8::/64"}
                  ]
           }
          }
    ```

3.  Attach the secondary network to a pod. For more information, see "Adding a pod to a secondary network".

</div>

<div>

<div class="title">

Verification

</div>

- Verify that all IP addresses got assigned to the network interfaces within the network namespace of a pod by entering the following command:

  ``` yaml
  $ oc exec -it <pod_name> -- ip a
  ```

  where:

  `<podname>`
  The name of the pod.

</div>

## Configuration of IP address assignment for a network attachment

<div wrapper="1" role="_abstract">

For secondary networks, you can assign IP addresses by using an IP Address Management (IPAM) CNI plugin, which supports various assignment methods, including Dynamic Host Configuration Protocol (DHCP) and static assignment.

</div>

The DHCP IPAM CNI plugin responsible for dynamic assignment of IP addresses operates with two distinct components:

- CNI Plugin: Responsible for integrating with the Kubernetes networking stack to request and release IP addresses.

- DHCP IPAM CNI Daemon: A listener for DHCP events that coordinates with existing DHCP servers in the environment to handle IP address assignment requests. This daemon is not a DHCP server itself.

For networks requiring `type: dhcp` in their IPAM configuration, ensure the DHCP server meets the following conditions:

- A DHCP server is available and running in the environment.

- The DHCP server is external to the cluster and you expect the server to form part of the existing network infrastructure for the customer.

- The DHCP server is appropriately configured to serve IP addresses to the nodes.

In cases where a DHCP server is unavailable in the environment, consider using the Whereabouts IPAM CNI plugin. The Whereabouts CNI provides similar IP address management capabilities without the need for an external DHCP server.

> [!NOTE]
> Use the Whereabouts CNI plugin when no external DHCP server exists or where static IP address management is preferred. The Whereabouts plugin includes a reconciler daemon to manage stale IP address allocations.

Ensure the periodic renewal of a DHCP lease throughout the lifetime of a container by including a separate daemon, the DHCP IPAM CNI Daemon. To deploy the DHCP IPAM CNI daemon, change the Cluster Network Operator (CNO) configuration to trigger the deployment of this daemon as part of the secondary network setup.

### Static IP address assignment configuration

The following table describes the configuration for static IP address assignment:

| Field | Type | Description |
|----|----|----|
| `type` | `string` | The IPAM address type. The value `static` is required. |
| `addresses` | `array` | An array of objects specifying IP addresses to assign to the virtual interface. Both IPv4 and IPv6 IP addresses are supported. |
| `routes` | `array` | An array of objects specifying routes to configure inside the pod. |
| `dns` | `array` | Optional: An array of objects specifying the DNS configuration. |

`ipam` static configuration object

The `addresses` array requires objects with the following fields:

| Field | Type | Description |
|----|----|----|
| `address` | `string` | An IP address and network prefix that you specify. For example, if you specify `10.10.21.10/24`, the secondary network gets assigned an IP address of `10.10.21.10` and the netmask of `255.255.255.0`. |
| `gateway` | `string` | The default gateway to route egress network traffic to. |

`ipam.addresses[]` array

| Field | Type | Description |
|----|----|----|
| `dst` | `string` | The IP address range in CIDR format, such as `192.168.17.0/24` or `0.0.0.0/0` for the default route. |
| `gw` | `string` | The gateway that routes network traffic. |

`ipam.routes[]` array

| Field | Type | Description |
|----|----|----|
| `nameservers` | `array` | An array of one or more IP addresses where DNS queries get sent. |
| `domain` | `array` | The default domain to append to a hostname. For example, if the domain is set to `example.com`, a DNS lookup query for `example-host` is rewritten as `example-host.example.com`. |
| `search` | `array` | An array of domain names to append to an unqualified hostname, such as `example-host`, during a DNS lookup query. |

`ipam.dns` object

<div class="formalpara">

<div class="title">

Static IP address assignment configuration example

</div>

``` json
{
  "ipam": {
    "type": "static",
      "addresses": [
        {
          "address": "191.168.1.7/24"
        }
      ]
  }
}
```

</div>

### Dynamic IP address (DHCP) assignment configuration

A pod obtains its original DHCP lease when the pod gets created. The lease must be periodically renewed by a minimal DHCP server deployment running on the cluster.

> [!IMPORTANT]
> For an Ethernet network attachment, the SR-IOV Network Operator does not create a DHCP server deployment; the Cluster Network Operator is responsible for creating the minimal DHCP server deployment.

To trigger the deployment of the DHCP server, you must create a shim network attachment by editing the Cluster Network Operator configuration, as in the following example:

<div class="formalpara">

<div class="title">

Example shim network attachment definition

</div>

``` yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  additionalNetworks:
  - name: dhcp-shim
    namespace: default
    type: Raw
    rawCNIConfig: |-
      {
        "name": "dhcp-shim",
        "cniVersion": "0.3.1",
        "type": "bridge",
        "ipam": {
          "type": "dhcp"
        }
      }
  # ...
```

</div>

where:

`type`
Specifies dynamic IP address assignment for the cluster.

## Dynamic IP address assignment configuration with Whereabouts

<div wrapper="1" role="_abstract">

The Whereabouts CNI plugin helps the dynamic assignment of an IP address to a secondary network without the use of a DHCP server.

</div>

The Whereabouts CNI plugin also supports overlapping IP address ranges and configuration of the same CIDR range multiple times within separate `NetworkAttachmentDefinition` CRDs. This provides greater flexibility and management capabilities in multitenant environments.

### Dynamic IP address configuration parameters

The following table describes the configuration objects for dynamic IP address assignment with Whereabouts:

| Field | Type | Description |
|----|----|----|
| `type` | `string` | The IPAM address type. The value `whereabouts` is required. |
| `range` | `string` | An IP address and range in CIDR notation. IP addresses are assigned from within this range of addresses. |
| `exclude` | `array` | Optional: A list of zero or more IP addresses and ranges in CIDR notation. IP addresses within an excluded address range are not assigned. |
| `network_name` | `string` | Optional: Helps ensure that each group or domain of pods gets its own set of IP addresses, even if they share the same range of IP addresses. Setting this field is important for keeping networks separate and organized, notably in multi-tenant environments. |

`ipam` whereabouts configuration parameters

### Dynamic IP address assignment configuration with Whereabouts that excludes IP address ranges

The following example shows a dynamic address assignment configuration in a NAD file that uses Whereabouts:

<div class="formalpara">

<div class="title">

Whereabouts dynamic IP address assignment that excludes specific IP address ranges

</div>

``` json
{
  "ipam": {
    "type": "whereabouts",
    "range": "192.0.2.192/27",
    "exclude": [
       "192.0.2.192/30",
       "192.0.2.196/32"
    ]
  }
}
```

</div>

### Dynamic IP address assignment that uses Whereabouts with overlapping IP address ranges

The following example shows a dynamic IP address assignment that uses overlapping IP address ranges for multitenant networks.

<div class="formalpara">

<div class="title">

NetworkAttachmentDefinition 1

</div>

``` json
{
  "ipam": {
    "type": "whereabouts",
    "range": "192.0.2.192/29",
    "network_name": "example_net_common",
  }
}
```

</div>

where:

`network_name`
Optional parameter. If set, must match the `network_name` of `NetworkAttachmentDefinition 2`.

<div class="formalpara">

<div class="title">

NetworkAttachmentDefinition 2

</div>

``` json
{
  "ipam": {
    "type": "whereabouts",
    "range": "192.0.2.192/24",
    "network_name": "example_net_common",
  }
}
```

</div>

where:

`network_name`
Optional parameter. If set, must match the `network_name` of `NetworkAttachmentDefinition 1`.

# Configuring SR-IOV additional network

<div wrapper="1" role="_abstract">

You can configure an additional network that uses SR-IOV hardware by creating an `SriovNetwork` object. When you create an `SriovNetwork` object, the SR-IOV Network Operator automatically creates a `NetworkAttachmentDefinition` object.

</div>

> [!NOTE]
> Do not modify or delete an `SriovNetwork` object if it is attached to any pods in a `running` state.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `SriovNetwork` object, and then save the YAML in the `<name>.yaml` file, where `<name>` is a name for this additional network. The object specification might resemble the following example:

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetwork
    metadata:
      name: attach1
      namespace: openshift-sriov-network-operator
    spec:
      resourceName: net1
      networkNamespace: project2
      ipam: |-
        {
          "type": "host-local",
          "subnet": "10.56.217.0/24",
          "rangeStart": "10.56.217.171",
          "rangeEnd": "10.56.217.181",
          "gateway": "10.56.217.1"
        }
    ```

2.  To create the object, enter the following command:

    ``` terminal
    $ oc create -f <name>.yaml
    ```

    where:

    `<name>`
    Specifies the name of the additional network.

3.  Optional: To confirm that the `NetworkAttachmentDefinition` object that is associated with the `SriovNetwork` object that you created in the previous step exists, enter the following command. Replace `<namespace>` with the `networkNamespace` value you specified in the `SriovNetwork` object.

    ``` terminal
    $ oc get net-attach-def -n <namespace>
    ```

</div>

# Assigning an SR-IOV network to a VRF

As a cluster administrator, you can assign an SR-IOV network interface to your VRF domain by using the CNI VRF plugin.

To do this, add the VRF configuration to the optional `metaPlugins` parameter of the `SriovNetwork` resource.

> [!NOTE]
> Applications that use VRFs need to bind to a specific device. The common usage is to use the `SO_BINDTODEVICE` option for a socket. `SO_BINDTODEVICE` binds the socket to a device that is specified in the passed interface name, for example, `eth1`. To use `SO_BINDTODEVICE`, the application must have `CAP_NET_RAW` capabilities.
>
> Using a VRF through the `ip vrf exec` command is not supported in OpenShift Container Platform pods. To use VRF, bind applications directly to the VRF interface.

## Creating an additional SR-IOV network attachment with the CNI VRF plugin

<div wrapper="1" role="_abstract">

The SR-IOV Network Operator manages additional network definitions. When you specify an additional SR-IOV network to create, the SR-IOV Network Operator creates the `NetworkAttachmentDefinition` custom resource (CR) automatically.

</div>

> [!NOTE]
> Do not edit `NetworkAttachmentDefinition` custom resources that the SR-IOV Network Operator manages. Doing so might disrupt network traffic on your additional network.

To create an additional SR-IOV network attachment with the CNI virtual routing and forwarding (VRF) plugin, perform the following procedure.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in to the OpenShift Container Platform cluster as a user with cluster-admin privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `SriovNetwork` custom resource (CR) for the additional SR-IOV network attachment and insert the `metaPlugins` configuration, as in the following example CR. Save the YAML as the file `sriov-network-attachment.yaml`.

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetwork
    metadata:
      name: example-network
      namespace: additional-sriov-network-1
    spec:
      ipam: |
        {
          "type": "host-local",
          "subnet": "10.56.217.0/24",
          "rangeStart": "10.56.217.171",
          "rangeEnd": "10.56.217.181",
          "routes": [{
            "dst": "0.0.0.0/0"
          }],
          "gateway": "10.56.217.1"
        }
      vlan: 0
      resourceName: intelnics
      metaPlugins : |
        {
          "type": "vrf",
          "vrfname": "example-vrf-name"
        }
    ```

    where:

    `metaPlugins.type`
    Set the `type` parameter to `vrf`.

    `metaPlugins.vrfname`
    Specify a name for the VRF in the `vrfname` parameter. An interface gets assigned to the VRF. If you do not specify a name for the VRF in a pod, the SR-IOV Network Operator automatically generates a name for the VRF.

2.  Create the `SriovNetwork` resource:

    ``` terminal
    $ oc create -f sriov-network-attachment.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Confirm that the SR-IOV Network Operator created the `NetworkAttachmentDefinition` CR by running the following command. The expected output shows the name of the NAD CR and the creation age in minutes.

    ``` terminal
    $ oc get network-attachment-definitions -n <namespace>
    ```

    - `<namespace>`: Replace `<namespace>` with the namespace that you specified when configuring the network attachment, for example, `additional-sriov-network-1`.

      > [!NOTE]
      > There might be a delay before the SR-IOV Network Operator creates the CR.

2.  To verify that the VRF CNI is correctly configured and that the additional SR-IOV network attachment is attached, do the following:

    1.  Create an SR-IOV network that uses the VRF CNI.

    2.  Assign the network to a pod.

    3.  Verify that the pod network attachment connects to the SR-IOV additional network. Ensure that you remote shell login into the pod and run the following command. The expected output shows the name of the VRF interface and its unique ID in the routing table.

        ``` terminal
        $ ip vrf show
        ```

    4.  Confirm that the VRF interface is `master` for the secondary interface by running the following command. Example output shows `5: net1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master red state UP mode`.

        ``` terminal
        $ ip link
        ```

</div>

# Runtime configuration for an Ethernet-based SR-IOV attachment

<div wrapper="1" role="_abstract">

When attaching a pod to an additional network, you can specify a runtime configuration to make specific customizations for the pod. For example, you can request a specific MAC hardware address.

</div>

You specify the runtime configuration by setting an annotation in the pod specification. The annotation key is `k8s.v1.cni.cncf.io/networks`, and it accepts a JSON object that describes the runtime configuration.

<div class="formalpara">

<div class="title">

Example runtime configuration for an Ethernet-based SR-IOV network attachment

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: sample-pod
  annotations:
    k8s.v1.cni.cncf.io/networks: |-
      [
        {
          "name": "<network_attachment>",
          "mac": "<mac_address>",
          "ips": ["<cidr_range>"]
        }
      ]
spec:
  containers:
  - name: sample-container
    image: <image>
    imagePullPolicy: IfNotPresent
    command: ["sleep", "infinity"]
```

</div>

where:

`k8s.v1.cni.cncf.io/networks.name`
The name of the SR-IOV network attachment definition CR. Example value is `ibl`.

`k8s.v1.cni.cncf.io/networks.mac`
Optional parameter. The MAC address for the SR-IOV device that is allocated from the resource type defined in the SR-IOV network attachment definition CR. To use this feature, you also must specify `{ "mac": true }` in the `SriovNetwork` object. Example value is `c2:11:22:33:44:55:66:77`.

`k8s.v1.cni.cncf.io/networks.ips`
Optional parameter. IP addresses for the SR-IOV device that is allocated from the resource type defined in the SR-IOV network attachment definition CR. Both IPv4 and IPv6 addresses are supported. To use this feature, you also must specify `{ "ips": true }` in the `SriovNetwork` object. Example value is `192.168.10.1/24", "2001::1/64`.

# Adding a pod to a secondary network

<div wrapper="1" role="_abstract">

To enable a pod to use additional network interfaces in OpenShift Container Platform, you can attach the pod to a secondary network. The pod continues to send normal cluster-related network traffic over the default network.

</div>

When a pod is created, a secondary network is attached to the pod. However, if a pod already exists, you cannot attach a secondary network to it.

The pod must be in the same namespace as the secondary network.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in to the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Add an annotation to the `Pod` object. Only one of the following annotation formats can be used:

    1.  To attach a secondary network without any customization, add an annotation with the following format:

        ``` yaml
        metadata:
          annotations:
            k8s.v1.cni.cncf.io/networks: <network>[,<network>,...]
        ```

        where:

        `k8s.v1.cni.cncf.io/networks`
        Specifies the name of the secondary network to associate with the pod. To specify more than one secondary network, separate each network with a comma. Do not include whitespace between the comma. If you specify the same secondary network multiple times, that pod will have multiple network interfaces attached to that network.

    2.  To attach a secondary network with customizations, add an annotation with the following format:

        ``` yaml
        metadata:
          annotations:
            k8s.v1.cni.cncf.io/networks: |-
              [
                {
                  "name": "<network>",
                  "namespace": "<namespace>",
                  "default-route": ["<default_route>"]
                }
              ]
        ```

        where:

        `<network>`
        Specifies the name of the secondary network defined by a `NetworkAttachmentDefinition` object.

        `<namespace>`
        Specifies the namespace where the `NetworkAttachmentDefinition` object is defined.

        `<default-route>`
        Optional parameter. Specifies an override for the default route, such as `192.168.17.1`.

2.  Create the pod by entering the following command.

    ``` terminal
    $ oc create -f <name>.yaml
    ```

    Replace `<name>` with the name of the pod.

3.  Optional: Confirm that the annotation exists in the `pod` CR by entering the following command. Replace `<name>` with the name of the pod.

    ``` terminal
    $ oc get pod <name> -o yaml
    ```

    In the following example, the `example-pod` pod is attached to the `net1` secondary network:

    ``` terminal
    $ oc get pod example-pod -o yaml
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        k8s.v1.cni.cncf.io/networks: macvlan-bridge
        k8s.v1.cni.cncf.io/network-status: |-
          [{
              "name": "ovn-kubernetes",
              "interface": "eth0",
              "ips": [
                  "10.128.2.14"
              ],
              "default": true,
              "dns": {}
          },{
              "name": "macvlan-bridge",
              "interface": "net1",
              "ips": [
                  "20.2.2.100"
              ],
              "mac": "22:2f:60:a5:f8:00",
              "dns": {}
          }]
      name: example-pod
      namespace: default
    spec:
      ...
    status:
      ...
    ```

    where:

    `k8s.v1.cni.cncf.io/network-status`
    Specifies a JSON array of objects. Each object describes the status of a secondary network attached to the pod. The annotation value is stored as a plain text value.

</div>

## Exposing MTU for vfio-pci SR-IOV devices to pod

<div wrapper="1" role="_abstract">

After adding a pod to an additional network, you can check that the MTU is available for the SR-IOV network.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check that the pod annotation includes MTU by running the following command:

    ``` terminal
    $ oc describe pod example-pod
    ```

    The following example shows the sample output:

    ``` text
    "mac": "20:04:0f:f1:88:01",
           "mtu": 1500,
           "dns": {},
           "device-info": {
             "type": "pci",
             "version": "1.1.0",
             "pci": {
               "pci-address": "0000:86:01.3"
        }
      }
    ```

2.  Verify that the MTU is available in `/etc/podnetinfo/` inside the pod by running the following command:

    ``` terminal
    $ oc exec example-pod -n sriov-tests -- cat /etc/podnetinfo/annotations | grep mtu
    ```

    The following example shows the sample output:

    ``` text
    k8s.v1.cni.cncf.io/network-status="[{
        \"name\": \"ovn-kubernetes\",
        \"interface\": \"eth0\",
        \"ips\": [
            \"10.131.0.67\"
        ],
        \"mac\": \"0a:58:0a:83:00:43\",
        \"default\": true,
        \"dns\": {}
        },{
        \"name\": \"sriov-tests/sriov-nic-1\",
        \"interface\": \"net1\",
        \"ips\": [
            \"192.168.10.1\"
        ],
        \"mac\": \"20:04:0f:f1:88:01\",
        \"mtu\": 1500,
        \"dns\": {},
        \"device-info\": {
            \"type\": \"pci\",
            \"version\": \"1.1.0\",
            \"pci\": {
                \"pci-address\": \"0000:86:01.3\"
            }
        }
        }]"
    ```

</div>

# Configuring parallel node draining during SR-IOV network policy updates

<div wrapper="1" role="_abstract">

By default, the SR-IOV Network Operator drains workloads from a node before every policy change. The Operator performs this action, one node at a time, to ensure that the reconfiguration does not impact workloads.

</div>

In large clusters, draining nodes sequentially can be time-consuming, taking hours or even days. In time-sensitive environments, you can enable parallel node draining in an `SriovNetworkPoolConfig` custom resource (CR) for faster rollouts of SR-IOV network configurations.

To configure parallel draining, use the `SriovNetworkPoolConfig` CR to create a node pool. You can then add nodes to the pool and define the maximum number of nodes in the pool that the Operator can drain in parallel. With this approach, you can enable parallel draining for faster reconfiguration while ensuring you still have enough nodes remaining in the pool to handle any running workloads.

> [!NOTE]
> A node can only belong to one SR-IOV network pool configuration. If a node is not part of a pool, the node gets added to a virtual, default, pool that with a configuration for draining one node at a time only.
>
> The node might restart during the draining process.

The procedure requires that you create SR-IOV resources and then parallel drain the nodes.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the SR-IOV Network Operator.

- Nodes have hardware that support SR-IOV.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file that defines the `SriovNetworkPoolConfig` resource:

    <div class="formalpara">

    <div class="title">

    Example `sriov-nw-pool.yaml` file

    </div>

    ``` yaml
    apiVersion: v1
    kind: SriovNetworkPoolConfig
    metadata:
      name: pool-1
      namespace: openshift-sriov-network-operator
    spec:
      maxUnavailable: 2
      nodeSelector:
        matchLabels:
          node-role.kubernetes.io/worker: ""
    ```

    </div>

    where:

    `name`
    Specify the name of the `SriovNetworkPoolConfig` object.

    `namespace`
    Specify namespace where the SR-IOV Network Operator is installed.

    `maxUnavailable`
    Specify an integer number, or percentage value, for nodes that can be unavailable in the pool during an update. For example, if you have 10 nodes and you set the maximum unavailable to 2, then only 2 nodes can be drained in parallel at any time, leaving 8 nodes for handling workloads.

    `nodeSelector`
    Specify the nodes to add the pool by using the node selector. This example adds all nodes with the `worker` role to the pool.

2.  Create the `SriovNetworkPoolConfig` resource by running the following command:

    ``` terminal
    $ oc create -f sriov-nw-pool.yaml
    ```

3.  Create the `sriov-test` namespace by running the following comand:

    ``` terminal
    $ oc create namespace sriov-test
    ```

4.  Create a YAML file that defines the `SriovNetworkNodePolicy` resource, as demonstrated in the following example YAML file:

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetworkNodePolicy
    metadata:
      name: sriov-nic-1
      namespace: openshift-sriov-network-operator
    spec:
      deviceType: netdevice
      nicSelector:
        pfNames: ["ens1"]
      nodeSelector:
        node-role.kubernetes.io/worker: ""
      numVfs: 5
      priority: 99
      resourceName: sriov_nic_1
    ```

5.  Create the `SriovNetworkNodePolicy` resource by running the following command:

    ``` terminal
    $ oc create -f sriov-node-policy.yaml
    ```

6.  Create a YAML file that defines the `SriovNetwork` resource:

    <div class="formalpara">

    <div class="title">

    Example `sriov-network.yaml` file

    </div>

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetwork
    metadata:
      name: sriov-nic-1
      namespace: openshift-sriov-network-operator
    spec:
      linkState: auto
      networkNamespace: sriov-test
      resourceName: sriov_nic_1
      capabilities: '{ "mac": true, "ips": true }'
      ipam: '{ "type": "static" }'
    ```

    </div>

7.  Create the `SriovNetwork` resource by running the following command:

    ``` terminal
    $ oc create -f sriov-network.yaml
    ```

8.  View the node pool you created by running the following command:

    ``` terminal
    $ oc get sriovNetworkpoolConfig -n openshift-sriov-network-operator
    ```

    Expected output shows the name of the node pool, such as `pool-1`, that includes all the node that have the `worker` role and the age of the node pool in seconds, such as `67s`.

9.  Update the number of virtual functions in the `SriovNetworkNodePolicy` resource to trigger workload draining in the cluster:

    ``` terminal
    $ oc patch SriovNetworkNodePolicy sriov-nic-1 -n openshift-sriov-network-operator --type merge -p '{"spec": {"numVfs": 4}}'
    ```

10. Check the draining status on the target cluster by running the following command:

    ``` terminal
    $ oc get sriovNetworkNodeState -n openshift-sriov-network-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAMESPACE                          NAME       SYNC STATUS   DESIRED SYNC STATE   CURRENT SYNC STATE   AGE
    openshift-sriov-network-operator   worker-0   InProgress    Drain_Required       DrainComplete        3d10h
    openshift-sriov-network-operator   worker-1   InProgress    Drain_Required       DrainComplete        3d10h
    ```

    </div>

    When the draining process completes, the `SYNC STATUS` changes to `Succeeded`, and the `DESIRED SYNC STATE` and `CURRENT SYNC STATE` values return to `IDLE`.

</div>

# Excluding the SR-IOV network topology for NUMA-aware scheduling

To exclude advertising the SR-IOV network resource’s Non-Uniform Memory Access (NUMA) node to the Topology Manager, you can configure the `excludeTopology` specification in the `SriovNetworkNodePolicy` custom resource. Use this configuration for more flexible SR-IOV network deployments during NUMA-aware pod scheduling.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have configured the CPU Manager policy to `static`. For more information about CPU Manager, see the *Additional resources* section.

- You have configured the Topology Manager policy to `single-numa-node`.

- You have installed the SR-IOV Network Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `SriovNetworkNodePolicy` CR:

    1.  Save the following YAML in the `sriov-network-node-policy.yaml` file, replacing values in the YAML to match your environment:

        ``` yaml
        apiVersion: sriovnetwork.openshift.io/v1
        kind: SriovNetworkNodePolicy
        metadata:
          name: <policy_name>
          namespace: openshift-sriov-network-operator
        spec:
          resourceName: sriovnuma0
          nodeSelector:
            kubernetes.io/hostname: <node_name>
          numVfs: <number_of_Vfs>
          nicSelector:
            vendor: "<vendor_ID>"
            deviceID: "<device_ID>"
          deviceType: netdevice
          excludeTopology: true
        ```

        - The resource name of the SR-IOV network device plugin. This YAML uses a sample `resourceName` value.

        - Identify the device for the Operator to configure by using the network interface controller (NIC selector).

        - To exclude advertising the NUMA node for the SR-IOV network resource to the Topology Manager, set the value to `true`. The default value is `false`.

          > [!NOTE]
          > If many `SriovNetworkNodePolicy` resources target the same SR-IOV network resource, the `SriovNetworkNodePolicy` resources must have the same value as the `excludeTopology` specification. Otherwise, the conflicting policy is rejected.

    2.  Create the `SriovNetworkNodePolicy` resource by running the following command. Successful output lists the name of the `SriovNetworkNodePolicy` resource and the `created` status.

        ``` terminal
        $ oc create -f sriov-network-node-policy.yaml
        ```

2.  Create the `SriovNetwork` CR:

    1.  Save the following YAML in the `sriov-network.yaml` file, replacing values in the YAML to match your environment:

        ``` yaml
        apiVersion: sriovnetwork.openshift.io/v1
        kind: SriovNetwork
        metadata:
          name: sriov-numa-0-network
          namespace: openshift-sriov-network-operator
        spec:
          resourceName: sriovnuma0
          networkNamespace: <namespace>
          ipam: |-
            {
              "type": "<ipam_type>",
            }
        ```

        - Replace `sriov-numa-0-network` with the name for the SR-IOV network resource.

        - Specify the resource name for the `SriovNetworkNodePolicy` CR from the previous step. This YAML uses a sample `resourceName` value.

        - Enter the namespace for your SR-IOV network resource.

        - Enter the IP address management configuration for the SR-IOV network.

    2.  Create the `SriovNetwork` resource by running the following command. Successful output lists the name of the `SriovNetwork` resource and the `created` status.

        ``` terminal
        $ oc create -f sriov-network.yaml
        ```

3.  Create a pod and assign the SR-IOV network resource from the previous step:

    1.  Save the following YAML in the `sriov-network-pod.yaml` file, replacing values in the YAML to match your environment:

        ``` yaml
        apiVersion: v1
        kind: Pod
        metadata:
          name: <pod_name>
          annotations:
            k8s.v1.cni.cncf.io/networks: |-
              [
                {
                  "name": "sriov-numa-0-network",
                }
              ]
        spec:
          containers:
          - name: <container_name>
            image: <image>
            imagePullPolicy: IfNotPresent
            command: ["sleep", "infinity"]
        ```

        - This is the name of the `SriovNetwork` resource that uses the `SriovNetworkNodePolicy` resource.

    2.  Create the `Pod` resource by running the following command. The expected output shows the name of the `Pod` resource and the `created` status.

        ``` terminal
        $ oc create -f sriov-network-pod.yaml
        ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify the status of the pod by running the following command, replacing `<pod_name>` with the name of the pod:

    ``` terminal
    $ oc get pod <pod_name>
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                     READY   STATUS    RESTARTS   AGE
    test-deployment-sriov-76cbbf4756-k9v72   1/1     Running   0          45h
    ```

    </div>

2.  Open a debug session with the target pod to verify that the SR-IOV network resources are deployed to a different node than the memory and CPU resources.

    1.  Open a debug session with the pod by running the following command, replacing \<pod_name\> with the target pod name.

        ``` terminal
        $ oc debug pod/<pod_name>
        ```

    2.  Set `/host` as the root directory within the debug shell. The debug pod mounts the root file system from the host in `/host` within the pod. By changing the root directory to `/host`, you can run binaries from the host file system:

        ``` terminal
        $ chroot /host
        ```

    3.  View information about the CPU allocation by running the following commands:

        ``` terminal
        $ lscpu | grep NUMA
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NUMA node(s):                    2
        NUMA node0 CPU(s):     0,2,4,6,8,10,12,14,16,18,...
        NUMA node1 CPU(s):     1,3,5,7,9,11,13,15,17,19,...
        ```

        </div>

        ``` terminal
        $ cat /proc/self/status | grep Cpus
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        Cpus_allowed:    ffff
        Cpus_allowed_list:  1,3,5,7
        ```

        </div>

        The expected output shows the CPUs (1, 3, 5, and 7) that get allocated to a `NUMA` node, such as `NUMA node1`. The SR-IOV network resource can use the NIC from another `NUMA` node, such as `NUMA node0`. Note that the `ffff` hexadecimal value represents the CPU cores that run a process.

        ``` terminal
        $ cat  /sys/class/net/net1/device/numa_node
        ```

        Expected output shows the number for the `NUMA` node, such as `0`.

        > [!NOTE]
        > If you set the `excludeTopology` specification to `True`, the required resources might exist in the same NUMA node.

</div>

# Additional resources

- [Configuring an SR-IOV network device](../../networking/hardware_networks/configuring-sriov-device.xml#configuring-sriov-device)

- [Using CPU Manager](../../scalability_and_performance/using-cpu-manager.xml#using-cpu-manager)
