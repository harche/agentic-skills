To get an update experience similar to connected clusters, you can use the following procedures to install and configure the OpenShift Update Service (OSUS) in a disconnected environment.

The following steps outline the high-level workflow on how to update a cluster in a disconnected environment using OSUS:

1.  Configure access to a secured registry.

2.  Update the global cluster pull secret to access your mirror registry.

3.  Install the OSUS Operator.

4.  Create a graph data container image for the OpenShift Update Service.

5.  Install the OSUS application and configure your clusters to use the OpenShift Update Service in your environment.

6.  Perform a supported update procedure from the documentation as you would with a connected cluster.

# Using the OpenShift Update Service in a disconnected environment

The OpenShift Update Service (OSUS) provides update recommendations to OpenShift Container Platform clusters. Red Hat publicly hosts the OpenShift Update Service, and clusters in a connected environment can connect to the service through public APIs to retrieve update recommendations.

However, clusters in a disconnected environment cannot access these public APIs to retrieve update information. To have a similar update experience in a disconnected environment, you can install and configure the OpenShift Update Service so that it is available within the disconnected environment.

A single OSUS instance is capable of serving recommendations to thousands of clusters. OSUS can be scaled horizontally to cater to more clusters by changing the replica value. So for most disconnected use cases, one OSUS instance is enough. For example, Red Hat hosts just one OSUS instance for the entire fleet of connected clusters.

If you want to keep update recommendations separate in different environments, you can run one OSUS instance for each environment. For example, in a case where you have separate test and stage environments, you might not want a cluster in a stage environment to receive update recommendations to version A if that version has not been tested in the test environment yet.

The following sections describe how to install an OSUS instance and configure it to provide update recommendations to a cluster.

<div>

<div class="title">

Additional resources

</div>

- [About the OpenShift Update Service](../../updating/understanding_updates/intro-to-updates.xml#update-service-about_understanding-openshift-updates)

- [Understanding update channels and releases](../../updating/understanding_updates/understanding-update-channels-release.xml#understanding-update-channels-releases)

</div>

# Prerequisites

- You must have the `oc` command-line interface (CLI) tool installed.

- You must provision a container image registry in your environment with the container images for your update, as described in [Mirroring OpenShift Container Platform images](../../disconnected/updating/mirroring-image-repository.xml#mirroring-ocp-image-repository).

# Configuring access to a secured registry for the OpenShift Update Service

If the release images are contained in a registry whose HTTPS X.509 certificate is signed by a custom certificate authority, complete the steps in [Configuring additional trust stores for image registry access](../../registry/configuring-registry-operator.xml#images-configuration-cas_configuring-registry-operator) along with following changes for the update service.

The OpenShift Update Service Operator needs the config map key name `updateservice-registry` in the registry CA cert.

<div class="formalpara">

<div class="title">

Image registry CA config map example for the update service

</div>

``` yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-registry-ca
data:
  updateservice-registry: |
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
  registry-with-port.example.com..5000: |
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
```

</div>

- The OpenShift Update Service Operator requires the config map key name `updateservice-registry` in the registry CA cert.

- If the registry has the port, such as `registry-with-port.example.com:5000`, `:` should be replaced with `..`.

# Updating the global cluster pull secret

<div wrapper="1" role="_abstract">

To add new registries or update authentication for your OpenShift Container Platform cluster, you can update the global pull secret by appending new credentials to the *additional-pull-secret*. To do this, you can use the `oc set data secret/additional-pull-secret -n kube-system` command. Hypershift manages the new credential propagation among the HostedCluster nodes.

</div>

Use this procedure when you need a separate registry to store images than the registry used during installation.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Optional: To append a new pull secret to the existing pull secret:

    1.  Download the pull secret by entering the following command:

        ``` terminal
        $ oc get secret/pull-secret -n openshift-config --template='{{index .data ".dockerconfigjson" | base64decode}}' > <pull_secret_location>
        ```

        where:

        `<pull_secret_location>`
        Specifies the path to the pull secret file.

    2.  Add the new pull secret by entering the following command:

        ``` terminal
        $ oc registry login --registry="<registry>" \
        --auth-basic="<username>:<password>" \
        --to=<pull_secret_location>
        ```

        where:

        `<registry>`
        Specifies the new registry. You can include many repositories within the same registry, for example: `--registry="<registry/my-namespace/my-repository>`.

        `<username>:<password>`
        Specifies the credentials of the new registry.

        `<pull_secret_location>`
        Specifies the path to the pull secret file.

2.  Update the global pull secret for your cluster by entering the following command. Note that this update rolls out to all nodes, which can take some time depending on the size of your cluster.

    ``` terminal
    $ oc set data secret/pull-secret -n openshift-config \
      --from-file=.dockerconfigjson=<pull_secret_location>
    ```

    where:

    `<pull_secret_location>`
    Specifies the path to the new pull secret file.

    This merges your additional pull secret with the original HostedCluster pull secret, making it available to all nodes in the cluster.

3.  Optional: Modify the additional pull secret added by entering the following command:

    ``` terminal
    $ oc edit secret additional-pull-secret -n kube-system
    ```

    The secret must contain a valid DockerConfigJSON format.

    <div class="formalpara">

    <div class="title">

    Example pull secret

    </div>

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: additional-pull-secret
      namespace: kube-system
    type: kubernetes.io/dockerconfigjson
    data:
      .dockerconfigjson: <base64-encoded-docker-config-json>
    ```

    </div>

    This results in the following states of the each pull secret:

    - **Original**: immutable

    - **Additional**: mutable

    - **Global**: final state of both the original and additional pull secrets

4.  Optional: Delete the additional pull secret added by entering the following command:

    ``` terminal
    $ oc delete secret additional-pull-secret -n kube-system
    ```

    This triggers the automatic cleanup process across your nodes.

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Transferring cluster ownership](https://docs.redhat.com/en/documentation/openshift_cluster_manager/1-latest/html-single/managing_clusters/index#transferring-cluster-ownership_downloading-and-updating-pull-secrets)

</div>

# Installing the OpenShift Update Service Operator

To install the OpenShift Update Service, you must first install the OpenShift Update Service Operator by using the OpenShift Container Platform web console or CLI.

> [!NOTE]
> For clusters that are installed in disconnected environments, also known as disconnected clusters, Operator Lifecycle Manager by default cannot access the Red Hat-provided software catalog sources hosted on remote registries because those remote sources require full internet connectivity. For more information, see [Using Operator Lifecycle Manager in disconnected environments](../../disconnected/using-olm.xml#olm-restricted-networks).

## Installing the OpenShift Update Service Operator by using the web console

You can use the web console to install the OpenShift Update Service Operator.

<div>

<div class="title">

Procedure

</div>

1.  In the web console, click **Ecosystem** → **Software Catalog**.

    > [!NOTE]
    > Enter `Update Service` into the **Filter by keyword…​** field to find the Operator faster.

2.  Choose **OpenShift Update Service** from the list of available Operators, and click **Install**.

    1.  Select an **Update channel**.

    2.  Select a **Version**.

    3.  Select **A specific namespace on the cluster** under **Installation Mode**.

    4.  Select a namespace for **Installed Namespace** or accept the recommended namespace `openshift-update-service`.

    5.  Select an **Update approval** strategy:

        - The **Automatic** strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available.

        - The **Manual** strategy requires a cluster administrator to approve the Operator update.

    6.  Click **Install**.

3.  Go to **Ecosystem** → **Installed Operators** and verify that the OpenShift Update Service Operator is installed.

4.  Ensure that **OpenShift Update Service** is listed in the correct namespace with a **Status** of **Succeeded**.

</div>

## Installing the OpenShift Update Service Operator by using the CLI

You can use the OpenShift CLI (`oc`) to install the OpenShift Update Service Operator.

<div>

<div class="title">

Procedure

</div>

1.  Create a namespace for the OpenShift Update Service Operator:

    1.  Create a `Namespace` object YAML file, for example, `update-service-namespace.yaml`, for the OpenShift Update Service Operator:

        ``` yaml
        apiVersion: v1
        kind: Namespace
        metadata:
          name: openshift-update-service
          annotations:
            openshift.io/node-selector: ""
          labels:
            openshift.io/cluster-monitoring: "true"
        ```

        - Set the `openshift.io/cluster-monitoring` label to enable Operator-recommended cluster monitoring on this namespace.

    2.  Create the namespace:

        ``` terminal
        $ oc create -f <filename>.yaml
        ```

        For example:

        ``` terminal
        $ oc create -f update-service-namespace.yaml
        ```

2.  Install the OpenShift Update Service Operator by creating the following objects:

    1.  Create an `OperatorGroup` object YAML file, for example, `update-service-operator-group.yaml`:

        ``` yaml
        apiVersion: operators.coreos.com/v1
        kind: OperatorGroup
        metadata:
          name: update-service-operator-group
          namespace: openshift-update-service
        spec:
          targetNamespaces:
          - openshift-update-service
        ```

    2.  Create an `OperatorGroup` object:

        ``` terminal
        $ oc -n openshift-update-service create -f <filename>.yaml
        ```

        For example:

        ``` terminal
        $ oc -n openshift-update-service create -f update-service-operator-group.yaml
        ```

    3.  Create a `Subscription` object YAML file, for example, `update-service-subscription.yaml`:

        <div class="formalpara">

        <div class="title">

        Example Subscription

        </div>

        ``` yaml
        apiVersion: operators.coreos.com/v1alpha1
        kind: Subscription
        metadata:
          name: update-service-subscription
          namespace: openshift-update-service
        spec:
          channel: v1
          installPlanApproval: "Automatic"
          source: "redhat-operators"
          sourceNamespace: "openshift-marketplace"
          name: "cincinnati-operator"
        ```

        </div>

        - Specify the name of the catalog source that provides the Operator. For clusters that do not use a custom Operator Lifecycle Manager (OLM), specify `redhat-operators`. If your OpenShift Container Platform cluster is installed in a disconnected environment, specify the name of the `CatalogSource` object created when you configured Operator Lifecycle Manager (OLM).

    4.  Create the `Subscription` object:

        ``` terminal
        $ oc create -f <filename>.yaml
        ```

        For example:

        ``` terminal
        $ oc -n openshift-update-service create -f update-service-subscription.yaml
        ```

        The OpenShift Update Service Operator is installed to the `openshift-update-service` namespace and targets the `openshift-update-service` namespace.

3.  Verify the Operator installation:

    ``` terminal
    $ oc -n openshift-update-service get clusterserviceversions
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                             DISPLAY                    VERSION   REPLACES   PHASE
    update-service-operator.v4.6.0   OpenShift Update Service   4.6.0                Succeeded
    ...
    ```

    </div>

    If the OpenShift Update Service Operator is listed, the installation was successful. The version number might be different than shown.

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Installing Operators in your namespace](../../operators/user/olm-installing-operators-in-namespace.xml#olm-installing-operators-in-namespace).

</div>

# Creating the OpenShift Update Service graph data container image

The OpenShift Update Service requires a graph data container image, from which the OpenShift Update Service retrieves information about channel membership and blocked update edges. Graph data is typically fetched directly from the update graph data repository. In environments where an internet connection is unavailable, loading this information from an init container is another way to make the graph data available to the OpenShift Update Service. The role of the init container is to provide a local copy of the graph data, and during pod initialization, the init container copies the data to a volume that is accessible by the service.

> [!NOTE]
> The oc-mirror OpenShift CLI (`oc`) plugin creates this graph data container image in addition to mirroring release images. If you used the oc-mirror plugin to mirror your release images, you can skip this procedure.

<div>

<div class="title">

Procedure

</div>

1.  Create a Dockerfile, for example, `./Dockerfile`, containing the following:

    ``` terminal
    FROM registry.access.redhat.com/ubi9/ubi:latest

    RUN curl -L -o cincinnati-graph-data.tar.gz https://api.openshift.com/api/upgrades_info/graph-data

    RUN mkdir -p /var/lib/cincinnati-graph-data && tar xvzf cincinnati-graph-data.tar.gz -C /var/lib/cincinnati-graph-data/ --no-overwrite-dir --no-same-owner

    CMD ["/bin/bash", "-c" ,"exec cp -rp /var/lib/cincinnati-graph-data/* /var/lib/cincinnati/graph-data"]
    ```

2.  Use the docker file created in the above step to build a graph data container image, for example, `registry.example.com/openshift/graph-data:latest`:

    ``` terminal
    $ podman build -f ./Dockerfile -t registry.example.com/openshift/graph-data:latest
    ```

3.  Push the graph data container image created in the previous step to a repository that is accessible to the OpenShift Update Service, for example, `registry.example.com/openshift/graph-data:latest`:

    ``` terminal
    $ podman push registry.example.com/openshift/graph-data:latest
    ```

    > [!NOTE]
    > To push a graph data image to a registry in a disconnected environment, copy the graph data container image created in the previous step to a repository that is accessible to the OpenShift Update Service. Run `oc image mirror --help` for available options.

</div>

# Creating an OpenShift Update Service application

You can create an OpenShift Update Service application by using the OpenShift Container Platform web console or CLI.

## Creating an OpenShift Update Service application by using the web console

You can use the OpenShift Container Platform web console to create an OpenShift Update Service application by using the OpenShift Update Service Operator.

<div>

<div class="title">

Prerequisites

</div>

- The OpenShift Update Service Operator has been installed.

- The OpenShift Update Service graph data container image has been created and pushed to a repository that is accessible to the OpenShift Update Service.

- The current release and update target releases have been mirrored to a registry in the disconnected environment.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the web console, click **Ecosystem** → **Installed Operators**.

2.  Choose **OpenShift Update Service** from the list of installed Operators.

3.  Click the **Update Service** tab.

4.  Click **Create UpdateService**.

5.  Enter a name in the **Name** field, for example, `service`.

6.  Enter the local pullspec in the **Graph Data Image** field to the graph data container image created in "Creating the OpenShift Update Service graph data container image", for example, `registry.example.com/openshift/graph-data:latest`.

7.  In the **Releases** field, enter the registry and repository created to contain the release images in "Mirroring the OpenShift Container Platform image repository", for example, `registry.example.com/ocp4/openshift4-release-images`.

8.  Enter `2` in the **Replicas** field.

9.  Click **Create** to create the OpenShift Update Service application.

10. Verify the OpenShift Update Service application:

    - From the **UpdateServices** list in the **Update Service** tab, click the Update Service application just created.

    - Click the **Resources** tab.

    - Verify each application resource has a status of **Created**.

</div>

## Creating an OpenShift Update Service application by using the CLI

You can use the OpenShift CLI (`oc`) to create an OpenShift Update Service application.

<div>

<div class="title">

Prerequisites

</div>

- The OpenShift Update Service Operator has been installed.

- The OpenShift Update Service graph data container image has been created and pushed to a repository that is accessible to the OpenShift Update Service.

- The current release and update target releases have been mirrored to a registry in the disconnected environment.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure the OpenShift Update Service target namespace, for example, `openshift-update-service`:

    ``` terminal
    $ NAMESPACE=openshift-update-service
    ```

    The namespace must match the `targetNamespaces` value from the operator group.

2.  Configure the name of the OpenShift Update Service application, for example, `service`:

    ``` terminal
    $ NAME=service
    ```

3.  Configure the registry and repository for the release images as configured in "Mirroring the OpenShift Container Platform image repository", for example, `registry.example.com/ocp4/openshift4-release-images`:

    ``` terminal
    $ RELEASE_IMAGES=registry.example.com/ocp4/openshift4-release-images
    ```

4.  Set the local pullspec for the graph data image to the graph data container image created in "Creating the OpenShift Update Service graph data container image", for example, `registry.example.com/openshift/graph-data:latest`:

    ``` terminal
    $ GRAPH_DATA_IMAGE=registry.example.com/openshift/graph-data:latest
    ```

5.  Create an OpenShift Update Service application object:

    ``` terminal
    $ oc -n "${NAMESPACE}" create -f - <<EOF
    apiVersion: updateservice.operator.openshift.io/v1
    kind: UpdateService
    metadata:
      name: ${NAME}
    spec:
      replicas: 2
      releases: ${RELEASE_IMAGES}
      graphDataImage: ${GRAPH_DATA_IMAGE}
    EOF
    ```

6.  Verify the OpenShift Update Service application:

    1.  Use the following command to obtain a policy engine route:

        ``` terminal
        $ while sleep 1; do POLICY_ENGINE_GRAPH_URI="$(oc -n "${NAMESPACE}" get -o jsonpath='{.status.policyEngineURI}/api/upgrades_info/v1/graph{"\n"}' updateservice "${NAME}")"; SCHEME="${POLICY_ENGINE_GRAPH_URI%%:*}"; if test "${SCHEME}" = http -o "${SCHEME}" = https; then break; fi; done
        ```

        You might need to poll until the command succeeds.

    2.  Retrieve a graph from the policy engine. Be sure to specify a valid version for `channel`. For example, if running in OpenShift Container Platform 4.17, use `stable-4.17`:

        ``` terminal
        $ while sleep 10; do HTTP_CODE="$(curl --header Accept:application/json --output /dev/stderr --write-out "%{http_code}" "${POLICY_ENGINE_GRAPH_URI}?channel=stable-4.6")"; if test "${HTTP_CODE}" -eq 200; then break; fi; echo "${HTTP_CODE}"; done
        ```

        This polls until the graph request succeeds; however, the resulting graph might be empty depending on which release images you have mirrored.

</div>

> [!NOTE]
> The policy engine route name must not be more than 63 characters based on RFC-1123. If you see `ReconcileCompleted` status as `false` with the reason `CreateRouteFailed` caused by `host must conform to DNS 1123 naming convention and must be no more than 63 characters`, try creating the Update Service with a shorter name.

# Configuring the Cluster Version Operator (CVO)

After the OpenShift Update Service Operator has been installed and the OpenShift Update Service application has been created, the Cluster Version Operator (CVO) can be updated to pull graph data from the OpenShift Update Service installed in your environment.

<div>

<div class="title">

Prerequisites

</div>

- The OpenShift Update Service Operator has been installed.

- The OpenShift Update Service graph data container image has been created and pushed to a repository that is accessible to the OpenShift Update Service.

- The current release and update target releases have been mirrored to a registry in the disconnected environment.

- The OpenShift Update Service application has been created.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the OpenShift Update Service target namespace, for example, `openshift-update-service`:

    ``` terminal
    $ NAMESPACE=openshift-update-service
    ```

2.  Set the name of the OpenShift Update Service application, for example, `service`:

    ``` terminal
    $ NAME=service
    ```

3.  Obtain the policy engine route:

    ``` terminal
    $ POLICY_ENGINE_GRAPH_URI="$(oc -n "${NAMESPACE}" get -o jsonpath='{.status.policyEngineURI}/api/upgrades_info/v1/graph{"\n"}' updateservice "${NAME}")"
    ```

4.  Set the patch for the pull graph data:

    ``` terminal
    $ PATCH="{\"spec\":{\"upstream\":\"${POLICY_ENGINE_GRAPH_URI}\"}}"
    ```

5.  Patch the CVO to use the OpenShift Update Service in your environment:

    ``` terminal
    $ oc patch clusterversion version -p $PATCH --type merge
    ```

</div>

> [!NOTE]
> See [Configuring the cluster-wide proxy](../../networking/configuring_network_settings/enable-cluster-wide-proxy.xml#enable-cluster-wide-proxy) to configure the CA to trust the update server.

# Next steps

Before updating your cluster, confirm that the following conditions are met:

- The Cluster Version Operator (CVO) is configured to use your installed OpenShift Update Service application.

- The release image signature config map for the new release is applied to your cluster.

  > [!NOTE]
  > The Cluster Version Operator (CVO) uses release image signatures to ensure that release images have not been modified, by verifying that the release image signatures match the expected result.

- The current release and update target release images are mirrored to a registry in the disconnected environment.

- A recent graph data container image has been mirrored to your registry.

- A recent version of the OpenShift Update Service Operator is installed.

  > [!NOTE]
  > If you have not recently installed or updated the OpenShift Update Service Operator, there might be a more recent version available. See [Using Operator Lifecycle Manager in disconnected environments](../../disconnected/using-olm.xml#olm-restricted-networks) for more information about how to update your OLM catalog in a disconnected environment.

After you configure your cluster to use the installed OpenShift Update Service and local mirror registry, you can use any of the following update methods:

- [Updating a cluster using the web console](../../updating/updating_a_cluster/updating-cluster-web-console.xml#updating-cluster-web-console)

- [Updating a cluster using the CLI](../../updating/updating_a_cluster/updating-cluster-cli.xml#updating-cluster-cli)

- [Performing a Control Plane Only update](../../updating/updating_a_cluster/control-plane-only-update.xml#control-plane-only-update)

- [Performing a canary rollout update](../../updating/updating_a_cluster/update-using-custom-machine-config-pools.xml#update-using-custom-machine-config-pools)
