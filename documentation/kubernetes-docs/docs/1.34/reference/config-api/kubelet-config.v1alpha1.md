# Kubelet Configuration (v1alpha1)

## Resource Types

* [CredentialProviderConfig](#kubelet-config-k8s-io-v1alpha1-CredentialProviderConfig)
* [ImagePullIntent](#kubelet-config-k8s-io-v1alpha1-ImagePullIntent)
* [ImagePulledRecord](#kubelet-config-k8s-io-v1alpha1-ImagePulledRecord)

## `CredentialProviderConfig`

CredentialProviderConfig is the configuration containing information about
each exec credential provider. Kubelet reads this configuration from disk and enables
each provider as specified by the CredentialProvider type.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubelet.config.k8s.io/v1alpha1` |
| `kind` string | `CredentialProviderConfig` |
| `providers` **[Required]**  [`[]CredentialProvider`](#kubelet-config-k8s-io-v1alpha1-CredentialProvider) | providers is a list of credential provider plugins that will be enabled by the kubelet. Multiple providers may match against a single image, in which case credentials from all providers will be returned to the kubelet. If multiple providers are called for a single image, the results are combined. If providers return overlapping auth keys, the value from the provider earlier in this list is attempted first. |

## `ImagePullIntent`

ImagePullIntent is a record of the kubelet attempting to pull an image.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubelet.config.k8s.io/v1alpha1` |
| `kind` string | `ImagePullIntent` |
| `image` **[Required]**  `string` | Image is the image spec from a Container's `image` field. The filename is a SHA-256 hash of this value. This is to avoid filename-unsafe characters like ':' and '/'. |

## `ImagePulledRecord`

ImagePullRecord is a record of an image that was pulled by the kubelet.

If there are no records in the `kubernetesSecrets` field and both `nodeWideCredentials`
and `anonymous` are `false`, credentials must be re-checked the next time an
image represented by this record is being requested.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubelet.config.k8s.io/v1alpha1` |
| `kind` string | `ImagePulledRecord` |
| `lastUpdatedTime` **[Required]**  [`meta/v1.Time`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#time-v1-meta) | LastUpdatedTime is the time of the last update to this record |
| `imageRef` **[Required]**  `string` | ImageRef is a reference to the image represented by this file as received from the CRI. The filename is a SHA-256 hash of this value. This is to avoid filename-unsafe characters like ':' and '/'. |
| `credentialMapping` **[Required]**  [`map[string]ImagePullCredentials`](#kubelet-config-k8s-io-v1alpha1-ImagePullCredentials) | CredentialMapping maps `image` to the set of credentials that it was previously pulled with. `image` in this case is the content of a pod's container `image` field that's got its tag/digest removed.  Example: Container requests the `hello-world:latest@sha256:91fb4b041da273d5a3273b6d587d62d518300a6ad268b28628f74997b93171b2` image: "credentialMapping": { "hello-world": { "nodePodsAccessible": true } } |

## `CredentialProvider`

**Appears in:**

* [CredentialProviderConfig](#kubelet-config-k8s-io-v1alpha1-CredentialProviderConfig)

CredentialProvider represents an exec plugin to be invoked by the kubelet. The plugin is only
invoked when an image being pulled matches the images handled by the plugin (see matchImages).

| Field | Description |
| --- | --- |
| `name` **[Required]**  `string` | name is the required name of the credential provider. It must match the name of the provider executable as seen by the kubelet. The executable must be in the kubelet's bin directory (set by the --image-credential-provider-bin-dir flag). Required to be unique across all providers. |
| `matchImages` **[Required]**  `[]string` | matchImages is a required list of strings used to match against images in order to determine if this provider should be invoked. If one of the strings matches the requested image from the kubelet, the plugin will be invoked and given a chance to provide credentials. Images are expected to contain the registry domain and URL path.  Each entry in matchImages is a pattern which can optionally contain a port and a path. Globs can be used in the domain, but not in the port or the path. Globs are supported as subdomains like `*.k8s.io` or `k8s.*.io`, and top-level-domains such as `k8s.*`. Matching partial subdomains like `app*.k8s.io` is also supported. Each glob can only match a single subdomain segment, so `*.io` does not match `*.k8s.io`.  A match exists between an image and a matchImage when all of the below are true:   * Both contain the same number of domain parts and each part matches. * The URL path of an imageMatch must be a prefix of the target image URL path. * If the imageMatch contains a port, then the port must match in the image as well.   Example values of matchImages:   * `123456789.dkr.ecr.us-east-1.amazonaws.com` * `*.azurecr.io` * `gcr.io` * `*.*.registry.io` * `registry.io:8080/path` |
| `defaultCacheDuration` **[Required]**  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | defaultCacheDuration is the default duration the plugin will cache credentials in-memory if a cache duration is not provided in the plugin response. This field is required. |
| `apiVersion` **[Required]**  `string` | Required input version of the exec CredentialProviderRequest. The returned CredentialProviderResponse MUST use the same encoding version as the input. Current supported values are:   * credentialprovider.kubelet.k8s.io/v1alpha1 |
| `args`  `[]string` | Arguments to pass to the command when executing it. |
| `env`  [`[]ExecEnvVar`](#kubelet-config-k8s-io-v1alpha1-ExecEnvVar) | Env defines additional environment variables to expose to the process. These are unioned with the host's environment, as well as variables client-go uses to pass argument to the plugin. |

## `ExecEnvVar`

**Appears in:**

* [CredentialProvider](#kubelet-config-k8s-io-v1alpha1-CredentialProvider)

ExecEnvVar is used for setting environment variables when executing an exec-based
credential plugin.

| Field | Description |
| --- | --- |
| `name` **[Required]**  `string` | No description provided. |
| `value` **[Required]**  `string` | No description provided. |

## `ImagePullCredentials`

**Appears in:**

* [ImagePulledRecord](#kubelet-config-k8s-io-v1alpha1-ImagePulledRecord)

ImagePullCredentials describe credentials that can be used to pull an image.

| Field | Description |
| --- | --- |
| `kubernetesSecrets`  [`[]ImagePullSecret`](#kubelet-config-k8s-io-v1alpha1-ImagePullSecret) | KuberneteSecretCoordinates is an index of coordinates of all the kubernetes secrets that were used to pull the image. |
| `kubernetesServiceAccounts`  [`[]ImagePullServiceAccount`](#kubelet-config-k8s-io-v1alpha1-ImagePullServiceAccount) | KubernetesServiceAccounts is an index of coordinates of all the kubernetes service accounts that were used to pull the image. |
| `nodePodsAccessible`  `bool` | NodePodsAccessible is a flag denoting the pull credentials are accessible by all the pods on the node, or that no credentials are needed for the pull.  If true, it is mutually exclusive with the `kubernetesSecrets` field. |

## `ImagePullSecret`

**Appears in:**

* [ImagePullCredentials](#kubelet-config-k8s-io-v1alpha1-ImagePullCredentials)

ImagePullSecret is a representation of a Kubernetes secret object coordinates along
with a credential hash of the pull secret credentials this object contains.

| Field | Description |
| --- | --- |
| `uid` **[Required]**  `string` | No description provided. |
| `namespace` **[Required]**  `string` | No description provided. |
| `name` **[Required]**  `string` | No description provided. |
| `credentialHash` **[Required]**  `string` | CredentialHash is a SHA-256 retrieved by hashing the image pull credentials content of the secret specified by the UID/Namespace/Name coordinates. |

## `ImagePullServiceAccount`

**Appears in:**

* [ImagePullCredentials](#kubelet-config-k8s-io-v1alpha1-ImagePullCredentials)

ImagePullServiceAccount is a representation of a Kubernetes service account object coordinates
for which the kubelet sent service account token to the credential provider plugin for image pull credentials.

| Field | Description |
| --- | --- |
| `uid` **[Required]**  `string` | No description provided. |
| `namespace` **[Required]**  `string` | No description provided. |
| `name` **[Required]**  `string` | No description provided. |

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
