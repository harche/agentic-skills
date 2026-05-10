# List All Container Images Running in a Cluster

This page shows how to use kubectl to list all of the Container images
for Pods running in a cluster.

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

In this exercise you will use kubectl to fetch all of the Pods
running in a cluster, and format the output to pull out the list
of Containers for each.

## List all Container images in all namespaces

* Fetch all Pods in all namespaces using `kubectl get pods --all-namespaces`
* Format the output to include only the list of Container image names
  using `-o jsonpath={.items[*].spec['initContainers', 'containers'][*].image}`. This will recursively parse out the
  `image` field from the returned json.
  + See the [jsonpath reference](/docs/reference/kubectl/jsonpath/)
    for further information on how to use jsonpath.
* Format the output using standard tools: `tr`, `sort`, `uniq`
  + Use `tr` to replace spaces with newlines
  + Use `sort` to sort the results
  + Use `uniq` to aggregate image counts

```
kubectl get pods --all-namespaces -o jsonpath="{.items[*].spec['initContainers', 'containers'][*].image}" |\
tr -s '[[:space:]]' '\n' |\
sort |\
uniq -c
```

The jsonpath is interpreted as follows:

* `.items[*]`: for each returned value
* `.spec`: get the spec
* `['initContainers', 'containers'][*]`: for each container
* `.image`: get the image

> **Note:**
> When fetching a single Pod by name, for example `kubectl get pod nginx`,
> the `.items[*]` portion of the path should be omitted because a single
> Pod is returned instead of a list of items.

## List Container images by Pod

The formatting can be controlled further by using the `range` operation to
iterate over elements individually.

```
kubectl get pods --all-namespaces -o jsonpath='{range .items[*]}{"\n"}{.metadata.name}{":\t"}{range .spec.containers[*]}{.image}{", "}{end}{end}' |\
sort
```

## List Container images filtering by Pod label

To target only Pods matching a specific label, use the -l flag. The
following matches only Pods with labels matching `app=nginx`.

```
kubectl get pods --all-namespaces -o jsonpath="{.items[*].spec.containers[*].image}" -l app=nginx
```

## List Container images filtering by Pod namespace

To target only pods in a specific namespace, use the namespace flag. The
following matches only Pods in the `kube-system` namespace.

```
kubectl get pods --namespace kube-system -o jsonpath="{.items[*].spec.containers[*].image}"
```

## List Container images using a go-template instead of jsonpath

As an alternative to jsonpath, Kubectl supports using [go-templates](https://pkg.go.dev/text/template)
for formatting the output:

```
kubectl get pods --all-namespaces -o go-template --template="{{range .items}}{{range .spec.containers}}{{.image}} {{end}}{{end}}"
```

## What's next

### Reference

* [Jsonpath](/docs/reference/kubectl/jsonpath/) reference guide
* [Go template](https://pkg.go.dev/text/template) reference guide

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
