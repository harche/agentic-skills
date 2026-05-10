# Installing Kubernetes with deployment tools

There are many methods and tools for setting up your own production Kubernetes cluster.
For example:

* [kubeadm](/docs/setup/production-environment/tools/kubeadm/)
* [Cluster API](https://cluster-api.sigs.k8s.io/): A Kubernetes sub-project focused on
  providing declarative APIs and tooling to simplify provisioning, upgrading, and operating
  multiple Kubernetes clusters.
* [kops](https://kops.sigs.k8s.io/): An automated cluster provisioning tool.
  For tutorials, best practices, configuration options and information on
  reaching out to the community, please check the
  [`kOps` website](https://kops.sigs.k8s.io/) for details.
* [kubespray](https://kubespray.io/):
  A composition of [Ansible](https://docs.ansible.com/) playbooks,
  [inventory](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/ansible/inventory.md),
  provisioning tools, and domain knowledge for generic OS/Kubernetes clusters configuration
  management tasks. You can reach out to the community on Slack channel
  [#kubespray](https://kubernetes.slack.com/messages/kubespray/).

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
