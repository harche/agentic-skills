# TokenRequest

TokenRequest requests a token for a given service account.

`apiVersion: authentication.k8s.io/v1`

`import "k8s.io/api/authentication/v1"`

## TokenRequest

TokenRequest requests a token for a given service account.

---

* **apiVersion**: authentication.k8s.io/v1
* **kind**: TokenRequest
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard object's metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **spec** ([TokenRequestSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-request-v1/#TokenRequestSpec)), required

  Spec holds information about the request being evaluated
* **status** ([TokenRequestStatus](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-request-v1/#TokenRequestStatus))

  Status is filled in by the server and indicates whether the token can be authenticated.

## TokenRequestSpec

TokenRequestSpec contains client provided parameters of a token request.

---

* **audiences** ([]string), required

  *Atomic: will be replaced during a merge*

  Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences.
* **boundObjectRef** (BoundObjectReference)

  BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation.

  *BoundObjectReference is a reference to an object that a token is bound to.*

  + **boundObjectRef.apiVersion** (string)

    API version of the referent.
  + **boundObjectRef.kind** (string)

    Kind of the referent. Valid kinds are 'Pod' and 'Secret'.
  + **boundObjectRef.name** (string)

    Name of the referent.
  + **boundObjectRef.uid** (string)

    UID of the referent.
* **expirationSeconds** (int64)

  ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response.

## TokenRequestStatus

TokenRequestStatus is the result of a token request.

---

* **expirationTimestamp** (Time), required

  ExpirationTimestamp is the time of expiration of the returned token.

  *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
* **token** (string), required

  Token is the opaque bearer token.

## Operations

---

### `create` create token of a ServiceAccount

#### HTTP Request

POST /api/v1/namespaces/{namespace}/serviceaccounts/{name}/token

#### Parameters

* **name** (*in path*): string, required

  name of the TokenRequest
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [TokenRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-request-v1/#TokenRequest), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([TokenRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-request-v1/#TokenRequest)): OK

201 ([TokenRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-request-v1/#TokenRequest)): Created

202 ([TokenRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-request-v1/#TokenRequest)): Accepted

401: Unauthorized

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
