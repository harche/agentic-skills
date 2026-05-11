# Configure a Pod to Use a PersistentVolume for Storage

This page shows you how to configure a Pod to use a
[PersistentVolumeClaim](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims "Claims storage resources defined in a PersistentVolume so that it can be mounted as a volume in a container.")
for storage.
Here is a summary of the process:

1. You, as cluster administrator, create a PersistentVolume backed by physical
   storage. You do not associate the volume with any Pod.
2. You, now taking the role of a developer / cluster user, create a
   PersistentVolumeClaim that is automatically bound to a suitable
   PersistentVolume.
3. You create a Pod that uses the above PersistentVolumeClaim for storage.

## Before you begin

* You need to have a Kubernetes cluster that has only one Node, and the
  [kubectl](/docs/reference/kubectl/ "A command line tool for communicating with a Kubernetes cluster.")
  command-line tool must be configured to communicate with your cluster. If you
  do not already have a single-node cluster, you can create one by using
  [Minikube](https://minikube.sigs.k8s.io/docs/).
* Familiarize yourself with the material in
  [Persistent Volumes](/docs/concepts/storage/persistent-volumes/).

## Create an index.html file on your Node

Open a shell to the single Node in your cluster. How you open a shell depends
on how you set up your cluster. For example, if you are using Minikube, you
can open a shell to your Node by entering `minikube ssh`.

In your shell on that Node, create a `/mnt/data` directory:

```
# This assumes that your Node uses "sudo" to run commands
# as the superuser
sudo mkdir /mnt/data
```

In the `/mnt/data` directory, create an `index.html` file:

```
# This again assumes that your Node uses "sudo" to run commands
# as the superuser
sudo sh -c "echo 'Hello from Kubernetes storage' > /mnt/data/index.html"
```

> **Note:**
> If your Node uses a tool for superuser access other than `sudo`, you can
> usually make this work if you replace `sudo` with the name of the other tool.

Test that the `index.html` file exists:

```
cat /mnt/data/index.html
```

The output should be:

```
Hello from Kubernetes storage
```

You can now close the shell to your Node.

## Create a PersistentVolume

In this exercise, you create a *hostPath* PersistentVolume. Kubernetes supports
hostPath for development and testing on a single-node cluster. A hostPath
PersistentVolume uses a file or directory on the Node to emulate network-attached storage.

In a production cluster, you would not use hostPath. Instead a cluster administrator
would provision a network resource like a Google Compute Engine persistent disk,
an NFS share, or an Amazon Elastic Block Store volume. Cluster administrators can also
use [StorageClasses](/docs/reference/generated/kubernetes-api/v1.34/#storageclass-v1-storage-k8s-io)
to set up
[dynamic provisioning](/docs/concepts/storage/dynamic-provisioning/).

Here is the configuration file for the hostPath PersistentVolume:

[`pods/storage/pv-volume.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/storage/pv-volume.yaml)![](/images/copycode.svg "Copy pods/storage/pv-volume.yaml to clipboard")

```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: task-pv-volume
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data"
```

The configuration file specifies that the volume is at `/mnt/data` on the
cluster's Node. The configuration also specifies a size of 10 gibibytes and
an access mode of `ReadWriteOnce`, which means the volume can be mounted as
read-write by a single Node. It defines the [StorageClass name](/docs/concepts/storage/persistent-volumes/#class)
`manual` for the PersistentVolume, which will be used to bind
PersistentVolumeClaim requests to this PersistentVolume.

> **Note:**
> This example uses the `ReadWriteOnce` access mode, for simplicity. For
> production use, the Kubernetes project recommends using the `ReadWriteOncePod`
> access mode instead.

Create the PersistentVolume:

```
kubectl apply -f https://k8s.io/examples/pods/storage/pv-volume.yaml
```

View information about the PersistentVolume:

```
kubectl get pv task-pv-volume
```

The output shows that the PersistentVolume has a `STATUS` of `Available`. This
means it has not yet been bound to a PersistentVolumeClaim.

```
NAME             CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS      CLAIM     STORAGECLASS   REASON    AGE
task-pv-volume   10Gi       RWO           Retain          Available             manual                   4s
```

## Create a PersistentVolumeClaim

The next step is to create a PersistentVolumeClaim. Pods use PersistentVolumeClaims
to request physical storage. In this exercise, you create a PersistentVolumeClaim
that requests a volume of at least three gibibytes that can provide read-write
access for at most one Node at a time.

Here is the configuration file for the PersistentVolumeClaim:

[`pods/storage/pv-claim.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/storage/pv-claim.yaml)![](/images/copycode.svg "Copy pods/storage/pv-claim.yaml to clipboard")

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: task-pv-claim
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 3Gi
```

Create the PersistentVolumeClaim:

```
kubectl apply -f https://k8s.io/examples/pods/storage/pv-claim.yaml
```

After you create the PersistentVolumeClaim, the Kubernetes control plane looks
for a PersistentVolume that satisfies the claim's requirements. If the control
plane finds a suitable PersistentVolume with the same StorageClass, it binds the
claim to the volume.

Look again at the PersistentVolume:

```
kubectl get pv task-pv-volume
```

Now the output shows a `STATUS` of `Bound`.

```
NAME             CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM                   STORAGECLASS   REASON    AGE
task-pv-volume   10Gi       RWO           Retain          Bound     default/task-pv-claim   manual                   2m
```

Look at the PersistentVolumeClaim:

```
kubectl get pvc task-pv-claim
```

The output shows that the PersistentVolumeClaim is bound to your PersistentVolume,
`task-pv-volume`.

```
NAME            STATUS    VOLUME           CAPACITY   ACCESSMODES   STORAGECLASS   AGE
task-pv-claim   Bound     task-pv-volume   10Gi       RWO           manual         30s
```

## Create a Pod

The next step is to create a Pod that uses your PersistentVolumeClaim as a volume.

Here is the configuration file for the Pod:

[`pods/storage/pv-pod.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/storage/pv-pod.yaml)![](/images/copycode.svg "Copy pods/storage/pv-pod.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: task-pv-pod
spec:
  volumes:
    - name: task-pv-storage
      persistentVolumeClaim:
        claimName: task-pv-claim
  containers:
    - name: task-pv-container
      image: nginx
      ports:
        - containerPort: 80
          name: "http-server"
      volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: task-pv-storage
```

Notice that the Pod's configuration file specifies a PersistentVolumeClaim, but
it does not specify a PersistentVolume. From the Pod's point of view, the claim
is a volume.

Create the Pod:

```
kubectl apply -f https://k8s.io/examples/pods/storage/pv-pod.yaml
```

Verify that the container in the Pod is running:

```
kubectl get pod task-pv-pod
```

Get a shell to the container running in your Pod:

```
kubectl exec -it task-pv-pod -- /bin/bash
```

In your shell, verify that nginx is serving the `index.html` file from the
hostPath volume:

```
# Be sure to run these 3 commands inside the root shell that comes from
# running "kubectl exec" in the previous step
apt update
apt install curl
curl http://localhost/
```

The output shows the text that you wrote to the `index.html` file on the
hostPath volume:

```
Hello from Kubernetes storage
```

If you see that message, you have successfully configured a Pod to
use storage from a PersistentVolumeClaim.

## Clean up

Delete the Pod:

```
kubectl delete pod task-pv-pod
```

## Mounting the same PersistentVolume in two places

You have understood how to create a PersistentVolume & PersistentVolumeClaim, and how to mount
the volume to a single location in a container. Let's explore how you can mount the same PersistentVolume
at two different locations in a container. Below is an example:

[`pods/storage/pv-duplicate.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/storage/pv-duplicate.yaml)![](/images/copycode.svg "Copy pods/storage/pv-duplicate.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: test
spec:
  containers:
    - name: test
      image: nginx
      volumeMounts:
        # a mount for site-data
        - name: config
          mountPath: /usr/share/nginx/html
          subPath: html
        # another mount for nginx config
        - name: config
          mountPath: /etc/nginx/nginx.conf
          subPath: nginx.conf
  volumes:
    - name: config
      persistentVolumeClaim:
        claimName: task-pv-storage
```

Here:

* `subPath`: This field allows specific files or directories from the mounted PersistentVolume to be exposed at
  different locations within the container. In this example:
  + `subPath: html` mounts the html directory.
  + `subPath: nginx.conf` mounts a specific file, nginx.conf.

Since the first subPath is `html`, an `html` directory has to be created within `/mnt/data/`
on the node.

The second subPath `nginx.conf` means that a file within the `/mnt/data/` directory will be used. No other directory
needs to be created.

Two volume mounts will be made on your nginx container:

* `/usr/share/nginx/html` for the static website
* `/etc/nginx/nginx.conf` for the default config

### Move the index.html file on your Node to a new folder

The `index.html` file mentioned here refers to the one created in the "[Create an index.html file on your Node](#create-an-index-html-file-on-your-node)" section.

Open a shell to the single Node in your cluster. How you open a shell depends on how you set up your cluster.
For example, if you are using Minikube, you can open a shell to your Node by entering `minikube ssh`.

Create a `/mnt/data/html` directory:

```
# This assumes that your Node uses "sudo" to run commands
# as the superuser
sudo mkdir /mnt/data/html
```

Move index.html into the directory:

```
# Move index.html from its current location to the html sub-directory
sudo mv /mnt/data/index.html html
```

### Create a new nginx.conf file

[`pods/storage/nginx.conf`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/storage/nginx.conf)![](/images/copycode.svg "Copy pods/storage/nginx.conf to clipboard")

```
user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;

events {
worker_connections  1024;
}

http {
include       /etc/nginx/mime.types;
default_type  application/octet-stream;

```
log_format  main  &#39;$remote_addr - $remote_user [$time_local] &#34;$request&#34; &#39;
                  &#39;$status $body_bytes_sent &#34;$http_referer&#34; &#39;
                  &#39;&#34;$http_user_agent&#34; &#34;$http_x_forwarded_for&#34;&#39;;

access_log  /var/log/nginx/access.log  main;

sendfile        on;
#tcp_nopush     on;

keepalive_timeout  60;

#gzip  on;

include /etc/nginx/conf.d/*.conf;
```

}
```

This is a modified version of the default `nginx.conf` file. Here, the default `keepalive_timeout` has been
modified to `60`

Create the nginx.conf file:

```
cat <<EOF > /mnt/data/nginx.conf
user  nginx;
worker_processes  auto;
error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '\$remote_addr - \$remote_user [\$time_local] "\$request" '
                      '\$status \$body_bytes_sent "\$http_referer" '
                      '"\$http_user_agent" "\$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  60;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}
EOF
```

### Create a Pod

Here we will create a pod that uses the existing persistentVolume and persistentVolumeClaim.
However, the pod mounts only a specific file, `nginx.conf`, and directory, `html`, to the container.

Create the Pod:

```
kubectl apply -f https://k8s.io/examples/pods/storage/pv-duplicate.yaml
```

Verify that the container in the Pod is running:

```
kubectl get pod test
```

Get a shell to the container running in your Pod:

```
kubectl exec -it test -- /bin/bash
```

In your shell, verify that nginx is serving the `index.html` file from the
hostPath volume:

```
# Be sure to run these 3 commands inside the root shell that comes from
# running "kubectl exec" in the previous step
apt update
apt install curl
curl http://localhost/
```

The output shows the text that you wrote to the `index.html` file on the
hostPath volume:

```
Hello from Kubernetes storage
```

In your shell, also verify that nginx is serving the `nginx.conf` file from the
hostPath volume:

```
# Be sure to run these commands inside the root shell that comes from
# running "kubectl exec" in the previous step
cat /etc/nginx/nginx.conf | grep keepalive_timeout
```

The output shows the modified text that you wrote to the `nginx.conf` file on the
hostPath volume:

```
keepalive_timeout  60;
```

If you see these messages, you have successfully configured a Pod to
use a specific file and directory in a storage from a PersistentVolumeClaim.

## Clean up

Delete the Pod:

```
kubectl delete pod test
kubectl delete pvc task-pv-claim
kubectl delete pv task-pv-volume
```

If you don't already have a shell open to the Node in your cluster,
open a new shell the same way that you did earlier.

In the shell on your Node, remove the file and directory that you created:

```
# This assumes that your Node uses "sudo" to run commands
# as the superuser
sudo rm /mnt/data/html/index.html
sudo rm /mnt/data/nginx.conf
sudo rmdir /mnt/data
```

You can now close the shell to your Node.

## Access control

Storage configured with a group ID (GID) allows writing only by Pods using the same
GID. Mismatched or missing GIDs cause permission denied errors. To reduce the
need for coordination with users, an administrator can annotate a PersistentVolume
with a GID. Then the GID is automatically added to any Pod that uses the
PersistentVolume.

Use the `pv.beta.kubernetes.io/gid` annotation as follows:

```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv1
  annotations:
    pv.beta.kubernetes.io/gid: "1234"
```

When a Pod consumes a PersistentVolume that has a GID annotation, the annotated GID
is applied to all containers in the Pod in the same way that GIDs specified in the
Pod's security context are. Every GID, whether it originates from a PersistentVolume
annotation or the Pod's specification, is applied to the first process run in
each container.

> **Note:**
> When a Pod consumes a PersistentVolume, the GIDs associated with the
> PersistentVolume are not present on the Pod resource itself.

## What's next

* Learn more about [PersistentVolumes](/docs/concepts/storage/persistent-volumes/).
* Read the [Persistent Storage design document](https://git.k8s.io/design-proposals-archive/storage/persistent-storage.md).

### Reference

* [PersistentVolume](/docs/reference/generated/kubernetes-api/v1.34/#persistentvolume-v1-core)
* [PersistentVolumeSpec](/docs/reference/generated/kubernetes-api/v1.34/#persistentvolumespec-v1-core)
* [PersistentVolumeClaim](/docs/reference/generated/kubernetes-api/v1.34/#persistentvolumeclaim-v1-core)
* [PersistentVolumeClaimSpec](/docs/reference/generated/kubernetes-api/v1.34/#persistentvolumeclaimspec-v1-core)

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
