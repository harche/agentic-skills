<div wrapper="1" role="_abstract">

In OpenShift Container Platform version 4.17, you can install a customized cluster on IBM PowerVC. To customize the installation, modify parameters in the `install-config.yaml` before you install the cluster.

</div>

# Prerequisites

- You reviewed details about the [OpenShift Container Platform installation and update](../../architecture/architecture-installation.xml#architecture-installation) processes.

- You read the documentation on [selecting a cluster installation method and preparing it for users](../../installing/overview/installing-preparing.xml#installing-preparing).

- You have a load balancing service you can use with the IBM PowerVC network you intend to use.

- You have a DHCP server backing the IBM PowerVC network you intend to use.

# Resource guidelines for installing OpenShift Container Platform on IBM PowerVC

To support an OpenShift Container Platform installation, it is recommended that your IBM PowerVC has room for the following resources available:

| Resource       | Value  |
|----------------|--------|
| Subnets        | 1      |
| RAM            | 88 GB  |
| vCPUs          | 22     |
| Volume storage | 275 GB |
| Instances      | 7      |

Recommended resources for a default OpenShift Container Platform cluster on IBM PowerVC

A cluster might function with fewer than recommended resources.

# Obtaining the installation program

<div wrapper="1" role="_abstract">

Before you install OpenShift Container Platform, download the installation file on the host you are using for installation.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You have a computer that runs Linux or macOS, with 500 MB of local disk space.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to the [Cluster Type](https://console.redhat.com/openshift/install) page on the Red Hat Hybrid Cloud Console. If you have a Red Hat account, log in with your credentials. If you do not, create an account.

    > [!TIP]
    > You can also [download the binaries for a specific OpenShift Container Platform release](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/).

2.  Select your infrastructure provider from the **Run it yourself** section of the page.

3.  Select your host operating system and architecture from the dropdown menus under **OpenShift Installer** and click **Download Installer**.

4.  Place the downloaded file in the directory where you want to store the installation configuration files.

    > [!IMPORTANT]
    > - The installation program creates several files on the computer that you use to install your cluster. You must keep the installation program and the files that the installation program creates after you finish installing the cluster. Both of the files are required to delete the cluster.
    >
    > - Deleting the files created by the installation program does not remove your cluster, even if the cluster failed during installation. To remove your cluster, complete the OpenShift Container Platform uninstallation procedures for your specific cloud provider.

5.  Extract the installation program. For example, on a computer that uses a Linux operating system, run the following command:

    ``` terminal
    $ tar -xvf openshift-install-linux.tar.gz
    ```

6.  Download your installation [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret). This pull secret allows you to authenticate with the services that are provided by the included authorities, including Quay.io, which serves the container images for OpenShift Container Platform components.

    > [!TIP]
    > Alternatively, you can retrieve the installation program from the [Red Hat Customer Portal](https://access.redhat.com/downloads/content/290/), where you can specify a version of the installation program to download. However, you must have an active subscription to access this page.

</div>

# Creating the installation configuration file

<div wrapper="1" role="_abstract">

You can customize the OpenShift Container Platform cluster you install on IBM PowerVC.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You have the OpenShift Container Platform installation program and the pull secret for your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `install-config.yaml` file.

    1.  Change to the directory that contains the installation program and run the following command:

        ``` terminal
        $ ./openshift-install create install-config --dir <installation_directory>
        ```

        - `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates.

          When specifying the directory:

        - Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.

        - Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.

    2.  At the prompts, provide the configuration details for your cloud:

        1.  Optional: Select an SSH key to use to access your cluster machines.

            > [!NOTE]
            > For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

        2.  Enter a descriptive name for your cluster.

2.  Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section.

3.  Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

    > [!IMPORTANT]
    > The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Installation configuration parameters for IBM PowerVC](../../installing/installing_ibm_powervc/installation-config-parameters-ibm-powervc.xml#installation-config-parameters-ibm-powervc)

</div>

# Deploying the cluster

You can install OpenShift Container Platform on a compatible cloud platform.

> [!IMPORTANT]
> You can run the `create cluster` command of the installation program only once, during initial installation.

<div>

<div class="title">

Prerequisites

</div>

- You have configured an account with the cloud platform that hosts your cluster.

- You have the OpenShift Container Platform installation program and the pull secret for your cluster.

- You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.

</div>

<div>

<div class="title">

Procedure

</div>

- In the directory that contains the installation program, initialize the cluster deployment by running the following command:

  ``` terminal
  $ ./openshift-install create cluster --dir <installation_directory> \
      --log-level=info
  ```

  - For `<installation_directory>`, specify the location of your customized `./install-config.yaml` file.

  - To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

When the cluster deployment completes successfully:

</div>

- The terminal displays directions for accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user.

- Credential information also outputs to `<installation_directory>/.openshift_install.log`.

> [!IMPORTANT]
> Do not delete the installation program or the files that the installation program creates. Both are required to delete the cluster.

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
...
INFO Install complete!
INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
INFO Login to the console with user: "kubeadmin", and password: "password"
INFO Time elapsed: 36m22s
```

</div>

> [!IMPORTANT]
> - The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
>
> - It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

# Installing the OpenShift CLI on Linux

<div wrapper="1" role="_abstract">

To manage your cluster and deploy applications from the command line, install the OpenShift CLI (`oc`) binary on Linux.

</div>

> [!IMPORTANT]
> If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.
>
> Download and install the new version of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal.

2.  Select the architecture from the **Product Variant** list.

3.  Select the appropriate version from the **Version** list.

4.  Click **Download Now** next to the **OpenShift v4.17 Linux Clients** entry and save the file.

5.  Unpack the archive:

    ``` terminal
    $ tar xvf <file>
    ```

6.  Place the `oc` binary in a directory that is on your `PATH`.

    To check your `PATH`, execute the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- After you install the OpenShift CLI, it is available using the `oc` command:

  ``` terminal
  $ oc <command>
  ```

</div>

# Installing the OpenShift CLI on Windows

<div wrapper="1" role="_abstract">

To manage your cluster and deploy applications from the command line, install OpenShift CLI (`oc`) binary on Windows.

</div>

> [!IMPORTANT]
> If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.
>
> Download and install the new version of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal.

2.  Select the appropriate version from the **Version** list.

3.  Click **Download Now** next to the **OpenShift v4.17 Windows Client** entry and save the file.

4.  Extract the archive with a ZIP program.

5.  Move the `oc` binary to a directory that is on your `PATH` variable.

    To check your `PATH` variable, open the command prompt and execute the following command:

    ``` terminal
    C:\> path
    ```

</div>

<div>

<div class="title">

Verification

</div>

- After you install the OpenShift CLI, it is available using the `oc` command:

  ``` terminal
  C:\> oc <command>
  ```

</div>

# Installing the OpenShift CLI on macOS

<div wrapper="1" role="_abstract">

To manage your cluster and deploy applications from the command line, install the OpenShift CLI (`oc`) binary on macOS.

</div>

> [!IMPORTANT]
> If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.
>
> Download and install the new version of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal.

2.  Select the architecture from the **Product Variant** list.

3.  Select the appropriate version from the **Version** list.

4.  Click **Download Now** next to the **OpenShift v4.17 macOS Clients** entry and save the file.

    > [!NOTE]
    > For macOS arm64, choose the **OpenShift v4.17 macOS arm64 Client** entry.

5.  Unpack and unzip the archive.

6.  Move the `oc` binary to a directory on your `PATH` variable.

    To check your `PATH` variable, open a terminal and execute the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify your installation by using an `oc` command:

  ``` terminal
  $ oc <command>
  ```

</div>

# Verifying cluster status

You can verify your OpenShift Container Platform cluster’s status during or after installation.

<div>

<div class="title">

Procedure

</div>

1.  In the cluster environment, export the administrator’s kubeconfig file:

    ``` terminal
    $ export KUBECONFIG=<installation_directory>/auth/kubeconfig
    ```

    - For `<installation_directory>`, specify the path to the directory that you stored the installation files in.

      The `kubeconfig` file contains information about the cluster that is used by the CLI to connect a client to the correct cluster and API server.

2.  View the control plane and compute machines created after a deployment:

    ``` terminal
    $ oc get nodes
    ```

3.  View your cluster’s version:

    ``` terminal
    $ oc get clusterversion
    ```

4.  View your Operators' status:

    ``` terminal
    $ oc get clusteroperator
    ```

5.  View all running pods in the cluster:

    ``` terminal
    $ oc get pods -A
    ```

</div>

# Logging in to the cluster by using the CLI

<div wrapper="1" role="_abstract">

To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation.

</div>

The `kubeconfig` file is specific to a cluster and is created during OpenShift Container Platform installation.

<div>

<div class="title">

Prerequisites

</div>

- You deployed an OpenShift Container Platform cluster.

- You installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Export the `kubeadmin` credentials by running the following command:

    ``` terminal
    $ export KUBECONFIG=<installation_directory>/auth/kubeconfig
    ```

    where:

    `<installation_directory>`
    Specifies the path to the directory that stores the installation files.

2.  Verify you can run `oc` commands successfully using the exported configuration by running the following command:

    ``` terminal
    $ oc whoami
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    system:admin
    ```

    </div>

</div>

<div id="additional-resources_installing-ibm-powervc-customizations-console" role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Accessing the web console](../../web_console/web-console.xml#web-console)

</div>

# Telemetry access for OpenShift Container Platform

<div wrapper="1" role="_abstract">

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

</div>

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

<div id="additional-resources_installing-ibm-powervc-customizations-telemetry" role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [About remote health monitoring](../../support/remote_health_monitoring/about-remote-health-monitoring.xml#about-remote-health-monitoring)

</div>
