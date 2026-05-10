# Security overview

It is important to understand how to properly secure various aspects of your OpenShift Container Platform cluster.

## Container security

A good starting point to understanding OpenShift Container Platform security is to review the concepts in [Understanding container security](../security/container_security/security-understanding.xml#security-understanding). This and subsequent sections provide a high-level walkthrough of the container security measures available in OpenShift Container Platform, including solutions for the host layer, the container and orchestration layer, and the build and application layer. These sections also include information on the following topics:

- Why container security is important and how it compares with existing security standards.

- Which container security measures are provided by the host (RHCOS and RHEL) layer and which are provided by OpenShift Container Platform.

- How to evaluate your container content and sources for vulnerabilities.

- How to design your build and deployment process to proactively check container content.

- How to control access to containers through authentication and authorization.

- How networking and attached storage are secured in OpenShift Container Platform.

- Containerized solutions for API management and SSO.

## Auditing

OpenShift Container Platform auditing provides a security-relevant chronological set of records documenting the sequence of activities that have affected the system by individual users, administrators, or other components of the system. Administrators can [configure the audit log policy](../security/audit-log-policy-config.xml#audit-log-policy-config) and [view audit logs](../security/audit-log-view.xml#audit-log-view).

## Certificates

Certificates are used by various components to validate access to the cluster. Administrators can [replace the default ingress certificate](../security/certificates/replacing-default-ingress-certificate.xml#replacing-default-ingress), [add API server certificates](../security/certificates/api-server.xml#api-server-certificates), or [add a service certificate](../security/certificates/service-serving-certificate.xml#add-service-serving).

You can also review more details about the types of certificates used by the cluster:

- [User-provided certificates for the API server](../security/certificate_types_descriptions/user-provided-certificates-for-api-server.xml#cert-types-user-provided-certificates-for-the-api-server)

- [Proxy certificates](../security/certificate_types_descriptions/proxy-certificates.xml#cert-types-proxy-certificates)

- [Service CA certificates](../security/certificate_types_descriptions/service-ca-certificates.xml#cert-types-service-ca-certificates)

- [Node certificates](../security/certificate_types_descriptions/node-certificates.xml#cert-types-node-certificates)

- [Bootstrap certificates](../security/certificate_types_descriptions/bootstrap-certificates.xml#cert-types-bootstrap-certificates)

- [etcd certificates](../security/certificate_types_descriptions/etcd-certificates.xml#cert-types-etcd-certificates)

- [OLM certificates](../security/certificate_types_descriptions/olm-certificates.xml#cert-types-olm-certificates)

- [Aggregated API client certificates](../security/certificate_types_descriptions/aggregated-api-client-certificates.xml#cert-types-aggregated-api-client-certificates)

- [Machine Config Operator certificates](../security/certificate_types_descriptions/machine-config-operator-certificates.xml#cert-types-machine-config-operator-certificates)

- [User-provided certificates for default ingress](../security/certificate_types_descriptions/user-provided-certificates-for-default-ingress.xml#cert-types-user-provided-certificates-for-default-ingress)

- [Ingress certificates](../security/certificate_types_descriptions/ingress-certificates.xml#cert-types-ingress-certificates)

- [Monitoring and cluster logging Operator component certificates](../security/certificate_types_descriptions/monitoring-and-cluster-logging-operator-component-certificates.xml#cert-types-monitoring-and-cluster-logging-operator-component-certificates)

- [Control plane certificates](../security/certificate_types_descriptions/control-plane-certificates.xml#cert-types-control-plane-certificates)

## Encrypting data

You can [enable etcd encryption](../etcd/etcd-encrypt.xml#etcd-encrypt) for your cluster to provide an additional layer of data security. For example, it can help protect the loss of sensitive data if an etcd backup is exposed to the incorrect parties.

## Vulnerability scanning

Administrators can use the Red Hat Quay Container Security Operator to run [vulnerability scans](../security/pod-vulnerability-scan.xml#pod-vulnerability-scan) and review information about detected vulnerabilities.

# Compliance overview

For many OpenShift Container Platform customers, regulatory readiness, or compliance, on some level is required before any systems can be put into production. That regulatory readiness can be imposed by national standards, industry standards, or the organization’s corporate governance framework.

## Compliance checking

Administrators can use the [Compliance Operator](../security/compliance_operator/co-concepts/compliance-operator-understanding.xml#understanding-compliance-operator) to run compliance scans and recommend remediations for any issues found. The [`oc-compliance` plugin](../security/compliance_operator/co-scans/oc-compliance-plug-in-using.xml#using-oc-compliance-plug-in) is an OpenShift CLI (`oc`) plugin that provides a set of utilities to easily interact with the Compliance Operator.

## File integrity checking

Administrators can use the [File Integrity Operator](../security/file_integrity_operator/file-integrity-operator-understanding.xml#understanding-file-integrity-operator) to continually run file integrity checks on cluster nodes and provide a log of files that have been modified.

# Additional resources

- [Understanding authentication](../authentication/understanding-authentication.xml#understanding-authentication)

- [Configuring the internal OAuth server](../authentication/configuring-internal-oauth.xml#configuring-internal-oauth)

- [Understanding identity provider configuration](../authentication/understanding-identity-provider.xml#understanding-identity-provider)

- [Using RBAC to define and apply permissions](../authentication/using-rbac.xml#using-rbac)

- [Managing security context constraints](../authentication/managing-security-context-constraints.xml#managing-pod-security-policies)
