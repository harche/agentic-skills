You can install OpenShift Container Platform on IBM Cloud® using installer-provisioned infrastructure. This process involves using an installation program to provision the underlying infrastructure for your cluster. Installing OpenShift Container Platform on IBM Cloud® using user-provisioned infrastructure is not supported at this time.

See [Installation process](../../architecture/architecture-installation.xml#installation-process_architecture-installation) for more information about installer-provisioned installation processes.

# Installing a cluster on installer-provisioned infrastructure

You can install a cluster on IBM Cloud® infrastructure that is provisioned by the OpenShift Container Platform installation program by using one of the following methods:

- **[Installing a customized cluster on IBM Cloud®](../../installing/installing_ibm_cloud/installing-ibm-cloud-customizations.xml#installing-ibm-cloud-customizations)**: You can install a customized cluster on IBM Cloud® infrastructure that the installation program provisions. The installation program allows for some customization to be applied at the installation stage. Many other customization options are available [post-installation](../../post_installation_configuration/cluster-tasks.xml#post-install-cluster-tasks).

- **[Installing a cluster on IBM Cloud® with network customizations](../../installing/installing_ibm_cloud/installing-ibm-cloud-customizations.xml#installing-ibm-cloud-customizations)**: You can customize your OpenShift Container Platform network configuration during installation, so that your cluster can coexist with your existing IP address allocations and adhere to your network requirements.

- **[Installing a cluster on IBM Cloud® into an existing VPC](../../installing/installing_ibm_cloud/installing-ibm-cloud-vpc.xml#installing-ibm-cloud-vpc)**: You can install OpenShift Container Platform on an existing IBM Cloud®. You can use this installation method if you have constraints set by the guidelines of your company, such as limits when creating new accounts or infrastructure.

- **[Installing a private cluster on an existing VPC](../../installing/installing_ibm_cloud/installing-ibm-cloud-private.xml#installing-ibm-cloud-private)**: You can install a private cluster on an existing Virtual Private Cloud (VPC). You can use this method to deploy OpenShift Container Platform on an internal network that is not visible to the internet.

- **[Installing a cluster on IBM Cloud in a restricted network](../../installing/installing_ibm_cloud/installing-ibm-cloud-restricted.xml#installing-ibm-cloud-restricted)**: You can install OpenShift Container Platform on IBM Cloud on installer-provisioned infrastructure by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components.

# Next steps

- [Configuring an IBM Cloud® account](../../installing/installing_ibm_cloud/installing-ibm-cloud-account.xml#installing-ibm-cloud-account)
