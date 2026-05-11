# Apply Pod Security Standards at the Namespace Level

> **Note**
> This tutorial applies only for new clusters.

Pod Security Admission is an admission controller that applies
[Pod Security Standards](/docs/concepts/security/pod-security-standards/)
when pods are created. It is a feature GA'ed in v1.25.
In this tutorial, you will enforce the `baseline` Pod Security Standard,
one namespace at a time.

You can also apply Pod Security Standards to multiple namespaces at once at the cluster
level. For instructions, refer to
[Apply Pod Security Standards at the cluster level](/docs/tutorials/security/cluster-level-pss/).

## Before you begin

Install the following on your workstation:

* [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
* [kubectl](/docs/tasks/tools/)

## Create cluster

1. Create a `kind` cluster as follows:

   ```
   kind create cluster --name psa-ns-level
   ```

   The output is similar to this:

   ```
   Creating cluster "psa-ns-level" ...
    ✓ Ensuring node image (kindest/node:v1.34.0) 🖼
    ✓ Preparing nodes 📦
    ✓ Writing configuration 📜
    ✓ Starting control-plane 🕹️
    ✓ Installing CNI 🔌
    ✓ Installing StorageClass 💾
   Set kubectl context to "kind-psa-ns-level"
   You can now use your cluster with:

   kubectl cluster-info --context kind-psa-ns-level

   Not sure what to do next? 😅  Check out https://kind.sigs.k8s.io/docs/user/quick-start/
   ```
2. Set the kubectl context to the new cluster:

   ```
   kubectl cluster-info --context kind-psa-ns-level
   ```

   The output is similar to this:

   ```
   Kubernetes control plane is running at https://127.0.0.1:50996
   CoreDNS is running at https://127.0.0.1:50996/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

   To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
   ```

## Create a namespace

Create a new namespace called `example`:

```
kubectl create ns example
```

The output is similar to this:

```
namespace/example created
```

## Enable Pod Security Standards checking for that namespace

1. Enable Pod Security Standards on this namespace using labels supported by
   built-in Pod Security Admission. In this step you will configure a check to
   warn on Pods that don't meet the latest version of the *baseline* pod
   security standard.

   ```
   kubectl label --overwrite ns example \
      pod-security.kubernetes.io/warn=baseline \
      pod-security.kubernetes.io/warn-version=latest
   ```
2. You can configure multiple pod security standard checks on any namespace, using labels.
   The following command will `enforce` the `baseline` Pod Security Standard, but
   `warn` and `audit` for `restricted` Pod Security Standards as per the latest
   version (default value)

   ```
   kubectl label --overwrite ns example \
     pod-security.kubernetes.io/enforce=baseline \
     pod-security.kubernetes.io/enforce-version=latest \
     pod-security.kubernetes.io/warn=restricted \
     pod-security.kubernetes.io/warn-version=latest \
     pod-security.kubernetes.io/audit=restricted \
     pod-security.kubernetes.io/audit-version=latest
   ```

## Verify the Pod Security Standard enforcement

1. Create a baseline Pod in the `example` namespace:

   ```
   kubectl apply -n example -f https://k8s.io/examples/security/example-baseline-pod.yaml
   ```

   The Pod does start OK; the output includes a warning. For example:

   ```
   Warning: would violate PodSecurity "restricted:latest": allowPrivilegeEscalation != false (container "nginx" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (container "nginx" must set securityContext.capabilities.drop=["ALL"]), runAsNonRoot != true (pod or container "nginx" must set securityContext.runAsNonRoot=true), seccompProfile (pod or container "nginx" must set securityContext.seccompProfile.type to "RuntimeDefault" or "Localhost")
   pod/nginx created
   ```
2. Create a baseline Pod in the `default` namespace:

   ```
   kubectl apply -n default -f https://k8s.io/examples/security/example-baseline-pod.yaml
   ```

   Output is similar to this:

   ```
   pod/nginx created
   ```

The Pod Security Standards enforcement and warning settings were applied only
to the `example` namespace. You could create the same Pod in the `default`
namespace with no warnings.

## Clean up

Now delete the cluster which you created above by running the following command:

```
kind delete cluster --name psa-ns-level
```

## What's next

* Run a
  [shell script](/examples/security/kind-with-namespace-level-baseline-pod-security.sh)
  to perform all the preceding steps all at once.

  1. Create kind cluster
  2. Create new namespace
  3. Apply `baseline` Pod Security Standard in `enforce` mode while applying
     `restricted` Pod Security Standard also in `warn` and `audit` mode.
  4. Create a new pod with the following pod security standards applied
* [Pod Security Admission](/docs/concepts/security/pod-security-admission/)
* [Pod Security Standards](/docs/concepts/security/pod-security-standards/)
* [Apply Pod Security Standards at the cluster level](/docs/tutorials/security/cluster-level-pss/)

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
