# Node Reference Information

This section contains the following reference topics about nodes:

* the kubelet's [checkpoint API](/docs/reference/node/kubelet-checkpoint-api/)
* a list of [Articles on dockershim Removal and on Using CRI-compatible Runtimes](/docs/reference/node/topics-on-dockershim-and-cri-compatible-runtimes/)
* [Kubelet Device Manager API Versions](/docs/reference/node/device-plugin-api-versions/)
* [Node Labels Populated By The Kubelet](/docs/reference/node/node-labels/)
* [Local Files And Paths Used By The Kubelet](/docs/reference/node/kubelet-files/)
* [Node `.status` information](/docs/reference/node/node-status/)
* [Linux Node Swap Behaviors](/docs/reference/node/swap-behavior/)
* [Seccomp information](/docs/reference/node/seccomp/)

You can also read node reference details from elsewhere in the
Kubernetes documentation, including:

* [Node Metrics Data](/docs/reference/instrumentation/node-metrics/).
* [CRI Pod & Container Metrics](/docs/reference/instrumentation/cri-pod-container-metrics/).
* [Understand Pressure Stall Information (PSI) Metrics](/docs/reference/instrumentation/understand-psi-metrics/).

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
