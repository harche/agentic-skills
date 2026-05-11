Installing the Red Hat build of OpenTelemetry involves the following steps:

1.  Installing the Red Hat build of OpenTelemetry Operator.

2.  Creating a namespace for an OpenTelemetry Collector instance.

3.  Creating an `OpenTelemetryCollector` custom resource to deploy the OpenTelemetry Collector instance.

# Installing the Red Hat build of OpenTelemetry from the web console

You can install the Red Hat build of OpenTelemetry from the OpenShift Container Platform web console.

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

1.  Install the Red Hat build of OpenTelemetry Operator:

    1.  In the web console, search for `Red Hat build of OpenTelemetry Operator`.

        > [!TIP]
        > In OpenShift Container Platform 4.19 or earlier, go to **Operators** → **OperatorHub**.
        >
        > In OpenShift Container Platform 4.20 or later, go to **Ecosystem** → **Software Catalog**.

    2.  Select the **Red Hat build of OpenTelemetry Operator** that is **provided by Red Hat** → **Install** → **Install** → **View Operator**.

        > [!IMPORTANT]
        > This installs the Operator with the default presets:
        >
        > - **Update channel** → **stable**
        >
        > - **Installation mode** → **All namespaces on the cluster**
        >
        > - **Installed Namespace** → **openshift-opentelemetry-operator**
        >
        > - **Update approval** → **Automatic**

    3.  In the **Details** tab of the installed Operator page, under **ClusterServiceVersion details**, verify that the installation **Status** is **Succeeded**.

2.  Create a permitted project of your choice for the **OpenTelemetry Collector** instance that you will create in the next step by going to **Home** → **Projects** → **Create Project**. Project names beginning with the `openshift-` prefix are not permitted.

3.  Create an **OpenTelemetry Collector** instance.

    1.  Go to **Ecosystem** → **Installed Operators**.

    2.  Select **OpenTelemetry Collector** → **Create OpenTelemetry Collector** → **YAML view**.

    3.  In the **YAML view**, customize the `OpenTelemetryCollector` custom resource (CR):

        <div class="formalpara">

        <div class="title">

        Example `OpenTelemetryCollector` CR

        </div>

        ``` yaml
        apiVersion: opentelemetry.io/v1beta1
        kind: OpenTelemetryCollector
        metadata:
          name: otel
          namespace: <permitted_project_of_opentelemetry_collector_instance>
        spec:
          mode: <deployment_mode>
          config:
            receivers:
              otlp:
                protocols:
                  grpc:
                  http:
              jaeger:
                protocols:
                  grpc: {}
                  thrift_binary: {}
                  thrift_compact: {}
                  thrift_http: {}
              zipkin: {}
            processors:
              batch: {}
              memory_limiter:
                check_interval: 1s
                limit_percentage: 50
                spike_limit_percentage: 30
            exporters:
              debug: {}
            service:
              pipelines:
                traces:
                  receivers: [otlp,jaeger,zipkin]
                  processors: [memory_limiter,batch]
                  exporters: [debug]
        ```

        </div>

        - The project that you have chosen for the `OpenTelemetryCollector` deployment. Project names beginning with the `openshift-` prefix are not permitted.

        - The deployment mode with the following supported values: the default `deployment`, `daemonset`, `statefulset`, or `sidecar`. For details, see *Deployment Modes*.

        - For details, see *Receivers*.

        - For details, see *Processors*.

        - For details, see *Exporters*.

    4.  Select **Create**.

</div>

<div>

<div class="title">

Verification

</div>

1.  Use the **Project:** dropdown list to select the project of the **OpenTelemetry Collector** instance.

2.  Go to **Ecosystem** → **Installed Operators** to verify that the **Status** of the **OpenTelemetry Collector** instance is **Condition: Ready**.

3.  Go to **Workloads** → **Pods** to verify that all the component pods of the **OpenTelemetry Collector** instance are running.

</div>

# Installing the Red Hat build of OpenTelemetry by using the CLI

You can install the Red Hat build of OpenTelemetry from the command line.

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

1.  Install the Red Hat build of OpenTelemetry Operator:

    1.  Create a project for the Red Hat build of OpenTelemetry Operator by running the following command:

        ``` terminal
        $ oc apply -f - << EOF
        apiVersion: project.openshift.io/v1
        kind: Project
        metadata:
          labels:
            kubernetes.io/metadata.name: openshift-opentelemetry-operator
            openshift.io/cluster-monitoring: "true"
          name: openshift-opentelemetry-operator
        EOF
        ```

    2.  Create an Operator group by running the following command:

        ``` terminal
        $ oc apply -f - << EOF
        apiVersion: operators.coreos.com/v1
        kind: OperatorGroup
        metadata:
          name: openshift-opentelemetry-operator
          namespace: openshift-opentelemetry-operator
        spec:
          upgradeStrategy: Default
        EOF
        ```

    3.  Create a subscription by running the following command:

        ``` terminal
        $ oc apply -f - << EOF
        apiVersion: operators.coreos.com/v1alpha1
        kind: Subscription
        metadata:
          name: opentelemetry-product
          namespace: openshift-opentelemetry-operator
        spec:
          channel: stable
          installPlanApproval: Automatic
          name: opentelemetry-product
          source: redhat-operators
          sourceNamespace: openshift-marketplace
        EOF
        ```

    4.  Check the Operator status by running the following command:

        ``` terminal
        $ oc get csv -n openshift-opentelemetry-operator
        ```

2.  Create a permitted project of your choice for the OpenTelemetry Collector instance that you will create in a subsequent step:

    - To create a permitted project without metadata, run the following command:

      ``` terminal
      $ oc new-project <permitted_project_of_opentelemetry_collector_instance>
      ```

      - Project names beginning with the `openshift-` prefix are not permitted.

    - To create a permitted project with metadata, run the following command:

      ``` terminal
      $ oc apply -f - << EOF
      apiVersion: project.openshift.io/v1
      kind: Project
      metadata:
        name: <permitted_project_of_opentelemetry_collector_instance>
      EOF
      ```

      - Project names beginning with the `openshift-` prefix are not permitted.

3.  Create an OpenTelemetry Collector instance in the project that you created for it.

    > [!NOTE]
    > You can create multiple OpenTelemetry Collector instances in separate projects on the same cluster.

    1.  Customize the `OpenTelemetryCollector` custom resource (CR):

        <div class="formalpara">

        <div class="title">

        Example `OpenTelemetryCollector` CR

        </div>

        ``` yaml
        apiVersion: opentelemetry.io/v1beta1
        kind: OpenTelemetryCollector
        metadata:
          name: otel
          namespace: <permitted_project_of_opentelemetry_collector_instance>
        spec:
          mode: <deployment_mode>
          config:
            receivers:
              otlp:
                protocols:
                  grpc:
                  http:
              jaeger:
                protocols:
                  grpc: {}
                  thrift_binary: {}
                  thrift_compact: {}
                  thrift_http: {}
              zipkin: {}
            processors:
              batch: {}
              memory_limiter:
                check_interval: 1s
                limit_percentage: 50
                spike_limit_percentage: 30
            exporters:
              debug: {}
            service:
              pipelines:
                traces:
                  receivers: [otlp,jaeger,zipkin]
                  processors: [memory_limiter,batch]
                  exporters: [debug]
        ```

        </div>

        - The project that you have chosen for the `OpenTelemetryCollector` deployment. Project names beginning with the `openshift-` prefix are not permitted.

        - The deployment mode with the following supported values: the default `deployment`, `daemonset`, `statefulset`, or `sidecar`. For details, see *Deployment Modes*.

        - For details, see *Receivers*.

        - For details, see *Processors*.

        - For details, see *Exporters*.

    2.  Apply the customized CR by running the following command:

        ``` terminal
        $ oc apply -f - << EOF
        <OpenTelemetryCollector_custom_resource>
        EOF
        ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the `status.phase` of the OpenTelemetry Collector pod is `Running` and the `conditions` are `type: Ready` by running the following command:

    ``` terminal
    $ oc get pod -l app.kubernetes.io/managed-by=opentelemetry-operator,app.kubernetes.io/instance=<namespace>.<instance_name> -o yaml
    ```

2.  Get the OpenTelemetry Collector service by running the following command:

    ``` terminal
    $ oc get service -l app.kubernetes.io/managed-by=opentelemetry-operator,app.kubernetes.io/instance=<namespace>.<instance_name>
    ```

</div>

# Using taints and tolerations

To schedule the OpenTelemetry pods on dedicated nodes, see [How to deploy the different OpenTelemetry components on infra nodes using nodeSelector and tolerations in OpenShift 4](https://access.redhat.com/solutions/7040771)

# Creating the required RBAC resources automatically

<div wrapper="1" role="_abstract">

Some Collector components require configuring the RBAC resources.

</div>

<div>

<div class="title">

Procedure

</div>

- Add the following permissions to the `opentelemetry-operator-controller-manage` service account so that the Red Hat build of OpenTelemetry Operator can create them automatically:

  ``` yaml
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRole
  metadata:
    name: generate-processors-rbac
  rules:
  - apiGroups:
    - rbac.authorization.k8s.io
    resources:
    - clusterrolebindings
    - clusterroles
    verbs:
    - create
    - delete
    - get
    - list
    - patch
    - update
    - watch
  ---
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRoleBinding
  metadata:
    name: generate-processors-rbac
  roleRef:
    apiGroup: rbac.authorization.k8s.io
    kind: ClusterRole
    name: generate-processors-rbac
  subjects:
  - kind: ServiceAccount
    name: opentelemetry-operator-controller-manager
    namespace: openshift-opentelemetry-operator
  ```

</div>

# Additional resources

- [Creating a cluster admin](../../post_installation_configuration/preparing-for-users.xml#creating-cluster-admin_post-install-preparing-for-users)

- [OperatorHub.io](https://operatorhub.io/)

- [Accessing the web console](../../web_console/web-console.xml#web-console)

- [Installing from the software catalog using the web console](../../operators/admin/olm-adding-operators-to-cluster.xml#olm-installing-from-software-catalog-using-web-console_olm-adding-operators-to-a-cluster)

- [Creating applications from installed Operators](../../operators/user/olm-creating-apps-from-installed-operators.xml#olm-creating-apps-from-installed-operators)

- [Getting started with the OpenShift CLI](../../cli_reference/openshift_cli/getting-started-cli.xml#getting-started-cli)
