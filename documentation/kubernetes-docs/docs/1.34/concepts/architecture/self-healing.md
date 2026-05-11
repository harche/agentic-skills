# Kubernetes Self-Healing

Kubernetes is designed with self-healing capabilities that help maintain the health and availability of workloads.
It automatically replaces failed containers, reschedules workloads when nodes become unavailable, and ensures that the desired state of the system is maintained.

## Self-Healing capabilities

* **Container-level restarts:** If a container inside a Pod fails, Kubernetes restarts it based on the [`restartPolicy`](/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy).
* **Replica replacement:** If a Pod in a [Deployment](/docs/concepts/workloads/controllers/deployment/) or [StatefulSet](/docs/concepts/workloads/controllers/statefulset/) fails, Kubernetes creates a replacement Pod to maintain the specified number of replicas.
  If a Pod that is part of a [DaemonSet](/docs/concepts/workloads/controllers/daemonset/) fails, the control plane
  creates a replacement Pod to run on the same node.
* **Persistent storage recovery:** If a node is running a Pod with a PersistentVolume (PV) attached, and the node fails, Kubernetes can reattach the volume to a new Pod on a different node.
* **Load balancing for Services:** If a Pod behind a [Service](/docs/concepts/services-networking/service/) fails, Kubernetes automatically removes it from the Service's endpoints to route traffic only to healthy Pods.

Here are some of the key components that provide Kubernetes self-healing:

* **[kubelet](/docs/concepts/architecture/#kubelet):** Ensures that containers are running, and restarts those that fail.
* **Deployment (via ReplicaSet), ReplicaSet, StatefulSet and DaemonSet controllers:** Maintain the desired number of Pod replicas.
* **PersistentVolume controller:** Manages volume attachment and detachment for stateful workloads.

## Considerations

* **Storage Failures:** If a persistent volume becomes unavailable, recovery steps may be required.
* **Application Errors:** Kubernetes can restart containers, but underlying application issues must be addressed separately.

## What's next

* Read more about [Pods](/docs/concepts/workloads/pods/)
* Learn about [Kubernetes Controllers](/docs/concepts/architecture/controller/)
* Explore [PersistentVolumes](/docs/concepts/storage/persistent-volumes/)
* Read about [node autoscaling](/docs/concepts/cluster-administration/node-autoscaling/). Node autoscaling
  also provides automatic healing if or when nodes fail in your cluster.

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
