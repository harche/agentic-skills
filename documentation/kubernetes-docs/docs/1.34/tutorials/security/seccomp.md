# Restrict a Container's Syscalls with seccomp

FEATURE STATE:
`Kubernetes v1.19 [stable]`

Seccomp stands for secure computing mode and has been a feature of the Linux
kernel since version 2.6.12. It can be used to sandbox the privileges of a
process, restricting the calls it is able to make from userspace into the
kernel. Kubernetes lets you automatically apply seccomp profiles loaded onto a
[node](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") to your Pods and containers.

Identifying the privileges required for your workloads can be difficult. In this
tutorial, you will go through how to load seccomp profiles into a local
Kubernetes cluster, how to apply them to a Pod, and how you can begin to craft
profiles that give only the necessary privileges to your container processes.

## Objectives

* Learn how to load seccomp profiles on a node
* Learn how to apply a seccomp profile to a container
* Observe auditing of syscalls made by a container process
* Observe behavior when a missing profile is specified
* Observe a violation of a seccomp profile
* Learn how to create fine-grained seccomp profiles
* Learn how to apply a container runtime default seccomp profile

## Before you begin

In order to complete all steps in this tutorial, you must install
[kind](/docs/tasks/tools/#kind) and [kubectl](/docs/tasks/tools/#kubectl).

The commands used in the tutorial assume that you are using
[Docker](https://www.docker.com/) as your container runtime. (The cluster that `kind` creates may
use a different container runtime internally). You could also use
[Podman](https://podman.io/) but in that case, you would have to follow specific
[instructions](https://kind.sigs.k8s.io/docs/user/rootless/) in order to complete the tasks
successfully.

This tutorial shows some examples that are still beta (since v1.25) and
others that use only generally available seccomp functionality. You should
make sure that your cluster is
[configured correctly](https://kind.sigs.k8s.io/docs/user/quick-start/#setting-kubernetes-version)
for the version you are using.

The tutorial also uses the `curl` tool for downloading examples to your computer.
You can adapt the steps to use a different tool if you prefer.

> **Note:**
> It is not possible to apply a seccomp profile to a container running with
> `privileged: true` set in the container's `securityContext`. Privileged containers always
> run as `Unconfined`.

## Download example seccomp profiles

The contents of these profiles will be explored later on, but for now go ahead
and download them into a directory named `profiles/` so that they can be loaded
into the cluster.

* audit.json
  * violation.json
    * fine-grained.json

[`pods/security/seccomp/profiles/audit.json`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/security/seccomp/profiles/audit.json)![](/images/copycode.svg "Copy pods/security/seccomp/profiles/audit.json to clipboard")

```
{
    "defaultAction": "SCMP_ACT_LOG"
}
```

[`pods/security/seccomp/profiles/violation.json`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/security/seccomp/profiles/violation.json)![](/images/copycode.svg "Copy pods/security/seccomp/profiles/violation.json to clipboard")

```
{
    "defaultAction": "SCMP_ACT_ERRNO"
}
```

[`pods/security/seccomp/profiles/fine-grained.json`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/security/seccomp/profiles/fine-grained.json)![](/images/copycode.svg "Copy pods/security/seccomp/profiles/fine-grained.json to clipboard")

```
{
    "defaultAction": "SCMP_ACT_ERRNO",
    "architectures": [
        "SCMP_ARCH_X86_64",
        "SCMP_ARCH_X86",
        "SCMP_ARCH_X32"
    ],
    "syscalls": [
        {
            "names": [
                "accept4",
                "epoll_wait",
                "pselect6",
                "futex",
                "madvise",
                "epoll_ctl",
                "getsockname",
                "setsockopt",
                "vfork",
                "mmap",
                "read",
                "write",
                "close",
                "arch_prctl",
                "sched_getaffinity",
                "munmap",
                "brk",
                "rt_sigaction",
                "rt_sigprocmask",
                "sigaltstack",
                "gettid",
                "clone",
                "bind",
                "socket",
                "openat",
                "readlinkat",
                "exit_group",
                "epoll_create1",
                "listen",
                "rt_sigreturn",
                "sched_yield",
                "clock_gettime",
                "connect",
                "dup2",
                "epoll_pwait",
                "execve",
                "exit",
                "fcntl",
                "getpid",
                "getuid",
                "ioctl",
                "mprotect",
                "nanosleep",
                "open",
                "poll",
                "recvfrom",
                "sendto",
                "set_tid_address",
                "setitimer",
                "writev",
                "fstatfs",
                "getdents64",
                "pipe2",
                "getrlimit"
            ],
            "action": "SCMP_ACT_ALLOW"
        }
    ]
}
```

Run these commands:

```
mkdir ./profiles
curl -L -o profiles/audit.json https://k8s.io/examples/pods/security/seccomp/profiles/audit.json
curl -L -o profiles/violation.json https://k8s.io/examples/pods/security/seccomp/profiles/violation.json
curl -L -o profiles/fine-grained.json https://k8s.io/examples/pods/security/seccomp/profiles/fine-grained.json
ls profiles
```

You should see three profiles listed at the end of the final step:

```
audit.json  fine-grained.json  violation.json
```

## Create a local Kubernetes cluster with kind

For simplicity, [kind](https://kind.sigs.k8s.io/) can be used to create a single
node cluster with the seccomp profiles loaded. Kind runs Kubernetes in Docker,
so each node of the cluster is a container. This allows for files
to be mounted in the filesystem of each container similar to loading files
onto a node.

[`pods/security/seccomp/kind.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/security/seccomp/kind.yaml)![](/images/copycode.svg "Copy pods/security/seccomp/kind.yaml to clipboard")

```
apiVersion: kind.x-k8s.io/v1alpha4
kind: Cluster
nodes:
- role: control-plane
  extraMounts:
  - hostPath: "./profiles"
    containerPath: "/var/lib/kubelet/seccomp/profiles"
```

Download that example kind configuration, and save it to a file named `kind.yaml`:

```
curl -L -O https://k8s.io/examples/pods/security/seccomp/kind.yaml
```

You can set a specific Kubernetes version by setting the node's container image.
See [Nodes](https://kind.sigs.k8s.io/docs/user/configuration/#nodes) within the
kind documentation about configuration for more details on this.
This tutorial assumes you are using Kubernetes v1.34.

As a beta feature, you can configure Kubernetes to use the profile that the
[container runtime](/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.")
prefers by default, rather than falling back to `Unconfined`.
If you want to try that, see
[enable the use of `RuntimeDefault` as the default seccomp profile for all workloads](#enable-the-use-of-runtimedefault-as-the-default-seccomp-profile-for-all-workloads)
before you continue.

Once you have a kind configuration in place, create the kind cluster with
that configuration:

```
kind create cluster --config=kind.yaml
```

After the new Kubernetes cluster is ready, identify the Docker container running
as the single node cluster:

```
docker ps
```

You should see output indicating that a container is running with name
`kind-control-plane`. The output is similar to:

```
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                       NAMES
6a96207fed4b        kindest/node:v1.18.2   "/usr/local/bin/entr…"   27 seconds ago      Up 24 seconds       127.0.0.1:42223->6443/tcp   kind-control-plane
```

If observing the filesystem of that container, you should see that the
`profiles/` directory has been successfully loaded into the default seccomp path
of the kubelet. Use `docker exec` to run a command in the Pod:

```
# Change 6a96207fed4b to the container ID you saw from "docker ps"
docker exec -it 6a96207fed4b ls /var/lib/kubelet/seccomp/profiles
```

```
audit.json  fine-grained.json  violation.json
```

You have verified that these seccomp profiles are available to the kubelet
running within kind.

## Create a Pod that uses the container runtime default seccomp profile

Most container runtimes provide a sane set of default syscalls that are allowed
or not. You can adopt these defaults for your workload by setting the seccomp
type in the security context of a pod or container to `RuntimeDefault`.

> **Note:**
> If you have the `seccompDefault` [configuration](/docs/reference/config-api/kubelet-config.v1beta1/)
> enabled, then Pods use the `RuntimeDefault` seccomp profile whenever
> no other seccomp profile is specified. Otherwise, the default is `Unconfined`.

Here's a manifest for a Pod that requests the `RuntimeDefault` seccomp profile
for all its containers:

[`pods/security/seccomp/ga/default-pod.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/security/seccomp/ga/default-pod.yaml)![](/images/copycode.svg "Copy pods/security/seccomp/ga/default-pod.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: default-pod
  labels:
    app: default-pod
spec:
  securityContext:
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: test-container
    image: hashicorp/http-echo:1.0
    args:
    - "-text=just made some more syscalls!"
    securityContext:
      allowPrivilegeEscalation: false
```

Create that Pod:

```
kubectl apply -f https://k8s.io/examples/pods/security/seccomp/ga/default-pod.yaml
```

```
kubectl get pod default-pod
```

The Pod should be showing as having started successfully:

```
NAME        READY   STATUS    RESTARTS   AGE
default-pod 1/1     Running   0          20s
```

Delete the Pod before moving to the next section:

```
kubectl delete pod default-pod --wait --now
```

## Create a Pod with a seccomp profile for syscall auditing

To start off, apply the `audit.json` profile, which will log all syscalls of the
process, to a new Pod.

Here's a manifest for that Pod:

[`pods/security/seccomp/ga/audit-pod.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/security/seccomp/ga/audit-pod.yaml)![](/images/copycode.svg "Copy pods/security/seccomp/ga/audit-pod.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: audit-pod
  labels:
    app: audit-pod
spec:
  securityContext:
    seccompProfile:
      type: Localhost
      localhostProfile: profiles/audit.json
  containers:
  - name: test-container
    image: hashicorp/http-echo:1.0
    args:
    - "-text=just made some syscalls!"
    securityContext:
      allowPrivilegeEscalation: false
```

> **Note:**
> Older versions of Kubernetes allowed you to configure seccomp
> behavior using [annotations](/docs/concepts/overview/working-with-objects/annotations "A key-value pair that is used to attach arbitrary non-identifying metadata to objects.").
> Kubernetes 1.34 only supports using fields within
> `.spec.securityContext` to configure seccomp, and this tutorial explains that
> approach.

Create the Pod in the cluster:

```
kubectl apply -f https://k8s.io/examples/pods/security/seccomp/ga/audit-pod.yaml
```

This profile does not restrict any syscalls, so the Pod should start
successfully.

```
kubectl get pod audit-pod
```

```
NAME        READY   STATUS    RESTARTS   AGE
audit-pod   1/1     Running   0          30s
```

In order to be able to interact with this endpoint exposed by this
container, create a NodePort [Service](/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.")
that allows access to the endpoint from inside the kind control plane container.

```
kubectl expose pod audit-pod --type NodePort --port 5678
```

Check what port the Service has been assigned on the node.

```
kubectl get service audit-pod
```

The output is similar to:

```
NAME        TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
audit-pod   NodePort   10.111.36.142   <none>        5678:32373/TCP   72s
```

Now you can use `curl` to access that endpoint from inside the kind control plane container,
at the port exposed by this Service. Use `docker exec` to run the `curl` command within the
container belonging to that control plane container:

```
# Change 6a96207fed4b to the control plane container ID and 32373 to the port number you saw from "docker ps"
docker exec -it 6a96207fed4b curl localhost:32373
```

```
just made some syscalls!
```

You can see that the process is running, but what syscalls did it actually make?
Because this Pod is running in a local cluster, you should be able to see those
in `/var/log/syslog` on your local system. Open up a new terminal window and `tail` the output for
calls from `http-echo`:

```
# The log path on your computer might be different from "/var/log/syslog"
tail -f /var/log/syslog | grep 'http-echo'
```

You should already see some logs of syscalls made by `http-echo`, and if you run `curl` again inside
the control plane container you will see more output written to the log.

For example:

```
Jul  6 15:37:40 my-machine kernel: [369128.669452] audit: type=1326 audit(1594067860.484:14536): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=51 compat=0 ip=0x46fe1f code=0x7ffc0000
Jul  6 15:37:40 my-machine kernel: [369128.669453] audit: type=1326 audit(1594067860.484:14537): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=54 compat=0 ip=0x46fdba code=0x7ffc0000
Jul  6 15:37:40 my-machine kernel: [369128.669455] audit: type=1326 audit(1594067860.484:14538): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=202 compat=0 ip=0x455e53 code=0x7ffc0000
Jul  6 15:37:40 my-machine kernel: [369128.669456] audit: type=1326 audit(1594067860.484:14539): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=288 compat=0 ip=0x46fdba code=0x7ffc0000
Jul  6 15:37:40 my-machine kernel: [369128.669517] audit: type=1326 audit(1594067860.484:14540): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=0 compat=0 ip=0x46fd44 code=0x7ffc0000
Jul  6 15:37:40 my-machine kernel: [369128.669519] audit: type=1326 audit(1594067860.484:14541): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=270 compat=0 ip=0x4559b1 code=0x7ffc0000
Jul  6 15:38:40 my-machine kernel: [369188.671648] audit: type=1326 audit(1594067920.488:14559): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=270 compat=0 ip=0x4559b1 code=0x7ffc0000
Jul  6 15:38:40 my-machine kernel: [369188.671726] audit: type=1326 audit(1594067920.488:14560): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=202 compat=0 ip=0x455e53 code=0x7ffc0000
```

You can begin to understand the syscalls required by the `http-echo` process by
looking at the `syscall=` entry on each line. While these are unlikely to
encompass all syscalls it uses, it can serve as a basis for a seccomp profile
for this container.

Delete the Service and the Pod before moving to the next section:

```
kubectl delete service audit-pod --wait
kubectl delete pod audit-pod --wait --now
```

## Create a Pod with a seccomp profile that causes violation

For demonstration, apply a profile to the Pod that does not allow for any
syscalls.

The manifest for this demonstration is:

[`pods/security/seccomp/ga/violation-pod.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/security/seccomp/ga/violation-pod.yaml)![](/images/copycode.svg "Copy pods/security/seccomp/ga/violation-pod.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: violation-pod
  labels:
    app: violation-pod
spec:
  securityContext:
    seccompProfile:
      type: Localhost
      localhostProfile: profiles/violation.json
  containers:
  - name: test-container
    image: hashicorp/http-echo:1.0
    args:
    - "-text=just made some syscalls!"
    securityContext:
      allowPrivilegeEscalation: false
```

Attempt to create the Pod in the cluster:

```
kubectl apply -f https://k8s.io/examples/pods/security/seccomp/ga/violation-pod.yaml
```

The Pod creates, but there is an issue.
If you check the status of the Pod, you should see that it failed to start.

```
kubectl get pod violation-pod
```

```
NAME            READY   STATUS             RESTARTS   AGE
violation-pod   0/1     CrashLoopBackOff   1          6s
```

As seen in the previous example, the `http-echo` process requires quite a few
syscalls. Here seccomp has been instructed to error on any syscall by setting
`"defaultAction": "SCMP_ACT_ERRNO"`. This is extremely secure, but removes the
ability to do anything meaningful. What you really want is to give workloads
only the privileges they need.

Delete the Pod before moving to the next section:

```
kubectl delete pod violation-pod --wait --now
```

## Create a Pod with a seccomp profile that only allows necessary syscalls

If you take a look at the `fine-grained.json` profile, you will notice some of the syscalls
seen in syslog of the first example where the profile set `"defaultAction": "SCMP_ACT_LOG"`. Now the profile is setting `"defaultAction": "SCMP_ACT_ERRNO"`,
but explicitly allowing a set of syscalls in the `"action": "SCMP_ACT_ALLOW"`
block. Ideally, the container will run successfully and you will see no messages
sent to `syslog`.

The manifest for this example is:

[`pods/security/seccomp/ga/fine-pod.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/security/seccomp/ga/fine-pod.yaml)![](/images/copycode.svg "Copy pods/security/seccomp/ga/fine-pod.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: fine-pod
  labels:
    app: fine-pod
spec:
  securityContext:
    seccompProfile:
      type: Localhost
      localhostProfile: profiles/fine-grained.json
  containers:
  - name: test-container
    image: hashicorp/http-echo:1.0
    args:
    - "-text=just made some syscalls!"
    securityContext:
      allowPrivilegeEscalation: false
```

Create the Pod in your cluster:

```
kubectl apply -f https://k8s.io/examples/pods/security/seccomp/ga/fine-pod.yaml
```

```
kubectl get pod fine-pod
```

The Pod should be showing as having started successfully:

```
NAME        READY   STATUS    RESTARTS   AGE
fine-pod   1/1     Running   0          30s
```

Open up a new terminal window and use `tail` to monitor for log entries that
mention calls from `http-echo`:

```
# The log path on your computer might be different from "/var/log/syslog"
tail -f /var/log/syslog | grep 'http-echo'
```

Next, expose the Pod with a NodePort Service:

```
kubectl expose pod fine-pod --type NodePort --port 5678
```

Check what port the Service has been assigned on the node:

```
kubectl get service fine-pod
```

The output is similar to:

```
NAME        TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
fine-pod    NodePort   10.111.36.142   <none>        5678:32373/TCP   72s
```

Use `curl` to access that endpoint from inside the kind control plane container:

```
# Change 6a96207fed4b to the control plane container ID and 32373 to the port number you saw from "docker ps"
docker exec -it 6a96207fed4b curl localhost:32373
```

```
just made some syscalls!
```

You should see no output in the `syslog`. This is because the profile allowed all
necessary syscalls and specified that an error should occur if one outside of
the list is invoked. This is an ideal situation from a security perspective, but
required some effort in analyzing the program. It would be nice if there was a
simple way to get closer to this security without requiring as much effort.

Delete the Service and the Pod before moving to the next section:

```
kubectl delete service fine-pod --wait
kubectl delete pod fine-pod --wait --now
```

## Enable the use of `RuntimeDefault` as the default seccomp profile for all workloads

FEATURE STATE:
`Kubernetes v1.27 [stable]`

To use seccomp profile defaulting, you must run the kubelet with the
`--seccomp-default`
[command line flag](/docs/reference/command-line-tools-reference/kubelet/)
enabled for each node where you want to use it.

If enabled, the kubelet will use the `RuntimeDefault` seccomp profile by default, which is
defined by the container runtime, instead of using the `Unconfined` (seccomp disabled) mode.
The default profiles aim to provide a strong set
of security defaults while preserving the functionality of the workload. It is
possible that the default profiles differ between container runtimes and their
release versions, for example when comparing those from CRI-O and containerd.

> **Note:**
> Enabling the feature will neither change the Kubernetes
> `securityContext.seccompProfile` API field nor add the deprecated annotations of
> the workload. This provides users the possibility to rollback anytime without
> actually changing the workload configuration. Tools like
> [`crictl inspect`](https://github.com/kubernetes-sigs/cri-tools) can be used to
> verify which seccomp profile is being used by a container.

Some workloads may require a lower amount of syscall restrictions than others.
This means that they can fail during runtime even with the `RuntimeDefault`
profile. To mitigate such a failure, you can:

* Run the workload explicitly as `Unconfined`.
* Disable the `SeccompDefault` feature for the nodes. Also making sure that
  workloads get scheduled on nodes where the feature is disabled.
* Create a custom seccomp profile for the workload.

If you were introducing this feature into production-like cluster, the Kubernetes project
recommends that you enable this feature gate on a subset of your nodes and then
test workload execution before rolling the change out cluster-wide.

You can find more detailed information about a possible upgrade and downgrade strategy
in the related Kubernetes Enhancement Proposal (KEP):
[Enable seccomp by default](https://github.com/kubernetes/enhancements/tree/9a124fd29d1f9ddf2ff455c49a630e3181992c25/keps/sig-node/2413-seccomp-by-default#upgrade--downgrade-strategy).

Kubernetes 1.34 lets you configure the seccomp profile
that applies when the spec for a Pod doesn't define a specific seccomp profile.
However, you still need to enable this defaulting for each node where you would
like to use it.

If you are running a Kubernetes 1.34 cluster and want to
enable the feature, either run the kubelet with the `--seccomp-default` command
line flag, or enable it through the [kubelet configuration
file](/docs/tasks/administer-cluster/kubelet-config-file/). To enable the
feature gate in [kind](https://kind.sigs.k8s.io), ensure that `kind` provides
the minimum required Kubernetes version and enables the `SeccompDefault` feature
[in the kind configuration](https://kind.sigs.k8s.io/docs/user/quick-start/#enable-feature-gates-in-your-cluster):

```
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    image: kindest/node:v1.28.0@sha256:9f3ff58f19dcf1a0611d11e8ac989fdb30a28f40f236f59f0bea31fb956ccf5c
    kubeadmConfigPatches:
      - |
        kind: JoinConfiguration
        nodeRegistration:
          kubeletExtraArgs:
            seccomp-default: "true"
  - role: worker
    image: kindest/node:v1.28.0@sha256:9f3ff58f19dcf1a0611d11e8ac989fdb30a28f40f236f59f0bea31fb956ccf5c
    kubeadmConfigPatches:
      - |
        kind: JoinConfiguration
        nodeRegistration:
          kubeletExtraArgs:
            seccomp-default: "true"
```

If the cluster is ready, then running a pod:

```
kubectl run --rm -it --restart=Never --image=alpine alpine -- sh
```

Should now have the default seccomp profile attached. This can be verified by
using `docker exec` to run `crictl inspect` for the container on the kind
worker:

```
docker exec -it kind-worker bash -c \
    'crictl inspect $(crictl ps --name=alpine -q) | jq .info.runtimeSpec.linux.seccomp'
```

```
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": ["SCMP_ARCH_X86_64", "SCMP_ARCH_X86", "SCMP_ARCH_X32"],
  "syscalls": [
    {
      "names": ["..."]
    }
  ]
}
```

## What's next

You can learn more about Linux seccomp:

* [A seccomp Overview](https://lwn.net/Articles/656307/)
* [Seccomp Security Profiles for Docker](https://docs.docker.com/engine/security/seccomp/)

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
