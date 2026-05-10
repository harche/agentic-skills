# Administration with kubeadm

If you don't yet have a cluster, visit
[bootstrapping clusters with `kubeadm`](/docs/setup/production-environment/tools/kubeadm/).

The tasks in this section are aimed at people administering an existing cluster:

* [Adding Linux worker nodes](/docs/tasks/administer-cluster/kubeadm/adding-linux-nodes/)
* [Adding Windows worker nodes](/docs/tasks/administer-cluster/kubeadm/adding-windows-nodes/)
* [Upgrading kubeadm clusters](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
* [Upgrading Linux nodes](/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes/)
* [Upgrading Windows nodes](/docs/tasks/administer-cluster/kubeadm/upgrading-windows-nodes/)
* [Configuring a cgroup driver](/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/)
* [Certificate Management with kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/)
* [Reconfiguring a kubeadm cluster](/docs/tasks/administer-cluster/kubeadm/kubeadm-reconfigure/)
* [Changing The Kubernetes Package Repository](/docs/tasks/administer-cluster/kubeadm/change-package-repository/)

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
