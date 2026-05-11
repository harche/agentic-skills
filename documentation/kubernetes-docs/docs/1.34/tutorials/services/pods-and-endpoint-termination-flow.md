# Explore Termination Behavior for Pods And Their Endpoints

Once you connected your Application with Service following steps
like those outlined in [Connecting Applications with Services](/docs/tutorials/services/connect-applications-service/),
you have a continuously running, replicated application, that is exposed on a network.
This tutorial helps you look at the termination flow for Pods and to explore ways to implement
graceful connection draining.

## Termination process for Pods and their endpoints

There are often cases when you need to terminate a Pod - be it to upgrade or scale down.
In order to improve application availability, it may be important to implement
a proper active connections draining.

This tutorial explains the flow of Pod termination in connection with the
corresponding endpoint state and removal by using
a simple nginx web server to demonstrate the concept.

## Example flow with endpoint termination

The following is the example flow described in the
[Termination of Pods](/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination)
document.

Let's say you have a Deployment containing a single `nginx` replica
(say just for the sake of demonstration purposes) and a Service:

[`service/pod-with-graceful-termination.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/service/pod-with-graceful-termination.yaml)![](/images/copycode.svg "Copy service/pod-with-graceful-termination.yaml to clipboard")

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      terminationGracePeriodSeconds: 120 # extra long grace period
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        lifecycle:
          preStop:
            exec:
              # Real life termination may take any time up to terminationGracePeriodSeconds.
              # In this example - just hang around for at least the duration of terminationGracePeriodSeconds,
              # at 120 seconds container will be forcibly terminated.
              # Note, all this time nginx will keep processing requests.
              command: [
                "/bin/sh", "-c", "sleep 180"
              ]
```

[`service/explore-graceful-termination-nginx.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/service/explore-graceful-termination-nginx.yaml)![](/images/copycode.svg "Copy service/explore-graceful-termination-nginx.yaml to clipboard")

```
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

Now create the Deployment Pod and Service using the above files:

```
kubectl apply -f pod-with-graceful-termination.yaml
kubectl apply -f explore-graceful-termination-nginx.yaml
```

Once the Pod and Service are running, you can get the name of any associated EndpointSlices:

```
kubectl get endpointslice
```

The output is similar to this:

```
NAME                  ADDRESSTYPE   PORTS   ENDPOINTS                 AGE
nginx-service-6tjbr   IPv4          80      10.12.1.199,10.12.1.201   22m
```

You can see its status, and validate that there is one endpoint registered:

```
kubectl get endpointslices -o json -l kubernetes.io/service-name=nginx-service
```

The output is similar to this:

```
{
    "addressType": "IPv4",
    "apiVersion": "discovery.k8s.io/v1",
    "endpoints": [
        {
            "addresses": [
                "10.12.1.201"
            ],
            "conditions": {
                "ready": true,
                "serving": true,
                "terminating": false
```

Now let's terminate the Pod and validate that the Pod is being terminated
respecting the graceful termination period configuration:

```
kubectl delete pod nginx-deployment-7768647bf9-b4b9s
```

All pods:

```
kubectl get pods
```

The output is similar to this:

```
NAME                                READY   STATUS        RESTARTS      AGE
nginx-deployment-7768647bf9-b4b9s   1/1     Terminating   0             4m1s
nginx-deployment-7768647bf9-rkxlw   1/1     Running       0             8s
```

You can see that the new pod got scheduled.

While the new endpoint is being created for the new Pod, the old endpoint is
still around in the terminating state:

```
kubectl get endpointslice -o json nginx-service-6tjbr
```

The output is similar to this:

```
{
    "addressType": "IPv4",
    "apiVersion": "discovery.k8s.io/v1",
    "endpoints": [
        {
            "addresses": [
                "10.12.1.201"
            ],
            "conditions": {
                "ready": false,
                "serving": true,
                "terminating": true
            },
            "nodeName": "gke-main-default-pool-dca1511c-d17b",
            "targetRef": {
                "kind": "Pod",
                "name": "nginx-deployment-7768647bf9-b4b9s",
                "namespace": "default",
                "uid": "66fa831c-7eb2-407f-bd2c-f96dfe841478"
            },
            "zone": "us-central1-c"
        },
        {
            "addresses": [
                "10.12.1.202"
            ],
            "conditions": {
                "ready": true,
                "serving": true,
                "terminating": false
            },
            "nodeName": "gke-main-default-pool-dca1511c-d17b",
            "targetRef": {
                "kind": "Pod",
                "name": "nginx-deployment-7768647bf9-rkxlw",
                "namespace": "default",
                "uid": "722b1cbe-dcd7-4ed4-8928-4a4d0e2bbe35"
            },
            "zone": "us-central1-c"
```

This allows applications to communicate their state during termination
and clients (such as load balancers) to implement connection draining functionality.
These clients may detect terminating endpoints and implement a special logic for them.

In Kubernetes, endpoints that are terminating always have their `ready` status set as `false`.
This needs to happen for backward
compatibility, so existing load balancers will not use it for regular traffic.
If traffic draining on terminating pod is needed, the actual readiness can be
checked as a condition `serving`.

When Pod is deleted, the old endpoint will also be deleted.

## What's next

* Learn how to [Connect Applications with Services](/docs/tutorials/services/connect-applications-service/)
* Learn more about [Using a Service to Access an Application in a Cluster](/docs/tasks/access-application-cluster/service-access-application-cluster/)
* Learn more about [Connecting a Front End to a Back End Using a Service](/docs/tasks/access-application-cluster/connecting-frontend-backend/)
* Learn more about [Creating an External Load Balancer](/docs/tasks/access-application-cluster/create-external-load-balancer/)

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
