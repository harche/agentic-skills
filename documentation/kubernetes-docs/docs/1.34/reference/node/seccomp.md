# Seccomp and Kubernetes

Seccomp stands for secure computing mode and has been a feature of the Linux
kernel since version 2.6.12. It can be used to sandbox the privileges of a
process, restricting the calls it is able to make from userspace into the
kernel. Kubernetes lets you automatically apply seccomp profiles loaded onto a
[node](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") to your Pods and containers.

## Seccomp fields

FEATURE STATE:
`Kubernetes v1.19 [stable]`

There are four ways to specify a seccomp profile for a
[pod](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster."):

* for the whole Pod using [`spec.securityContext.seccompProfile`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context)
* for a single container using [`spec.containers[*].securityContext.seccompProfile`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context-1)
* for an (restartable / sidecar) init container using [`spec.initContainers[*].securityContext.seccompProfile`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context-1)
* for an [ephemeral container](/docs/concepts/workloads/pods/ephemeral-containers/) using [`spec.ephemeralContainers[*].securityContext.seccompProfile`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context-2)

[`pods/security/seccomp/fields.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/security/seccomp/fields.yaml)![](/images/copycode.svg "Copy pods/security/seccomp/fields.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: pod
spec:
  securityContext:
    seccompProfile:
      type: Unconfined
  ephemeralContainers:
  - name: ephemeral-container
    image: debian
    securityContext:
      seccompProfile:
        type: RuntimeDefault
  initContainers:
  - name: init-container
    image: debian
    securityContext:
      seccompProfile:
        type: RuntimeDefault
  containers:
  - name: container
    image: docker.io/library/debian:stable
    securityContext:
      seccompProfile:
        type: Localhost
        localhostProfile: my-profile.json
```

The Pod in the example above runs as `Unconfined`, while the
`ephemeral-container` and `init-container` specifically defines
`RuntimeDefault`. If the ephemeral or init container would not have set the
`securityContext.seccompProfile` field explicitly, then the value would be
inherited from the Pod. The same applies to the container, which runs a
`Localhost` profile `my-profile.json`.

Generally speaking, fields from (ephemeral) containers have a higher priority
than the Pod level value, while containers which do not set the seccomp field
inherit the profile from the Pod.

> **Note:**
> It is not possible to apply a seccomp profile to a Pod or container running with
> `privileged: true` set in the container's `securityContext`. Privileged
> containers always run as `Unconfined`.

The following values are possible for the `seccompProfile.type`:

`Unconfined`
:   The workload runs without any seccomp restrictions.

`RuntimeDefault`
:   A default seccomp profile defined by the
    [container runtime](/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.")
    is applied. The default profiles aim to provide a strong set of security
    defaults while preserving the functionality of the workload. It is possible that
    the default profiles differ between container runtimes and their release
    versions, for example when comparing those from
    [CRI-O](https://cri-o.io/#what-is-cri-o "A lightweight container runtime specifically for Kubernetes") and
    [containerd](https://containerd.io/docs/ "A container runtime with an emphasis on simplicity, robustness and portability").

`Localhost`
:   The `localhostProfile` will be applied, which has to be available on the node
    disk (on Linux it's `/var/lib/kubelet/seccomp`). The availability of the seccomp
    profile is verified by the
    [container runtime](/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.")
    on container creation. If the profile does not exist, then the container
    creation will fail with a `CreateContainerError`.

### `Localhost` profiles

Seccomp profiles are JSON files following the scheme defined by the
[OCI runtime specification](https://github.com/opencontainers/runtime-spec/blob/f329913/config-linux.md#seccomp).
A profile basically defines actions based on matched syscalls, but also allows
to pass specific values as arguments to syscalls. For example:

```
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "defaultErrnoRet": 38,
  "syscalls": [
    {
      "names": [
        "adjtimex",
        "alarm",
        "bind",
        "waitid",
        "waitpid",
        "write",
        "writev"
      ],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

The `defaultAction` in the profile above is defined as `SCMP_ACT_ERRNO` and
will return as fallback to the actions defined in `syscalls`. The error is
defined as code `38` via the `defaultErrnoRet` field.

The following actions are generally possible:

`SCMP_ACT_ERRNO`
:   Return the specified error code.

`SCMP_ACT_ALLOW`
:   Allow the syscall to be executed.

`SCMP_ACT_KILL_PROCESS`
:   Kill the process.

`SCMP_ACT_KILL_THREAD` and `SCMP_ACT_KILL`
:   Kill only the thread.

`SCMP_ACT_TRAP`
:   Throw a `SIGSYS` signal.

`SCMP_ACT_NOTIFY` and `SECCOMP_RET_USER_NOTIF`.
:   Notify the user space.

`SCMP_ACT_TRACE`
:   Notify a tracing process with the specified value.

`SCMP_ACT_LOG`
:   Allow the syscall to be executed after the action has been logged to syslog or
    auditd.

Some actions like `SCMP_ACT_NOTIFY` or `SECCOMP_RET_USER_NOTIF` may be not
supported depending on the container runtime, OCI runtime or Linux kernel
version being used. There may be also further limitations, for example that
`SCMP_ACT_NOTIFY` cannot be used as `defaultAction` or for certain syscalls like
`write`. All those limitations are defined by either the OCI runtime
([runc](https://github.com/opencontainers/runc),
[crun](https://github.com/containers/crun)) or
[libseccomp](https://github.com/seccomp/libseccomp).

The `syscalls` JSON array contains a list of objects referencing syscalls by
their respective `names`. For example, the action `SCMP_ACT_ALLOW` can be used
to create a whitelist of allowed syscalls as outlined in the example above. It
would also be possible to define another list using the action `SCMP_ACT_ERRNO`
but a different return (`errnoRet`) value.

It is also possible to specify the arguments (`args`) passed to certain
syscalls. More information about those advanced use cases can be found in the
[OCI runtime spec](https://github.com/opencontainers/runtime-spec/blob/f329913/config-linux.md#seccomp)
and the [Seccomp Linux kernel documentation](https://www.kernel.org/doc/Documentation/prctl/seccomp_filter.txt).

## Further reading

* [Restrict a Container's Syscalls with seccomp](/docs/tutorials/security/seccomp/)
* [Pod Security Standards](/docs/concepts/security/pod-security-standards/)

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
