# kubeadm Configuration (v1beta3)

## Overview

Package v1beta3 defines the v1beta3 version of the kubeadm configuration file format.
This version improves on the v1beta2 format by fixing some minor issues and adding a few new fields.

A list of changes since v1beta2:

* The deprecated "ClusterConfiguration.useHyperKubeImage" field has been removed.
  Kubeadm no longer supports the hyperkube image.
* The "ClusterConfiguration.dns.type" field has been removed since CoreDNS is the only supported
  DNS server type by kubeadm.
* Include "datapolicy" tags on the fields that hold secrets.
  This would result in the field values to be omitted when API structures are printed with klog.
* Add "InitConfiguration.skipPhases", "JoinConfiguration.skipPhases" to allow skipping
  a list of phases during kubeadm init/join command execution.
* Add "InitConfiguration.nodeRegistration.imagePullPolicy" and "JoinConfiguration.nodeRegistration.imagePullPolicy"
  to allow specifying the images pull policy during kubeadm "init" and "join".
  The value must be one of "Always", "Never" or "IfNotPresent".
  "IfNotPresent" is the default, which has been the existing behavior prior to this addition.
* Add "InitConfiguration.patches.directory", "JoinConfiguration.patches.directory" to allow
  the user to configure a directory from which to take patches for components deployed by kubeadm.
* Move the BootstrapToken* API and related utilities out of the "kubeadm" API group to a new group
  "bootstraptoken". The kubeadm API version v1beta3 no longer contains the BootstrapToken* structures.

Migration from old kubeadm config versions

* kubeadm v1.15.x and newer can be used to migrate from v1beta1 to v1beta2.
* kubeadm v1.22.x and newer no longer support v1beta1 and older APIs, but can be used to migrate v1beta2 to v1beta3.
* kubeadm v1.27.x and newer no longer support v1beta2 and older APIs,

## Basics

The preferred way to configure kubeadm is to pass an YAML configuration file with the `--config` option. Some of the
configuration options defined in the kubeadm config file are also available as command line flags, but only
the most common/simple use case are supported with this approach.

A kubeadm config file could contain multiple configuration types separated using three dashes (`---`).

kubeadm supports the following configuration types:

```
apiVersion: kubeadm.k8s.io/v1beta3
kind: InitConfiguration

apiVersion: kubeadm.k8s.io/v1beta3
kind: ClusterConfiguration

apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration

apiVersion: kubeproxy.config.k8s.io/v1alpha1
kind: KubeProxyConfiguration

apiVersion: kubeadm.k8s.io/v1beta3
kind: JoinConfiguration
```

To print the defaults for "init" and "join" actions use the following commands:

```
kubeadm config print init-defaults
kubeadm config print join-defaults
```

The list of configuration types that must be included in a configuration file depends by the action you are
performing (`init` or `join`) and by the configuration options you are going to use (defaults or advanced
customization).

If some configuration types are not provided, or provided only partially, kubeadm will use default values; defaults
provided by kubeadm includes also enforcing consistency of values across components when required (e.g.
`--cluster-cidr` flag on controller manager and `clusterCIDR` on kube-proxy).

Users are always allowed to override default values, with the only exception of a small subset of setting with
relevance for security (e.g. enforce authorization-mode Node and RBAC on api server).

If the user provides a configuration types that is not expected for the action you are performing, kubeadm will
ignore those types and print a warning.

## Kubeadm init configuration types

When executing kubeadm init with the `--config` option, the following configuration types could be used:
InitConfiguration, ClusterConfiguration, KubeProxyConfiguration, KubeletConfiguration, but only one
between InitConfiguration and ClusterConfiguration is mandatory.

```
apiVersion: kubeadm.k8s.io/v1beta3
kind: InitConfiguration
bootstrapTokens:
  ...
nodeRegistration:
  ...
```

The InitConfiguration type should be used to configure runtime settings, that in case of kubeadm init
are the configuration of the bootstrap token and all the setting which are specific to the node where
kubeadm is executed, including:

* NodeRegistration, that holds fields that relate to registering the new node to the cluster;
  use it to customize the node name, the CRI socket to use or any other settings that should apply to this
  node only (e.g. the node ip).
* LocalAPIEndpoint, that represents the endpoint of the instance of the API server to be deployed on this node;
  use it e.g. to customize the API server advertise address.

```
apiVersion: kubeadm.k8s.io/v1beta3
kind: ClusterConfiguration
networking:
  ...
etcd:
  ...
apiServer:
  extraArgs:
    ...
  extraVolumes:
    ...
...
```

The ClusterConfiguration type should be used to configure cluster-wide settings,
including settings for:

* `networking` that holds configuration for the networking topology of the cluster; use it e.g. to customize
  Pod subnet or services subnet.
* `etcd`: use it e.g. to customize the local etcd or to configure the API server
  for using an external etcd cluster.
* kube-apiserver, kube-scheduler, kube-controller-manager configurations; use it to customize control-plane
  components by adding customized setting or overriding kubeadm default settings.

```
apiVersion: kubeproxy.config.k8s.io/v1alpha1
kind: KubeProxyConfiguration
  ...
```

The KubeProxyConfiguration type should be used to change the configuration passed to kube-proxy instances
deployed in the cluster. If this object is not provided or provided only partially, kubeadm applies defaults.

See https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/ or
https://pkg.go.dev/k8s.io/kube-proxy/config/v1alpha1#KubeProxyConfiguration
for kube-proxy official documentation.

```
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
  ...
```

The KubeletConfiguration type should be used to change the configurations that will be passed to all kubelet instances
deployed in the cluster. If this object is not provided or provided only partially, kubeadm applies defaults.

See https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/ or
https://pkg.go.dev/k8s.io/kubelet/config/v1beta1#KubeletConfiguration
for kubelet official documentation.

Here is a fully populated example of a single YAML file containing multiple
configuration types to be used during a `kubeadm init` run.

```
apiVersion: kubeadm.k8s.io/v1beta3
kind: InitConfiguration
bootstrapTokens:
  - token: "9a08jv.c0izixklcxtmnze7"
    description: "kubeadm bootstrap token"
    ttl: "24h"
  - token: "783bde.3f89s0fje9f38fhf"
    description: "another bootstrap token"
    usages:
      - authentication
      - signing
    groups:
      - system:bootstrappers:kubeadm:default-node-token
nodeRegistration:
  name: "ec2-10-100-0-1"
  criSocket: "/var/run/dockershim.sock"
  taints:
    - key: "kubeadmNode"
      value: "someValue"
      effect: "NoSchedule"
  kubeletExtraArgs:
    v: 4
  ignorePreflightErrors:
    - IsPrivilegedUser
  imagePullPolicy: "IfNotPresent"
localAPIEndpoint:
  advertiseAddress: "10.100.0.1"
  bindPort: 6443
certificateKey: "e6a2eb8581237ab72a4f494f30285ec12a9694d750b9785706a83bfcbbbd2204"
skipPhases:
  - addon/kube-proxy
---
apiVersion: kubeadm.k8s.io/v1beta3
kind: ClusterConfiguration
etcd:
  # one of local or external
  local:
    imageRepository: "registry.k8s.io"
    imageTag: "3.2.24"
    dataDir: "/var/lib/etcd"
    extraArgs:
      listen-client-urls: "http://10.100.0.1:2379"
    serverCertSANs:
      -  "ec2-10-100-0-1.compute-1.amazonaws.com"
    peerCertSANs:
      - "10.100.0.1"
  # external:
    # endpoints:
    # - "10.100.0.1:2379"
    # - "10.100.0.2:2379"
    # caFile: "/etcd/kubernetes/pki/etcd/etcd-ca.crt"
    # certFile: "/etcd/kubernetes/pki/etcd/etcd.crt"
    # keyFile: "/etcd/kubernetes/pki/etcd/etcd.key"
networking:
  serviceSubnet: "10.96.0.0/16"
  podSubnet: "10.244.0.0/24"
  dnsDomain: "cluster.local"
kubernetesVersion: "v1.21.0"
controlPlaneEndpoint: "10.100.0.1:6443"
apiServer:
  extraArgs:
    authorization-mode: "Node,RBAC"
  extraVolumes:
    - name: "some-volume"
      hostPath: "/etc/some-path"
      mountPath: "/etc/some-pod-path"
      readOnly: false
      pathType: File
  certSANs:
    - "10.100.1.1"
    - "ec2-10-100-0-1.compute-1.amazonaws.com"
  timeoutForControlPlane: 4m0s
controllerManager:
  extraArgs:
    "node-cidr-mask-size": "20"
  extraVolumes:
    - name: "some-volume"
      hostPath: "/etc/some-path"
      mountPath: "/etc/some-pod-path"
      readOnly: false
      pathType: File
scheduler:
  extraArgs:
    bind-address: "10.100.0.1"
  extraVolumes:
    - name: "some-volume"
      hostPath: "/etc/some-path"
      mountPath: "/etc/some-pod-path"
      readOnly: false
      pathType: File
certificatesDir: "/etc/kubernetes/pki"
imageRepository: "registry.k8s.io"
clusterName: "example-cluster"
---
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
# kubelet specific options here
---
apiVersion: kubeproxy.config.k8s.io/v1alpha1
kind: KubeProxyConfiguration
# kube-proxy specific options here
```

## Kubeadm join configuration types

When executing `kubeadm join` with the `--config` option, the JoinConfiguration type should be provided.

```
apiVersion: kubeadm.k8s.io/v1beta3
kind: JoinConfiguration
  ...
```

The JoinConfiguration type should be used to configure runtime settings, that in case of `kubeadm join`
are the discovery method used for accessing the cluster info and all the setting which are specific
to the node where kubeadm is executed, including:

* `nodeRegistration`, that holds fields that relate to registering the new node to the cluster;
  use it to customize the node name, the CRI socket to use or any other settings that should apply to this
  node only (e.g. the node ip).
* `apiEndpoint`, that represents the endpoint of the instance of the API server to be eventually deployed on this node.

## Resource Types

* [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)
* [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)
* [JoinConfiguration](#kubeadm-k8s-io-v1beta3-JoinConfiguration)

## `BootstrapToken`

**Appears in:**

* [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)

BootstrapToken describes one bootstrap token, stored as a Secret in the cluster

| Field | Description |
| --- | --- |
| `token` **[Required]**  [`BootstrapTokenString`](#BootstrapTokenString) | `token` is used for establishing bidirectional trust between nodes and control-planes. Used for joining nodes in the cluster. |
| `description`  `string` | `description` sets a human-friendly message why this token exists and what it's used for, so other administrators can know its purpose. |
| `ttl`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | `ttl` defines the time to live for this token. Defaults to `24h`. `expires` and `ttl` are mutually exclusive. |
| `expires`  [`meta/v1.Time`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#time-v1-meta) | `expires` specifies the timestamp when this token expires. Defaults to being set dynamically at runtime based on the `ttl`. `expires` and `ttl` are mutually exclusive. |
| `usages`  `[]string` | `usages` describes the ways in which this token can be used. Can by default be used for establishing bidirectional trust, but that can be changed here. |
| `groups`  `[]string` | `groups` specifies the extra groups that this token will authenticate as when/if used for authentication |

## `BootstrapTokenString`

**Appears in:**

* [BootstrapToken](#BootstrapToken)

BootstrapTokenString is a token of the format `abcdef.abcdef0123456789` that is used
for both validation of the practically of the API server from a joining node's point
of view and as an authentication method for the node in the bootstrap phase of
"kubeadm join". This token is and should be short-lived.

| Field | Description |
| --- | --- |
| `-` **[Required]**  `string` | No description provided. |
| `-` **[Required]**  `string` | No description provided. |

## `ClusterConfiguration`

ClusterConfiguration contains cluster-wide configuration for a kubeadm cluster.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubeadm.k8s.io/v1beta3` |
| `kind` string | `ClusterConfiguration` |
| `etcd`  [`Etcd`](#kubeadm-k8s-io-v1beta3-Etcd) | `etcd` holds the configuration for etcd. |
| `networking`  [`Networking`](#kubeadm-k8s-io-v1beta3-Networking) | `networking` holds configuration for the networking topology of the cluster. |
| `kubernetesVersion`  `string` | `kubernetesVersion` is the target version of the control plane. |
| `controlPlaneEndpoint`  `string` | `controlPlaneEndpoint` sets a stable IP address or DNS name for the control plane. It can be a valid IP address or a RFC-1123 DNS subdomain, both with optional TCP port. In case the `controlPlaneEndpoint` is not specified, the `advertiseAddress` + `bindPort` are used; in case the `controlPlaneEndpoint` is specified but without a TCP port, the `bindPort` is used. Possible usages are:   * In a cluster with more than one control plane instances, this field should be   assigned the address of the external load balancer in front of the   control plane instances. * In environments with enforced node recycling, the `controlPlaneEndpoint` could   be used for assigning a stable DNS to the control plane. |
| `apiServer`  [`APIServer`](#kubeadm-k8s-io-v1beta3-APIServer) | `apiServer` contains extra settings for the API server. |
| `controllerManager`  [`ControlPlaneComponent`](#kubeadm-k8s-io-v1beta3-ControlPlaneComponent) | `controllerManager` contains extra settings for the controller manager. |
| `scheduler`  [`ControlPlaneComponent`](#kubeadm-k8s-io-v1beta3-ControlPlaneComponent) | `scheduler` contains extra settings for the scheduler. |
| `dns`  [`DNS`](#kubeadm-k8s-io-v1beta3-DNS) | `dns` defines the options for the DNS add-on installed in the cluster. |
| `certificatesDir`  `string` | `certificatesDir` specifies where to store or look for all required certificates. |
| `imageRepository`  `string` | `imageRepository` sets the container registry to pull images from. If empty, `registry.k8s.io` will be used by default. In case of kubernetes version is a CI build (kubernetes version starts with `ci/`) `gcr.io/k8s-staging-ci-images` will be used as a default for control plane components and for kube-proxy, while `registry.k8s.io` will be used for all the other images. |
| `featureGates`  `map[string]bool` | `featureGates` contains the feature gates enabled by the user. |
| `clusterName`  `string` | The cluster name. |

## `InitConfiguration`

InitConfiguration contains a list of elements that is specific "kubeadm init"-only runtime
information.
`kubeadm init`-only information. These fields are solely used the first time `kubeadm init` runs.
After that, the information in the fields IS NOT uploaded to the `kubeadm-config` ConfigMap
that is used by `kubeadm upgrade` for instance. These fields must be omitempty.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubeadm.k8s.io/v1beta3` |
| `kind` string | `InitConfiguration` |
| `bootstrapTokens`  [`[]BootstrapToken`](#BootstrapToken) | `bootstrapTokens` is respected at `kubeadm init` time and describes a set of Bootstrap Tokens to create. This information IS NOT uploaded to the kubeadm cluster configmap, partly because of its sensitive nature |
| `nodeRegistration`  [`NodeRegistrationOptions`](#kubeadm-k8s-io-v1beta3-NodeRegistrationOptions) | `nodeRegistration` holds fields that relate to registering the new control-plane node to the cluster. |
| `localAPIEndpoint`  [`APIEndpoint`](#kubeadm-k8s-io-v1beta3-APIEndpoint) | `localAPIEndpoint` represents the endpoint of the API server instance that's deployed on this control plane node. In HA setups, this differs from `ClusterConfiguration.controlPlaneEndpoint` in the sense that `controlPlaneEndpoint` is the global endpoint for the cluster, which then load-balances the requests to each individual API server. This configuration object lets you customize what IP/DNS name and port the local API server advertises it's accessible on. By default, kubeadm tries to auto-detect the IP of the default interface and use that, but in case that process fails you may set the desired value here. |
| `certificateKey`  `string` | `certificateKey` sets the key with which certificates and keys are encrypted prior to being uploaded in a Secret in the cluster during the `uploadcerts init` phase. The certificate key is a hex encoded string that is an AES key of size 32 bytes. |
| `skipPhases`  `[]string` | `skipPhases` is a list of phases to skip during command execution. The list of phases can be obtained with the `kubeadm init --help` command. The flag "--skip-phases" takes precedence over this field. |
| `patches`  [`Patches`](#kubeadm-k8s-io-v1beta3-Patches) | `patches` contains options related to applying patches to components deployed by kubeadm during `kubeadm init`. |

## `JoinConfiguration`

JoinConfiguration contains elements describing a particular node.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubeadm.k8s.io/v1beta3` |
| `kind` string | `JoinConfiguration` |
| `nodeRegistration`  [`NodeRegistrationOptions`](#kubeadm-k8s-io-v1beta3-NodeRegistrationOptions) | `nodeRegistration` holds fields that relate to registering the new control-plane node to the cluster. |
| `caCertPath`  `string` | `caCertPath` is the path to the SSL certificate authority used to secure communications between a node and the control-plane. Defaults to "/etc/kubernetes/pki/ca.crt". |
| `discovery` **[Required]**  [`Discovery`](#kubeadm-k8s-io-v1beta3-Discovery) | `discovery` specifies the options for the kubelet to use during the TLS bootstrap process. |
| `controlPlane`  [`JoinControlPlane`](#kubeadm-k8s-io-v1beta3-JoinControlPlane) | `controlPlane` defines the additional control plane instance to be deployed on the joining node. If nil, no additional control plane instance will be deployed. |
| `skipPhases`  `[]string` | `skipPhases` is a list of phases to skip during command execution. The list of phases can be obtained with the `kubeadm join --help` command. The flag `--skip-phases` takes precedence over this field. |
| `patches`  [`Patches`](#kubeadm-k8s-io-v1beta3-Patches) | `patches` contains options related to applying patches to components deployed by kubeadm during `kubeadm join`. |

## `APIEndpoint`

**Appears in:**

* [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)
* [JoinControlPlane](#kubeadm-k8s-io-v1beta3-JoinControlPlane)

APIEndpoint struct contains elements of API server instance deployed on a node.

| Field | Description |
| --- | --- |
| `advertiseAddress`  `string` | `advertiseAddress` sets the IP address for the API server to advertise. |
| `bindPort`  `int32` | `bindPort` sets the secure port for the API Server to bind to. Defaults to 6443. |

## `APIServer`

**Appears in:**

* [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)

APIServer holds settings necessary for API server deployments in the cluster

| Field | Description |
| --- | --- |
| `ControlPlaneComponent` **[Required]**  [`ControlPlaneComponent`](#kubeadm-k8s-io-v1beta3-ControlPlaneComponent) | (Members of `ControlPlaneComponent` are embedded into this type.) No description provided. |
| `certSANs`  `[]string` | `certSANs` sets extra Subject Alternative Names (SANs) for the API Server signing certificate. |
| `timeoutForControlPlane`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | `timeoutForControlPlane` controls the timeout that we wait for API server to appear. |

## `BootstrapTokenDiscovery`

**Appears in:**

* [Discovery](#kubeadm-k8s-io-v1beta3-Discovery)

BootstrapTokenDiscovery is used to set the options for bootstrap token based discovery.

| Field | Description |
| --- | --- |
| `token` **[Required]**  `string` | `token` is a token used to validate cluster information fetched from the control-plane. |
| `apiServerEndpoint`  `string` | `apiServerEndpoint` is an IP or domain name to the API server from which information will be fetched. |
| `caCertHashes`  `[]string` | `caCertHashes` specifies a set of public key pins to verify when token-based discovery is used. The root CA found during discovery must match one of these values. Specifying an empty set disables root CA pinning, which can be unsafe. Each hash is specified as `<type>:<value>`, where the only currently supported type is "sha256". This is a hex-encoded SHA-256 hash of the Subject Public Key Info (SPKI) object in DER-encoded ASN.1. These hashes can be calculated using, for example, OpenSSL. |
| `unsafeSkipCAVerification`  `bool` | `unsafeSkipCAVerification` allows token-based discovery without CA verification via `caCertHashes`. This can weaken the security of kubeadm since other nodes can impersonate the control-plane. |

## `ControlPlaneComponent`

**Appears in:**

* [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)
* [APIServer](#kubeadm-k8s-io-v1beta3-APIServer)

ControlPlaneComponent holds settings common to control plane component of the cluster

| Field | Description |
| --- | --- |
| `extraArgs`  `map[string]string` | `extraArgs` is an extra set of flags to pass to the control plane component. A key in this map is the flag name as it appears on the command line except without leading dash(es). |
| `extraVolumes`  [`[]HostPathMount`](#kubeadm-k8s-io-v1beta3-HostPathMount) | `extraVolumes` is an extra set of host volumes, mounted to the control plane component. |

## `DNS`

**Appears in:**

* [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)

DNS defines the DNS addon that should be used in the cluster

| Field | Description |
| --- | --- |
| `ImageMeta` **[Required]**  [`ImageMeta`](#kubeadm-k8s-io-v1beta3-ImageMeta) | (Members of `ImageMeta` are embedded into this type.) `imageMeta` allows to customize the image used for the DNS component. |

## `Discovery`

**Appears in:**

* [JoinConfiguration](#kubeadm-k8s-io-v1beta3-JoinConfiguration)

Discovery specifies the options for the kubelet to use during the TLS Bootstrap process.

| Field | Description |
| --- | --- |
| `bootstrapToken`  [`BootstrapTokenDiscovery`](#kubeadm-k8s-io-v1beta3-BootstrapTokenDiscovery) | `bootstrapToken` is used to set the options for bootstrap token based discovery. `bootstrapToken` and `file` are mutually exclusive. |
| `file`  [`FileDiscovery`](#kubeadm-k8s-io-v1beta3-FileDiscovery) | `file` is used to specify a file or URL to a kubeconfig file from which to load cluster information. `bootstrapToken` and `file` are mutually exclusive. |
| `tlsBootstrapToken`  `string` | `tlsBootstrapToken` is a token used for TLS bootstrapping. If `bootstrapToken` is set, this field is defaulted to `.bootstrapToken.token`, but can be overridden. If `file` is set, this field **must be set** in case the KubeConfigFile does not contain any other authentication information |
| `timeout`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | `timeout` modifies the discovery timeout. |

## `Etcd`

**Appears in:**

* [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)

Etcd contains elements describing Etcd configuration.

| Field | Description |
| --- | --- |
| `local`  [`LocalEtcd`](#kubeadm-k8s-io-v1beta3-LocalEtcd) | `local` provides configuration knobs for configuring the local etcd instance. `local` and `external` are mutually exclusive. |
| `external`  [`ExternalEtcd`](#kubeadm-k8s-io-v1beta3-ExternalEtcd) | `external` describes how to connect to an external etcd cluster. `local` and `external` are mutually exclusive. |

## `ExternalEtcd`

**Appears in:**

* [Etcd](#kubeadm-k8s-io-v1beta3-Etcd)

ExternalEtcd describes an external etcd cluster.
Kubeadm has no knowledge of where certificate files live and they must be supplied.

| Field | Description |
| --- | --- |
| `endpoints` **[Required]**  `[]string` | `endpoints` contains the list of etcd members. |
| `caFile` **[Required]**  `string` | `caFile` is an SSL Certificate Authority (CA) file used to secure etcd communication. Required if using a TLS connection. |
| `certFile` **[Required]**  `string` | `certFile` is an SSL certification file used to secure etcd communication. Required if using a TLS connection. |
| `keyFile` **[Required]**  `string` | `keyFile` is an SSL key file used to secure etcd communication. Required if using a TLS connection. |

## `FileDiscovery`

**Appears in:**

* [Discovery](#kubeadm-k8s-io-v1beta3-Discovery)

FileDiscovery is used to specify a file or URL to a kubeconfig file from which to load
cluster information.

| Field | Description |
| --- | --- |
| `kubeConfigPath` **[Required]**  `string` | `kubeConfigPath` is used to specify the actual file path or URL to the kubeconfig file from which to load cluster information. |

## `HostPathMount`

**Appears in:**

* [ControlPlaneComponent](#kubeadm-k8s-io-v1beta3-ControlPlaneComponent)

HostPathMount contains elements describing volumes that are mounted from the host.

| Field | Description |
| --- | --- |
| `name` **[Required]**  `string` | `name` is the name of the volume inside the Pod template. |
| `hostPath` **[Required]**  `string` | `hostPath` is the path in the host that will be mounted inside the Pod. |
| `mountPath` **[Required]**  `string` | `mountPath` is the path inside the Pod where `hostPath` will be mounted. |
| `readOnly`  `bool` | `readOnly` controls write access to the volume. |
| `pathType`  [`core/v1.HostPathType`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#hostpathtype-v1-core) | `pathType` is the type of the `hostPath`. |

## `ImageMeta`

**Appears in:**

* [DNS](#kubeadm-k8s-io-v1beta3-DNS)
* [LocalEtcd](#kubeadm-k8s-io-v1beta3-LocalEtcd)

ImageMeta allows to customize the image used for components that are not
originated from the Kubernetes/Kubernetes release process

| Field | Description |
| --- | --- |
| `imageRepository`  `string` | `imageRepository` sets the container registry to pull images from. If not set, the `imageRepository` defined in ClusterConfiguration will be used instead. |
| `imageTag`  `string` | `imageTag` allows to specify a tag for the image. In case this value is set, kubeadm does not change automatically the version of the above components during upgrades. |

## `JoinControlPlane`

**Appears in:**

* [JoinConfiguration](#kubeadm-k8s-io-v1beta3-JoinConfiguration)

JoinControlPlane contains elements describing an additional control plane instance
to be deployed on the joining node.

| Field | Description |
| --- | --- |
| `localAPIEndpoint`  [`APIEndpoint`](#kubeadm-k8s-io-v1beta3-APIEndpoint) | `localAPIEndpoint` represents the endpoint of the API server instance to be deployed on this node. |
| `certificateKey`  `string` | `certificateKey` is the key that is used for decryption of certificates after they are downloaded from the secret upon joining a new control plane node. The corresponding encryption key is in the InitConfiguration. The certificate key is a hex encoded string that is an AES key of size 32 bytes. |

## `LocalEtcd`

**Appears in:**

* [Etcd](#kubeadm-k8s-io-v1beta3-Etcd)

LocalEtcd describes that kubeadm should run an etcd cluster locally.

| Field | Description |
| --- | --- |
| `ImageMeta` **[Required]**  [`ImageMeta`](#kubeadm-k8s-io-v1beta3-ImageMeta) | (Members of `ImageMeta` are embedded into this type.) ImageMeta allows to customize the container used for etcd. |
| `dataDir` **[Required]**  `string` | `dataDir` is the directory etcd will place its data. Defaults to "/var/lib/etcd". |
| `extraArgs`  `map[string]string` | `extraArgs` are extra arguments provided to the etcd binary when run inside a static Pod. A key in this map is the flag name as it appears on the command line except without leading dash(es). |
| `serverCertSANs`  `[]string` | `serverCertSANs` sets extra Subject Alternative Names (SANs) for the etcd server signing certificate. |
| `peerCertSANs`  `[]string` | `peerCertSANs` sets extra Subject Alternative Names (SANs) for the etcd peer signing certificate. |

## `Networking`

**Appears in:**

* [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)

Networking contains elements describing cluster's networking configuration.

| Field | Description |
| --- | --- |
| `serviceSubnet`  `string` | `serviceSubnet` is the subnet used by Kubernetes Services. Defaults to "10.96.0.0/12". |
| `podSubnet`  `string` | `podSubnet` is the subnet used by Pods. |
| `dnsDomain`  `string` | `dnsDomain` is the DNS domain used by Kubernetes Services. Defaults to "cluster.local". |

## `NodeRegistrationOptions`

**Appears in:**

* [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)
* [JoinConfiguration](#kubeadm-k8s-io-v1beta3-JoinConfiguration)

NodeRegistrationOptions holds fields that relate to registering a new control-plane or
node to the cluster, either via `kubeadm init` or `kubeadm join`.

| Field | Description |
| --- | --- |
| `name`  `string` | `name` is the `.metadata.name` field of the Node API object that will be created in this `kubeadm init` or `kubeadm join` operation. This field is also used in the `CommonName` field of the kubelet's client certificate to the API server. Defaults to the hostname of the node if not provided. |
| `criSocket`  `string` | `criSocket` is used to retrieve container runtime info. This information will be annotated to the Node API object, for later re-use. |
| `taints` **[Required]**  [`[]core/v1.Taint`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#taint-v1-core) | `taints` specifies the taints the Node API object should be registered with. If this field is unset, i.e. nil, it will be defaulted with a control-plane taint for control-plane nodes. If you don't want to taint your control-plane node, set this field to an empty list, i.e. `taints: []` in the YAML file. This field is solely used for Node registration. |
| `kubeletExtraArgs`  `map[string]string` | `kubeletExtraArgs` passes through extra arguments to the kubelet. The arguments here are passed to the kubelet command line via the environment file kubeadm writes at runtime for the kubelet to source. This overrides the generic base-level configuration in the `kubelet-config` ConfigMap. Flags have higher priority when parsing. These values are local and specific to the node kubeadm is executing on. A key in this map is the flag name as it appears on the command line except without leading dash(es). |
| `ignorePreflightErrors`  `[]string` | `ignorePreflightErrors` provides a list of pre-flight errors to be ignored when the current node is registered, e.g. `IsPrevilegedUser,Swap`. Value `all` ignores errors from all checks. |
| `imagePullPolicy`  [`core/v1.PullPolicy`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#pullpolicy-v1-core) | `imagePullPolicy` specifies the policy for image pulling during kubeadm "init" and "join" operations. The value of this field must be one of "Always", "IfNotPresent" or "Never". If this field is not set, kubeadm will default it to "IfNotPresent", or pull the required images if not present on the host. |

## `Patches`

**Appears in:**

* [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)
* [JoinConfiguration](#kubeadm-k8s-io-v1beta3-JoinConfiguration)

Patches contains options related to applying patches to components deployed by kubeadm.

| Field | Description |
| --- | --- |
| `directory`  `string` | `directory` is a path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd". "patchtype" can be one of "strategic" "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |

This page is automatically generated.

If you plan to report an issue with this page, mention that the page is auto-generated in your issue description. The fix may need to happen elsewhere in the Kubernetes project.

## Feedback

Was this page helpful?

Yes
No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on
[Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes).
Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to
[report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io)
or
[suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

const yes = document.querySelector('.feedback--yes');
const no = document.querySelector('.feedback--no');
document.querySelectorAll('.feedback--link').forEach(link => {
link.href = link.href + window.location.pathname;
});
const sendFeedback = (value) => {
if (!gtag) { console.log('!gtag'); }
gtag('event', 'click', {
'event_category': 'Helpful',
'event_label': window.location.pathname,
value
});
};
const disableButtons = () => {
yes.disabled = true;
yes.classList.add('feedback--button__disabled');
no.disabled = true;
no.classList.add('feedback--button__disabled');
};
yes.addEventListener('click', () => {
sendFeedback(1);
disableButtons();
document.querySelector('.feedback--response').classList.remove('feedback--response__hidden');
});
no.addEventListener('click', () => {
sendFeedback(0);
disableButtons();
document.querySelector('.feedback--response').classList.remove('feedback--response__hidden');
});

Last modified April 23, 2026 at 2:12 AM PST: [Merge pull request #55450 from sayanchowdhury/update-release-1.34-hugo.toml (d1f313a)](https://github.com/kubernetes/website/commit/d1f313a65f45bd4882d05fe9b6bea162fa2fdc16)
