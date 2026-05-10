# Communication between Nodes and the Control Plane

This document catalogs the communication paths between the [API server](/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API.")
and the Kubernetes [cluster](/docs/reference/glossary/?all=true#term-cluster "A set of worker machines, called nodes, that run containerized applications. Every cluster has at least one worker node.").
The intent is to allow users to customize their installation to harden the network configuration
such that the cluster can be run on an untrusted network (or on fully public IPs on a cloud
provider).

## Node to Control Plane

Kubernetes has a "hub-and-spoke" API pattern. All API usage from nodes (or the pods they run)
terminates at the API server. None of the other control plane components are designed to expose
remote services. The API server is configured to listen for remote connections on a secure HTTPS
port (typically 443) with one or more forms of client
[authentication](/docs/reference/access-authn-authz/authentication/) enabled.
One or more forms of [authorization](/docs/reference/access-authn-authz/authorization/) should be
enabled, especially if [anonymous requests](/docs/reference/access-authn-authz/authentication/#anonymous-requests)
or [service account tokens](/docs/reference/access-authn-authz/authentication/#service-account-tokens)
are allowed.

Nodes should be provisioned with the public root [certificate](/docs/tasks/tls/managing-tls-in-a-cluster/ "A cryptographically secure file used to validate access to the Kubernetes cluster.") for the cluster such that they can
connect securely to the API server along with valid client credentials. A good approach is that the
client credentials provided to the kubelet are in the form of a client certificate. See
[kubelet TLS bootstrapping](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/)
for automated provisioning of kubelet client certificates.

[Pods](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") that wish to connect to the API server can do so securely by leveraging a service account so
that Kubernetes will automatically inject the public root certificate and a valid bearer token
into the pod when it is instantiated.
The `kubernetes` service (in `default` namespace) is configured with a virtual IP address that is
redirected (via `kube-proxy`) to the HTTPS endpoint on the API server.

The control plane components also communicate with the API server over the secure port.

As a result, the default operating mode for connections from the nodes and pod running on the
nodes to the control plane is secured by default and can run over untrusted and/or public
networks.

## Control plane to node

There are two primary communication paths from the control plane (the API server) to the nodes.
The first is from the API server to the [kubelet](/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") process which runs on each node in the cluster.
The second is from the API server to any node, pod, or service through the API server's *proxy*
functionality.

### API server to kubelet

The connections from the API server to the kubelet are used for:

* Fetching logs for pods.
* Attaching (usually through `kubectl`) to running pods.
* Providing the kubelet's port-forwarding functionality.

These connections terminate at the kubelet's HTTPS endpoint. By default, the API server does not
verify the kubelet's serving certificate, which makes the connection subject to man-in-the-middle
attacks and **unsafe** to run over untrusted and/or public networks.

To verify this connection, use the `--kubelet-certificate-authority` flag to provide the API
server with a root certificate bundle to use to verify the kubelet's serving certificate.

If that is not possible, use [SSH tunneling](#ssh-tunnels) between the API server and kubelet if
required to avoid connecting over an
untrusted or public network.

Finally, [Kubelet authentication and/or authorization](/docs/reference/access-authn-authz/kubelet-authn-authz/)
should be enabled to secure the kubelet API.

### API server to nodes, pods, and services

The connections from the API server to a node, pod, or service default to plain HTTP connections
and are therefore neither authenticated nor encrypted. They can be run over a secure HTTPS
connection by prefixing `https:` to the node, pod, or service name in the API URL, but they will
not validate the certificate provided by the HTTPS endpoint nor provide client credentials. So
while the connection will be encrypted, it will not provide any guarantees of integrity. These
connections **are not currently safe** to run over untrusted or public networks.

### SSH tunnels

Kubernetes supports [SSH tunnels](https://www.ssh.com/academy/ssh/tunneling) to protect the control plane to nodes communication paths. In this
configuration, the API server initiates an SSH tunnel to each node in the cluster (connecting to
the SSH server listening on port 22) and passes all traffic destined for a kubelet, node, pod, or
service through the tunnel.
This tunnel ensures that the traffic is not exposed outside of the network in which the nodes are
running.

> **Note:**
> SSH tunnels are currently deprecated, so you shouldn't opt to use them unless you know what you
> are doing. The [Konnectivity service](#konnectivity-service) is a replacement for this
> communication channel.

### Konnectivity service

FEATURE STATE:
`Kubernetes v1.18 [beta]`

As a replacement to the SSH tunnels, the Konnectivity service provides TCP level proxy for the
control plane to cluster communication. The Konnectivity service consists of two parts: the
Konnectivity server in the control plane network and the Konnectivity agents in the nodes network.
The Konnectivity agents initiate connections to the Konnectivity server and maintain the network
connections.
After enabling the Konnectivity service, all control plane to nodes traffic goes through these
connections.

Follow the [Konnectivity service task](/docs/tasks/extend-kubernetes/setup-konnectivity/) to set
up the Konnectivity service in your cluster.

## What's next

* Read about the [Kubernetes control plane components](/docs/concepts/architecture/#control-plane-components)
* Learn more about [Hubs and Spoke model](https://book.kubebuilder.io/multiversion-tutorial/conversion-concepts.html#hubs-spokes-and-other-wheel-metaphors)
* Learn how to [Secure a Cluster](/docs/tasks/administer-cluster/securing-a-cluster/)
* Learn more about the [Kubernetes API](/docs/concepts/overview/kubernetes-api/)
* [Set up Konnectivity service](/docs/tasks/extend-kubernetes/setup-konnectivity/)
* [Use Port Forwarding to Access Applications in a Cluster](/docs/tasks/access-application-cluster/port-forward-access-application-cluster/)
* Learn how to [Fetch logs for Pods](/docs/tasks/debug/debug-application/debug-running-pod/#examine-pod-logs), [use kubectl port-forward](/docs/tasks/access-application-cluster/port-forward-access-application-cluster/#forward-a-local-port-to-a-port-on-the-pod)

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
