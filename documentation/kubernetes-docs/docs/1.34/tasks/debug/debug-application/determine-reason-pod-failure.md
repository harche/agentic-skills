# Determine the Reason for Pod Failure

This page shows how to write and read a Container termination message.

Termination messages provide a way for containers to write
information about fatal events to a location where it can
be easily retrieved and surfaced by tools like dashboards
and monitoring software. In most cases, information that you
put in a termination message should also be written to
the general
[Kubernetes logs](/docs/concepts/cluster-administration/logging/).

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

## Writing and reading a termination message

In this exercise, you create a Pod that runs one container.
The manifest for that Pod specifies a command that runs when the container starts:

[`debug/termination.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/debug/termination.yaml)![](/images/copycode.svg "Copy debug/termination.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: termination-demo
spec:
  containers:
  - name: termination-demo-container
    image: debian
    command: ["/bin/sh"]
    args: ["-c", "sleep 10 && echo Sleep expired > /dev/termination-log"]
```

1. Create a Pod based on the YAML configuration file:

   ```
   kubectl apply -f https://k8s.io/examples/debug/termination.yaml
   ```

   In the YAML file, in the `command` and `args` fields, you can see that the
   container sleeps for 10 seconds and then writes "Sleep expired" to
   the `/dev/termination-log` file. After the container writes
   the "Sleep expired" message, it terminates.
2. Display information about the Pod:

   ```
   kubectl get pod termination-demo
   ```

   Repeat the preceding command until the Pod is no longer running.
3. Display detailed information about the Pod:

   ```
   kubectl get pod termination-demo --output=yaml
   ```

   The output includes the "Sleep expired" message:

   ```
   apiVersion: v1
   kind: Pod
   ...
       lastState:
         terminated:
           containerID: ...
           exitCode: 0
           finishedAt: ...
           message: |
             Sleep expired
           ...
   ```
4. Use a Go template to filter the output so that it includes only the termination message:

   ```
   kubectl get pod termination-demo -o go-template="{{range .status.containerStatuses}}{{.lastState.terminated.message}}{{end}}"
   ```

If you are running a multi-container Pod, you can use a Go template to include the container's name.
By doing so, you can discover which of the containers is failing:

```
kubectl get pod multi-container-pod -o go-template='{{range .status.containerStatuses}}{{printf "%s:\n%s\n\n" .name .lastState.terminated.message}}{{end}}'
```

## Customizing the termination message

Kubernetes retrieves termination messages from the termination message file
specified in the `terminationMessagePath` field of a Container, which has a default
value of `/dev/termination-log`. By customizing this field, you can tell Kubernetes
to use a different file. Kubernetes use the contents from the specified file to
populate the Container's status message on both success and failure.

The termination message is intended to be brief final status, such as an assertion failure message.
The kubelet truncates messages that are longer than 4096 bytes.

The total message length across all containers is limited to 12KiB, divided equally among each container.
For example, if there are 12 containers (`initContainers` or `containers`), each has 1024 bytes of available termination message space.

The default termination message path is `/dev/termination-log`.
You cannot set the termination message path after a Pod is launched.

In the following example, the container writes termination messages to
`/tmp/my-log` for Kubernetes to retrieve:

```
apiVersion: v1
kind: Pod
metadata:
  name: msg-path-demo
spec:
  containers:
  - name: msg-path-demo-container
    image: debian
    terminationMessagePath: "/tmp/my-log"
```

Moreover, users can set the `terminationMessagePolicy` field of a Container for
further customization. This field defaults to "`File`" which means the termination
messages are retrieved only from the termination message file. By setting the
`terminationMessagePolicy` to "`FallbackToLogsOnError`", you can tell Kubernetes
to use the last chunk of container log output if the termination message file
is empty and the container exited with an error. The log output is limited to
2048 bytes or 80 lines, whichever is smaller.

## What's next

* See the `terminationMessagePath` field in
  [Container](/docs/reference/generated/kubernetes-api/v1.34/#container-v1-core).
* See [ImagePullBackOff](/docs/concepts/containers/images/#imagepullbackoff) in [Images](/docs/concepts/containers/images/).
* Learn about [retrieving logs](/docs/concepts/cluster-administration/logging/).
* Learn about [Go templates](https://pkg.go.dev/text/template).
* Learn about [Pod status](/docs/tasks/debug/debug-application/debug-init-containers/#understanding-pod-status) and [Pod phase](/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase).
* Learn about [container states](/docs/concepts/workloads/pods/pod-lifecycle/#container-states).

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
