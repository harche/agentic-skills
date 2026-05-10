# Proxies in Kubernetes

This page explains proxies used with Kubernetes.

## Proxies

There are several different proxies you may encounter when using Kubernetes:

1. The [kubectl proxy](/docs/tasks/access-application-cluster/access-cluster/#directly-accessing-the-rest-api):

   * runs on a user's desktop or in a pod
   * proxies from a localhost address to the Kubernetes apiserver
   * client to proxy uses HTTP
   * proxy to apiserver uses HTTPS
   * locates apiserver
   * adds authentication headers
2. The [apiserver proxy](/docs/tasks/access-application-cluster/access-cluster-services/#discovering-builtin-services):

   * is a bastion built into the apiserver
   * connects a user outside of the cluster to cluster IPs which otherwise might not be reachable
   * runs in the apiserver processes
   * client to proxy uses HTTPS (or http if apiserver so configured)
   * proxy to target may use HTTP or HTTPS as chosen by proxy using available information
   * can be used to reach a Node, Pod, or Service
   * does load balancing when used to reach a Service
3. The [kube proxy](/docs/concepts/services-networking/service/#ips-and-vips):

   * runs on each node
   * proxies UDP, TCP and SCTP
   * does not understand HTTP
   * provides load balancing
   * is only used to reach services
4. A Proxy/Load-balancer in front of apiserver(s):

   * existence and implementation varies from cluster to cluster (e.g. nginx)
   * sits between all clients and one or more apiservers
   * acts as load balancer if there are several apiservers.
5. Cloud Load Balancers on external services:

   * are provided by some cloud providers (e.g. AWS ELB, Google Cloud Load Balancer)
   * are created automatically when the Kubernetes service has type `LoadBalancer`
   * usually supports UDP/TCP only
   * SCTP support is up to the load balancer implementation of the cloud provider
   * implementation varies by cloud provider.

Kubernetes users will typically not need to worry about anything other than the first two types. The cluster admin
will typically ensure that the latter types are set up correctly.

## Requesting redirects

Proxies have replaced redirect capabilities. Redirects have been deprecated.

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
