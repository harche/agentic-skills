# kube-apiserver Audit Configuration (v1)

## Resource Types

* [Event](#audit-k8s-io-v1-Event)
* [EventList](#audit-k8s-io-v1-EventList)
* [Policy](#audit-k8s-io-v1-Policy)
* [PolicyList](#audit-k8s-io-v1-PolicyList)

## `Event`

**Appears in:**

* [EventList](#audit-k8s-io-v1-EventList)

Event captures all the information that can be included in an API audit log.

| Field | Description |
| --- | --- |
| `apiVersion` string | `audit.k8s.io/v1` |
| `kind` string | `Event` |
| `level` **[Required]**  [`Level`](#audit-k8s-io-v1-Level) | AuditLevel at which event was generated |
| `auditID` **[Required]**  [`k8s.io/apimachinery/pkg/types.UID`](https://pkg.go.dev/k8s.io/apimachinery/pkg/types#UID) | Unique audit ID, generated for each request. |
| `stage` **[Required]**  [`Stage`](#audit-k8s-io-v1-Stage) | Stage of the request handling when this event instance was generated. |
| `requestURI` **[Required]**  `string` | RequestURI is the request URI as sent by the client to a server. |
| `verb` **[Required]**  `string` | Verb is the kubernetes verb associated with the request. For non-resource requests, this is the lower-cased HTTP method. |
| `user` **[Required]**  [`authentication/v1.UserInfo`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#userinfo-v1-authentication-k8s-io) | Authenticated user information. |
| `impersonatedUser`  [`authentication/v1.UserInfo`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#userinfo-v1-authentication-k8s-io) | Impersonated user information. |
| `sourceIPs`  `[]string` | Source IPs, from where the request originated and intermediate proxies. The source IPs are listed from (in order):   1. X-Forwarded-For request header IPs 2. X-Real-Ip header, if not present in the X-Forwarded-For list 3. The remote address for the connection, if it doesn't match the last    IP in the list up to here (X-Forwarded-For or X-Real-Ip).    Note: All but the last IP can be arbitrarily set by the client. |
| `userAgent`  `string` | UserAgent records the user agent string reported by the client. Note that the UserAgent is provided by the client, and must not be trusted. |
| `objectRef`  [`ObjectReference`](#audit-k8s-io-v1-ObjectReference) | Object reference this request is targeted at. Does not apply for List-type requests, or non-resource requests. |
| `responseStatus`  [`meta/v1.Status`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#status-v1-meta) | The response status, populated even when the ResponseObject is not a Status type. For successful responses, this will only include the Code and StatusSuccess. For non-status type error responses, this will be auto-populated with the error Message. |
| `requestObject`  [`k8s.io/apimachinery/pkg/runtime.Unknown`](https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime#Unknown) | API object from the request, in JSON format. The RequestObject is recorded as-is in the request (possibly re-encoded as JSON), prior to version conversion, defaulting, admission or merging. It is an external versioned object type, and may not be a valid object on its own. Omitted for non-resource requests. Only logged at Request Level and higher. |
| `responseObject`  [`k8s.io/apimachinery/pkg/runtime.Unknown`](https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime#Unknown) | API object returned in the response, in JSON. The ResponseObject is recorded after conversion to the external type, and serialized as JSON. Omitted for non-resource requests. Only logged at Response Level. |
| `requestReceivedTimestamp`  [`meta/v1.MicroTime`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#microtime-v1-meta) | Time the request reached the apiserver. |
| `stageTimestamp`  [`meta/v1.MicroTime`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#microtime-v1-meta) | Time the request reached current audit stage. |
| `annotations`  `map[string]string` | Annotations is an unstructured key value map stored with an audit event that may be set by plugins invoked in the request serving chain, including authentication, authorization and admission plugins. Note that these annotations are for the audit event, and do not correspond to the metadata.annotations of the submitted object. Keys should uniquely identify the informing component to avoid name collisions (e.g. podsecuritypolicy.admission.k8s.io/policy). Values should be short. Annotations are included in the Metadata level. |

## `EventList`

EventList is a list of audit Events.

| Field | Description |
| --- | --- |
| `apiVersion` string | `audit.k8s.io/v1` |
| `kind` string | `EventList` |
| `metadata`  [`meta/v1.ListMeta`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#listmeta-v1-meta) | No description provided. |
| `items` **[Required]**  [`[]Event`](#audit-k8s-io-v1-Event) | No description provided. |

## `Policy`

**Appears in:**

* [PolicyList](#audit-k8s-io-v1-PolicyList)

Policy defines the configuration of audit logging, and the rules for how different request
categories are logged.

| Field | Description |
| --- | --- |
| `apiVersion` string | `audit.k8s.io/v1` |
| `kind` string | `Policy` |
| `metadata`  [`meta/v1.ObjectMeta`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#objectmeta-v1-meta) | ObjectMeta is included for interoperability with API infrastructure. Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `rules` **[Required]**  [`[]PolicyRule`](#audit-k8s-io-v1-PolicyRule) | Rules specify the audit Level a request should be recorded at. A request may match multiple rules, in which case the FIRST matching rule is used. The default audit level is None, but can be overridden by a catch-all rule at the end of the list. PolicyRules are strictly ordered. |
| `omitStages`  [`[]Stage`](#audit-k8s-io-v1-Stage) | OmitStages is a list of stages for which no events are created. Note that this can also be specified per rule in which case the union of both are omitted. |
| `omitManagedFields`  `bool` | OmitManagedFields indicates whether to omit the managed fields of the request and response bodies from being written to the API audit log. This is used as a global default - a value of 'true' will omit the managed fields, otherwise the managed fields will be included in the API audit log. Note that this can also be specified per rule in which case the value specified in a rule will override the global default. |

## `PolicyList`

PolicyList is a list of audit Policies.

| Field | Description |
| --- | --- |
| `apiVersion` string | `audit.k8s.io/v1` |
| `kind` string | `PolicyList` |
| `metadata`  [`meta/v1.ListMeta`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#listmeta-v1-meta) | No description provided. |
| `items` **[Required]**  [`[]Policy`](#audit-k8s-io-v1-Policy) | No description provided. |

## `GroupResources`

**Appears in:**

* [PolicyRule](#audit-k8s-io-v1-PolicyRule)

GroupResources represents resource kinds in an API group.

| Field | Description |
| --- | --- |
| `group`  `string` | Group is the name of the API group that contains the resources. The empty string represents the core API group. |
| `resources`  `[]string` | Resources is a list of resources this rule applies to.  For example:   * `pods` matches pods. * `pods/log` matches the log subresource of pods. * `*` matches all resources and their subresources. * `pods/*` matches all subresources of pods. * `*/scale` matches all scale subresources.   If wildcard is present, the validation rule will ensure resources do not overlap with each other.  An empty list implies all resources and subresources in this API groups apply. |
| `resourceNames`  `[]string` | ResourceNames is a list of resource instance names that the policy matches. Using this field requires Resources to be specified. An empty list implies that every instance of the resource is matched. |

## `Level`

(Alias of `string`)

**Appears in:**

* [Event](#audit-k8s-io-v1-Event)
* [PolicyRule](#audit-k8s-io-v1-PolicyRule)

Level defines the amount of information logged during auditing

## `ObjectReference`

**Appears in:**

* [Event](#audit-k8s-io-v1-Event)

ObjectReference contains enough information to let you inspect or modify the referred object.

| Field | Description |
| --- | --- |
| `resource`  `string` | No description provided. |
| `namespace`  `string` | No description provided. |
| `name`  `string` | No description provided. |
| `uid`  [`k8s.io/apimachinery/pkg/types.UID`](https://pkg.go.dev/k8s.io/apimachinery/pkg/types#UID) | No description provided. |
| `apiGroup`  `string` | APIGroup is the name of the API group that contains the referred object. The empty string represents the core API group. |
| `apiVersion`  `string` | APIVersion is the version of the API group that contains the referred object. |
| `resourceVersion`  `string` | No description provided. |
| `subresource`  `string` | No description provided. |

## `PolicyRule`

**Appears in:**

* [Policy](#audit-k8s-io-v1-Policy)

PolicyRule maps requests based off metadata to an audit Level.
Requests must match the rules of every field (an intersection of rules).

| Field | Description |
| --- | --- |
| `level` **[Required]**  [`Level`](#audit-k8s-io-v1-Level) | The Level that requests matching this rule are recorded at. |
| `users`  `[]string` | The users (by authenticated user name) this rule applies to. An empty list implies every user. |
| `userGroups`  `[]string` | The user groups this rule applies to. A user is considered matching if it is a member of any of the UserGroups. An empty list implies every user group. |
| `verbs`  `[]string` | The verbs that match this rule. An empty list implies every verb. |
| `resources`  [`[]GroupResources`](#audit-k8s-io-v1-GroupResources) | Resources that this rule matches. An empty list implies all kinds in all API groups. |
| `namespaces`  `[]string` | Namespaces that this rule matches. The empty string "" matches non-namespaced resources. An empty list implies every namespace. |
| `nonResourceURLs`  `[]string` | NonResourceURLs is a set of URL paths that should be audited. `*`s are allowed, but only as the full, final step in the path. Examples:   * `/metrics` - Log requests for apiserver metrics * `/healthz*` - Log all health checks |
| `omitStages`  [`[]Stage`](#audit-k8s-io-v1-Stage) | OmitStages is a list of stages for which no events are created. Note that this can also be specified policy wide in which case the union of both are omitted. An empty list means no restrictions will apply. |
| `omitManagedFields`  `bool` | OmitManagedFields indicates whether to omit the managed fields of the request and response bodies from being written to the API audit log.   * a value of 'true' will drop the managed fields from the API audit log * a value of 'false' indicates that the managed fields should be included   in the API audit log   Note that the value, if specified, in this rule will override the global default   If a value is not specified then the global default specified in   Policy.OmitManagedFields will stand. |

## `Stage`

(Alias of `string`)

**Appears in:**

* [Event](#audit-k8s-io-v1-Event)
* [Policy](#audit-k8s-io-v1-Policy)
* [PolicyRule](#audit-k8s-io-v1-PolicyRule)

Stage defines the stages in request handling that audit events may be generated.

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
