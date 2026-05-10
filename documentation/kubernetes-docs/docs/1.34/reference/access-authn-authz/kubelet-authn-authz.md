# Kubelet authentication/authorization

## Overview

A kubelet's HTTPS endpoint exposes APIs which give access to data of varying sensitivity,
and allow you to perform operations with varying levels of power on the node and within containers.

This document describes how to authenticate and authorize access to the kubelet's HTTPS endpoint.

## Kubelet authentication

By default, requests to the kubelet's HTTPS endpoint that are not rejected by other configured
authentication methods are treated as anonymous requests, and given a username of `system:anonymous`
and a group of `system:unauthenticated`.

To disable anonymous access and send `401 Unauthorized` responses to unauthenticated requests:

* start the kubelet with the `--anonymous-auth=false` flag

To enable X509 client certificate authentication to the kubelet's HTTPS endpoint:

* start the kubelet with the `--client-ca-file` flag, providing a CA bundle to verify client certificates with
* start the apiserver with `--kubelet-client-certificate` and `--kubelet-client-key` flags
* see the [apiserver authentication documentation](/docs/reference/access-authn-authz/authentication/#x509-client-certificates) for more details

To enable API bearer tokens (including service account tokens) to be used to authenticate to the kubelet's HTTPS endpoint:

* ensure the `authentication.k8s.io/v1beta1` API group is enabled in the API server
* start the kubelet with the `--authentication-token-webhook` and `--kubeconfig` flags
* the kubelet calls the `TokenReview` API on the configured API server to determine user information from bearer tokens

## Kubelet authorization

Any request that is successfully authenticated (including an anonymous request) is then authorized. The default authorization mode is `AlwaysAllow`, which allows all requests.

There are many possible reasons to subdivide access to the kubelet API:

* anonymous auth is enabled, but anonymous users' ability to call the kubelet API should be limited
* bearer token auth is enabled, but arbitrary API users' (like service accounts) ability to call the kubelet API should be limited
* client certificate auth is enabled, but only some of the client certificates signed by the configured CA should be allowed to use the kubelet API

To subdivide access to the kubelet API, delegate authorization to the API server:

* ensure the `authorization.k8s.io/v1beta1` API group is enabled in the API server
* start the kubelet with the `--authorization-mode=Webhook` and the `--kubeconfig` flags
* the kubelet calls the `SubjectAccessReview` API on the configured API server to determine whether each request is authorized

The kubelet authorizes API requests using the same [request attributes](/docs/reference/access-authn-authz/authorization/#review-your-request-attributes) approach as the apiserver.

The verb is determined from the incoming request's HTTP verb:

| HTTP verb | request verb |
| --- | --- |
| POST | create |
| GET, HEAD | get |
| PUT | update |
| PATCH | patch |
| DELETE | delete |

The resource and subresource is determined from the incoming request's path:

| Kubelet API | resource | subresource |
| --- | --- | --- |
| /stats/* | nodes | stats |
| /metrics/* | nodes | metrics |
| /logs/* | nodes | log |
| /spec/* | nodes | spec |
| /checkpoint/* | nodes | checkpoint |
| *all others* | nodes | proxy |

The namespace and API group attributes are always an empty string, and
the resource name is always the name of the kubelet's `Node` API object.

When running in this mode, ensure the user identified by the `--kubelet-client-certificate` and `--kubelet-client-key`
flags passed to the apiserver is authorized for the following attributes:

* verb=*, resource=nodes, subresource=proxy
* verb=*, resource=nodes, subresource=stats
* verb=*, resource=nodes, subresource=log
* verb=*, resource=nodes, subresource=spec
* verb=*, resource=nodes, subresource=metrics

### Fine-grained authorization

FEATURE STATE:
`Kubernetes v1.33 [beta]`(enabled by default)

When the feature gate `KubeletFineGrainedAuthz` is enabled kubelet performs a
fine-grained check before falling back to the `proxy` subresource for the `/pods`,
`/runningPods`, `/configz` and `/healthz` endpoints. The resource and subresource
are determined from the incoming request's path:

| Kubelet API | resource | subresource |
| --- | --- | --- |
| /stats/* | nodes | stats |
| /metrics/* | nodes | metrics |
| /logs/* | nodes | log |
| /pods | nodes | pods, proxy |
| /runningPods/ | nodes | pods, proxy |
| /healthz | nodes | healthz, proxy |
| /configz | nodes | configz, proxy |
| *all others* | nodes | proxy |

When the feature-gate `KubeletFineGrainedAuthz` is enabled, ensure the user
identified by the `--kubelet-client-certificate` and `--kubelet-client-key`
flags passed to the API server is authorized for the following attributes:

* verb=*, resource=nodes, subresource=proxy
* verb=*, resource=nodes, subresource=stats
* verb=*, resource=nodes, subresource=log
* verb=*, resource=nodes, subresource=metrics
* verb=*, resource=nodes, subresource=configz
* verb=*, resource=nodes, subresource=healthz
* verb=*, resource=nodes, subresource=pods

If [RBAC authorization](/docs/reference/access-authn-authz/rbac/) is used,
enabling this gate also ensure that the builtin `system:kubelet-api-admin` ClusterRole
is updated with permissions to access all the above mentioned subresources.

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
