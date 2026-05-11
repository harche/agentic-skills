# Linux Kernel Version Requirements

> **Note:**
> **Note:** This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](/docs/contribute/style/content-guide/#third-party-content) before submitting a change. [More information.](#third-party-content-disclaimer)

Many features rely on specific kernel functionalities and have minimum kernel version requirements.
However, relying solely on kernel version numbers may not be sufficient
for certain operating system distributions,
as maintainers for distributions such as RHEL, Ubuntu and SUSE often backport selected features
to older kernel releases (retaining the older kernel version).

## Pod sysctls

On Linux, the `sysctl()` system call configures kernel parameters at run time. There is a command
line tool named `sysctl` that you can use to configure these parameters, and many are exposed via
the `proc` filesystem.

Some sysctls are only available if you have a modern enough kernel.

The following sysctls have a minimal kernel version requirement,
and are supported in the [safe set](/docs/tasks/administer-cluster/sysctl-cluster/#safe-and-unsafe-sysctls):

* `net.ipv4.ip_local_reserved_ports` (since Kubernetes 1.27, needs kernel 3.16+);
* `net.ipv4.tcp_keepalive_time` (since Kubernetes 1.29, needs kernel 4.5+);
* `net.ipv4.tcp_fin_timeout` (since Kubernetes 1.29, needs kernel 4.6+);
* `net.ipv4.tcp_keepalive_intvl` (since Kubernetes 1.29, needs kernel 4.5+);
* `net.ipv4.tcp_keepalive_probes` (since Kubernetes 1.29, needs kernel 4.5+);
* `net.ipv4.tcp_syncookies` (namespaced since kernel 4.6+).
* `net.ipv4.tcp_rmem` (since Kubernetes 1.32, needs kernel 4.15+).
* `net.ipv4.tcp_wmem` (since Kubernetes 1.32, needs kernel 4.15+).
* `net.ipv4.vs.conn_reuse_mode` (used in `ipvs` proxy mode, needs kernel 4.1+);

### kube proxy `nftables` proxy mode

For Kubernetes 1.34, the
[`nftables` mode](/docs/reference/networking/virtual-ips/#proxy-mode-nftables) of kube-proxy requires
version 1.0.1 or later
of the nft command-line tool, as well as kernel 5.13 or later.

For testing/development purposes, you can use older kernels, as far back as 5.4 if you set the
`nftables.skipKernelVersionCheck` option in the kube-proxy config.
But this is not recommended in production since it may cause problems with other nftables
users on the system.

## Version 2 control groups

Kubernetes cgroup v1 support is in maintained mode starting from Kubernetes v1.31; using cgroup v2
is recommended.
In [Linux 5.8](https://github.com/torvalds/linux/commit/4a7e89c5ec0238017a757131eb9ab8dc111f961c), the system-level `cpu.stat` file was added to the root cgroup for convenience.

In runc document, Kernel older than 5.2 is not recommended due to lack of freezer.

## Pressure Stall Information (PSI)

[Pressure Stall Information](/docs/reference/instrumentation/understand-psi-metrics/) is supported in Linux kernel versions 4.20 and up, but requires the following configuration:

* The kernel must be compiled with the `CONFIG_PSI=y` option. Most modern distributions enable this by default. You can check your kernel's configuration by running `zgrep CONFIG_PSI /proc/config.gz`.
* Some Linux distributions may compile PSI into the kernel but disable it by default. If so, you need to enable it at boot time by adding the `psi=1` parameter to the kernel command line.

## Other kernel requirements

Some features may depend on new kernel functionalities and have specific kernel requirements:

1. [Recursive read only mount](/docs/concepts/storage/volumes/#recursive-read-only-mounts):
   This is implemented by applying the `MOUNT_ATTR_RDONLY` attribute with the `AT_RECURSIVE` flag
   using `mount_setattr`(2) added in Linux kernel v5.12.
2. Pod user namespace support requires minimal kernel version 6.5+, according to
   [KEP-127](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/127-user-namespaces/README.md).
3. For [node system swap](/docs/concepts/architecture/nodes/#swap-memory), tmpfs set to `noswap`
   is not supported until kernel 6.3.

## Linux kernel long term maintenance

Active kernel releases can be found in [kernel.org](https://www.kernel.org/category/releases.html).

There are usually several *long term maintenance* kernel releases provided for the purposes of backporting
bug fixes for older kernel trees. Only important bug fixes are applied to such kernels and they don't
usually see very frequent releases, especially for older trees.
See the Linux kernel website for the [list of releases](https://www.kernel.org/category/releases.html)
in the *Longterm* category.

## What's next

* See [sysctls](/docs/tasks/administer-cluster/sysctl-cluster/) for more details.
* Allow running kube-proxy with in [nftables mode](/docs/reference/networking/virtual-ips/#proxy-mode-nftables).
* Read more information in [cgroups v2](/docs/concepts/architecture/cgroups/).

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
