# Local Files And Paths Used By The Kubelet

The [kubelet](/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") is mostly a stateless
process running on a Kubernetes [node](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.").
This document outlines files that kubelet reads and writes.

> **Note:**
> This document is for informational purpose and not describing any guaranteed behaviors or APIs.
> It lists resources used by the kubelet, which is an implementation detail and a subject to change at any release.

The kubelet typically uses the [control plane](/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.") as
the source of truth on what needs to run on the Node, and the
[container runtime](/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.") to retrieve
the current state of containers. So long as you provide a *kubeconfig* (API client configuration)
to the kubelet, the kubelet does connect to your control plane; otherwise the node operates in
*standalone mode*.

On Linux nodes, the kubelet also relies on reading cgroups and various system files to collect metrics.

On Windows nodes, the kubelet collects metrics via a different mechanism that does not rely on
paths.

There are also a few other files that are used by the kubelet as well,
as kubelet communicates using local Unix-domain sockets. Some are sockets that the
kubelet listens on, and for other sockets the kubelet discovers them and then connects
as a client.

> **Note:**
> This page lists paths as Linux paths, which map to the Windows paths by adding a root disk
> `C:\` in place of `/` (unless specified otherwise).
> For example, `/var/lib/kubelet/device-plugins` maps to `C:\var\lib\kubelet\device-plugins`.

## Configuration

### Kubelet configuration files

The path to the kubelet configuration file can be configured
using the command line argument `--config`. The kubelet also supports
[drop-in configuration files](/docs/tasks/administer-cluster/kubelet-config-file/#kubelet-conf-d)
to enhance configuration.

### Certificates

Certificates and private keys are typically located at `/var/lib/kubelet/pki`,
but can be configured using the `--cert-dir` kubelet command line argument.
Names of certificate files are also configurable.

### Manifests

Manifests for static pods are typically located in `/etc/kubernetes/manifests`.
Location can be configured using the `staticPodPath` kubelet configuration option.

### Systemd unit settings

When kubelet is running as a systemd unit, some kubelet configuration may be declared
in systemd unit settings file. Typically it includes:

* command line arguments to [run kubelet](/docs/reference/command-line-tools-reference/kubelet/)
* environment variables, used by kubelet or [configuring golang runtime](https://pkg.go.dev/runtime#hdr-Environment_Variables)

## State

### Checkpoint files for resource managers

All resource managers keep the mapping of Pods to allocated resources in state files.
State files are located in the kubelet's base directory, also termed the *root directory*
(but not the same as `/`, the node root directory). You can configure the base directory
for the kubelet
using the kubelet command line argument `--root-dir`.

Names of files:

* `memory_manager_state` for the [Memory Manager](/docs/tasks/administer-cluster/memory-manager/)
* `cpu_manager_state` for the [CPU Manager](/docs/tasks/administer-cluster/cpu-management-policies/)
* `dra_manager_state` for [DRA](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)

### Checkpoint file for device manager

Device manager creates checkpoints in the same directory with socket files: `/var/lib/kubelet/device-plugins/`.
The name of a checkpoint file is `kubelet_internal_checkpoint` for
[Device Manager](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-integration-with-the-topology-manager)

### Pod resource checkpoints

FEATURE STATE:
`Kubernetes v1.33 [beta]`(enabled by default)

If a node has enabled the `InPlacePodVerticalScaling`[feature gate](/docs/reference/command-line-tools-reference/feature-gates/),
the kubelet stores a local record of *allocated* and *actuated* Pod resources.
See [Resize CPU and Memory Resources assigned to Containers](/docs/tasks/configure-pod-container/resize-container-resources/)
for more details on how these records are used.

Names of files:

* `allocated_pods_state` records the resources allocated to each pod running on the node
* `actuated_pods_state` records the resources that have been accepted by the runtime
  for each pod pod running on the node

The files are located within the kubelet base directory
(`/var/lib/kubelet` by default on Linux; configurable using `--root-dir`).

### Container runtime

Kubelet communicates with the container runtime using socket configured via the
configuration parameters:

* `containerRuntimeEndpoint` for runtime operations
* `imageServiceEndpoint` for image management operations

The actual values of those endpoints depend on the container runtime being used.

### Device plugins

The kubelet exposes a socket at the path `/var/lib/kubelet/device-plugins/kubelet.sock` for
various [Device Plugins to register](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-implementation).

When a device plugin registers itself, it provides its socket path for the kubelet to connect.

The device plugin socket should be in the directory `device-plugins` within the kubelet base
directory. On a typical Linux node, this means `/var/lib/kubelet/device-plugins`.

### Pod resources API

[Pod Resources API](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#monitoring-device-plugin-resources)
will be exposed at the path `/var/lib/kubelet/pod-resources`.

### DRA, CSI, and Device plugins

The kubelet looks for socket files created by device plugins managed via [DRA](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/),
device manager, or storage plugins, and then attempts to connect
to these sockets. The directory that the kubelet looks in is `plugins_registry` within the kubelet base
directory, so on a typical Linux node this means `/var/lib/kubelet/plugins_registry`.

Note, for the device plugins there are two alternative registration mechanisms
Only one should be used for a given plugin.

The types of plugins that can place socket files into that directory are:

* CSI plugins
* DRA plugins
* Device Manager plugins

(typically `/var/lib/kubelet/plugins_registry`).

### Graceful node shutdown

FEATURE STATE:
`Kubernetes v1.21 [beta]`(enabled by default)

[Graceful node shutdown](/docs/concepts/cluster-administration/node-shutdown/#graceful-node-shutdown)
stores state locally at `/var/lib/kubelet/graceful_node_shutdown_state`.

### Image Pull Records

FEATURE STATE:
`Kubernetes v1.33 [alpha]`(disabled by default)

The kubelet stores records of attempted and successful image pulls, and uses it
to verify that the image was previously successfully pulled with the same credentials.

These records are cached as files in the `image_registry` directory within
the kubelet base directory. On a typical Linux node, this means `/var/lib/kubelet/image_manager`.
There are two subdirectories to `image_manager`:

* `pulling` - stores records about images the Kubelet is attempting to pull.
* `pulled` - stores records about images that were successfully pulled by the Kubelet,
  along with metadata about the credentials used for the pulls.

See [Ensure Image Pull Credential Verification](/docs/concepts/containers/images/#ensureimagepullcredentialverification)
for details.

## Security profiles & configuration

### Seccomp

Seccomp profile files referenced from Pods should be placed in `/var/lib/kubelet/seccomp`.
See the [seccomp reference](/docs/reference/node/seccomp/) for details.

### AppArmor

The kubelet does not load or refer to AppArmor profiles by a Kubernetes-specific path.
AppArmor profiles are loaded via the node operating system rather then referenced by their path.

## Locking

FEATURE STATE:
`Kubernetes v1.2 [alpha]`

A lock file for the kubelet; typically `/var/run/kubelet.lock`. The kubelet uses this to ensure
that two different kubelets don't try to run in conflict with each other.
You can configure the path to the lock file using the the `--lock-file` kubelet command line argument.

If two kubelets on the same node use a different value for the lock file path, they will not be able to
detect a conflict when both are running.

## What's next

* Learn about the kubelet [command line arguments](/docs/reference/command-line-tools-reference/kubelet/).
* Review the [Kubelet Configuration (v1beta1) reference](/docs/reference/config-api/kubelet-config.v1beta1/)

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
