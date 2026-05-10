<div wrapper="1" role="_abstract">

The External Secrets Operator for Red Hat OpenShift is a cluster-wide service that provides lifecycle management for secrets fetched from external secret management systems.

</div>

These release notes track the development of External Secrets Operator.

For more information, see [External Secrets Operator overview](../../security/external_secrets_operator/index.xml#external-secrets-operator-about).

# Release notes for External Secrets Operator for Red Hat OpenShift 1.1.0 (General Availability)

<div wrapper="1" role="_abstract">

External Secrets Operator for Red Hat OpenShift version 1.1.0 is based on the upstream external-secrets project, version v0.20.4. For more information, see the [external-secrets project release notes for v0.20.4](https://https://github.com/external-secrets/external-secrets/tree/v0.20.4).

</div>

Issued: 2026-03-17

The following advisories are available for the External Secrets Operator for Red Hat OpenShift 1.1.0:

- [RHBA-2026:5554](https://access.redhat.com/errata/RHBA-2026:5554)

- [RHBA-2026:5555](https://access.redhat.com/errata/RHBA-2026:5555)

- [RHBA-2026:5558](https://access.redhat.com/errata/RHBA-2026:5557)

- [RHBA-2026:5589](https://access.redhat.com/errata/RHBA-2026:5589)

## New features and enhancements

**Customization feature is now available for External Secrets Operator components**

With this release, the Operator API, `externalsecretsconfig.operator.openshift.io` allows users to customize various aspects of the `external-secrets` controllers. The new API allows users to add custom annotations and environment variables, and allows configuring revision history limits for the `external-secrets` deployments.

For more information, see [Customizing the External Secrets Operator for Red Hat OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/security_and_compliance/index#external-secrets-log-levels).

# Release notes for External Secrets Operator for Red Hat OpenShift 1.0.0 (General Availability)

<div wrapper="1" role="_abstract">

External Secrets Operator for Red Hat OpenShift version 1.0.0 is based on the upstream external-secrets project, version v0.19.0. For more information, see the [external-secrets project release notes for v0.19.0](https://github.com/external-secrets/external-secrets/releases/tag/v0.19.0).

</div>

Issued: 2025-11-03

The following advisories are available for the External Secrets Operator for Red Hat OpenShift 1.0.0:

- [RHBA-2025:19416](https://access.redhat.com/errata/RHBA-2025:19416)

- [RHBA-2025:19417](https://access.redhat.com/errata/RHBA-2025:19417)

- [RHBA-2025:19418](https://access.redhat.com/errata/RHBA-2025:19418)

- [RHBA-2025:19463](https://access.redhat.com/errata/RHBA-2025:19463)

## Fixed issues

- Before this release, many of the APIs listed in the console for the External Secrets Operator for Red Hat OpenShift were missing descriptions. With this release, the API descriptions have been added. ([OCPBUGS-61081](https://issues.redhat.com/browse/OCPBUGS-61081))

## New features and enhancements

**Renaming and improvements on the Operator API**

With this release, the Operator API, `externalsecrets.operator.openshift.io` has been renamed to `externalsecretsconfigs.operator.openshift.io` to avoid confusion with the external-secrets provided API that has the same name, but a different purpose. The external-secrets provided API has also been restructured and new features are added.

For more information, see [External Secrets Operator for Red Hat OpenShift APIs](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html-single/security_and_compliance/index#external-secrets-operator-api).

**Support to collect metrics of External Secrets Operator**

With this release, the External Secrets Operator for Red Hat OpenShift supports collecting metrics for both the Operator and operands. This is optional and must be enabled.

For more information, see [Monitoring the External Secrets Operator for Red Hat OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html-single/security_and_compliance/index#external-secrets-monitoring).

**Support to configure proxy for External Secrets Operator**

With this release, the External Secrets Operator for Red Hat OpenShift supports configuring proxy for both the Operator and operand.

For more information, see [About the egress proxy for the External Secrets Operator for Red Hat OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html-single/security_and_compliance/index#external-secrets-operator-proxy).

**Root filesystem is read-only for External Secrets Operator for Red Hat OpenShift containers**

With this release, to improve security, the External Secrets Operator for Red Hat OpenShift and all its operands have the `readOnlyRootFilesystem` security context set to true by default. This enhancement hardens the containers and prevents a potential attacker from modifying the contents of the container’s root file system.

**Network policy hardening is now available for External Secrets Operator components**

With this release, External Secrets Operator for Red Hat OpenShift includes pre-defined `NetworkPolicy` resources designed for enhanced security by governing ingress and egress traffic for operand components. These policies cover essential internal traffic, such as ingress to the metrics and webhook servers, and egress to the OpenShift API server and DNS server. Note that deployment of the `NetworkPolicy` is enabled by default and egress allow policies must be explicitly defined in the `ExternalSecretsConfig` custom resource for the `external-secrets` component to fetch secrets from external providers.

For more information, see [Configuring network policy for the operand](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html-single/security_and_compliance/index#external-secrets-operator-config-net-policy).

# Release notes for External Secrets Operator for Red Hat OpenShift 0.1.0 (Technology Preview)

<div wrapper="1" role="_abstract">

Version `0.1.0` of the External Secrets Operator for Red Hat OpenShift is based on the upstream external-secrets version `0.14.3`. For more information, see the [external-secrets project release notes for v0.14.3](https://github.com/external-secrets/external-secrets/releases/tag/v0.14.3).

</div>

Issued: 2025-06-26

The following advisories are available for the External Secrets Operator for Red Hat OpenShift 0.1.0:

- [RHBA-2025:9747](https://access.redhat.com/errata/RHBA-2025:9747)

- [RHBA-2025:9746](https://access.redhat.com/errata/RHBA-2025:9746)

- [RHBA-2025:9757](https://access.redhat.com/errata/RHBA-2025:9757)

- [RHBA-2025:9763](https://access.redhat.com/errata/RHBA-2025:9763)

## New features and enhancements

- This is the initial, Technology Preview release of the External Secrets Operator for Red Hat OpenShift.
