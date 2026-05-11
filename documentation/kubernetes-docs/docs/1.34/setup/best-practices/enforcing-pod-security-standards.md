# Enforcing Pod Security Standards

This page provides an overview of best practices when it comes to enforcing
[Pod Security Standards](/docs/concepts/security/pod-security-standards/).

## Using the built-in Pod Security Admission Controller

FEATURE STATE:
`Kubernetes v1.25 [stable]`

The [Pod Security Admission Controller](/docs/reference/access-authn-authz/admission-controllers/#podsecurity)
intends to replace the deprecated PodSecurityPolicies.

### Configure all cluster namespaces

Namespaces that lack any configuration at all should be considered significant gaps in your cluster
security model. We recommend taking the time to analyze the types of workloads occurring in each
namespace, and by referencing the Pod Security Standards, decide on an appropriate level for
each of them. Unlabeled namespaces should only indicate that they've yet to be evaluated.

In the scenario that all workloads in all namespaces have the same security requirements,
we provide an [example](/docs/tasks/configure-pod-container/enforce-standards-namespace-labels/#applying-to-all-namespaces)
that illustrates how the PodSecurity labels can be applied in bulk.

### Embrace the principle of least privilege

In an ideal world, every pod in every namespace would meet the requirements of the `restricted`
policy. However, this is not possible nor practical, as some workloads will require elevated
privileges for legitimate reasons.

* Namespaces allowing `privileged` workloads should establish and enforce appropriate access controls.
* For workloads running in those permissive namespaces, maintain documentation about their unique
  security requirements. If at all possible, consider how those requirements could be further
  constrained.

### Adopt a multi-mode strategy

The `audit` and `warn` modes of the Pod Security Standards admission controller make it easy to
collect important security insights about your pods without breaking existing workloads.

It is good practice to enable these modes for all namespaces, setting them to the *desired* level
and version you would eventually like to `enforce`. The warnings and audit annotations generated in
this phase can guide you toward that state. If you expect workload authors to make changes to fit
within the desired level, enable the `warn` mode. If you expect to use audit logs to monitor/drive
changes to fit within the desired level, enable the `audit` mode.

When you have the `enforce` mode set to your desired value, these modes can still be useful in a
few different ways:

* By setting `warn` to the same level as `enforce`, clients will receive warnings when attempting
  to create Pods (or resources that have Pod templates) that do not pass validation. This will help
  them update those resources to become compliant.
* In Namespaces that pin `enforce` to a specific non-latest version, setting the `audit` and `warn`
  modes to the same level as `enforce`, but to the `latest` version, gives visibility into settings
  that were allowed by previous versions but are not allowed per current best practices.

## Third-party alternatives

> **Note:**
> **Note:** This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](/docs/contribute/style/content-guide/#third-party-content) before submitting a change. [More information.](#third-party-content-disclaimer)

Other alternatives for enforcing security profiles are being developed in the Kubernetes
ecosystem:

* [Kubewarden](https://github.com/kubewarden).
* [Kyverno](https://kyverno.io/policies/).
* [OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper).

The decision to go with a *built-in* solution (e.g. PodSecurity admission controller) versus a
third-party tool is entirely dependent on your own situation. When evaluating any solution,
trust of your supply chain is crucial. Ultimately, using *any* of the aforementioned approaches
will be better than doing nothing.

Items on this page refer to third party products or projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for those third-party products or projects. See the [CNCF website guidelines](https://github.com/cncf/foundation/blob/master/website-guidelines.md) for more details.

You should read the [content guide](/docs/contribute/style/content-guide/#third-party-content) before proposing a change that adds an extra third-party link.

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
