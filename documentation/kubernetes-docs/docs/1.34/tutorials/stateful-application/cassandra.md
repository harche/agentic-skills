# Example: Deploying Cassandra with a StatefulSet

This tutorial shows you how to run [Apache Cassandra](https://cassandra.apache.org/) on Kubernetes.
Cassandra, a database, needs persistent storage to provide data durability (application *state*).
In this example, a custom Cassandra seed provider lets the database discover new Cassandra instances as they join the Cassandra cluster.

*StatefulSets* make it easier to deploy stateful applications into your Kubernetes cluster.
For more information on the features used in this tutorial, see
[StatefulSet](/docs/concepts/workloads/controllers/statefulset/).

> **Note:**
> Cassandra and Kubernetes both use the term *node* to mean a member of a cluster. In this
> tutorial, the Pods that belong to the StatefulSet are Cassandra nodes and are members
> of the Cassandra cluster (called a *ring*). When those Pods run in your Kubernetes cluster,
> the Kubernetes control plane schedules those Pods onto Kubernetes
> [Nodes](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.").
>
> When a Cassandra node starts, it uses a *seed list* to bootstrap discovery of other
> nodes in the ring.
> This tutorial deploys a custom Cassandra seed provider that lets the database discover
> new Cassandra Pods as they appear inside your Kubernetes cluster.

## Objectives

* Create and validate a Cassandra headless [Service](/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.").
* Use a [StatefulSet](/docs/concepts/workloads/controllers/statefulset/ "A StatefulSet manages deployment and scaling of a set of Pods, with durable storage and persistent identifiers for each Pod.") to create a Cassandra ring.
* Validate the StatefulSet.
* Modify the StatefulSet.
* Delete the StatefulSet and its [Pods](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.").

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

To complete this tutorial, you should already have a basic familiarity with
[Pods](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster."),
[Services](/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service."), and
[StatefulSets](/docs/concepts/workloads/controllers/statefulset/ "A StatefulSet manages deployment and scaling of a set of Pods, with durable storage and persistent identifiers for each Pod.").

### Additional Minikube setup instructions

> **Caution:**
> [Minikube](https://minikube.sigs.k8s.io/docs/) defaults to 2048MB of memory and 2 CPU.
> Running Minikube with the default resource configuration results in insufficient resource
> errors during this tutorial. To avoid these errors, start Minikube with the following settings:
>
> ```
> minikube start --memory 5120 --cpus=4
> ```

## Creating a headless Service for Cassandra

In Kubernetes, a [Service](/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.") describes a set of
[Pods](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") that perform the same task.

The following Service is used for DNS lookups between Cassandra Pods and clients within your cluster:

[`application/cassandra/cassandra-service.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/application/cassandra/cassandra-service.yaml)![](/images/copycode.svg "Copy application/cassandra/cassandra-service.yaml to clipboard")

```
apiVersion: v1
kind: Service
metadata:
  labels:
    app: cassandra
  name: cassandra
spec:
  clusterIP: None
  ports:
  - port: 9042
  selector:
    app: cassandra
```

Create a Service to track all Cassandra StatefulSet members from the `cassandra-service.yaml` file:

```
kubectl apply -f https://k8s.io/examples/application/cassandra/cassandra-service.yaml
```

### Validating (optional)

Get the Cassandra Service.

```
kubectl get svc cassandra
```

The response is

```
NAME        TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
cassandra   ClusterIP   None         <none>        9042/TCP   45s
```

If you don't see a Service named `cassandra`, that means creation failed. Read
[Debug Services](/docs/tasks/debug/debug-application/debug-service/)
for help troubleshooting common issues.

## Using a StatefulSet to create a Cassandra ring

The StatefulSet manifest, included below, creates a Cassandra ring that consists of three Pods.

> **Note:**
> This example uses the default provisioner for Minikube.
> Please update the following StatefulSet for the cloud you are working with.

[`application/cassandra/cassandra-statefulset.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/application/cassandra/cassandra-statefulset.yaml)![](/images/copycode.svg "Copy application/cassandra/cassandra-statefulset.yaml to clipboard")

```
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: cassandra
  labels:
    app: cassandra
spec:
  serviceName: cassandra
  replicas: 3
  selector:
    matchLabels:
      app: cassandra
  template:
    metadata:
      labels:
        app: cassandra
    spec:
      terminationGracePeriodSeconds: 500
      containers:
      - name: cassandra
        image: gcr.io/google-samples/cassandra:v13
        imagePullPolicy: Always
        ports:
        - containerPort: 7000
          name: intra-node
        - containerPort: 7001
          name: tls-intra-node
        - containerPort: 7199
          name: jmx
        - containerPort: 9042
          name: cql
        resources:
          limits:
            cpu: "500m"
            memory: 1Gi
          requests:
            cpu: "500m"
            memory: 1Gi
        securityContext:
          capabilities:
            add:
              - IPC_LOCK
        lifecycle:
          preStop:
            exec:
              command:
              - /bin/sh
              - -c
              - nodetool drain
        env:
          - name: MAX_HEAP_SIZE
            value: 512M
          - name: HEAP_NEWSIZE
            value: 100M
          - name: CASSANDRA_SEEDS
            value: "cassandra-0.cassandra.default.svc.cluster.local"
          - name: CASSANDRA_CLUSTER_NAME
            value: "K8Demo"
          - name: CASSANDRA_DC
            value: "DC1-K8Demo"
          - name: CASSANDRA_RACK
            value: "Rack1-K8Demo"
          - name: POD_IP
            valueFrom:
              fieldRef:
                fieldPath: status.podIP
        readinessProbe:
          exec:
            command:
            - /bin/bash
            - -c
            - /ready-probe.sh
          initialDelaySeconds: 15
          timeoutSeconds: 5
        # These volume mounts are persistent. They are like inline claims,
        # but not exactly because the names need to match exactly one of
        # the stateful pod volumes.
        volumeMounts:
        - name: cassandra-data
          mountPath: /cassandra_data
  # These are converted to volume claims by the controller
  # and mounted at the paths mentioned above.
  # do not use these in production until ssd GCEPersistentDisk or other ssd pd
  volumeClaimTemplates:
  - metadata:
      name: cassandra-data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: fast
      resources:
        requests:
          storage: 1Gi
---
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: fast
provisioner: k8s.io/minikube-hostpath
parameters:
  type: pd-ssd
```

Create the Cassandra StatefulSet from the `cassandra-statefulset.yaml` file:

```
# Use this if you are able to apply cassandra-statefulset.yaml unmodified
kubectl apply -f https://k8s.io/examples/application/cassandra/cassandra-statefulset.yaml
```

If you need to modify `cassandra-statefulset.yaml` to suit your cluster, download
<https://k8s.io/examples/application/cassandra/cassandra-statefulset.yaml> and then apply
that manifest, from the folder you saved the modified version into:

```
# Use this if you needed to modify cassandra-statefulset.yaml locally
kubectl apply -f cassandra-statefulset.yaml
```

## Validating the Cassandra StatefulSet

1. Get the Cassandra StatefulSet:

   ```
   kubectl get statefulset cassandra
   ```

   The response should be similar to:

   ```
   NAME        DESIRED   CURRENT   AGE
   cassandra   3         0         13s
   ```

   The `StatefulSet` resource deploys Pods sequentially.
2. Get the Pods to see the ordered creation status:

   ```
   kubectl get pods -l="app=cassandra"
   ```

   The response should be similar to:

   ```
   NAME          READY     STATUS              RESTARTS   AGE
   cassandra-0   1/1       Running             0          1m
   cassandra-1   0/1       ContainerCreating   0          8s
   ```

   It can take several minutes for all three Pods to deploy. Once they are deployed, the same command
   returns output similar to:

   ```
   NAME          READY     STATUS    RESTARTS   AGE
   cassandra-0   1/1       Running   0          10m
   cassandra-1   1/1       Running   0          9m
   cassandra-2   1/1       Running   0          8m
   ```
3. Run the Cassandra [nodetool](https://cwiki.apache.org/confluence/display/CASSANDRA2/NodeTool) inside the first Pod, to
   display the status of the ring.

   ```
   kubectl exec -it cassandra-0 -- nodetool status
   ```

   The response should look something like:

   ```
   Datacenter: DC1-K8Demo
   ======================
   Status=Up/Down
   |/ State=Normal/Leaving/Joining/Moving
   --  Address     Load       Tokens       Owns (effective)  Host ID                               Rack
   UN  172.17.0.5  83.57 KiB  32           74.0%             e2dd09e6-d9d3-477e-96c5-45094c08db0f  Rack1-K8Demo
   UN  172.17.0.4  101.04 KiB  32           58.8%             f89d6835-3a42-4419-92b3-0e62cae1479c  Rack1-K8Demo
   UN  172.17.0.6  84.74 KiB  32           67.1%             a6a1e8c2-3dc5-4417-b1a0-26507af2aaad  Rack1-K8Demo
   ```

## Modifying the Cassandra StatefulSet

Use `kubectl edit` to modify the size of a Cassandra StatefulSet.

1. Run the following command:

   ```
   kubectl edit statefulset cassandra
   ```

   This command opens an editor in your terminal. The line you need to change is the `replicas` field.
   The following sample is an excerpt of the StatefulSet file:

   ```
   # Please edit the object below. Lines beginning with a '#' will be ignored,
   # and an empty file will abort the edit. If an error occurs while saving this file will be
   # reopened with the relevant failures.
   #
   apiVersion: apps/v1
   kind: StatefulSet
   metadata:
     creationTimestamp: 2016-08-13T18:40:58Z
     generation: 1
     labels:
     app: cassandra
     name: cassandra
     namespace: default
     resourceVersion: "323"
     uid: 7a219483-6185-11e6-a910-42010a8a0fc0
   spec:
     replicas: 3
   ```
2. Change the number of replicas to 4, and then save the manifest.

   The StatefulSet now scales to run with 4 Pods.
3. Get the Cassandra StatefulSet to verify your change:

   ```
   kubectl get statefulset cassandra
   ```

   The response should be similar to:

   ```
   NAME        DESIRED   CURRENT   AGE
   cassandra   4         4         36m
   ```

## Cleaning up

Deleting or scaling a StatefulSet down does not delete the volumes associated with the StatefulSet.
This setting is for your safety because your data is more valuable than automatically purging all related StatefulSet resources.

> **Warning:**
> Depending on the storage class and reclaim policy, deleting the *PersistentVolumeClaims* may cause the associated volumes
> to also be deleted. Never assume you'll be able to access data if its volume claims are deleted.

1. Run the following commands (chained together into a single command) to delete everything in the Cassandra StatefulSet:

   ```
   grace=$(kubectl get pod cassandra-0 -o=jsonpath='{.spec.terminationGracePeriodSeconds}') \
     && kubectl delete statefulset -l app=cassandra \
     && echo "Sleeping ${grace} seconds" 1>&2 \
     && sleep $grace \
     && kubectl delete persistentvolumeclaim -l app=cassandra
   ```
2. Run the following command to delete the Service you set up for Cassandra:

   ```
   kubectl delete service -l app=cassandra
   ```

## Cassandra container environment variables

The Pods in this tutorial use the [`gcr.io/google-samples/cassandra:v13`](https://github.com/kubernetes/examples/blob/master/cassandra/image/Dockerfile)
image from Google's [container registry](https://cloud.google.com/container-registry/docs/).
The Docker image above is based on [debian-base](https://github.com/kubernetes/release/tree/master/images/build/debian-base)
and includes OpenJDK 8.

This image includes a standard Cassandra installation from the Apache Debian repo.
By using environment variables you can change values that are inserted into `cassandra.yaml`.

| Environment variable | Default value |
| --- | --- |
| `CASSANDRA_CLUSTER_NAME` | `'Test Cluster'` |
| `CASSANDRA_NUM_TOKENS` | `32` |
| `CASSANDRA_RPC_ADDRESS` | `0.0.0.0` |

## What's next

* Learn how to [Scale a StatefulSet](/docs/tasks/run-application/scale-stateful-set/).
* Learn more about the [*KubernetesSeedProvider*](https://github.com/kubernetes/examples/blob/master/cassandra/java/src/main/java/io/k8s/cassandra/KubernetesSeedProvider.java)
* See more custom [Seed Provider Configurations](https://git.k8s.io/examples/cassandra/java/README.md)

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
