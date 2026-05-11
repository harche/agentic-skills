OpenShift Container Platform Security Profiles Operator (SPO) provides a way to define secure computing ([seccomp](https://kubernetes.io/docs/tutorials/security/seccomp/)) profiles and SELinux profiles as custom resources, synchronizing profiles to every node in a given namespace. For the latest updates, see the [release notes](../../security/security_profiles_operator/spo-release-notes.xml#spo-release-notes).

The SPO can distribute custom resources to each node while a reconciliation loop ensures that the profiles stay up-to-date. See [Understanding the Security Profiles Operator](../../security/security_profiles_operator/spo-understanding.xml#spo-understanding).

The SPO manages SELinux policies and seccomp profiles for namespaced workloads. For more information, see [Enabling the Security Profiles Operator](../../security/security_profiles_operator/spo-enabling.xml#spo-enabling).

You can create [seccomp](../../security/security_profiles_operator/spo-seccomp.xml#spo-seccomp) and [SELinux](../../security/security_profiles_operator/spo-selinux.xml#spo-selinux) profiles, bind policies to pods, record workloads, and synchronize all worker nodes in a namespace.

Use [Advanced Security Profile Operator tasks](../../security/security_profiles_operator/spo-advanced.xml#spo-advanced) to enable the log enricher, configure webhooks and metrics, or restrict profiles to a single namespace.

Use [SPO Advanced Audit Logging](../../security/security_profiles_operator/spo-logging.xml#spo-advanced) to access logs in RHCOS containers for container-level security audit features.

[Troubleshoot the Security Profiles Operator](../../security/security_profiles_operator/spo-troubleshooting.xml#spo-inspecting-seccomp-profiles_spo-troubleshooting) as needed, or engage [Red Hat support](https://access.redhat.com/support/).

You can [Uninstall the Security Profiles Operator](../../security/security_profiles_operator/spo-uninstalling.xml#spo-uninstalling) by removing the profiles before removing the Operator.
