# TokenReview

TokenReview attempts to authenticate a token to a known user.

`apiVersion: authentication.k8s.io/v1`

`import "k8s.io/api/authentication/v1"`

## TokenReview

TokenReview attempts to authenticate a token to a known user. Note: TokenReview requests may be cached by the webhook token authenticator plugin in the kube-apiserver.

---

* **apiVersion**: authentication.k8s.io/v1
* **kind**: TokenReview
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard object's metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **spec** ([TokenReviewSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-review-v1/#TokenReviewSpec)), required

  Spec holds information about the request being evaluated
* **status** ([TokenReviewStatus](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-review-v1/#TokenReviewStatus))

  Status is filled in by the server and indicates whether the request can be authenticated.

## TokenReviewSpec

TokenReviewSpec is a description of the token authentication request.

---

* **audiences** ([]string)

  *Atomic: will be replaced during a merge*

  Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver.
* **token** (string)

  Token is the opaque bearer token.

## TokenReviewStatus

TokenReviewStatus is the result of the token authentication request.

---

* **audiences** ([]string)

  *Atomic: will be replaced during a merge*

  Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token's audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is "true", the token is valid against the audience of the Kubernetes API server.
* **authenticated** (boolean)

  Authenticated indicates that the token was associated with a known user.
* **error** (string)

  Error indicates that the token couldn't be checked
* **user** (UserInfo)

  User is the UserInfo associated with the provided token.

  *UserInfo holds the information about the user needed to implement the user.Info interface.*

  + **user.extra** (map[string][]string)

    Any additional information provided by the authenticator.
  + **user.groups** ([]string)

    *Atomic: will be replaced during a merge*

    The names of groups this user is a part of.
  + **user.uid** (string)

    A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs.
  + **user.username** (string)

    The name that uniquely identifies this user among all active users.

## Operations

---

### `create` create a TokenReview

#### HTTP Request

POST /apis/authentication.k8s.io/v1/tokenreviews

#### Parameters

* **body**: [TokenReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-review-v1/#TokenReview), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([TokenReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-review-v1/#TokenReview)): OK

201 ([TokenReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-review-v1/#TokenReview)): Created

202 ([TokenReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-review-v1/#TokenReview)): Accepted

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
