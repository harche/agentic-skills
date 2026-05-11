# Cloud Native Security and Kubernetes

Concepts for keeping your cloud native workload secure.

Kubernetes is based on a cloud native architecture and draws on advice from the
[CNCF](https://cncf.io/ "Cloud Native Computing Foundation") about good practices for
cloud native information security.

Read on for an overview of how Kubernetes is designed to help you deploy a
secure cloud native platform.

## Cloud native information security

The CNCF [white paper](https://github.com/cncf/tag-security/blob/main/community/resources/security-whitepaper/v2/CNCF_cloud-native-security-whitepaper-May2022-v2.pdf)
on cloud native security defines security controls and practices that are
appropriate to different *lifecycle phases*.

## *Develop* lifecycle phase

* Ensure the integrity of development environments.
* Design applications following good practices for information security,
  appropriate for your context.
* Consider end user security as part of solution design.

To achieve this, you can:

1. Adopt an architecture, such as [zero trust](https://glossary.cncf.io/zero-trust-architecture/),
   that minimizes attack surfaces, even for internal threats.
2. Define a code review process that considers security concerns.
3. Build a *threat model* of your system or application that identifies
   trust boundaries. Use that threat model to identify risks and determine
   how to treat them.
4. Incorporate advanced security automation, such as *fuzzing* and
   [security chaos engineering](https://glossary.cncf.io/security-chaos-engineering/),
   where it's justified.

## *Distribute* lifecycle phase

* Ensure the security of the supply chain for container images you execute.
* Ensure the security of the supply chain for the cluster and other components
  that execute your application. For example, this might include an external
  database that your cloud native application uses for persistence.

To achieve this, you can:

1. Scan container images and other artifacts for known vulnerabilities.
2. Ensure that software distribution uses encryption in transit, with
   a chain of trust for the software source.
3. Adopt and follow processes to update dependencies when updates are
   available, especially in response to security announcements.
4. Use validation mechanisms such as digital certificates for supply
   chain assurance.
5. Subscribe to feeds and other mechanisms to alert you to security
   risks.
6. Restrict access to artifacts. Place container images in a
   [private registry](/docs/concepts/containers/images/#using-a-private-registry)
   that only allows authorized clients to pull images.

## *Deploy* lifecycle phase

Ensure appropriate restrictions on what can be deployed, who can deploy it,
and where it can be deployed.
You can enforce measures from the *distribute* phase, such as verifying the
cryptographic identity of container image artifacts.

You can deploy different applications and cluster components into different
[namespaces](/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster."). Containers
and namespaces both provide isolation mechanisms that are relevant to
information security.

When you deploy Kubernetes, you also set the foundation for your
applications' runtime environment: a Kubernetes cluster (or
multiple clusters).
That infrastructure must provide the security guarantees that higher
layers expect.

## *Runtime* lifecycle phase

The Runtime phase comprises three critical areas: [access](#protection-runtime-access),
[compute](#protection-runtime-compute), and [storage](#protection-runtime-storage).

### Runtime protection: access

The Kubernetes API is what makes your cluster work. Protecting this API is key
to providing effective cluster security.

Other pages in the Kubernetes documentation have more detail about how to set up
specific aspects of access control. The [security checklist](/docs/concepts/security/security-checklist/)
provides suggested basic checks for your cluster.

Beyond that, securing your cluster means implementing effective
[authentication](/docs/concepts/security/controlling-access/#authentication) and
[authorization](/docs/concepts/security/controlling-access/#authorization) for API access. Use [ServiceAccounts](/docs/concepts/security/service-accounts/) to
provide and manage security identities for workloads and cluster
components.

Kubernetes uses TLS to protect API traffic; make sure to deploy the cluster using
TLS (including for traffic between nodes and the control plane) and protect the
encryption keys. If you use Kubernetes' own API for
[CertificateSigningRequests](/docs/reference/access-authn-authz/certificate-signing-requests/#certificate-signing-requests),
pay special attention to restricting misuse there.

### Runtime protection: compute

[Containers](/docs/concepts/containers/ "A lightweight and portable executable image that contains software and all of its dependencies.") provide two
things: isolation between applications and a mechanism to combine
those isolated applications to run on the same host computer. Those two
aspects—isolation and aggregation—mean that runtime security involves
identifying trade-offs and finding an appropriate balance.

Kubernetes relies on a [container runtime](/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.")
to set up and run containers. The Kubernetes project does
not recommend a specific container runtime, and you should make sure that
the runtime(s) you choose meet your information security needs.

To protect your compute at runtime, you can:

1. Enforce [Pod Security Standards](/docs/concepts/security/pod-security-standards/)
   for applications to help ensure they run with only the necessary privileges.
2. Run a specialized operating system on your nodes that is designed specifically
   for running containerized workloads. This is typically based on a read-only
   operating system (*immutable image*) that provides only the services
   essential for running containers.

   Container-specific operating systems help isolate system components and
   present a reduced attack surface in case of a container escape.
3. Define [ResourceQuotas](/docs/concepts/policy/resource-quotas/) to
   fairly allocate shared resources, and use
   mechanisms such as [LimitRanges](/docs/concepts/policy/limit-range/)
   to ensure that Pods specify their resource requirements.
4. Partition workloads across different nodes to improve isolation.
   Use [node isolation](/docs/concepts/scheduling-eviction/assign-pod-node/#node-isolation-restriction)
   mechanisms, either from Kubernetes itself or from the ecosystem, to ensure that
   Pods with different trust contexts run on separate sets of nodes.
5. Use a [container runtime](/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.")
   that provides security restrictions.
6. On Linux nodes, use a Linux security module such as [AppArmor](/docs/tutorials/security/apparmor/)
   or [seccomp](/docs/tutorials/security/seccomp/).

### Runtime protection: storage

To protect storage for your cluster and the applications that run there, you can:

1. Integrate your cluster with an external storage plugin that provides encryption at
   rest for volumes.
2. Enable [encryption at rest](/docs/tasks/administer-cluster/encrypt-data/) for
   API objects.
3. Protect data durability using backups, and verify that you can restore them whenever needed.
4. Authenticate connections between cluster nodes and any network storage they rely
   upon.
5. Implement data encryption within your own application.

For encryption keys, generating these within specialized hardware provides
the best protection against disclosure risks. A *hardware security module*
can let you perform cryptographic operations without allowing the security
key to be copied elsewhere.

### Networking and security

You should also consider network security measures, such as
[NetworkPolicy](/docs/concepts/services-networking/network-policies/) or a
[service mesh](https://glossary.cncf.io/service-mesh/).
Some network plugins for Kubernetes provide encryption for your
cluster network using technologies such as a virtual
private network (VPN) overlay.
By design, Kubernetes lets you use your own networking plugin for your
cluster. If you use managed Kubernetes, the provider may have already selected a
network plugin for you.

The network plugin you choose and the way you integrate it can have a
strong impact on the security of information in transit.

### Observability and runtime security

Kubernetes lets you extend your cluster with extra tooling. You can set up third
party solutions to help you monitor or troubleshoot your applications and the
clusters they are running. You also get some basic observability features built
in to Kubernetes itself. Your code running in containers can generate logs,
publish metrics, or provide other observability data; at deploy time, you need to
make sure your cluster provides an appropriate level of protection there.

If you set up a metrics dashboard or something similar, review the chain of components
that populate data into that dashboard, as well as the dashboard itself. Make sure
that the whole chain is designed with enough resilience and integrity protection
that you can rely on it even during an incident where your cluster might be degraded.

Where appropriate, deploy security measures below the Kubernetes layer,
such as cryptographically measured boot or authenticated distribution
of time (which helps ensure the fidelity of logs and audit records).

For a high-assurance environment, deploy cryptographic protections to ensure that
logs are both tamper-proof and confidential.

## What's next

### Cloud native security

* CNCF [white paper](https://github.com/cncf/tag-security/blob/main/community/resources/security-whitepaper/v2/CNCF_cloud-native-security-whitepaper-May2022-v2.pdf)
  on cloud native security.
* CNCF [white paper](https://github.com/cncf/tag-security/blob/f80844baaea22a358f5b20dca52cd6f72a32b066/supply-chain-security/supply-chain-security-paper/CNCF_SSCP_v1.pdf)
  on good practices for securing a software supply chain.
* [Fixing the Kubernetes clusterf**k: Understanding security from the kernel up](https://archive.fosdem.org/2020/schedule/event/kubernetes/) (FOSDEM 2020)
* [Kubernetes Security Best Practices](https://www.youtube.com/watch?v=wqsUfvRyYpw) (Kubernetes Forum Seoul 2019)
* [Towards Measured Boot Out of the Box](https://www.youtube.com/watch?v=EzSkU3Oecuw) (Linux Security Summit 2016)

### Kubernetes and information security

* [Kubernetes security](/docs/concepts/security/)
* [Securing your cluster](/docs/tasks/administer-cluster/securing-a-cluster/)
* [Data encryption in transit](/docs/tasks/tls/managing-tls-in-a-cluster/) for the control plane
* [Data encryption at rest](/docs/tasks/administer-cluster/encrypt-data/)
* [Secrets in Kubernetes](/docs/concepts/configuration/secret/)
* [Controlling Access to the Kubernetes API](/docs/concepts/security/controlling-access/)
* [Network policies](/docs/concepts/services-networking/network-policies/) for Pods
* [Pod security standards](/docs/concepts/security/pod-security-standards/)
* [RuntimeClasses](/docs/concepts/containers/runtime-class/)

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
