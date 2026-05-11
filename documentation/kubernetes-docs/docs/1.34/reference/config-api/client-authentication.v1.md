# Client Authentication (v1)

## Resource Types

* [ExecCredential](#client-authentication-k8s-io-v1-ExecCredential)

## `ExecCredential`

ExecCredential is used by exec-based plugins to communicate credentials to
HTTP transports.

| Field | Description |
| --- | --- |
| `apiVersion` string | `client.authentication.k8s.io/v1` |
| `kind` string | `ExecCredential` |
| `spec` **[Required]**  [`ExecCredentialSpec`](#client-authentication-k8s-io-v1-ExecCredentialSpec) | Spec holds information passed to the plugin by the transport. |
| `status`  [`ExecCredentialStatus`](#client-authentication-k8s-io-v1-ExecCredentialStatus) | Status is filled in by the plugin and holds the credentials that the transport should use to contact the API. |

## `Cluster`

**Appears in:**

* [ExecCredentialSpec](#client-authentication-k8s-io-v1-ExecCredentialSpec)

Cluster contains information to allow an exec plugin to communicate
with the kubernetes cluster being authenticated to.

To ensure that this struct contains everything someone would need to communicate
with a kubernetes cluster (just like they would via a kubeconfig), the fields
should shadow "k8s.io/client-go/tools/clientcmd/api/v1".Cluster, with the exception
of CertificateAuthority, since CA data will always be passed to the plugin as bytes.

| Field | Description |
| --- | --- |
| `server` **[Required]**  `string` | Server is the address of the kubernetes cluster (https://hostname:port). |
| `tls-server-name`  `string` | TLSServerName is passed to the server for SNI and is used in the client to check server certificates against. If ServerName is empty, the hostname used to contact the server is used. |
| `insecure-skip-tls-verify`  `bool` | InsecureSkipTLSVerify skips the validity check for the server's certificate. This will make your HTTPS connections insecure. |
| `certificate-authority-data`  `[]byte` | CAData contains PEM-encoded certificate authority certificates. If empty, system roots should be used. |
| `proxy-url`  `string` | ProxyURL is the URL to the proxy to be used for all requests to this cluster. |
| `disable-compression`  `bool` | DisableCompression allows client to opt-out of response compression for all requests to the server. This is useful to speed up requests (specifically lists) when client-server network bandwidth is ample, by saving time on compression (server-side) and decompression (client-side): https://github.com/kubernetes/kubernetes/issues/112296. |
| `config`  [`k8s.io/apimachinery/pkg/runtime.RawExtension`](https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime/#RawExtension) | Config holds additional config data that is specific to the exec plugin with regards to the cluster being authenticated to.  This data is sourced from the clientcmd Cluster object's extensions[client.authentication.k8s.io/exec] field:  clusters:   * name: my-cluster   cluster:   ...   extensions:   + name: client.authentication.k8s.io/exec # reserved extension name for per cluster exec config     extension:     audience: 06e3fbd18de8 # arbitrary config   In some environments, the user config may be exactly the same across many clusters (i.e. call this exec plugin) minus some details that are specific to each cluster such as the audience. This field allows the per cluster config to be directly specified with the cluster info. Using this field to store secret data is not recommended as one of the prime benefits of exec plugins is that no secrets need to be stored directly in the kubeconfig. |

## `ExecCredentialSpec`

**Appears in:**

* [ExecCredential](#client-authentication-k8s-io-v1-ExecCredential)

ExecCredentialSpec holds request and runtime specific information provided by
the transport.

| Field | Description |
| --- | --- |
| `cluster`  [`Cluster`](#client-authentication-k8s-io-v1-Cluster) | Cluster contains information to allow an exec plugin to communicate with the kubernetes cluster being authenticated to. Note that Cluster is non-nil only when provideClusterInfo is set to true in the exec provider config (i.e., ExecConfig.ProvideClusterInfo). |
| `interactive` **[Required]**  `bool` | Interactive declares whether stdin has been passed to this exec plugin. |

## `ExecCredentialStatus`

**Appears in:**

* [ExecCredential](#client-authentication-k8s-io-v1-ExecCredential)

ExecCredentialStatus holds credentials for the transport to use.

Token and ClientKeyData are sensitive fields. This data should only be
transmitted in-memory between client and exec plugin process. Exec plugin
itself should at least be protected via file permissions.

| Field | Description |
| --- | --- |
| `expirationTimestamp`  [`meta/v1.Time`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#time-v1-meta) | ExpirationTimestamp indicates a time when the provided credentials expire. |
| `token` **[Required]**  `string` | Token is a bearer token used by the client for request authentication. |
| `clientCertificateData` **[Required]**  `string` | PEM-encoded client TLS certificates (including intermediates, if any). |
| `clientKeyData` **[Required]**  `string` | PEM-encoded private key for the above certificate. |

This page is automatically generated.

If you plan to report an issue with this page, mention that the page is auto-generated in your issue description. The fix may need to happen elsewhere in the Kubernetes project.

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
