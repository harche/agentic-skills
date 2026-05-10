# kubeadm init

This command initializes a Kubernetes control plane node.

### Synopsis

Run this command in order to set up the Kubernetes control plane

The "init" command executes the following phases:

```
preflight                     Run pre-flight checks
certs                         Certificate generation
  /ca                           Generate the self-signed Kubernetes CA to provision identities for other Kubernetes components
  /apiserver                    Generate the certificate for serving the Kubernetes API
  /apiserver-kubelet-client     Generate the certificate for the API server to connect to kubelet
  /front-proxy-ca               Generate the self-signed CA to provision identities for front proxy
  /front-proxy-client           Generate the certificate for the front proxy client
  /etcd-ca                      Generate the self-signed CA to provision identities for etcd
  /etcd-server                  Generate the certificate for serving etcd
  /etcd-peer                    Generate the certificate for etcd nodes to communicate with each other
  /etcd-healthcheck-client      Generate the certificate for liveness probes to healthcheck etcd
  /apiserver-etcd-client        Generate the certificate the apiserver uses to access etcd
  /sa                           Generate a private key for signing service account tokens along with its public key
kubeconfig                    Generate all kubeconfig files necessary to establish the control plane and the admin kubeconfig file
  /admin                        Generate a kubeconfig file for the admin to use and for kubeadm itself
  /super-admin                  Generate a kubeconfig file for the super-admin
  /kubelet                      Generate a kubeconfig file for the kubelet to use *only* for cluster bootstrapping purposes
  /controller-manager           Generate a kubeconfig file for the controller manager to use
  /scheduler                    Generate a kubeconfig file for the scheduler to use
etcd                          Generate static Pod manifest file for local etcd
  /local                        Generate the static Pod manifest file for a local, single-node local etcd instance
control-plane                 Generate all static Pod manifest files necessary to establish the control plane
  /apiserver                    Generates the kube-apiserver static Pod manifest
  /controller-manager           Generates the kube-controller-manager static Pod manifest
  /scheduler                    Generates the kube-scheduler static Pod manifest
kubelet-start                 Write kubelet settings and (re)start the kubelet
wait-control-plane            Wait for the control plane to start
upload-config                 Upload the kubeadm and kubelet configuration to a ConfigMap
  /kubeadm                      Upload the kubeadm ClusterConfiguration to a ConfigMap
  /kubelet                      Upload the kubelet component config to a ConfigMap
upload-certs                  Upload certificates to kubeadm-certs
mark-control-plane            Mark a node as a control-plane
bootstrap-token               Generates bootstrap tokens used to join a node to a cluster
kubelet-finalize              Updates settings relevant to the kubelet after TLS bootstrap
  /enable-client-cert-rotation  Enable kubelet client certificate rotation
addon                         Install required addons for passing conformance tests
  /coredns                      Install the CoreDNS addon to a Kubernetes cluster
  /kube-proxy                   Install the kube-proxy addon to a Kubernetes cluster
show-join-command             Show the join command for control-plane and worker node
```

```
kubeadm init [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | The IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-bind-port int32     Default: 6443 | |
|  | Port for the API Server to bind to. |
| --apiserver-cert-extra-sans strings | |
|  | Optional extra Subject Alternative Names (SANs) to use for the API Server serving certificate. Can be both IP addresses and DNS names. |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --certificate-key string | |
|  | Key used to encrypt the control-plane certificates in the kubeadm-certs Secret. The certificate key is a hex encoded string that is an AES key of size 32 bytes. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane-endpoint string | |
|  | Specify a stable IP address or DNS name for the control plane. |
| --cri-socket string | |
|  | Path to the CRI socket to connect. If empty kubeadm will try to auto-detect this value; use this option only if you have more than one CRI installed or if you have non-standard CRI socket. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| --feature-gates string | |
|  | A set of key=value pairs that describe feature gates for various features. Options are: ControlPlaneKubeletLocalMode=true|false (BETA - default=true) NodeLocalCRISocket=true|false (BETA - default=true) PublicKeysECDSA=true|false (DEPRECATED - default=false) RootlessControlPlane=true|false (ALPHA - default=false) WaitForAllControlPlaneComponents=true|false (default=true) |
| -h, --help | |
|  | help for init |
| --ignore-preflight-errors strings | |
|  | A list of checks whose errors will be shown as warnings. Example: 'IsPrivilegedUser,Swap'. Value 'all' ignores errors from all checks. |
| --image-repository string     Default: "registry.k8s.io" | |
|  | Choose a container registry to pull control plane images from |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |
| --node-name string | |
|  | Specify the node name. |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |
| --pod-network-cidr string | |
|  | Specify range of IP addresses for the pod network. If set, the control plane will automatically allocate CIDRs for every node. |
| --service-cidr string     Default: "10.96.0.0/12" | |
|  | Use alternative range of IP address for service VIPs. |
| --service-dns-domain string     Default: "cluster.local" | |
|  | Use alternative domain for services, e.g. "myorg.internal". |
| --skip-certificate-key-print | |
|  | Don't print the key used to encrypt the control-plane certificates. |
| --skip-phases strings | |
|  | List of phases to be skipped |
| --skip-token-print | |
|  | Skip printing of the default bootstrap token generated by 'kubeadm init'. |
| --token string | |
|  | The token to use for establishing bidirectional trust between nodes and control-plane nodes. The format is [a-z0-9]{6}.[a-z0-9]{16} - e.g. abcdef.0123456789abcdef |
| --token-ttl duration     Default: 24h0m0s | |
|  | The duration before the token is automatically deleted (e.g. 1s, 2m, 3h). If set to '0', the token will never expire |
| --upload-certs | |
|  | Upload control-plane certificates to the kubeadm-certs Secret. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Init workflow

`kubeadm init` bootstraps a Kubernetes control plane node by executing the
following steps:

1. Runs a series of pre-flight checks to validate the system state
   before making changes. Some checks only trigger warnings, others are
   considered errors and will exit kubeadm until the problem is corrected or the
   user specifies `--ignore-preflight-errors=<list-of-errors>`.
2. Generates a self-signed CA to set up identities for each component in the cluster. The user can provide their
   own CA cert and/or key by dropping it in the cert directory configured via `--cert-dir`
   (`/etc/kubernetes/pki` by default).
   The API server certs will have additional SAN entries for any `--apiserver-cert-extra-sans`
   arguments, lowercased if necessary.
3. Writes kubeconfig files in `/etc/kubernetes/` for the kubelet, the controller-manager, and the
   scheduler to connect to the API server, each with its own identity. Also
   additional kubeconfig files are written, for kubeadm as administrative entity (`admin.conf`)
   and for a super admin user that can bypass RBAC (`super-admin.conf`).
4. Generates static Pod manifests for the API server,
   controller-manager and scheduler. In case an external etcd is not provided,
   an additional static Pod manifest is generated for etcd.

   Static Pod manifests are written to `/etc/kubernetes/manifests`; the kubelet
   watches this directory for Pods to create on startup.

   Once control plane Pods are up and running, the `kubeadm init` sequence can continue.
5. Apply labels and taints to the control plane node so that no additional workloads will
   run there.
6. Generates the token that additional nodes can use to register
   themselves with a control plane in the future. Optionally, the user can provide a
   token via `--token`, as described in the
   [kubeadm token](/docs/reference/setup-tools/kubeadm/kubeadm-token/) documents.
7. Makes all the necessary configurations for allowing node joining with the
   [Bootstrap Tokens](/docs/reference/access-authn-authz/bootstrap-tokens/) and
   [TLS Bootstrap](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/)
   mechanism:

   * Write a ConfigMap for making available all the information required
     for joining, and set up related RBAC access rules.
   * Let Bootstrap Tokens access the CSR signing API.
   * Configure auto-approval for new CSR requests.

   See [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) for additional information.
8. Installs a DNS server (CoreDNS) and the kube-proxy addon components via the API server.
   In Kubernetes version 1.11 and later CoreDNS is the default DNS server.
   Please note that although the DNS server is deployed, it will not be scheduled until CNI is installed.

   > **Warning:**
   > kube-dns usage with kubeadm is deprecated as of v1.18 and is removed in v1.21.

### Using init phases with kubeadm

kubeadm allows you to create a control plane node in phases using the `kubeadm init phase` command.

To view the ordered list of phases and sub-phases you can call `kubeadm init --help`. The list
will be located at the top of the help screen and each phase will have a description next to it.
Note that by calling `kubeadm init` all of the phases and sub-phases will be executed in this exact order.

Some phases have unique flags, so if you want to have a look at the list of available options add
`--help`, for example:

```
sudo kubeadm init phase control-plane controller-manager --help
```

You can also use `--help` to see the list of sub-phases for a certain parent phase:

```
sudo kubeadm init phase control-plane --help
```

`kubeadm init` also exposes a flag called `--skip-phases` that can be used to skip certain phases.
The flag accepts a list of phase names and the names can be taken from the above ordered list.

An example:

```
sudo kubeadm init phase control-plane all --config=configfile.yaml
sudo kubeadm init phase etcd local --config=configfile.yaml
# you can now modify the control plane and etcd manifest files
sudo kubeadm init --skip-phases=control-plane,etcd --config=configfile.yaml
```

What this example would do is write the manifest files for the control plane and etcd in
`/etc/kubernetes/manifests` based on the configuration in `configfile.yaml`. This allows you to
modify the files and then skip these phases using `--skip-phases`. By calling the last command you
will create a control plane node with the custom manifest files.

FEATURE STATE:
`Kubernetes v1.22 [beta]`

Alternatively, you can use the `skipPhases` field under `InitConfiguration`.

### Using kubeadm init with a configuration file

> **Caution:**
> The configuration file is still considered beta and may change in future versions.

It's possible to configure `kubeadm init` with a configuration file instead of command
line flags, and some more advanced features may only be available as
configuration file options. This file is passed using the `--config` flag and it must
contain a `ClusterConfiguration` structure and optionally more structures separated by `---\n`.
Mixing `--config` with others flags may not be allowed in some cases.

The default configuration can be printed out using the
[kubeadm config print](/docs/reference/setup-tools/kubeadm/kubeadm-config/) command.

If your configuration is not using the latest version it is **recommended** that you migrate using
the [kubeadm config migrate](/docs/reference/setup-tools/kubeadm/kubeadm-config/) command.

For more information on the fields and usage of the configuration you can navigate to our
[API reference page](/docs/reference/config-api/kubeadm-config.v1beta4/).

### Using kubeadm init with feature gates

kubeadm supports a set of feature gates that are unique to kubeadm and can only be applied
during cluster creation with `kubeadm init`. These features can control the behavior
of the cluster. Feature gates are removed after a feature graduates to GA.

To pass a feature gate you can either use the `--feature-gates` flag for
`kubeadm init`, or you can add items into the `featureGates` field when you pass
a [configuration file](/docs/reference/config-api/kubeadm-config.v1beta4/#kubeadm-k8s-io-v1beta4-ClusterConfiguration)
using `--config`.

Passing [feature gates for core Kubernetes components](/docs/reference/command-line-tools-reference/feature-gates/)
directly to kubeadm is not supported. Instead, it is possible to pass them by
[Customizing components with the kubeadm API](/docs/setup/production-environment/tools/kubeadm/control-plane-flags/).

List of feature gates:

kubeadm feature gates

| Feature | Default | Alpha | Beta | GA |
| --- | --- | --- | --- | --- |
| `ControlPlaneKubeletLocalMode` | `true` | 1.31 | 1.33 | - |
| `NodeLocalCRISocket` | `true` | 1.32 | 1.34 | - |
| `WaitForAllControlPlaneComponents` | `true` | 1.30 | 1.33 | 1.34 |

> **Note:**
> Once a feature gate goes GA its value becomes locked to `true` by default.

Feature gate descriptions:

`ControlPlaneKubeletLocalMode`
:   With this feature gate enabled, when joining a new control plane node, kubeadm will configure the kubelet
    to connect to the local kube-apiserver. This ensures that there will not be a violation of the version skew
    policy during rolling upgrades.

`NodeLocalCRISocket`
:   With this feature gate enabled, kubeadm will read/write the CRI socket for each node from/to the file
    `/var/lib/kubelet/instance-config.yaml` instead of reading/writing it from/to the annotation
    `kubeadm.alpha.kubernetes.io/cri-socket` on the Node object. The new file is applied as an instance
    configuration patch, before any other user managed patches are applied when the `--patches` flag
    is used. It contains a single field `containerRuntimeEndpoint` from the
    [KubeletConfiguration file format](/docs/reference/config-api/kubelet-config.v1beta1/). If the feature gate
    is enabled during upgrade, but the file `/var/lib/kubelet/instance-config.yaml` does not exist yet,
    kubeadm will attempt to read the CRI socket value from the file `/var/lib/kubelet/kubeadm-flags.env`.

`WaitForAllControlPlaneComponents`
:   With this feature gate enabled, kubeadm will wait for all control plane components (kube-apiserver,
    kube-controller-manager, kube-scheduler) on a control plane node to report status 200 on their `/livez`
    or `/healthz` endpoints. These checks are performed on `https://ADDRESS:PORT/ENDPOINT`.

    * `PORT` is taken from `--secure-port` of a component.
    * `ADDRESS` is `--advertise-address` for kube-apiserver and `--bind-address` for the
      kube-controller-manager and kube-scheduler.
    * `ENDPOINT` is only `/healthz` for kube-controller-manager until it supports `/livez` as well.

    If you specify custom `ADDRESS` or `PORT` in the kubeadm configuration they will be respected.
    Without the feature gate enabled, kubeadm will only wait for the kube-apiserver
    on a control plane node to become ready. The wait process starts right after the kubelet on the host
    is started by kubeadm. You are advised to enable this feature gate in case you wish to observe a ready
    state from all control plane components during the `kubeadm init` or `kubeadm join` command execution.

List of deprecated feature gates:

kubeadm deprecated feature gates

| Feature | Default | Alpha | Beta | GA | Deprecated |
| --- | --- | --- | --- | --- | --- |
| `PublicKeysECDSA` | `false` | 1.19 | - | - | 1.31 |
| `RootlessControlPlane` | `false` | 1.22 | - | - | 1.31 |

Feature gate descriptions:

`PublicKeysECDSA`
:   Can be used to create a cluster that uses ECDSA certificates instead of the default RSA algorithm.
    Renewal of existing ECDSA certificates is also supported using `kubeadm certs renew`, but you cannot
    switch between the RSA and ECDSA algorithms on the fly or during upgrades. Kubernetes versions before v1.31
    had a bug where keys in generated kubeconfig files were set use RSA, even when you had enabled the
    `PublicKeysECDSA` feature gate. This feature gate is deprecated in favor of the `encryptionAlgorithm`
    functionality available in kubeadm v1beta4.

`RootlessControlPlane`
:   Setting this flag configures the kubeadm deployed control plane component static Pod containers
    for `kube-apiserver`, `kube-controller-manager`, `kube-scheduler` and `etcd` to run as non-root users.
    If the flag is not set, those components run as root. You can change the value of this feature gate before
    you upgrade to a newer version of Kubernetes.

List of removed feature gates:

kubeadm removed feature gates

| Feature | Alpha | Beta | GA | Removed |
| --- | --- | --- | --- | --- |
| `EtcdLearnerMode` | 1.27 | 1.29 | 1.32 | 1.33 |
| `IPv6DualStack` | 1.16 | 1.21 | 1.23 | 1.24 |
| `UnversionedKubeletConfigMap` | 1.22 | 1.23 | 1.25 | 1.26 |
| `UpgradeAddonsBeforeControlPlane` | 1.28 | - | - | 1.31 |

Feature gate descriptions:

`EtcdLearnerMode`
:   When joining a new control plane node, a new etcd member will be created
    as a learner and promoted to a voting member only after the etcd data are fully aligned.

`IPv6DualStack`
:   This flag helps to configure components dual stack when the feature is in progress. For more details on Kubernetes
    dual-stack support see [Dual-stack support with kubeadm](/docs/setup/production-environment/tools/kubeadm/dual-stack-support/).

`UnversionedKubeletConfigMap`
:   This flag controls the name of the [ConfigMap](/docs/concepts/configuration/configmap/ "An API object used to store non-confidential data in key-value pairs. Can be consumed as environment variables, command-line arguments, or configuration files in a volume.") where kubeadm stores
    kubelet configuration data. With this flag not specified or set to `true`, the ConfigMap is named `kubelet-config`.
    If you set this flag to `false`, the name of the ConfigMap includes the major and minor version for Kubernetes
    (for example: `kubelet-config-1.34`). Kubeadm ensures that RBAC rules for reading and writing
    that ConfigMap are appropriate for the value you set. When kubeadm writes this ConfigMap (during `kubeadm init`
    or `kubeadm upgrade apply`), kubeadm respects the value of `UnversionedKubeletConfigMap`. When reading that ConfigMap
    (during `kubeadm join`, `kubeadm reset`, `kubeadm upgrade`...), kubeadm attempts to use unversioned ConfigMap name first.
    If that does not succeed, kubeadm falls back to using the legacy (versioned) name for that ConfigMap.

`UpgradeAddonsBeforeControlPlane`
:   This feature gate has been removed. It was introduced in v1.28 as a deprecated feature and then removed in v1.31.
    For documentation on older versions, please switch to the corresponding website version.

### Adding kube-proxy parameters

For information about kube-proxy parameters in the kubeadm configuration see:

* [kube-proxy reference](/docs/reference/config-api/kube-proxy-config.v1alpha1/)

For information about enabling IPVS mode with kubeadm see:

* [IPVS](https://github.com/kubernetes/kubernetes/blob/master/pkg/proxy/ipvs/README.md)

### Passing custom flags to control plane components

For information about passing flags to control plane components see:

* [control-plane-flags](/docs/setup/production-environment/tools/kubeadm/control-plane-flags/)

### Running kubeadm without an Internet connection

For running kubeadm without an Internet connection you have to pre-pull the required control plane images.

You can list and pull the images using the `kubeadm config images` sub-command:

```
kubeadm config images list
kubeadm config images pull
```

You can pass `--config` to the above commands with a [kubeadm configuration file](#config-file)
to control the `kubernetesVersion` and `imageRepository` fields.

All default `registry.k8s.io` images that kubeadm requires support multiple architectures.

### Using custom images

By default, kubeadm pulls images from `registry.k8s.io`. If the
requested Kubernetes version is a CI label (such as `ci/latest`)
`gcr.io/k8s-staging-ci-images` is used.

You can override this behavior by using [kubeadm with a configuration file](#config-file).
Allowed customization are:

* To provide `kubernetesVersion` which affects the version of the images.
* To provide an alternative `imageRepository` to be used instead of
  `registry.k8s.io`.
* To provide a specific `imageRepository` and `imageTag` for etcd or CoreDNS.

Image paths between the default `registry.k8s.io` and a custom repository specified using
`imageRepository` may differ for backwards compatibility reasons. For example,
one image might have a subpath at `registry.k8s.io/subpath/image`, but be defaulted
to `my.customrepository.io/image` when using a custom repository.

To ensure you push the images to your custom repository in paths that kubeadm
can consume, you must:

* Pull images from the defaults paths at `registry.k8s.io` using `kubeadm config images {list|pull}`.
* Push images to the paths from `kubeadm config images list --config=config.yaml`,
  where `config.yaml` contains the custom `imageRepository`, and/or `imageTag` for etcd and CoreDNS.
* Pass the same `config.yaml` to `kubeadm init`.

#### Custom sandbox (pause) images

To set a custom image for these you need to configure this in your
[container runtime](/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.") to use the image.
Consult the documentation for your container runtime to find out how to change this setting;
for selected container runtimes, you can also find advice within the
[Container Runtimes](/docs/setup/production-environment/container-runtimes/) topic.

### Uploading control plane certificates to the cluster

By adding the flag `--upload-certs` to `kubeadm init` you can temporary upload
the control plane certificates to a Secret in the cluster. Please note that this Secret
will expire automatically after 2 hours. The certificates are encrypted using
a 32byte key that can be specified using `--certificate-key`. The same key can be used
to download the certificates when additional control plane nodes are joining, by passing
`--control-plane` and `--certificate-key` to `kubeadm join`.

The following phase command can be used to re-upload the certificates after expiration:

```
kubeadm init phase upload-certs --upload-certs --config=SOME_YAML_FILE
```

> **Note:**
> A predefined `certificateKey` can be provided in `InitConfiguration` when passing the
> [configuration file](/docs/reference/config-api/kubeadm-config.v1beta4/) with `--config`.

If a predefined certificate key is not passed to `kubeadm init` and
`kubeadm init phase upload-certs` a new key will be generated automatically.

The following command can be used to generate a new key on demand:

```
kubeadm certs certificate-key
```

### Certificate management with kubeadm

For detailed information on certificate management with kubeadm see
[Certificate Management with kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/).
The document includes information about using external CA, custom certificates
and certificate renewal.

### Managing the kubeadm drop-in file for the kubelet

The `kubeadm` package ships with a configuration file for running the `kubelet` by `systemd`.
Note that the kubeadm CLI never touches this drop-in file. This drop-in file is part of the kubeadm
DEB/RPM package.

For further information, see
[Managing the kubeadm drop-in file for systemd](/docs/setup/production-environment/tools/kubeadm/kubelet-integration/#the-kubelet-drop-in-file-for-systemd).

### Use kubeadm with CRI runtimes

By default, kubeadm attempts to detect your container runtime. For more details on this detection,
see the [kubeadm CRI installation guide](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-runtime).

### Setting the node name

By default, kubeadm assigns a node name based on a machine's host address.
You can override this setting with the `--node-name` flag.
The flag passes the appropriate [`--hostname-override`](/docs/reference/command-line-tools-reference/kubelet/#options)
value to the kubelet.

Be aware that overriding the hostname can
[interfere with cloud providers](https://github.com/kubernetes/website/pull/8873).

### Automating kubeadm

Rather than copying the token you obtained from `kubeadm init` to each node, as
in the [basic kubeadm tutorial](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/),
you can parallelize the token distribution for easier automation. To implement this automation,
you must know the IP address that the control plane node will have after it is started, or use a
DNS name or an address of a load balancer.

1. Generate a token. This token must have the form `<6 character string>.<16 character string>`.
   More formally, it must match the regex: `[a-z0-9]{6}\.[a-z0-9]{16}`.

   kubeadm can generate a token for you:

   ```
   kubeadm token generate
   ```
2. Start both the control plane node and the worker nodes concurrently with this token.
   As they come up they should find each other and form the cluster. The same
   `--token` argument can be used on both `kubeadm init` and `kubeadm join`.
3. Similar can be done for `--certificate-key` when joining additional control plane
   nodes. The key can be generated using:

   ```
   kubeadm certs certificate-key
   ```

Once the cluster is up, you can use the `/etc/kubernetes/admin.conf` file from
a control plane node to talk to the cluster with administrator credentials or
[Generating kubeconfig files for additional users](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#kubeconfig-additional-users).

Note that this style of bootstrap has some relaxed security guarantees because
it does not allow the root CA hash to be validated with
`--discovery-token-ca-cert-hash` (since it's not generated when the nodes are provisioned).
For details, see the [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/).

## What's next

* [kubeadm init phase](/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/) to understand more about
  `kubeadm init` phases
* [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) to bootstrap a Kubernetes
  worker node and join it to the cluster
* [kubeadm upgrade](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/) to upgrade a Kubernetes
  cluster to a newer version
* [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) to revert any changes made
  to this host by `kubeadm init` or `kubeadm join`

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
