# FlowSchema

FlowSchema defines the schema of a group of flows.

`apiVersion: flowcontrol.apiserver.k8s.io/v1`

`import "k8s.io/api/flowcontrol/v1"`

## FlowSchema

FlowSchema defines the schema of a group of flows. Note that a flow is made up of a set of inbound API requests with similar attributes and is identified by a pair of strings: the name of the FlowSchema and a "flow distinguisher".

---

* **apiVersion**: flowcontrol.apiserver.k8s.io/v1
* **kind**: FlowSchema
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  `metadata` is the standard object's metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **spec** ([FlowSchemaSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchemaSpec))

  `spec` is the specification of the desired behavior of a FlowSchema. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>
* **status** ([FlowSchemaStatus](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchemaStatus))

  `status` is the current status of a FlowSchema. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>

## FlowSchemaSpec

FlowSchemaSpec describes how the FlowSchema's specification looks like.

---

* **distinguisherMethod** (FlowDistinguisherMethod)

  `distinguisherMethod` defines how to compute the flow distinguisher for requests that match this schema. `nil` specifies that the distinguisher is disabled and thus will always be the empty string.

  *FlowDistinguisherMethod specifies the method of a flow distinguisher.*

  + **distinguisherMethod.type** (string), required

    `type` is the type of flow distinguisher method The supported types are "ByUser" and "ByNamespace". Required.
* **matchingPrecedence** (int32)

  `matchingPrecedence` is used to choose among the FlowSchemas that match a given request. The chosen FlowSchema is among those with the numerically lowest (which we take to be logically highest) MatchingPrecedence. Each MatchingPrecedence value must be ranged in [1,10000]. Note that if the precedence is not specified, it will be set to 1000 as default.
* **priorityLevelConfiguration** (PriorityLevelConfigurationReference), required

  `priorityLevelConfiguration` should reference a PriorityLevelConfiguration in the cluster. If the reference cannot be resolved, the FlowSchema will be ignored and marked as invalid in its status. Required.

  *PriorityLevelConfigurationReference contains information that points to the "request-priority" being used.*

  + **priorityLevelConfiguration.name** (string), required

    `name` is the name of the priority level configuration being referenced Required.
* **rules** ([]PolicyRulesWithSubjects)

  *Atomic: will be replaced during a merge*

  `rules` describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema.

  *PolicyRulesWithSubjects prescribes a test that applies to a request to an apiserver. The test considers the subject making the request, the verb being requested, and the resource to be acted upon. This PolicyRulesWithSubjects matches a request if and only if both (a) at least one member of subjects matches the request and (b) at least one member of resourceRules or nonResourceRules matches the request.*

  + **rules.subjects** ([]Subject), required

    *Atomic: will be replaced during a merge*

    subjects is the list of normal user, serviceaccount, or group that this rule cares about. There must be at least one member in this slice. A slice that includes both the system:authenticated and system:unauthenticated user groups matches every request. Required.

    *Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account.*

    - **rules.subjects.kind** (string), required

      `kind` indicates which one of the other fields is non-empty. Required
    - **rules.subjects.group** (GroupSubject)

      `group` matches based on user group name.

      *GroupSubject holds detailed information for group-kind subject.*

      * **rules.subjects.group.name** (string), required

        name is the user group that matches, or "*" to match all user groups. See <https://github.com/kubernetes/apiserver/blob/master/pkg/authentication/user/user.go> for some well-known group names. Required.
    - **rules.subjects.serviceAccount** (ServiceAccountSubject)

      `serviceAccount` matches ServiceAccounts.

      *ServiceAccountSubject holds detailed information for service-account-kind subject.*

      * **rules.subjects.serviceAccount.name** (string), required

        `name` is the name of matching ServiceAccount objects, or "*" to match regardless of name. Required.
      * **rules.subjects.serviceAccount.namespace** (string), required

        `namespace` is the namespace of matching ServiceAccount objects. Required.
    - **rules.subjects.user** (UserSubject)

      `user` matches based on username.

      *UserSubject holds detailed information for user-kind subject.*

      * **rules.subjects.user.name** (string), required

        `name` is the username that matches, or "*" to match all usernames. Required.
  + **rules.nonResourceRules** ([]NonResourcePolicyRule)

    *Atomic: will be replaced during a merge*

    `nonResourceRules` is a list of NonResourcePolicyRules that identify matching requests according to their verb and the target non-resource URL.

    *NonResourcePolicyRule is a predicate that matches non-resource requests according to their verb and the target non-resource URL. A NonResourcePolicyRule matches a request if and only if both (a) at least one member of verbs matches the request and (b) at least one member of nonResourceURLs matches the request.*

    - **rules.nonResourceRules.nonResourceURLs** ([]string), required

      *Set: unique values will be kept during a merge*

      `nonResourceURLs` is a set of url prefixes that a user should have access to and may not be empty. For example:

      * "/healthz" is legal
      * "/hea*" is illegal
      * "/hea" is legal but matches nothing
      * "/hea/*" also matches nothing
      * "/healthz/*" matches all per-component health checks.
        "*" matches all non-resource urls. if it is present, it must be the only entry. Required.
    - **rules.nonResourceRules.verbs** ([]string), required

      *Set: unique values will be kept during a merge*

      `verbs` is a list of matching verbs and may not be empty. "*" matches all verbs. If it is present, it must be the only entry. Required.
  + **rules.resourceRules** ([]ResourcePolicyRule)

    *Atomic: will be replaced during a merge*

    `resourceRules` is a slice of ResourcePolicyRules that identify matching requests according to their verb and the target resource. At least one of `resourceRules` and `nonResourceRules` has to be non-empty.

    *ResourcePolicyRule is a predicate that matches some resource requests, testing the request's verb and the target resource. A ResourcePolicyRule matches a resource request if and only if: (a) at least one member of verbs matches the request, (b) at least one member of apiGroups matches the request, (c) at least one member of resources matches the request, and (d) either (d1) the request does not specify a namespace (i.e., `Namespace==""`) and clusterScope is true or (d2) the request specifies a namespace and least one member of namespaces matches the request's namespace.*

    - **rules.resourceRules.apiGroups** ([]string), required

      *Set: unique values will be kept during a merge*

      `apiGroups` is a list of matching API groups and may not be empty. "*" matches all API groups and, if present, must be the only entry. Required.
    - **rules.resourceRules.resources** ([]string), required

      *Set: unique values will be kept during a merge*

      `resources` is a list of matching resources (i.e., lowercase and plural) with, if desired, subresource. For example, [ "services", "nodes/status" ]. This list may not be empty. "*" matches all resources and, if present, must be the only entry. Required.
    - **rules.resourceRules.verbs** ([]string), required

      *Set: unique values will be kept during a merge*

      `verbs` is a list of matching verbs and may not be empty. "*" matches all verbs and, if present, must be the only entry. Required.
    - **rules.resourceRules.clusterScope** (boolean)

      `clusterScope` indicates whether to match requests that do not specify a namespace (which happens either because the resource is not namespaced or the request targets all namespaces). If this field is omitted or false then the `namespaces` field must contain a non-empty list.
    - **rules.resourceRules.namespaces** ([]string)

      *Set: unique values will be kept during a merge*

      `namespaces` is a list of target namespaces that restricts matches. A request that specifies a target namespace matches only if either (a) this list contains that target namespace or (b) this list contains "*". Note that "*" matches any specified namespace but does not match a request that *does not specify* a namespace (see the `clusterScope` field for that). This list may be empty, but only if `clusterScope` is true.

## FlowSchemaStatus

FlowSchemaStatus represents the current state of a FlowSchema.

---

* **conditions** ([]FlowSchemaCondition)

  *Patch strategy: merge on key `type`*

  *Map: unique values on key type will be kept during a merge*

  `conditions` is a list of the current states of FlowSchema.

  *FlowSchemaCondition describes conditions for a FlowSchema.*

  + **conditions.lastTransitionTime** (Time)

    `lastTransitionTime` is the last time the condition transitioned from one status to another.

    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
  + **conditions.message** (string)

    `message` is a human-readable message indicating details about last transition.
  + **conditions.reason** (string)

    `reason` is a unique, one-word, CamelCase reason for the condition's last transition.
  + **conditions.status** (string)

    `status` is the status of the condition. Can be True, False, Unknown. Required.
  + **conditions.type** (string)

    `type` is the type of the condition. Required.

## FlowSchemaList

FlowSchemaList is a list of FlowSchema objects.

---

* **apiVersion**: flowcontrol.apiserver.k8s.io/v1
* **kind**: FlowSchemaList
* **metadata** ([ListMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/#ListMeta))

  `metadata` is the standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **items** ([][FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema)), required

  `items` is a list of FlowSchemas.

## Operations

---

### `get` read the specified FlowSchema

#### HTTP Request

GET /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the FlowSchema
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema)): OK

401: Unauthorized

### `get` read status of the specified FlowSchema

#### HTTP Request

GET /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the FlowSchema
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema)): OK

401: Unauthorized

### `list` list or watch objects of kind FlowSchema

#### HTTP Request

GET /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas

#### Parameters

* **allowWatchBookmarks** (*in query*): boolean

  [allowWatchBookmarks](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#allowWatchBookmarks)
* **continue** (*in query*): string

  [continue](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#continue)
* **fieldSelector** (*in query*): string

  [fieldSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldSelector)
* **labelSelector** (*in query*): string

  [labelSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#labelSelector)
* **limit** (*in query*): integer

  [limit](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#limit)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)
* **resourceVersion** (*in query*): string

  [resourceVersion](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#resourceVersion)
* **resourceVersionMatch** (*in query*): string

  [resourceVersionMatch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#resourceVersionMatch)
* **sendInitialEvents** (*in query*): boolean

  [sendInitialEvents](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#sendInitialEvents)
* **timeoutSeconds** (*in query*): integer

  [timeoutSeconds](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#timeoutSeconds)
* **watch** (*in query*): boolean

  [watch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#watch)

#### Response

200 ([FlowSchemaList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchemaList)): OK

401: Unauthorized

### `create` create a FlowSchema

#### HTTP Request

POST /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas

#### Parameters

* **body**: [FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema)): OK

201 ([FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema)): Created

202 ([FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema)): Accepted

401: Unauthorized

### `update` replace the specified FlowSchema

#### HTTP Request

PUT /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the FlowSchema
* **body**: [FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema)): OK

201 ([FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema)): Created

401: Unauthorized

### `update` replace status of the specified FlowSchema

#### HTTP Request

PUT /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the FlowSchema
* **body**: [FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema)): OK

201 ([FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema)): Created

401: Unauthorized

### `patch` partially update the specified FlowSchema

#### HTTP Request

PATCH /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the FlowSchema
* **body**: [Patch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/patch/#Patch), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **force** (*in query*): boolean

  [force](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#force)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema)): OK

201 ([FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema)): Created

401: Unauthorized

### `patch` partially update status of the specified FlowSchema

#### HTTP Request

PATCH /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the FlowSchema
* **body**: [Patch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/patch/#Patch), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **force** (*in query*): boolean

  [force](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#force)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema)): OK

201 ([FlowSchema](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/#FlowSchema)): Created

401: Unauthorized

### `delete` delete a FlowSchema

#### HTTP Request

DELETE /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the FlowSchema
* **body**: [DeleteOptions](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/delete-options/#DeleteOptions)
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **gracePeriodSeconds** (*in query*): integer

  [gracePeriodSeconds](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#gracePeriodSeconds)
* **ignoreStoreReadErrorWithClusterBreakingPotential** (*in query*): boolean

  [ignoreStoreReadErrorWithClusterBreakingPotential](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#ignoreStoreReadErrorWithClusterBreakingPotential)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)
* **propagationPolicy** (*in query*): string

  [propagationPolicy](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#propagationPolicy)

#### Response

200 ([Status](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/status/#Status)): OK

202 ([Status](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/status/#Status)): Accepted

401: Unauthorized

### `deletecollection` delete collection of FlowSchema

#### HTTP Request

DELETE /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas

#### Parameters

* **body**: [DeleteOptions](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/delete-options/#DeleteOptions)
* **continue** (*in query*): string

  [continue](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#continue)
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldSelector** (*in query*): string

  [fieldSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldSelector)
* **gracePeriodSeconds** (*in query*): integer

  [gracePeriodSeconds](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#gracePeriodSeconds)
* **ignoreStoreReadErrorWithClusterBreakingPotential** (*in query*): boolean

  [ignoreStoreReadErrorWithClusterBreakingPotential](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#ignoreStoreReadErrorWithClusterBreakingPotential)
* **labelSelector** (*in query*): string

  [labelSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#labelSelector)
* **limit** (*in query*): integer

  [limit](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#limit)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)
* **propagationPolicy** (*in query*): string

  [propagationPolicy](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#propagationPolicy)
* **resourceVersion** (*in query*): string

  [resourceVersion](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#resourceVersion)
* **resourceVersionMatch** (*in query*): string

  [resourceVersionMatch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#resourceVersionMatch)
* **sendInitialEvents** (*in query*): boolean

  [sendInitialEvents](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#sendInitialEvents)
* **timeoutSeconds** (*in query*): integer

  [timeoutSeconds](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#timeoutSeconds)

#### Response

200 ([Status](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/status/#Status)): OK

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
