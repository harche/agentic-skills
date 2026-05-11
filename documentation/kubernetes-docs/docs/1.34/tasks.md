# Tasks

This section of the Kubernetes documentation contains pages that
show how to do individual tasks. A task page shows how to do a
single thing, typically by giving a short sequence of steps.

If you would like to write a task page, see
[Creating a Documentation Pull Request](/docs/contribute/new-content/open-a-pr/).

---

##### [Install Tools](/docs/tasks/tools/)

Set up Kubernetes tools on your computer.

##### [Administer a Cluster](/docs/tasks/administer-cluster/)

Learn common tasks for administering a cluster.

##### [Configure Pods and Containers](/docs/tasks/configure-pod-container/)

Perform common configuration tasks for Pods and containers.

##### [Monitoring, Logging, and Debugging](/docs/tasks/debug/)

Set up monitoring and logging to troubleshoot a cluster, or debug a containerized application.

##### [Manage Kubernetes Objects](/docs/tasks/manage-kubernetes-objects/)

Declarative and imperative paradigms for interacting with the Kubernetes API.

##### [Managing Secrets](/docs/tasks/configmap-secret/)

Managing confidential settings data using Secrets.

##### [Inject Data Into Applications](/docs/tasks/inject-data-application/)

Specify configuration and other data for the Pods that run your workload.

##### [Run Applications](/docs/tasks/run-application/)

Run and manage both stateless and stateful applications.

##### [Run Jobs](/docs/tasks/job/)

Run Jobs using parallel processing.

##### [Access Applications in a Cluster](/docs/tasks/access-application-cluster/)

Configure load balancing, port forwarding, or setup firewall or DNS configurations to access applications in a cluster.

##### [Extend Kubernetes](/docs/tasks/extend-kubernetes/)

Understand advanced ways to adapt your Kubernetes cluster to the needs of your work environment.

##### [TLS](/docs/tasks/tls/)

Understand how to protect traffic within your cluster using Transport Layer Security (TLS).

##### [Manage Cluster Daemons](/docs/tasks/manage-daemon/)

Perform common tasks for managing a DaemonSet, such as performing a rolling update.

##### [Networking](/docs/tasks/network/)

Learn how to configure networking for your cluster.

##### [Extend kubectl with plugins](/docs/tasks/extend-kubectl/kubectl-plugins/)

Extend kubectl by creating and installing kubectl plugins.

##### [Manage HugePages](/docs/tasks/manage-hugepages/scheduling-hugepages/)

Configure and manage huge pages as a schedulable resource in a cluster.

##### [Schedule GPUs](/docs/tasks/manage-gpus/scheduling-gpus/)

Configure and schedule GPUs for use as a resource by nodes in a cluster.

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
