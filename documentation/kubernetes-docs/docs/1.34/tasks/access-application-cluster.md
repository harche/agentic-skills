# Access Applications in a Cluster

Configure load balancing, port forwarding, or setup firewall or DNS configurations to access applications in a cluster.

---

##### [Deploy and Access the Kubernetes Dashboard](/docs/tasks/access-application-cluster/web-ui-dashboard/)

Deploy the web UI (Kubernetes Dashboard) and access it.

##### [Accessing Clusters](/docs/tasks/access-application-cluster/access-cluster/)

##### [Configure Access to Multiple Clusters](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)

##### [Use Port Forwarding to Access Applications in a Cluster](/docs/tasks/access-application-cluster/port-forward-access-application-cluster/)

##### [Use a Service to Access an Application in a Cluster](/docs/tasks/access-application-cluster/service-access-application-cluster/)

##### [Connect a Frontend to a Backend Using Services](/docs/tasks/access-application-cluster/connecting-frontend-backend/)

##### [Create an External Load Balancer](/docs/tasks/access-application-cluster/create-external-load-balancer/)

##### [List All Container Images Running in a Cluster](/docs/tasks/access-application-cluster/list-all-running-container-images/)

##### [Communicate Between Containers in the Same Pod Using a Shared Volume](/docs/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume/)

##### [Configure DNS for a Cluster](/docs/tasks/access-application-cluster/configure-dns-cluster/)

##### [Access Services Running on Clusters](/docs/tasks/access-application-cluster/access-cluster-services/)

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
