# Updating Configuration via a ConfigMap

This page provides a step-by-step example of updating configuration within a Pod via a ConfigMap
and builds upon the [Configure a Pod to Use a ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/) task.
At the end of this tutorial, you will understand how to change the configuration for a running application.
This tutorial uses the `alpine` and `nginx` images as examples.

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

You need to have the [curl](https://curl.se/) command-line tool for making HTTP requests from
the terminal or command prompt. If you do not have `curl` available, you can install it. Check the
documentation for your local operating system.

## Objectives

* Update configuration via a ConfigMap mounted as a Volume
* Update environment variables of a Pod via a ConfigMap
* Update configuration via a ConfigMap in a multi-container Pod
* Update configuration via a ConfigMap in a Pod possessing a Sidecar Container

## Update configuration via a ConfigMap mounted as a Volume

Use the `kubectl create configmap` command to create a ConfigMap from
[literal values](/docs/tasks/configure-pod-container/configure-pod-configmap/#create-configmaps-from-literal-values):

```
kubectl create configmap sport --from-literal=sport=football
```

Below is an example of a Deployment manifest with the ConfigMap `sport` mounted as a
[volume](/docs/concepts/storage/volumes/ "A directory containing data, accessible to the containers in a pod.") into the Pod's only container.

[`deployments/deployment-with-configmap-as-volume.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/deployments/deployment-with-configmap-as-volume.yaml)![](/images/copycode.svg "Copy deployments/deployment-with-configmap-as-volume.yaml to clipboard")

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: configmap-volume
  labels:
    app.kubernetes.io/name: configmap-volume
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: configmap-volume
  template:
    metadata:
      labels:
        app.kubernetes.io/name: configmap-volume
    spec:
      containers:
        - name: alpine
          image: alpine:3
          command:
            - /bin/sh
            - -c
            - while true; do echo "$(date) My preferred sport is $(cat /etc/config/sport)";
              sleep 10; done;
          ports:
            - containerPort: 80
          volumeMounts:
            - name: config-volume
              mountPath: /etc/config
      volumes:
        - name: config-volume
          configMap:
            name: sport
```

Create the Deployment:

```
kubectl apply -f https://k8s.io/examples/deployments/deployment-with-configmap-as-volume.yaml
```

Check the pods for this Deployment to ensure they are ready (matching by
[selector](/docs/concepts/overview/working-with-objects/labels/ "Allows users to filter a list of resources based on labels.")):

```
kubectl get pods --selector=app.kubernetes.io/name=configmap-volume
```

You should see an output similar to:

```
NAME                                READY   STATUS    RESTARTS   AGE
configmap-volume-6b976dfdcf-qxvbm   1/1     Running   0          72s
configmap-volume-6b976dfdcf-skpvm   1/1     Running   0          72s
configmap-volume-6b976dfdcf-tbc6r   1/1     Running   0          72s
```

On each node where one of these Pods is running, the kubelet fetches the data for
that ConfigMap and translates it to files in a local volume.
The kubelet then mounts that volume into the container, as specified in the Pod template.
The code running in that container loads the information from the file
and uses it to print a report to stdout.
You can check this report by viewing the logs for one of the Pods in that Deployment:

```
# Pick one Pod that belongs to the Deployment, and view its logs
kubectl logs deployments/configmap-volume
```

You should see an output similar to:

```
Found 3 pods, using pod/configmap-volume-76d9c5678f-x5rgj
Thu Jan  4 14:06:46 UTC 2024 My preferred sport is football
Thu Jan  4 14:06:56 UTC 2024 My preferred sport is football
Thu Jan  4 14:07:06 UTC 2024 My preferred sport is football
Thu Jan  4 14:07:16 UTC 2024 My preferred sport is football
Thu Jan  4 14:07:26 UTC 2024 My preferred sport is football
```

Edit the ConfigMap:

```
kubectl edit configmap sport
```

In the editor that appears, change the value of key `sport` from `football` to `cricket`. Save your changes.
The kubectl tool updates the ConfigMap accordingly (if you see an error, try again).

Here's an example of how that manifest could look after you edit it:

```
apiVersion: v1
data:
  sport: cricket
kind: ConfigMap
# You can leave the existing metadata as they are.
# The values you'll see won't exactly match these.
metadata:
  creationTimestamp: "2024-01-04T14:05:06Z"
  name: sport
  namespace: default
  resourceVersion: "1743935"
  uid: 024ee001-fe72-487e-872e-34d6464a8a23
```

You should see the following output:

```
configmap/sport edited
```

Tail (follow the latest entries in) the logs of one of the pods that belongs to this Deployment:

```
kubectl logs deployments/configmap-volume --follow
```

After few seconds, you should see the log output change as follows:

```
Thu Jan  4 14:11:36 UTC 2024 My preferred sport is football
Thu Jan  4 14:11:46 UTC 2024 My preferred sport is football
Thu Jan  4 14:11:56 UTC 2024 My preferred sport is football
Thu Jan  4 14:12:06 UTC 2024 My preferred sport is cricket
Thu Jan  4 14:12:16 UTC 2024 My preferred sport is cricket
```

When you have a ConfigMap that is mapped into a running Pod using either a
`configMap` volume or a `projected` volume, and you update that ConfigMap,
the running Pod sees the update almost immediately.
However, your application only sees the change if it is written to either poll for changes,
or watch for file updates.
An application that loads its configuration once at startup will not notice a change.

> **Note:**
> The total delay from the moment when the ConfigMap is updated to the moment when
> new keys are projected to the Pod can be as long as kubelet sync period.
> Also check [Mounted ConfigMaps are updated automatically](/docs/tasks/configure-pod-container/configure-pod-configmap/#mounted-configmaps-are-updated-automatically).

## Update environment variables of a Pod via a ConfigMap

Use the `kubectl create configmap` command to create a ConfigMap from
[literal values](/docs/tasks/configure-pod-container/configure-pod-configmap/#create-configmaps-from-literal-values):

```
kubectl create configmap fruits --from-literal=fruits=apples
```

Below is an example of a Deployment manifest with an environment variable configured via the ConfigMap `fruits`.

[`deployments/deployment-with-configmap-as-envvar.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/deployments/deployment-with-configmap-as-envvar.yaml)![](/images/copycode.svg "Copy deployments/deployment-with-configmap-as-envvar.yaml to clipboard")

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: configmap-env-var
  labels:
    app.kubernetes.io/name: configmap-env-var
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: configmap-env-var
  template:
    metadata:
      labels:
        app.kubernetes.io/name: configmap-env-var
    spec:
      containers:
        - name: alpine
          image: alpine:3
          env:
            - name: FRUITS
              valueFrom:
                configMapKeyRef:
                  key: fruits
                  name: fruits
          command:
            - /bin/sh
            - -c
            - while true; do echo "$(date) The basket is full of $FRUITS";
                sleep 10; done;
          ports:
            - containerPort: 80
```

Create the Deployment:

```
kubectl apply -f https://k8s.io/examples/deployments/deployment-with-configmap-as-envvar.yaml
```

Check the pods for this Deployment to ensure they are ready (matching by
[selector](/docs/concepts/overview/working-with-objects/labels/ "Allows users to filter a list of resources based on labels.")):

```
kubectl get pods --selector=app.kubernetes.io/name=configmap-env-var
```

You should see an output similar to:

```
NAME                                 READY   STATUS    RESTARTS   AGE
configmap-env-var-59cfc64f7d-74d7z   1/1     Running   0          46s
configmap-env-var-59cfc64f7d-c4wmj   1/1     Running   0          46s
configmap-env-var-59cfc64f7d-dpr98   1/1     Running   0          46s
```

The key-value pair in the ConfigMap is configured as an environment variable in the container of the Pod.
Check this by viewing the logs of one Pod that belongs to the Deployment.

```
kubectl logs deployment/configmap-env-var
```

You should see an output similar to:

```
Found 3 pods, using pod/configmap-env-var-7c994f7769-l74nq
Thu Jan  4 16:07:06 UTC 2024 The basket is full of apples
Thu Jan  4 16:07:16 UTC 2024 The basket is full of apples
Thu Jan  4 16:07:26 UTC 2024 The basket is full of apples
```

Edit the ConfigMap:

```
kubectl edit configmap fruits
```

In the editor that appears, change the value of key `fruits` from `apples` to `mangoes`. Save your changes.
The kubectl tool updates the ConfigMap accordingly (if you see an error, try again).

Here's an example of how that manifest could look after you edit it:

```
apiVersion: v1
data:
  fruits: mangoes
kind: ConfigMap
# You can leave the existing metadata as they are.
# The values you'll see won't exactly match these.
metadata:
  creationTimestamp: "2024-01-04T16:04:19Z"
  name: fruits
  namespace: default
  resourceVersion: "1749472"
```

You should see the following output:

```
configmap/fruits edited
```

Tail the logs of the Deployment and observe the output for few seconds:

```
# As the text explains, the output does NOT change
kubectl logs deployments/configmap-env-var --follow
```

Notice that the output remains **unchanged**, even though you edited the ConfigMap:

```
Thu Jan  4 16:12:56 UTC 2024 The basket is full of apples
Thu Jan  4 16:13:06 UTC 2024 The basket is full of apples
Thu Jan  4 16:13:16 UTC 2024 The basket is full of apples
Thu Jan  4 16:13:26 UTC 2024 The basket is full of apples
```

> **Note:**
> Although the value of the key inside the ConfigMap has changed, the environment variable
> in the Pod still shows the earlier value. This is because environment variables for a
> process running inside a Pod are **not** updated when the source data changes; if you
> wanted to force an update, you would need to have Kubernetes replace your existing Pods.
> The new Pods would then run with the updated information.

You can trigger that replacement. Perform a rollout for the Deployment, using
[`kubectl rollout`](/docs/reference/kubectl/generated/kubectl_rollout/):

```
# Trigger the rollout
kubectl rollout restart deployment configmap-env-var

# Wait for the rollout to complete
kubectl rollout status deployment configmap-env-var --watch=true
```

Next, check the Deployment:

```
kubectl get deployment configmap-env-var
```

You should see an output similar to:

```
NAME                READY   UP-TO-DATE   AVAILABLE   AGE
configmap-env-var   3/3     3            3           12m
```

Check the Pods:

```
kubectl get pods --selector=app.kubernetes.io/name=configmap-env-var
```

The rollout causes Kubernetes to make a new [ReplicaSet](/docs/concepts/workloads/controllers/replicaset/ "ReplicaSet ensures that a specified number of Pod replicas are running at one time")
for the Deployment; that means the existing Pods eventually terminate, and new ones are created.
After few seconds, you should see an output similar to:

```
NAME                                 READY   STATUS        RESTARTS   AGE
configmap-env-var-6d94d89bf5-2ph2l   1/1     Running       0          13s
configmap-env-var-6d94d89bf5-74twx   1/1     Running       0          8s
configmap-env-var-6d94d89bf5-d5vx8   1/1     Running       0          11s
```

> **Note:**
> Please wait for the older Pods to fully terminate before proceeding with the next steps.

View the logs for a Pod in this Deployment:

```
# Pick one Pod that belongs to the Deployment, and view its logs
kubectl logs deployment/configmap-env-var
```

You should see an output similar to the below:

```
Found 3 pods, using pod/configmap-env-var-6d9ff89fb6-bzcf6
Thu Jan  4 16:30:35 UTC 2024 The basket is full of mangoes
Thu Jan  4 16:30:45 UTC 2024 The basket is full of mangoes
Thu Jan  4 16:30:55 UTC 2024 The basket is full of mangoes
```

This demonstrates the scenario of updating environment variables in a Pod that are derived
from a ConfigMap. Changes to the ConfigMap values are applied to the Pod during the subsequent
rollout. If Pods get created for another reason, such as scaling up the Deployment, then the new Pods
also use the latest configuration values; if you don't trigger a rollout, then you might find that your
app is running with a mix of old and new environment variable values.

## Update configuration via a ConfigMap in a multi-container Pod

Use the `kubectl create configmap` command to create a ConfigMap from
[literal values](/docs/tasks/configure-pod-container/configure-pod-configmap/#create-configmaps-from-literal-values):

```
kubectl create configmap color --from-literal=color=red
```

Below is an example manifest for a Deployment that manages a set of Pods, each with two containers.
The two containers share an `emptyDir` volume that they use to communicate.
The first container runs a web server (`nginx`). The mount path for the shared volume in the
web server container is `/usr/share/nginx/html`. The second helper container is based on `alpine`,
and for this container the `emptyDir` volume is mounted at `/pod-data`. The helper container writes
a file in HTML that has its content based on a ConfigMap. The web server container serves the HTML via HTTP.

[`deployments/deployment-with-configmap-two-containers.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/deployments/deployment-with-configmap-two-containers.yaml)![](/images/copycode.svg "Copy deployments/deployment-with-configmap-two-containers.yaml to clipboard")

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: configmap-two-containers
  labels:
    app.kubernetes.io/name: configmap-two-containers
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: configmap-two-containers
  template:
    metadata:
      labels:
        app.kubernetes.io/name: configmap-two-containers
    spec:
      volumes:
        - name: shared-data
          emptyDir: {}
        - name: config-volume
          configMap:
            name: color
      containers:
        - name: nginx
          image: nginx
          volumeMounts:
            - name: shared-data
              mountPath: /usr/share/nginx/html
        - name: alpine
          image: alpine:3
          volumeMounts:
            - name: shared-data
              mountPath: /pod-data
            - name: config-volume
              mountPath: /etc/config
          command:
            - /bin/sh
            - -c
            - while true; do echo "$(date) My preferred color is $(cat /etc/config/color)" > /pod-data/index.html;
              sleep 10; done;
```

Create the Deployment:

```
kubectl apply -f https://k8s.io/examples/deployments/deployment-with-configmap-two-containers.yaml
```

Check the pods for this Deployment to ensure they are ready (matching by
[selector](/docs/concepts/overview/working-with-objects/labels/ "Allows users to filter a list of resources based on labels.")):

```
kubectl get pods --selector=app.kubernetes.io/name=configmap-two-containers
```

You should see an output similar to:

```
NAME                                        READY   STATUS    RESTARTS   AGE
configmap-two-containers-565fb6d4f4-2xhxf   2/2     Running   0          20s
configmap-two-containers-565fb6d4f4-g5v4j   2/2     Running   0          20s
configmap-two-containers-565fb6d4f4-mzsmf   2/2     Running   0          20s
```

Expose the Deployment (the `kubectl` tool creates a
[Service](/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.") for you):

```
kubectl expose deployment configmap-two-containers --name=configmap-service --port=8080 --target-port=80
```

Use `kubectl` to forward the port:

```
# this stays running in the background
kubectl port-forward service/configmap-service 8080:8080 &
```

Access the service.

```
curl http://localhost:8080
```

You should see an output similar to:

```
Fri Jan  5 08:08:22 UTC 2024 My preferred color is red
```

Edit the ConfigMap:

```
kubectl edit configmap color
```

In the editor that appears, change the value of key `color` from `red` to `blue`. Save your changes.
The kubectl tool updates the ConfigMap accordingly (if you see an error, try again).

Here's an example of how that manifest could look after you edit it:

```
apiVersion: v1
data:
  color: blue
kind: ConfigMap
# You can leave the existing metadata as they are.
# The values you'll see won't exactly match these.
metadata:
  creationTimestamp: "2024-01-05T08:12:05Z"
  name: color
  namespace: configmap
  resourceVersion: "1801272"
  uid: 80d33e4a-cbb4-4bc9-ba8c-544c68e425d6
```

Loop over the service URL for few seconds.

```
# Cancel this when you're happy with it (Ctrl-C)
while true; do curl --connect-timeout 7.5 http://localhost:8080; sleep 10; done
```

You should see the output change as follows:

```
Fri Jan  5 08:14:00 UTC 2024 My preferred color is red
Fri Jan  5 08:14:02 UTC 2024 My preferred color is red
Fri Jan  5 08:14:20 UTC 2024 My preferred color is red
Fri Jan  5 08:14:22 UTC 2024 My preferred color is red
Fri Jan  5 08:14:32 UTC 2024 My preferred color is blue
Fri Jan  5 08:14:43 UTC 2024 My preferred color is blue
Fri Jan  5 08:15:00 UTC 2024 My preferred color is blue
```

## Update configuration via a ConfigMap in a Pod possessing a sidecar container

The above scenario can be replicated by using a [Sidecar Container](/docs/concepts/workloads/pods/sidecar-containers/)
as a helper container to write the HTML file.
As a Sidecar Container is conceptually an Init Container, it is guaranteed to start before the main web server container.
This ensures that the HTML file is always available when the web server is ready to serve it.

If you are continuing from the previous scenario, you can reuse the ConfigMap named `color` for this scenario.
If you are executing this scenario independently, use the `kubectl create configmap` command to create a ConfigMap
from [literal values](/docs/tasks/configure-pod-container/configure-pod-configmap/#create-configmaps-from-literal-values):

```
kubectl create configmap color --from-literal=color=blue
```

Below is an example manifest for a Deployment that manages a set of Pods, each with a main container and
a sidecar container. The two containers share an `emptyDir` volume that they use to communicate.
The main container runs a web server (NGINX). The mount path for the shared volume in the web server container
is `/usr/share/nginx/html`. The second container is a Sidecar Container based on Alpine Linux which acts as
a helper container. For this container the `emptyDir` volume is mounted at `/pod-data`. The Sidecar Container
writes a file in HTML that has its content based on a ConfigMap. The web server container serves the HTML via HTTP.

[`deployments/deployment-with-configmap-and-sidecar-container.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/deployments/deployment-with-configmap-and-sidecar-container.yaml)![](/images/copycode.svg "Copy deployments/deployment-with-configmap-and-sidecar-container.yaml to clipboard")

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: configmap-sidecar-container
  labels:
    app.kubernetes.io/name: configmap-sidecar-container
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: configmap-sidecar-container
  template:
    metadata:
      labels:
        app.kubernetes.io/name: configmap-sidecar-container
    spec:
      volumes:
        - name: shared-data
          emptyDir: {}
        - name: config-volume
          configMap:
            name: color
      containers:
        - name: nginx
          image: nginx
          volumeMounts:
            - name: shared-data
              mountPath: /usr/share/nginx/html
      initContainers:
        - name: alpine
          image: alpine:3
          restartPolicy: Always
          volumeMounts:
            - name: shared-data
              mountPath: /pod-data
            - name: config-volume
              mountPath: /etc/config
          command:
            - /bin/sh
            - -c
            - while true; do echo "$(date) My preferred color is $(cat /etc/config/color)" > /pod-data/index.html;
              sleep 10; done;
```

Create the Deployment:

```
kubectl apply -f https://k8s.io/examples/deployments/deployment-with-configmap-and-sidecar-container.yaml
```

Check the pods for this Deployment to ensure they are ready (matching by
[selector](/docs/concepts/overview/working-with-objects/labels/ "Allows users to filter a list of resources based on labels.")):

```
kubectl get pods --selector=app.kubernetes.io/name=configmap-sidecar-container
```

You should see an output similar to:

```
NAME                                           READY   STATUS    RESTARTS   AGE
configmap-sidecar-container-5fb59f558b-87rp7   2/2     Running   0          94s
configmap-sidecar-container-5fb59f558b-ccs7s   2/2     Running   0          94s
configmap-sidecar-container-5fb59f558b-wnmgk   2/2     Running   0          94s
```

Expose the Deployment (the `kubectl` tool creates a
[Service](/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.") for you):

```
kubectl expose deployment configmap-sidecar-container --name=configmap-sidecar-service --port=8081 --target-port=80
```

Use `kubectl` to forward the port:

```
# this stays running in the background
kubectl port-forward service/configmap-sidecar-service 8081:8081 &
```

Access the service.

```
curl http://localhost:8081
```

You should see an output similar to:

```
Sat Feb 17 13:09:05 UTC 2024 My preferred color is blue
```

Edit the ConfigMap:

```
kubectl edit configmap color
```

In the editor that appears, change the value of key `color` from `blue` to `green`. Save your changes.
The kubectl tool updates the ConfigMap accordingly (if you see an error, try again).

Here's an example of how that manifest could look after you edit it:

```
apiVersion: v1
data:
  color: green
kind: ConfigMap
# You can leave the existing metadata as they are.
# The values you'll see won't exactly match these.
metadata:
  creationTimestamp: "2024-02-17T12:20:30Z"
  name: color
  namespace: default
  resourceVersion: "1054"
  uid: e40bb34c-58df-4280-8bea-6ed16edccfaa
```

Loop over the service URL for few seconds.

```
# Cancel this when you're happy with it (Ctrl-C)
while true; do curl --connect-timeout 7.5 http://localhost:8081; sleep 10; done
```

You should see the output change as follows:

```
Sat Feb 17 13:12:35 UTC 2024 My preferred color is blue
Sat Feb 17 13:12:45 UTC 2024 My preferred color is blue
Sat Feb 17 13:12:55 UTC 2024 My preferred color is blue
Sat Feb 17 13:13:05 UTC 2024 My preferred color is blue
Sat Feb 17 13:13:15 UTC 2024 My preferred color is green
Sat Feb 17 13:13:25 UTC 2024 My preferred color is green
Sat Feb 17 13:13:35 UTC 2024 My preferred color is green
```

## Update configuration via an immutable ConfigMap that is mounted as a volume

> **Note:**
> Immutable ConfigMaps are especially used for configuration that is constant and is **not** expected
> to change over time. Marking a ConfigMap as immutable allows a performance improvement where the kubelet does not watch for changes.
>
> If you do need to make a change, you should plan to either:
>
> * change the name of the ConfigMap, and switch to running Pods that reference the new name
> * replace all the nodes in your cluster that have previously run a Pod that used the old value
> * restart the kubelet on any node where the kubelet previously loaded the old ConfigMap

An example manifest for an [Immutable ConfigMap](/docs/concepts/configuration/configmap/#configmap-immutable) is shown below.

[`configmap/immutable-configmap.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/configmap/immutable-configmap.yaml)![](/images/copycode.svg "Copy configmap/immutable-configmap.yaml to clipboard")

```
apiVersion: v1
data:
  company_name: "ACME, Inc." # existing fictional company name
kind: ConfigMap
immutable: true
metadata:
  name: company-name-20150801
```

Create the Immutable ConfigMap:

```
kubectl apply -f https://k8s.io/examples/configmap/immutable-configmap.yaml
```

Below is an example of a Deployment manifest with the Immutable ConfigMap `company-name-20150801` mounted as a
[volume](/docs/concepts/storage/volumes/ "A directory containing data, accessible to the containers in a pod.") into the Pod's only container.

[`deployments/deployment-with-immutable-configmap-as-volume.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/deployments/deployment-with-immutable-configmap-as-volume.yaml)![](/images/copycode.svg "Copy deployments/deployment-with-immutable-configmap-as-volume.yaml to clipboard")

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: immutable-configmap-volume
  labels:
    app.kubernetes.io/name: immutable-configmap-volume
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: immutable-configmap-volume
  template:
    metadata:
      labels:
        app.kubernetes.io/name: immutable-configmap-volume
    spec:
      containers:
        - name: alpine
          image: alpine:3
          command:
            - /bin/sh
            - -c
            - while true; do echo "$(date) The name of the company is $(cat /etc/config/company_name)";
              sleep 10; done;
          ports:
            - containerPort: 80
          volumeMounts:
            - name: config-volume
              mountPath: /etc/config
      volumes:
        - name: config-volume
          configMap:
            name: company-name-20150801
```

Create the Deployment:

```
kubectl apply -f https://k8s.io/examples/deployments/deployment-with-immutable-configmap-as-volume.yaml
```

Check the pods for this Deployment to ensure they are ready (matching by
[selector](/docs/concepts/overview/working-with-objects/labels/ "Allows users to filter a list of resources based on labels.")):

```
kubectl get pods --selector=app.kubernetes.io/name=immutable-configmap-volume
```

You should see an output similar to:

```
NAME                                          READY   STATUS    RESTARTS   AGE
immutable-configmap-volume-78b6fbff95-5gsfh   1/1     Running   0          62s
immutable-configmap-volume-78b6fbff95-7vcj4   1/1     Running   0          62s
immutable-configmap-volume-78b6fbff95-vdslm   1/1     Running   0          62s
```

The Pod's container refers to the data defined in the ConfigMap and uses it to print a report to stdout.
You can check this report by viewing the logs for one of the Pods in that Deployment:

```
# Pick one Pod that belongs to the Deployment, and view its logs
kubectl logs deployments/immutable-configmap-volume
```

You should see an output similar to:

```
Found 3 pods, using pod/immutable-configmap-volume-78b6fbff95-5gsfh
Wed Mar 20 03:52:34 UTC 2024 The name of the company is ACME, Inc.
Wed Mar 20 03:52:44 UTC 2024 The name of the company is ACME, Inc.
Wed Mar 20 03:52:54 UTC 2024 The name of the company is ACME, Inc.
```

> **Note:**
> Once a ConfigMap is marked as immutable, it is not possible to revert this change
> nor to mutate the contents of the data or the binaryData field.
> In order to modify the behavior of the Pods that use this configuration,
> you will create a new immutable ConfigMap and edit the Deployment
> to define a slightly different pod template, referencing the new ConfigMap.

Create a new immutable ConfigMap by using the manifest shown below:

[`configmap/new-immutable-configmap.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/configmap/new-immutable-configmap.yaml)![](/images/copycode.svg "Copy configmap/new-immutable-configmap.yaml to clipboard")

```
apiVersion: v1
data:
  company_name: "Fiktivesunternehmen GmbH" # new fictional company name
kind: ConfigMap
immutable: true
metadata:
  name: company-name-20240312
```

```
kubectl apply -f https://k8s.io/examples/configmap/new-immutable-configmap.yaml
```

You should see an output similar to:

```
configmap/company-name-20240312 created
```

Check the newly created ConfigMap:

```
kubectl get configmap
```

You should see an output displaying both the old and new ConfigMaps:

```
NAME                    DATA   AGE
company-name-20150801   1      22m
company-name-20240312   1      24s
```

Modify the Deployment to reference the new ConfigMap.

Edit the Deployment:

```
kubectl edit deployment immutable-configmap-volume
```

In the editor that appears, update the existing volume definition to use the new ConfigMap.

```
volumes:
- configMap:
    defaultMode: 420
    name: company-name-20240312 # Update this field
  name: config-volume
```

You should see the following output:

```
deployment.apps/immutable-configmap-volume edited
```

This will trigger a rollout. Wait for all the previous Pods to terminate and the new Pods to be in a ready state.

Monitor the status of the Pods:

```
kubectl get pods --selector=app.kubernetes.io/name=immutable-configmap-volume
```

```
NAME                                          READY   STATUS        RESTARTS   AGE
immutable-configmap-volume-5fdb88fcc8-29v8n   1/1     Running       0          13s
immutable-configmap-volume-5fdb88fcc8-52ddd   1/1     Running       0          14s
immutable-configmap-volume-5fdb88fcc8-n5jx4   1/1     Running       0          15s
immutable-configmap-volume-78b6fbff95-5gsfh   1/1     Terminating   0          32m
immutable-configmap-volume-78b6fbff95-7vcj4   1/1     Terminating   0          32m
immutable-configmap-volume-78b6fbff95-vdslm   1/1     Terminating   0          32m
```

You should eventually see an output similar to:

```
NAME                                          READY   STATUS    RESTARTS   AGE
immutable-configmap-volume-5fdb88fcc8-29v8n   1/1     Running   0          43s
immutable-configmap-volume-5fdb88fcc8-52ddd   1/1     Running   0          44s
immutable-configmap-volume-5fdb88fcc8-n5jx4   1/1     Running   0          45s
```

View the logs for a Pod in this Deployment:

```
# Pick one Pod that belongs to the Deployment, and view its logs
kubectl logs deployment/immutable-configmap-volume
```

You should see an output similar to the below:

```
Found 3 pods, using pod/immutable-configmap-volume-5fdb88fcc8-n5jx4
Wed Mar 20 04:24:17 UTC 2024 The name of the company is Fiktivesunternehmen GmbH
Wed Mar 20 04:24:27 UTC 2024 The name of the company is Fiktivesunternehmen GmbH
Wed Mar 20 04:24:37 UTC 2024 The name of the company is Fiktivesunternehmen GmbH
```

Once all the deployments have migrated to use the new immutable ConfigMap, it is advised to delete the old one.

```
kubectl delete configmap company-name-20150801
```

## Summary

Changes to a ConfigMap mounted as a Volume on a Pod are available seamlessly after the subsequent kubelet sync.

Changes to a ConfigMap that configures environment variables for a Pod are available after the subsequent rollout for the Pod.

Once a ConfigMap is marked as immutable, it is not possible to revert this change
(you cannot make an immutable ConfigMap mutable), and you also cannot make any change
to the contents of the `data` or the `binaryData` field. You can delete and recreate
the ConfigMap, or you can make a new different ConfigMap. When you delete a ConfigMap,
running containers and their Pods maintain a mount point to any volume that referenced
that existing ConfigMap.

## Cleaning up

Terminate the `kubectl port-forward` commands in case they are running.

Delete the resources created during the tutorial:

```
kubectl delete deployment configmap-volume configmap-env-var configmap-two-containers configmap-sidecar-container immutable-configmap-volume
kubectl delete service configmap-service configmap-sidecar-service
kubectl delete configmap sport fruits color company-name-20240312

kubectl delete configmap company-name-20150801 # In case it was not handled during the task execution
```

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
