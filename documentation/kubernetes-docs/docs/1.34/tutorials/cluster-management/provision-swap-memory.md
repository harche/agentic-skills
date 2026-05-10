# Configuring swap memory on Kubernetes nodes

This page provides an example of how to provision and configure swap memory on a Kubernetes node using kubeadm.

## Objectives

* Provision swap memory on a Kubernetes node using kubeadm.
* Learn to configure both encrypted and unencrypted swap.
* Learn to enable swap on boot.

## Before you begin

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [KodeKloud](https://kodekloud.com/public-playgrounds)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)

Your Kubernetes server must be at or later than version 1.33.

To check the version, enter `kubectl version`.

You need at least one worker node in your cluster which needs to run a Linux operating system.
It is required for this demo that the kubeadm tool be installed, following the steps outlined in the
[kubeadm installation guide](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/).

On each worker node where you will configure swap use, you need:

* `fallocate`
* `mkswap`
* `swapon`
* For encrypted swap space (recommended), you also need:
* `cryptsetup`

## Install a swap-enabled cluster with kubeadm

### Create a swap file and turn swap on

If swap is not enabled, there's a need to provision swap on the node.
The following sections demonstrate creating 4GiB of swap, both in the encrypted and unencrypted case.

* Setting up encrypted swap
  * Setting up unencrypted swap

An encrypted swap file can be set up as follows.
Bear in mind that this example uses the `cryptsetup` binary (which is available
on most Linux distributions).

```
# Allocate storage and restrict access
fallocate --length 4GiB /swapfile
chmod 600 /swapfile

# Create an encrypted device backed by the allocated storage
cryptsetup --type plain --cipher aes-xts-plain64 --key-size 256 -d /dev/urandom open /swapfile cryptswap

# Format the swap space
mkswap /dev/mapper/cryptswap

# Activate the swap space for paging
swapon /dev/mapper/cryptswap
```

An unencrypted swap file can be set up as follows.

```
# Allocate storage and restrict access
fallocate --length 4GiB /swapfile
chmod 600 /swapfile

# Format the swap space
mkswap /swapfile

# Activate the swap space for paging
swapon /swapfile
```

#### Verify that swap is enabled

Swap can be verified to be enabled with both `swapon -s` command or the `free` command.

Using `swapon -s`:

```
Filename       Type		Size		Used		Priority
/dev/dm-0      partition 	4194300		0		-2
```

Using `free -h`:

```
               total        used        free      shared  buff/cache   available
Mem:           3.8Gi       1.3Gi       249Mi        25Mi       2.5Gi       2.5Gi
Swap:          4.0Gi          0B       4.0Gi
```

#### Enable swap on boot

After setting up swap, to start the swap file at boot time,
you typically either set up a systemd unit to activate (encrypted) swap, or you
add a line similar to `/swapfile swap swap defaults 0 0` into `/etc/fstab`.

Using systemd for swap activation allows the system to delay kubelet start until swap is available,
if that is something you want to ensure.
In a similar way, using systemd allows your server to leave swap active until kubelet
(and, typically, your container runtime) have shut down.

### Set up kubelet configuration

After enabling swap on the node, kubelet needs to be configured to use it.
You need to select a [swap behavior](/docs/reference/node/swap-behavior/)
for this node. You'll configure *LimitedSwap* behavior for this tutorial.

Find and edit the kubelet configuration file, and:

* set `failSwapOn` to false
* set `memorySwap.swapBehavior` to LimitedSwap

```
 # this fragment goes into the kubelet's configuration file
 failSwapOn: false
 memorySwap:
     swapBehavior: LimitedSwap
```

In order for these configurations to take effect, kubelet needs to be restarted.
Typically you do that by running:

```
systemctl restart kubelet.service
```

You should find that the kubelet is now healthy, and that you can run Pods
that use swap memory as needed.

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
