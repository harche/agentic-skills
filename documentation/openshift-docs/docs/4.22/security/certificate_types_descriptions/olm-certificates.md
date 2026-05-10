# Management

All certificates for Operator Lifecycle Manager (OLM) components (`olm-operator`, `catalog-operator`, `packageserver`, and `marketplace-operator`) are managed by the system.

When installing Operators that include webhooks or API services in their `ClusterServiceVersion` (CSV) object, OLM creates and rotates the certificates for these resources. Certificates for resources in the `openshift-operator-lifecycle-manager` namespace are managed by OLM.

OLM does not update the certificates of Operators that it manages in proxy environments. These certificates must be managed by the user using the subscription config.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Next steps

</div>

- [Configuring proxy support in Operator Lifecycle Manager](../../operators/admin/olm-configuring-proxy-support.xml#olm-configuring-proxy-support)

</div>

# Additional resources

- [Proxy certificates](../../security/certificate_types_descriptions/proxy-certificates.xml#cert-types-proxy-certificates)

- [Replacing the default ingress certificate](../../security/certificates/replacing-default-ingress-certificate.xml#replacing-default-ingress)

- [Updating the CA bundle](../../security/certificates/updating-ca-bundle.xml#updating-ca-bundle)
