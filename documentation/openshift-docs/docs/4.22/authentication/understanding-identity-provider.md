The OpenShift Container Platform master includes a built-in OAuth server. Developers and administrators obtain OAuth access tokens to authenticate themselves to the API.

As an administrator, you can configure OAuth to specify an identity provider after you install your cluster.

# About identity providers in OpenShift Container Platform

By default, only a `kubeadmin` user exists on your cluster. To specify an identity provider, you must create a custom resource (CR) that describes that identity provider and add it to the cluster.

> [!NOTE]
> OpenShift Container Platform user names containing `/`, `:`, and `%` are not supported.

# Supported identity providers

You can configure the following types of identity providers:

| Identity provider | Description |
|----|----|
| [htpasswd](../authentication/identity_providers/configuring-htpasswd-identity-provider.xml#configuring-htpasswd-identity-provider) | Configure the `htpasswd` identity provider to validate user names and passwords against a flat file generated using [`htpasswd`](http://httpd.apache.org/docs/2.4/programs/htpasswd.html). |
| [Keystone](../authentication/identity_providers/configuring-keystone-identity-provider.xml#configuring-keystone-identity-provider) | Configure the `keystone` identity provider to integrate your OpenShift Container Platform cluster with Keystone to enable shared authentication with an OpenStack Keystone v3 server configured to store users in an internal database. |
| [LDAP](../authentication/identity_providers/configuring-ldap-identity-provider.xml#configuring-ldap-identity-provider) | Configure the `ldap` identity provider to validate user names and passwords against an LDAPv3 server, using simple bind authentication. |
| [Basic authentication](../authentication/identity_providers/configuring-basic-authentication-identity-provider.xml#configuring-basic-authentication-identity-provider) | Configure a `basic-authentication` identity provider for users to log in to OpenShift Container Platform with credentials validated against a remote identity provider. Basic authentication is a generic backend integration mechanism. |
| [Request header](../authentication/identity_providers/configuring-request-header-identity-provider.xml#configuring-request-header-identity-provider) | Configure a `request-header` identity provider to identify users from request header values, such as `X-Remote-User`. It is typically used in combination with an authenticating proxy, which sets the request header value. |
| [GitHub or GitHub Enterprise](../authentication/identity_providers/configuring-github-identity-provider.xml#configuring-github-identity-provider) | Configure a `github` identity provider to validate user names and passwords against GitHub or GitHub Enterprise’s OAuth authentication server. |
| [GitLab](../authentication/identity_providers/configuring-gitlab-identity-provider.xml#configuring-gitlab-identity-provider) | Configure a `gitlab` identity provider to use [GitLab.com](https://gitlab.com/) or any other GitLab instance as an identity provider. |
| [Google](../authentication/identity_providers/configuring-google-identity-provider.xml#configuring-google-identity-provider) | Configure a `google` identity provider using [Google’s OpenID Connect integration](https://developers.google.com/identity/protocols/OpenIDConnect). |
| [OpenID Connect](../authentication/identity_providers/configuring-oidc-identity-provider.xml#configuring-oidc-identity-provider) | Configure an `oidc` identity provider to integrate with an OpenID Connect identity provider using an [Authorization Code Flow](http://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth). |

Once an identity provider has been defined, you can [use RBAC to define and apply permissions](../authentication/using-rbac.xml#authorization-overview_using-rbac).

# Removing the kubeadmin user

After you define an identity provider and create a new `cluster-admin` user, you can remove the `kubeadmin` to improve cluster security.

> [!WARNING]
> If you follow this procedure before another user is a `cluster-admin`, then OpenShift Container Platform must be reinstalled. It is not possible to undo this command.

<div>

<div class="title">

Prerequisites

</div>

- You must have configured at least one identity provider.

- You must have added the `cluster-admin` role to a user.

- You must be logged in as an administrator.

</div>

<div>

<div class="title">

Procedure

</div>

- Remove the `kubeadmin` secrets:

  ``` terminal
  $ oc delete secrets kubeadmin -n kube-system
  ```

</div>

# Identity provider parameters

<div wrapper="1" role="_abstract">

The following parameters are common to all identity providers:

</div>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p>The provider name is prefixed to provider user names to form an identity name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mappingMethod</code></p></td>
<td style="text-align: left;"><p>Defines how new identities are mapped to users when they log in. Enter one of the following values:</p>
<dl>
<dt>claim</dt>
<dd>
<p>The default value. Provisions a user with the identity’s preferred user name. Fails if a user with that user name is already mapped to another identity.</p>
</dd>
<dt>lookup</dt>
<dd>
<p>Looks up an existing identity, user identity mapping, and user, but does not automatically provision users or identities. This allows cluster administrators to set up identities and users manually, or using an external process. Using this method requires you to manually provision users.</p>
</dd>
<dt>add</dt>
<dd>
<p>Provisions a user with the identity’s preferred user name. If a user with that user name already exists, the identity is mapped to the existing user, adding to any existing identity mappings for the user. Required when multiple identity providers are configured that identify the same set of users and map to the same user names.</p>
</dd>
</dl></td>
</tr>
</tbody>
</table>

> [!NOTE]
> When adding or changing identity providers, you can map identities from the new provider to existing users by setting the `mappingMethod` parameter to `add`.

# Sample identity provider CR

The following custom resource (CR) shows the parameters and default values that you use to configure an identity provider. This example uses the htpasswd identity provider.

<div class="formalpara">

<div class="title">

Sample identity provider CR

</div>

``` yaml
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: my_identity_provider
    mappingMethod: claim
    type: HTPasswd
    htpasswd:
      fileData:
        name: htpass-secret
```

</div>

- This provider name is prefixed to provider user names to form an identity name.

- Controls how mappings are established between this provider’s identities and `User` objects.

- An existing secret containing a file generated using [`htpasswd`](http://httpd.apache.org/docs/2.4/programs/htpasswd.html).

# Manually provisioning a user when using the lookup mapping method

Typically, identities are automatically mapped to users during login. The `lookup` mapping method disables this automatic mapping, which requires you to provision users manually. If you are using the `lookup` mapping method, use the following procedure for each user after configuring the identity provider.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an OpenShift Container Platform user:

    ``` terminal
    $ oc create user <username>
    ```

2.  Create an OpenShift Container Platform identity:

    ``` terminal
    $ oc create identity <identity_provider>:<identity_provider_user_id>
    ```

    Where `<identity_provider_user_id>` is a name that uniquely represents the user in the identity provider.

3.  Create a user identity mapping for the created user and identity:

    ``` terminal
    $ oc create useridentitymapping <identity_provider>:<identity_provider_user_id> <username>
    ```

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [How to create user, identity and map user and identity in LDAP authentication for `mappingMethod` as `lookup` inside the OAuth manifest](https://access.redhat.com/solutions/6006921)

- [How to create user, identity and map user and identity in OIDC authentication for `mappingMethod` as `lookup`](https://access.redhat.com/solutions/7072510)

</div>
