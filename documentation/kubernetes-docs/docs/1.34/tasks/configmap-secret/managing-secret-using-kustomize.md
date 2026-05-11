# Managing Secrets using Kustomize

Creating Secret objects using kustomization.yaml file.

`kubectl` supports using the [Kustomize object management tool](/docs/tasks/manage-kubernetes-objects/kustomization/) to manage Secrets
and ConfigMaps. You create a *resource generator* using Kustomize, which
generates a Secret that you can apply to the API server using `kubectl`.

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

## Create a Secret

You can generate a Secret by defining a `secretGenerator` in a
`kustomization.yaml` file that references other existing files, `.env` files, or
literal values. For example, the following instructions create a kustomization
file for the username `admin` and the password `1f2d1e2e67df`.

> **Note:**
> The `stringData` field for a Secret does not work well with server-side apply.

### Create the kustomization file

* Literals
  * Files
    * .env files

```
secretGenerator:
- name: database-creds
  literals:
  - username=admin
  - password=1f2d1e2e67df
```

1. Store the credentials in files. The filenames are the keys of the secret:

   ```
   echo -n 'admin' > ./username.txt
   echo -n '1f2d1e2e67df' > ./password.txt
   ```

   The `-n` flag ensures that there's no newline character at the end of your
   files.
2. Create the `kustomization.yaml` file:

   ```
   secretGenerator:
   - name: database-creds
     files:
     - username.txt
     - password.txt
   ```

You can also define the secretGenerator in the `kustomization.yaml` file by
providing `.env` files. For example, the following `kustomization.yaml` file
pulls in data from an `.env.secret` file:

```
secretGenerator:
- name: db-user-pass
  envs:
  - .env.secret
```

In all cases, you don't need to encode the values in base64. The name of the YAML
file **must** be `kustomization.yaml` or `kustomization.yml`.

### Apply the kustomization file

To create the Secret, apply the directory that contains the kustomization file:

```
kubectl apply -k <directory-path>
```

The output is similar to:

```
secret/database-creds-5hdh7hhgfk created
```

When a Secret is generated, the Secret name is created by hashing
the Secret data and appending the hash value to the name. This ensures that
a new Secret is generated each time the data is modified.

To verify that the Secret was created and to decode the Secret data,

```
kubectl get -k <directory-path> -o jsonpath='{.data}'
```

The output is similar to:

```
{ "password": "MWYyZDFlMmU2N2Rm", "username": "YWRtaW4=" }
```

```
echo 'MWYyZDFlMmU2N2Rm' | base64 --decode
```

The output is similar to:

```
1f2d1e2e67df
```

For more information, refer to
[Managing Secrets using kubectl](/docs/tasks/configmap-secret/managing-secret-using-kubectl/#verify-the-secret) and
[Declarative Management of Kubernetes Objects Using Kustomize](/docs/tasks/manage-kubernetes-objects/kustomization/).

## Edit a Secret

1. In your `kustomization.yaml` file, modify the data, such as the `password`.
2. Apply the directory that contains the kustomization file:

   ```
   kubectl apply -k <directory-path>
   ```

   The output is similar to:

   ```
   secret/db-user-pass-6f24b56cc8 created
   ```

The edited Secret is created as a new `Secret` object, instead of updating the
existing `Secret` object. You might need to update references to the Secret in
your Pods.

## Clean up

To delete a Secret, use `kubectl`:

```
kubectl delete secret db-user-pass
```

## What's next

* Read more about the [Secret concept](/docs/concepts/configuration/secret/)
* Learn how to [manage Secrets using kubectl](/docs/tasks/configmap-secret/managing-secret-using-kubectl/)
* Learn how to [manage Secrets using config file](/docs/tasks/configmap-secret/managing-secret-using-config-file/)

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
