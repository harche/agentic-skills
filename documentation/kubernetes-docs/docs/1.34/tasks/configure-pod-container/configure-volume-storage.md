# Configure a Pod to Use a Volume for Storage

This page shows how to configure a Pod to use a Volume for storage.

A Container's file system lives only as long as the Container does. So when a
Container terminates and restarts, filesystem changes are lost. For more
consistent storage that is independent of the Container, you can use a
[Volume](/docs/concepts/storage/volumes/). This is especially important for stateful
applications, such as key-value stores (such as Redis) and databases.

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

## Configure a volume for a Pod

In this exercise, you create a Pod that runs one Container. This Pod has a
Volume of type
[emptyDir](/docs/concepts/storage/volumes/#emptydir)
that lasts for the life of the Pod, even if the Container terminates and
restarts. Here is the configuration file for the Pod:

[`pods/storage/redis.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/storage/redis.yaml)![](/images/copycode.svg "Copy pods/storage/redis.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: redis
spec:
  containers:
  - name: redis
    image: redis
    volumeMounts:
    - name: redis-storage
      mountPath: /data/redis
  volumes:
  - name: redis-storage
    emptyDir: {}
```

1. Create the Pod:

   ```
   kubectl apply -f https://k8s.io/examples/pods/storage/redis.yaml
   ```
2. Verify that the Pod's Container is running, and then watch for changes to
   the Pod:

   ```
   kubectl get pod redis --watch
   ```

   The output looks like this:

   ```
   NAME      READY     STATUS    RESTARTS   AGE
   redis     1/1       Running   0          13s
   ```
3. In another terminal, get a shell to the running Container:

   ```
   kubectl exec -it redis -- /bin/bash
   ```
4. In your shell, go to `/data/redis`, and then create a file:

   ```
   root@redis:/data# cd /data/redis/
   root@redis:/data/redis# echo Hello > test-file
   ```
5. In your shell, list the running processes:

   ```
   root@redis:/data/redis# apt-get update
   root@redis:/data/redis# apt-get install procps
   root@redis:/data/redis# ps aux
   ```

   The output is similar to this:

   ```
   USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
   redis        1  0.1  0.1  33308  3828 ?        Ssl  00:46   0:00 redis-server *:6379
   root        12  0.0  0.0  20228  3020 ?        Ss   00:47   0:00 /bin/bash
   root        15  0.0  0.0  17500  2072 ?        R+   00:48   0:00 ps aux
   ```
6. In your shell, kill the Redis process:

   ```
   root@redis:/data/redis# kill <pid>
   ```

   where `<pid>` is the Redis process ID (PID).
7. In your original terminal, watch for changes to the Redis Pod. Eventually,
   you will see something like this:

   ```
   NAME      READY     STATUS     RESTARTS   AGE
   redis     1/1       Running    0          13s
   redis     0/1       Completed  0         6m
   redis     1/1       Running    1         6m
   ```

At this point, the Container has terminated and restarted. This is because the
Redis Pod has a
[restartPolicy](/docs/reference/generated/kubernetes-api/v1.34/#podspec-v1-core)
of `Always`.

1. Get a shell into the restarted Container:

   ```
   kubectl exec -it redis -- /bin/bash
   ```
2. In your shell, go to `/data/redis`, and verify that `test-file` is still there.

   ```
   root@redis:/data/redis# cd /data/redis/
   root@redis:/data/redis# ls
   test-file
   ```
3. Delete the Pod that you created for this exercise:

   ```
   kubectl delete pod redis
   ```

## What's next

* See [Volume](/docs/reference/generated/kubernetes-api/v1.34/#volume-v1-core).
* See [Pod](/docs/reference/generated/kubernetes-api/v1.34/#pod-v1-core).
* In addition to the local disk storage provided by `emptyDir`, Kubernetes
  supports many different network-attached storage solutions, including PD on
  GCE and EBS on EC2, which are preferred for critical data and will handle
  details such as mounting and unmounting the devices on the nodes. See
  [Volumes](/docs/concepts/storage/volumes/) for more details.

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
