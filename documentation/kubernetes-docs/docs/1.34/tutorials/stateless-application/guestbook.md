# Example: Deploying PHP Guestbook application with Redis

This tutorial shows you how to build and deploy a simple *(not production
ready)*, multi-tier web application using Kubernetes and
[Docker](https://www.docker.com/). This example consists of the following
components:

* A single-instance [Redis](https://www.redis.io/) to store guestbook entries
* Multiple web frontend instances

## Objectives

* Start up a Redis leader.
* Start up two Redis followers.
* Start up the guestbook frontend.
* Expose and view the Frontend Service.
* Clean up.

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

Your Kubernetes server must be at or later than version v1.14.

To check the version, enter `kubectl version`.

## Start up the Redis Database

The guestbook application uses Redis to store its data.

### Creating the Redis Deployment

The manifest file, included below, specifies a Deployment controller that runs a single replica Redis Pod.

[`application/guestbook/redis-leader-deployment.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/application/guestbook/redis-leader-deployment.yaml)![](/images/copycode.svg "Copy application/guestbook/redis-leader-deployment.yaml to clipboard")

```
# SOURCE: https://cloud.google.com/kubernetes-engine/docs/tutorials/guestbook
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis-leader
  labels:
    app: redis
    role: leader
    tier: backend
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
        role: leader
        tier: backend
    spec:
      containers:
      - name: leader
        image: "docker.io/redis:6.0.5"
        resources:
          requests:
            cpu: 100m
            memory: 100Mi
        ports:
        - containerPort: 6379
```

1. Launch a terminal window in the directory you downloaded the manifest files.
2. Apply the Redis Deployment from the `redis-leader-deployment.yaml` file:

   ```
   kubectl apply -f https://k8s.io/examples/application/guestbook/redis-leader-deployment.yaml
   ```
3. Query the list of Pods to verify that the Redis Pod is running:

   ```
   kubectl get pods
   ```

   The response should be similar to this:

   ```
   NAME                           READY   STATUS    RESTARTS   AGE
   redis-leader-fb76b4755-xjr2n   1/1     Running   0          13s
   ```
4. Run the following command to view the logs from the Redis leader Pod:

   ```
   kubectl logs -f deployment/redis-leader
   ```

### Creating the Redis leader Service

The guestbook application needs to communicate to the Redis to write its data.
You need to apply a [Service](/docs/concepts/services-networking/service/) to
proxy the traffic to the Redis Pod. A Service defines a policy to access the
Pods.

[`application/guestbook/redis-leader-service.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/application/guestbook/redis-leader-service.yaml)![](/images/copycode.svg "Copy application/guestbook/redis-leader-service.yaml to clipboard")

```
# SOURCE: https://cloud.google.com/kubernetes-engine/docs/tutorials/guestbook
apiVersion: v1
kind: Service
metadata:
  name: redis-leader
  labels:
    app: redis
    role: leader
    tier: backend
spec:
  ports:
  - port: 6379
    targetPort: 6379
  selector:
    app: redis
    role: leader
    tier: backend
```

1. Apply the Redis Service from the following `redis-leader-service.yaml` file:

   ```
   kubectl apply -f https://k8s.io/examples/application/guestbook/redis-leader-service.yaml
   ```
2. Query the list of Services to verify that the Redis Service is running:

   ```
   kubectl get service
   ```

   The response should be similar to this:

   ```
   NAME           TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
   kubernetes     ClusterIP   10.0.0.1     <none>        443/TCP    1m
   redis-leader   ClusterIP   10.103.78.24 <none>        6379/TCP   16s
   ```

> **Note:**
> This manifest file creates a Service named `redis-leader` with a set of labels
> that match the labels previously defined, so the Service routes network
> traffic to the Redis Pod.

### Set up Redis followers

Although the Redis leader is a single Pod, you can make it highly available
and meet traffic demands by adding a few Redis followers, or replicas.

[`application/guestbook/redis-follower-deployment.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/application/guestbook/redis-follower-deployment.yaml)![](/images/copycode.svg "Copy application/guestbook/redis-follower-deployment.yaml to clipboard")

```
# SOURCE: https://cloud.google.com/kubernetes-engine/docs/tutorials/guestbook
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis-follower
  labels:
    app: redis
    role: follower
    tier: backend
spec:
  replicas: 2
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
        role: follower
        tier: backend
    spec:
      containers:
      - name: follower
        image: us-docker.pkg.dev/google-samples/containers/gke/gb-redis-follower:v2
        resources:
          requests:
            cpu: 100m
            memory: 100Mi
        ports:
        - containerPort: 6379
```

1. Apply the Redis Deployment from the following `redis-follower-deployment.yaml` file:

   ```
   kubectl apply -f https://k8s.io/examples/application/guestbook/redis-follower-deployment.yaml
   ```
2. Verify that the two Redis follower replicas are running by querying the list of Pods:

   ```
   kubectl get pods
   ```

   The response should be similar to this:

   ```
   NAME                             READY   STATUS    RESTARTS   AGE
   redis-follower-dddfbdcc9-82sfr   1/1     Running   0          37s
   redis-follower-dddfbdcc9-qrt5k   1/1     Running   0          38s
   redis-leader-fb76b4755-xjr2n     1/1     Running   0          11m
   ```

### Creating the Redis follower service

The guestbook application needs to communicate with the Redis followers to
read data. To make the Redis followers discoverable, you must set up another
[Service](/docs/concepts/services-networking/service/).

[`application/guestbook/redis-follower-service.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/application/guestbook/redis-follower-service.yaml)![](/images/copycode.svg "Copy application/guestbook/redis-follower-service.yaml to clipboard")

```
# SOURCE: https://cloud.google.com/kubernetes-engine/docs/tutorials/guestbook
apiVersion: v1
kind: Service
metadata:
  name: redis-follower
  labels:
    app: redis
    role: follower
    tier: backend
spec:
  ports:
    # the port that this service should serve on
  - port: 6379
  selector:
    app: redis
    role: follower
    tier: backend
```

1. Apply the Redis Service from the following `redis-follower-service.yaml` file:

   ```
   kubectl apply -f https://k8s.io/examples/application/guestbook/redis-follower-service.yaml
   ```
2. Query the list of Services to verify that the Redis Service is running:

   ```
   kubectl get service
   ```

   The response should be similar to this:

   ```
   NAME             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
   kubernetes       ClusterIP   10.96.0.1       <none>        443/TCP    3d19h
   redis-follower   ClusterIP   10.110.162.42   <none>        6379/TCP   9s
   redis-leader     ClusterIP   10.103.78.24    <none>        6379/TCP   6m10s
   ```

> **Note:**
> This manifest file creates a Service named `redis-follower` with a set of
> labels that match the labels previously defined, so the Service routes network
> traffic to the Redis Pod.

## Set up and Expose the Guestbook Frontend

Now that you have the Redis storage of your guestbook up and running, start
the guestbook web servers. Like the Redis followers, the frontend is deployed
using a Kubernetes Deployment.

The guestbook app uses a PHP frontend. It is configured to communicate with
either the Redis follower or leader Services, depending on whether the request
is a read or a write. The frontend exposes a JSON interface, and serves a
jQuery-Ajax-based UX.

### Creating the Guestbook Frontend Deployment

[`application/guestbook/frontend-deployment.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/application/guestbook/frontend-deployment.yaml)![](/images/copycode.svg "Copy application/guestbook/frontend-deployment.yaml to clipboard")

```
# SOURCE: https://cloud.google.com/kubernetes-engine/docs/tutorials/guestbook
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
spec:
  replicas: 3
  selector:
    matchLabels:
        app: guestbook
        tier: frontend
  template:
    metadata:
      labels:
        app: guestbook
        tier: frontend
    spec:
      containers:
      - name: php-redis
        image: us-docker.pkg.dev/google-samples/containers/gke/gb-frontend:v5
        env:
        - name: GET_HOSTS_FROM
          value: "dns"
        resources:
          requests:
            cpu: 100m
            memory: 100Mi
        ports:
        - containerPort: 80
```

1. Apply the frontend Deployment from the `frontend-deployment.yaml` file:

   ```
   kubectl apply -f https://k8s.io/examples/application/guestbook/frontend-deployment.yaml
   ```
2. Query the list of Pods to verify that the three frontend replicas are running:

   ```
   kubectl get pods -l app=guestbook -l tier=frontend
   ```

   The response should be similar to this:

   ```
   NAME                        READY   STATUS    RESTARTS   AGE
   frontend-85595f5bf9-5tqhb   1/1     Running   0          47s
   frontend-85595f5bf9-qbzwm   1/1     Running   0          47s
   frontend-85595f5bf9-zchwc   1/1     Running   0          47s
   ```

### Creating the Frontend Service

The `Redis` Services you applied is only accessible within the Kubernetes
cluster because the default type for a Service is
[ClusterIP](/docs/concepts/services-networking/service/#publishing-services-service-types).
`ClusterIP` provides a single IP address for the set of Pods the Service is
pointing to. This IP address is accessible only within the cluster.

If you want guests to be able to access your guestbook, you must configure the
frontend Service to be externally visible, so a client can request the Service
from outside the Kubernetes cluster. However a Kubernetes user can use
`kubectl port-forward` to access the service even though it uses a
`ClusterIP`.

> **Note:**
> Some cloud providers, like Google Compute Engine or Google Kubernetes Engine,
> support external load balancers. If your cloud provider supports load
> balancers and you want to use it, uncomment `type: LoadBalancer`.

[`application/guestbook/frontend-service.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/application/guestbook/frontend-service.yaml)![](/images/copycode.svg "Copy application/guestbook/frontend-service.yaml to clipboard")

```
# SOURCE: https://cloud.google.com/kubernetes-engine/docs/tutorials/guestbook
apiVersion: v1
kind: Service
metadata:
  name: frontend
  labels:
    app: guestbook
    tier: frontend
spec:
  # if your cluster supports it, uncomment the following to automatically create
  # an external load-balanced IP for the frontend service.
  # type: LoadBalancer
  #type: LoadBalancer
  ports:
    # the port that this service should serve on
  - port: 80
  selector:
    app: guestbook
    tier: frontend
```

1. Apply the frontend Service from the `frontend-service.yaml` file:

   ```
   kubectl apply -f https://k8s.io/examples/application/guestbook/frontend-service.yaml
   ```
2. Query the list of Services to verify that the frontend Service is running:

   ```
   kubectl get services
   ```

   The response should be similar to this:

   ```
   NAME             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
   frontend         ClusterIP   10.97.28.230    <none>        80/TCP     19s
   kubernetes       ClusterIP   10.96.0.1       <none>        443/TCP    3d19h
   redis-follower   ClusterIP   10.110.162.42   <none>        6379/TCP   5m48s
   redis-leader     ClusterIP   10.103.78.24    <none>        6379/TCP   11m
   ```

### Viewing the Frontend Service via `kubectl port-forward`

1. Run the following command to forward port `8080` on your local machine to port `80` on the service.

   ```
   kubectl port-forward svc/frontend 8080:80
   ```

   The response should be similar to this:

   ```
   Forwarding from 127.0.0.1:8080 -> 80
   Forwarding from [::1]:8080 -> 80
   ```
2. load the page <http://localhost:8080> in your browser to view your guestbook.

### Viewing the Frontend Service via `LoadBalancer`

If you deployed the `frontend-service.yaml` manifest with type: `LoadBalancer`
you need to find the IP address to view your Guestbook.

1. Run the following command to get the IP address for the frontend Service.

   ```
   kubectl get service frontend
   ```

   The response should be similar to this:

   ```
   NAME       TYPE           CLUSTER-IP      EXTERNAL-IP        PORT(S)        AGE
   frontend   LoadBalancer   10.51.242.136   109.197.92.229     80:32372/TCP   1m
   ```
2. Copy the external IP address, and load the page in your browser to view your guestbook.

> **Note:**
> Try adding some guestbook entries by typing in a message, and clicking Submit.
> The message you typed appears in the frontend. This message indicates that
> data is successfully added to Redis through the Services you created earlier.

## Scale the Web Frontend

You can scale up or down as needed because your servers are defined as a
Service that uses a Deployment controller.

1. Run the following command to scale up the number of frontend Pods:

   ```
   kubectl scale deployment frontend --replicas=5
   ```
2. Query the list of Pods to verify the number of frontend Pods running:

   ```
   kubectl get pods
   ```

   The response should look similar to this:

   ```
   NAME                             READY   STATUS    RESTARTS   AGE
   frontend-85595f5bf9-5df5m        1/1     Running   0          83s
   frontend-85595f5bf9-7zmg5        1/1     Running   0          83s
   frontend-85595f5bf9-cpskg        1/1     Running   0          15m
   frontend-85595f5bf9-l2l54        1/1     Running   0          14m
   frontend-85595f5bf9-l9c8z        1/1     Running   0          14m
   redis-follower-dddfbdcc9-82sfr   1/1     Running   0          97m
   redis-follower-dddfbdcc9-qrt5k   1/1     Running   0          97m
   redis-leader-fb76b4755-xjr2n     1/1     Running   0          108m
   ```
3. Run the following command to scale down the number of frontend Pods:

   ```
   kubectl scale deployment frontend --replicas=2
   ```
4. Query the list of Pods to verify the number of frontend Pods running:

   ```
   kubectl get pods
   ```

   The response should look similar to this:

   ```
   NAME                             READY   STATUS    RESTARTS   AGE
   frontend-85595f5bf9-cpskg        1/1     Running   0          16m
   frontend-85595f5bf9-l9c8z        1/1     Running   0          15m
   redis-follower-dddfbdcc9-82sfr   1/1     Running   0          98m
   redis-follower-dddfbdcc9-qrt5k   1/1     Running   0          98m
   redis-leader-fb76b4755-xjr2n     1/1     Running   0          109m
   ```

## Cleaning up

Deleting the Deployments and Services also deletes any running Pods. Use
labels to delete multiple resources with one command.

1. Run the following commands to delete all Pods, Deployments, and Services.

   ```
   kubectl delete deployment -l app=redis
   kubectl delete service -l app=redis
   kubectl delete deployment frontend
   kubectl delete service frontend
   ```

   The response should look similar to this:

   ```
   deployment.apps "redis-follower" deleted
   deployment.apps "redis-leader" deleted
   deployment.apps "frontend" deleted
   service "frontend" deleted
   ```
2. Query the list of Pods to verify that no Pods are running:

   ```
   kubectl get pods
   ```

   The response should look similar to this:

   ```
   No resources found in default namespace.
   ```

## What's next

* Complete the [Kubernetes Basics](/docs/tutorials/kubernetes-basics/) Interactive Tutorials
* Use Kubernetes to create a blog using [Persistent Volumes for MySQL and Wordpress](/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/#visit-your-new-wordpress-blog)
* Read more about [connecting applications with services](/docs/tutorials/services/connect-applications-service/)
* Read more about [using labels effectively](/docs/concepts/overview/working-with-objects/labels/#using-labels-effectively)

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
