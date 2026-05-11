# Pod Hostname

This page explains how to set a Pod's hostname,
potential side effects after configuration, and the underlying mechanics.

## Default Pod hostname

When a Pod is created, its hostname (as observed from within the Pod)
is derived from the Pod's metadata.name value.
Both the hostname and its corresponding fully qualified domain name (FQDN)
are set to the metadata.name value (from the Pod's perspective)

```
apiVersion: v1
kind: Pod
metadata:
  name: busybox-1
spec:
  containers:
  - image: busybox:1.28
    command:
      - sleep
      - "3600"
    name: busybox
```

The Pod created by this manifest will have its hostname and fully qualified domain name (FQDN) set to `busybox-1`.

## Hostname with pod's hostname and subdomain fields

The Pod spec includes an optional `hostname` field.
When set, this value takes precedence over the Pod's `metadata.name` as the
hostname (observed from within the Pod).
For example, a Pod with spec.hostname set to `my-host` will have its hostname set to `my-host`.

The Pod spec also includes an optional `subdomain` field,
indicating the Pod belongs to a subdomain within its namespace.
If a Pod has `spec.hostname` set to "foo" and spec.subdomain set
to "bar" in the namespace `my-namespace`, its hostname becomes `foo` and its
fully qualified domain name (FQDN) becomes
`foo.bar.my-namespace.svc.cluster-domain.example` (observed from within the Pod).

When both hostname and subdomain are set, the cluster's DNS server will
create A and/or AAAA records based on these fields.
Refer to: [Pod's hostname and subdomain fields](/docs/concepts/services-networking/dns-pod-service/#pod-hostname-and-subdomain-field).

## Hostname with pod's setHostnameAsFQDN fields

FEATURE STATE:
`Kubernetes v1.22 [stable]`

When a Pod is configured to have fully qualified domain name (FQDN), its
hostname is the short hostname. For example, if you have a Pod with the fully
qualified domain name `busybox-1.busybox-subdomain.my-namespace.svc.cluster-domain.example`,
then by default the `hostname` command inside that Pod returns `busybox-1` and the
`hostname --fqdn` command returns the FQDN.

When both `setHostnameAsFQDN: true` and the subdomain field is set in the Pod spec,
the kubelet writes the Pod's FQDN
into the hostname for that Pod's namespace. In this case, both `hostname` and `hostname --fqdn`
return the Pod's FQDN.

The Pod's FQDN is constructed in the same manner as previously defined.
It is composed of the Pod's `spec.hostname` (if specified) or `metadata.name` field,
the `spec.subdomain`, the `namespace` name, and the cluster domain suffix.

> **Note:**
> In Linux, the hostname field of the kernel (the `nodename` field of `struct utsname`) is limited to 64 characters.
>
> If a Pod enables this feature and its FQDN is longer than 64 character, it will fail to start.
> The Pod will remain in `Pending` status (`ContainerCreating` as seen by `kubectl`) generating
> error events, such as "Failed to construct FQDN from Pod hostname and cluster domain".
>
> This means that when using this field,
> you must ensure the combined length of the Pod's `metadata.name` (or `spec.hostname`)
> and `spec.subdomain` fields results in an FQDN that does not exceed 64 characters.

## Hostname with pod's hostnameOverride

FEATURE STATE:
`Kubernetes v1.34 [alpha]`(disabled by default)

Setting a value for `hostnameOverride` in the Pod spec causes the kubelet
to unconditionally set both the Pod's hostname and fully qualified domain name (FQDN)
to the `hostnameOverride` value.

The `hostnameOverride` field has a length limitation of 64 characters
and must adhere to the DNS subdomain names standard defined in [RFC 1123](https://datatracker.ietf.org/doc/html/rfc1123).

Example:

```
apiVersion: v1
kind: Pod
metadata:
  name: busybox-2-busybox-example-domain
spec:
  hostnameOverride: busybox-2.busybox.example.domain
  containers:
  - image: busybox:1.28
    command:
      - sleep
      - "3600"
    name: busybox
```

> **Note:**
> This only affects the hostname within the Pod; it does not affect the Pod's A or AAAA records in the cluster DNS server.

If `hostnameOverride` is set alongside `hostname` and `subdomain` fields:

* The hostname inside the Pod is overridden to the `hostnameOverride` value.
* The Pod's A and/or AAAA records in the cluster DNS server are still generated based on the `hostname` and `subdomain` fields.

Note: If `hostnameOverride` is set, you cannot simultaneously set the `hostNetwork` and `setHostnameAsFQDN` fields.
The API server will explicitly reject any create request attempting this combination.

For details on behavior when `hostnameOverride` is set in combination with
other fields (hostname, subdomain, setHostnameAsFQDN, hostNetwork),
see the table in the [KEP-4762 design details](https://github.com/kubernetes/enhancements/blob/master/keps/sig-network/4762-allow-arbitrary-fqdn-as-pod-hostname/README.md#design-details).

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
