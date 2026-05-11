The steps for removing the Red Hat build of OpenTelemetry from an OpenShift Container Platform cluster are as follows:

1.  Shut down all Red Hat build of OpenTelemetry pods.

2.  Remove any OpenTelemetryCollector instances.

3.  Remove the Red Hat build of OpenTelemetry Operator.

# Removing an OpenTelemetry Collector instance by using the web console

You can remove an OpenTelemetry Collector instance in the **Administrator** view of the web console.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the web console as a cluster administrator with the `cluster-admin` role.

- For Red Hat OpenShift Dedicated, you must be logged in using an account with the `dedicated-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to **Ecosystem** → **Installed Operators** → **Red Hat build of OpenTelemetry Operator** → **OpenTelemetryInstrumentation** or **OpenTelemetryCollector**.

2.  To remove the relevant instance, select ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) → **Delete** …​ → **Delete**.

3.  Optional: Remove the Red Hat build of OpenTelemetry Operator.

</div>

# Removing an OpenTelemetry Collector instance by using the CLI

You can remove an OpenTelemetry Collector instance on the command line.

<div>

<div class="title">

Prerequisites

</div>

- An active OpenShift CLI (`oc`) session by a cluster administrator with the `cluster-admin` role.

  > [!TIP]
  > - Ensure that your OpenShift CLI (`oc`) version is up to date and matches your OpenShift Container Platform version.
  >
  > - Run `oc login`:
  >
  >   ``` terminal
  >   $ oc login --username=<your_username>
  >   ```

</div>

<div>

<div class="title">

Procedure

</div>

1.  Get the name of the OpenTelemetry Collector instance by running the following command:

    ``` terminal
    $ oc get deployments -n <project_of_opentelemetry_instance>
    ```

2.  Remove the OpenTelemetry Collector instance by running the following command:

    ``` terminal
    $ oc delete opentelemetrycollectors <opentelemetry_instance_name> -n <project_of_opentelemetry_instance>
    ```

3.  Optional: Remove the Red Hat build of OpenTelemetry Operator.

</div>

<div>

<div class="title">

Verification

</div>

- To verify successful removal of the OpenTelemetry Collector instance, run `oc get deployments` again:

  ``` terminal
  $ oc get deployments -n <project_of_opentelemetry_instance>
  ```

</div>

# Additional resources

- [Deleting Operators from a cluster](../../operators/admin/olm-deleting-operators-from-cluster.xml#olm-deleting-operators-from-a-cluster)

- [Getting started with the OpenShift CLI](../../cli_reference/openshift_cli/getting-started-cli.xml#getting-started-cli)
