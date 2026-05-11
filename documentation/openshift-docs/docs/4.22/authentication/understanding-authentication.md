For users to interact with OpenShift Container Platform, they must first authenticate to the cluster. The authentication layer identifies the user associated with requests to the OpenShift Container Platform API. The authorization layer then uses information about the requesting user to determine if the request is allowed.

As an administrator, you can configure authentication for OpenShift Container Platform.

# Users

A *user* in OpenShift Container Platform is an entity that can make requests to the OpenShift Container Platform API. An OpenShift Container Platform `User` object represents an actor which can be granted permissions in the system by adding roles to them or to their groups. Typically, this represents the account of a developer or administrator that is interacting with OpenShift Container Platform.

Several types of users can exist:

| User type | Description |
|----|----|
| `Regular users` | This is the way most interactive OpenShift Container Platform users are represented. Regular users are created automatically in the system upon first login or can be created via the API. Regular users are represented with the `User` object. Examples: `joe` `alice` |
| `System users` | Many of these are created automatically when the infrastructure is defined, mainly for the purpose of enabling the infrastructure to interact with the API securely. They include a cluster administrator (with access to everything), a per-node user, users for use by routers and registries, and various others. Finally, there is an `anonymous` system user that is used by default for unauthenticated requests. Examples: `system:admin` `system:openshift-registry` `system:node:node1.example.com` |
| `Service accounts` | These are special system users associated with projects; some are created automatically when the project is first created, while project administrators can create more for the purpose of defining access to the contents of each project. Service accounts are represented with the `ServiceAccount` object. Examples: `system:serviceaccount:default:deployer` `system:serviceaccount:foo:builder` |

Each user must authenticate in some way to access OpenShift Container Platform. API requests with no authentication or invalid authentication are authenticated as requests by the `anonymous` system user. After authentication, policy determines what the user is authorized to do.

# Groups

A user can be assigned to one or more *groups*, each of which represent a certain set of users. Groups are useful when managing authorization policies to grant permissions to multiple users at once, for example allowing access to objects within a project, versus granting them to users individually.

In addition to explicitly defined groups, there are also system groups, or *virtual groups*, that are automatically provisioned by the cluster.

The following default virtual groups are most important:

| Virtual group | Description |
|----|----|
| `system:authenticated` | Automatically associated with all authenticated users. |
| `system:authenticated:oauth` | Automatically associated with all users authenticated with an OAuth access token. |
| `system:unauthenticated` | Automatically associated with all unauthenticated users. |

# API authentication

Requests to the OpenShift Container Platform API are authenticated using the following methods:

OAuth access tokens
- Obtained from the OpenShift Container Platform OAuth server using the `<namespace_route>/oauth/authorize` and `<namespace_route>/oauth/token` endpoints.

- Sent as an `Authorization: Bearer…​` header.

- Sent as a websocket subprotocol header in the form `base64url.bearer.authorization.k8s.io.<base64url-encoded-token>` for websocket requests.

X.509 client certificates
- Requires an HTTPS connection to the API server.

- Verified by the API server against a trusted certificate authority bundle.

- The API server creates and distributes certificates to controllers to authenticate themselves.

Any request with an invalid access token or an invalid certificate is rejected by the authentication layer with a `401` error.

If no access token or certificate is presented, the authentication layer assigns the `system:anonymous` virtual user and the `system:unauthenticated` virtual group to the request. This allows the authorization layer to determine which requests, if any, an anonymous user is allowed to make.

## OpenShift Container Platform OAuth server

The OpenShift Container Platform Control Plane includes a built-in OAuth server. Users obtain OAuth access tokens to authenticate themselves to the API.

When a person requests a new OAuth token, the OAuth server uses the configured identity provider to determine the identity of the person making the request.

It then determines what user that identity maps to, creates an access token for that user, and returns the token for use.

### OAuth token requests

Every request for an OAuth token must specify the OAuth client that will receive and use the token. The following OAuth clients are automatically created when starting the OpenShift Container Platform API:

| OAuth client | Usage |
|----|----|
| `openshift-browser-client` | Requests tokens at `<namespace_route>/oauth/token/request` with a user-agent that can handle interactive logins. <sup>\[1\]</sup> |
| `openshift-challenging-client` | Requests tokens with a user-agent that can handle `WWW-Authenticate` challenges. |

<div wrapper="1" role="small">

1.  `<namespace_route>` refers to the namespace route. This is found by running the following command:

    ``` terminal
    $ oc get route oauth-openshift -n openshift-authentication -o json | jq .spec.host
    ```

</div>

All requests for OAuth tokens involve a request to `<namespace_route>/oauth/authorize`. Most authentication integrations place an authenticating proxy in front of this endpoint, or configure OpenShift Container Platform to validate credentials against a backing identity provider. Requests to `<namespace_route>/oauth/authorize` can come from user-agents that cannot display interactive login pages, such as the CLI. Therefore, OpenShift Container Platform supports authenticating using a `WWW-Authenticate` challenge in addition to interactive login flows.

If an authenticating proxy is placed in front of the `<namespace_route>/oauth/authorize` endpoint, it sends unauthenticated, non-browser user-agents `WWW-Authenticate` challenges rather than displaying an interactive login page or redirecting to an interactive login flow.

> [!NOTE]
> To prevent cross-site request forgery (CSRF) attacks against browser clients, only send Basic authentication challenges with if a `X-CSRF-Token` header is on the request. Clients that expect to receive Basic `WWW-Authenticate` challenges must set this header to a non-empty value.
>
> If the authenticating proxy cannot support `WWW-Authenticate` challenges, or if OpenShift Container Platform is configured to use an identity provider that does not support WWW-Authenticate challenges, you must use a browser to manually obtain a token from `<namespace_route>/oauth/token/request`.

### API impersonation

You can configure a request to the OpenShift Container Platform API to act as though it originated from another user. For more information, see [User impersonation](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation) in the Kubernetes documentation.

### Authentication metrics for Prometheus

OpenShift Container Platform captures the following Prometheus system metrics during authentication attempts:

- `openshift_auth_basic_password_count` counts the number of `oc login` user name and password attempts.

- `openshift_auth_basic_password_count_result` counts the number of `oc login` user name and password attempts by result, `success` or `error`.

- `openshift_auth_form_password_count` counts the number of web console login attempts.

- `openshift_auth_form_password_count_result` counts the number of web console login attempts by result, `success` or `error`.

- `openshift_auth_password_total` counts the total number of `oc login` and web console login attempts.
