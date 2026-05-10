# Building a Basic DaemonSet

This page demonstrates how to build a basic [DaemonSet](/docs/concepts/workloads/controllers/daemonset "Ensures a copy of a Pod is running across a set of nodes in a cluster.")
that runs a Pod on every node in a Kubernetes cluster.
It covers a simple use case of mounting a file from the host, logging its contents using
an [init container](/docs/concepts/workloads/pods/init-containers/), and utilizing a pause container.

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

A Kubernetes cluster with at least two nodes (one control plane node and one worker node)
to demonstrate the behavior of DaemonSets.

## Define the DaemonSet

In this task, a basic DaemonSet is created which ensures that the copy of a Pod is scheduled on every node.
The Pod will use an init container to read and log the contents of `/etc/machine-id` from the host,
while the main container will be a `pause` container, which keeps the Pod running.

[`application/basic-daemonset.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/application/basic-daemonset.yaml)![](/images/copycode.svg "Copy application/basic-daemonset.yaml to clipboard")

```
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: example-daemonset
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: example
  template:
    metadata:
      labels:
        app.kubernetes.io/name: example
    spec:
      containers:
      - name: pause
        image: registry.k8s.io/pause
      initContainers:
      - name: log-machine-id
        image: busybox:1.37
        command: ['sh', '-c', 'cat /etc/machine-id > /var/log/machine-id.log']
        volumeMounts:
        - name: machine-id
          mountPath: /etc/machine-id
          readOnly: true
        - name: log-dir
          mountPath: /var/log
      volumes:
      - name: machine-id
        hostPath:
          path: /etc/machine-id
          type: File
      - name: log-dir
        hostPath:
          path: /var/log
```

1. Create a DaemonSet based on the (YAML) manifest:

   ```
   kubectl apply -f https://k8s.io/examples/application/basic-daemonset.yaml
   ```
2. Once applied, you can verify that the DaemonSet is running a Pod on every node in the cluster:

   ```
   kubectl get pods -o wide
   ```

   The output will list one Pod per node, similar to:

   ```
   NAME                                READY   STATUS    RESTARTS   AGE    IP       NODE
   example-daemonset-xxxxx             1/1     Running   0          5m     x.x.x.x  node-1
   example-daemonset-yyyyy             1/1     Running   0          5m     x.x.x.x  node-2
   ```
3. You can inspect the contents of the logged `/etc/machine-id` file by checking
   the log directory mounted from the host:

   ```
   kubectl exec <pod-name> -- cat /var/log/machine-id.log
   ```

   Where `<pod-name>` is the name of one of your Pods.

## Cleaning up

To delete the DaemonSet, run this command:

```
kubectl delete --cascade=foreground --ignore-not-found --now daemonsets/example-daemonset
```

This simple DaemonSet example introduces key components like init containers and host path volumes,
which can be expanded upon for more advanced use cases. For more details refer to
[DaemonSet](/docs/concepts/workloads/controllers/daemonset/).

## What's next

* See [Performing a rolling update on a DaemonSet](/docs/tasks/manage-daemon/update-daemon-set/)
* See [Creating a DaemonSet to adopt existing DaemonSet pods](/docs/concepts/workloads/controllers/daemonset/)

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
