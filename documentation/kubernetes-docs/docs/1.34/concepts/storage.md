# Storage

Ways to provide both long-term and temporary storage to Pods in your cluster.

---

##### [Volumes](/docs/concepts/storage/volumes/)

##### [Persistent Volumes](/docs/concepts/storage/persistent-volumes/)

##### [Projected Volumes](/docs/concepts/storage/projected-volumes/)

##### [Ephemeral Volumes](/docs/concepts/storage/ephemeral-volumes/)

##### [Storage Classes](/docs/concepts/storage/storage-classes/)

##### [Volume Attributes Classes](/docs/concepts/storage/volume-attributes-classes/)

##### [Dynamic Volume Provisioning](/docs/concepts/storage/dynamic-provisioning/)

##### [Volume Snapshots](/docs/concepts/storage/volume-snapshots/)

##### [Volume Snapshot Classes](/docs/concepts/storage/volume-snapshot-classes/)

##### [CSI Volume Cloning](/docs/concepts/storage/volume-pvc-datasource/)

##### [Storage Capacity](/docs/concepts/storage/storage-capacity/)

##### [Node-specific Volume Limits](/docs/concepts/storage/storage-limits/)

##### [Local ephemeral storage](/docs/concepts/storage/ephemeral-storage/)

##### [Volume Health Monitoring](/docs/concepts/storage/volume-health-monitoring/)

##### [Windows Storage](/docs/concepts/storage/windows-storage/)

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
