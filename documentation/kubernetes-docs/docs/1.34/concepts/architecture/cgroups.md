# About cgroup v2

On Linux, [control groups](/docs/reference/glossary/?all=true#term-cgroup "A group of Linux processes with optional resource isolation, accounting and limits.")
constrain resources that are allocated to processes.

The [kubelet](/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") and the
underlying container runtime need to interface with cgroups to enforce
[resource management for pods and containers](/docs/concepts/configuration/manage-resources-containers/) which
includes cpu/memory requests and limits for containerized workloads.

There are two versions of cgroups in Linux: cgroup v1 and cgroup v2. cgroup v2 is
the new generation of the `cgroup` API.

## What is cgroup v2?

FEATURE STATE:
`Kubernetes v1.25 [stable]`

cgroup v2 is the next version of the Linux `cgroup` API. cgroup v2 provides a
unified control system with enhanced resource management
capabilities.

cgroup v2 offers several improvements over cgroup v1, such as the following:

* Single unified hierarchy design in API
* Safer sub-tree delegation to containers
* Newer features like [Pressure Stall Information](https://www.kernel.org/doc/html/latest/accounting/psi.html)
* Enhanced resource allocation management and isolation across multiple resources
  + Unified accounting for different types of memory allocations (network memory, kernel memory, etc)
  + Accounting for non-immediate resource changes such as page cache write backs

Some Kubernetes features exclusively use cgroup v2 for enhanced resource
management and isolation. For example, the
[MemoryQoS](/docs/concepts/workloads/pods/pod-qos/#memory-qos-with-cgroup-v2) feature improves memory QoS
and relies on cgroup v2 primitives.

## Using cgroup v2

The recommended way to use cgroup v2 is to use a Linux distribution that
enables and uses cgroup v2 by default.

To check if your distribution uses cgroup v2, refer to [Identify cgroup version on Linux nodes](#check-cgroup-version).

### Requirements

cgroup v2 has the following requirements:

* OS distribution enables cgroup v2
* Linux Kernel version is 5.8 or later
* Container runtime supports cgroup v2. For example:
  + [containerd](https://containerd.io/) v1.4 and later
  + [cri-o](https://cri-o.io/) v1.20 and later
* The kubelet and the container runtime are configured to use the [systemd cgroup driver](/docs/setup/production-environment/container-runtimes/#systemd-cgroup-driver)

### Linux Distribution cgroup v2 support

For a list of Linux distributions that use cgroup v2, refer to the [cgroup v2 documentation](https://github.com/opencontainers/runc/blob/main/docs/cgroup-v2.md)

* Container Optimized OS (since M97)
* Ubuntu (since 21.10, 22.04+ recommended)
* Debian GNU/Linux (since Debian 11 bullseye)
* Fedora (since 31)
* Arch Linux (since April 2021)
* RHEL and RHEL-like distributions (since 9)

To check if your distribution is using cgroup v2, refer to your distribution's
documentation or follow the instructions in [Identify the cgroup version on Linux nodes](#check-cgroup-version).

You can also enable cgroup v2 manually on your Linux distribution by modifying
the kernel cmdline boot arguments. If your distribution uses GRUB,
`systemd.unified_cgroup_hierarchy=1` should be added in `GRUB_CMDLINE_LINUX`
under `/etc/default/grub`, followed by `sudo update-grub`. However, the
recommended approach is to use a distribution that already enables cgroup v2 by
default.

### Migrating to cgroup v2

To migrate to cgroup v2, ensure that you meet the [requirements](#requirements), then upgrade
to a kernel version that enables cgroup v2 by default.

The kubelet automatically detects that the OS is running on cgroup v2 and
performs accordingly with no additional configuration required.

There should not be any noticeable difference in the user experience when
switching to cgroup v2, unless users are accessing the cgroup file system
directly, either on the node or from within the containers.

cgroup v2 uses a different API than cgroup v1, so if there are any
applications that directly access the cgroup file system, they need to be
updated to newer versions that support cgroup v2. For example:

* Some third-party monitoring and security agents may depend on the cgroup filesystem.
  Update these agents to versions that support cgroup v2.
* If you run [cAdvisor](https://github.com/google/cadvisor) as a stand-alone
  DaemonSet for monitoring pods and containers, update it to v0.43.0 or later.
* If you deploy Java applications, prefer to use versions which fully support cgroup v2:
  + [OpenJDK / HotSpot](https://bugs.openjdk.org/browse/JDK-8230305): jdk8u372, 11.0.16, 15 and later
  + [IBM Semeru Runtimes](https://www.ibm.com/support/pages/apar/IJ46681): 8.0.382.0, 11.0.20.0, 17.0.8.0, and later
  + [IBM Java](https://www.ibm.com/support/pages/apar/IJ46681): 8.0.8.6 and later
* If you are using the [uber-go/automaxprocs](https://github.com/uber-go/automaxprocs) package, make sure
  the version you use is v1.5.1 or higher.

## Identify the cgroup version on Linux Nodes

The cgroup version depends on the Linux distribution being used and the
default cgroup version configured on the OS. To check which cgroup version your
distribution uses, run the `stat -fc %T /sys/fs/cgroup/` command on
the node:

```
stat -fc %T /sys/fs/cgroup/
```

For cgroup v2, the output is `cgroup2fs`.

For cgroup v1, the output is `tmpfs.`

## What's next

* Learn more about [cgroups](https://man7.org/linux/man-pages/man7/cgroups.7.html)
* Learn more about [container runtime](/docs/concepts/architecture/cri)
* Learn more about [cgroup drivers](/docs/setup/production-environment/container-runtimes/#cgroup-drivers)

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
