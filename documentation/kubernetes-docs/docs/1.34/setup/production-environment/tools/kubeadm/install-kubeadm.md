# Installing kubeadm

![](/images/kubeadm-stacked-color.png)
This page shows how to install the `kubeadm` toolbox.
For information on how to create a cluster with kubeadm once you have performed this installation process,
see the [Creating a cluster with kubeadm](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/) page.

This installation guide is for Kubernetes v1.34. If you want to use a different Kubernetes version, please refer to the following pages instead:

* [Installing kubeadm (Kubernetes v1.36)](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
* [Installing kubeadm (Kubernetes v1.35)](https://v1-35.docs.kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
* [Installing kubeadm (Kubernetes v1.33)](https://v1-33.docs.kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
* [Installing kubeadm (Kubernetes v1.32)](https://v1-32.docs.kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)

## Before you begin

* A compatible Linux host. The Kubernetes project provides generic instructions for Linux distributions
  based on Debian and Red Hat, and those distributions without a package manager.
* 2 GB or more of RAM per machine (any less will leave little room for your apps).
* 2 CPUs or more for control plane machines.
* Full network connectivity between all machines in the cluster (public or private network is fine).
* Unique hostname, MAC address, and product_uuid for every node. See [here](#verify-mac-address) for more details.
* Certain ports are open on your machines. See [here](#check-required-ports) for more details.

> **Note:**
> The `kubeadm` installation is done via binaries that use dynamic linking and assumes that your target system provides `glibc`.
> This is a reasonable assumption on many Linux distributions (including Debian, Ubuntu, Fedora, CentOS, etc.)
> but it is not always the case with custom and lightweight distributions which don't include `glibc` by default, such as Alpine Linux.
> The expectation is that the distribution either includes `glibc` or a
> [compatibility layer](https://wiki.alpinelinux.org/wiki/Running_glibc_programs)
> that provides the expected symbols.

## Check your OS version

> **Note:**
> **Note:** This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](/docs/contribute/style/content-guide/#third-party-content) before submitting a change. [More information.](#third-party-content-disclaimer)

* Linux
  * Windows

* The kubeadm project supports LTS kernels. See [List of LTS kernels](https://www.kernel.org/category/releases.html).
* You can get the kernel version using the command `uname -r`

For more information, see [Linux Kernel Requirements](/docs/reference/node/kernel-version-requirements/).

* The kubeadm project supports recent kernel versions. For a list of recent kernels, see [Windows Server Release Information](https://learn.microsoft.com/en-us/windows/release-health/windows-server-release-info).
* You can get the kernel version (also called the OS version) using the command `systeminfo`

For more information, see [Windows OS version compatibility](/docs/concepts/windows/intro/#windows-os-version-support).

A Kubernetes cluster created by kubeadm depends on software that use kernel features.
This software includes, but is not limited to the
[container runtime](/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers."),
the [kubelet](/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod."), and a [Container Network Interface](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/ "Container network interface (CNI) plugins are a type of Network plugin that adheres to the appc/CNI specification.") plugin.

To help you avoid unexpected errors as a result of an unsupported kernel version, kubeadm runs the `SystemVerification`
pre-flight check. This check fails if the kernel version is not supported.

You may choose to skip the check, if you know that your kernel
provides the required features, even though kubeadm does not support its version.

## Verify the MAC address and product_uuid are unique for every node

* You can get the MAC address of the network interfaces using the command `ip link` or `ifconfig -a`
* The product_uuid can be checked by using the command `sudo cat /sys/class/dmi/id/product_uuid`

It is very likely that hardware devices will have unique addresses, although some virtual machines may have
identical values. Kubernetes uses these values to uniquely identify the nodes in the cluster.
If these values are not unique to each node, the installation process
may [fail](https://github.com/kubernetes/kubeadm/issues/31).

## Check network adapters

If you have more than one network adapter, and your Kubernetes components are not reachable on the default
route, we recommend you add IP route(s) so Kubernetes cluster addresses go via the appropriate adapter.

## Check required ports

These [required ports](/docs/reference/networking/ports-and-protocols/)
need to be open in order for Kubernetes components to communicate with each other.
You can use tools like [netcat](https://netcat.sourceforge.net) to check if a port is open. For example:

```
nc 127.0.0.1 6443 -zv -w 2
```

The pod network plugin you use may also require certain ports to be
open. Since this differs with each pod network plugin, please see the
documentation for the plugins about what port(s) those need.

## Swap configuration

The default behavior of a kubelet is to fail to start if swap memory is detected on a node.
This means that swap should either be disabled or tolerated by kubelet.

* To tolerate swap, add `failSwapOn: false` to kubelet configuration or as a command line argument.
  Note: even if `failSwapOn: false` is provided, workloads wouldn't have swap access by default.
  This can be changed by setting a `swapBehavior`, again in the kubelet configuration file. To use swap,
  set a `swapBehavior` other than the default `NoSwap` setting.
  See [Swap memory management](/docs/concepts/cluster-administration/swap-memory-management/) for more details.
* To disable swap, `sudo swapoff -a` can be used to disable swapping temporarily.
  To make this change persistent across reboots, make sure swap is disabled in
  config files like `/etc/fstab`, `systemd.swap`, depending how it was configured on your system.

## Installing a container runtime

To run containers in Pods, Kubernetes uses a
[container runtime](/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.").

By default, Kubernetes uses the
[Container Runtime Interface](/docs/concepts/architecture/cri "Protocol for communication between the kubelet and the local container runtime.") (CRI)
to interface with your chosen container runtime.

If you don't specify a runtime, kubeadm automatically tries to detect an installed
container runtime by scanning through a list of known endpoints.

If multiple or no container runtimes are detected kubeadm will throw an error
and will request that you specify which one you want to use.

See [container runtimes](/docs/setup/production-environment/container-runtimes/)
for more information.

> **Note:**
> Docker Engine does not implement the [CRI](/docs/concepts/architecture/cri/)
> which is a requirement for a container runtime to work with Kubernetes.
> For that reason, an additional service [cri-dockerd](https://mirantis.github.io/cri-dockerd/)
> has to be installed. cri-dockerd is a project based on the legacy built-in
> Docker Engine support that was [removed](/dockershim) from the kubelet in version 1.24.

The tables below include the known endpoints for supported operating systems:

* Linux
  * Windows

Linux container runtimes

| Runtime | Path to Unix domain socket |
| --- | --- |
| containerd | `unix:///var/run/containerd/containerd.sock` |
| CRI-O | `unix:///var/run/crio/crio.sock` |
| Docker Engine (using cri-dockerd) | `unix:///var/run/cri-dockerd.sock` |

Windows container runtimes

| Runtime | Path to Windows named pipe |
| --- | --- |
| containerd | `npipe:////./pipe/containerd-containerd` |
| Docker Engine (using cri-dockerd) | `npipe:////./pipe/cri-dockerd` |

## Installing kubeadm, kubelet and kubectl

You will install these packages on all of your machines:

* `kubeadm`: the command to bootstrap the cluster.
* `kubelet`: the component that runs on all of the machines in your cluster
  and does things like starting pods and containers.
* `kubectl`: the command line util to talk to your cluster.

kubeadm **will not** install or manage `kubelet` or `kubectl` for you, so you will
need to ensure they match the version of the Kubernetes control plane you want
kubeadm to install for you. If you do not, there is a risk of a version skew occurring that
can lead to unexpected, buggy behaviour. However, *one* minor version skew between the
kubelet and the control plane is supported, but the kubelet version may never exceed the API
server version. For example, the kubelet running 1.7.0 should be fully compatible with a 1.8.0 API server,
but not vice versa.

For information about installing `kubectl`, see [Install and set up kubectl](/docs/tasks/tools/).

> **Warning:**
> These instructions exclude all Kubernetes packages from any system upgrades.
> This is because kubeadm and Kubernetes require
> [special attention to upgrade](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/).

For more information on version skews, see:

* Kubernetes [version and version-skew policy](/docs/setup/release/version-skew-policy/)
* Kubeadm-specific [version skew policy](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#version-skew-policy)

> **Note:**
> **Note:** The legacy package repositories (`apt.kubernetes.io` and `yum.kubernetes.io`) have been
> [deprecated and frozen starting from September 13, 2023](/blog/2023/08/31/legacy-package-repository-deprecation/).
> **Using the [new package repositories hosted at `pkgs.k8s.io`](/blog/2023/08/15/pkgs-k8s-io-introduction/)
> is strongly recommended and required in order to install Kubernetes versions released after September 13, 2023.**
> The deprecated legacy repositories, and their contents, might be removed at any time in the future and without
> a further notice period. The new package repositories provide downloads for Kubernetes versions starting with v1.24.0.

> **Note:**
> There's a dedicated package repository for each Kubernetes minor version. If you want to install
> a minor version other than v1.34, please see the installation guide for
> your desired minor version.

* Debian-based distributions
  * Red Hat-based distributions
    * Without a package manager

These instructions are for Kubernetes v1.34.

1. Update the `apt` package index and install packages needed to use the Kubernetes `apt` repository:

   ```
   sudo apt-get update
   # apt-transport-https may be a dummy package; if so, you can skip that package
   sudo apt-get install -y apt-transport-https ca-certificates curl gpg
   ```
2. Download the public signing key for the Kubernetes package repositories.
   The same signing key is used for all repositories so you can disregard the version in the URL:

   ```
   # If the directory `/etc/apt/keyrings` does not exist, it should be created before the curl command, read the note below.
   # sudo mkdir -p -m 755 /etc/apt/keyrings
   curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.34/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
   ```

> **Note:**
> In releases older than Debian 12 and Ubuntu 22.04, directory `/etc/apt/keyrings` does not
> exist by default, and it should be created before the curl command.

3. Add the appropriate Kubernetes `apt` repository. Please note that this repository have packages
   only for Kubernetes 1.34; for other Kubernetes minor versions, you need to
   change the Kubernetes minor version in the URL to match your desired minor version
   (you should also check that you are reading the documentation for the version of Kubernetes
   that you plan to install).

   ```
   # This overwrites any existing configuration in /etc/apt/sources.list.d/kubernetes.list
   echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.34/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
   ```
4. Update the `apt` package index, install kubelet, kubeadm and kubectl, and pin their version:

   ```
   sudo apt-get update
   sudo apt-get install -y kubelet kubeadm kubectl
   sudo apt-mark hold kubelet kubeadm kubectl
   ```
5. (Optional) Enable the kubelet service before running kubeadm:

   ```
   sudo systemctl enable --now kubelet
   ```

1. Set SELinux to `permissive` mode:

   These instructions are for Kubernetes 1.34.

   ```
   # Set SELinux in permissive mode (effectively disabling it)
   sudo setenforce 0
   sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
   ```

> **Caution:**
> * Setting SELinux in permissive mode by running `setenforce 0` and `sed ...`
> effectively disables it. This is required to allow containers to access the host
> filesystem; for example, some cluster network plugins require that. You have to
> do this until SELinux support is improved in the kubelet.
> * You can leave SELinux enabled if you know how to configure it but it may require
> settings that are not supported by kubeadm.

2. Add the Kubernetes `yum` repository. The `exclude` parameter in the
   repository definition ensures that the packages related to Kubernetes are
   not upgraded upon running `yum update` as there's a special procedure that
   must be followed for upgrading Kubernetes. Please note that this repository
   have packages only for Kubernetes 1.34; for other
   Kubernetes minor versions, you need to change the Kubernetes minor version
   in the URL to match your desired minor version (you should also check that
   you are reading the documentation for the version of Kubernetes that you
   plan to install).

   ```
   # This overwrites any existing configuration in /etc/yum.repos.d/kubernetes.repo
   cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
   [kubernetes]
   name=Kubernetes
   baseurl=https://pkgs.k8s.io/core:/stable:/v1.34/rpm/
   enabled=1
   gpgcheck=1
   gpgkey=https://pkgs.k8s.io/core:/stable:/v1.34/rpm/repodata/repomd.xml.key
   exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
   EOF
   ```
3. Install kubelet, kubeadm and kubectl:

   For systems with DNF:

   ```
   sudo yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
   ```

   For systems with DNF5:

   ```
   sudo yum install -y kubelet kubeadm kubectl --setopt=disable_excludes=kubernetes
   ```
4. (Optional) Enable the kubelet service before running kubeadm:

   ```
   sudo systemctl enable --now kubelet
   ```

Install CNI plugins (required for most pod network):

```
CNI_PLUGINS_VERSION="v1.3.0"
ARCH="amd64"
DEST="/opt/cni/bin"
sudo mkdir -p "$DEST"
curl -L "https://github.com/containernetworking/plugins/releases/download/${CNI_PLUGINS_VERSION}/cni-plugins-linux-${ARCH}-${CNI_PLUGINS_VERSION}.tgz" | sudo tar -C "$DEST" -xz
```

Define the directory to download command files:

> **Note:**
> The `DOWNLOAD_DIR` variable must be set to a writable directory.
> If you are running Flatcar Container Linux, set `DOWNLOAD_DIR="/opt/bin"`.

```
DOWNLOAD_DIR="/usr/local/bin"
sudo mkdir -p "$DOWNLOAD_DIR"
```

Optionally install crictl (required for interaction with the Container Runtime Interface (CRI), optional for kubeadm):

```
CRICTL_VERSION="v1.31.0"
ARCH="amd64"
curl -L "https://github.com/kubernetes-sigs/cri-tools/releases/download/${CRICTL_VERSION}/crictl-${CRICTL_VERSION}-linux-${ARCH}.tar.gz" | sudo tar -C $DOWNLOAD_DIR -xz
```

Install `kubeadm`, `kubelet` and add a `kubelet` systemd service:

```
RELEASE="$(curl -sSL https://dl.k8s.io/release/stable.txt)"
ARCH="amd64"
cd $DOWNLOAD_DIR
sudo curl -L --remote-name-all https://dl.k8s.io/release/${RELEASE}/bin/linux/${ARCH}/{kubeadm,kubelet}
sudo chmod +x {kubeadm,kubelet}

RELEASE_VERSION="v0.16.2"
curl -sSL "https://raw.githubusercontent.com/kubernetes/release/${RELEASE_VERSION}/cmd/krel/templates/latest/kubelet/kubelet.service" | sed "s:/usr/bin:${DOWNLOAD_DIR}:g" | sudo tee /usr/lib/systemd/system/kubelet.service
sudo mkdir -p /usr/lib/systemd/system/kubelet.service.d
curl -sSL "https://raw.githubusercontent.com/kubernetes/release/${RELEASE_VERSION}/cmd/krel/templates/latest/kubeadm/10-kubeadm.conf" | sed "s:/usr/bin:${DOWNLOAD_DIR}:g" | sudo tee /usr/lib/systemd/system/kubelet.service.d/10-kubeadm.conf
```

> **Note:**
> Please refer to the note in the [Before you begin](#before-you-begin) section for Linux distributions
> that do not include `glibc` by default.

Install `kubectl` by following the instructions on [Install Tools page](/docs/tasks/tools/#kubectl).

Optionally, enable the kubelet service before running kubeadm:

```
sudo systemctl enable --now kubelet
```

> **Note:**
> The Flatcar Container Linux distribution mounts the `/usr` directory as a read-only filesystem.
> Before bootstrapping your cluster, you need to take additional steps to configure a writable directory.
> See the [Kubeadm Troubleshooting guide](/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/#usr-mounted-read-only)
> to learn how to set up a writable directory.

The kubelet is now restarting every few seconds, as it waits in a crashloop for
kubeadm to tell it what to do.

## Configuring a cgroup driver

Both the container runtime and the kubelet have a property called
["cgroup driver"](/docs/setup/production-environment/container-runtimes/#cgroup-drivers), which is important
for the management of cgroups on Linux machines.

> **Warning:**
> Matching the container runtime and kubelet cgroup drivers is required or otherwise the kubelet process will fail.
>
> See [Configuring a cgroup driver](/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/) for more details.

## Troubleshooting

If you are running into difficulties with kubeadm, please consult our
[troubleshooting docs](/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/).

## What's next

* [Using kubeadm to Create a Cluster](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)

Items on this page refer to third party products or projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for those third-party products or projects. See the [CNCF website guidelines](https://github.com/cncf/foundation/blob/master/website-guidelines.md) for more details.

You should read the [content guide](/docs/contribute/style/content-guide/#third-party-content) before proposing a change that adds an extra third-party link.

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
