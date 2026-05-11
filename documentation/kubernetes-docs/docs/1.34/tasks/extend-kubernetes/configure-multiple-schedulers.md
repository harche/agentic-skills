# Configure Multiple Schedulers

Kubernetes ships with a default scheduler that is described
[here](/docs/reference/command-line-tools-reference/kube-scheduler/).
If the default scheduler does not suit your needs you can implement your own scheduler.
Moreover, you can even run multiple schedulers simultaneously alongside the default
scheduler and instruct Kubernetes what scheduler to use for each of your pods. Let's
learn how to run multiple schedulers in Kubernetes with an example.

A detailed description of how to implement a scheduler is outside the scope of this
document. Please refer to the kube-scheduler implementation in
[pkg/scheduler](https://github.com/kubernetes/kubernetes/tree/master/pkg/scheduler)
in the Kubernetes source directory for a canonical example.

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

To check the version, enter `kubectl version`.

## Package the scheduler

Package your scheduler binary into a container image. For the purposes of this example,
you can use the default scheduler (kube-scheduler) as your second scheduler.
Clone the [Kubernetes source code from GitHub](https://github.com/kubernetes/kubernetes)
and build the source.

```
git clone https://github.com/kubernetes/kubernetes.git
cd kubernetes
make
```

Create a container image containing the kube-scheduler binary. Here is the `Dockerfile`
to build the image:

```
FROM busybox
ADD ./_output/local/bin/linux/amd64/kube-scheduler /usr/local/bin/kube-scheduler
```

Save the file as `Dockerfile`, build the image and push it to a registry. This example
pushes the image to
[Google Container Registry (GCR)](https://cloud.google.com/container-registry/).
For more details, please read the GCR
[documentation](https://cloud.google.com/container-registry/docs/). Alternatively
you can also use the [docker hub](https://hub.docker.com/search?q=). For more details
refer to the docker hub [documentation](https://docs.docker.com/docker-hub/repos/create/#create-a-repository).

```
docker build -t gcr.io/my-gcp-project/my-kube-scheduler:1.0 .     # The image name and the repository
gcloud docker -- push gcr.io/my-gcp-project/my-kube-scheduler:1.0 # used in here is just an example
```

## Define a Kubernetes Deployment for the scheduler

Now that you have your scheduler in a container image, create a pod
configuration for it and run it in your Kubernetes cluster. But instead of creating a pod
directly in the cluster, you can use a [Deployment](/docs/concepts/workloads/controllers/deployment/)
for this example. A [Deployment](/docs/concepts/workloads/controllers/deployment/) manages a
[Replica Set](/docs/concepts/workloads/controllers/replicaset/) which in turn manages the pods,
thereby making the scheduler resilient to failures. Here is the deployment
config. Save it as `my-scheduler.yaml`:

[`admin/sched/my-scheduler.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/admin/sched/my-scheduler.yaml)![](/images/copycode.svg "Copy admin/sched/my-scheduler.yaml to clipboard")

```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-scheduler
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: my-scheduler-as-kube-scheduler
subjects:
- kind: ServiceAccount
  name: my-scheduler
  namespace: kube-system
roleRef:
  kind: ClusterRole
  name: system:kube-scheduler
  apiGroup: rbac.authorization.k8s.io
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: my-scheduler-as-volume-scheduler
subjects:
- kind: ServiceAccount
  name: my-scheduler
  namespace: kube-system
roleRef:
  kind: ClusterRole
  name: system:volume-scheduler
  apiGroup: rbac.authorization.k8s.io
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: my-scheduler-extension-apiserver-authentication-reader
  namespace: kube-system
roleRef:
  kind: Role
  name: extension-apiserver-authentication-reader
  apiGroup: rbac.authorization.k8s.io
subjects:
- kind: ServiceAccount
  name: my-scheduler
  namespace: kube-system
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-scheduler-config
  namespace: kube-system
data:
  my-scheduler-config.yaml: |
    apiVersion: kubescheduler.config.k8s.io/v1
    kind: KubeSchedulerConfiguration
    profiles:
      - schedulerName: my-scheduler
    leaderElection:
      leaderElect: false
---
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    component: scheduler
    tier: control-plane
  name: my-scheduler
  namespace: kube-system
spec:
  selector:
    matchLabels:
      component: scheduler
      tier: control-plane
  replicas: 1
  template:
    metadata:
      labels:
        component: scheduler
        tier: control-plane
        version: second
    spec:
      serviceAccountName: my-scheduler
      containers:
      - command:
        - /usr/local/bin/kube-scheduler
        - --config=/etc/kubernetes/my-scheduler/my-scheduler-config.yaml
        image: gcr.io/my-gcp-project/my-kube-scheduler:1.0
        livenessProbe:
          httpGet:
            path: /healthz
            port: 10259
            scheme: HTTPS
          initialDelaySeconds: 15
        name: kube-second-scheduler
        readinessProbe:
          httpGet:
            path: /healthz
            port: 10259
            scheme: HTTPS
        resources:
          requests:
            cpu: '0.1'
        securityContext:
          privileged: false
        volumeMounts:
          - name: config-volume
            mountPath: /etc/kubernetes/my-scheduler
      hostNetwork: false
      hostPID: false
      volumes:
        - name: config-volume
          configMap:
            name: my-scheduler-config
```

In the above manifest, you use a [KubeSchedulerConfiguration](/docs/reference/scheduling/config/)
to customize the behavior of your scheduler implementation. This configuration has been passed to
the `kube-scheduler` during initialization with the `--config` option. The `my-scheduler-config` ConfigMap stores the configuration file. The Pod of the`my-scheduler` Deployment mounts the `my-scheduler-config` ConfigMap as a volume.

In the aforementioned Scheduler Configuration, your scheduler implementation is represented via
a [KubeSchedulerProfile](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-KubeSchedulerProfile).

> **Note:**
> To determine if a scheduler is responsible for scheduling a specific Pod, the `spec.schedulerName` field in a
> PodTemplate or Pod manifest must match the `schedulerName` field of the `KubeSchedulerProfile`.
> All schedulers running in the cluster must have unique names.

Also, note that you create a dedicated service account `my-scheduler` and bind the ClusterRole
`system:kube-scheduler` to it so that it can acquire the same privileges as `kube-scheduler`.

Please see the
[kube-scheduler documentation](/docs/reference/command-line-tools-reference/kube-scheduler/) for
detailed description of other command line arguments and
[Scheduler Configuration reference](/docs/reference/config-api/kube-scheduler-config.v1/) for
detailed description of other customizable `kube-scheduler` configurations.

## Run the second scheduler in the cluster

In order to run your scheduler in a Kubernetes cluster, create the deployment
specified in the config above in a Kubernetes cluster:

```
kubectl create -f my-scheduler.yaml
```

Verify that the scheduler pod is running:

```
kubectl get pods --namespace=kube-system
```

```
NAME                                           READY     STATUS    RESTARTS   AGE
....
my-scheduler-lnf4s-4744f                       1/1       Running   0          2m
...
```

You should see a "Running" my-scheduler pod, in addition to the default kube-scheduler
pod in this list.

### Enable leader election

To run multiple-scheduler with leader election enabled, you must do the following:

Update the following fields for the KubeSchedulerConfiguration in the `my-scheduler-config` ConfigMap in your YAML file:

* `leaderElection.leaderElect` to `true`
* `leaderElection.resourceNamespace` to `<lock-object-namespace>`
* `leaderElection.resourceName` to `<lock-object-name>`

> **Note:**
> The control plane creates the lock objects for you, but the namespace must already exist.
> You can use the `kube-system` namespace.

If RBAC is enabled on your cluster, you must update the `system:kube-scheduler` cluster role.
Add your scheduler name to the resourceNames of the rule applied for `endpoints` and `leases` resources, as in the following example:

```
kubectl edit clusterrole system:kube-scheduler
```

[`admin/sched/clusterrole.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/admin/sched/clusterrole.yaml)![](/images/copycode.svg "Copy admin/sched/clusterrole.yaml to clipboard")

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: "true"
  labels:
    kubernetes.io/bootstrapping: rbac-defaults
  name: system:kube-scheduler
rules:
  - apiGroups:
      - coordination.k8s.io
    resources:
      - leases
    verbs:
      - create
  - apiGroups:
      - coordination.k8s.io
    resourceNames:
      - kube-scheduler
      - my-scheduler
    resources:
      - leases
    verbs:
      - get
      - update
  - apiGroups:
      - ""
    resourceNames:
      - kube-scheduler
      - my-scheduler
    resources:
      - endpoints
    verbs:
      - delete
      - get
      - patch
      - update
```

## Specify schedulers for pods

Now that your second scheduler is running, create some pods, and direct them
to be scheduled by either the default scheduler or the one you deployed.
In order to schedule a given pod using a specific scheduler, specify the name of the
scheduler in that pod spec. Let's look at three examples.

* Pod spec without any scheduler name

  [`admin/sched/pod1.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/admin/sched/pod1.yaml)![](/images/copycode.svg "Copy admin/sched/pod1.yaml to clipboard")

  ```
  apiVersion: v1
  kind: Pod
  metadata:
    name: no-annotation
    labels:
      name: multischeduler-example
  spec:
    containers:
    - name: pod-with-no-annotation-container
      image: registry.k8s.io/pause:3.8
  ```

  When no scheduler name is supplied, the pod is automatically scheduled using the
  default-scheduler.

  Save this file as `pod1.yaml` and submit it to the Kubernetes cluster.

  ```
  kubectl create -f pod1.yaml
  ```
* Pod spec with `default-scheduler`

  [`admin/sched/pod2.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/admin/sched/pod2.yaml)![](/images/copycode.svg "Copy admin/sched/pod2.yaml to clipboard")

  ```
  apiVersion: v1
  kind: Pod
  metadata:
    name: annotation-default-scheduler
    labels:
      name: multischeduler-example
  spec:
    schedulerName: default-scheduler
    containers:
    - name: pod-with-default-annotation-container
      image: registry.k8s.io/pause:3.8
  ```

  A scheduler is specified by supplying the scheduler name as a value to `spec.schedulerName`. In this case, we supply the name of the
  default scheduler which is `default-scheduler`.

  Save this file as `pod2.yaml` and submit it to the Kubernetes cluster.

  ```
  kubectl create -f pod2.yaml
  ```
* Pod spec with `my-scheduler`

  [`admin/sched/pod3.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/admin/sched/pod3.yaml)![](/images/copycode.svg "Copy admin/sched/pod3.yaml to clipboard")

  ```
  apiVersion: v1
  kind: Pod
  metadata:
    name: annotation-second-scheduler
    labels:
      name: multischeduler-example
  spec:
    schedulerName: my-scheduler
    containers:
    - name: pod-with-second-annotation-container
      image: registry.k8s.io/pause:3.8
  ```

  In this case, we specify that this pod should be scheduled using the scheduler that we
  deployed - `my-scheduler`. Note that the value of `spec.schedulerName` should match the name supplied for the scheduler
  in the `schedulerName` field of the mapping `KubeSchedulerProfile`.

  Save this file as `pod3.yaml` and submit it to the Kubernetes cluster.

  ```
  kubectl create -f pod3.yaml
  ```

  Verify that all three pods are running.

  ```
  kubectl get pods
  ```

### Verifying that the pods were scheduled using the desired schedulers

In order to make it easier to work through these examples, we did not verify that the
pods were actually scheduled using the desired schedulers. We can verify that by
changing the order of pod and deployment config submissions above. If we submit all the
pod configs to a Kubernetes cluster before submitting the scheduler deployment config,
we see that the pod `annotation-second-scheduler` remains in "Pending" state forever
while the other two pods get scheduled. Once we submit the scheduler deployment config
and our new scheduler starts running, the `annotation-second-scheduler` pod gets
scheduled as well.

Alternatively, you can look at the "Scheduled" entries in the event logs to
verify that the pods were scheduled by the desired schedulers.

```
kubectl get events
```

You can also use a [custom scheduler configuration](/docs/reference/scheduling/config/#multiple-profiles)
or a custom container image for the cluster's main scheduler by modifying its static pod manifest
on the relevant control plane nodes.

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
