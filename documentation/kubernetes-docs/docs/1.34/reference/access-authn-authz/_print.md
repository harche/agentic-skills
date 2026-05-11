This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/reference/access-authn-authz/).

# API Access Control

* 1: [Authenticating](#pg-a6264859a5ad6e2f4a6e4cff9ce4fa8b)
* 2: [Authenticating with Bootstrap Tokens](#pg-de45b6ca7419a0e308044425b2ac52bb)
* 3: [Authorization](#pg-342be69d36f174f762c36f4fe11fcb20)
* 4: [Using RBAC Authorization](#pg-954776b47f2d90515f375623a0ce98e1)
* 5: [Using Node Authorization](#pg-9cbb97d4d9f08d67931a1baae4e6519c)
* 6: [Webhook Mode](#pg-215c25173044b8f97e9b0494b0c7e53f)
* 7: [Using ABAC Authorization](#pg-a5bdc757c01991e5e6ab1a82b90639ea)
* 8: [Admission Control in Kubernetes](#pg-518807b9b00bda46d7c7e6e0b17c18f8)
* 9: [Dynamic Admission Control](#pg-d04751f776f1faa6a82bbb7f0a200950)
* 10: [Managing Service Accounts](#pg-bea207258f3576b8ec7444a20d498e1d)
* 11: [Certificates and Certificate Signing Requests](#pg-3d0c14d1e3cfade38febc343cd044c73)
* 12: [Mapping PodSecurityPolicies to Pod Security Standards](#pg-643e4cec52a8577e9454649bdaac84d0)
* 13: [Kubelet authentication/authorization](#pg-36e1423f0b5caa8eafeb6f53c175d13c)
* 14: [TLS bootstrapping](#pg-d17c42b1760f6d5c333fc91ca9b453f4)
* 15: [Mutating Admission Policy](#pg-d3609999485b1c57de7445f9a47d9799)
* 16: [Validating Admission Policy](#pg-7b9fccf8215aea0edc5c97e72f1f72e4)

For an introduction to how Kubernetes implements and controls API access,
read [Controlling Access to the Kubernetes API](/docs/concepts/security/controlling-access/).

Reference documentation:

* [Authenticating](/docs/reference/access-authn-authz/authentication/)
  + [Authenticating with Bootstrap Tokens](/docs/reference/access-authn-authz/bootstrap-tokens/)
* [Admission Controllers](/docs/reference/access-authn-authz/admission-controllers/)
  + [Dynamic Admission Control](/docs/reference/access-authn-authz/extensible-admission-controllers/)
* [Authorization](/docs/reference/access-authn-authz/authorization/)
  + [Role Based Access Control](/docs/reference/access-authn-authz/rbac/)
  + [Attribute Based Access Control](/docs/reference/access-authn-authz/abac/)
  + [Node Authorization](/docs/reference/access-authn-authz/node/)
  + [Webhook Authorization](/docs/reference/access-authn-authz/webhook/)
* [Certificate Signing Requests](/docs/reference/access-authn-authz/certificate-signing-requests/)
  + including [CSR approval](/docs/reference/access-authn-authz/certificate-signing-requests/#approval-rejection)
    and [certificate signing](/docs/reference/access-authn-authz/certificate-signing-requests/#signing)
* Service accounts
  + [Developer guide](/docs/tasks/configure-pod-container/configure-service-account/)
  + [Administration](/docs/reference/access-authn-authz/service-accounts-admin/)
* [Kubelet Authentication & Authorization](/docs/reference/access-authn-authz/kubelet-authn-authz/)
  + including kubelet [TLS bootstrapping](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/)
