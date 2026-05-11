# Create static Pods

*Static Pods* are managed directly by the kubelet daemon on a specific node,
without the [API server](/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API.")
observing them.
Unlike Pods that are managed by the control plane (for example, a
[Deployment](/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster."));
instead, the kubelet watches each static Pod (and restarts it if it fails).

Static Pods are always bound to one [Kubelet](/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") on a specific node.

The kubelet automatically tries to create a [mirror Pod](/docs/reference/glossary/?all=true#term-mirror-pod "An object in the API server that tracks a static pod on a kubelet.")
on the Kubernetes API server for each static Pod.
This means that the Pods running on a node are visible on the API server,
but cannot be controlled from there.
The Pod names will be suffixed with the node hostname with a leading hyphen.

> **Note:**
> If you are running clustered Kubernetes and are using static
> Pods to run a Pod on every node, you should probably be using a
> [DaemonSet](/docs/concepts/workloads/controllers/daemonset "Ensures a copy of a Pod is running across a set of nodes in a cluster.") instead.

> **Note:**
> The `spec` of a static Pod cannot refer to other API objects
> (e.g., [ServiceAccount](/docs/tasks/configure-pod-container/configure-service-account/ "Provides an identity for processes that run in a Pod."),
> [ConfigMap](/docs/concepts/configuration/configmap/ "An API object used to store non-confidential data in key-value pairs. Can be consumed as environment variables, command-line arguments, or configuration files in a volume."),
> [Secret](/docs/concepts/configuration/secret/ "Stores sensitive information, such as passwords, OAuth tokens, and ssh keys."), etc).

> **Note:**
> Static pods do not support [ephemeral containers](/docs/concepts/workloads/pods/ephemeral-containers/).

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

This page assumes you're using [CRI-O](https://cri-o.io/#what-is-cri-o "A lightweight container runtime specifically for Kubernetes") to run Pods,
and that your nodes are running the Fedora operating system.
Instructions for other distributions or Kubernetes installations may vary.

## Create a static pod

You can configure a static Pod with either a
[file system hosted configuration file](/docs/tasks/configure-pod-container/static-pod/#configuration-files)
or a [web hosted configuration file](/docs/tasks/configure-pod-container/static-pod/#pods-created-via-http).

### Filesystem-hosted static Pod manifest

Manifests are standard Pod definitions in JSON or YAML format in a specific directory.
Use the `staticPodPath: <the directory>` field in the
[kubelet configuration file](/docs/reference/config-api/kubelet-config.v1beta1/),
which periodically scans the directory and creates/deletes static Pods as YAML/JSON files appear/disappear there.
Note that the kubelet will ignore files starting with dots when scanning the specified directory.

For example, this is how to start a simple web server as a static Pod:

1. Choose a node where you want to run the static Pod. In this example, it's `my-node1`.

   ```
   ssh my-node1
   ```
2. Choose a directory, say `/etc/kubernetes/manifests` and place a web server
   Pod definition there, for example `/etc/kubernetes/manifests/static-web.yaml`:

   ```
   # Run this command on the node where kubelet is running
   mkdir -p /etc/kubernetes/manifests/
   cat <<EOF >/etc/kubernetes/manifests/static-web.yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: static-web
     labels:
       role: myrole
   spec:
     containers:
       - name: web
         image: nginx
         ports:
           - name: web
             containerPort: 80
             protocol: TCP
   EOF
   ```
3. Configure the kubelet on that node to set a `staticPodPath` value in the
   [kubelet configuration file](/docs/reference/config-api/kubelet-config.v1beta1/).
   See [Set Kubelet Parameters Via A Configuration File](/docs/tasks/administer-cluster/kubelet-config-file/)
   for more information.

   An alternative and deprecated method is to configure the kubelet on that node
   to look for static Pod manifests locally, using a command line argument.
   To use the deprecated approach, start the kubelet with the
   `--pod-manifest-path=/etc/kubernetes/manifests/` argument.
4. Restart the kubelet. On Fedora, you would run:

   ```
   # Run this command on the node where the kubelet is running
   systemctl restart kubelet
   ```

### Web-hosted static pod manifest

Kubelet periodically downloads a file specified by `--manifest-url=<URL>` argument
and interprets it as a JSON/YAML file that contains Pod definitions.
Similar to how [filesystem-hosted manifests](#configuration-files) work, the kubelet
refetches the manifest on a schedule. If there are changes to the list of static
Pods, the kubelet applies them.

To use this approach:

1. Create a YAML file and store it on a web server so that you can pass the URL of that file to the kubelet.

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: static-web
     labels:
       role: myrole
   spec:
     containers:
       - name: web
         image: nginx
         ports:
           - name: web
             containerPort: 80
             protocol: TCP
   ```
2. Configure the kubelet on your selected node to use this web manifest by
   running it with `--manifest-url=<manifest-url>`.
   On Fedora, edit `/etc/kubernetes/kubelet` to include this line:

   ```
   KUBELET_ARGS="--cluster-dns=10.254.0.10 --cluster-domain=kube.local --manifest-url=<manifest-url>"
   ```
3. Restart the kubelet. On Fedora, you would run:

   ```
   # Run this command on the node where the kubelet is running
   systemctl restart kubelet
   ```

## Observe static pod behavior

When the kubelet starts, it automatically starts all defined static Pods. As you have
defined a static Pod and restarted the kubelet, the new static Pod should
already be running.

You can view running containers (including static Pods) by running (on the node):

```
# Run this command on the node where the kubelet is running
crictl ps
```

The output might be something like:

```
CONTAINER       IMAGE                                 CREATED           STATE      NAME    ATTEMPT    POD ID
129fd7d382018   docker.io/library/nginx@sha256:...    11 minutes ago    Running    web     0          34533c6729106
```

> **Note:**
> `crictl` outputs the image URI and SHA-256 checksum. `NAME` will look more like:
> `docker.io/library/nginx@sha256:0d17b565c37bcbd895e9d92315a05c1c3c9a29f762b011a10c54a66cd53c9b31`.

You can see the mirror Pod on the API server:

```
kubectl get pods
```

```
NAME                  READY   STATUS    RESTARTS        AGE
static-web-my-node1   1/1     Running   0               2m
```

> **Note:**
> Make sure the kubelet has permission to create the mirror Pod in the API server.
> If not, the creation request is rejected by the API server.

[Labels](/docs/concepts/overview/working-with-objects/labels "Tags objects with identifying attributes that are meaningful and relevant to users.") from the static Pod are
propagated into the mirror Pod. You can use those labels as normal via
[selectors](/docs/concepts/overview/working-with-objects/labels/ "Allows users to filter a list of resources based on labels."), etc.

If you try to use `kubectl` to delete the mirror Pod from the API server,
the kubelet *doesn't* remove the static Pod:

```
kubectl delete pod static-web-my-node1
```

```
pod "static-web-my-node1" deleted
```

You can see that the Pod is still running:

```
kubectl get pods
```

```
NAME                  READY   STATUS    RESTARTS   AGE
static-web-my-node1   1/1     Running   0          4s
```

Back on your node where the kubelet is running, you can try to stop the container manually.
You'll see that, after a time, the kubelet will notice and will restart the Pod
automatically:

```
# Run these commands on the node where the kubelet is running
crictl stop 129fd7d382018 # replace with the ID of your container
sleep 20
crictl ps
```

```
CONTAINER       IMAGE                                 CREATED           STATE      NAME    ATTEMPT    POD ID
89db4553e1eeb   docker.io/library/nginx@sha256:...    19 seconds ago    Running    web     1          34533c6729106
```

Once you identify the right container, you can get the logs for that container with `crictl`:

```
# Run these commands on the node where the container is running
crictl logs <container_id>
```

```
10.240.0.48 - - [16/Nov/2022:12:45:49 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.47.0" "-"
10.240.0.48 - - [16/Nov/2022:12:45:50 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.47.0" "-"
10.240.0.48 - - [16/Nove/2022:12:45:51 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.47.0" "-"
```

To find more about how to debug using `crictl`, please visit
[*Debugging Kubernetes nodes with crictl*](/docs/tasks/debug/debug-cluster/crictl/).

## Dynamic addition and removal of static pods

The running kubelet periodically scans the configured directory
(`/etc/kubernetes/manifests` in our example) for changes and
adds/removes Pods as files appear/disappear in this directory.

```
# This assumes you are using filesystem-hosted static Pod configuration
# Run these commands on the node where the container is running
#
mv /etc/kubernetes/manifests/static-web.yaml /tmp
sleep 20
crictl ps
# You see that no nginx container is running
mv /tmp/static-web.yaml  /etc/kubernetes/manifests/
sleep 20
crictl ps
```

```
CONTAINER       IMAGE                                 CREATED           STATE      NAME    ATTEMPT    POD ID
f427638871c35   docker.io/library/nginx@sha256:...    19 seconds ago    Running    web     1          34533c6729106
```

## What's next

* [Generate static Pod manifests for control plane components](/docs/reference/setup-tools/kubeadm/implementation-details/#generate-static-pod-manifests-for-control-plane-components)
* [Generate static Pod manifest for local etcd](/docs/reference/setup-tools/kubeadm/implementation-details/#generate-static-pod-manifest-for-local-etcd)
* [Debugging Kubernetes nodes with `crictl`](/docs/tasks/debug/debug-cluster/crictl/)
* [Learn more about `crictl`](https://github.com/kubernetes-sigs/cri-tools)
* [Map `docker` CLI commands to `crictl`](/docs/reference/tools/map-crictl-dockercli/)
* [Set up etcd instances as static pods managed by a kubelet](/docs/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm/)

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
