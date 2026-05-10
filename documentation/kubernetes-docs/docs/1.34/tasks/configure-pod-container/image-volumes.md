# Use an Image Volume With a Pod

FEATURE STATE:
`Kubernetes v1.33 [beta]`(disabled by default)

This page shows how to configure a pod using image volumes. This allows you to
mount content from OCI registries inside containers.

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

Your Kubernetes server must be at or later than version v1.31.

To check the version, enter `kubectl version`.

* The container runtime needs to support the image volumes feature
* You need to exec commands in the host
* You need to be able to exec into pods
* You need to enable the `ImageVolume` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/)

## Run a Pod that uses an image volume

An image volume for a pod is enabled by setting the `volumes.[*].image` field of `.spec`
to a valid reference and consuming it in the `volumeMounts` of the container. For example:

[`pods/image-volumes.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/image-volumes.yaml)![](/images/copycode.svg "Copy pods/image-volumes.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: image-volume
spec:
  containers:
  - name: shell
    command: ["sleep", "infinity"]
    image: debian
    volumeMounts:
    - name: volume
      mountPath: /volume
  volumes:
  - name: volume
    image:
      reference: quay.io/crio/artifact:v2
      pullPolicy: IfNotPresent
```

1. Create the pod on your cluster:

   ```
   kubectl apply -f https://k8s.io/examples/pods/image-volumes.yaml
   ```
2. Attach to the container:

   ```
   kubectl attach -it image-volume bash
   ```
3. Check the content of a file in the volume:

   ```
   cat /volume/dir/file
   ```

   The output is similar to:

   ```
   1
   ```

   You can also check another file in a different path:

   ```
   cat /volume/file
   ```

   The output is similar to:

   ```
   2
   ```

## Use `subPath` (or `subPathExpr`)

It is possible to utilize
[`subPath`](/docs/concepts/storage/volumes/#using-subpath) or
[`subPathExpr`](/docs/concepts/storage/volumes/#using-subpath-expanded-environment)
from Kubernetes v1.33 when using the image volume feature.

[`pods/image-volumes-subpath.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/pods/image-volumes-subpath.yaml)![](/images/copycode.svg "Copy pods/image-volumes-subpath.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: image-volume
spec:
  containers:
  - name: shell
    command: ["sleep", "infinity"]
    image: debian
    volumeMounts:
    - name: volume
      mountPath: /volume
      subPath: dir
  volumes:
  - name: volume
    image:
      reference: quay.io/crio/artifact:v2
      pullPolicy: IfNotPresent
```

1. Create the pod on your cluster:

   ```
   kubectl apply -f https://k8s.io/examples/pods/image-volumes-subpath.yaml
   ```
2. Attach to the container:

   ```
   kubectl attach -it image-volume bash
   ```
3. Check the content of the file from the `dir` sub path in the volume:

   ```
   cat /volume/file
   ```

   The output is similar to:

   ```
   1
   ```

## Further reading

* [`image` volumes](/docs/concepts/storage/volumes/#image)

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
