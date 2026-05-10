# Kubernetes External Metrics (v1beta1)

Package v1beta1 is the v1beta1 version of the external metrics API.

## Resource Types

* [ExternalMetricValue](#external-metrics-k8s-io-v1beta1-ExternalMetricValue)
* [ExternalMetricValueList](#external-metrics-k8s-io-v1beta1-ExternalMetricValueList)

## `ExternalMetricValue`

**Appears in:**

* [ExternalMetricValueList](#external-metrics-k8s-io-v1beta1-ExternalMetricValueList)

ExternalMetricValue is a metric value for external metric
A single metric value is identified by metric name and a set of string labels.
For one metric there can be multiple values with different sets of labels.

| Field | Description |
| --- | --- |
| `apiVersion` string | `external.metrics.k8s.io/v1beta1` |
| `kind` string | `ExternalMetricValue` |
| `metricName` **[Required]**  `string` | the name of the metric |
| `metricLabels` **[Required]**  `map[string]string` | a set of labels that identify a single time series for the metric |
| `timestamp` **[Required]**  [`meta/v1.Time`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#time-v1-meta) | indicates the time at which the metrics were produced |
| `window` **[Required]**  `int64` | indicates the window ([Timestamp-Window, Timestamp]) from which these metrics were calculated, when returning rate metrics calculated from cumulative metrics (or zero for non-calculated instantaneous metrics). |
| `value` **[Required]**  [`k8s.io/apimachinery/pkg/api/resource.Quantity`](https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity) | the value of the metric |

## `ExternalMetricValueList`

ExternalMetricValueList is a list of values for a given metric for some set labels

| Field | Description |
| --- | --- |
| `apiVersion` string | `external.metrics.k8s.io/v1beta1` |
| `kind` string | `ExternalMetricValueList` |
| `metadata` **[Required]**  [`meta/v1.ListMeta`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#listmeta-v1-meta) | No description provided. |
| `items` **[Required]**  [`[]ExternalMetricValue`](#external-metrics-k8s-io-v1beta1-ExternalMetricValue) | value of the metric matching a given set of labels |

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
