# Configuration APIs

---

##### [Client Authentication (v1)](/docs/reference/config-api/client-authentication.v1/)

##### [Client Authentication (v1beta1)](/docs/reference/config-api/client-authentication.v1beta1/)

##### [Event Rate Limit Configuration (v1alpha1)](/docs/reference/config-api/apiserver-eventratelimit.v1alpha1/)

##### [Image Policy API (v1alpha1)](/docs/reference/config-api/imagepolicy.v1alpha1/)

##### [kube-apiserver Admission (v1)](/docs/reference/config-api/apiserver-admission.v1/)

##### [kube-apiserver Audit Configuration (v1)](/docs/reference/config-api/apiserver-audit.v1/)

##### [kube-apiserver Configuration (v1)](/docs/reference/config-api/apiserver-config.v1/)

##### [kube-apiserver Configuration (v1alpha1)](/docs/reference/config-api/apiserver-config.v1alpha1/)

##### [kube-apiserver Configuration (v1beta1)](/docs/reference/config-api/apiserver-config.v1beta1/)

##### [kube-controller-manager Configuration (v1alpha1)](/docs/reference/config-api/kube-controller-manager-config.v1alpha1/)

##### [kube-proxy Configuration (v1alpha1)](/docs/reference/config-api/kube-proxy-config.v1alpha1/)

##### [kube-scheduler Configuration (v1)](/docs/reference/config-api/kube-scheduler-config.v1/)

##### [kubeadm Configuration (v1beta3)](/docs/reference/config-api/kubeadm-config.v1beta3/)

##### [kubeadm Configuration (v1beta4)](/docs/reference/config-api/kubeadm-config.v1beta4/)

##### [kubeconfig (v1)](/docs/reference/config-api/kubeconfig.v1/)

##### [Kubelet Configuration (v1)](/docs/reference/config-api/kubelet-config.v1/)

##### [Kubelet Configuration (v1alpha1)](/docs/reference/config-api/kubelet-config.v1alpha1/)

##### [Kubelet Configuration (v1beta1)](/docs/reference/config-api/kubelet-config.v1beta1/)

##### [Kubelet CredentialProvider (v1)](/docs/reference/config-api/kubelet-credentialprovider.v1/)

##### [kuberc (v1alpha1)](/docs/reference/config-api/kuberc.v1alpha1/)

##### [kuberc (v1beta1)](/docs/reference/config-api/kuberc.v1beta1/)

##### [WebhookAdmission Configuration (v1)](/docs/reference/config-api/apiserver-webhookadmission.v1/)

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
