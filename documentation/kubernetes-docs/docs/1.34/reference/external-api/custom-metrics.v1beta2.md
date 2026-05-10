# Kubernetes Custom Metrics (v1beta2)

Package v1beta2 is the v1beta2 version of the custom_metrics API.

## Resource Types

* [MetricListOptions](#custom-metrics-k8s-io-v1beta2-MetricListOptions)
* [MetricValue](#custom-metrics-k8s-io-v1beta2-MetricValue)
* [MetricValueList](#custom-metrics-k8s-io-v1beta2-MetricValueList)

## `MetricListOptions`

MetricListOptions is used to select metrics by their label selectors

| Field | Description |
| --- | --- |
| `apiVersion` string | `custom.metrics.k8s.io/v1beta2` |
| `kind` string | `MetricListOptions` |
| `labelSelector`  `string` | A selector to restrict the list of returned objects by their labels. Defaults to everything. |
| `metricLabelSelector`  `string` | A selector to restrict the list of returned metrics by their labels |

## `MetricValue`

**Appears in:**

* [MetricValueList](#custom-metrics-k8s-io-v1beta2-MetricValueList)

MetricValue is the metric value for some object

| Field | Description |
| --- | --- |
| `apiVersion` string | `custom.metrics.k8s.io/v1beta2` |
| `kind` string | `MetricValue` |
| `describedObject` **[Required]**  [`core/v1.ObjectReference`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#objectreference-v1-core) | a reference to the described object |
| `metric` **[Required]**  [`MetricIdentifier`](#custom-metrics-k8s-io-v1beta2-MetricIdentifier) | No description provided. |
| `timestamp` **[Required]**  [`meta/v1.Time`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#time-v1-meta) | indicates the time at which the metrics were produced |
| `windowSeconds` **[Required]**  `int64` | indicates the window ([Timestamp-Window, Timestamp]) from which these metrics were calculated, when returning rate metrics calculated from cumulative metrics (or zero for non-calculated instantaneous metrics). |
| `value` **[Required]**  [`k8s.io/apimachinery/pkg/api/resource.Quantity`](https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity) | the value of the metric for this |

## `MetricValueList`

MetricValueList is a list of values for a given metric for some set of objects

| Field | Description |
| --- | --- |
| `apiVersion` string | `custom.metrics.k8s.io/v1beta2` |
| `kind` string | `MetricValueList` |
| `metadata` **[Required]**  [`meta/v1.ListMeta`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#listmeta-v1-meta) | No description provided. |
| `items` **[Required]**  [`[]MetricValue`](#custom-metrics-k8s-io-v1beta2-MetricValue) | the value of the metric across the described objects |

## `MetricIdentifier`

**Appears in:**

* [MetricValue](#custom-metrics-k8s-io-v1beta2-MetricValue)

MetricIdentifier identifies a metric by name and, optionally, selector

| Field | Description |
| --- | --- |
| `name` **[Required]**  `string` | name is the name of the given metric |
| `selector`  [`meta/v1.LabelSelector`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#labelselector-v1-meta) | selector represents the label selector that could be used to select this metric, and will generally just be the selector passed in to the query used to fetch this metric. When left blank, only the metric's Name will be used to gather metrics. |

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
