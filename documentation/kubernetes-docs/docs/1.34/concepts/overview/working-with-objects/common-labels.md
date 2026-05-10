# Recommended Labels

You can visualize and manage Kubernetes objects with more tools than kubectl and
the dashboard. A common set of labels allows tools to work interoperably, describing
objects in a common manner that all tools can understand.

In addition to supporting tooling, the recommended labels describe applications
in a way that can be queried.

The metadata is organized around the concept of an *application*. Kubernetes is not
a platform as a service (PaaS) and doesn't have or enforce a formal notion of an application.
Instead, applications are informal and described with metadata. The definition of
what an application contains is loose.

> **Note:**
> These are recommended labels. They make it easier to manage applications
> but aren't required for any core tooling.

Shared labels and annotations share a common prefix: `app.kubernetes.io`. Labels
without a prefix are private to users. The shared prefix ensures that shared labels
do not interfere with custom user labels.

## Labels

In order to take full advantage of using these labels, they should be applied
on every resource object.

| Key | Description | Example | Type |
| --- | --- | --- | --- |
| `app.kubernetes.io/name` | The name of the application | `mysql` | string |
| `app.kubernetes.io/instance` | A unique name identifying the instance of an application | `mysql-abcxyz` | string |
| `app.kubernetes.io/version` | The current version of the application (e.g., a [SemVer 1.0](https://semver.org/spec/v1.0.0.html), revision hash, etc.) | `5.7.21` | string |
| `app.kubernetes.io/component` | The component within the architecture | `database` | string |
| `app.kubernetes.io/part-of` | The name of a higher level application this one is part of | `wordpress` | string |
| `app.kubernetes.io/managed-by` | The tool being used to manage the operation of an application | `Helm` | string |

To illustrate these labels in action, consider the following [StatefulSet](/docs/concepts/workloads/controllers/statefulset/ "A StatefulSet manages deployment and scaling of a set of Pods, with durable storage and persistent identifiers for each Pod.") object:

```
# This is an excerpt
apiVersion: apps/v1
kind: StatefulSet
metadata:
  labels:
    app.kubernetes.io/name: mysql
    app.kubernetes.io/instance: mysql-abcxyz
    app.kubernetes.io/version: "5.7.21"
    app.kubernetes.io/component: database
    app.kubernetes.io/part-of: wordpress
    app.kubernetes.io/managed-by: Helm
```

## Applications And Instances Of Applications

An application can be installed one or more times into a Kubernetes cluster and,
in some cases, the same namespace. For example, WordPress can be installed more
than once where different websites are different installations of WordPress.

The name of an application and the instance name are recorded separately. For
example, WordPress has a `app.kubernetes.io/name` of `wordpress` while it has
an instance name, represented as `app.kubernetes.io/instance` with a value of
`wordpress-abcxyz`. This enables the application and instance of the application
to be identifiable. Every instance of an application must have a unique name.

## Examples

To illustrate different ways to use these labels the following examples have varying complexity.

### A Simple Stateless Service

Consider the case for a simple stateless service deployed using `Deployment` and `Service` objects. The following two snippets represent how the labels could be used in their simplest form.

The `Deployment` is used to oversee the pods running the application itself.

```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app.kubernetes.io/name: myservice
    app.kubernetes.io/instance: myservice-abcxyz
...
```

The `Service` is used to expose the application.

```
apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/name: myservice
    app.kubernetes.io/instance: myservice-abcxyz
...
```

### Web Application With A Database

Consider a slightly more complicated application: a web application (WordPress)
using a database (MySQL), installed using Helm. The following snippets illustrate
the start of objects used to deploy this application.

The start to the following `Deployment` is used for WordPress:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app.kubernetes.io/name: wordpress
    app.kubernetes.io/instance: wordpress-abcxyz
    app.kubernetes.io/version: "4.9.4"
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: server
    app.kubernetes.io/part-of: wordpress
...
```

The `Service` is used to expose WordPress:

```
apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/name: wordpress
    app.kubernetes.io/instance: wordpress-abcxyz
    app.kubernetes.io/version: "4.9.4"
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: server
    app.kubernetes.io/part-of: wordpress
...
```

MySQL is exposed as a `StatefulSet` with metadata for both it and the larger application it belongs to:

```
apiVersion: apps/v1
kind: StatefulSet
metadata:
  labels:
    app.kubernetes.io/name: mysql
    app.kubernetes.io/instance: mysql-abcxyz
    app.kubernetes.io/version: "5.7.21"
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: database
    app.kubernetes.io/part-of: wordpress
...
```

The `Service` is used to expose MySQL as part of WordPress:

```
apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/name: mysql
    app.kubernetes.io/instance: mysql-abcxyz
    app.kubernetes.io/version: "5.7.21"
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: database
    app.kubernetes.io/part-of: wordpress
...
```

With the MySQL `StatefulSet` and `Service` you'll notice information about both MySQL and WordPress, the broader application, are included.

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
