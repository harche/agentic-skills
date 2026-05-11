# Share Process Namespace between Containers in a Pod

This page shows how to configure process namespace sharing for a pod. When
process namespace sharing is enabled, processes in a container are visible
to all other containers in the same pod.

You can use this feature to configure cooperating containers, such as a log
handler sidecar container, or to troubleshoot container images that don't
include debugging utilities like a shell.

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

## Configure a Pod

Process namespace sharing is enabled using the `shareProcessNamespace` field of
`.spec` for a Pod. For example:

[`pods/share-process-namespace.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/share-process-namespace.yaml)![](/images/copycode.svg "Copy pods/share-process-namespace.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  shareProcessNamespace: true
  containers:
  - name: nginx
    image: nginx
  - name: shell
    image: busybox:1.28
    command: ["sleep", "3600"]
    securityContext:
      capabilities:
        add:
        - SYS_PTRACE
    stdin: true
    tty: true
```

1. Create the pod `nginx` on your cluster:

   ```
   kubectl apply -f https://k8s.io/examples/pods/share-process-namespace.yaml
   ```
2. Attach to the `shell` container and run `ps`:

   ```
   kubectl exec -it nginx -c shell -- /bin/sh
   ```

   If you don't see a command prompt, try pressing enter. In the container shell:

   ```
   # run this inside the "shell" container
   ps ax
   ```

   The output is similar to this:

   ```
   PID   USER     TIME  COMMAND
       1 root      0:00 /pause
       8 root      0:00 nginx: master process nginx -g daemon off;
      14 101       0:00 nginx: worker process
      15 root      0:00 sh
      21 root      0:00 ps ax
   ```

You can signal processes in other containers. For example, send `SIGHUP` to
`nginx` to restart the worker process. This requires the `SYS_PTRACE` capability.

```
# run this inside the "shell" container
kill -HUP 8   # change "8" to match the PID of the nginx leader process, if necessary
ps ax
```

The output is similar to this:

```
PID   USER     TIME  COMMAND
    1 root      0:00 /pause
    8 root      0:00 nginx: master process nginx -g daemon off;
   15 root      0:00 sh
   22 101       0:00 nginx: worker process
   23 root      0:00 ps ax
```

It's even possible to access the file system of another container using the
`/proc/$pid/root` link.

```
# run this inside the "shell" container
# change "8" to the PID of the Nginx process, if necessary
head /proc/8/root/etc/nginx/nginx.conf
```

The output is similar to this:

```
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
```

## Understanding process namespace sharing

Pods share many resources so it makes sense they would also share a process
namespace. Some containers may expect to be isolated from others, though,
so it's important to understand the differences:

1. **The container process no longer has PID 1.** Some containers refuse
   to start without PID 1 (for example, containers using `systemd`) or run
   commands like `kill -HUP 1` to signal the container process. In pods with a
   shared process namespace, `kill -HUP 1` will signal the pod sandbox
   (`/pause` in the above example).
2. **Processes are visible to other containers in the pod.** This includes all
   information visible in `/proc`, such as passwords that were passed as arguments
   or environment variables. These are protected only by regular Unix permissions.
3. **Container filesystems are visible to other containers in the pod through the
   `/proc/$pid/root` link.** This makes debugging easier, but it also means
   that filesystem secrets are protected only by filesystem permissions.

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
