# kube-apiserver Configuration (v1beta1)

Package v1beta1 is the v1beta1 version of the API.

## Resource Types

* [AuthenticationConfiguration](#apiserver-k8s-io-v1beta1-AuthenticationConfiguration)
* [AuthorizationConfiguration](#apiserver-k8s-io-v1beta1-AuthorizationConfiguration)
* [EgressSelectorConfiguration](#apiserver-k8s-io-v1beta1-EgressSelectorConfiguration)
* [TracingConfiguration](#apiserver-k8s-io-v1beta1-TracingConfiguration)

## `TracingConfiguration`

**Appears in:**

* [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)
* [TracingConfiguration](#apiserver-k8s-io-v1alpha1-TracingConfiguration)
* [TracingConfiguration](#apiserver-k8s-io-v1beta1-TracingConfiguration)

TracingConfiguration provides versioned configuration for OpenTelemetry tracing clients.

| Field | Description |
| --- | --- |
| `endpoint`  `string` | Endpoint of the collector this component will report traces to. The connection is insecure, and does not currently support TLS. Recommended is unset, and endpoint is the otlp grpc default, localhost:4317. |
| `samplingRatePerMillion`  `int32` | SamplingRatePerMillion is the number of samples to collect per million spans. Recommended is unset. If unset, sampler respects its parent span's sampling rate, but otherwise never samples. |

## `AuthenticationConfiguration`

AuthenticationConfiguration provides versioned configuration for authentication.

| Field | Description |
| --- | --- |
| `apiVersion` string | `apiserver.k8s.io/v1beta1` |
| `kind` string | `AuthenticationConfiguration` |
| `jwt` **[Required]**  [`[]JWTAuthenticator`](#apiserver-k8s-io-v1beta1-JWTAuthenticator) | jwt is a list of authenticator to authenticate Kubernetes users using JWT compliant tokens. The authenticator will attempt to parse a raw ID token, verify it's been signed by the configured issuer. The public key to verify the signature is discovered from the issuer's public endpoint using OIDC discovery. For an incoming token, each JWT authenticator will be attempted in the order in which it is specified in this list. Note however that other authenticators may run before or after the JWT authenticators. The specific position of JWT authenticators in relation to other authenticators is neither defined nor stable across releases. Since each JWT authenticator must have a unique issuer URL, at most one JWT authenticator will attempt to cryptographically validate the token.  The minimum valid JWT payload must contain the following claims: { "iss": "https://issuer.example.com", "aud": ["audience"], "exp": 1234567890, "": "username" } |
| `anonymous` **[Required]**  [`AnonymousAuthConfig`](#apiserver-k8s-io-v1beta1-AnonymousAuthConfig) | If present --anonymous-auth must not be set |

## `AuthorizationConfiguration`

| Field | Description |
| --- | --- |
| `apiVersion` string | `apiserver.k8s.io/v1beta1` |
| `kind` string | `AuthorizationConfiguration` |
| `authorizers` **[Required]**  [`[]AuthorizerConfiguration`](#apiserver-k8s-io-v1beta1-AuthorizerConfiguration) | Authorizers is an ordered list of authorizers to authorize requests against. This is similar to the --authorization-modes kube-apiserver flag Must be at least one. |

## `EgressSelectorConfiguration`

EgressSelectorConfiguration provides versioned configuration for egress selector clients.

| Field | Description |
| --- | --- |
| `apiVersion` string | `apiserver.k8s.io/v1beta1` |
| `kind` string | `EgressSelectorConfiguration` |
| `egressSelections` **[Required]**  [`[]EgressSelection`](#apiserver-k8s-io-v1beta1-EgressSelection) | connectionServices contains a list of egress selection client configurations |

## `TracingConfiguration`

TracingConfiguration provides versioned configuration for tracing clients.

| Field | Description |
| --- | --- |
| `apiVersion` string | `apiserver.k8s.io/v1beta1` |
| `kind` string | `TracingConfiguration` |
| `TracingConfiguration` **[Required]**  [`TracingConfiguration`](#TracingConfiguration) | (Members of `TracingConfiguration` are embedded into this type.) Embed the component config tracing configuration struct |

## `AnonymousAuthCondition`

**Appears in:**

* [AnonymousAuthConfig](#apiserver-k8s-io-v1beta1-AnonymousAuthConfig)

AnonymousAuthCondition describes the condition under which anonymous auth
should be enabled.

| Field | Description |
| --- | --- |
| `path` **[Required]**  `string` | Path for which anonymous auth is enabled. |

## `AnonymousAuthConfig`

**Appears in:**

* [AuthenticationConfiguration](#apiserver-k8s-io-v1beta1-AuthenticationConfiguration)

AnonymousAuthConfig provides the configuration for the anonymous authenticator.

| Field | Description |
| --- | --- |
| `enabled` **[Required]**  `bool` | No description provided. |
| `conditions` **[Required]**  [`[]AnonymousAuthCondition`](#apiserver-k8s-io-v1beta1-AnonymousAuthCondition) | If set, anonymous auth is only allowed if the request meets one of the conditions. |

## `AudienceMatchPolicyType`

(Alias of `string`)

**Appears in:**

* [Issuer](#apiserver-k8s-io-v1beta1-Issuer)

AudienceMatchPolicyType is a set of valid values for issuer.audienceMatchPolicy

## `AuthorizerConfiguration`

**Appears in:**

* [AuthorizationConfiguration](#apiserver-k8s-io-v1beta1-AuthorizationConfiguration)

| Field | Description |
| --- | --- |
| `type` **[Required]**  `string` | Type refers to the type of the authorizer "Webhook" is supported in the generic API server Other API servers may support additional authorizer types like Node, RBAC, ABAC, etc. |
| `name` **[Required]**  `string` | Name used to describe the webhook This is explicitly used in monitoring machinery for metrics Note: Names must be DNS1123 labels like `myauthorizername` or subdomains like `myauthorizer.example.domain` Required, with no default |
| `webhook` **[Required]**  [`WebhookConfiguration`](#apiserver-k8s-io-v1beta1-WebhookConfiguration) | Webhook defines the configuration for a Webhook authorizer Must be defined when Type=Webhook Must not be defined when Type!=Webhook |

## `ClaimMappings`

**Appears in:**

* [JWTAuthenticator](#apiserver-k8s-io-v1beta1-JWTAuthenticator)

ClaimMappings provides the configuration for claim mapping

| Field | Description |
| --- | --- |
| `username` **[Required]**  [`PrefixedClaimOrExpression`](#apiserver-k8s-io-v1beta1-PrefixedClaimOrExpression) | username represents an option for the username attribute. The claim's value must be a singular string. Same as the --oidc-username-claim and --oidc-username-prefix flags. If username.expression is set, the expression must produce a string value. If username.expression uses 'claims.email', then 'claims.email_verified' must be used in username.expression or extra[*].valueExpression or claimValidationRules[*].expression. An example claim validation rule expression that matches the validation automatically applied when username.claim is set to 'email' is 'claims.?email_verified.orValue(true) == true'. By explicitly comparing the value to true, we let type-checking see the result will be a boolean, and to make sure a non-boolean email_verified claim will be caught at runtime.  In the flag based approach, the --oidc-username-claim and --oidc-username-prefix are optional. If --oidc-username-claim is not set, the default value is "sub". For the authentication config, there is no defaulting for claim or prefix. The claim and prefix must be set explicitly. For claim, if --oidc-username-claim was not set with legacy flag approach, configure username.claim="sub" in the authentication config. For prefix: (1) --oidc-username-prefix="-", no prefix was added to the username. For the same behavior using authentication config, set username.prefix="" (2) --oidc-username-prefix="" and --oidc-username-claim != "email", prefix was "<value of --oidc-issuer-url>#". For the same behavior using authentication config, set username.prefix="#" (3) --oidc-username-prefix="". For the same behavior using authentication config, set username.prefix="" |
| `groups`  [`PrefixedClaimOrExpression`](#apiserver-k8s-io-v1beta1-PrefixedClaimOrExpression) | groups represents an option for the groups attribute. The claim's value must be a string or string array claim. If groups.claim is set, the prefix must be specified (and can be the empty string). If groups.expression is set, the expression must produce a string or string array value. "", [], and null values are treated as the group mapping not being present. |
| `uid`  [`ClaimOrExpression`](#apiserver-k8s-io-v1beta1-ClaimOrExpression) | uid represents an option for the uid attribute. Claim must be a singular string claim. If uid.expression is set, the expression must produce a string value. |
| `extra`  [`[]ExtraMapping`](#apiserver-k8s-io-v1beta1-ExtraMapping) | extra represents an option for the extra attribute. expression must produce a string or string array value. If the value is empty, the extra mapping will not be present.  hard-coded extra key/value   * key: "foo"   valueExpression: "'bar'"   This will result in an extra attribute - foo: ["bar"]   hard-coded key, value copying claim value   * key: "foo"   valueExpression: "claims.some_claim"   This will result in an extra attribute - foo: [value of some_claim]   hard-coded key, value derived from claim value   * key: "admin"   valueExpression: '(has(claims.is_admin) && claims.is_admin) ? "true":""'   This will result in: * if is_admin claim is present and true, extra attribute - admin: ["true"] * if is_admin claim is present and false or is_admin claim is not present, no extra attribute will be added |

## `ClaimOrExpression`

**Appears in:**

* [ClaimMappings](#apiserver-k8s-io-v1beta1-ClaimMappings)

ClaimOrExpression provides the configuration for a single claim or expression.

| Field | Description |
| --- | --- |
| `claim`  `string` | claim is the JWT claim to use. Either claim or expression must be set. Mutually exclusive with expression. |
| `expression`  `string` | expression represents the expression which will be evaluated by CEL.  CEL expressions have access to the contents of the token claims, organized into CEL variable:   * 'claims' is a map of claim names to claim values.   For example, a variable named 'sub' can be accessed as 'claims.sub'.   Nested claims can be accessed using dot notation, e.g. 'claims.foo.bar'.   Documentation on CEL: https://kubernetes.io/docs/reference/using-api/cel/  Mutually exclusive with claim. |

## `ClaimValidationRule`

**Appears in:**

* [JWTAuthenticator](#apiserver-k8s-io-v1beta1-JWTAuthenticator)

ClaimValidationRule provides the configuration for a single claim validation rule.

| Field | Description |
| --- | --- |
| `claim`  `string` | claim is the name of a required claim. Same as --oidc-required-claim flag. Only string claim keys are supported. Mutually exclusive with expression and message. |
| `requiredValue`  `string` | requiredValue is the value of a required claim. Same as --oidc-required-claim flag. Only string claim values are supported. If claim is set and requiredValue is not set, the claim must be present with a value set to the empty string. Mutually exclusive with expression and message. |
| `expression`  `string` | expression represents the expression which will be evaluated by CEL. Must produce a boolean.  CEL expressions have access to the contents of the token claims, organized into CEL variable:   * 'claims' is a map of claim names to claim values.   For example, a variable named 'sub' can be accessed as 'claims.sub'.   Nested claims can be accessed using dot notation, e.g. 'claims.foo.bar'.   Must return true for the validation to pass.   Documentation on CEL: https://kubernetes.io/docs/reference/using-api/cel/  Mutually exclusive with claim and requiredValue. |
| `message`  `string` | message customizes the returned error message when expression returns false. message is a literal string. Mutually exclusive with claim and requiredValue. |

## `Connection`

**Appears in:**

* [EgressSelection](#apiserver-k8s-io-v1beta1-EgressSelection)

Connection provides the configuration for a single egress selection client.

| Field | Description |
| --- | --- |
| `proxyProtocol` **[Required]**  [`ProtocolType`](#apiserver-k8s-io-v1beta1-ProtocolType) | Protocol is the protocol used to connect from client to the konnectivity server. |
| `transport`  [`Transport`](#apiserver-k8s-io-v1beta1-Transport) | Transport defines the transport configurations we use to dial to the konnectivity server. This is required if ProxyProtocol is HTTPConnect or GRPC. |

## `EgressSelection`

**Appears in:**

* [EgressSelectorConfiguration](#apiserver-k8s-io-v1beta1-EgressSelectorConfiguration)

EgressSelection provides the configuration for a single egress selection client.

| Field | Description |
| --- | --- |
| `name` **[Required]**  `string` | name is the name of the egress selection. Currently supported values are "controlplane", "master", "etcd" and "cluster" The "master" egress selector is deprecated in favor of "controlplane" |
| `connection` **[Required]**  [`Connection`](#apiserver-k8s-io-v1beta1-Connection) | connection is the exact information used to configure the egress selection |

## `EgressSelectorType`

(Alias of `string`)

**Appears in:**

* [Issuer](#apiserver-k8s-io-v1beta1-Issuer)

EgressSelectorType is an indicator of which egress selection should be used for sending traffic.

## `ExtraMapping`

**Appears in:**

* [ClaimMappings](#apiserver-k8s-io-v1beta1-ClaimMappings)

ExtraMapping provides the configuration for a single extra mapping.

| Field | Description |
| --- | --- |
| `key` **[Required]**  `string` | key is a string to use as the extra attribute key. key must be a domain-prefix path (e.g. example.org/foo). All characters before the first "/" must be a valid subdomain as defined by RFC 1123. All characters trailing the first "/" must be valid HTTP Path characters as defined by RFC 3986. key must be lowercase. Required to be unique. |
| `valueExpression` **[Required]**  `string` | valueExpression is a CEL expression to extract extra attribute value. valueExpression must produce a string or string array value. "", [], and null values are treated as the extra mapping not being present. Empty string values contained within a string array are filtered out.  CEL expressions have access to the contents of the token claims, organized into CEL variable:   * 'claims' is a map of claim names to claim values.   For example, a variable named 'sub' can be accessed as 'claims.sub'.   Nested claims can be accessed using dot notation, e.g. 'claims.foo.bar'.   Documentation on CEL: https://kubernetes.io/docs/reference/using-api/cel/ |

## `Issuer`

**Appears in:**

* [JWTAuthenticator](#apiserver-k8s-io-v1beta1-JWTAuthenticator)

Issuer provides the configuration for an external provider's specific settings.

| Field | Description |
| --- | --- |
| `url` **[Required]**  `string` | url points to the issuer URL in a format https://url or https://url/path. This must match the "iss" claim in the presented JWT, and the issuer returned from discovery. Same value as the --oidc-issuer-url flag. Discovery information is fetched from "{url}/.well-known/openid-configuration" unless overridden by discoveryURL. Required to be unique across all JWT authenticators. Note that egress selection configuration is not used for this network connection. |
| `discoveryURL`  `string` | discoveryURL, if specified, overrides the URL used to fetch discovery information instead of using "{url}/.well-known/openid-configuration". The exact value specified is used, so "/.well-known/openid-configuration" must be included in discoveryURL if needed.  The "issuer" field in the fetched discovery information must match the "issuer.url" field in the AuthenticationConfiguration and will be used to validate the "iss" claim in the presented JWT. This is for scenarios where the well-known and jwks endpoints are hosted at a different location than the issuer (such as locally in the cluster).  Example: A discovery url that is exposed using kubernetes service 'oidc' in namespace 'oidc-namespace' and discovery information is available at '/.well-known/openid-configuration'. discoveryURL: "https://oidc.oidc-namespace/.well-known/openid-configuration" certificateAuthority is used to verify the TLS connection and the hostname on the leaf certificate must be set to 'oidc.oidc-namespace'.  curl https://oidc.oidc-namespace/.well-known/openid-configuration (.discoveryURL field) { issuer: "https://oidc.example.com" (.url field) }  discoveryURL must be different from url. Required to be unique across all JWT authenticators. Note that egress selection configuration is not used for this network connection. |
| `certificateAuthority`  `string` | certificateAuthority contains PEM-encoded certificate authority certificates used to validate the connection when fetching discovery information. If unset, the system verifier is used. Same value as the content of the file referenced by the --oidc-ca-file flag. |
| `audiences` **[Required]**  `[]string` | audiences is the set of acceptable audiences the JWT must be issued to. At least one of the entries must match the "aud" claim in presented JWTs. Same value as the --oidc-client-id flag (though this field supports an array). Required to be non-empty. |
| `audienceMatchPolicy`  [`AudienceMatchPolicyType`](#apiserver-k8s-io-v1beta1-AudienceMatchPolicyType) | audienceMatchPolicy defines how the "audiences" field is used to match the "aud" claim in the presented JWT. Allowed values are:   1. "MatchAny" when multiple audiences are specified and 2. empty (or unset) or "MatchAny" when a single audience is specified.  * MatchAny: the "aud" claim in the presented JWT must match at least one of the entries in the "audiences" field.   For example, if "audiences" is ["foo", "bar"], the "aud" claim in the presented JWT must contain either "foo" or "bar" (and may contain both). * "": The match policy can be empty (or unset) when a single audience is specified in the "audiences" field. The "aud" claim in the presented JWT must contain the single audience (and may contain others).   For more nuanced audience validation, use claimValidationRules. example: claimValidationRule[].expression: 'sets.equivalent(claims.aud, ["bar", "foo", "baz"])' to require an exact match. |
| `egressSelectorType`  [`EgressSelectorType`](#apiserver-k8s-io-v1beta1-EgressSelectorType) | egressSelectorType is an indicator of which egress selection should be used for sending all traffic related to this issuer (discovery, JWKS, distributed claims, etc). If unspecified, no custom dialer is used. When specified, the valid choices are "controlplane" and "cluster". These correspond to the associated values in the --egress-selector-config-file.   * controlplane: for traffic intended to go to the control plane. * cluster: for traffic intended to go to the system being managed by Kubernetes. |

## `JWTAuthenticator`

**Appears in:**

* [AuthenticationConfiguration](#apiserver-k8s-io-v1beta1-AuthenticationConfiguration)

JWTAuthenticator provides the configuration for a single JWT authenticator.

| Field | Description |
| --- | --- |
| `issuer` **[Required]**  [`Issuer`](#apiserver-k8s-io-v1beta1-Issuer) | issuer contains the basic OIDC provider connection options. |
| `claimValidationRules`  [`[]ClaimValidationRule`](#apiserver-k8s-io-v1beta1-ClaimValidationRule) | claimValidationRules are rules that are applied to validate token claims to authenticate users. |
| `claimMappings` **[Required]**  [`ClaimMappings`](#apiserver-k8s-io-v1beta1-ClaimMappings) | claimMappings points claims of a token to be treated as user attributes. |
| `userValidationRules`  [`[]UserValidationRule`](#apiserver-k8s-io-v1beta1-UserValidationRule) | userValidationRules are rules that are applied to final user before completing authentication. These allow invariants to be applied to incoming identities such as preventing the use of the system: prefix that is commonly used by Kubernetes components. The validation rules are logically ANDed together and must all return true for the validation to pass. |

## `PrefixedClaimOrExpression`

**Appears in:**

* [ClaimMappings](#apiserver-k8s-io-v1beta1-ClaimMappings)

PrefixedClaimOrExpression provides the configuration for a single prefixed claim or expression.

| Field | Description |
| --- | --- |
| `claim`  `string` | claim is the JWT claim to use. Mutually exclusive with expression. |
| `prefix`  `string` | prefix is prepended to claim's value to prevent clashes with existing names. prefix needs to be set if claim is set and can be the empty string. Mutually exclusive with expression. |
| `expression`  `string` | expression represents the expression which will be evaluated by CEL.  CEL expressions have access to the contents of the token claims, organized into CEL variable:   * 'claims' is a map of claim names to claim values.   For example, a variable named 'sub' can be accessed as 'claims.sub'.   Nested claims can be accessed using dot notation, e.g. 'claims.foo.bar'.   Documentation on CEL: https://kubernetes.io/docs/reference/using-api/cel/  Mutually exclusive with claim and prefix. |

## `ProtocolType`

(Alias of `string`)

**Appears in:**

* [Connection](#apiserver-k8s-io-v1beta1-Connection)

ProtocolType is a set of valid values for Connection.ProtocolType

## `TCPTransport`

**Appears in:**

* [Transport](#apiserver-k8s-io-v1beta1-Transport)

TCPTransport provides the information to connect to konnectivity server via TCP

| Field | Description |
| --- | --- |
| `url` **[Required]**  `string` | URL is the location of the konnectivity server to connect to. As an example it might be "https://127.0.0.1:8131" |
| `tlsConfig`  [`TLSConfig`](#apiserver-k8s-io-v1beta1-TLSConfig) | TLSConfig is the config needed to use TLS when connecting to konnectivity server |

## `TLSConfig`

**Appears in:**

* [TCPTransport](#apiserver-k8s-io-v1beta1-TCPTransport)

TLSConfig provides the authentication information to connect to konnectivity server
Only used with TCPTransport

| Field | Description |
| --- | --- |
| `caBundle`  `string` | caBundle is the file location of the CA to be used to determine trust with the konnectivity server. Must be absent/empty if TCPTransport.URL is prefixed with http:// If absent while TCPTransport.URL is prefixed with https://, default to system trust roots. |
| `clientKey`  `string` | clientKey is the file location of the client key to be used in mtls handshakes with the konnectivity server. Must be absent/empty if TCPTransport.URL is prefixed with http:// Must be configured if TCPTransport.URL is prefixed with https:// |
| `clientCert`  `string` | clientCert is the file location of the client certificate to be used in mtls handshakes with the konnectivity server. Must be absent/empty if TCPTransport.URL is prefixed with http:// Must be configured if TCPTransport.URL is prefixed with https:// |

## `Transport`

**Appears in:**

* [Connection](#apiserver-k8s-io-v1beta1-Connection)

Transport defines the transport configurations we use to dial to the konnectivity server

| Field | Description |
| --- | --- |
| `tcp`  [`TCPTransport`](#apiserver-k8s-io-v1beta1-TCPTransport) | TCP is the TCP configuration for communicating with the konnectivity server via TCP ProxyProtocol of GRPC is not supported with TCP transport at the moment Requires at least one of TCP or UDS to be set |
| `uds`  [`UDSTransport`](#apiserver-k8s-io-v1beta1-UDSTransport) | UDS is the UDS configuration for communicating with the konnectivity server via UDS Requires at least one of TCP or UDS to be set |

## `UDSTransport`

**Appears in:**

* [Transport](#apiserver-k8s-io-v1beta1-Transport)

UDSTransport provides the information to connect to konnectivity server via UDS

| Field | Description |
| --- | --- |
| `udsName` **[Required]**  `string` | UDSName is the name of the unix domain socket to connect to konnectivity server This does not use a unix:// prefix. (Eg: /etc/srv/kubernetes/konnectivity-server/konnectivity-server.socket) |

## `UserValidationRule`

**Appears in:**

* [JWTAuthenticator](#apiserver-k8s-io-v1beta1-JWTAuthenticator)

UserValidationRule provides the configuration for a single user info validation rule.

| Field | Description |
| --- | --- |
| `expression` **[Required]**  `string` | expression represents the expression which will be evaluated by CEL. Must return true for the validation to pass.  CEL expressions have access to the contents of UserInfo, organized into CEL variable:   * 'user' - authentication.k8s.io/v1, Kind=UserInfo object   Refer to https://github.com/kubernetes/api/blob/release-1.28/authentication/v1/types.go#L105-L122 for the definition.   API documentation: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#userinfo-v1-authentication-k8s-io   Documentation on CEL: https://kubernetes.io/docs/reference/using-api/cel/ |
| `message`  `string` | message customizes the returned error message when rule returns false. message is a literal string. |

## `WebhookConfiguration`

**Appears in:**

* [AuthorizerConfiguration](#apiserver-k8s-io-v1beta1-AuthorizerConfiguration)

| Field | Description |
| --- | --- |
| `authorizedTTL` **[Required]**  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | The duration to cache 'authorized' responses from the webhook authorizer. Same as setting `--authorization-webhook-cache-authorized-ttl` flag Default: 5m0s |
| `cacheAuthorizedRequests`  `bool` | CacheAuthorizedRequests specifies whether authorized requests should be cached. If set to true, the TTL for cached decisions can be configured via the AuthorizedTTL field. Default: true |
| `unauthorizedTTL` **[Required]**  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | The duration to cache 'unauthorized' responses from the webhook authorizer. Same as setting `--authorization-webhook-cache-unauthorized-ttl` flag Default: 30s |
| `cacheUnauthorizedRequests`  `bool` | CacheUnauthorizedRequests specifies whether unauthorized requests should be cached. If set to true, the TTL for cached decisions can be configured via the UnauthorizedTTL field. Default: true |
| `timeout` **[Required]**  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | Timeout for the webhook request Maximum allowed value is 30s. Required, no default value. |
| `subjectAccessReviewVersion` **[Required]**  `string` | The API version of the authorization.k8s.io SubjectAccessReview to send to and expect from the webhook. Same as setting `--authorization-webhook-version` flag Valid values: v1beta1, v1 Required, no default value |
| `matchConditionSubjectAccessReviewVersion` **[Required]**  `string` | MatchConditionSubjectAccessReviewVersion specifies the SubjectAccessReview version the CEL expressions are evaluated against Valid values: v1 Required, no default value |
| `failurePolicy` **[Required]**  `string` | Controls the authorization decision when a webhook request fails to complete or returns a malformed response or errors evaluating matchConditions. Valid values:   * NoOpinion: continue to subsequent authorizers to see if one of   them allows the request * Deny: reject the request without consulting subsequent authorizers   Required, with no default. |
| `connectionInfo` **[Required]**  [`WebhookConnectionInfo`](#apiserver-k8s-io-v1beta1-WebhookConnectionInfo) | ConnectionInfo defines how we talk to the webhook |
| `matchConditions` **[Required]**  [`[]WebhookMatchCondition`](#apiserver-k8s-io-v1beta1-WebhookMatchCondition) | matchConditions is a list of conditions that must be met for a request to be sent to this webhook. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.  The exact matching logic is (in order):   1. If at least one matchCondition evaluates to FALSE, then the webhook is skipped. 2. If ALL matchConditions evaluate to TRUE, then the webhook is called. 3. If at least one matchCondition evaluates to an error (but none are FALSE):    * If failurePolicy=Deny, then the webhook rejects the request    * If failurePolicy=NoOpinion, then the error is ignored and the webhook is skipped |

## `WebhookConnectionInfo`

**Appears in:**

* [WebhookConfiguration](#apiserver-k8s-io-v1beta1-WebhookConfiguration)

| Field | Description |
| --- | --- |
| `type` **[Required]**  `string` | Controls how the webhook should communicate with the server. Valid values:   * KubeConfigFile: use the file specified in kubeConfigFile to locate the   server. * InClusterConfig: use the in-cluster configuration to call the   SubjectAccessReview API hosted by kube-apiserver. This mode is not   allowed for kube-apiserver. |
| `kubeConfigFile` **[Required]**  `string` | Path to KubeConfigFile for connection info Required, if connectionInfo.Type is KubeConfig |

## `WebhookMatchCondition`

**Appears in:**

* [WebhookConfiguration](#apiserver-k8s-io-v1beta1-WebhookConfiguration)

| Field | Description |
| --- | --- |
| `expression` **[Required]**  `string` | expression represents the expression which will be evaluated by CEL. Must evaluate to bool. CEL expressions have access to the contents of the SubjectAccessReview in v1 version. If version specified by subjectAccessReviewVersion in the request variable is v1beta1, the contents would be converted to the v1 version before evaluating the CEL expression.   * 'resourceAttributes' describes information for a resource access request and is unset for non-resource requests. e.g. has(request.resourceAttributes) && request.resourceAttributes.namespace == 'default' * 'nonResourceAttributes' describes information for a non-resource access request and is unset for resource requests. e.g. has(request.nonResourceAttributes) && request.nonResourceAttributes.path == '/healthz'. * 'user' is the user to test for. e.g. request.user == 'alice' * 'groups' is the groups to test for. e.g. ('group1' in request.groups) * 'extra' corresponds to the user.Info.GetExtra() method from the authenticator. * 'uid' is the information about the requesting user. e.g. request.uid == '1'   Documentation on CEL: https://kubernetes.io/docs/reference/using-api/cel/ |

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
