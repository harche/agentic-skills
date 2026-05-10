Many cloud providers can enable authentication by using account tokens that provide short-term, limited-privilege security credentials.

OpenShift Container Platform includes the Cloud Credential Operator (CCO) to manage cloud provider credentials as custom resource definitions (CRDs). The CCO syncs on `CredentialsRequest` custom resources (CRs) to allow OpenShift Container Platform components to request cloud provider credentials with any specific permissions required.

Previously, on clusters where the CCO is in *manual mode*, Operators managed by Operator Lifecycle Manager (OLM) often provided detailed instructions in the OperatorHub for how users could manually provision any required cloud credentials.

Starting in OpenShift Container Platform 4.14, the CCO can detect when it is running on clusters enabled to use short-term credentials on certain cloud providers. It can then semi-automate provisioning certain credentials, provided that the Operator author has enabled their Operator to support the updated CCO.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [About the Cloud Credential Operator](../../../authentication/managing_cloud_provider_credentials/about-cloud-credential-operator.xml#about-cloud-credential-operator)

- [CCO-based workflow for OLM-managed Operators with AWS STS](../../../operators/operator_sdk/token_auth/osdk-cco-aws-sts.xml#osdk-cco-aws-sts)

- [CCO-based workflow for OLM-managed Operators with Microsoft Entra Workload ID](../../../operators/operator_sdk/token_auth/osdk-cco-azure.xml#osdk-cco-azure)

- [CCO-based workflow for OLM-managed Operators with GCP Workload Identity](../../../operators/operator_sdk/token_auth/osdk-cco-gcp.xml#osdk-cco-gcp)

</div>
