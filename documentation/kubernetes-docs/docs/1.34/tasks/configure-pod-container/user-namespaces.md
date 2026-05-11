# Use a User Namespace With a Pod

FEATURE STATE:
`Kubernetes v1.33 [beta]`(enabled by default)

This page shows how to configure a user namespace for pods. This allows you to
isolate the user running inside the container from the one in the host.

A process running as root in a container can run as a different (non-root) user
in the host; in other words, the process has full privileges for operations
inside the user namespace, but is unprivileged for operations outside the
namespace.

You can use this feature to reduce the damage a compromised container can do to
the host or other pods in the same node. There are [several security
vulnerabilities](https://github.com/kubernetes/enhancements/tree/217d790720c5aef09b8bd4d6ca96284a0affe6c2/keps/sig-node/127-user-namespaces#motivation) rated either **HIGH** or **CRITICAL** that were not
exploitable when user namespaces is active. It is expected user namespace will
mitigate some future vulnerabilities too.

Without using a user namespace a container running as root, in the case of a
container breakout, has root privileges on the node. And if some capability were
granted to the container, the capabilities are valid on the host too. None of
this is true when user namespaces are used.

## Before you begin

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [KodeKloud](https://kodekloud.com/public-playgrounds)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)

Your Kubernetes server must be at or later than version v1.25.

To check the version, enter `kubectl version`.

> **Note:**
> 🛇 This item links to a third party project or product that is not part of Kubernetes itself. [More information](#third-party-content-disclaimer)

* The node OS needs to be Linux
* You need to exec commands in the host
* You need to be able to exec into pods
* You need to enable the `UserNamespacesSupport`
  [feature gate](/docs/reference/command-line-tools-reference/feature-gates/)

> **Note:**
> The feature gate to enable user namespaces was previously named
> `UserNamespacesStatelessPodsSupport`, when only stateless pods were supported.
> Only Kubernetes v1.25 through to v1.27 recognise `UserNamespacesStatelessPodsSupport`.

The cluster that you're using **must** include at least one node that meets the
[requirements](/docs/concepts/workloads/pods/user-namespaces/#before-you-begin)
for using user namespaces with Pods.

If you have a mixture of nodes and only some of the nodes provide user namespace support for
Pods, you also need to ensure that the user namespace Pods are
[scheduled](/docs/concepts/scheduling-eviction/assign-pod-node/) to suitable nodes.

## Run a Pod that uses a user namespace

A user namespace for a pod is enabled setting the `hostUsers` field of `.spec`
to `false`. For example:

[`pods/user-namespaces-stateless.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/user-namespaces-stateless.yaml)![](/images/copycode.svg "Copy pods/user-namespaces-stateless.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: userns
spec:
  hostUsers: false
  containers:
  - name: shell
    command: ["sleep", "infinity"]
    image: debian
```

1. Create the pod on your cluster:

   ```
   kubectl apply -f https://k8s.io/examples/pods/user-namespaces-stateless.yaml
   ```
2. Exec into the pod and run `readlink /proc/self/ns/user`:

   ```
   kubectl exec -ti userns -- bash
   ```

Run this command:

```
readlink /proc/self/ns/user
```

The output is similar to:

```
user:[4026531837]
```

Also run:

```
cat /proc/self/uid_map
```

The output is similar to:

```
0  833617920      65536
```

Then, open a shell in the host and run the same commands.

The `readlink` command shows the user namespace the process is running in. It
should be different when it is run on the host and inside the container.

The last number of the `uid_map` file inside the container must be 65536, on the
host it must be a bigger number.

If you are running the kubelet inside a user namespace, you need to compare the
output from running the command in the pod to the output of running in the host:

```
readlink /proc/$pid/ns/user
```

replacing `$pid` with the kubelet PID.

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
