# Kubernetes Security and Disclosure Information

This page describes Kubernetes security and disclosure information.

## Security Announcements

Join the [kubernetes-security-announce](https://groups.google.com/forum/#!forum/kubernetes-security-announce)
group for emails about security and major API announcements.

## Report a Vulnerability

We're extremely grateful for security researchers and users that report vulnerabilities to
the Kubernetes Open Source Community. All reports are thoroughly investigated by a set of community volunteers.

To make a report, submit your vulnerability to the [Kubernetes bug bounty program](https://hackerone.com/kubernetes).
This allows triage and handling of the vulnerability with standardized response times.

You can also email the private [security@kubernetes.io](mailto:security@kubernetes.io)
list with the security details and the details expected for
[all Kubernetes bug reports](https://github.com/kubernetes/kubernetes/blob/master/.github/ISSUE_TEMPLATE/bug-report.yaml).

You may encrypt your email to this list using the GPG keys of the
[Security Response Committee members](https://git.k8s.io/security/README.md#product-security-committee-psc).
Encryption using GPG is NOT required to make a disclosure.

### When Should I Report a Vulnerability?

* You think you discovered a potential security vulnerability in Kubernetes
* You are unsure how a vulnerability affects Kubernetes
* You think you discovered a vulnerability in another project that Kubernetes depends on
  + For projects with their own vulnerability reporting and disclosure process, please report it directly there

### When Should I NOT Report a Vulnerability?

* You need help tuning Kubernetes components for security
* You need help applying security related updates
* Your issue is not security related

## Security Vulnerability Response

Each report is acknowledged and analyzed by Security Response Committee members within 3 working days.
This will set off the [Security Release Process](https://git.k8s.io/security/security-release-process.md#disclosures).

Any vulnerability information shared with Security Response Committee stays within Kubernetes project
and will not be disseminated to other projects unless it is necessary to get the issue fixed.

As the security issue moves from triage, to identified fix, to release planning we will keep the reporter updated.

## Public Disclosure Timing

A public disclosure date is negotiated by the Kubernetes Security Response Committee and the bug submitter.
We prefer to fully disclose the bug as soon as possible once a user mitigation is available. It is reasonable
to delay disclosure when the bug or the fix is not yet fully understood, the solution is not well-tested,
or for vendor coordination. The timeframe for disclosure is from immediate (especially if it's already publicly known)
to a few weeks. For a vulnerability with a straightforward mitigation, we expect report date to disclosure date
to be on the order of 7 days. The Kubernetes Security Response Committee holds the final say when setting a disclosure date.

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
