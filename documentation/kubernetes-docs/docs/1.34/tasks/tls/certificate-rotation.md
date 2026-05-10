# Configure Certificate Rotation for the Kubelet

This page shows how to enable and configure certificate rotation for the kubelet.

FEATURE STATE:
`Kubernetes v1.19 [stable]`

## Before you begin

* Kubernetes version 1.8.0 or later is required

## Overview

The kubelet uses certificates for authenticating to the Kubernetes API. By
default, these certificates are issued with one year expiration so that they do
not need to be renewed too frequently.

Kubernetes contains [kubelet certificate
rotation](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/),
that will automatically generate a new key and request a new certificate from
the Kubernetes API as the current certificate approaches expiration. Once the
new certificate is available, it will be used for authenticating connections to
the Kubernetes API.

## Enabling client certificate rotation

The `kubelet` process accepts an argument `--rotate-certificates` that controls
if the kubelet will automatically request a new certificate as the expiration of
the certificate currently in use approaches.

The `kube-controller-manager` process accepts an argument
`--cluster-signing-duration` (`--experimental-cluster-signing-duration` prior to 1.19)
that controls how long certificates will be issued for.

## Understanding the certificate rotation configuration

When a kubelet starts up, if it is configured to bootstrap (using the
`--bootstrap-kubeconfig` flag), it will use its initial certificate to connect
to the Kubernetes API and issue a certificate signing request. You can view the
status of certificate signing requests using:

```
kubectl get csr
```

Initially a certificate signing request from the kubelet on a node will have a
status of `Pending`. If the certificate signing requests meets specific
criteria, it will be auto approved by the controller manager, then it will have
a status of `Approved`. Next, the controller manager will sign a certificate,
issued for the duration specified by the
`--cluster-signing-duration` parameter, and the signed certificate
will be attached to the certificate signing request.

The kubelet will retrieve the signed certificate from the Kubernetes API and
write that to disk, in the location specified by `--cert-dir`. Then the kubelet
will use the new certificate to connect to the Kubernetes API.

As the expiration of the signed certificate approaches, the kubelet will
automatically issue a new certificate signing request, using the Kubernetes API.
This can happen at any point between 30% and 10% of the time remaining on the
certificate. Again, the controller manager will automatically approve the certificate
request and attach a signed certificate to the certificate signing request. The
kubelet will retrieve the new signed certificate from the Kubernetes API and
write that to disk. Then it will update the connections it has to the
Kubernetes API to reconnect using the new certificate.

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
