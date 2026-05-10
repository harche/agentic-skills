# Use Port Forwarding to Access Applications in a Cluster

This page shows how to use `kubectl port-forward` to connect to a MongoDB
server running in a Kubernetes cluster. This type of connection can be useful
for database debugging.

## Before you begin

* You need to have a Kubernetes cluster, and the kubectl command-line tool must
  be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
  cluster, you can create one by using
  [minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
  or you can use one of these Kubernetes playgrounds:

  + [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
  + [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
  + [KodeKloud](https://kodekloud.com/public-playgrounds)
  + [Play with Kubernetes](https://labs.play-with-k8s.com/)Your Kubernetes server must be at or later than version v1.10.

  To check the version, enter `kubectl version`.
* Install [MongoDB Shell](https://www.mongodb.com/try/download/shell).

## Creating MongoDB deployment and service

1. Create a Deployment that runs MongoDB:

   ```
   kubectl apply -f https://k8s.io/examples/application/mongodb/mongo-deployment.yaml
   ```

   The output of a successful command verifies that the deployment was created:

   ```
   deployment.apps/mongo created
   ```

   View the pod status to check that it is ready:

   ```
   kubectl get pods
   ```

   The output displays the pod created:

   ```
   NAME                     READY   STATUS    RESTARTS   AGE
   mongo-75f59d57f4-4nd6q   1/1     Running   0          2m4s
   ```

   View the Deployment's status:

   ```
   kubectl get deployment
   ```

   The output displays that the Deployment was created:

   ```
   NAME    READY   UP-TO-DATE   AVAILABLE   AGE
   mongo   1/1     1            1           2m21s
   ```

   The Deployment automatically manages a ReplicaSet.
   View the ReplicaSet status using:

   ```
   kubectl get replicaset
   ```

   The output displays that the ReplicaSet was created:

   ```
   NAME               DESIRED   CURRENT   READY   AGE
   mongo-75f59d57f4   1         1         1       3m12s
   ```
2. Create a Service to expose MongoDB on the network:

   ```
   kubectl apply -f https://k8s.io/examples/application/mongodb/mongo-service.yaml
   ```

   The output of a successful command verifies that the Service was created:

   ```
   service/mongo created
   ```

   Check the Service created:

   ```
   kubectl get service mongo
   ```

   The output displays the service created:

   ```
   NAME    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)     AGE
   mongo   ClusterIP   10.96.41.183   <none>        27017/TCP   11s
   ```
3. Verify that the MongoDB server is running in the Pod, and listening on port 27017:

   ```
   # Change mongo-75f59d57f4-4nd6q to the name of the Pod
   kubectl get pod mongo-75f59d57f4-4nd6q --template='{{(index (index .spec.containers 0).ports 0).containerPort}}{{"\n"}}'
   ```

   The output displays the port for MongoDB in that Pod:

   ```
   27017
   ```

   27017 is the official TCP port for MongoDB.

## Forward a local port to a port on the Pod

1. `kubectl port-forward` allows using resource name, such as a pod name, to select a matching pod to port forward to.

   ```
   # Change mongo-75f59d57f4-4nd6q to the name of the Pod
   kubectl port-forward mongo-75f59d57f4-4nd6q 28015:27017
   ```

   which is the same as

   ```
   kubectl port-forward pods/mongo-75f59d57f4-4nd6q 28015:27017
   ```

   or

   ```
   kubectl port-forward deployment/mongo 28015:27017
   ```

   or

   ```
   kubectl port-forward replicaset/mongo-75f59d57f4 28015:27017
   ```

   or

   ```
   kubectl port-forward service/mongo 28015:27017
   ```

   Any of the above commands works. The output is similar to this:

   ```
   Forwarding from 127.0.0.1:28015 -> 27017
   Forwarding from [::1]:28015 -> 27017
   ```

   > **Note:**
   > `kubectl port-forward` does not return. To continue with the exercises, you will need to open another terminal.
2. Start the MongoDB command line interface:

   ```
   mongosh --port 28015
   ```
3. At the MongoDB command line prompt, enter the `ping` command:

   ```
   db.runCommand( { ping: 1 } )
   ```

   A successful ping request returns:

   ```
   { ok: 1 }
   ```

### Optionally let *kubectl* choose the local port

If you don't need a specific local port, you can let `kubectl` choose and allocate
the local port and thus relieve you from having to manage local port conflicts, with
the slightly simpler syntax:

```
kubectl port-forward deployment/mongo :27017
```

The `kubectl` tool finds a local port number that is not in use (avoiding low ports numbers,
because these might be used by other applications). The output is similar to:

```
Forwarding from 127.0.0.1:63753 -> 27017
Forwarding from [::1]:63753 -> 27017
```

## Discussion

Connections made to local port 28015 are forwarded to port 27017 of the Pod that
is running the MongoDB server. With this connection in place, you can use your
local workstation to debug the database that is running in the Pod.

> **Note:**
> `kubectl port-forward` is implemented for TCP ports only.
> The support for UDP protocol is tracked in
> [issue 47862](https://github.com/kubernetes/kubernetes/issues/47862).

## What's next

Learn more about [kubectl port-forward](/docs/reference/generated/kubectl/kubectl-commands/#port-forward).

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
