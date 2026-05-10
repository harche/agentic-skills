# Field Selectors

*Field selectors* let you select Kubernetes [objects](/docs/concepts/overview/working-with-objects/#kubernetes-objects "An entity in the Kubernetes system, representing part of the state of your cluster.") based on the
value of one or more resource fields. Here are some examples of field selector queries:

* `metadata.name=my-service`
* `metadata.namespace!=default`
* `status.phase=Pending`

This `kubectl` command selects all Pods for which the value of the [`status.phase`](/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase) field is `Running`:

```
kubectl get pods --field-selector status.phase=Running
```

> **Note:**
> Field selectors are essentially resource *filters*. By default, no selectors/filters are applied, meaning that all resources of the specified type are selected. This makes the `kubectl` queries `kubectl get pods` and `kubectl get pods --field-selector ""` equivalent.

## Supported fields

Supported field selectors vary by Kubernetes resource type. All resource types support the `metadata.name` and `metadata.namespace` fields. Using unsupported field selectors produces an error. For example:

```
kubectl get ingress --field-selector foo.bar=baz
```

```
Error from server (BadRequest): Unable to find "ingresses" that match label selector "", field selector "foo.bar=baz": "foo.bar" is not a known field selector: only "metadata.name", "metadata.namespace"
```

### List of supported fields

| Kind | Fields |
| --- | --- |
| Pod | `spec.nodeName` `spec.restartPolicy` `spec.schedulerName` `spec.serviceAccountName` `spec.hostNetwork` `status.phase` `status.podIP` `status.podIPs` `status.nominatedNodeName` |
| Event | `involvedObject.kind` `involvedObject.namespace` `involvedObject.name` `involvedObject.uid` `involvedObject.apiVersion` `involvedObject.resourceVersion` `involvedObject.fieldPath` `reason` `reportingComponent` `source` `type` |
| Secret | `type` |
| Namespace | `status.phase` |
| ReplicaSet | `status.replicas` |
| ReplicationController | `status.replicas` |
| Job | `status.successful` |
| Node | `spec.unschedulable` |
| CertificateSigningRequest | `spec.signerName` |

### Custom resources fields

All custom resource types support the `metadata.name` and `metadata.namespace` fields.

Additionally, the `spec.versions[*].selectableFields` field of a [CustomResourceDefinition](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/ "Custom code that defines a resource to add to your Kubernetes API server without building a complete custom server.")
declares which other fields in a custom resource may be used in field selectors. See [selectable fields for custom resources](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#crd-selectable-fields)
for more information about how to use field selectors with CustomResourceDefinitions.

## Supported operators

You can use the `=`, `==`, and `!=` operators with field selectors (`=` and `==` mean the same thing). This `kubectl` command, for example, selects all Kubernetes Services that aren't in the `default` namespace:

```
kubectl get services  --all-namespaces --field-selector metadata.namespace!=default
```

> **Note:**
> [Set-based operators](/docs/concepts/overview/working-with-objects/labels/#set-based-requirement)
> (`in`, `notin`, `exists`) are not supported for field selectors.

## Chained selectors

As with [label](/docs/concepts/overview/working-with-objects/labels/) and other selectors, field selectors can be chained together as a comma-separated list. This `kubectl` command selects all Pods for which the `status.phase` does not equal `Running` and the `spec.restartPolicy` field equals `Always`:

```
kubectl get pods --field-selector=status.phase!=Running,spec.restartPolicy=Always
```

## Multiple resource types

You can use field selectors across multiple resource types. This `kubectl` command selects all Statefulsets and Services that are not in the `default` namespace:

```
kubectl get statefulsets,services --all-namespaces --field-selector metadata.namespace!=default
```

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
