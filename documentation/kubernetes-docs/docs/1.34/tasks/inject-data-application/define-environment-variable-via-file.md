# Define Environment Variable Values Using An Init Container

FEATURE STATE:
`Kubernetes v1.34 [alpha]`(disabled by default)

This page show how to configure environment variables for containers in a Pod via file.

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

Your Kubernetes server must be version v1.34.

To check the version, enter `kubectl version`.

## How the design works

In this exercise, you will create a Pod that sources environment variables from files,
projecting these values into the running container.

[`pods/inject/envars-file-container.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/inject/envars-file-container.yaml)![](/images/copycode.svg "Copy pods/inject/envars-file-container.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: envfile-test-pod
spec:
  initContainers:
    - name: setup-envfile
      image:  nginx
      command: ['sh', '-c', 'echo "DB_ADDRESS=address\nREST_ENDPOINT=endpoint" > /data/config.env']
      volumeMounts:
        - name: config
          mountPath: /data
  containers:
    - name: use-envfile
      image: nginx
      command: [ "/bin/sh", "-c", "env" ]
      env:
        - name: DB_ADDRESS
          valueFrom:
            fileKeyRef:
              path: config.env
              volumeName: config
              key: DB_ADDRESS
              optional: false
  restartPolicy: Never
  volumes:
    - name: config
      emptyDir: {}
```

In this manifest, you can see the `initContainer` mounts an `emptyDir` volume and writes environment variables to a file within it,
and the regular containers reference both the file and the environment variable key
through the `fileKeyRef` field without needing to mount the volume.
When `optional` field is set to false, the specified `key` in `fileKeyRef` must exist in the environment variables file.

The volume will only be mounted to the container that writes to the file
(`initContainer`), while the consumer container that consumes the environment variable will not have the volume mounted.

The env file format adheres to the [kubernetes env file standard](/docs/tasks/inject-data-application/define-environment-variable-via-file/#env-file-syntax).

During container initialization, the kubelet retrieves environment variables
from specified files in the `emptyDir` volume and exposes them to the container.

> **Note:**
> All container types (initContainers, regular containers, sidecars containers,
> and ephemeral containers) support environment variable loading from files.
>
> While these environment variables can store sensitive information,
> `emptyDir` volumes don't provide the same protection mechanisms as
> dedicated Secret objects. Therefore, exposing confidential environment variables
> to containers through this feature is not considered a security best practice.

Create the Pod:

```
kubectl apply -f https://k8s.io/examples/pods/inject/envars-file-container.yaml
```

Verify that the container in the Pod is running:

```
# If the new Pod isn't yet healthy, rerun this command a few times.
kubectl get pods
```

Check container logs for environment variables:

```
kubectl logs dapi-test-pod -c use-envfile | grep DB_ADDRESS
```

The output shows the values of selected environment variables:

```
DB_ADDRESS=address
```

## Env File Syntax

The format of Kubernetes env files originates from `.env` files.

In a shell environment, `.env` files are typically loaded using the `source .env` command.

For Kubernetes, the defined env file format adheres to stricter syntax rules:

* Blank Lines: Blank lines are ignored.
* Leading Spaces: Leading spaces on all lines are ignored.
* Variable Declaration: Variables must be declared as `VAR=VAL`. Spaces surrounding `=` and trailing spaces are ignored.

  ```
  VAR=VAL → VAL
  ```
* Comments: Lines beginning with # are treated as comments and ignored.

  ```
  # comment
  VAR=VAL → VAL

  VAR=VAL # not a comment → VAL # not a comment
  ```
* Line Continuation: A backslash (`\`) at the end of a variable declaration line indicates the value continues on the next line. The lines are joined with a single space.

  ```
  VAR=VAL \
  VAL2
  → VAL VAL2
  ```

## What's next

* Learn more about [environment variables](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/).
* Read [Defining Environment Variables for a Container](/docs/tasks/inject-data-application/define-environment-variable-container/)
* Read [Expose Pod Information to Containers Through Environment Variables](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)

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
