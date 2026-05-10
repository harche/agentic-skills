# Mixed Version Proxy

FEATURE STATE:
`Kubernetes v1.28 [alpha]`(disabled by default)

Kubernetes 1.34 includes an alpha feature that lets an
[API Server](/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API.")
proxy a resource requests to other *peer* API servers. This is useful when there are multiple
API servers running different versions of Kubernetes in one cluster
(for example, during a long-lived rollout to a new release of Kubernetes).

This enables cluster administrators to configure highly available clusters that can be upgraded
more safely, by directing resource requests (made during the upgrade) to the correct kube-apiserver.
That proxying prevents users from seeing unexpected 404 Not Found errors that stem
from the upgrade process.

This mechanism is called the *Mixed Version Proxy*.

## Enabling the Mixed Version Proxy

Ensure that `UnknownVersionInteroperabilityProxy` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/)
is enabled when you start the [API Server](/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API."):

```
kube-apiserver \
--feature-gates=UnknownVersionInteroperabilityProxy=true \
# required command line arguments for this feature
--peer-ca-file=<path to kube-apiserver CA cert>
--proxy-client-cert-file=<path to aggregator proxy cert>,
--proxy-client-key-file=<path to aggregator proxy key>,
--requestheader-client-ca-file=<path to aggregator CA cert>,
# requestheader-allowed-names can be set to blank to allow any Common Name
--requestheader-allowed-names=<valid Common Names to verify proxy client cert against>,

# optional flags for this feature
--peer-advertise-ip=`IP of this kube-apiserver that should be used by peers to proxy requests`
--peer-advertise-port=`port of this kube-apiserver that should be used by peers to proxy requests`

# …and other flags as usual
```

### Proxy transport and authentication between API servers

* The source kube-apiserver reuses the
  [existing APIserver client authentication flags](/docs/tasks/extend-kubernetes/configure-aggregation-layer/#kubernetes-apiserver-client-authentication)
  `--proxy-client-cert-file` and `--proxy-client-key-file` to present its identity that
  will be verified by its peer (the destination kube-apiserver). The destination API server
  verifies that peer connection based on the configuration you specify using the
  `--requestheader-client-ca-file` command line argument.
* To authenticate the destination server's serving certs, you must configure a certificate
  authority bundle by specifying the `--peer-ca-file` command line argument to the **source** API server.

### Configuration for peer API server connectivity

To set the network location of a kube-apiserver that peers will use to proxy requests, use the
`--peer-advertise-ip` and `--peer-advertise-port` command line arguments to kube-apiserver or specify
these fields in the API server configuration file.
If these flags are unspecified, peers will use the value from either `--advertise-address` or
`--bind-address` command line argument to the kube-apiserver.
If those too, are unset, the host's default interface is used.

## Mixed version proxying

When you enable mixed version proxying, the [aggregation layer](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)
loads a special filter that does the following:

* When a resource request reaches an API server that cannot serve that API
  (either because it is at a version pre-dating the introduction of the API or the API is turned off on the API server)
  the API server attempts to send the request to a peer API server that can serve the requested API.
  It does so by identifying API groups / versions / resources that the local server doesn't recognise,
  and tries to proxy those requests to a peer API server that is capable of handling the request.
* If the peer API server fails to respond, the *source* API server responds with 503 ("Service Unavailable") error.

### How it works under the hood

When an API Server receives a resource request, it first checks which API servers can
serve the requested resource. This check happens using the internal
[`StorageVersion` API](/docs/reference/generated/kubernetes-api/v1.34/#storageversioncondition-v1alpha1-internal-apiserver-k8s-io).

* If the resource is known to the API server that received the request
  (for example, `GET /api/v1/pods/some-pod`), the request is handled locally.
* If there is no internal `StorageVersion` object found for the requested resource
  (for example, `GET /my-api/v1/my-resource`) and the configured APIService specifies proxying
  to an extension API server, that proxying happens following the usual
  [flow](/docs/tasks/extend-kubernetes/configure-aggregation-layer/) for extension APIs.
* If a valid internal `StorageVersion` object is found for the requested resource
  (for example, `GET /batch/v1/jobs`) and the API server trying to handle the request
  (the *handling API server*) has the `batch` API disabled, then the *handling API server*
  fetches the peer API servers that do serve the relevant API group / version / resource
  (`api/v1/batch` in this case) using the information in the fetched `StorageVersion` object.
  The *handling API server* then proxies the request to one of the matching peer kube-apiservers
  that are aware of the requested resource.

  + If there is no peer known for that API group / version / resource, the handling API server
    passes the request to its own handler chain which should eventually return a 404 ("Not Found") response.
  + If the handling API server has identified and selected a peer API server, but that peer fails
    to respond (for reasons such as network connectivity issues, or a data race between the request
    being received and a controller registering the peer's info into the control plane), then the handling
    API server responds with a 503 ("Service Unavailable") error.

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
