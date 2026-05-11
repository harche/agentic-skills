<div wrapper="1" role="_abstract">

In Operator Lifecycle Manager (OLM) v1, extensions watch all namespaces by default. Some Operators support only namespace-scoped watching based on OLM (Classic) install modes. To install these Operators, configure the watch namespace for the extension. For more information, see "Discovering bundle install modes".

</div>

> [!IMPORTANT]
> Configuring a watch namespace for a cluster extension is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

# Extension configuration

<div wrapper="1" role="_abstract">

Configure the namespace an extension watches by using the `.spec.config` field in the `ClusterExtension` resource.

</div>

> [!IMPORTANT]
> OLM v1 configuration API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

Extensions watch all namespaces by default. Some Operators support only namespace-scoped watching based on OLM (Classic) install modes. Configure the `.spec.config.inline.watchNamespace` field to install these Operators.

Whether you must configure this field depends on the install modes supported by the bundle.

## Configuration API structure

The configuration API uses an opaque structure. The bundle validates the configuration values, not OLM v1. Operator authors can define their own configuration requirements.

Currently, the `Inline` configuration type is the only supported type:

<div class="formalpara">

<div class="title">

Example inline configuration

</div>

``` yaml
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <extension_name>
...
spec:
  namespace: <installation_namespace>
  config:
    configType: Inline
    inline:
      watchNamespace: <watch_namespace>
```

</div>

where:

`<installation_namespace>`
Specifies the namespace where the extension components run.

`config.configType`
Specifies the configuration type. Currently, `Inline` is the only supported type.

`<watch_namespace>`
Specifies the namespace where the extension watches for custom resources. The watch namespace can match or differ from the installation namespace, depending on the install modes supported by the bundle.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Operator groups](../../operators/understanding/olm/olm-understanding-operatorgroups.xml#olm-understanding-operatorgroups)

</div>

# Watch namespace configuration requirements

<div wrapper="1" role="_abstract">

Avoid installation failures by using the correct `watchNamespace` value for the install modes supported by your bundle. Requirements vary based on whether the bundle supports `AllNamespaces`, `OwnNamespace`, and `SingleNamespace` install modes.

</div>

OLM (Classic) `registry+v1` bundles declare the install modes they support. These install modes control whether `watchNamespace` configuration is required or optional, and what values are valid.

> [!NOTE]
> OLM v1 does not support multi-tenancy. You cannot install the same extension more than once on a cluster. As a result, the `MultiNamespace` install mode is not supported.

`AllNamespaces`
Watches resources across all namespaces in the cluster.

`OwnNamespace`
Watches resources only in the installation namespace.

`SingleNamespace`
Watches resources in a single namespace that differs from the installation namespace.

Whether the `.spec.config.inline.watchNamespace` field is required depends on the install modes that the bundle supports.

| Bundle install mode support | watchNamespace field | Valid values |
|----|----|----|
| `AllNamespaces` mode only | Not applicable | The `watchNamespace` field is not supported. Extensions watch all namespaces. |
| `OwnNamespace` mode only | Required | Must match `.spec.namespace` field |
| `SingleNamespace` mode only | Required | Must differ from `.spec.namespace` field |
| Both `OwnNamespace` and `SingleNamespace` install modes | Required | Can match or differ from `.spec.namespace` field |
| `AllNamespaces` install mode with one or both of the `OwnNamespace` and `SingleNamespace` install modes | Optional | Omit to watch all namespaces, or specify a namespace to watch only that namespace |

Watch namespace requirements by bundle capability

> [!IMPORTANT]
> OLM v1 validates the `watchNamespace` value based on the install mode support that is declared by the bundle. The installation fails with a validation error if you specify an invalid value or omit a required field.

# Discovering bundle install modes

<div wrapper="1" role="_abstract">

You can render the bundle metadata to find which install modes a bundle supports.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You have installed the `jq` CLI tool.

- You have installed the `opm` CLI tool.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Render the bundle metadata by running the following command:

    ``` terminal
    $ opm render <bundle_image> -o json | \
      jq 'select(.schema == "olm.bundle") | .properties[] | select(.type == "olm.bundle.object")'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` json
    {
      "type": "olm.bundle.object",
      "value": {
        "data": "...",
        "ref": "olm.csv"
      }
    }
    ```

    </div>

2.  Decode the base64-encoded CSV data to view install mode declarations:

    ``` terminal
    $ echo "<base64_data>" | base64 -d | jq '.spec.installModes'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` json
    [
      {
        "type": "OwnNamespace",
        "supported": true
      },
      {
        "type": "SingleNamespace",
        "supported": true
      },
      {
        "type": "MultiNamespace",
        "supported": false
      },
      {
        "type": "AllNamespaces",
        "supported": false
      }
    ]
    ```

    </div>

    In this example, the bundle supports both `OwnNamespace` and `SingleNamespace` modes. The `.spec.config.inline.watchNamespace` field is required and can match or differ from the `.spec.namespace` field.

</div>

# Configuring a watch namespace for a cluster extension (Technology Preview)

<div wrapper="1" role="_abstract">

You can configure the watch namespace for extensions that support namespace-scoped resource watching.

</div>

> [!IMPORTANT]
> Configuring watch namespace for a cluster extension is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

- You have enabled the `TechPreviewNoUpgrade` feature set on the cluster.

- You have created a service account and assigned enough role-based access controls (RBAC) to install, update, and manage the extension. For more information, see "Cluster extension permissions".

- You have verified the supported install modes for the extension and determined the required `watchNamespace` configuration.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a custom resource (CR) based on where you want the extension to watch for resources:

    - To configure the extension to watch its own installation namespace:

      ``` yaml
      apiVersion: olm.operatorframework.io/v1
      kind: ClusterExtension
      metadata:
        name: <extension_name>
      spec:
        namespace: <installation_namespace>
        config:
          configType: Inline
          inline:
            watchNamespace: <installation_namespace>
        serviceAccount:
          name: <service_account>
        source:
          sourceType: Catalog
          catalog:
            packageName: <package_name>
            version: <version>
            upgradeConstraintPolicy: CatalogProvided
      ```

      where:

      `config.inline.watchNamespace`
      Specifies the namespace to watch for resources. For requirements and valid values, see "Extension configuration".

    - To configure the extension to watch a different namespace:

      ``` yaml
      apiVersion: olm.operatorframework.io/v1
      kind: ClusterExtension
      metadata:
        name: <extension_name>
      spec:
        namespace: <installation_namespace>
        config:
          configType: Inline
          inline:
            watchNamespace: <watched_namespace>
        serviceAccount:
          name: <service_account>
        source:
          sourceType: Catalog
          catalog:
            packageName: <package_name>
            version: <version>
            upgradeConstraintPolicy: CatalogProvided
      ```

2.  Apply the CR to the cluster by running the following command:

    ``` terminal
    $ oc apply -f <cluster_extension_cr>.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the extension installed successfully by running the following command:

  ``` terminal
  $ oc get clusterextension <extension_name> -o yaml
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` yaml
  apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    name: <extension_name>
  spec:
    namespace: <installation_namespace>
    config:
      configType: Inline
      inline:
        watchNamespace: <installation_namespace>
  status:
    conditions:
    - type: Installed
      status: "True"
      reason: Succeeded
  ```

  </div>

</div>

## Watch namespace configuration examples

<div wrapper="1" role="_abstract">

To configure the `watchNamespace` field correctly for your bundle’s install mode, see the following examples. These show valid configurations for Operators that support the `AllNamespaces`, `OwnNamespace`, and `SingleNamespace` install modes.

</div>

<div class="formalpara">

<div class="title">

Example `AllNamespaces` install mode

</div>

``` yaml
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: example-extension
spec:
  namespace: openshift-operators
  serviceAccount:
    name: example-sa
  source:
    sourceType: Catalog
    catalog:
      packageName: example-operator
```

</div>

- The `config` field is omitted. The extension watches all namespaces by default.

<div class="formalpara">

<div class="title">

Example `OwnNamespace` install mode

</div>

``` yaml
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: example-extension
spec:
  namespace: example-operators
  config:
    configType: Inline
    inline:
      watchNamespace: example-operators
  serviceAccount:
    name: example-sa
  source:
    sourceType: Catalog
    catalog:
      packageName: example-operator
```

</div>

- You must set the `watchNamespace` field to use the `OwnNamespace` install mode.

- The `watchNamespace` value must match the `spec.namespace` field value.

<div class="formalpara">

<div class="title">

Example `SingleNamespace` install mode

</div>

``` yaml
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: example-extension
spec:
  namespace: example-operators
  config:
    configType: Inline
    inline:
      watchNamespace: production
  serviceAccount:
    name: example-sa
  source:
    sourceType: Catalog
    catalog:
      packageName: example-operator
```

</div>

- You must set the `watchNamespace` field to use the `SingleNamespace` install mode.

- The `watchNamespace` value must differ from the `spec.namespace` field value.

- In this example, the extension runs in the `example-operators` namespace but watches resources in the `production` namespace.

## Watch namespace validation errors

<div wrapper="1" role="_abstract">

Validation errors occur when the `watchNamespace` field is omitted or contains an invalid value for the install modes supported by the bundle.

</div>

| Error | Cause | Resolution |
|----|----|----|
| Required field missing | The bundle requires the `watchNamespace` field but it is omitted. | Add the `watchNamespace` field with a value that matches the install modes supported by the bundle. |
| `OwnNamespace` validation error | The bundle only supports `OwnNamespace` mode but the `watchNamespace` value does not match the `.spec.namespace` field. | Set the `watchNamespace` field to the same value as the `.spec.namespace` field. |
| `SingleNamespace` validation error | The bundle only supports `SingleNamespace` mode but the `watchNamespace` value matches the `.spec.namespace` field. | Set the `watchNamespace` field to a different namespace than the `.spec.namespace` field. |
| Invalid configuration | The `.spec.config` structure is malformed or has unsupported fields. | Verify the configuration follows the correct API structure with `configType: Inline` and valid `inline` fields. |

Common `watchNamespace` field validation errors

# Additional resources

- [Installing a cluster extension in all namespaces](../../extensions/ce/managing-ce.xml#olmv1-installing-an-operator_managing-ce)
