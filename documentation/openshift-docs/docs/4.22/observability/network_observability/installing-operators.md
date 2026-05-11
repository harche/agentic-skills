<div wrapper="1" role="_abstract">

Installing the Loki Operator is recommended before using the Network Observability Operator. You can use network observability without Loki, but special considerations apply if you only need metrics or external exporters.

</div>

The Loki Operator integrates a gateway that implements multi-tenancy and authentication with Loki for data flow storage. The `LokiStack` resource manages Loki, which is a scalable, highly-available, multi-tenant log aggregation system, and a web proxy with OpenShift Container Platform authentication. The `LokiStack` proxy uses OpenShift Container Platform authentication to enforce multi-tenancy and facilitate the saving and indexing of data in Loki log stores.

# Network observability without Loki

<div wrapper="1" role="_abstract">

Compare the features available with network observability with and without installing the Loki Operator.

</div>

If you only want to export flows to a Kafka consumer or IPFIX collector, or you only need dashboard metrics, then you do not need to install Loki or provide storage for Loki. The following table compares available features with and without Loki.

|  | **With Loki** | **Without Loki** |
|----|----|----|
| **Exporters** | X | X |
| **Multi-tenancy** | X | X |
| **Complete filtering and aggregations capabilities** <sup>\[1\]</sup> | X |  |
| **Partial filtering and aggregations capabilities** <sup>\[2\]</sup> | X | X |
| **Flow-based metrics and dashboards** | X | X |
| **Traffic flows view overview** <sup>\[3\]</sup> | X | X |
| **Traffic flows view table** | X |  |
| **Topology view** | X | X |
| **OpenShift Container Platform console Network Traffic tab integration** | X | X |

Comparison of feature availability with and without Loki

<div wrapper="1" role="small">

1.  Such as per pod.

2.  Such as per workload or namespace.

3.  Statistics on packet drops are only available with Loki.

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Export enriched network flow data](../../observability/network_observability/configuring-operator.xml#network-observability-enriched-flows_network_observability)

</div>

# Installing the Loki Operator

<div wrapper="1" role="_abstract">

Install the supported Loki Operator version from the software catalog to enable the secure `LokiStack` instance, which provides automatic in-cluster authentication and authorization for network observability.

</div>

The [Loki Operator versions 6.0+](https://catalog.redhat.com/software/containers/openshift-logging/loki-rhel9-operator/64479927e1820602a81cdf13) are the supported Loki Operator versions for network observability; these versions provide the ability to create a `LokiStack` instance using the `openshift-network` tenant configuration mode and provide fully-automatic, in-cluster authentication and authorization support for network observability.

<div>

<div class="title">

Prerequisites

</div>

- You have administrator permissions.

- You have access to the OpenShift Container Platform web console.

- You have access to a supported object store. For example: AWS S3, Google Cloud Storage, Azure, Swift, Minio, or OpenShift Data Foundation.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, click **Ecosystem** → **Software Catalog**.

2.  Choose **Loki Operator** from the list of available Operators, and click **Install**.

3.  Under **Installation Mode**, select **All namespaces on the cluster**.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that you installed the Loki Operator. Visit the **Ecosystem** → **Installed Operators** page and look for **Loki Operator**.

2.  Verify that **Loki Operator** is listed with **Status** as **Succeeded** in all the projects.

</div>

> [!IMPORTANT]
> To uninstall Loki, refer to the uninstallation process that corresponds with the method you used to install Loki. You might have remaining `ClusterRoles` and `ClusterRoleBindings`, data stored in object store, and persistent volume that must be removed.

## Creating a secret for Loki storage

<div wrapper="1" role="_abstract">

Create a secret with cloud storage credentials, such as for Amazon Web Services (AWS), to allow the Loki Operator to access the necessary object store for log persistence.

</div>

The Loki Operator supports a few log storage options, such as AWS S3, Google Cloud Storage, Azure, Swift, Minio, OpenShift Data Foundation. The following example shows how to create a secret for AWS S3 storage. The secret created in this example, `loki-s3`, is referenced in "Creating a LokiStack custom resource". You can create this secret in the web console or CLI.

<div>

<div class="title">

Procedure

</div>

1.  Using the web console, navigate to the **Project** → **All Projects** dropdown and select **Create Project**.

2.  Name the project `netobserv` and click **Create**.

3.  Navigate to the Import icon, **+**, in the top right corner. Paste your YAML file into the editor.

    The following shows an example secret YAML file for S3 storage:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: loki-s3
      namespace: netobserv-loki
    stringData:
      access_key_id: QUtJQUlPU0ZPRE5ON0VYQU1QTEUK
      access_key_secret: d0phbHJYVXRuRkVNSS9LN01ERU5HL2JQeFJmaUNZRVhBTVBMRUtFWQo=
      bucketnames: s3-bucket-name
      endpoint: https://s3.eu-central-1.amazonaws.com
      region: eu-central-1
    ```

    where:

    `metadata.namespace`
    Specifies the namespace for the Loki S3 secret. While this example uses `netobserv-loki`, you can use a different namespace for different components.

    `stringData.access_key_id`
    Specifies the access key ID for the S3 bucket.

    `stringData.access_key_secret`
    Specifies the secret access key for the S3 bucket.

    `stringData.bucketnames`
    Specifies the name of the S3 bucket.

    `stringData.endpoint`
    Specifies the endpoint URL for the S3 service.

    `stringData.region`
    Specifies the AWS region where the bucket is located.

</div>

<div>

<div class="title">

Verification

</div>

- After you create the secret, you view the secret listed under **Workloads** → **Secrets** in the web console.

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Creating a LokiStack custom resource](../../observability/network_observability/installing-operators.xml#network-observability-lokistack-create_network_observability)

- [Flow Collector API Reference](../../observability/network_observability/flowcollector-api.xml#network-observability-flowcollector-api-specifications_network_observability)

- [Flow Collector sample resource](../../observability/network_observability/configuring-operator.xml#network-observability-flowcollector-view_network_observability)

</div>

## Creating a LokiStack custom resource

<div wrapper="1" role="_abstract">

Deploy the `LokiStack` custom resource using the web console or OpenShift CLI (`oc`), ensuring you configure the correct namespace, deployment size, and secret name for Loki object storage.

</div>

You can deploy a `LokiStack` custom resource (CR) to create a namespace or new project.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Ecosystem** → **Installed Operators**, viewing **All projects** from the **Project** dropdown.

2.  Look for **Loki Operator**. In the details, under **Provided APIs**, select **LokiStack**.

3.  Click **Create LokiStack**.

4.  Ensure the following fields are specified in either **Form View** or **YAML view**:

    ``` yaml
    apiVersion: loki.grafana.com/v1
    kind: LokiStack
    metadata:
      name: loki
      namespace: netobserv-loki
    spec:
      size: 1x.small
      storage:
        schemas:
        - version: v13
          effectiveDate: '2022-06-01'
        secret:
          name: loki-s3
          type: s3
      storageClassName: gp3
      tenants:
        mode: openshift-network
    ```

    where:

    `metadata.namespace`
    Specifies the namespace for the `LokiStack` resource. While this example uses `netobserv-loki`, you can use a different namespace for different components.

    `spec.size`
    Specifies the deployment size. In Loki Operator 5.8 and later versions, the supported size options for production instances of Loki are `1x.extra-small`, `1x.small`, or `1x.medium`.

    > [!IMPORTANT]
    > It is not possible to change the number `1x` for the deployment size.

    `spec.storageClassName`
    Specifies a storage class name that is available on the cluster for `ReadWriteOnce` access mode. For best performance, specify a storage class that allocates block storage. Use the `oc get storageclasses` command to see available storage classes on your cluster.

    > [!IMPORTANT]
    > You must not reuse the same `LokiStack` custom resource that is used for logging.

5.  Click **Create**.

</div>

## Creating a new group for the cluster-admin user role

> [!IMPORTANT]
> Querying application logs for multiple namespaces as a `cluster-admin` user, where the sum total of characters of all of the namespaces in the cluster is greater than 5120, results in the error `Parse error: input size too long (XXXX > 5120)`. For better control over access to logs in LokiStack, make the `cluster-admin` user a member of the `cluster-admin` group. If the `cluster-admin` group does not exist, create it and add the desired users to it.

Use the following procedure to create a new group for users with `cluster-admin` permissions.

<div>

<div class="title">

Procedure

</div>

1.  Enter the following command to create a new group:

    ``` terminal
    $ oc adm groups new cluster-admin
    ```

2.  Enter the following command to add the desired user to the `cluster-admin` group:

    ``` terminal
    $ oc adm groups add-users cluster-admin <username>
    ```

3.  Enter the following command to add `cluster-admin` user role to the group:

    ``` terminal
    $ oc adm policy add-cluster-role-to-group cluster-admin cluster-admin
    ```

</div>

## Custom admin group access

If you need to see cluster-wide logs without necessarily being an administrator, or if you already have any group defined that you want to use here, you can specify a custom group using the `adminGroup` field. Users who are members of any group specified in the `adminGroups` field of the `LokiStack` custom resource (CR) have the same read access to logs as administrators.

Administrator users have access to all network logs across the cluster.

<div class="formalpara">

<div class="title">

Example LokiStack CR

</div>

``` yaml
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: loki
  namespace: netobserv
spec:
  tenants:
    mode: openshift-network
    openshift:
      adminGroups:
      - cluster-admin
      - custom-admin-group
```

</div>

- Custom admin groups are only available in this mode.

- Entering an empty list `[]` value for this field disables admin groups.

- Overrides the default groups (`system:cluster-admins`, `cluster-admin`, `dedicated-admin`)

## Loki deployment sizing

Sizing for Loki follows the format of `1x.<size>` where the value `1x` is number of instances and `<size>` specifies performance capabilities.

> [!IMPORTANT]
> It is not possible to change the number `1x` for the deployment size.

|  | 1x.demo | 1x.extra-small | 1x.small | 1x.medium |
|----|----|----|----|----|
| **Data transfer** | Demo use only | 100GB/day | 500GB/day | 2TB/day |
| **Queries per second (QPS)** | Demo use only | 1-25 QPS at 200ms | 25-50 QPS at 200ms | 25-75 QPS at 200ms |
| **Replication factor** | None | 2 | 2 | 2 |
| **Total CPU requests** | None | 14 vCPUs | 34 vCPUs | 54 vCPUs |
| **Total memory requests** | None | 31Gi | 67Gi | 139Gi |
| **Total disk requests** | 40Gi | 430Gi | 430Gi | 590Gi |

Loki sizing

## LokiStack ingestion limits and health alerts

<div wrapper="1" role="_abstract">

The `LokiStack` instance includes default ingestion and query limits that can be overridden by administrators to manage performance and prevent system alerts or errors.

</div>

> [!NOTE]
> You might want to update the ingestion and query limits if you get Loki errors showing up in the Console plugin, or in `flowlogs-pipeline` logs.

Here is an example of configured limits:

``` yaml
spec:
  limits:
    global:
      ingestion:
        ingestionBurstSize: 40
        ingestionRate: 20
        maxGlobalStreamsPerTenant: 25000
      queries:
        maxChunksPerQuery: 2000000
        maxEntriesLimitPerQuery: 10000
        maxQuerySeries: 3000
```

For more information about these settings, see the [LokiStack API reference](https://loki-operator.dev/docs/api.md/#loki-grafana-com-v1-IngestionLimitSpec).

# Installing the Network Observability Operator

<div wrapper="1" role="_abstract">

Install the Network Observability Operator and use the setup wizard to create the `FlowCollector` custom resource definition (CRD) to complete the initial configuration.

</div>

You can set specifications in the web console when you create the `FlowCollector`.

> [!IMPORTANT]
> The actual memory consumption of the Operator depends on your cluster size and the number of resources deployed. Memory consumption might need to be adjusted accordingly. For more information refer to "Network Observability controller manager pod runs out of memory" in the "Important Flow Collector configuration considerations" section.

<div>

<div class="title">

Prerequisites

</div>

- If you choose to use Loki, install the [Loki Operator version 5.7+](https://catalog.redhat.com/software/containers/openshift-logging/loki-rhel8-operator/622b46bcae289285d6fcda39).

- You must have `cluster-admin` privileges.

- One of the following supported architectures is required: `amd64`, `ppc64le`, `arm64`, or `s390x`.

- Any CPU supported by Red Hat Enterprise Linux (RHEL) 9.

- Must be configured with OVN-Kubernetes as the main network plugin, and optionally using secondary interfaces with Multus and SR-IOV.

</div>

> [!NOTE]
> Additionally, this installation example uses the `netobserv` namespace, which is used across all components. You can optionally use a different namespace.

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, click **Ecosystem** → **Software Catalog**.

2.  Choose **Network Observability Operator** from the list of available Operators in the software catalog, and click **Install**.

3.  Select the checkbox `Enable Operator recommended cluster monitoring on this Namespace`.

4.  Navigate to **Operators** → **Installed Operators**. Under Provided APIs for Network Observability, select the **Flow Collector** link.

5.  Follow the **Network Observability FlowCollector setup** wizard.

6.  Click **Create**.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

To confirm this was successful, when you navigate to **Observe** you should see **Network Traffic** listed in the options.

</div>

In the absence of **Application Traffic** within the OpenShift Container Platform cluster, default filters might show that there are "No results", which results in no visual flow. Beside the filter selections, select **Clear all filters** to see the flow.

# Enabling multi-tenancy in network observability

<div wrapper="1" role="_abstract">

Enable multi-tenancy in network observability by configuring cluster roles and namespace roles to grant project administrators and developers granular, restricted access to flows and metrics in Loki and Prometheus.

</div>

Access is enabled for project administrators. Project administrators who have limited access to some namespaces can access flows for only those namespaces.

For Developers, multi-tenancy is available for both Loki and Prometheus but requires different access rights.

<div>

<div class="title">

Prerequisite

</div>

- If you are using Loki, you have installed at least [Loki Operator version 5.7](https://catalog.redhat.com/software/containers/openshift-logging/loki-rhel8-operator/622b46bcae289285d6fcda39).

- You must be logged in as a project administrator.

</div>

<div>

<div class="title">

Procedure

</div>

- For per-tenant access, you must have the `netobserv-loki-reader` cluster role and the `netobserv-metrics-reader` namespace role to use the developer perspective. Run the following commands for this level of access:

  ``` terminal
  $ oc adm policy add-cluster-role-to-user netobserv-loki-reader <user_group_or_name>
  ```

  ``` terminal
  $ oc adm policy add-role-to-user netobserv-metrics-reader <user_group_or_name> -n <namespace>
  ```

- For cluster-wide access, non-cluster-administrators must have the `netobserv-loki-reader`, `cluster-monitoring-view`, and `netobserv-metrics-reader` cluster roles. In this scenario, you can use either the admin perspective or the developer perspective. Run the following commands for this level of access:

  ``` terminal
  $ oc adm policy add-cluster-role-to-user netobserv-loki-reader <user_group_or_name>
  ```

  ``` terminal
  $ oc adm policy add-cluster-role-to-user cluster-monitoring-view <user_group_or_name>
  ```

  ``` terminal
  $ oc adm policy add-cluster-role-to-user netobserv-metrics-reader <user_group_or_name>
  ```

</div>

# Important Flow Collector configuration considerations

<div wrapper="1" role="_abstract">

Review essential `FlowCollector` configuration options before initial deployment to avoid pod disruptions caused by later reconfiguration. Key settings include Kafka integration, enriched flow data exports, SR-IOV traffic monitoring, and advanced tracking for DNS and packet drops.

</div>

When you create the `FlowCollector` instance, you can reconfigure it, but the pods are terminated and recreated again, which can be disruptive.

Therefore, you can consider configuring the following options when creating the `FlowCollector` for the first time.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Configuring the Flow Collector resource with Kafka](../../observability/network_observability/configuring-operator.xml#network-observability-flowcollector-kafka-config_network_observability)

- [Export enriched network flow data to Kafka or IPFIX](../../observability/network_observability/configuring-operator.xml#network-observability-enriched-flows_network_observability)

- [Configuring monitoring for SR-IOV interface traffic](../../observability/network_observability/network-observability-secondary-networks.xml#network-observability-SR-IOV-config_network-observability-secondary-networks)

- [Working with conversation tracking](../../observability/network_observability/observing-network-traffic.xml#network-observability-working-with-conversations_nw-observe-network-traffic)

- [Working with DNS tracking](../../observability/network_observability/observing-network-traffic.xml#network-observability-dns-tracking_nw-observe-network-traffic)

- [Working with packet drops](../../observability/network_observability/observing-network-traffic.xml#network-observability-packet-drops_nw-observe-network-traffic)

- [Flow Collector API Reference](../../observability/network_observability/flowcollector-api.xml#network-observability-flowcollector-api-specifications_network_observability)

- [Flow Collector sample resource](../../observability/network_observability/configuring-operator.xml#network-observability-flowcollector-view_network_observability)

- [Resource considerations](../../observability/network_observability/configuring-operator.xml#network-observability-resources-table_network_observability)

- [Troubleshooting network observability controller manager pod runs out of memory](../../observability/network_observability/troubleshooting-network-observability.xml#controller-manager-pod-runs-out-of-memory_network-observability-troubleshooting)

- [Network observability architecture](../../observability/network_observability/understanding-network-observability-operator.xml#network-observability-architecture_nw-network-observability-operator)

</div>

## Migrating removed stored versions of the FlowCollector CRD

<div wrapper="1" role="_abstract">

Manually remove the deprecated `v1alpha1` version from the `FlowCollector` custom resource definition (CRD) `storedVersion` list to prevent upgrade errors and successfully migrate to Network Observability Operator 1.6.

</div>

There are two options to remove stored versions:

1.  Use the Storage Version Migrator Operator.

2.  Uninstall and reinstall the Network Observability Operator, ensuring that the installation is in a clean state.

<div>

<div class="title">

Prerequisites

</div>

- You have an older version of the Operator installed, and you want to prepare your cluster to install the latest version of the Operator. Or you have attempted to install the Network Observability Operator 1.6 and run into the error: `Failed risk of data loss updating "flowcollectors.flows.netobserv.io": new CRD removes version v1alpha1 that is listed as a stored version on the existing CRD`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that the old `FlowCollector` CRD version is still referenced in the `storedVersion`:

    ``` terminal
    $ oc get crd flowcollectors.flows.netobserv.io -ojsonpath='{.status.storedVersions}'
    ```

2.  If `v1alpha1` appears in the list of results, proceed with **Step a** to use the Kubernetes Storage Version Migrator or **Step b** to uninstall and reinstall the CRD and the Operator.

    1.  **Option 1: Kubernetes Storage Version Migrator**: Create a YAML to define the `StorageVersionMigration` object, for example `migrate-flowcollector-v1alpha1.yaml`:

        ``` yaml
        apiVersion: migration.k8s.io/v1alpha1
        kind: StorageVersionMigration
        metadata:
          name: migrate-flowcollector-v1alpha1
        spec:
          resource:
            group: flows.netobserv.io
            resource: flowcollectors
            version: v1alpha1
        ```

        1.  Save the file.

        2.  Apply the `StorageVersionMigration` by running the following command:

            ``` terminal
            $ oc apply -f migrate-flowcollector-v1alpha1.yaml
            ```

        3.  Update the `FlowCollector` CRD to manually remove `v1alpha1` from the `storedVersion`:

            ``` terminal
            $ oc edit crd flowcollectors.flows.netobserv.io
            ```

    2.  **Option 2: Reinstall**: Save the Network Observability Operator 1.5 version of the `FlowCollector` CR to a file, for example `flowcollector-1.5.yaml`.

        ``` terminal
        $ oc get flowcollector cluster -o yaml > flowcollector-1.5.yaml
        ```

        1.  Follow the steps in "Uninstalling the Network Observability Operator", which uninstalls the Operator and removes the existing `FlowCollector` CRD.

        2.  Install the Network Observability Operator latest version, 1.6.0.

        3.  Create the `FlowCollector` using backup that was saved in Step b.

</div>

<div>

<div class="title">

Verification

</div>

- Run the following command:

  ``` terminal
  $ oc get crd flowcollectors.flows.netobserv.io -ojsonpath='{.status.storedVersions}'
  ```

  The list of results should no longer show `v1alpha1` and only show the latest version, `v1beta1`.

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Kubernetes Storage Version Migrator Operator](../../operators/operator-reference.xml#cluster-kube-storage-version-migrator-operator_operator-reference)

</div>

# Installing Kafka (optional)

<div wrapper="1" role="_abstract">

The Kafka Operator is supported for large-scale environments. Kafka provides high-throughput and low-latency data feeds for forwarding network flow data in a more resilient, scalable way.

</div>

You can install the Kafka Operator as [Red Hat AMQ Streams](https://access.redhat.com/documentation/en-us/red_hat_amq_streams/2.2) from the Operator Hub, just as the Loki Operator and Network Observability Operator were installed. Refer to "Configuring the FlowCollector resource with Kafka" to configure Kafka as a storage option.

> [!NOTE]
> To uninstall Kafka, refer to the uninstallation process that corresponds with the method you used to install.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Configuring the FlowCollector resource with Kafka](../../observability/network_observability/configuring-operator.xml#network-observability-flowcollector-kafka-config_network_observability)

</div>

# Uninstalling the Network Observability Operator

<div wrapper="1" role="_abstract">

Uninstall the Network Observability Operator using the OpenShift Container Platform web console Operator Hub, working in the **Ecosystem** → **Installed Operators** area.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Remove the `FlowCollector` custom resource.

    1.  Click **Flow Collector**, which is next to the **Network Observability Operator** in the **Provided APIs** column.

    2.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) for the **cluster** and select **Delete FlowCollector**.

2.  Uninstall the Network Observability Operator.

    1.  Navigate back to the **Ecosystem** → **Installed Operators** area.

    2.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to the **Network Observability Operator** and select **Uninstall Operator**.

    3.  **Home** → **Projects** and select `openshift-netobserv-operator`

    4.  Navigate to **Actions** and select **Delete Project**

3.  Remove the `FlowCollector` custom resource definition (CRD).

    1.  Navigate to **Administration** → **CustomResourceDefinitions**.

    2.  Look for **FlowCollector** and click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=).

    3.  Select **Delete CustomResourceDefinition**.

        > [!IMPORTANT]
        > The Loki Operator and Kafka remain if they were installed and must be removed separately. Additionally, you might have remaining data stored in an object store, and a persistent volume that must be removed.

</div>
