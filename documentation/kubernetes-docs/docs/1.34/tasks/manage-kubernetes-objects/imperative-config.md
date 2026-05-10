# Imperative Management of Kubernetes Objects Using Configuration Files

Kubernetes objects can be created, updated, and deleted by using the `kubectl`
command-line tool along with an object configuration file written in YAML or JSON.
This document explains how to define and manage objects using configuration files.

## Before you begin

Install [`kubectl`](/docs/tasks/tools/).

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

## Trade-offs

The `kubectl` tool supports three kinds of object management:

* Imperative commands
* Imperative object configuration
* Declarative object configuration

See [Kubernetes Object Management](/docs/concepts/overview/working-with-objects/object-management/)
for a discussion of the advantages and disadvantage of each kind of object management.

## How to create objects

You can use `kubectl create -f` to create an object from a configuration file.
Refer to the [kubernetes API reference](/docs/reference/generated/kubernetes-api/v1.34/)
for details.

* `kubectl create -f <filename|url>`

## How to update objects

> **Warning:**
> Updating objects with the `replace` command drops all
> parts of the spec not specified in the configuration file. This
> should not be used with objects whose specs are partially managed
> by the cluster, such as Services of type `LoadBalancer`, where
> the `externalIPs` field is managed independently from the configuration
> file. Independently managed fields must be copied to the configuration
> file to prevent `replace` from dropping them.

You can use `kubectl replace -f` to update a live object according to a
configuration file.

* `kubectl replace -f <filename|url>`

## How to delete objects

You can use `kubectl delete -f` to delete an object that is described in a
configuration file.

* `kubectl delete -f <filename|url>`

> **Note:**
> If configuration file has specified the `generateName` field in the `metadata`
> section instead of the `name` field, you cannot delete the object using
> `kubectl delete -f <filename|url>`.
> You will have to use other flags for deleting the object. For example:
>
> ```
> kubectl delete <type> <name>
> kubectl delete <type> -l <label>
> ```

## How to view an object

You can use `kubectl get -f` to view information about an object that is
described in a configuration file.

* `kubectl get -f <filename|url> -o yaml`

The `-o yaml` flag specifies that the full object configuration is printed.
Use `kubectl get -h` to see a list of options.

## Limitations

The `create`, `replace`, and `delete` commands work well when each object's
configuration is fully defined and recorded in its configuration
file. However when a live object is updated, and the updates are not merged
into its configuration file, the updates will be lost the next time a `replace`
is executed. This can happen if a controller, such as
a HorizontalPodAutoscaler, makes updates directly to a live object. Here's
an example:

1. You create an object from a configuration file.
2. Another source updates the object by changing some field.
3. You replace the object from the configuration file. Changes made by
   the other source in step 2 are lost.

If you need to support multiple writers to the same object, you can use
`kubectl apply` to manage the object.

## Creating and editing an object from a URL without saving the configuration

Suppose you have the URL of an object configuration file. You can use
`kubectl create --edit` to make changes to the configuration before the
object is created. This is particularly useful for tutorials and tasks
that point to a configuration file that could be modified by the reader.

```
kubectl create -f <url> --edit
```

## Migrating from imperative commands to imperative object configuration

Migrating from imperative commands to imperative object configuration involves
several manual steps.

1. Export the live object to a local object configuration file:

   ```
   kubectl get <kind>/<name> -o yaml > <kind>_<name>.yaml
   ```
2. Manually remove the status field from the object configuration file.
3. For subsequent object management, use `replace` exclusively.

   ```
   kubectl replace -f <kind>_<name>.yaml
   ```

## Defining controller selectors and PodTemplate labels

> **Warning:**
> Updating selectors on controllers is strongly discouraged.

The recommended approach is to define a single, immutable PodTemplate label
used only by the controller selector with no other semantic meaning.

Example label:

```
selector:
  matchLabels:
      controller-selector: "apps/v1/deployment/nginx"
template:
  metadata:
    labels:
      controller-selector: "apps/v1/deployment/nginx"
```

## What's next

* [Managing Kubernetes Objects Using Imperative Commands](/docs/tasks/manage-kubernetes-objects/imperative-command/)
* [Declarative Management of Kubernetes Objects Using Configuration Files](/docs/tasks/manage-kubernetes-objects/declarative-config/)
* [Kubectl Command Reference](/docs/reference/generated/kubectl/kubectl-commands/)
* [Kubernetes API Reference](/docs/reference/generated/kubernetes-api/v1.34/)

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
