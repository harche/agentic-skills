# SubjectAccessReview

SubjectAccessReview checks whether or not a user or group can perform an action.

`apiVersion: authorization.k8s.io/v1`

`import "k8s.io/api/authorization/v1"`

## SubjectAccessReview

SubjectAccessReview checks whether or not a user or group can perform an action.

---

* **apiVersion**: authorization.k8s.io/v1
* **kind**: SubjectAccessReview
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **spec** ([SubjectAccessReviewSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authorization-resources/subject-access-review-v1/#SubjectAccessReviewSpec)), required

  Spec holds information about the request being evaluated
* **status** ([SubjectAccessReviewStatus](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authorization-resources/subject-access-review-v1/#SubjectAccessReviewStatus))

  Status is filled in by the server and indicates whether the request is allowed or not

## SubjectAccessReviewSpec

SubjectAccessReviewSpec is a description of the access request. Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set

---

* **extra** (map[string][]string)

  Extra corresponds to the user.Info.GetExtra() method from the authenticator. Since that is input to the authorizer it needs a reflection here.
* **groups** ([]string)

  *Atomic: will be replaced during a merge*

  Groups is the groups you're testing for.
* **nonResourceAttributes** (NonResourceAttributes)

  NonResourceAttributes describes information for a non-resource access request

  *NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface*

  + **nonResourceAttributes.path** (string)

    Path is the URL path of the request
  + **nonResourceAttributes.verb** (string)

    Verb is the standard HTTP verb
* **resourceAttributes** (ResourceAttributes)

  ResourceAuthorizationAttributes describes information for a resource access request

  *ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface*

  + **resourceAttributes.fieldSelector** (FieldSelectorAttributes)

    fieldSelector describes the limitation on access based on field. It can only limit access, not broaden it.

    *FieldSelectorAttributes indicates a field limited access. Webhook authors are encouraged to * ensure rawSelector and requirements are not both set * consider the requirements field if set * not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the *SubjectAccessReview endpoints of the kube-apiserver: * If rawSelector is empty and requirements are empty, the request is not limited. * If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. * If rawSelector is empty and requirements are present, the requirements should be honored * If rawSelector is present and requirements are present, the request is invalid.*

    - **resourceAttributes.fieldSelector.rawSelector** (string)

      rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver's *SubjectAccessReview will parse the rawSelector as long as the requirements are not present.
    - **resourceAttributes.fieldSelector.requirements** ([]FieldSelectorRequirement)

      *Atomic: will be replaced during a merge*

      requirements is the parsed interpretation of a field selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood.

      *FieldSelectorRequirement is a selector that contains values, a key, and an operator that relates the key and values.*

      * **resourceAttributes.fieldSelector.requirements.key** (string), required

        key is the field selector key that the requirement applies to.
      * **resourceAttributes.fieldSelector.requirements.operator** (string), required

        operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. The list of operators may grow in the future.
      * **resourceAttributes.fieldSelector.requirements.values** ([]string)

        *Atomic: will be replaced during a merge*

        values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty.
  + **resourceAttributes.group** (string)

    Group is the API Group of the Resource. "*" means all.
  + **resourceAttributes.labelSelector** (LabelSelectorAttributes)

    labelSelector describes the limitation on access based on labels. It can only limit access, not broaden it.

    *LabelSelectorAttributes indicates a label limited access. Webhook authors are encouraged to * ensure rawSelector and requirements are not both set * consider the requirements field if set * not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the *SubjectAccessReview endpoints of the kube-apiserver: * If rawSelector is empty and requirements are empty, the request is not limited. * If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. * If rawSelector is empty and requirements are present, the requirements should be honored * If rawSelector is present and requirements are present, the request is invalid.*

    - **resourceAttributes.labelSelector.rawSelector** (string)

      rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver's *SubjectAccessReview will parse the rawSelector as long as the requirements are not present.
    - **resourceAttributes.labelSelector.requirements** ([]LabelSelectorRequirement)

      *Atomic: will be replaced during a merge*

      requirements is the parsed interpretation of a label selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood.

      *A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.*

      * **resourceAttributes.labelSelector.requirements.key** (string), required

        key is the label key that the selector applies to.
      * **resourceAttributes.labelSelector.requirements.operator** (string), required

        operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
      * **resourceAttributes.labelSelector.requirements.values** ([]string)

        *Atomic: will be replaced during a merge*

        values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
  + **resourceAttributes.name** (string)

    Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all.
  + **resourceAttributes.namespace** (string)

    Namespace is the namespace of the action being requested. Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview
  + **resourceAttributes.resource** (string)

    Resource is one of the existing resource types. "*" means all.
  + **resourceAttributes.subresource** (string)

    Subresource is one of the existing resource types. "" means none.
  + **resourceAttributes.verb** (string)

    Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy. "*" means all.
  + **resourceAttributes.version** (string)

    Version is the API Version of the Resource. "*" means all.
* **uid** (string)

  UID information about the requesting user.
* **user** (string)

  User is the user you're testing for. If you specify "User" but not "Groups", then is it interpreted as "What if User were not a member of any groups

## SubjectAccessReviewStatus

SubjectAccessReviewStatus

---

* **allowed** (boolean), required

  Allowed is required. True if the action would be allowed, false otherwise.
* **denied** (boolean)

  Denied is optional. True if the action would be denied, otherwise false. If both allowed is false and denied is false, then the authorizer has no opinion on whether to authorize the action. Denied may not be true if Allowed is true.
* **evaluationError** (string)

  EvaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request.
* **reason** (string)

  Reason is optional. It indicates why a request was allowed or denied.

## Operations

---

### `create` create a SubjectAccessReview

#### HTTP Request

POST /apis/authorization.k8s.io/v1/subjectaccessreviews

#### Parameters

* **body**: [SubjectAccessReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authorization-resources/subject-access-review-v1/#SubjectAccessReview), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([SubjectAccessReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authorization-resources/subject-access-review-v1/#SubjectAccessReview)): OK

201 ([SubjectAccessReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authorization-resources/subject-access-review-v1/#SubjectAccessReview)): Created

202 ([SubjectAccessReview](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authorization-resources/subject-access-review-v1/#SubjectAccessReview)): Accepted

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
