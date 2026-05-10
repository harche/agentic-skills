# Kubernetes Metrics (v1beta1)

Package v1beta1 is the v1beta1 version of the metrics API.

## Resource Types

* [NodeMetrics](#metrics-k8s-io-v1beta1-NodeMetrics)
* [NodeMetricsList](#metrics-k8s-io-v1beta1-NodeMetricsList)
* [PodMetrics](#metrics-k8s-io-v1beta1-PodMetrics)
* [PodMetricsList](#metrics-k8s-io-v1beta1-PodMetricsList)

## `NodeMetrics`

**Appears in:**

* [NodeMetricsList](#metrics-k8s-io-v1beta1-NodeMetricsList)

NodeMetrics sets resource usage metrics of a node.

| Field | Description |
| --- | --- |
| `apiVersion` string | `metrics.k8s.io/v1beta1` |
| `kind` string | `NodeMetrics` |
| `metadata`  [`meta/v1.ObjectMeta`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#objectmeta-v1-meta) | Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `timestamp` **[Required]**  [`meta/v1.Time`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#time-v1-meta) | The following fields define time interval from which metrics were collected from the interval [Timestamp-Window, Timestamp]. |
| `window` **[Required]**  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | No description provided. |
| `usage` **[Required]**  [`core/v1.ResourceList`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#resourcelist-v1-core) | The memory usage is the memory working set. |

## `NodeMetricsList`

NodeMetricsList is a list of NodeMetrics.

| Field | Description |
| --- | --- |
| `apiVersion` string | `metrics.k8s.io/v1beta1` |
| `kind` string | `NodeMetricsList` |
| `metadata` **[Required]**  [`meta/v1.ListMeta`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#listmeta-v1-meta) | Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `items` **[Required]**  [`[]NodeMetrics`](#metrics-k8s-io-v1beta1-NodeMetrics) | List of node metrics. |

## `PodMetrics`

**Appears in:**

* [PodMetricsList](#metrics-k8s-io-v1beta1-PodMetricsList)

PodMetrics sets resource usage metrics of a pod.

| Field | Description |
| --- | --- |
| `apiVersion` string | `metrics.k8s.io/v1beta1` |
| `kind` string | `PodMetrics` |
| `metadata`  [`meta/v1.ObjectMeta`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#objectmeta-v1-meta) | Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `timestamp` **[Required]**  [`meta/v1.Time`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#time-v1-meta) | The following fields define time interval from which metrics were collected from the interval [Timestamp-Window, Timestamp]. |
| `window` **[Required]**  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | No description provided. |
| `containers` **[Required]**  [`[]ContainerMetrics`](#metrics-k8s-io-v1beta1-ContainerMetrics) | Metrics for all containers are collected within the same time window. |

## `PodMetricsList`

PodMetricsList is a list of PodMetrics.

| Field | Description |
| --- | --- |
| `apiVersion` string | `metrics.k8s.io/v1beta1` |
| `kind` string | `PodMetricsList` |
| `metadata` **[Required]**  [`meta/v1.ListMeta`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#listmeta-v1-meta) | Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `items` **[Required]**  [`[]PodMetrics`](#metrics-k8s-io-v1beta1-PodMetrics) | List of pod metrics. |

## `ContainerMetrics`

**Appears in:**

* [PodMetrics](#metrics-k8s-io-v1beta1-PodMetrics)

ContainerMetrics sets resource usage metrics of a container.

| Field | Description |
| --- | --- |
| `name` **[Required]**  `string` | Container name corresponding to the one from pod.spec.containers. |
| `usage` **[Required]**  [`core/v1.ResourceList`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#resourcelist-v1-core) | The memory usage is the memory working set. |

This page is automatically generated.

If you plan to report an issue with this page, mention that the page is auto-generated in your issue description. The fix may need to happen elsewhere in the Kubernetes project.

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
