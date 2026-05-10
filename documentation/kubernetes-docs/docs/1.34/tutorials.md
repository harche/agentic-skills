# Tutorials

This section of the Kubernetes documentation contains tutorials.
A tutorial shows how to accomplish a goal that is larger than a single
[task](/docs/tasks/). Typically a tutorial has several sections,
each of which has a sequence of steps.
Before walking through each tutorial, you may want to bookmark the
[Standardized Glossary](/docs/reference/glossary/) page for later references.

## Basics

* [Kubernetes Basics](/docs/tutorials/kubernetes-basics/) is an in-depth interactive tutorial that helps you understand the Kubernetes system and try out some basic Kubernetes features.
* [Introduction to Kubernetes (edX)](https://www.edx.org/course/introduction-kubernetes-linuxfoundationx-lfs158x)
* [Hello Minikube](/docs/tutorials/hello-minikube/)

## Configuration

* [Configuring Redis Using a ConfigMap](/docs/tutorials/configuration/configure-redis-using-configmap/)

## Authoring Pods

* [Adopting Sidecar Containers](/docs/tutorials/configuration/pod-sidecar-containers/)

## Stateless Applications

* [Exposing an External IP Address to Access an Application in a Cluster](/docs/tutorials/stateless-application/expose-external-ip-address/)
* [Example: Deploying PHP Guestbook application with Redis](/docs/tutorials/stateless-application/guestbook/)

## Stateful Applications

* [StatefulSet Basics](/docs/tutorials/stateful-application/basic-stateful-set/)
* [Example: WordPress and MySQL with Persistent Volumes](/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/)
* [Example: Deploying Cassandra with Stateful Sets](/docs/tutorials/stateful-application/cassandra/)
* [Running ZooKeeper, A CP Distributed System](/docs/tutorials/stateful-application/zookeeper/)

## Services

* [Connecting Applications with Services](/docs/tutorials/services/connect-applications-service/)
* [Using Source IP](/docs/tutorials/services/source-ip/)

## Security

* [Apply Pod Security Standards at Cluster level](/docs/tutorials/security/cluster-level-pss/)
* [Apply Pod Security Standards at Namespace level](/docs/tutorials/security/ns-level-pss/)
* [Restrict a Container's Access to Resources with AppArmor](/docs/tutorials/security/apparmor/)
* [Seccomp](/docs/tutorials/security/seccomp/)

## Cluster Management

* [Configuring Swap Memory on Kubernetes Nodes](/docs/tutorials/cluster-management/provision-swap-memory/)
* [Running Kubelet in Standalone Mode](/docs/tutorials/cluster-management/kubelet-standalone/)
* [Install Drivers and Allocate Devices with DRA](/docs/tutorials/cluster-management/install-use-dra/)

## What's next

If you would like to write a tutorial, see
[Content Page Types](/docs/contribute/style/page-content-types/)
for information about the tutorial page type.

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
