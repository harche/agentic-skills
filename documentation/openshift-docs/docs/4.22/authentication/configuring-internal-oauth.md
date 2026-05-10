# OpenShift Container Platform OAuth server

The OpenShift Container Platform Control Plane includes a built-in OAuth server. Users obtain OAuth access tokens to authenticate themselves to the API.

When a person requests a new OAuth token, the OAuth server uses the configured identity provider to determine the identity of the person making the request.

It then determines what user that identity maps to, creates an access token for that user, and returns the token for use.

# OAuth token request flows and responses

The OAuth server supports standard [authorization code grant](https://tools.ietf.org/html/rfc6749#section-4.1) and the [implicit grant](https://tools.ietf.org/html/rfc6749#section-4.2) OAuth authorization flows.

When requesting an OAuth token using the implicit grant flow (`response_type=token`) with a client_id configured to request `WWW-Authenticate challenges` (like `openshift-challenging-client`), these are the possible server responses from `/oauth/authorize`, and how they should be handled:

| Status | Content | Client response |
|----|----|----|
| 302 | `Location` header containing an `access_token` parameter in the URL fragment ([RFC 6749 section 4.2.2](https://tools.ietf.org/html/rfc6749#section-4.2.2)) | Use the `access_token` value as the OAuth token. |
| 302 | `Location` header containing an `error` query parameter ([RFC 6749 section 4.1.2.1](https://tools.ietf.org/html/rfc6749#section-4.1.2.1)) | Fail, optionally surfacing the `error` (and optional `error_description`) query values to the user. |
| 302 | Other `Location` header | Follow the redirect, and process the result using these rules. |
| 401 | `WWW-Authenticate` header present | Respond to challenge if type is recognized (e.g. `Basic`, `Negotiate`, etc), resubmit request, and process the result using these rules. |
| 401 | `WWW-Authenticate` header missing | No challenge authentication is possible. Fail and show response body (which might contain links or details on alternate methods to obtain an OAuth token). |
| Other | Other | Fail, optionally surfacing response body to the user. |

# Options for the internal OAuth server

Several configuration options are available for the internal OAuth server.

## OAuth token duration options

The internal OAuth server generates two kinds of tokens:

| Token | Description |
|----|----|
| Access tokens | Longer-lived tokens that grant access to the API. |
| Authorize codes | Short-lived tokens whose only use is to be exchanged for an access token. |

You can configure the default duration for both types of token. If necessary, you can override the duration of the access token by using an `OAuthClient` object definition.

## OAuth grant options

When the OAuth server receives token requests for a client to which the user has not previously granted permission, the action that the OAuth server takes is dependent on the OAuth client’s grant strategy.

The OAuth client requesting token must provide its own grant strategy.

You can apply the following default methods:

| Grant option | Description                                   |
|--------------|-----------------------------------------------|
| `auto`       | Auto-approve the grant and retry the request. |
| `prompt`     | Prompt the user to approve or deny the grant. |

# Configuring the internal OAuth server’s token duration

You can configure default options for the internal OAuth server’s token duration.

> [!IMPORTANT]
> By default, tokens are only valid for 24 hours. Existing sessions expire after this time elapses.

If the default time is insufficient, then this can be modified using the following procedure.

<div>

<div class="title">

Procedure

</div>

1.  Create a configuration file that contains the token duration options. The following file sets this to 48 hours, twice the default.

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: OAuth
    metadata:
      name: cluster
    spec:
      tokenConfig:
        accessTokenMaxAgeSeconds: 172800
    ```

    - Set `accessTokenMaxAgeSeconds` to control the lifetime of access tokens. The default lifetime is 24 hours, or 86400 seconds. This attribute cannot be negative. If set to zero, the default lifetime is used.

2.  Apply the new configuration file:

    > [!NOTE]
    > Because you update the existing OAuth server, you must use the `oc apply` command to apply the change.

    ``` terminal
    $ oc apply -f </path/to/file.yaml>
    ```

3.  Confirm that the changes are in effect:

    ``` terminal
    $ oc describe oauth.config.openshift.io/cluster
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    ...
    Spec:
      Token Config:
        Access Token Max Age Seconds:  172800
    ...
    ```

    </div>

</div>

# Configuring token inactivity timeout for the internal OAuth server

You can configure OAuth tokens to expire after a set period of inactivity. By default, no token inactivity timeout is set.

> [!NOTE]
> If the token inactivity timeout is also configured in your OAuth client, that value overrides the timeout that is set in the internal OAuth server configuration.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have configured an identity provider (IDP).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Update the `OAuth` configuration to set a token inactivity timeout.

    1.  Edit the `OAuth` object:

        ``` terminal
        $ oc edit oauth cluster
        ```

        Add the `spec.tokenConfig.accessTokenInactivityTimeout` field and set your timeout value:

        ``` yaml
        apiVersion: config.openshift.io/v1
        kind: OAuth
        metadata:
        ...
        spec:
          tokenConfig:
            accessTokenInactivityTimeout: 400s
        ```

        - Set a value with the appropriate units, for example `400s` for 400 seconds, or `30m` for 30 minutes. The minimum allowed timeout value is `300s`.

    2.  Save the file to apply the changes.

2.  Check that the OAuth server pods have restarted:

    ``` terminal
    $ oc get clusteroperators authentication
    ```

    Do not continue to the next step until `PROGRESSING` is listed as `False`, as shown in the following output:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME             VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
    authentication   4.17.0    True        False         False      145m
    ```

    </div>

3.  Check that a new revision of the Kubernetes API server pods has rolled out. This will take several minutes.

    ``` terminal
    $ oc get clusteroperators kube-apiserver
    ```

    Do not continue to the next step until `PROGRESSING` is listed as `False`, as shown in the following output:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME             VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
    kube-apiserver   4.17.0     True        False         False      145m
    ```

    </div>

    If `PROGRESSING` is showing `True`, wait a few minutes and try again.

</div>

<div>

<div class="title">

Verification

</div>

1.  Log in to the cluster with an identity from your IDP.

2.  Execute a command and verify that it was successful.

3.  Wait longer than the configured timeout without using the identity. In this procedure’s example, wait longer than 400 seconds.

4.  Try to execute a command from the same identity’s session.

    This command should fail because the token should have expired due to inactivity longer than the configured timeout.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    error: You must be logged in to the server (Unauthorized)
    ```

    </div>

</div>

# Customizing the internal OAuth server URL

You can customize the internal OAuth server URL by setting the custom hostname and TLS certificate in the `spec.componentRoutes` field of the cluster `Ingress` configuration.

> [!WARNING]
> If you update the internal OAuth server URL, you might break trust from components in the cluster that need to communicate with the OpenShift OAuth server to retrieve OAuth access tokens. Components that need to trust the OAuth server will need to include the proper CA bundle when calling OAuth endpoints. For example:
>
> ``` terminal
> $ oc login -u <username> -p <password> --certificate-authority=<path_to_ca.crt>
> ```
>
> - For self-signed certificates, the `ca.crt` file must contain the custom CA certificate, otherwise the login will not succeed.
>
> The Cluster Authentication Operator publishes the OAuth server’s serving certificate in the `oauth-serving-cert` config map in the `openshift-config-managed` namespace. You can find the certificate in the `data.ca-bundle.crt` key of the config map.

<div>

<div class="title">

Prerequisites

</div>

- You have logged in to the cluster as a user with administrative privileges.

- You have created a secret in the `openshift-config` namespace containing the TLS certificate and key. This is required if the domain for the custom hostname suffix does not match the cluster domain suffix. The secret is optional if the suffix matches.

  > [!TIP]
  > You can create a TLS secret by using the `oc create secret tls` command.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the cluster `Ingress` configuration:

    ``` terminal
    $ oc edit ingress.config.openshift.io cluster
    ```

2.  Set the custom hostname and optionally the serving certificate and key:

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: Ingress
    metadata:
      name: cluster
    spec:
      componentRoutes:
        - name: oauth-openshift
          namespace: openshift-authentication
          hostname: <custom_hostname>
          servingCertKeyPairSecret:
            name: <secret_name>
    ```

    - The custom hostname.

    - Reference to a secret in the `openshift-config` namespace that contains a TLS certificate (`tls.crt`) and key (`tls.key`). This is required if the domain for the custom hostname suffix does not match the cluster domain suffix. The secret is optional if the suffix matches.

3.  Save the file to apply the changes.

</div>

# OAuth server metadata

Applications running in OpenShift Container Platform might have to discover information about the built-in OAuth server. For example, they might have to discover what the address of the `<namespace_route>` is without manual configuration. To aid in this, OpenShift Container Platform implements the IETF [OAuth 2.0 Authorization Server Metadata](https://tools.ietf.org/html/draft-ietf-oauth-discovery-10) draft specification.

Thus, any application running inside the cluster can issue a `GET` request to ***https://openshift.default.svc/.well-known/oauth-authorization-server*** to fetch the following information:

    {
      "issuer": "https://<namespace_route>",
      "authorization_endpoint": "https://<namespace_route>/oauth/authorize",
      "token_endpoint": "https://<namespace_route>/oauth/token",
      "scopes_supported": [
        "user:full",
        "user:info",
        "user:check-access",
        "user:list-scoped-projects",
        "user:list-projects"
      ],
      "response_types_supported": [
        "code",
        "token"
      ],
      "grant_types_supported": [
        "authorization_code",
        "implicit"
      ],
      "code_challenge_methods_supported": [
        "plain",
        "S256"
      ]
    }

- The authorization server’s issuer identifier, which is a URL that uses the `https` scheme and has no query or fragment components. This is the location where `.well-known` [RFC 5785](https://tools.ietf.org/html/rfc5785) resources containing information about the authorization server are published.

- URL of the authorization server’s authorization endpoint. See [RFC 6749](https://tools.ietf.org/html/rfc6749).

- URL of the authorization server’s token endpoint. See [RFC 6749](https://tools.ietf.org/html/rfc6749).

- JSON array containing a list of the OAuth 2.0 [RFC 6749](https://tools.ietf.org/html/rfc6749) scope values that this authorization server supports. Note that not all supported scope values are advertised.

- JSON array containing a list of the OAuth 2.0 `response_type` values that this authorization server supports. The array values used are the same as those used with the `response_types` parameter defined by "OAuth 2.0 Dynamic Client Registration Protocol" in [RFC 7591](https://tools.ietf.org/html/rfc7591).

- JSON array containing a list of the OAuth 2.0 grant type values that this authorization server supports. The array values used are the same as those used with the `grant_types` parameter defined by `OAuth 2.0 Dynamic Client Registration Protocol` in [RFC 7591](https://tools.ietf.org/html/rfc7591).

- JSON array containing a list of PKCE [RFC 7636](https://tools.ietf.org/html/rfc7636) code challenge methods supported by this authorization server. Code challenge method values are used in the `code_challenge_method` parameter defined in [Section 4.3 of RFC 7636](https://tools.ietf.org/html/rfc7636#section-4.3). The valid code challenge method values are those registered in the IANA `PKCE Code Challenge Methods` registry. See [IANA OAuth Parameters](http://www.iana.org/assignments/oauth-parameters).

# Troubleshooting OAuth API events

In some cases the API server returns an `unexpected condition` error message that is difficult to debug without direct access to the API master log. The underlying reason for the error is purposely obscured in order to avoid providing an unauthenticated user with information about the server’s state.

A subset of these errors is related to service account OAuth configuration issues. These issues are captured in events that can be viewed by non-administrator users. When encountering an `unexpected condition` server error during OAuth, run `oc get events` to view these events under `ServiceAccount`.

The following example warns of a service account that is missing a proper OAuth redirect URI:

``` terminal
$ oc get events | grep ServiceAccount
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
1m         1m          1         proxy                    ServiceAccount                                  Warning   NoSAOAuthRedirectURIs   service-account-oauth-client-getter   system:serviceaccount:myproject:proxy has no redirectURIs; set serviceaccounts.openshift.io/oauth-redirecturi.<some-value>=<redirect> or create a dynamic URI using serviceaccounts.openshift.io/oauth-redirectreference.<some-value>=<reference>
```

</div>

Running `oc describe sa/<service_account_name>` reports any OAuth events associated with the given service account name.

``` terminal
$ oc describe sa/proxy | grep -A5 Events
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
Events:
  FirstSeen     LastSeen        Count   From                                    SubObjectPath   Type            Reason                  Message
  ---------     --------        -----   ----                                    -------------   --------        ------                  -------
  3m            3m              1       service-account-oauth-client-getter                     Warning         NoSAOAuthRedirectURIs   system:serviceaccount:myproject:proxy has no redirectURIs; set serviceaccounts.openshift.io/oauth-redirecturi.<some-value>=<redirect> or create a dynamic URI using serviceaccounts.openshift.io/oauth-redirectreference.<some-value>=<reference>
```

</div>

The following is a list of the possible event errors:

**No redirect URI annotations or an invalid URI is specified**

``` terminal
Reason                  Message
NoSAOAuthRedirectURIs   system:serviceaccount:myproject:proxy has no redirectURIs; set serviceaccounts.openshift.io/oauth-redirecturi.<some-value>=<redirect> or create a dynamic URI using serviceaccounts.openshift.io/oauth-redirectreference.<some-value>=<reference>
```

**Invalid route specified**

``` terminal
Reason                  Message
NoSAOAuthRedirectURIs   [routes.route.openshift.io "<name>" not found, system:serviceaccount:myproject:proxy has no redirectURIs; set serviceaccounts.openshift.io/oauth-redirecturi.<some-value>=<redirect> or create a dynamic URI using serviceaccounts.openshift.io/oauth-redirectreference.<some-value>=<reference>]
```

**Invalid reference type specified**

``` terminal
Reason                  Message
NoSAOAuthRedirectURIs   [no kind "<name>" is registered for version "v1", system:serviceaccount:myproject:proxy has no redirectURIs; set serviceaccounts.openshift.io/oauth-redirecturi.<some-value>=<redirect> or create a dynamic URI using serviceaccounts.openshift.io/oauth-redirectreference.<some-value>=<reference>]
```

**Missing SA tokens**

``` terminal
Reason                  Message
NoSAOAuthTokens         system:serviceaccount:myproject:proxy has no tokens
```
