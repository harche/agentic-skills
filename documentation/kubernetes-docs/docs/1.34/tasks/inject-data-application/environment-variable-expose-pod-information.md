# Expose Pod Information to Containers Through Environment Variables

This page shows how a Pod can use environment variables to expose information
about itself to containers running in the Pod, using the *downward API*.
You can use environment variables to expose Pod fields, container fields, or both.

In Kubernetes, there are two ways to expose Pod and container fields to a running container:

* *Environment variables*, as explained in this task
* [Volume files](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)

Together, these two ways of exposing Pod and container fields are called the
downward API.

As Services are the primary mode of communication between containerized applications managed by Kubernetes,
it is helpful to be able to discover them at runtime.

Read more about accessing Services [here](/docs/tutorials/services/connect-applications-service/#accessing-the-service).

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

## Use Pod fields as values for environment variables

In this part of exercise, you create a Pod that has one container, and you
project Pod-level fields into the running container as environment variables.

[`pods/inject/dapi-envars-pod.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/inject/dapi-envars-pod.yaml)![](/images/copycode.svg "Copy pods/inject/dapi-envars-pod.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: dapi-envars-fieldref
spec:
  containers:
    - name: test-container
      image: registry.k8s.io/busybox:1.27.2
      command: [ "sh", "-c"]
      args:
      - while true; do
          echo -en '\n';
          printenv MY_NODE_NAME MY_POD_NAME MY_POD_NAMESPACE;
          printenv MY_POD_IP MY_POD_SERVICE_ACCOUNT;
          sleep 10;
        done;
      env:
        - name: MY_NODE_NAME
          valueFrom:
            fieldRef:
              fieldPath: spec.nodeName
        - name: MY_POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: MY_POD_NAMESPACE
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace
        - name: MY_POD_IP
          valueFrom:
            fieldRef:
              fieldPath: status.podIP
        - name: MY_POD_SERVICE_ACCOUNT
          valueFrom:
            fieldRef:
              fieldPath: spec.serviceAccountName
  restartPolicy: Never
```

In that manifest, you can see five environment variables. The `env`
field is an array of
environment variable definitions.
The first element in the array specifies that the `MY_NODE_NAME` environment
variable gets its value from the Pod's `spec.nodeName` field. Similarly, the
other environment variables get their names from Pod fields.

> **Note:**
> The fields in this example are Pod fields. They are not fields of the
> container in the Pod.

Create the Pod:

```
kubectl apply -f https://k8s.io/examples/pods/inject/dapi-envars-pod.yaml
```

Verify that the container in the Pod is running:

```
# If the new Pod isn't yet healthy, rerun this command a few times.
kubectl get pods
```

View the container's logs:

```
kubectl logs dapi-envars-fieldref
```

The output shows the values of selected environment variables:

```
minikube
dapi-envars-fieldref
default
172.17.0.4
default
```

To see why these values are in the log, look at the `command` and `args` fields
in the configuration file. When the container starts, it writes the values of
five environment variables to stdout. It repeats this every ten seconds.

Next, get a shell into the container that is running in your Pod:

```
kubectl exec -it dapi-envars-fieldref -- sh
```

In your shell, view the environment variables:

```
# Run this in a shell inside the container
printenv
```

The output shows that certain environment variables have been assigned the
values of Pod fields:

```
MY_POD_SERVICE_ACCOUNT=default
...
MY_POD_NAMESPACE=default
MY_POD_IP=172.17.0.4
...
MY_NODE_NAME=minikube
...
MY_POD_NAME=dapi-envars-fieldref
```

## Use container fields as values for environment variables

In the preceding exercise, you used information from Pod-level fields as the values
for environment variables.
In this next exercise, you are going to pass fields that are part of the Pod
definition, but taken from the specific
[container](/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container)
rather than from the Pod overall.

Here is a manifest for another Pod that again has just one container:

[`pods/inject/dapi-envars-container.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/inject/dapi-envars-container.yaml)![](/images/copycode.svg "Copy pods/inject/dapi-envars-container.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: dapi-envars-resourcefieldref
spec:
  containers:
    - name: test-container
      image: registry.k8s.io/busybox:1.27.2
      command: [ "sh", "-c"]
      args:
      - while true; do
          echo -en '\n';
          printenv MY_CPU_REQUEST MY_CPU_LIMIT;
          printenv MY_MEM_REQUEST MY_MEM_LIMIT;
          sleep 10;
        done;
      resources:
        requests:
          memory: "32Mi"
          cpu: "125m"
        limits:
          memory: "64Mi"
          cpu: "250m"
      env:
        - name: MY_CPU_REQUEST
          valueFrom:
            resourceFieldRef:
              containerName: test-container
              resource: requests.cpu
        - name: MY_CPU_LIMIT
          valueFrom:
            resourceFieldRef:
              containerName: test-container
              resource: limits.cpu
        - name: MY_MEM_REQUEST
          valueFrom:
            resourceFieldRef:
              containerName: test-container
              resource: requests.memory
        - name: MY_MEM_LIMIT
          valueFrom:
            resourceFieldRef:
              containerName: test-container
              resource: limits.memory
  restartPolicy: Never
```

In this manifest, you can see four environment variables. The `env`
field is an array of
environment variable definitions.
The first element in the array specifies that the `MY_CPU_REQUEST` environment
variable gets its value from the `requests.cpu` field of a container named
`test-container`. Similarly, the other environment variables get their values
from fields that are specific to this container.

Create the Pod:

```
kubectl apply -f https://k8s.io/examples/pods/inject/dapi-envars-container.yaml
```

Verify that the container in the Pod is running:

```
# If the new Pod isn't yet healthy, rerun this command a few times.
kubectl get pods
```

View the container's logs:

```
kubectl logs dapi-envars-resourcefieldref
```

The output shows the values of selected environment variables:

```
1
1
33554432
67108864
```

## What's next

* Read [Defining Environment Variables for a Container](/docs/tasks/inject-data-application/define-environment-variable-container/)
* Read the [`spec`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#PodSpec)
  API definition for Pod. This includes the definition of Container (part of Pod).
* Read the list of [available fields](/docs/concepts/workloads/pods/downward-api/#available-fields) that you
  can expose using the downward API.

Read about Pods, containers and environment variables in the legacy API reference:

* [PodSpec](/docs/reference/generated/kubernetes-api/v1.34/#podspec-v1-core)
* [Container](/docs/reference/generated/kubernetes-api/v1.34/#container-v1-core)
* [EnvVar](/docs/reference/generated/kubernetes-api/v1.34/#envvar-v1-core)
* [EnvVarSource](/docs/reference/generated/kubernetes-api/v1.34/#envvarsource-v1-core)
* [ObjectFieldSelector](/docs/reference/generated/kubernetes-api/v1.34/#objectfieldselector-v1-core)
* [ResourceFieldSelector](/docs/reference/generated/kubernetes-api/v1.34/#resourcefieldselector-v1-core)

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
