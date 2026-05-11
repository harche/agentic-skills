# Kubelet CredentialProvider (v1)

## Resource Types

* [CredentialProviderRequest](#credentialprovider-kubelet-k8s-io-v1-CredentialProviderRequest)
* [CredentialProviderResponse](#credentialprovider-kubelet-k8s-io-v1-CredentialProviderResponse)

## `CredentialProviderRequest`

CredentialProviderRequest includes the image that the kubelet requires authentication for.
Kubelet will pass this request object to the plugin via stdin. In general, plugins should
prefer responding with the same apiVersion they were sent.

| Field | Description |
| --- | --- |
| `apiVersion` string | `credentialprovider.kubelet.k8s.io/v1` |
| `kind` string | `CredentialProviderRequest` |
| `image` **[Required]**  `string` | image is the container image that is being pulled as part of the credential provider plugin request. Plugins may optionally parse the image to extract any information required to fetch credentials. |
| `serviceAccountToken` **[Required]**  `string` | serviceAccountToken is the service account token bound to the pod for which the image is being pulled. This token is only sent to the plugin if the tokenAttributes.serviceAccountTokenAudience field is configured in the kubelet's credential provider configuration. |
| `serviceAccountAnnotations` **[Required]**  `map[string]string` | serviceAccountAnnotations is a map of annotations on the service account bound to the pod for which the image is being pulled. The list of annotations in the service account that need to be passed to the plugin is configured in the kubelet's credential provider configuration. |

## `CredentialProviderResponse`

CredentialProviderResponse holds credentials that the kubelet should use for the specified
image provided in the original request. Kubelet will read the response from the plugin via stdout.
This response should be set to the same apiVersion as CredentialProviderRequest.

| Field | Description |
| --- | --- |
| `apiVersion` string | `credentialprovider.kubelet.k8s.io/v1` |
| `kind` string | `CredentialProviderResponse` |
| `cacheKeyType` **[Required]**  [`PluginCacheKeyType`](#credentialprovider-kubelet-k8s-io-v1-PluginCacheKeyType) | cacheKeyType indicates the type of caching key to use based on the image provided in the request. There are three valid values for the cache key type: Image, Registry, and Global. If an invalid value is specified, the response will NOT be used by the kubelet. |
| `cacheDuration`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | cacheDuration indicates the duration the provided credentials should be cached for. The kubelet will use this field to set the in-memory cache duration for credentials in the AuthConfig. If null, the kubelet will use defaultCacheDuration provided in CredentialProviderConfig. If set to 0, the kubelet will not cache the provided AuthConfig. |
| `auth`  [`map[string]AuthConfig`](#credentialprovider-kubelet-k8s-io-v1-AuthConfig) | auth is a map containing authentication information passed into the kubelet. Each key is a match image string (more on this below). The corresponding authConfig value should be valid for all images that match against this key. A plugin should set this field to null if no valid credentials can be returned for the requested image.  Each key in the map is a pattern which can optionally contain a port and a path. Globs can be used in the domain, but not in the port or the path. Globs are supported as subdomains like '*.k8s.io' or 'k8s.*.io', and top-level-domains such as 'k8s.*'. Matching partial subdomains like 'app*.k8s.io' is also supported. Each glob can only match a single subdomain segment, so *.io does not match *.k8s.io.  The kubelet will match images against the key when all of the below are true:   * Both contain the same number of domain parts and each part matches. * The URL path of an imageMatch must be a prefix of the target image URL path. * If the imageMatch contains a port, then the port must match in the image as well.   When multiple keys are returned, the kubelet will traverse all keys in reverse order so that:   * longer keys come before shorter keys with the same prefix * non-wildcard keys come before wildcard keys with the same prefix.   For any given match, the kubelet will attempt an image pull with the provided credentials, stopping after the first successfully authenticated pull.  Example keys:   * 123456789.dkr.ecr.us-east-1.amazonaws.com * *.azurecr.io * gcr.io * *.*.registry.io * registry.io:8080/path |

## `AuthConfig`

**Appears in:**

* [CredentialProviderResponse](#credentialprovider-kubelet-k8s-io-v1-CredentialProviderResponse)

AuthConfig contains authentication information for a container registry.
Only username/password based authentication is supported today, but more authentication
mechanisms may be added in the future.

| Field | Description |
| --- | --- |
| `username` **[Required]**  `string` | username is the username used for authenticating to the container registry An empty username is valid. |
| `password` **[Required]**  `string` | password is the password used for authenticating to the container registry An empty password is valid. |

## `PluginCacheKeyType`

(Alias of `string`)

**Appears in:**

* [CredentialProviderResponse](#credentialprovider-kubelet-k8s-io-v1-CredentialProviderResponse)

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
