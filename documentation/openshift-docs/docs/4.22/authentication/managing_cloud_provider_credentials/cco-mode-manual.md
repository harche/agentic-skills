Manual mode is supported for Amazon Web Services (AWS), global Microsoft Azure, Microsoft Azure Stack Hub, Google Cloud, IBM Cloud®, and Nutanix.

# User-managed credentials

In manual mode, a user manages cloud credentials instead of the Cloud Credential Operator (CCO). To use this mode, you must examine the `CredentialsRequest` CRs in the release image for the version of OpenShift Container Platform that you are running or installing, create corresponding credentials in the underlying cloud provider, and create Kubernetes Secrets in the correct namespaces to satisfy all `CredentialsRequest` CRs for the cluster’s cloud provider. Some platforms use the CCO utility (`ccoctl`) to facilitate this process during installation and updates.

Using manual mode with long-term credentials allows each cluster component to have only the permissions it requires, without storing an administrator-level credential in the cluster. This mode also does not require connectivity to services such as the AWS public IAM endpoint. However, you must manually reconcile permissions with new release images for every upgrade.

For information about configuring your cloud provider to use manual mode, see the manual credentials management options for your cloud provider.

> [!NOTE]
> An AWS, global Azure, or Google Cloud cluster that uses manual mode might be configured to use short-term credentials for different components. For more information, see [Manual mode with short-term credentials for components](../../authentication/managing_cloud_provider_credentials/cco-short-term-creds.xml#cco-short-term-creds).

# Additional resources

- [Manually creating long-term credentials for AWS](../../installing/installing_aws/ipi/installing-aws-customizations.xml#manually-create-iam_installing-aws-customizations)

- [Manually creating long-term credentials for Azure](../../installing/installing_azure/ipi/installing-azure-customizations.xml#manually-create-iam_installing-azure-customizations)

- [Manually creating long-term credentials for Google Cloud](../../installing/installing_gcp/installing-gcp-customizations.xml#manually-create-iam_installing-gcp-customizations)

- [Configuring IAM for IBM Cloud®](../../installing/installing_ibm_cloud/configuring-iam-ibm-cloud.xml#configuring-iam-ibm-cloud)

- [Configuring IAM for Nutanix](../../installing/installing_nutanix/installing-nutanix-installer-provisioned.xml#manually-create-iam-nutanix_installing-nutanix-installer-provisioned)

- [Manual mode with short-term credentials for components](../../authentication/managing_cloud_provider_credentials/cco-short-term-creds.xml#cco-short-term-creds)

- [Preparing to update a cluster with manually maintained credentials](../../updating/preparing_for_updates/preparing-manual-creds-update.xml#preparing-manual-creds-update)
