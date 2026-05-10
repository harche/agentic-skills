# Use Cascading Deletion in a Cluster

This page shows you how to specify the type of
[cascading deletion](/docs/concepts/architecture/garbage-collection/#cascading-deletion)
to use in your cluster during [garbage collection](/docs/concepts/architecture/garbage-collection/ "A collective term for the various mechanisms Kubernetes uses to clean up cluster resources.").

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

You also need to [create a sample Deployment](/docs/tasks/run-application/run-stateless-application-deployment/#creating-and-exploring-an-nginx-deployment)
to experiment with the different types of cascading deletion. You will need to
recreate the Deployment for each type.

## Check owner references on your pods

Check that the `ownerReferences` field is present on your pods:

```
kubectl get pods -l app=nginx --output=yaml
```

The output has an `ownerReferences` field similar to this:

```
apiVersion: v1
    ...
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: nginx-deployment-6b474476c4
      uid: 4fdcd81c-bd5d-41f7-97af-3a3b759af9a7
    ...
```

## Use foreground cascading deletion

By default, Kubernetes uses [background cascading deletion](/docs/concepts/architecture/garbage-collection/#background-deletion)
to delete dependents of an object. You can switch to foreground cascading deletion
using either `kubectl` or the Kubernetes API, depending on the Kubernetes
version your cluster runs.

To check the version, enter `kubectl version`.

You can delete objects using foreground cascading deletion using `kubectl` or the
Kubernetes API.

**Using kubectl**

Run the following command:

```
kubectl delete deployment nginx-deployment --cascade=foreground
```

**Using the Kubernetes API**

1. Start a local proxy session:

   ```
   kubectl proxy --port=8080
   ```
2. Use `curl` to trigger deletion:

   ```
   curl -X DELETE localhost:8080/apis/apps/v1/namespaces/default/deployments/nginx-deployment \
       -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Foreground"}' \
       -H "Content-Type: application/json"
   ```

   The output contains a `foregroundDeletion` [finalizer](/docs/concepts/overview/working-with-objects/finalizers/ "A namespaced key that tells Kubernetes to wait until specific conditions are met before it fully deletes an object marked for deletion.")
   like this:

   ```
   "kind": "Deployment",
   "apiVersion": "apps/v1",
   "metadata": {
       "name": "nginx-deployment",
       "namespace": "default",
       "uid": "d1ce1b02-cae8-4288-8a53-30e84d8fa505",
       "resourceVersion": "1363097",
       "creationTimestamp": "2021-07-08T20:24:37Z",
       "deletionTimestamp": "2021-07-08T20:27:39Z",
       "finalizers": [
         "foregroundDeletion"
       ]
       ...
   ```

## Use background cascading deletion

1. [Create a sample Deployment](/docs/tasks/run-application/run-stateless-application-deployment/#creating-and-exploring-an-nginx-deployment).
2. Use either `kubectl` or the Kubernetes API to delete the Deployment,
   depending on the Kubernetes version your cluster runs.

   To check the version, enter `kubectl version`.

You can delete objects using background cascading deletion using `kubectl`
or the Kubernetes API.

Kubernetes uses background cascading deletion by default, and does so
even if you run the following commands without the `--cascade` flag or the
`propagationPolicy` argument.

**Using kubectl**

Run the following command:

```
kubectl delete deployment nginx-deployment --cascade=background
```

**Using the Kubernetes API**

1. Start a local proxy session:

   ```
   kubectl proxy --port=8080
   ```
2. Use `curl` to trigger deletion:

   ```
   curl -X DELETE localhost:8080/apis/apps/v1/namespaces/default/deployments/nginx-deployment \
       -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Background"}' \
       -H "Content-Type: application/json"
   ```

   The output is similar to this:

   ```
   "kind": "Status",
   "apiVersion": "v1",
   ...
   "status": "Success",
   "details": {
       "name": "nginx-deployment",
       "group": "apps",
       "kind": "deployments",
       "uid": "cc9eefb9-2d49-4445-b1c1-d261c9396456"
   }
   ```

## Delete owner objects and orphan dependents

By default, when you tell Kubernetes to delete an object, the
[controller](/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") also deletes
dependent objects. You can make Kubernetes *orphan* these dependents using
`kubectl` or the Kubernetes API, depending on the Kubernetes version your
cluster runs.

To check the version, enter `kubectl version`.

**Using kubectl**

Run the following command:

```
kubectl delete deployment nginx-deployment --cascade=orphan
```

**Using the Kubernetes API**

1. Start a local proxy session:

   ```
   kubectl proxy --port=8080
   ```
2. Use `curl` to trigger deletion:

   ```
   curl -X DELETE localhost:8080/apis/apps/v1/namespaces/default/deployments/nginx-deployment \
       -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Orphan"}' \
       -H "Content-Type: application/json"
   ```

   The output contains `orphan` in the `finalizers` field, similar to this:

   ```
   "kind": "Deployment",
   "apiVersion": "apps/v1",
   "namespace": "default",
   "uid": "6f577034-42a0-479d-be21-78018c466f1f",
   "creationTimestamp": "2021-07-09T16:46:37Z",
   "deletionTimestamp": "2021-07-09T16:47:08Z",
   "deletionGracePeriodSeconds": 0,
   "finalizers": [
     "orphan"
   ],
   ...
   ```

You can check that the Pods managed by the Deployment are still running:

```
kubectl get pods -l app=nginx
```

## What's next

* Learn about [owners and dependents](/docs/concepts/overview/working-with-objects/owners-dependents/) in Kubernetes.
* Learn about Kubernetes [finalizers](/docs/concepts/overview/working-with-objects/finalizers/).
* Learn about [garbage collection](/docs/concepts/architecture/garbage-collection/).

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
