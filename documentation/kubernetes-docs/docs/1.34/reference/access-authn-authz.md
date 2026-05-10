# API Access Control

For an introduction to how Kubernetes implements and controls API access,
read [Controlling Access to the Kubernetes API](/docs/concepts/security/controlling-access/).

Reference documentation:

* [Authenticating](/docs/reference/access-authn-authz/authentication/)
  + [Authenticating with Bootstrap Tokens](/docs/reference/access-authn-authz/bootstrap-tokens/)
* [Admission Controllers](/docs/reference/access-authn-authz/admission-controllers/)
  + [Dynamic Admission Control](/docs/reference/access-authn-authz/extensible-admission-controllers/)
* [Authorization](/docs/reference/access-authn-authz/authorization/)
  + [Role Based Access Control](/docs/reference/access-authn-authz/rbac/)
  + [Attribute Based Access Control](/docs/reference/access-authn-authz/abac/)
  + [Node Authorization](/docs/reference/access-authn-authz/node/)
  + [Webhook Authorization](/docs/reference/access-authn-authz/webhook/)
* [Certificate Signing Requests](/docs/reference/access-authn-authz/certificate-signing-requests/)
  + including [CSR approval](/docs/reference/access-authn-authz/certificate-signing-requests/#approval-rejection)
    and [certificate signing](/docs/reference/access-authn-authz/certificate-signing-requests/#signing)
* Service accounts
  + [Developer guide](/docs/tasks/configure-pod-container/configure-service-account/)
  + [Administration](/docs/reference/access-authn-authz/service-accounts-admin/)
* [Kubelet Authentication & Authorization](/docs/reference/access-authn-authz/kubelet-authn-authz/)
  + including kubelet [TLS bootstrapping](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/)

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
