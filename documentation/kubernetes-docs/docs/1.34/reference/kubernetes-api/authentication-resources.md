# Authentication Resources

---

##### [ServiceAccount](/docs/reference/kubernetes-api/authentication-resources/service-account-v1/)

ServiceAccount binds together: * a name, understood by users, and perhaps by peripheral systems, for an identity * a principal that can be authenticated and authorized * a set of secrets.

##### [TokenRequest](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)

TokenRequest requests a token for a given service account.

##### [TokenReview](/docs/reference/kubernetes-api/authentication-resources/token-review-v1/)

TokenReview attempts to authenticate a token to a known user.

##### [CertificateSigningRequest](/docs/reference/kubernetes-api/authentication-resources/certificate-signing-request-v1/)

CertificateSigningRequest objects provide a mechanism to obtain x509 certificates by submitting a certificate signing request, and having it asynchronously approved and issued.

##### [ClusterTrustBundle v1beta1](/docs/reference/kubernetes-api/authentication-resources/cluster-trust-bundle-v1beta1/)

ClusterTrustBundle is a cluster-scoped container for X.

##### [SelfSubjectReview](/docs/reference/kubernetes-api/authentication-resources/self-subject-review-v1/)

SelfSubjectReview contains the user information that the kube-apiserver has about the user making this request.

##### [PodCertificateRequest v1alpha1](/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/)

PodCertificateRequest encodes a pod requesting a certificate from a given signer.

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
