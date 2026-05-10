# Configure Pods and Containers

Perform common configuration tasks for Pods and containers.

---

##### [Assign Memory Resources to Containers and Pods](/docs/tasks/configure-pod-container/assign-memory-resource/)

##### [Assign CPU Resources to Containers and Pods](/docs/tasks/configure-pod-container/assign-cpu-resource/)

##### [Assign Devices to Pods and Containers](/docs/tasks/configure-pod-container/assign-resources/)

Assign infrastructure resources to your Kubernetes workloads.

##### [Assign Pod-level CPU and memory resources](/docs/tasks/configure-pod-container/assign-pod-level-resources/)

##### [Configure GMSA for Windows Pods and containers](/docs/tasks/configure-pod-container/configure-gmsa/)

##### [Resize CPU and Memory Resources assigned to Containers](/docs/tasks/configure-pod-container/resize-container-resources/)

##### [Configure RunAsUserName for Windows pods and containers](/docs/tasks/configure-pod-container/configure-runasusername/)

##### [Create a Windows HostProcess Pod](/docs/tasks/configure-pod-container/create-hostprocess-pod/)

##### [Configure Quality of Service for Pods](/docs/tasks/configure-pod-container/quality-service-pod/)

##### [Assign Extended Resources to a Container](/docs/tasks/configure-pod-container/extended-resource/)

##### [Configure a Pod to Use a Volume for Storage](/docs/tasks/configure-pod-container/configure-volume-storage/)

##### [Configure a Pod to Use a PersistentVolume for Storage](/docs/tasks/configure-pod-container/configure-persistent-volume-storage/)

##### [Configure a Pod to Use a Projected Volume for Storage](/docs/tasks/configure-pod-container/configure-projected-volume-storage/)

##### [Configure a Security Context for a Pod or Container](/docs/tasks/configure-pod-container/security-context/)

##### [Configure Service Accounts for Pods](/docs/tasks/configure-pod-container/configure-service-account/)

##### [Pull an Image from a Private Registry](/docs/tasks/configure-pod-container/pull-image-private-registry/)

##### [Configure Liveness, Readiness and Startup Probes](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)

##### [Assign Pods to Nodes](/docs/tasks/configure-pod-container/assign-pods-nodes/)

##### [Assign Pods to Nodes using Node Affinity](/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/)

##### [Configure Pod Initialization](/docs/tasks/configure-pod-container/configure-pod-initialization/)

##### [Attach Handlers to Container Lifecycle Events](/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/)

##### [Configure a Pod to Use a ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/)

##### [Share Process Namespace between Containers in a Pod](/docs/tasks/configure-pod-container/share-process-namespace/)

##### [Use a User Namespace With a Pod](/docs/tasks/configure-pod-container/user-namespaces/)

##### [Use an Image Volume With a Pod](/docs/tasks/configure-pod-container/image-volumes/)

##### [Create static Pods](/docs/tasks/configure-pod-container/static-pod/)

##### [Translate a Docker Compose File to Kubernetes Resources](/docs/tasks/configure-pod-container/translate-compose-kubernetes/)

##### [Enforce Pod Security Standards by Configuring the Built-in Admission Controller](/docs/tasks/configure-pod-container/enforce-standards-admission-controller/)

##### [Enforce Pod Security Standards with Namespace Labels](/docs/tasks/configure-pod-container/enforce-standards-namespace-labels/)

##### [Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller](/docs/tasks/configure-pod-container/migrate-from-psp/)

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
