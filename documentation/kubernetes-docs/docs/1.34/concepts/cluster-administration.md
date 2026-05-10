# Cluster Administration

Lower-level detail relevant to creating or administering a Kubernetes cluster.

The cluster administration overview is for anyone creating or administering a Kubernetes cluster.
It assumes some familiarity with core Kubernetes [concepts](/docs/concepts/).

## Planning a cluster

See the guides in [Setup](/docs/setup/) for examples of how to plan, set up, and configure
Kubernetes clusters. The solutions listed in this article are called *distros*.

> **Note:**
> Not all distros are actively maintained. Choose distros which have been tested with a recent
> version of Kubernetes.

Before choosing a guide, here are some considerations:

* Do you want to try out Kubernetes on your computer, or do you want to build a high-availability,
  multi-node cluster? Choose distros best suited for your needs.
* Will you be using **a hosted Kubernetes cluster**, such as
  [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/), or **hosting your own cluster**?
* Will your cluster be **on-premises**, or **in the cloud (IaaS)**? Kubernetes does not directly
  support hybrid clusters. Instead, you can set up multiple clusters.
* **If you are configuring Kubernetes on-premises**, consider which
  [networking model](/docs/concepts/cluster-administration/networking/) fits best.
* Will you be running Kubernetes on **"bare metal" hardware** or on **virtual machines (VMs)**?
* Do you **want to run a cluster**, or do you expect to do **active development of Kubernetes project code**?
  If the latter, choose an actively-developed distro. Some distros only use binary releases, but
  offer a greater variety of choices.
* Familiarize yourself with the [components](/docs/concepts/overview/components/) needed to run a cluster.

## Managing a cluster

* Learn how to [manage nodes](/docs/concepts/architecture/nodes/).

  + Read about [Node autoscaling](/docs/concepts/cluster-administration/node-autoscaling/).
* Learn how to set up and manage the [resource quota](/docs/concepts/policy/resource-quotas/) for shared clusters.

## Securing a cluster

* [Generate Certificates](/docs/tasks/administer-cluster/certificates/) describes the steps to
  generate certificates using different tool chains.
* [Kubernetes Container Environment](/docs/concepts/containers/container-environment/) describes
  the environment for Kubelet managed containers on a Kubernetes node.
* [Controlling Access to the Kubernetes API](/docs/concepts/security/controlling-access/) describes
  how Kubernetes implements access control for its own API.
* [Authenticating](/docs/reference/access-authn-authz/authentication/) explains authentication in
  Kubernetes, including the various authentication options.
* [Authorization](/docs/reference/access-authn-authz/authorization/) is separate from
  authentication, and controls how HTTP calls are handled.
* [Using Admission Controllers](/docs/reference/access-authn-authz/admission-controllers/)
  explains plug-ins which intercepts requests to the Kubernetes API server after authentication
  and authorization.
* [Admission Webhook Good Practices](/docs/concepts/cluster-administration/admission-webhooks-good-practices/)
  provides good practices and considerations when designing mutating admission
  webhooks and validating admission webhooks.
* [Using Sysctls in a Kubernetes Cluster](/docs/tasks/administer-cluster/sysctl-cluster/)
  describes to an administrator how to use the `sysctl` command-line tool to set kernel parameters
  .
* [Auditing](/docs/tasks/debug/debug-cluster/audit/) describes how to interact with Kubernetes'
  audit logs.

### Securing the kubelet

* [Control Plane-Node communication](/docs/concepts/architecture/control-plane-node-communication/)
* [TLS bootstrapping](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/)
* [Kubelet authentication/authorization](/docs/reference/access-authn-authz/kubelet-authn-authz/)

## Optional Cluster Services

* [DNS Integration](/docs/concepts/services-networking/dns-pod-service/) describes how to resolve
  a DNS name directly to a Kubernetes service.
* [Logging and Monitoring Cluster Activity](/docs/concepts/cluster-administration/logging/)
  explains how logging in Kubernetes works and how to implement it.

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
