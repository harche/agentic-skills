# Concepts

The Concepts section helps you learn about the parts of the Kubernetes system and the abstractions Kubernetes uses to represent your [cluster](/docs/reference/glossary/?all=true#term-cluster "A set of worker machines, called nodes, that run containerized applications. Every cluster has at least one worker node."), and helps you obtain a deeper understanding of how Kubernetes works.

---

##### [Overview](/docs/concepts/overview/)

Kubernetes is a portable, extensible, open source platform for managing containerized workloads and services that facilitate both declarative configuration and automation. It has a large, rapidly growing ecosystem. Kubernetes services, support, and tools are widely available.

##### [Cluster Architecture](/docs/concepts/architecture/)

The architectural concepts behind Kubernetes.

##### [Containers](/docs/concepts/containers/)

Technology for packaging an application along with its runtime dependencies.

##### [Workloads](/docs/concepts/workloads/)

Understand Pods, the smallest deployable compute object in Kubernetes, and the higher-level abstractions that help you to run them.

##### [Services, Load Balancing, and Networking](/docs/concepts/services-networking/)

Concepts and resources behind networking in Kubernetes.

##### [Storage](/docs/concepts/storage/)

Ways to provide both long-term and temporary storage to Pods in your cluster.

##### [Configuration](/docs/concepts/configuration/)

Resources that Kubernetes provides for configuring Pods.

##### [Security](/docs/concepts/security/)

Concepts for keeping your cloud-native workload secure.

##### [Policies](/docs/concepts/policy/)

Manage security and best-practices with policies.

##### [Scheduling, Preemption and Eviction](/docs/concepts/scheduling-eviction/)

##### [Cluster Administration](/docs/concepts/cluster-administration/)

Lower-level detail relevant to creating or administering a Kubernetes cluster.

##### [Windows in Kubernetes](/docs/concepts/windows/)

Kubernetes supports nodes that run Microsoft Windows.

##### [Extending Kubernetes](/docs/concepts/extend-kubernetes/)

Different ways to change the behavior of your Kubernetes cluster.

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
