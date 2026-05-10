<div wrapper="1" role="_abstract">

The Security Profiles Operator provides a way to define secure computing ([seccomp](http://kubernetes.io/docs/tutorials/security/seccomp/)) and SELinux profiles as custom resources, synchronizing profiles to every node in a given namespace.

</div>

These release notes track the development of the Security Profiles Operator in OpenShift Container Platform.

For an overview of the Security Profiles Operator, see [Security Profiles Operator Overview](../../security/security_profiles_operator/spo-overview.xml#spo-overview).

# Security Profiles Operator 0.10.0

The following advisory is available for the Security Profiles Operator 0.10.0: [RHSA-2026:2852 - OpenShift Security Profiles Operator update](http://access.redhat.com/errata/RHSA-2026:2852)

## Bug fixes

- In some instances when Security Profiles Operator (SPO) 0.9.0 was used with OpenShift Container Platform version 4.20 and above, SPO would create the `profilerecording` resource but the workload would fail. Failure of the workload prevented the creation of the needed container for running the Operator. With the 0.10.0 release of SPO. the `profilerecording` resource is reliably created, therefore the needed container for running the Operator is reliably created. [CMP-3537](https://issues.redhat.com/browse/CMP-3537).

- For version 0.9.0 of Security Profiles Operator (SPO), the `spod` pods would fail to run with the error message `fsmount:fscontext:proc/: could not get mount id: operation not permitted`. With the release of version 0.10.0, the `spod` pods run reliably. [CMP-4007](https://issues.redhat.com/browse/CMP-4007).

- In releases of SPO 0.9.0 and earlier, there was a bug in syntax of the `selinux` usage. With this release of SPO, the change is from `<policyName>_.process` to `<policyName>.process`. The new syntax omits the `_`. Examples in the documentation now show this updated usage. [CMP-4104](https://issues.redhat.com/browse/CMP-4104)

## New features and enhancements

- With the release of SPO v0.10.0, the Operator now supports Red Hat Enterprise Linux CoreOS (RHCOS) 10 containers. [CMP-4033](https://issues.redhat.com/browse/CMP-4033)

- In this release of the Security Profiles Operator, the Advanced Audit Logging Framework is available as a General Availability (GA) feature. The Advanced Audit Logging Framework uses the Audit JSON Log Enricher to capture and log terminal-based command activity in Red Hat Enterprise Linux CoreOS (RHCOS) containers, including `oc rsh`, `oc exec`, and `oc debug` commands. For more details, see [Advanced Audit Logging Framework](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/security_and_compliance/security-profiles-operator#spo-audit-logging_spo-advanced).

# Security Profiles Operator 0.9.0

The following advisory is available for the Security Profiles Operator 0.9.0: [RHBA-2025:15655 - OpenShift Security Profiles Operator update](http://access.redhat.com/errata/RHBA-2025:15655)

This update manages security profiles as cluster-wide resources rather than namespace resources. To update Security Profiles Operator to a version later than 0.8.6 requires manual migration. For migration instructions, see [Security Profiles Operator 0.9.0 Update Migration Guide](http://access.redhat.com/articles/7130594).

## Bug fixes

- Before this update, the spod pods could fail to start and enter into a `CrashLoopBackOff` state due to an error in parsing the semanage configuration file. This issue is caused by a change to the RHEL 9 image naming convention beginning in OpenShift Container Platform 4.19. ([OCPBUGS-55829](http://issues.redhat.com/browse/OCPBUGS-55829))

- Before this update, the Security Profiles Operator would fail to apply a `RawSelinuxProfile` to newly added nodes due to a reconciler type mismatch error. With this update, the operator now correctly handles `RawSelinuxProfile` objects and policies are applied to all nodes as expected. ([OCPBUGS-33718](http://issues.redhat.com/browse/OCPBUGS-33718))

# Security Profiles Operator 0.8.6

The following advisory is available for the Security Profiles Operator 0.8.6:

- [RHBA-2024:10380 - OpenShift Security Profiles Operator update](http://access.redhat.com/errata/RHBA-2024:10380)

This update includes upgraded dependencies in underlying base images.

# Security Profiles Operator 0.8.5

The following advisory is available for the Security Profiles Operator 0.8.5:

- [RHBA-2024:5016 - OpenShift Security Profiles Operator bug fix update](http://access.redhat.com/errata/RHBA-2024:5016)

## Bug fixes

- When attempting to install the Security Profile Operator from the web console, the option to enable Operator-recommended cluster monitoring was unavailable for the namespace. With this update, you can now enabled Operator-recommend cluster monitoring in the namespace. ([OCPBUGS-37794](http://issues.redhat.com/browse/OCPBUGS-37794))

- Previously, the Security Profiles Operator would intermittently be not visible in the OperatorHub, which caused limited access to install the Operator via the web console. With this update, the Security Profiles Operator is present in the OperatorHub.

# Security Profiles Operator 0.8.4

The following advisory is available for the Security Profiles Operator 0.8.4:

- [RHBA-2024:4781 - OpenShift Security Profiles Operator bug fix update](http://access.redhat.com/errata/RHBA-2024:4781)

This update addresses CVEs in underlying dependencies.

## New features and enhancements

- You can now specify a default security profile in the `image` attribute of a `ProfileBinding` object by setting a wildcard. For more information, see [Binding workloads to profiles with ProfileBindings (SELinux)](../../security/security_profiles_operator/spo-selinux.xml#spo-binding-workloads_spo-selinux) and [Binding workloads to profiles with ProfileBindings (Seccomp)](../../security/security_profiles_operator/spo-seccomp.xml#spo-binding-workloads_spo-seccomp).

# Security Profiles Operator 0.8.2

The following advisory is available for the Security Profiles Operator 0.8.2:

- [RHBA-2023:5958 - OpenShift Security Profiles Operator bug fix update](http://access.redhat.com/errata/RHBA-2023:5958)

## Bug fixes

- Previously, `SELinuxProfile` objects did not inherit custom attributes from the same namespace. With this update, the issue has now been resolved and `SELinuxProfile` object attributes are inherited from the same namespace as expected. ([OCPBUGS-17164](http://issues.redhat.com/browse/OCPBUGS-17164))

- Previously, RawSELinuxProfiles would hang during the creation process and would not reach an `Installed` state. With this update, the issue has been resolved and RawSELinuxProfiles are created successfully. ([**OCPBUGS-19744**](http://issues.redhat.com/browse/OCPBUGS-19744))

- Previously, patching the `enableLogEnricher` to `true` would cause the `seccompProfile` `log-enricher-trace` pods to be stuck in a `Pending` state. With this update, `log-enricher-trace` pods reach an `Installed` state as expected. ([OCPBUGS-22182](http://issues.redhat.com/browse/OCPBUGS-22182))

- Previously, the Security Profiles Operator generated high cardinality metrics, causing Prometheus pods using high amounts of memory. With this update, the following metrics will no longer apply in the Security Profiles Operator namespace:

  - `rest_client_request_duration_seconds`

  - `rest_client_request_size_bytes`

  - `rest_client_response_size_bytes`

    ([**OCPBUGS-22406**](http://issues.redhat.com/browse/OCPBUGS-22406))

# Security Profiles Operator 0.8.0

The following advisory is available for the Security Profiles Operator 0.8.0:

- [RHBA-2023:4689 - OpenShift Security Profiles Operator bug fix update](http://access.redhat.com/errata/RHBA-2023:4689)

## Bug fixes

- Previously, while trying to install Security Profiles Operator in a disconnected cluster, the secure hashes provided were incorrect due to a SHA relabeling issue. With this update, the SHAs provided work consistently with disconnected environments. ([**OCPBUGS-14404**](http://issues.redhat.com/browse/OCPBUGS-14404))

# Security Profiles Operator 0.7.1

The following advisory is available for the Security Profiles Operator 0.7.1:

- [RHSA-2023:2029 - OpenShift Security Profiles Operator bug fix update](http://access.redhat.com/errata/RHSA-2023:2029)

## New features and enhancements

- Security Profiles Operator (SPO) now automatically selects the appropriate `selinuxd` image for RHEL 8- and 9-based Red Hat Enterprise Linux CoreOS (RHCOS) systems.

  > [!IMPORTANT]
  > Users that mirror images for disconnected environments must mirror both `selinuxd` images provided by the Security Profiles Operator.

- You can now enable memory optimization inside of an `spod` daemon. For more information, see [Enabling memory optimization in the spod daemon](../../security/security_profiles_operator/spo-advanced.xml#spo-memory-optimization_spo-advanced).

  > [!NOTE]
  > SPO memory optimization is not enabled by default.

- The daemon resource requirements are now configurable. For more information, see [Customizing daemon resource requirements](../../security/security_profiles_operator/spo-advanced.xml#spo-daemon-requirements_spo-advanced).

- The priority class name is now configurable in the `spod` configuration. For more information, see [Setting a custom priority class name for the spod daemon pod](../../security/security_profiles_operator/spo-advanced.xml#spo-custom-priority-class_spo-advanced).

## Deprecated and removed features

- The default `nginx-1.19.1` seccomp profile is now removed from the Security Profiles Operator deployment.

## Bug fixes

- Previously, a Security Profiles Operator (SPO) SELinux policy did not inherit low-level policy definitions from the container template. If you selected another template, such as net_container, the policy would not work because it required low-level policy definitions that only existed in the container template. This issue occurred when the SPO SELinux policy attempted to translate SELinux policies from the SPO custom format to the Common Intermediate Language (CIL) format. With this update, the container template appends to any SELinux policies that require translation from SPO to CIL. Additionally, the SPO SELinux policy can inherit low-level policy definitions from any supported policy template. ([**OCPBUGS-12879**](http://issues.redhat.com/browse/OCPBUGS-12879))

## Known issue

- When uninstalling the Security Profiles Operator, the `MutatingWebhookConfiguration` object is not deleted and must be manually removed. As a workaround, delete the `MutatingWebhookConfiguration` object after uninstalling the Security Profiles Operator. These steps are defined in [Uninstalling the Security Profiles Operator](../../security/security_profiles_operator/spo-uninstalling.xml#spo-uninstalling). ([**OCPBUGS-4687**](http://issues.redhat.com/browse/OCPBUGS-4687))

# Security Profiles Operator 0.5.2

The following advisory is available for the Security Profiles Operator 0.5.2:

- [RHBA-2023:0788 - OpenShift Security Profiles Operator bug fix update](http://access.redhat.com/errata/RHBA-2023:0788)

This update addresses a CVE in an underlying dependency.

## Known issue

- When uninstalling the Security Profiles Operator, the `MutatingWebhookConfiguration` object is not deleted and must be manually removed. As a workaround, delete the `MutatingWebhookConfiguration` object after uninstalling the Security Profiles Operator. These steps are defined in [Uninstalling the Security Profiles Operator](../../security/security_profiles_operator/spo-uninstalling.xml#spo-uninstalling). ([OCPBUGS-4687](http://issues.redhat.com/browse/OCPBUGS-4687))

# Security Profiles Operator 0.5.0

The following advisory is available for the Security Profiles Operator 0.5.0:

- [RHBA-2022:8762 - OpenShift Security Profiles Operator bug fix update](http://access.redhat.com/errata/RHBA-2022:8762)

## Known issue

- When uninstalling the Security Profiles Operator, the `MutatingWebhookConfiguration` object is not deleted and must be manually removed. As a workaround, delete the `MutatingWebhookConfiguration` object after uninstalling the Security Profiles Operator. These steps are defined in [Uninstalling the Security Profiles Operator](../../security/security_profiles_operator/spo-uninstalling.xml#spo-uninstalling). ([OCPBUGS-4687](http://issues.redhat.com/browse/OCPBUGS-4687))
