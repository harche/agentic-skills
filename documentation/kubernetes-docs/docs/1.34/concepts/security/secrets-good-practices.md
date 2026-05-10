# Good practices for Kubernetes Secrets

Principles and practices for good Secret management for cluster administrators and application developers.

In Kubernetes, a Secret is an object that stores sensitive information, such as passwords, OAuth tokens, and SSH keys.

Secrets give you more control over how sensitive information is used and reduces
the risk of accidental exposure. Secret values are encoded as base64 strings and
are stored unencrypted by default, but can be configured to be
[encrypted at rest](/docs/tasks/administer-cluster/encrypt-data/#ensure-all-secrets-are-encrypted).

A [Pod](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") can reference the Secret in
a variety of ways, such as in a volume mount or as an environment variable.
Secrets are designed for confidential data and
[ConfigMaps](/docs/tasks/configure-pod-container/configure-pod-configmap/) are
designed for non-confidential data.

The following good practices are intended for both cluster administrators and
application developers. Use these guidelines to improve the security of your
sensitive information in Secret objects, as well as to more effectively manage
your Secrets.

## Cluster administrators

This section provides good practices that cluster administrators can use to
improve the security of confidential information in the cluster.

### Configure encryption at rest

By default, Secret objects are stored unencrypted in [etcd](/docs/tasks/administer-cluster/configure-upgrade-etcd/ "Consistent and highly-available key value store used as backing store of Kubernetes for all cluster data."). You should configure encryption of your Secret
data in `etcd`. For instructions, refer to
[Encrypt Secret Data at Rest](/docs/tasks/administer-cluster/encrypt-data/).

### Configure least-privilege access to Secrets

When planning your access control mechanism, such as Kubernetes
[Role-based Access Control](/docs/reference/access-authn-authz/rbac/ "Manages authorization decisions, allowing admins to dynamically configure access policies through the Kubernetes API.") [(RBAC)](/docs/reference/access-authn-authz/rbac/),
consider the following guidelines for access to `Secret` objects. You should
also follow the other guidelines in
[RBAC good practices](/docs/concepts/security/rbac-good-practices/).

* **Components**: Restrict `watch` or `list` access to only the most
  privileged, system-level components. Only grant `get` access for Secrets if
  the component's normal behavior requires it.
* **Humans**: Restrict `get`, `watch`, or `list` access to Secrets. Only allow
  cluster administrators to access `etcd`. This includes read-only access. For
  more complex access control, such as restricting access to Secrets with
  specific annotations, consider using third-party authorization mechanisms.

> **Caution:**
> Granting `list` access to Secrets implicitly lets the subject fetch the
> contents of the Secrets.

A user who can create a Pod that uses a Secret can also see the value of that
Secret. Even if cluster policies do not allow a user to read the Secret
directly, the same user could have access to run a Pod that then exposes the
Secret. You can detect or limit the impact caused by Secret data being exposed,
either intentionally or unintentionally, by a user with this access. Some
recommendations include:

* Use short-lived Secrets
* Implement audit rules that alert on specific events, such as concurrent
  reading of multiple Secrets by a single user

#### Restrict Access for Secrets

Use separate namespaces to isolate access to mounted secrets.

### Improve etcd management policies

Consider wiping or shredding the durable storage used by `etcd` once it is
no longer in use.

If there are multiple `etcd` instances, configure encrypted SSL/TLS
communication between the instances to protect the Secret data in transit.

### Configure access to external Secrets

> **Note:**
> **Note:** This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](/docs/contribute/style/content-guide/#third-party-content) before submitting a change. [More information.](#third-party-content-disclaimer)

You can use third-party Secrets store providers to keep your confidential data
outside your cluster and then configure Pods to access that information.
The [Kubernetes Secrets Store CSI Driver](https://secrets-store-csi-driver.sigs.k8s.io/)
is a DaemonSet that lets the kubelet retrieve Secrets from external stores, and
mount the Secrets as a volume into specific Pods that you authorize to access
the data.

For a list of supported providers, refer to
[Providers for the Secret Store CSI Driver](https://secrets-store-csi-driver.sigs.k8s.io/concepts.html#provider-for-the-secrets-store-csi-driver).

## Good practices for using swap memory

For best practices for setting swap memory for Linux nodes, please refer to
[swap memory management](/docs/concepts/cluster-administration/swap-memory-management/#good-practice-for-using-swap-in-a-kubernetes-cluster).

## Developers

This section provides good practices for developers to use to improve the
security of confidential data when building and deploying Kubernetes resources.

### Restrict Secret access to specific containers

If you are defining multiple containers in a Pod, and only one of those
containers needs access to a Secret, define the volume mount or environment
variable configuration so that the other containers do not have access to that
Secret.

### Protect Secret data after reading

Applications still need to protect the value of confidential information after
reading it from an environment variable or volume. For example, your
application must avoid logging the secret data in the clear or transmitting it
to an untrusted party.

### Avoid sharing Secret manifests

If you configure a Secret through a
[manifest](/docs/reference/glossary/?all=true#term-manifest "A serialized specification of one or more Kubernetes API objects."), with the secret
data encoded as base64, sharing this file or checking it in to a source
repository means the secret is available to everyone who can read the manifest.

> **Caution:**
> Base64 encoding is *not* an encryption method, it provides no additional
> confidentiality over plain text.

Items on this page refer to third party products or projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for those third-party products or projects. See the [CNCF website guidelines](https://github.com/cncf/foundation/blob/master/website-guidelines.md) for more details.

You should read the [content guide](/docs/contribute/style/content-guide/#third-party-content) before proposing a change that adds an extra third-party link.

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
