This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/concepts/cluster-administration/).

# Cluster Administration

Lower-level detail relevant to creating or administering a Kubernetes cluster.

* 1: [Node Shutdowns](#pg-16c1422c18d5129a279e2665c901e8c3)
* 2: [Swap memory management](#pg-240bbf5f8a89640813a6d0052a7f25e1)
* 3: [Node Autoscaling](#pg-4ae6e7bda71061ba22fc25b550862444)
* 4: [Certificates](#pg-2bf9a93ab5ba014fb6ff70b22c29d432)
* 5: [Cluster Networking](#pg-d649067a69d8d5c7e71564b42b96909e)
* 6: [Observability](#pg-6dc1280c519a8fb0e17d2182a282f624)
* 7: [Admission Webhook Good Practices](#pg-36267e27053712ce65663b894ebc8b3c)
* 8: [Good practices for Dynamic Resource Allocation as a Cluster Admin](#pg-2b8f3836f8e444efb8b7997a89fd1e4e)
* 9: [Logging Architecture](#pg-c4b1e87a84441f8a90699a345ce48d68)
* 10: [Compatibility Version For Kubernetes Control Plane Components](#pg-ffefe4383ad78ecf6542f8d6943ad960)
* 11: [Metrics For Kubernetes System Components](#pg-cbfd3654996eae9fcdef009f70fa83f0)
* 12: [Metrics for Kubernetes Object States](#pg-0d497efe8a549d8f9ffeca15e365cf91)
* 13: [System Logs](#pg-5cc31ecfba86467f8884856412cfb6b2)
* 14: [Traces For Kubernetes System Components](#pg-3da54ad355f6fe6574d67bd9a9a42bcb)
* 15: [Proxies in Kubernetes](#pg-08e94e6a480e0d6b2de72d84a1b97617)
* 16: [API Priority and Fairness](#pg-31c9327d2332c585341b64ddafa19cdd)
* 17: [Installing Addons](#pg-85d633ae590aa20ec024f1b7af1d74fc)
* 18: [Coordinated Leader Election](#pg-9bbd2d79b9af3b1a869b28b010c515a6)

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
