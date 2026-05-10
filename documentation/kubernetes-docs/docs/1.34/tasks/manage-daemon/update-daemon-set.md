# Perform a Rolling Update on a DaemonSet

This page shows how to perform a rolling update on a DaemonSet.

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

## DaemonSet Update Strategy

DaemonSet has two update strategy types:

* `OnDelete`: With `OnDelete` update strategy, after you update a DaemonSet template, new
  DaemonSet pods will *only* be created when you manually delete old DaemonSet
  pods. This is the same behavior of DaemonSet in Kubernetes version 1.5 or
  before.
* `RollingUpdate`: This is the default update strategy.
  With `RollingUpdate` update strategy, after you update a
  DaemonSet template, old DaemonSet pods will be killed, and new DaemonSet pods
  will be created automatically, in a controlled fashion. At most one pod of
  the DaemonSet will be running on each node during the whole update process.

## Performing a Rolling Update

To enable the rolling update feature of a DaemonSet, you must set its
`.spec.updateStrategy.type` to `RollingUpdate`.

You may want to set
[`.spec.updateStrategy.rollingUpdate.maxUnavailable`](/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSetSpec)
(default to 1),
[`.spec.minReadySeconds`](/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSetSpec)
(default to 0) and
[`.spec.updateStrategy.rollingUpdate.maxSurge`](/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSetSpec)
(defaults to 0) as well.

### Creating a DaemonSet with `RollingUpdate` update strategy

This YAML file specifies a DaemonSet with an update strategy as 'RollingUpdate'

[`controllers/fluentd-daemonset.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/controllers/fluentd-daemonset.yaml)![](/images/copycode.svg "Copy controllers/fluentd-daemonset.yaml to clipboard")

```
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd-elasticsearch
  namespace: kube-system
  labels:
    k8s-app: fluentd-logging
spec:
  selector:
    matchLabels:
      name: fluentd-elasticsearch
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
  template:
    metadata:
      labels:
        name: fluentd-elasticsearch
    spec:
      tolerations:
      # these tolerations are to have the daemonset runnable on control plane nodes
      # remove them if your control plane nodes should not run pods
      - key: node-role.kubernetes.io/control-plane
        operator: Exists
        effect: NoSchedule
      - key: node-role.kubernetes.io/master
        operator: Exists
        effect: NoSchedule
      containers:
      - name: fluentd-elasticsearch
        image: quay.io/fluentd_elasticsearch/fluentd:v5.0.1
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
      terminationGracePeriodSeconds: 30
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers
```

After verifying the update strategy of the DaemonSet manifest, create the DaemonSet:

```
kubectl create -f https://k8s.io/examples/controllers/fluentd-daemonset.yaml
```

Alternatively, use `kubectl apply` to create the same DaemonSet if you plan to
update the DaemonSet with `kubectl apply`.

```
kubectl apply -f https://k8s.io/examples/controllers/fluentd-daemonset.yaml
```

### Checking DaemonSet `RollingUpdate` update strategy

Check the update strategy of your DaemonSet, and make sure it's set to
`RollingUpdate`:

```
kubectl get ds/fluentd-elasticsearch -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}' -n kube-system
```

If you haven't created the DaemonSet in the system, check your DaemonSet
manifest with the following command instead:

```
kubectl apply -f https://k8s.io/examples/controllers/fluentd-daemonset.yaml --dry-run=client -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
```

The output from both commands should be:

```
RollingUpdate
```

If the output isn't `RollingUpdate`, go back and modify the DaemonSet object or
manifest accordingly.

### Updating a DaemonSet template

Any updates to a `RollingUpdate` DaemonSet `.spec.template` will trigger a rolling
update. Let's update the DaemonSet by applying a new YAML file. This can be done with several different `kubectl` commands.

[`controllers/fluentd-daemonset-update.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/controllers/fluentd-daemonset-update.yaml)![](/images/copycode.svg "Copy controllers/fluentd-daemonset-update.yaml to clipboard")

```
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd-elasticsearch
  namespace: kube-system
  labels:
    k8s-app: fluentd-logging
spec:
  selector:
    matchLabels:
      name: fluentd-elasticsearch
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
  template:
    metadata:
      labels:
        name: fluentd-elasticsearch
    spec:
      tolerations:
      # these tolerations are to have the daemonset runnable on control plane nodes
      # remove them if your control plane nodes should not run pods
      - key: node-role.kubernetes.io/control-plane
        operator: Exists
        effect: NoSchedule
      - key: node-role.kubernetes.io/master
        operator: Exists
        effect: NoSchedule
      containers:
      - name: fluentd-elasticsearch
        image: quay.io/fluentd_elasticsearch/fluentd:v5.0.1
        resources:
          limits:
            memory: 200Mi
          requests:
            cpu: 100m
            memory: 200Mi
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
      terminationGracePeriodSeconds: 30
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers
```

#### Declarative commands

If you update DaemonSets using
[configuration files](/docs/tasks/manage-kubernetes-objects/declarative-config/),
use `kubectl apply`:

```
kubectl apply -f https://k8s.io/examples/controllers/fluentd-daemonset-update.yaml
```

#### Imperative commands

If you update DaemonSets using
[imperative commands](/docs/tasks/manage-kubernetes-objects/imperative-command/),
use `kubectl edit` :

```
kubectl edit ds/fluentd-elasticsearch -n kube-system
```

##### Updating only the container image

If you only need to update the container image in the DaemonSet template, i.e.
`.spec.template.spec.containers[*].image`, use `kubectl set image`:

```
kubectl set image ds/fluentd-elasticsearch fluentd-elasticsearch=quay.io/fluentd_elasticsearch/fluentd:v2.6.0 -n kube-system
```

### Watching the rolling update status

Finally, watch the rollout status of the latest DaemonSet rolling update:

```
kubectl rollout status ds/fluentd-elasticsearch -n kube-system
```

When the rollout is complete, the output is similar to this:

```
daemonset "fluentd-elasticsearch" successfully rolled out
```

## Troubleshooting

### DaemonSet rolling update is stuck

Sometimes, a DaemonSet rolling update may be stuck. Here are some possible
causes:

#### Some nodes run out of resources

The rollout is stuck because new DaemonSet pods can't be scheduled on at least one
node. This is possible when the node is
[running out of resources](/docs/concepts/scheduling-eviction/node-pressure-eviction/).

When this happens, find the nodes that don't have the DaemonSet pods scheduled on
by comparing the output of `kubectl get nodes` and the output of:

```
kubectl get pods -l name=fluentd-elasticsearch -o wide -n kube-system
```

Once you've found those nodes, delete some non-DaemonSet pods from the node to
make room for new DaemonSet pods.

> **Note:**
> This will cause service disruption when deleted pods are not controlled by any controllers or pods are not
> replicated. This does not respect [PodDisruptionBudget](/docs/tasks/run-application/configure-pdb/)
> either.

#### Broken rollout

If the recent DaemonSet template update is broken, for example, the container is
crash looping, or the container image doesn't exist (often due to a typo),
DaemonSet rollout won't progress.

To fix this, update the DaemonSet template again. New rollout won't be
blocked by previous unhealthy rollouts.

#### Clock skew

If `.spec.minReadySeconds` is specified in the DaemonSet, clock skew between
master and nodes will make DaemonSet unable to detect the right rollout
progress.

## Clean up

Delete DaemonSet from a namespace :

```
kubectl delete ds fluentd-elasticsearch -n kube-system
```

## What's next

* See [Performing a rollback on a DaemonSet](/docs/tasks/manage-daemon/rollback-daemon-set/)
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
