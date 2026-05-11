# Assign Pods to Nodes using Node Affinity

This page shows how to assign a Kubernetes Pod to a particular node using Node Affinity in a
Kubernetes cluster.

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

Your Kubernetes server must be at or later than version v1.10.

To check the version, enter `kubectl version`.

## Add a label to a node

1. List the nodes in your cluster, along with their labels:

   ```
   kubectl get nodes --show-labels
   ```

   The output is similar to this:

   ```
   NAME      STATUS    ROLES    AGE     VERSION        LABELS
   worker0   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker0
   worker1   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker1
   worker2   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker2
   ```
2. Choose one of your nodes, and add a label to it:

   ```
   kubectl label nodes <your-node-name> disktype=ssd
   ```

   where `<your-node-name>` is the name of your chosen node.
3. Verify that your chosen node has a `disktype=ssd` label:

   ```
   kubectl get nodes --show-labels
   ```

   The output is similar to this:

   ```
   NAME      STATUS    ROLES    AGE     VERSION        LABELS
   worker0   Ready     <none>   1d      v1.13.0        ...,disktype=ssd,kubernetes.io/hostname=worker0
   worker1   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker1
   worker2   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker2
   ```

   In the preceding output, you can see that the `worker0` node has a
   `disktype=ssd` label.

## Schedule a Pod using required node affinity

This manifest describes a Pod that has a `requiredDuringSchedulingIgnoredDuringExecution` node affinity,`disktype: ssd`.
This means that the pod will get scheduled only on a node that has a `disktype=ssd` label.

[`pods/pod-nginx-required-affinity.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/pod-nginx-required-affinity.yaml)![](/images/copycode.svg "Copy pods/pod-nginx-required-affinity.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
```

1. Apply the manifest to create a Pod that is scheduled onto your
   chosen node:

   ```
   kubectl apply -f https://k8s.io/examples/pods/pod-nginx-required-affinity.yaml
   ```
2. Verify that the pod is running on your chosen node:

   ```
   kubectl get pods --output=wide
   ```

   The output is similar to this:

   ```
   NAME     READY     STATUS    RESTARTS   AGE    IP           NODE
   nginx    1/1       Running   0          13s    10.200.0.4   worker0
   ```

## Schedule a Pod using preferred node affinity

This manifest describes a Pod that has a `preferredDuringSchedulingIgnoredDuringExecution` node affinity,`disktype: ssd`.
This means that the pod will prefer a node that has a `disktype=ssd` label.

[`pods/pod-nginx-preferred-affinity.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/pod-nginx-preferred-affinity.yaml)![](/images/copycode.svg "Copy pods/pod-nginx-preferred-affinity.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  affinity:
    nodeAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 1
        preference:
          matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
```

1. Apply the manifest to create a Pod that is scheduled onto your
   chosen node:

   ```
   kubectl apply -f https://k8s.io/examples/pods/pod-nginx-preferred-affinity.yaml
   ```
2. Verify that the pod is running on your chosen node:

   ```
   kubectl get pods --output=wide
   ```

   The output is similar to this:

   ```
   NAME     READY     STATUS    RESTARTS   AGE    IP           NODE
   nginx    1/1       Running   0          13s    10.200.0.4   worker0
   ```

## What's next

Learn more about
[Node Affinity](/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity).

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
