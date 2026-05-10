# kubectl reference

---

##### [kubectl](/docs/reference/kubectl/generated/kubectl/)

##### [kubectl annotate](/docs/reference/kubectl/generated/kubectl_annotate/)

##### [kubectl api-resources](/docs/reference/kubectl/generated/kubectl_api-resources/)

##### [kubectl api-versions](/docs/reference/kubectl/generated/kubectl_api-versions/)

##### [kubectl apply](/docs/reference/kubectl/generated/kubectl_apply/)

##### [kubectl attach](/docs/reference/kubectl/generated/kubectl_attach/)

##### [kubectl auth](/docs/reference/kubectl/generated/kubectl_auth/)

##### [kubectl autoscale](/docs/reference/kubectl/generated/kubectl_autoscale/)

##### [kubectl certificate](/docs/reference/kubectl/generated/kubectl_certificate/)

##### [kubectl cluster-info](/docs/reference/kubectl/generated/kubectl_cluster-info/)

##### [kubectl completion](/docs/reference/kubectl/generated/kubectl_completion/)

##### [kubectl config](/docs/reference/kubectl/generated/kubectl_config/)

##### [kubectl cordon](/docs/reference/kubectl/generated/kubectl_cordon/)

##### [kubectl cp](/docs/reference/kubectl/generated/kubectl_cp/)

##### [kubectl create](/docs/reference/kubectl/generated/kubectl_create/)

##### [kubectl debug](/docs/reference/kubectl/generated/kubectl_debug/)

##### [kubectl delete](/docs/reference/kubectl/generated/kubectl_delete/)

##### [kubectl describe](/docs/reference/kubectl/generated/kubectl_describe/)

##### [kubectl diff](/docs/reference/kubectl/generated/kubectl_diff/)

##### [kubectl drain](/docs/reference/kubectl/generated/kubectl_drain/)

##### [kubectl edit](/docs/reference/kubectl/generated/kubectl_edit/)

##### [kubectl events](/docs/reference/kubectl/generated/kubectl_events/)

##### [kubectl exec](/docs/reference/kubectl/generated/kubectl_exec/)

##### [kubectl explain](/docs/reference/kubectl/generated/kubectl_explain/)

##### [kubectl expose](/docs/reference/kubectl/generated/kubectl_expose/)

##### [kubectl get](/docs/reference/kubectl/generated/kubectl_get/)

##### [kubectl kustomize](/docs/reference/kubectl/generated/kubectl_kustomize/)

##### [kubectl label](/docs/reference/kubectl/generated/kubectl_label/)

##### [kubectl logs](/docs/reference/kubectl/generated/kubectl_logs/)

##### [kubectl options](/docs/reference/kubectl/generated/kubectl_options/)

##### [kubectl patch](/docs/reference/kubectl/generated/kubectl_patch/)

##### [kubectl plugin](/docs/reference/kubectl/generated/kubectl_plugin/)

##### [kubectl port-forward](/docs/reference/kubectl/generated/kubectl_port-forward/)

##### [kubectl proxy](/docs/reference/kubectl/generated/kubectl_proxy/)

##### [kubectl replace](/docs/reference/kubectl/generated/kubectl_replace/)

##### [kubectl rollout](/docs/reference/kubectl/generated/kubectl_rollout/)

##### [kubectl run](/docs/reference/kubectl/generated/kubectl_run/)

##### [kubectl scale](/docs/reference/kubectl/generated/kubectl_scale/)

##### [kubectl set](/docs/reference/kubectl/generated/kubectl_set/)

##### [kubectl taint](/docs/reference/kubectl/generated/kubectl_taint/)

##### [kubectl top](/docs/reference/kubectl/generated/kubectl_top/)

##### [kubectl uncordon](/docs/reference/kubectl/generated/kubectl_uncordon/)

##### [kubectl version](/docs/reference/kubectl/generated/kubectl_version/)

##### [kubectl wait](/docs/reference/kubectl/generated/kubectl_wait/)

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
