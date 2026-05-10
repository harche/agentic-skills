# Dual-stack support with kubeadm

FEATURE STATE:
`Kubernetes v1.23 [stable]`

Your Kubernetes cluster includes [dual-stack](/docs/concepts/services-networking/dual-stack/)
networking, which means that cluster networking lets you use either address family.
In a cluster, the control plane can assign both an IPv4 address and an IPv6 address to a single
[Pod](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") or a [Service](/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.").

## Before you begin

You need to have installed the [kubeadm](/docs/reference/setup-tools/kubeadm/ "A tool for quickly installing Kubernetes and setting up a secure cluster.") tool,
following the steps from [Installing kubeadm](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/).

For each server that you want to use as a [node](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes."),
make sure it allows IPv6 forwarding.

### Enable IPv6 packet forwarding

To check if IPv6 packet forwarding is enabled:

```
sysctl net.ipv6.conf.all.forwarding
```

If the output is `net.ipv6.conf.all.forwarding = 1` it is already enabled.
Otherwise it is not enabled yet.

To manually enable IPv6 packet forwarding:

```
# sysctl params required by setup, params persist across reboots
cat <<EOF | sudo tee -a /etc/sysctl.d/k8s.conf
net.ipv6.conf.all.forwarding = 1
EOF

# Apply sysctl params without reboot
sudo sysctl --system
```

You need to have an IPv4 and and IPv6 address range to use. Cluster operators typically
use private address ranges for IPv4. For IPv6, a cluster operator typically chooses a global
unicast address block from within `2000::/3`, using a range that is assigned to the operator.
You don't have to route the cluster's IP address ranges to the public internet.

The size of the IP address allocations should be suitable for the number of Pods and
Services that you are planning to run.

> **Note:**
> If you are upgrading an existing cluster with the `kubeadm upgrade` command,
> `kubeadm` does not support making modifications to the pod IP address range
> (“cluster CIDR”) nor to the cluster's Service address range (“Service CIDR”).

### Create a dual-stack cluster

To create a dual-stack cluster with `kubeadm init` you can pass command line arguments
similar to the following example:

```
# These address ranges are examples
kubeadm init --pod-network-cidr=10.244.0.0/16,2001:db8:42:0::/56 --service-cidr=10.96.0.0/16,2001:db8:42:1::/112
```

To make things clearer, here is an example kubeadm
[configuration file](/docs/reference/config-api/kubeadm-config.v1beta4/)
`kubeadm-config.yaml` for the primary dual-stack control plane node.

```
---
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
networking:
  podSubnet: 10.244.0.0/16,2001:db8:42:0::/56
  serviceSubnet: 10.96.0.0/16,2001:db8:42:1::/112
---
apiVersion: kubeadm.k8s.io/v1beta4
kind: InitConfiguration
localAPIEndpoint:
  advertiseAddress: "10.100.0.1"
  bindPort: 6443
nodeRegistration:
  kubeletExtraArgs:
  - name: "node-ip"
    value: "10.100.0.2,fd00:1:2:3::2"
```

`advertiseAddress` in InitConfiguration specifies the IP address that the API Server
will advertise it is listening on. The value of `advertiseAddress` equals the
`--apiserver-advertise-address` flag of `kubeadm init`.

Run kubeadm to initiate the dual-stack control plane node:

```
kubeadm init --config=kubeadm-config.yaml
```

The kube-controller-manager flags `--node-cidr-mask-size-ipv4|--node-cidr-mask-size-ipv6`
are set with default values. See [configure IPv4/IPv6 dual stack](/docs/concepts/services-networking/dual-stack/#configure-ipv4-ipv6-dual-stack).

> **Note:**
> The `--apiserver-advertise-address` flag does not support dual-stack.

### Join a node to dual-stack cluster

Before joining a node, make sure that the node has IPv6 routable network interface and allows IPv6 forwarding.

Here is an example kubeadm [configuration file](/docs/reference/config-api/kubeadm-config.v1beta4/)
`kubeadm-config.yaml` for joining a worker node to the cluster.

```
apiVersion: kubeadm.k8s.io/v1beta4
kind: JoinConfiguration
discovery:
  bootstrapToken:
    apiServerEndpoint: 10.100.0.1:6443
    token: "clvldh.vjjwg16ucnhp94qr"
    caCertHashes:
    - "sha256:a4863cde706cfc580a439f842cc65d5ef112b7b2be31628513a9881cf0d9fe0e"
    # change auth info above to match the actual token and CA certificate hash for your cluster
nodeRegistration:
  kubeletExtraArgs:
  - name: "node-ip"
    value: "10.100.0.2,fd00:1:2:3::3"
```

Also, here is an example kubeadm [configuration file](/docs/reference/config-api/kubeadm-config.v1beta4/)
`kubeadm-config.yaml` for joining another control plane node to the cluster.

```
apiVersion: kubeadm.k8s.io/v1beta4
kind: JoinConfiguration
controlPlane:
  localAPIEndpoint:
    advertiseAddress: "10.100.0.2"
    bindPort: 6443
discovery:
  bootstrapToken:
    apiServerEndpoint: 10.100.0.1:6443
    token: "clvldh.vjjwg16ucnhp94qr"
    caCertHashes:
    - "sha256:a4863cde706cfc580a439f842cc65d5ef112b7b2be31628513a9881cf0d9fe0e"
    # change auth info above to match the actual token and CA certificate hash for your cluster
nodeRegistration:
  kubeletExtraArgs:
  - name: "node-ip"
    value: "10.100.0.2,fd00:1:2:3::4"
```

`advertiseAddress` in JoinConfiguration.controlPlane specifies the IP address that the
API Server will advertise it is listening on. The value of `advertiseAddress` equals
the `--apiserver-advertise-address` flag of `kubeadm join`.

```
kubeadm join --config=kubeadm-config.yaml
```

### Create a single-stack cluster

> **Note:**
> Dual-stack support doesn't mean that you need to use dual-stack addressing.
> You can deploy a single-stack cluster that has the dual-stack networking feature enabled.

To make things more clear, here is an example kubeadm
[configuration file](/docs/reference/config-api/kubeadm-config.v1beta4/)
`kubeadm-config.yaml` for the single-stack control plane node.

```
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
networking:
  podSubnet: 10.244.0.0/16
  serviceSubnet: 10.96.0.0/16
```

## What's next

* [Validate IPv4/IPv6 dual-stack](/docs/tasks/network/validate-dual-stack/) networking
* Read about [Dual-stack](/docs/concepts/services-networking/dual-stack/) cluster networking
* Learn more about the kubeadm [configuration format](/docs/reference/config-api/kubeadm-config.v1beta4/)

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
