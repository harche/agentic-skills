# Using sysctls in a Kubernetes Cluster

FEATURE STATE:
`Kubernetes v1.21 [stable]`

This document describes how to configure and use kernel parameters within a
Kubernetes cluster using the [sysctl](/docs/tasks/administer-cluster/sysctl-cluster/ "An interface for getting and setting Unix kernel parameters")
interface.

> **Note:**
> Starting from Kubernetes version 1.23, the kubelet supports the use of either `/` or `.`
> as separators for sysctl names.
> Starting from Kubernetes version 1.25, setting Sysctls for a Pod supports setting sysctls with slashes.
> For example, you can represent the same sysctl name as `kernel.shm_rmid_forced` using a
> period as the separator, or as `kernel/shm_rmid_forced` using a slash as a separator.
> For more sysctl parameter conversion method details, please refer to
> the page [sysctl.d(5)](https://man7.org/linux/man-pages/man5/sysctl.d.5.html) from
> the Linux man-pages project.

## Before you begin

> **Note:**
> `sysctl` is a Linux-specific command-line tool used to configure various kernel parameters
> and it is not available on non-Linux operating systems.

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [KodeKloud](https://kodekloud.com/public-playgrounds)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)

For some steps, you also need to be able to reconfigure the command line
options for the kubelets running on your cluster.

## Listing all Sysctl Parameters

In Linux, the sysctl interface allows an administrator to modify kernel
parameters at runtime. Parameters are available via the `/proc/sys/` virtual
process file system. The parameters cover various subsystems such as:

* kernel (common prefix: `kernel.`)
* networking (common prefix: `net.`)
* virtual memory (common prefix: `vm.`)
* MDADM (common prefix: `dev.`)
* More subsystems are described in [Kernel docs](https://www.kernel.org/doc/Documentation/sysctl/README).

To get a list of all parameters, you can run

```
sudo sysctl -a
```

## Safe and Unsafe Sysctls

Kubernetes classes sysctls as either *safe* or *unsafe*. In addition to proper
namespacing, a *safe* sysctl must be properly *isolated* between pods on the
same node. This means that setting a *safe* sysctl for one pod

* must not have any influence on any other pod on the node
* must not allow to harm the node's health
* must not allow to gain CPU or memory resources outside of the resource limits
  of a pod.

By far, most of the *namespaced* sysctls are not necessarily considered *safe*.
The following sysctls are supported in the *safe* set:

* `kernel.shm_rmid_forced`;
* `net.ipv4.ip_local_port_range`;
* `net.ipv4.tcp_syncookies`;
* `net.ipv4.ping_group_range` (since Kubernetes 1.18);
* `net.ipv4.ip_unprivileged_port_start` (since Kubernetes 1.22);
* `net.ipv4.ip_local_reserved_ports` (since Kubernetes 1.27, needs kernel 3.16+);
* `net.ipv4.tcp_keepalive_time` (since Kubernetes 1.29, needs kernel 4.5+);
* `net.ipv4.tcp_fin_timeout` (since Kubernetes 1.29, needs kernel 4.6+);
* `net.ipv4.tcp_keepalive_intvl` (since Kubernetes 1.29, needs kernel 4.5+);
* `net.ipv4.tcp_keepalive_probes` (since Kubernetes 1.29, needs kernel 4.5+).
* `net.ipv4.tcp_rmem` (since Kubernetes 1.32, needs kernel 4.15+).
* `net.ipv4.tcp_wmem` (since Kubernetes 1.32, needs kernel 4.15+).

> **Note:**
> There are some exceptions to the set of safe sysctls:
>
> * The `net.*` sysctls are not allowed with host networking enabled.
> * The `net.ipv4.tcp_syncookies` sysctl is not namespaced on Linux kernel version 4.5 or lower.

This list will be extended in future Kubernetes versions when the kubelet
supports better isolation mechanisms.

### Enabling Unsafe Sysctls

All *safe* sysctls are enabled by default.

All *unsafe* sysctls are disabled by default and must be allowed manually by the
cluster admin on a per-node basis. Pods with disabled unsafe sysctls will be
scheduled, but will fail to launch.

With the warning above in mind, the cluster admin can allow certain *unsafe*
sysctls for very special situations such as high-performance or real-time
application tuning. *Unsafe* sysctls are enabled on a node-by-node basis with a
flag of the kubelet; for example:

```
kubelet --allowed-unsafe-sysctls \
  'kernel.msg*,net.core.somaxconn' ...
```

For [Minikube](/docs/tasks/tools/#minikube "A tool for running Kubernetes locally."), this can be done via the `extra-config` flag:

```
minikube start --extra-config="kubelet.allowed-unsafe-sysctls=kernel.msg*,net.core.somaxconn"...
```

Only *namespaced* sysctls can be enabled this way.

## Setting Sysctls for a Pod

A number of sysctls are *namespaced* in today's Linux kernels. This means that
they can be set independently for each pod on a node. Only namespaced sysctls
are configurable via the pod securityContext within Kubernetes.

The following sysctls are known to be namespaced. This list could change
in future versions of the Linux kernel.

* `kernel.shm*`,
* `kernel.msg*`,
* `kernel.sem`,
* `fs.mqueue.*`,
* Those `net.*` that can be set in container networking namespace. However,
  there are exceptions (e.g., `net.netfilter.nf_conntrack_max` and
  `net.netfilter.nf_conntrack_expect_max` can be set in container networking
  namespace but are unnamespaced before Linux 5.12.2).

Sysctls with no namespace are called *node-level* sysctls. If you need to set
them, you must manually configure them on each node's operating system, or by
using a DaemonSet with privileged containers.

Use the pod securityContext to configure namespaced sysctls. The securityContext
applies to all containers in the same pod.

This example uses the pod securityContext to set a safe sysctl
`kernel.shm_rmid_forced` and two unsafe sysctls `net.core.somaxconn` and
`kernel.msgmax`. There is no distinction between *safe* and *unsafe* sysctls in
the specification.

> **Warning:**
> Only modify sysctl parameters after you understand their effects, to avoid
> destabilizing your operating system.

```
apiVersion: v1
kind: Pod
metadata:
  name: sysctl-example
spec:
  securityContext:
    sysctls:
    - name: kernel.shm_rmid_forced
      value: "0"
    - name: net.core.somaxconn
      value: "1024"
    - name: kernel.msgmax
      value: "65536"
  ...
```

> **Warning:**
> Due to their nature of being *unsafe*, the use of *unsafe* sysctls
> is at-your-own-risk and can lead to severe problems like wrong behavior of
> containers, resource shortage or complete breakage of a node.

It is good practice to consider nodes with special sysctl settings as
*tainted* within a cluster, and only schedule pods onto them which need those
sysctl settings. It is suggested to use the Kubernetes [*taints and toleration*
feature](/docs/reference/generated/kubectl/kubectl-commands/#taint) to implement this.

A pod with the *unsafe* sysctls will fail to launch on any node which has not
enabled those two *unsafe* sysctls explicitly. As with *node-level* sysctls it
is recommended to use
[*taints and toleration* feature](/docs/reference/generated/kubectl/kubectl-commands/#taint) or
[taints on nodes](/docs/concepts/scheduling-eviction/taint-and-toleration/)
to schedule those pods onto the right nodes.

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
