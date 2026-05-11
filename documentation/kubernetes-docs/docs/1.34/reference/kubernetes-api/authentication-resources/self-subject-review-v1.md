# SelfSubjectReview

SelfSubjectReview contains the user information that the kube-apiserver has about the user making this request.

`apiVersion: authentication.k8s.io/v1`

`import "k8s.io/api/authentication/v1"`

## SelfSubjectReview

SelfSubjectReview contains the user information that the kube-apiserver has about the user making this request. When using impersonation, users will receive the user info of the user being impersonated. If impersonation or request header authentication is used, any extra keys will have their case ignored and returned as lowercase.

---

* **apiVersion**: authentication.k8s.io/v1
* **kind**: SelfSubjectReview
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard object's metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **status** ([SelfSubjectReviewStatus](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/self-subject-review-v1/#SelfSubjectReviewStatus))

  Status is filled in by the server with the user attributes.

## SelfSubjectReviewStatus

SelfSubjectReviewStatus is filled by the kube-apiserver and sent back to a user.

---

* **userInfo** (UserInfo)

  User attributes of the user making this request.

  *UserInfo holds the information about the user needed to implement the user.Info interface.*

  + **userInfo.extra** (map[string][]string)

    Any additional information provided by the authenticator.
  + **userInfo.groups** ([]string)

    *Atomic: will be replaced during a merge*

    The names of groups this user is a part of.
  + **userInfo.uid** (string)

    A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs.
  + **userInfo.username** (string)

    The name that uniquely identifies this user among all active users.

## Operations

---

### `create` create a SelfSubjectReview

#### HTTP Request

POST /apis/authentication.k8s.io/v1/selfsubjectreviews

#### Parameters

* **body**: [SelfSubjectReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/self-subject-review-v1/#SelfSubjectReview), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([SelfSubjectReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/self-subject-review-v1/#SelfSubjectReview)): OK

201 ([SelfSubjectReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/self-subject-review-v1/#SelfSubjectReview)): Created

202 ([SelfSubjectReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/self-subject-review-v1/#SelfSubjectReview)): Accepted

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
