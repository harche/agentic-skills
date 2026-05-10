# Run Applications

Run and manage both stateless and stateful applications.

---

##### [Run a Stateless Application Using a Deployment](/docs/tasks/run-application/run-stateless-application-deployment/)

##### [Run a Single-Instance Stateful Application](/docs/tasks/run-application/run-single-instance-stateful-application/)

##### [Run a Replicated Stateful Application](/docs/tasks/run-application/run-replicated-stateful-application/)

##### [Scale a StatefulSet](/docs/tasks/run-application/scale-stateful-set/)

##### [Delete a StatefulSet](/docs/tasks/run-application/delete-stateful-set/)

##### [Force Delete StatefulSet Pods](/docs/tasks/run-application/force-delete-stateful-set-pod/)

##### [Horizontal Pod Autoscaling](/docs/tasks/run-application/horizontal-pod-autoscale/)

##### [HorizontalPodAutoscaler Walkthrough](/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)

##### [Specifying a Disruption Budget for your Application](/docs/tasks/run-application/configure-pdb/)

##### [Accessing the Kubernetes API from a Pod](/docs/tasks/run-application/access-api-from-pod/)

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
