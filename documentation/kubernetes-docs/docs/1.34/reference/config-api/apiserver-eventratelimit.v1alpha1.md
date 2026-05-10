# Event Rate Limit Configuration (v1alpha1)

## Resource Types

* [Configuration](#eventratelimit-admission-k8s-io-v1alpha1-Configuration)

## `Configuration`

Configuration provides configuration for the EventRateLimit admission
controller.

| Field | Description |
| --- | --- |
| `apiVersion` string | `eventratelimit.admission.k8s.io/v1alpha1` |
| `kind` string | `Configuration` |
| `limits` **[Required]**  [`[]Limit`](#eventratelimit-admission-k8s-io-v1alpha1-Limit) | limits are the limits to place on event queries received. Limits can be placed on events received server-wide, per namespace, per user, and per source+object. At least one limit is required. |

## `Limit`

**Appears in:**

* [Configuration](#eventratelimit-admission-k8s-io-v1alpha1-Configuration)

Limit is the configuration for a particular limit type

| Field | Description |
| --- | --- |
| `type` **[Required]**  [`LimitType`](#eventratelimit-admission-k8s-io-v1alpha1-LimitType) | type is the type of limit to which this configuration applies |
| `qps` **[Required]**  `int32` | qps is the number of event queries per second that are allowed for this type of limit. The qps and burst fields are used together to determine if a particular event query is accepted. The qps determines how many queries are accepted once the burst amount of queries has been exhausted. |
| `burst` **[Required]**  `int32` | burst is the burst number of event queries that are allowed for this type of limit. The qps and burst fields are used together to determine if a particular event query is accepted. The burst determines the maximum size of the allowance granted for a particular bucket. For example, if the burst is 10 and the qps is 3, then the admission control will accept 10 queries before blocking any queries. Every second, 3 more queries will be allowed. If some of that allowance is not used, then it will roll over to the next second, until the maximum allowance of 10 is reached. |
| `cacheSize`  `int32` | cacheSize is the size of the LRU cache for this type of limit. If a bucket is evicted from the cache, then the allowance for that bucket is reset. If more queries are later received for an evicted bucket, then that bucket will re-enter the cache with a clean slate, giving that bucket a full allowance of burst queries.  The default cache size is 4096.  If limitType is 'server', then cacheSize is ignored. |

## `LimitType`

(Alias of `string`)

**Appears in:**

* [Limit](#eventratelimit-admission-k8s-io-v1alpha1-Limit)

LimitType is the type of the limit (e.g., per-namespace)

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
