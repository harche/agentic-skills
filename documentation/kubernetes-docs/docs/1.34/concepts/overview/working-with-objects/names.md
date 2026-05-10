# Object Names and IDs

Each [object](/docs/concepts/overview/working-with-objects/#kubernetes-objects "An entity in the Kubernetes system, representing part of the state of your cluster.") in your cluster has a [*Name*](#names) that is unique for that type of resource.
Every Kubernetes object also has a [*UID*](#uids) that is unique across your whole cluster.

For example, you can only have one Pod named `myapp-1234` within the same [namespace](/docs/concepts/overview/working-with-objects/namespaces/), but you can have one Pod and one Deployment that are each named `myapp-1234`.

For non-unique user-provided attributes, Kubernetes provides [labels](/docs/concepts/overview/working-with-objects/labels/) and [annotations](/docs/concepts/overview/working-with-objects/annotations/).

## Names

A client-provided string that refers to an object in a [resource](/docs/reference/using-api/api-concepts/#standard-api-terminology "A Kubernetes entity, representing an endpoint on the Kubernetes API server.")
URL, such as `/api/v1/pods/some-name`.

Only one object of a given kind can have a given name at a time. However, if you delete the object, you can make a new object with the same name.

**Names must be unique across all [API versions](/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning)
of the same resource. API resources are distinguished by their API group, resource type, namespace
(for namespaced resources), and name. In other words, API version is irrelevant in this context.**

> **Note:**
> In cases when objects represent a physical entity, like a Node representing a physical host, when the host is re-created under the same name without deleting and re-creating the Node, Kubernetes treats the new host as the old one, which may lead to inconsistencies.

The server may generate a name when `generateName` is provided instead of `name` in a resource create request.
When `generateName` is used, the provided value is used as a name prefix, which server appends a generated suffix
to. Even though the name is generated, it may conflict with existing names resulting in an HTTP 409 response. This
became far less likely to happen in Kubernetes v1.31 and later, since the server will make up to 8 attempts to generate a
unique name before returning an HTTP 409 response.

Below are four types of commonly used name constraints for resources.

### DNS Subdomain Names

Most resource types require a name that can be used as a DNS subdomain name
as defined in [RFC 1123](https://tools.ietf.org/html/rfc1123).
This means the name must:

* contain no more than 253 characters
* contain only lowercase alphanumeric characters, '-' or '.'
* start with an alphanumeric character
* end with an alphanumeric character

### RFC 1123 Label Names

Some resource types require their names to follow the DNS
label standard as defined in [RFC 1123](https://tools.ietf.org/html/rfc1123).
This means the name must:

* contain at most 63 characters
* contain only lowercase alphanumeric characters or '-'
* start with an alphabetic character
* end with an alphanumeric character

> **Note:**
> When the `RelaxedServiceNameValidation` feature gate is enabled,
> Service object names are allowed to start with a digit.

### RFC 1035 Label Names

Some resource types require their names to follow the DNS
label standard as defined in [RFC 1035](https://tools.ietf.org/html/rfc1035).
This means the name must:

* contain at most 63 characters
* contain only lowercase alphanumeric characters or '-'
* start with an alphabetic character
* end with an alphanumeric character

> **Note:**
> While RFC 1123 technically allows labels to start with digits, the current
> Kubernetes implementation requires both RFC 1035 and RFC 1123 labels to start
> with an alphabetic character. The exception is when the `RelaxedServiceNameValidation`
> feature gate is enabled for Service objects, which allows Service names to start with digits.

### Path Segment Names

Some resource types require their names to be able to be safely encoded as a
path segment. In other words, the name may not be "." or ".." and the name may
not contain "/" or "%".

Here's an example manifest for a Pod named `nginx-demo`.

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx-demo
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

> **Note:**
> Some resource types have additional restrictions on their names.

## UIDs

A Kubernetes systems-generated string to uniquely identify objects.

Every object created over the whole lifetime of a Kubernetes cluster has a distinct UID. It is intended to distinguish between historical occurrences of similar entities.

Kubernetes UIDs are universally unique identifiers (also known as UUIDs).
UUIDs are standardized as ISO/IEC 9834-8 and as ITU-T X.667.

## What's next

* Read about [labels](/docs/concepts/overview/working-with-objects/labels/) and [annotations](/docs/concepts/overview/working-with-objects/annotations/) in Kubernetes.
* See the [Identifiers and Names in Kubernetes](https://git.k8s.io/design-proposals-archive/architecture/identifiers.md) design document.

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
