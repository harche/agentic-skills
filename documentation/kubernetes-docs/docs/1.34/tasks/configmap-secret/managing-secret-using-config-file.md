# Managing Secrets using Configuration File

Creating Secret objects using resource configuration file.

## Before you begin

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [KodeKloud](https://kodekloud.com/public-playgrounds)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)

## Create the Secret

You can define the `Secret` object in a manifest first, in JSON or YAML format,
and then create that object. The
[Secret](/docs/reference/generated/kubernetes-api/v1.34/#secret-v1-core)
resource contains two maps: `data` and `stringData`.
The `data` field is used to store arbitrary data, encoded using base64. The
`stringData` field is provided for convenience, and it allows you to provide
the same data as unencoded strings.
The keys of `data` and `stringData` must consist of alphanumeric characters,
`-`, `_` or `.`.

The following example stores two strings in a Secret using the `data` field.

1. Convert the strings to base64:

   ```
   echo -n 'admin' | base64
   echo -n '1f2d1e2e67df' | base64
   ```

   > **Note:**
   > The serialized JSON and YAML values of Secret data are encoded as base64 strings. Newlines are not valid within these strings and must be omitted. When using the `base64` utility on Darwin/macOS, users should avoid using the `-b` option to split long lines. Conversely, Linux users *should* add the option `-w 0` to `base64` commands or the pipeline `base64 | tr -d '\n'` if the `-w` option is not available.

   The output is similar to:

   ```
   YWRtaW4=
   MWYyZDFlMmU2N2Rm
   ```
2. Create the manifest:

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: mysecret
   type: Opaque
   data:
     username: YWRtaW4=
     password: MWYyZDFlMmU2N2Rm
   ```

   Note that the name of a Secret object must be a valid
   [DNS subdomain name](/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).
3. Create the Secret using [`kubectl apply`](/docs/reference/generated/kubectl/kubectl-commands#apply):

   ```
   kubectl apply -f ./secret.yaml
   ```

   The output is similar to:

   ```
   secret/mysecret created
   ```

To verify that the Secret was created and to decode the Secret data, refer to
[Managing Secrets using kubectl](/docs/tasks/configmap-secret/managing-secret-using-kubectl/#verify-the-secret).

### Specify unencoded data when creating a Secret

For certain scenarios, you may wish to use the `stringData` field instead. This
field allows you to put a non-base64 encoded string directly into the Secret,
and the string will be encoded for you when the Secret is created or updated.

A practical example of this might be where you are deploying an application
that uses a Secret to store a configuration file, and you want to populate
parts of that configuration file during your deployment process.

For example, if your application uses the following configuration file:

```
apiUrl: "https://my.api.com/api/v1"
username: "<user>"
password: "<password>"
```

You could store this in a Secret using the following definition:

```
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
stringData:
  config.yaml: |
    apiUrl: "https://my.api.com/api/v1"
    username: <user>
    password: <password>
```

> **Note:**
> The `stringData` field for a Secret does not work well with server-side apply.

When you retrieve the Secret data, the command returns the encoded values,
and not the plaintext values you provided in `stringData`.

For example, if you run the following command:

```
kubectl get secret mysecret -o yaml
```

The output is similar to:

```
apiVersion: v1
data:
  config.yaml: YXBpVXJsOiAiaHR0cHM6Ly9teS5hcGkuY29tL2FwaS92MSIKdXNlcm5hbWU6IHt7dXNlcm5hbWV9fQpwYXNzd29yZDoge3twYXNzd29yZH19
kind: Secret
metadata:
  creationTimestamp: 2018-11-15T20:40:59Z
  name: mysecret
  namespace: default
  resourceVersion: "7225"
  uid: c280ad2e-e916-11e8-98f2-025000000001
type: Opaque
```

### Specify both `data` and `stringData`

If you specify a field in both `data` and `stringData`, the value from `stringData` is used.

For example, if you define the following Secret:

```
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  username: YWRtaW4=
stringData:
  username: administrator
```

> **Note:**
> The `stringData` field for a Secret does not work well with server-side apply.

The `Secret` object is created as follows:

```
apiVersion: v1
data:
  username: YWRtaW5pc3RyYXRvcg==
kind: Secret
metadata:
  creationTimestamp: 2018-11-15T20:46:46Z
  name: mysecret
  namespace: default
  resourceVersion: "7579"
  uid: 91460ecb-e917-11e8-98f2-025000000001
type: Opaque
```

`YWRtaW5pc3RyYXRvcg==` decodes to `administrator`.

## Edit a Secret

To edit the data in the Secret you created using a manifest, modify the `data`
or `stringData` field in your manifest and apply the file to your
cluster. You can edit an existing `Secret` object unless it is
[immutable](/docs/concepts/configuration/secret/#secret-immutable).

For example, if you want to change the password from the previous example to
`birdsarentreal`, do the following:

1. Encode the new password string:

   ```
   echo -n 'birdsarentreal' | base64
   ```

   The output is similar to:

   ```
   YmlyZHNhcmVudHJlYWw=
   ```
2. Update the `data` field with your new password string:

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: mysecret
   type: Opaque
   data:
     username: YWRtaW4=
     password: YmlyZHNhcmVudHJlYWw=
   ```
3. Apply the manifest to your cluster:

   ```
   kubectl apply -f ./secret.yaml
   ```

   The output is similar to:

   ```
   secret/mysecret configured
   ```

Kubernetes updates the existing `Secret` object. In detail, the `kubectl` tool
notices that there is an existing `Secret` object with the same name. `kubectl`
fetches the existing object, plans changes to it, and submits the changed
`Secret` object to your cluster control plane.

If you specified `kubectl apply --server-side` instead, `kubectl` uses
[Server Side Apply](/docs/reference/using-api/server-side-apply/) instead.

## Clean up

To delete the Secret you have created:

```
kubectl delete secret mysecret
```

## What's next

* Read more about the [Secret concept](/docs/concepts/configuration/secret/)
* Learn how to [manage Secrets using kubectl](/docs/tasks/configmap-secret/managing-secret-using-kubectl/)
* Learn how to [manage Secrets using kustomize](/docs/tasks/configmap-secret/managing-secret-using-kustomize/)

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
