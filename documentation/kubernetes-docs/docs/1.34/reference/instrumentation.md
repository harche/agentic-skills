# Instrumentation

---

##### [Kubernetes Component SLI Metrics](/docs/reference/instrumentation/slis/)

High-level indicators for measuring the reliability and performance of Kubernetes components.

##### [CRI Pod & Container Metrics](/docs/reference/instrumentation/cri-pod-container-metrics/)

Collection of Pod & Container metrics via the CRI.

##### [Node metrics data](/docs/reference/instrumentation/node-metrics/)

Mechanisms for accessing metrics at node, volume, pod and container level, as seen by the kubelet.

##### [Understand Pressure Stall Information (PSI) Metrics](/docs/reference/instrumentation/understand-psi-metrics/)

Detailed explanation of Pressure Stall Information (PSI) metrics and how to use them to identify resource pressure in Kubernetes.

##### [Kubernetes z-pages](/docs/reference/instrumentation/zpages/)

Provides runtime diagnostics for Kubernetes components, offering insights into component runtime status and configuration flags.

##### [Kubernetes Metrics Reference](/docs/reference/instrumentation/metrics/)

Details of the metric data that Kubernetes components export.

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
