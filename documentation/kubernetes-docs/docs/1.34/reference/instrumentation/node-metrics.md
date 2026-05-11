# Node metrics data

Mechanisms for accessing metrics at node, volume, pod and container level, as seen by the kubelet.

The [kubelet](/docs/reference/command-line-tools-reference/kubelet/)
gathers metric statistics at the node, volume, pod and container level,
and emits this information in the
[Summary API](/docs/reference/config-api/kubelet-stats.v1alpha1/).

You can send a proxied request to the stats summary API via the
Kubernetes API server.

Here is an example of a Summary API request for a node named `minikube`:

```
kubectl get --raw "/api/v1/nodes/minikube/proxy/stats/summary"
```

Here is the same API call using `curl`:

```
# You need to run "kubectl proxy" first
# Change 8080 to the port that "kubectl proxy" assigns
curl http://localhost:8080/api/v1/nodes/minikube/proxy/stats/summary
```

> **Note:**
> Beginning with `metrics-server` 0.6.x, `metrics-server` queries the `/metrics/resource`
> kubelet endpoint, and not `/stats/summary`.

## Summary metrics API source

By default, Kubernetes fetches node summary metrics data using an embedded
[cAdvisor](https://github.com/google/cadvisor) that runs within the kubelet. If you
enable the `PodAndContainerStatsFromCRI` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/)
in your cluster, and you use a container runtime that supports statistics access via
[Container Runtime Interface](/docs/concepts/architecture/cri "Protocol for communication between the kubelet and the local container runtime.") (CRI), then
the kubelet [fetches Pod- and container-level metric data using CRI](/docs/reference/instrumentation/cri-pod-container-metrics/), and not via cAdvisor.

## Pressure Stall Information (PSI)

FEATURE STATE:
`Kubernetes v1.34 [beta]`

As a beta feature, Kubernetes lets you configure kubelet to collect Linux kernel
[Pressure Stall Information](https://docs.kernel.org/accounting/psi.html)
(PSI) for CPU, memory, and I/O usage. The information is collected at node, pod and container level.
See [Summary API](/docs/reference/config-api/kubelet-stats.v1alpha1/) for detailed schema.
This feature is enabled by default, by setting the `KubeletPSI` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/). The information is also exposed in
[Prometheus metrics](/docs/concepts/cluster-administration/system-metrics/#psi-metrics).

You can learn how to interpret the PSI metrics in [Understand PSI Metrics](/docs/reference/instrumentation/understand-psi-metrics/).

### Requirements

Pressure Stall Information requires:

* [Linux kernel versions 4.20 or later](/docs/reference/node/kernel-version-requirements/#requirements-psi).
* [cgroup v2](/docs/concepts/architecture/cgroups/)

## What's next

The task pages for [Troubleshooting Clusters](/docs/tasks/debug/debug-cluster/) discuss
how to use a metrics pipeline that rely on these data.

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
