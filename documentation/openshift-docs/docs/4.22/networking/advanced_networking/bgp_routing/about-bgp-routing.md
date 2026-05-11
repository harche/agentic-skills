<div wrapper="1" role="_abstract">

Learn about the Border Gateway Protocol (BGP) routing capabilities available in the cluster, including implementation and configuration of BGP by using FRR-K8s resources. Take into account key considerations for using the MetalLB Operator, including required migration of existing `FRRConfiguration` custom resources to the `openshift-frr-k8s` namespace to ensure compatibility with current implementations.

</div>

This feature provides native BGP routing capabilities for the cluster.

> [!IMPORTANT]
> If you are using the MetalLB Operator and there are existing `FRRConfiguration` CRs in the `metallb-system` namespace created by cluster administrators or third-party cluster components other than the MetalLB Operator, you must ensure that they are copied to the `openshift-frr-k8s` namespace or that those third-party cluster components use the new namespace. For more information, see "Migrating FRR-K8s resources".

# About Border Gateway Protocol (BGP) routing

<div wrapper="1" role="_abstract">

To enable external routing for your cluster, configure Border Gateway Protocol (BGP) using FRRouting (FRR) and the FRR-K8s daemon. You can define routing behavior with the `FRRConfiguration` custom resource (CR) and ensure compatibility with the MetalLB Operator by using the required namespace and migration approach.

</div>

OpenShift Container Platform supports BGP routing through FRR, a free, open source internet routing protocol suite for Linux, UNIX, and similar operating systems. FRR-K8s is a Kubernetes-based daemon set that exposes a subset of the FRR API in a Kubernetes-compliant manner. As a cluster administrator, you can use the `FRRConfiguration` custom resource to access FRR services.

## Supported platforms

BGP routing is supported on the following infrastructure types:

- Bare metal

BGP routing requires that you have properly configured BGP for your network provider. Outages or misconfigurations of your network provider might cause disruptions to your cluster network.

## Considerations for use with the MetalLB Operator

The MetalLB Operator is installed as an add-on to the cluster. Deployment of the MetalLB Operator automatically enables FRR-K8s as an additional routing capability provider and uses the FRR-K8s daemon installed by this feature.

Before upgrading to 4.18, any existing `FRRConfiguration` in the `metallb-system` namespace not managed by the MetalLB operator (added by a cluster administrator or any other component) needs to be copied to the `openshift-frr-k8s` namespace manually, creating the namespace if necessary.

> [!IMPORTANT]
> If you are using the MetalLB Operator and there are existing `FRRConfiguration` CRs in the `metallb-system` namespace created by cluster administrators or third-party cluster components other than MetalLB Operator, you must:
>
> - Ensure that these existing `FRRConfiguration` CRs are copied to the `openshift-frr-k8s` namespace.
>
> - Ensure that the third-party cluster components use the new namespace for the `FRRConfiguration` CRs that they create.

## Cluster Network Operator configuration

The Cluster Network Operator API exposes the following API field to configure BGP routing:

- `spec.additionalRoutingCapabilities`: Enables deployment of the FRR-K8s daemon for the cluster, which can be used independently of route advertisements. When enabled, the FRR-K8s daemon is deployed on all nodes.

## BGP routing custom resources

The following custom resources are used to configure BGP routing:

`FRRConfiguration`
This custom resource defines the FRR configuration for the BGP routing. This CR is namespaced.

# Configuring the FRRConfiguration CR

<div wrapper="1" role="_abstract">

To customize routing behavior beyond standard MetalLB capabilities, configure the `FRRConfiguration` custom resource (CR).

</div>

The following reference examples demonstrate how to define specific FRRouting (FRR) parameters to enable advanced services, such as receiving routes:

The `routers` parameter
You can use the `routers` parameter to configure multiple routers, one for each Virtual Routing and Forwarding (VRF) resource. For each router, you must define the Autonomous System Number (ASN).

You can also define a list of Border Gateway Protocol (BGP) neighbors to connect to, as in the following example:

<div class="formalpara">

<div class="title">

Example FRRConfiguration CR

</div>

``` yaml
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  name: test
  namespace: frr-k8s-system
spec:
  bgp:
    routers:
    - asn: 64512
      neighbors:
      - address: 172.30.0.3
        asn: 4200000000
        ebgpMultiHop: true
        port: 180
      - address: 172.18.0.6
        asn: 4200000000
        port: 179
# ...
```

</div>

The `toAdvertise` parameter
By default, `FRR-K8s` does not advertise the prefixes configured as part of a router configuration. To advertise the prefixes, you use the `toAdvertise` parameter.

You can advertise a subset of the prefixes, as in the following example:

<div class="formalpara">

<div class="title">

Example FRRConfiguration CR

</div>

``` yaml
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  name: test
  namespace: frr-k8s-system
spec:
  bgp:
    routers:
    - asn: 64512
      neighbors:
      - address: 172.30.0.3
        asn: 4200000000
        ebgpMultiHop: true
        port: 180
        toAdvertise:
          allowed:
            prefixes:
            - 192.168.2.0/24
      prefixes:
        - 192.168.2.0/24
        - 192.169.2.0/24
# ...
```

</div>

- `allowed.prefixes`: Advertises a subset of prefixes.

The following example shows you how to advertise all of the prefixes:

<div class="formalpara">

<div class="title">

Example FRRConfiguration CR

</div>

``` yaml
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  name: test
  namespace: frr-k8s-system
spec:
  bgp:
    routers:
    - asn: 64512
      neighbors:
      - address: 172.30.0.3
        asn: 4200000000
        ebgpMultiHop: true
        port: 180
        toAdvertise:
          allowed:
            mode: all
      prefixes:
        - 192.168.2.0/24
        - 192.169.2.0/24
# ...
```

</div>

- `allowed.mode`: Advertises all prefixes.

The `toReceive` parameter
By default, `FRR-K8s` does not process any prefixes advertised by a neighbor. You can use the `toReceive` parameter to process such addresses.

You can configure for a subset of the prefixes, as in this example:

<div class="formalpara">

<div class="title">

Example FRRConfiguration CR

</div>

``` yaml
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  name: test
  namespace: frr-k8s-system
spec:
  bgp:
    routers:
    - asn: 64512
      neighbors:
      - address: 172.18.0.5
          asn: 64512
          port: 179
          toReceive:
            allowed:
              prefixes:
              - prefix: 192.168.1.0/24
              - prefix: 192.169.2.0/24
                ge: 25
                le: 28
# ...
```

</div>

- `prefixes`: The prefix is applied if the prefix length is less than or equal to the `le` prefix length and greater than or equal to the `ge` prefix length.

The following example configures FRR to handle all the prefixes announced:

<div class="formalpara">

<div class="title">

Example FRRConfiguration CR

</div>

``` yaml
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  name: test
  namespace: frr-k8s-system
spec:
  bgp:
    routers:
    - asn: 64512
      neighbors:
      - address: 172.18.0.5
          asn: 64512
          port: 179
          toReceive:
            allowed:
              mode: all
# ...
```

</div>

The `bgp` parameter
You can use the `bgp` parameter to define various `BFD` profiles and associate them with a neighbor. In the following example, `BFD` backs up the `BGP` session and `FRR` can detect link failures:

<div class="formalpara">

<div class="title">

Example FRRConfiguration CR

</div>

``` yaml
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  name: test
  namespace: frr-k8s-system
spec:
  bgp:
    routers:
    - asn: 64512
      neighbors:
      - address: 172.30.0.3
        asn: 64512
        port: 180
        bfdProfile: defaultprofile
    bfdProfiles:
      - name: defaultprofile
# ...
```

</div>

The `nodeSelector` parameter
By default, `FRR-K8s` applies the configuration to all nodes where the daemon is running. You can use the `nodeSelector` parameter to specify the nodes to which you want to apply the configuration. For example:

<div class="formalpara">

<div class="title">

Example FRRConfiguration CR

</div>

``` yaml
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  name: test
  namespace: frr-k8s-system
spec:
  bgp:
    routers:
    - asn: 64512
  nodeSelector:
    labelSelector:
    foo: "bar"
# ...
```

</div>

The `interface` parameter
You can use the `interface` parameter to configure unnumbered BGP peering by using the following example configuration:

<div class="formalpara">

<div class="title">

Example `FRRConfiguration` CR

</div>

``` yaml
apiVersion: frrk8s.metallb.io/v1beta1
kind: FRRConfiguration
metadata:
  name: test
  namespace: frr-k8s-system
spec:
  bgp:
    bfdProfiles:
    - echoMode: false
      name: simple
      passiveMode: false
    routers:
    - asn: 64512
      neighbors:
      - asn: 64512
        bfdProfile: simple
        disableMP: false
        interface: net10
        port: 179
        toAdvertise:
          allowed:
            mode: filtered
            prefixes:
            - 5.5.5.5/32
        toReceive:
          allowed:
            mode: filtered
      prefixes:
      - 5.5.5.5/32
# ...
```

</div>

- `neighbors.interface`: Activates unnumbered BGP peering.

> [!NOTE]
> To use the `interface` parameter, you must establish a point-to-point, layer 2 connection between the two BGP peers. You can use unnumbered BGP peering with IPv4, IPv6, or dual-stack, but you must enable IPv6 RAs (Router Advertisements). Each interface is limited to one BGP connection.
>
> If you use this parameter, you cannot specify a value in the `spec.bgp.routers.neighbors.address` parameter.

The parameters for the `FRRConfiguration` custom resource are described in the following table:

| Parameter | Type | Description |
|----|----|----|
| `spec.bgp.routers` | `array` | Specifies the routers that FRR is to configure (one per VRF). |
| `spec.bgp.routers.asn` | `integer` | The Autonomous System Number (ASN) to use for the local end of the session. |
| `spec.bgp.routers.id` | `string` | Specifies the ID of the `bgp` router. |
| `spec.bgp.routers.vrf` | `string` | Specifies the host VRF used to establish sessions from this router. |
| `spec.bgp.routers.neighbors` | `array` | Specifies the neighbors to establish BGP sessions with. |
| `spec.bgp.routers.neighbors.asn` | `integer` | Specifies the ASN to use for the remote end of the session. If you use this parameter, you cannot specify a value in the `spec.bgp.routers.neighbors.dynamicASN` parameter. |
| `spec.bgp.routers.neighbors.dynamicASN` | `string` | Detects the ASN to use for the remote end of the session without explicitly setting it. Specify `internal` for a neighbor with the same ASN, or `external` for a neighbor with a different ASN. If you use this parameter, you cannot specify a value in the `spec.bgp.routers.neighbors.asn` parameter. |
| `spec.bgp.routers.neighbors.address` | `string` | Specifies the IP address to establish the session with. If you use this parameter, you cannot specify a value in the `spec.bgp.routers.neighbors.interface` parameter. |
| `spec.bgp.routers.neighbors.interface` | `string` | Specifies the interface name to use when establishing a session. Use this parameter to configure unnumbered BGP peering. There must be a point-to-point, layer 2 connection between the two BGP peers. You can use unnumbered BGP peering with IPv4, IPv6, or dual-stack, but you must enable IPv6 RAs (Router Advertisements). Each interface is limited to one BGP connection. |
| `spec.bgp.routers.neighbors.port` | `integer` | Specifies the port to dial when establishing the session. Defaults to `179`. |
| `spec.bgp.routers.neighbors.password` | `string` | Specifies the password to use for establishing the BGP session. `Password` and `PasswordSecret` are mutually exclusive. |
| `spec.bgp.routers.neighbors.passwordSecret` | `string` | Specifies the name of the authentication secret for the neighbor. The secret must be of type "kubernetes.io/basic-auth", and in the same namespace as the FRR-K8s daemon. The key "password" stores the password in the secret. `Password` and `PasswordSecret` are mutually exclusive. |
| `spec.bgp.routers.neighbors.holdTime` | `duration` | Specifies the requested BGP hold time, per RFC4271. Defaults to 180s. |
| `spec.bgp.routers.neighbors.keepaliveTime` | `duration` | Specifies the requested BGP keepalive time, per RFC4271. Defaults to `60s`. |
| `spec.bgp.routers.neighbors.connectTime` | `duration` | Specifies how long BGP waits between connection attempts to a neighbor. |
| `spec.bgp.routers.neighbors.ebgpMultiHop` | `boolean` | Indicates if the BGPPeer is a multi-hop away. |
| `spec.bgp.routers.neighbors.bfdProfile` | `string` | Specifies the name of the BFD Profile to use for the BFD session associated with the BGP session. If not set, the BFD session is not set up. |
| `spec.bgp.routers.neighbors.toAdvertise.allowed` | `array` | Represents the list of prefixes to advertise to a neighbor, and the associated properties. |
| `spec.bgp.routers.neighbors.toAdvertise.allowed.prefixes` | `string array` | Specifies the list of prefixes to advertise to a neighbor. This list must match the prefixes that you define in the router. |
| `spec.bgp.routers.neighbors.toAdvertise.allowed.mode` | `string` | Specifies the mode to use when handling the prefixes. You can set to `filtered` to allow only the prefixes in the prefixes list. You can set to `all` to allow all the prefixes configured on the router. |
| `spec.bgp.routers.neighbors.toAdvertise.withLocalPref` | `array` | Specifies the prefixes associated with an advertised local preference. You must specify the prefixes associated with a local preference in the prefixes allowed to be advertised. |
| `spec.bgp.routers.neighbors.toAdvertise.withLocalPref.prefixes` | `string array` | Specifies the prefixes associated with the local preference. |
| `spec.bgp.routers.neighbors.toAdvertise.withLocalPref.localPref` | `integer` | Specifies the local preference associated with the prefixes. |
| `spec.bgp.routers.neighbors.toAdvertise.withCommunity` | `array` | Specifies the prefixes associated with an advertised BGP community. You must include the prefixes associated with a local preference in the list of prefixes that you want to advertise. |
| `spec.bgp.routers.neighbors.toAdvertise.withCommunity.prefixes` | `string array` | Specifies the prefixes associated with the community. |
| `spec.bgp.routers.neighbors.toAdvertise.withCommunity.community` | `string` | Specifies the community associated with the prefixes. |
| `spec.bgp.routers.neighbors.toReceive` | `array` | Specifies the prefixes to receive from a neighbor. |
| `spec.bgp.routers.neighbors.toReceive.allowed` | `array` | Specifies the information that you want to receive from a neighbor. |
| `spec.bgp.routers.neighbors.toReceive.allowed.prefixes` | `array` | Specifies the prefixes allowed from a neighbor. |
| `spec.bgp.routers.neighbors.toReceive.allowed.mode` | `string` | Specifies the mode to use when handling the prefixes. When set to `filtered`, only the prefixes in the `prefixes` list are allowed. When set to `all`, all the prefixes configured on the router are allowed. |
| `spec.bgp.routers.neighbors.disableMP` | `boolean` | Disables MP BGP to prevent it from separating IPv4 and IPv6 route exchanges into distinct BGP sessions. |
| `spec.bgp.routers.prefixes` | `string array` | Specifies all prefixes to advertise from this router instance. |
| `spec.bgp.bfdProfiles` | `array` | Specifies the list of BFD profiles to use when configuring the neighbors. |
| `spec.bgp.bfdProfiles.name` | `string` | The name of the BFD Profile to be referenced in other parts of the configuration. |
| `spec.bgp.bfdProfiles.receiveInterval` | `integer` | Specifies the minimum interval at which this system can receive control packets, in milliseconds. Defaults to `300ms`. |
| `spec.bgp.bfdProfiles.transmitInterval` | `integer` | Specifies the minimum transmission interval, excluding jitter, that this system wants to use to send BFD control packets, in milliseconds. Defaults to `300ms`. |
| `spec.bgp.bfdProfiles.detectMultiplier` | `integer` | Configures the detection multiplier to determine packet loss. To determine the connection loss-detection timer, multiply the remote transmission interval by this value. |
| `spec.bgp.bfdProfiles.echoInterval` | `integer` | Configures the minimal echo receive transmission-interval that this system can handle, in milliseconds. Defaults to `50ms`. |
| `spec.bgp.bfdProfiles.echoMode` | `boolean` | Enables or disables the echo transmission mode. This mode is disabled by default, and not supported on multihop setups. |
| `spec.bgp.bfdProfiles.passiveMode` | `boolean` | Mark session as passive. A passive session does not attempt to start the connection and waits for control packets from peers before it begins replying. |
| `spec.bgp.bfdProfiles.MinimumTtl` | `integer` | For multihop sessions only. Configures the minimum expected TTL for an incoming BFD control packet. |
| `spec.nodeSelector` | `string` | Limits the nodes that attempt to apply this configuration. If specified, only those nodes whose labels match the specified selectors attempt to apply the configuration. If it is not specified, all nodes attempt to apply this configuration. |
| `status` | `string` | Defines the observed state of FRRConfiguration. |

MetalLB FRRConfiguration custom resource

# Additional resources

- [FRRouting User Guide: BGP](https://docs.frrouting.org/en/latest/bgp.html)

- [Migrating FRR-K8s resources](../../../networking/advanced_networking/bgp_routing/migrating-frr-k8s-resources.xml#migrating-frr-k8s-resources)
