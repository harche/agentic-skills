# Kubernetes API Aggregation Layer

The aggregation layer allows Kubernetes to be extended with additional APIs, beyond what is
offered by the core Kubernetes APIs.
The additional APIs can either be ready-made solutions such as a
[metrics server](https://github.com/kubernetes-sigs/metrics-server), or APIs that you develop yourself.

The aggregation layer is different from
[Custom Resource Definitions](/docs/concepts/extend-kubernetes/api-extension/custom-resources/),
which are a way to make the [kube-apiserver](/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API.")
recognise new kinds of object.

## Aggregation layer

The aggregation layer runs in-process with the kube-apiserver. Until an extension resource is
registered, the aggregation layer will do nothing. To register an API, you add an *APIService*
object, which "claims" the URL path in the Kubernetes API. At that point, the aggregation layer
will proxy anything sent to that API path (e.g. `/apis/myextension.mycompany.io/v1/…`) to the
registered APIService.

The most common way to implement the APIService is to run an *extension API server* in Pod(s) that
run in your cluster. If you're using the extension API server to manage resources in your cluster,
the extension API server (also written as "extension-apiserver") is typically paired with one or
more [controllers](/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state."). The apiserver-builder
library provides a skeleton for both extension API servers and the associated controller(s).

### Response latency

Extension API servers should have low latency networking to and from the kube-apiserver.
Discovery requests are required to round-trip from the kube-apiserver in five seconds or less.

If your extension API server cannot achieve that latency requirement, consider making changes that
let you meet it.

## What's next

* To get the aggregator working in your environment, [configure the aggregation layer](/docs/tasks/extend-kubernetes/configure-aggregation-layer/).
* Then, [setup an extension api-server](/docs/tasks/extend-kubernetes/setup-extension-api-server/) to work with the aggregation layer.
* Read about [APIService](/docs/reference/kubernetes-api/cluster-resources/api-service-v1/) in the API reference
* Learn about [Declarative Validation Concepts](/docs/reference/using-api/declarative-validation/), an internal mechanism for defining validation rules that in the future will help support validation for extension API server development.

Alternatively: learn how to
[extend the Kubernetes API using Custom Resource Definitions](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/).

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
