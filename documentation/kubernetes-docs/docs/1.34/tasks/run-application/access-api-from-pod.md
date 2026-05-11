# Accessing the Kubernetes API from a Pod

This guide demonstrates how to access the Kubernetes API from within a pod.

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

## Accessing the API from within a Pod

When accessing the API from within a Pod, locating and authenticating
to the API server are slightly different to the external client case.

The easiest way to use the Kubernetes API from a Pod is to use
one of the official [client libraries](/docs/reference/using-api/client-libraries/). These
libraries can automatically discover the API server and authenticate.

### Using Official Client Libraries

From within a Pod, the recommended ways to connect to the Kubernetes API are:

* For a Go client, use the official
  [Go client library](https://github.com/kubernetes/client-go/).
  The `rest.InClusterConfig()` function handles API host discovery and authentication automatically.
  See [an example here](https://git.k8s.io/client-go/examples/in-cluster-client-configuration/main.go).
* For a Python client, use the official
  [Python client library](https://github.com/kubernetes-client/python/).
  The `config.load_incluster_config()` function handles API host discovery and authentication automatically.
  See [an example here](https://github.com/kubernetes-client/python/blob/master/examples/in_cluster_config.py).
* There are a number of other libraries available, please refer to the
  [Client Libraries](/docs/reference/using-api/client-libraries/) page.

In each case, the service account credentials of the Pod are used to communicate
securely with the API server.

### Directly accessing the REST API

While running in a Pod, your container can create an HTTPS URL for the Kubernetes API
server by fetching the `KUBERNETES_SERVICE_HOST` and `KUBERNETES_SERVICE_PORT_HTTPS`
environment variables. The API server's in-cluster address is also published to a
Service named `kubernetes` in the `default` namespace so that pods may reference
`kubernetes.default.svc` as a DNS name for the local API server.

> **Note:**
> Kubernetes does not guarantee that the API server has a valid certificate for
> the hostname `kubernetes.default.svc`;
> however, the control plane **is** expected to present a valid certificate for the
> hostname or IP address that `$KUBERNETES_SERVICE_HOST` represents.

The recommended way to authenticate to the API server is with a
[service account](/docs/tasks/configure-pod-container/configure-service-account/)
credential. By default, a Pod
is associated with a service account, and a credential (token) for that
service account is placed into the filesystem tree of each container in that Pod,
at `/var/run/secrets/kubernetes.io/serviceaccount/token`.

If available, a certificate bundle is placed into the filesystem tree of each
container at `/var/run/secrets/kubernetes.io/serviceaccount/ca.crt`, and should be
used to verify the serving certificate of the API server.

Finally, the default namespace to be used for namespaced API operations is placed in a file
at `/var/run/secrets/kubernetes.io/serviceaccount/namespace` in each container.

### Using kubectl proxy

If you would like to query the API without an official client library, you can run `kubectl proxy`
as the [command](/docs/tasks/inject-data-application/define-command-argument-container/)
of a new sidecar container in the Pod. This way, `kubectl proxy` will authenticate
to the API and expose it on the `localhost` interface of the Pod, so that other containers
in the Pod can use it directly.

### Without using a proxy

It is possible to avoid using the kubectl proxy by passing the authentication token
directly to the API server. The internal certificate secures the connection.

```
# Point to the internal API server hostname
APISERVER=https://kubernetes.default.svc

# Path to ServiceAccount token
SERVICEACCOUNT=/var/run/secrets/kubernetes.io/serviceaccount

# Read this Pod's namespace
NAMESPACE=$(cat ${SERVICEACCOUNT}/namespace)

# Read the ServiceAccount bearer token
TOKEN=$(cat ${SERVICEACCOUNT}/token)

# Reference the internal certificate authority (CA)
CACERT=${SERVICEACCOUNT}/ca.crt

# Explore the API with TOKEN
curl --cacert ${CACERT} --header "Authorization: Bearer ${TOKEN}" -X GET ${APISERVER}/api
```

The output will be similar to this:

```
{
  "kind": "APIVersions",
  "versions": ["v1"],
  "serverAddressByClientCIDRs": [
    {
      "clientCIDR": "0.0.0.0/0",
      "serverAddress": "10.0.1.149:443"
    }
  ]
}
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
