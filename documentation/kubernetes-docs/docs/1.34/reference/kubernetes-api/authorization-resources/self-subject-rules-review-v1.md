# SelfSubjectRulesReview

SelfSubjectRulesReview enumerates the set of actions the current user can perform within a namespace.

`apiVersion: authorization.k8s.io/v1`

`import "k8s.io/api/authorization/v1"`

## SelfSubjectRulesReview

SelfSubjectRulesReview enumerates the set of actions the current user can perform within a namespace. The returned list of actions may be incomplete depending on the server's authorization mode, and any errors experienced during the evaluation. SelfSubjectRulesReview should be used by UIs to show/hide actions, or to quickly let an end user reason about their permissions. It should NOT Be used by external systems to drive authorization decisions as this raises confused deputy, cache lifetime/revocation, and correctness concerns. SubjectAccessReview, and LocalAccessReview are the correct way to defer authorization decisions to the API server.

---

* **apiVersion**: authorization.k8s.io/v1
* **kind**: SelfSubjectRulesReview
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **spec** ([SelfSubjectRulesReviewSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authorization-resources/self-subject-rules-review-v1/#SelfSubjectRulesReviewSpec)), required

  Spec holds information about the request being evaluated.
* **status** (SubjectRulesReviewStatus)

  Status is filled in by the server and indicates the set of actions a user can perform.

  *SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending on the set of authorizers the server is configured with and any errors experienced during evaluation. Because authorization rules are additive, if a rule appears in a list it's safe to assume the subject has that permission, even if that list is incomplete.*

  + **status.incomplete** (boolean), required

    Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn't support rules evaluation.
  + **status.nonResourceRules** ([]NonResourceRule), required

    *Atomic: will be replaced during a merge*

    NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.

    *NonResourceRule holds information that describes a rule for the non-resource*

    - **status.nonResourceRules.verbs** ([]string), required

      *Atomic: will be replaced during a merge*

      Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options. "*" means all.
    - **status.nonResourceRules.nonResourceURLs** ([]string)

      *Atomic: will be replaced during a merge*

      NonResourceURLs is a set of partial urls that a user should have access to. *s are allowed, but only as the full, final step in the path. "*" means all.
  + **status.resourceRules** ([]ResourceRule), required

    *Atomic: will be replaced during a merge*

    ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.

    *ResourceRule is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.*

    - **status.resourceRules.verbs** ([]string), required

      *Atomic: will be replaced during a merge*

      Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy. "*" means all.
    - **status.resourceRules.apiGroups** ([]string)

      *Atomic: will be replaced during a merge*

      APIGroups is the name of the APIGroup that contains the resources. If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "*" means all.
    - **status.resourceRules.resourceNames** ([]string)

      *Atomic: will be replaced during a merge*

      ResourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed. "*" means all.
    - **status.resourceRules.resources** ([]string)

      *Atomic: will be replaced during a merge*

      Resources is a list of resources this rule applies to. "*" means all in the specified apiGroups.
      "*/foo" represents the subresource 'foo' for all resources in the specified apiGroups.
  + **status.evaluationError** (string)

    EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn't support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete.

## SelfSubjectRulesReviewSpec

SelfSubjectRulesReviewSpec defines the specification for SelfSubjectRulesReview.

---

* **namespace** (string)

  Namespace to evaluate rules for. Required.

## Operations

---

### `create` create a SelfSubjectRulesReview

#### HTTP Request

POST /apis/authorization.k8s.io/v1/selfsubjectrulesreviews

#### Parameters

* **body**: [SelfSubjectRulesReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authorization-resources/self-subject-rules-review-v1/#SelfSubjectRulesReview), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([SelfSubjectRulesReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authorization-resources/self-subject-rules-review-v1/#SelfSubjectRulesReview)): OK

201 ([SelfSubjectRulesReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authorization-resources/self-subject-rules-review-v1/#SelfSubjectRulesReview)): Created

202 ([SelfSubjectRulesReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authorization-resources/self-subject-rules-review-v1/#SelfSubjectRulesReview)): Accepted

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
