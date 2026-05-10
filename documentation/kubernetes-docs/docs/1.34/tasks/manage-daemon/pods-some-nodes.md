# Running Pods on Only Some Nodes

This page demonstrates how can you run [Pods](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") on only some [Nodes](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") as part of a [DaemonSet](/docs/concepts/workloads/controllers/daemonset "Ensures a copy of a Pod is running across a set of nodes in a cluster.")

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

## Running Pods on only some Nodes

Imagine that you want to run a [DaemonSet](/docs/concepts/workloads/controllers/daemonset "Ensures a copy of a Pod is running across a set of nodes in a cluster."), but you only need to run those daemon pods
on nodes that have local solid state (SSD) storage. For example, the Pod might provide cache service to the
node, and the cache is only useful when low-latency local storage is available.

### Step 1: Add labels to your nodes

Add the label `ssd=true` to the nodes which have SSDs.

```
kubectl label nodes example-node-1 example-node-2 ssd=true
```

### Step 2: Create the manifest

Let's create a [DaemonSet](/docs/concepts/workloads/controllers/daemonset "Ensures a copy of a Pod is running across a set of nodes in a cluster.") which will provision the daemon pods on the SSD labeled [nodes](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") only.

Next, use a `nodeSelector` to ensure that the DaemonSet only runs Pods on nodes
with the `ssd` label set to `"true"`.

[`controllers/daemonset-label-selector.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/controllers/daemonset-label-selector.yaml)![](/images/copycode.svg "Copy controllers/daemonset-label-selector.yaml to clipboard")

```
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: ssd-driver
  labels:
    app: nginx
spec:
  selector:
    matchLabels:
      app: ssd-driver-pod
  template:
    metadata:
      labels:
        app: ssd-driver-pod
    spec:
      nodeSelector:
        ssd: "true"
      containers:
        - name: example-container
          image: example-image
```

### Step 3: Create the DaemonSet

Create the DaemonSet from the manifest by using `kubectl create` or `kubectl apply`

Let's label another node as `ssd=true`.

```
kubectl label nodes example-node-3 ssd=true
```

Labelling the node automatically triggers the control plane (specifically, the DaemonSet controller)
to run a new daemon pod on that node.

```
kubectl get pods -o wide
```

The output is similar to:

```
NAME                              READY     STATUS    RESTARTS   AGE    IP      NODE
<daemonset-name><some-hash-01>    1/1       Running   0          13s    .....   example-node-1
<daemonset-name><some-hash-02>    1/1       Running   0          13s    .....   example-node-2
<daemonset-name><some-hash-03>    1/1       Running   0          5s     .....   example-node-3
```

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
