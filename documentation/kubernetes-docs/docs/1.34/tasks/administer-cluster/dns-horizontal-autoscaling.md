# Autoscale the DNS Service in a Cluster

This page shows how to enable and configure autoscaling of the DNS service in
your Kubernetes cluster.

## Before you begin

* You need to have a Kubernetes cluster, and the kubectl command-line tool must
  be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
  cluster, you can create one by using
  [minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
  or you can use one of these Kubernetes playgrounds:

  + [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
  + [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
  + [KodeKloud](https://kodekloud.com/public-playgrounds)
  + [Play with Kubernetes](https://labs.play-with-k8s.com/)

  To check the version, enter `kubectl version`.
* This guide assumes your nodes use the AMD64 or Intel 64 CPU architecture.
* Make sure [Kubernetes DNS](/docs/concepts/services-networking/dns-pod-service/) is enabled.

## Determine whether DNS horizontal autoscaling is already enabled

List the [Deployments](/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster.")
in your cluster in the kube-system [namespace](/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster."):

```
kubectl get deployment --namespace=kube-system
```

The output is similar to this:

```
NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
...
kube-dns-autoscaler    1/1     1            1           ...
...
```

If you see "kube-dns-autoscaler" in the output, DNS horizontal autoscaling is
already enabled, and you can skip to
[Tuning autoscaling parameters](#tuning-autoscaling-parameters).

## Get the name of your DNS Deployment

List the DNS deployments in your cluster in the kube-system namespace:

```
kubectl get deployment -l k8s-app=kube-dns --namespace=kube-system
```

The output is similar to this:

```
NAME      READY   UP-TO-DATE   AVAILABLE   AGE
...
coredns   2/2     2            2           ...
...
```

If you don't see a Deployment for DNS services, you can also look for it by name:

```
kubectl get deployment --namespace=kube-system
```

and look for a deployment named `coredns` or `kube-dns`.

Your scale target is

```
Deployment/<your-deployment-name>
```

where `<your-deployment-name>` is the name of your DNS Deployment. For example, if
the name of your Deployment for DNS is coredns, your scale target is Deployment/coredns.

> **Note:**
> CoreDNS is the default DNS service for Kubernetes. CoreDNS sets the label
> `k8s-app=kube-dns` so that it can work in clusters that originally used
> kube-dns.

## Enable DNS horizontal autoscaling

In this section, you create a new Deployment. The Pods in the Deployment run a
container based on the `cluster-proportional-autoscaler-amd64` image.

Create a file named `dns-horizontal-autoscaler.yaml` with this content:

[`admin/dns/dns-horizontal-autoscaler.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/admin/dns/dns-horizontal-autoscaler.yaml)![](/images/copycode.svg "Copy admin/dns/dns-horizontal-autoscaler.yaml to clipboard")

```
kind: ServiceAccount
apiVersion: v1
metadata:
  name: kube-dns-autoscaler
  namespace: kube-system
---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: system:kube-dns-autoscaler
rules:
  - apiGroups: [""]
    resources: ["nodes"]
    verbs: ["list", "watch"]
  - apiGroups: [""]
    resources: ["replicationcontrollers/scale"]
    verbs: ["get", "update"]
  - apiGroups: ["apps"]
    resources: ["deployments/scale", "replicasets/scale"]
    verbs: ["get", "update"]
# Remove the configmaps rule once below issue is fixed:
# kubernetes-incubator/cluster-proportional-autoscaler#16
  - apiGroups: [""]
    resources: ["configmaps"]
    verbs: ["get", "create"]
---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: system:kube-dns-autoscaler
subjects:
  - kind: ServiceAccount
    name: kube-dns-autoscaler
    namespace: kube-system
roleRef:
  kind: ClusterRole
  name: system:kube-dns-autoscaler
  apiGroup: rbac.authorization.k8s.io

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kube-dns-autoscaler
  namespace: kube-system
  labels:
    k8s-app: kube-dns-autoscaler
    kubernetes.io/cluster-service: "true"
spec:
  selector:
    matchLabels:
      k8s-app: kube-dns-autoscaler
  template:
    metadata:
      labels:
        k8s-app: kube-dns-autoscaler
    spec:
      priorityClassName: system-cluster-critical
      securityContext:
        seccompProfile:
          type: RuntimeDefault
        supplementalGroups: [ 65534 ]
        fsGroup: 65534
      nodeSelector:
        kubernetes.io/os: linux
      containers:
      - name: autoscaler
        image: registry.k8s.io/cpa/cluster-proportional-autoscaler:1.8.4
        resources:
            requests:
                cpu: "20m"
                memory: "10Mi"
        command:
          - /cluster-proportional-autoscaler
          - --namespace=kube-system
          - --configmap=kube-dns-autoscaler
          # Should keep target in sync with cluster/addons/dns/kube-dns.yaml.base
          - --target=<SCALE_TARGET>
          # When cluster is using large nodes(with more cores), "coresPerReplica" should dominate.
          # If using small nodes, "nodesPerReplica" should dominate.
          - --default-params={"linear":{"coresPerReplica":256,"nodesPerReplica":16,"preventSinglePointFailure":true,"includeUnschedulableNodes":true}}
          - --logtostderr=true
          - --v=2
      tolerations:
      - key: "CriticalAddonsOnly"
        operator: "Exists"
      serviceAccountName: kube-dns-autoscaler
```

In the file, replace `<SCALE_TARGET>` with your scale target.

Go to the directory that contains your configuration file, and enter this
command to create the Deployment:

```
kubectl apply -f dns-horizontal-autoscaler.yaml
```

The output of a successful command is:

```
deployment.apps/kube-dns-autoscaler created
```

DNS horizontal autoscaling is now enabled.

## Tune DNS autoscaling parameters

Verify that the kube-dns-autoscaler [ConfigMap](/docs/concepts/configuration/configmap/ "An API object used to store non-confidential data in key-value pairs. Can be consumed as environment variables, command-line arguments, or configuration files in a volume.") exists:

```
kubectl get configmap --namespace=kube-system
```

The output is similar to this:

```
NAME                  DATA      AGE
...
kube-dns-autoscaler   1         ...
...
```

Modify the data in the ConfigMap:

```
kubectl edit configmap kube-dns-autoscaler --namespace=kube-system
```

Look for this line:

```
linear: '{"coresPerReplica":256,"min":1,"nodesPerReplica":16}'
```

Modify the fields according to your needs. The "min" field indicates the
minimal number of DNS backends. The actual number of backends is
calculated using this equation:

```
replicas = max( ceil( cores × 1/coresPerReplica ) , ceil( nodes × 1/nodesPerReplica ) )
```

Note that the values of both `coresPerReplica` and `nodesPerReplica` are
floats.

The idea is that when a cluster is using nodes that have many cores,
`coresPerReplica` dominates. When a cluster is using nodes that have fewer
cores, `nodesPerReplica` dominates.

There are other supported scaling patterns. For details, see
[cluster-proportional-autoscaler](https://github.com/kubernetes-sigs/cluster-proportional-autoscaler).

## Disable DNS horizontal autoscaling

There are a few options for tuning DNS horizontal autoscaling. Which option to
use depends on different conditions.

### Option 1: Scale down the kube-dns-autoscaler deployment to 0 replicas

This option works for all situations. Enter this command:

```
kubectl scale deployment --replicas=0 kube-dns-autoscaler --namespace=kube-system
```

The output is:

```
deployment.apps/kube-dns-autoscaler scaled
```

Verify that the replica count is zero:

```
kubectl get rs --namespace=kube-system
```

The output displays 0 in the DESIRED and CURRENT columns:

```
NAME                                  DESIRED   CURRENT   READY   AGE
...
kube-dns-autoscaler-6b59789fc8        0         0         0       ...
...
```

### Option 2: Delete the kube-dns-autoscaler deployment

This option works if kube-dns-autoscaler is under your own control, which means
no one will re-create it:

```
kubectl delete deployment kube-dns-autoscaler --namespace=kube-system
```

The output is:

```
deployment.apps "kube-dns-autoscaler" deleted
```

### Option 3: Delete the kube-dns-autoscaler manifest file from the master node

This option works if kube-dns-autoscaler is under control of the (deprecated)
[Addon Manager](https://git.k8s.io/kubernetes/cluster/addons/README.md),
and you have write access to the master node.

Sign in to the master node and delete the corresponding manifest file.
The common path for this kube-dns-autoscaler is:

```
/etc/kubernetes/addons/dns-horizontal-autoscaler/dns-horizontal-autoscaler.yaml
```

After the manifest file is deleted, the Addon Manager will delete the
kube-dns-autoscaler Deployment.

## Understanding how DNS horizontal autoscaling works

* The cluster-proportional-autoscaler application is deployed separately from
  the DNS service.
* An autoscaler Pod runs a client that polls the Kubernetes API server for the
  number of nodes and cores in the cluster.
* A desired replica count is calculated and applied to the DNS backends based on
  the current schedulable nodes and cores and the given scaling parameters.
* The scaling parameters and data points are provided via a ConfigMap to the
  autoscaler, and it refreshes its parameters table every poll interval to be up
  to date with the latest desired scaling parameters.
* Changes to the scaling parameters are allowed without rebuilding or restarting
  the autoscaler Pod.
* The autoscaler provides a controller interface to support two control
  patterns: *linear* and *ladder*.

## What's next

* Read about [Guaranteed Scheduling For Critical Add-On Pods](/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/).
* Learn more about the
  [implementation of cluster-proportional-autoscaler](https://github.com/kubernetes-sigs/cluster-proportional-autoscaler).

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
