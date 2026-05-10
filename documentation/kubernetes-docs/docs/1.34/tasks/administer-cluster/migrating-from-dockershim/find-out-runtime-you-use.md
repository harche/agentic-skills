# Find Out What Container Runtime is Used on a Node

This page outlines steps to find out what [container runtime](/docs/setup/production-environment/container-runtimes/)
the nodes in your cluster use.

Depending on the way you run your cluster, the container runtime for the nodes may
have been pre-configured or you need to configure it. If you're using a managed
Kubernetes service, there might be vendor-specific ways to check what container runtime is
configured for the nodes. The method described on this page should work whenever
the execution of `kubectl` is allowed.

## Before you begin

Install and configure `kubectl`. See [Install Tools](/docs/tasks/tools/#kubectl) section for details.

## Find out the container runtime used on a Node

Use `kubectl` to fetch and show node information:

```
kubectl get nodes -o wide
```

The output is similar to the following. The column `CONTAINER-RUNTIME` outputs
the runtime and its version.

For Docker Engine, the output is similar to this:

```
NAME         STATUS   VERSION    CONTAINER-RUNTIME
node-1       Ready    v1.16.15   docker://19.3.1
node-2       Ready    v1.16.15   docker://19.3.1
node-3       Ready    v1.16.15   docker://19.3.1
```

If your runtime shows as Docker Engine, you still might not be affected by the
removal of dockershim in Kubernetes v1.24.
[Check the runtime endpoint](#which-endpoint) to see if you use dockershim.
If you don't use dockershim, you aren't affected.

For containerd, the output is similar to this:

```
NAME         STATUS   VERSION   CONTAINER-RUNTIME
node-1       Ready    v1.19.6   containerd://1.4.1
node-2       Ready    v1.19.6   containerd://1.4.1
node-3       Ready    v1.19.6   containerd://1.4.1
```

Find out more information about container runtimes
on [Container Runtimes](/docs/setup/production-environment/container-runtimes/)
page.

## Find out what container runtime endpoint you use

The container runtime talks to the kubelet over a Unix socket using the [CRI
protocol](/docs/concepts/architecture/cri/), which is based on the gRPC
framework. The kubelet acts as a client, and the runtime acts as the server.
In some cases, you might find it useful to know which socket your nodes use. For
example, with the removal of dockershim in Kubernetes v1.24 and later, you might
want to know whether you use Docker Engine with dockershim.

> **Note:**
> If you currently use Docker Engine in your nodes with `cri-dockerd`, you aren't
> affected by the dockershim removal.

You can check which socket you use by checking the kubelet configuration on your
nodes.

1. Read the starting commands for the kubelet process:

   ```
   tr \\0 ' ' < /proc/"$(pgrep kubelet)"/cmdline
   ```

   If you don't have `tr` or `pgrep`, check the command line for the kubelet
   process manually.
2. In the output, look for the `--container-runtime` flag and the
   `--container-runtime-endpoint` flag.

   * If your nodes use Kubernetes v1.23 and earlier and these flags aren't
     present or if the `--container-runtime` flag is not `remote`,
     you use the dockershim socket with Docker Engine. The `--container-runtime` command line
     argument is not available in Kubernetes v1.27 and later.
   * If the `--container-runtime-endpoint` flag is present, check the socket
     name to find out which runtime you use. For example,
     `unix:///run/containerd/containerd.sock` is the containerd endpoint.

If you want to change the Container Runtime on a Node from Docker Engine to containerd,
you can find out more information on [migrating from Docker Engine to containerd](/docs/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd/),
or, if you want to continue using Docker Engine in Kubernetes v1.24 and later, migrate to a
CRI-compatible adapter like [`cri-dockerd`](https://github.com/Mirantis/cri-dockerd).

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
