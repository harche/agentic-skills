<div wrapper="1" role="_abstract">

External Secrets Operator for Red Hat OpenShift uses the following two APIs to configure the `external-secrets` application deployment.

</div>

| Group                   | Version    | Kind                     |
|-------------------------|------------|--------------------------|
| `operator.openshift.io` | `v1alpha1` | `externalsecretsConfig`  |
| `operator.openshift.io` | `v1alpha1` | `externalsecretsmanager` |

The following list contains the External Secrets Operator for Red Hat OpenShift APIs:

- ExternalSecretsConfig

- ExternalSecretsManager

# externalSecretsManagerList

<div wrapper="1" role="_abstract">

The `externalSecretsManagerList` object fetches the list of `externalSecretsManager` objects.

</div>

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `apiVersion` | *string* | The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1`. |  |  |
| `kind` | *string* | `kind` specifies the type of the object, which is `externalSecretsManagerList` for this API. |  |  |
| `metadata` | [*ListMeta*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#listmeta-v1-meta) | Refer to Kubernetes API documentation for details about the `metadata` fields. |  |  |
| `items` | *array* |  |  |  |

# externalSecretsManager

<div wrapper="1" role="_abstract">

The `externalSecretsManager` object defines the configuration and information of deployments managed by the External Secrets Operator. Set the name to `cluster` as this allows only one instance of `externalSecretsManager` per cluster.

</div>

You can configure global options by using `externalSecretsManager`. This serves as a centralized configuration for managing multiple controllers of the Operator. The Operator automatically creates the `externalSecretsManager` object during installation.

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `apiVersion` | *string* | The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1`. |  |  |
| `kind` | *string* | `kind` specifies the type of the object, which is `externalSecretsManager` for this Object. |  |  |
| `metadata` | [*ObjectMeta*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for details about the `metadata` fields. |  |  |
| `spec` | *object* | `spec` contains specifications of the desired behavior. |  |  |
| `status` | *object* | `status` displays the most recently observed state of the controllers in the External Secrets Operator. |  |  |

# externalSecretsConfigList

<div wrapper="1" role="_abstract">

The `externalSecretsConfigList` object fetches the list of `externalSecretsConfig` objects.

</div>

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `apiVersion` | *string* | The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1` |  |  |
| `kind` | *string* | `kind` specifies the type of the object, which is `externalSecretsList` for this API. |  |  |
| `metadata` | [*ListMeta*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#listmeta-v1-meta) | Refer to Kubernetes API documentation for details about the `metadata` fields. |  |  |
| `items` | *array* | `Items` contains a list of `externalSecrets` objects. |  |  |

# externalSecretsConfig

<div wrapper="1" role="_abstract">

The `externalSecretsConfig` object defines the configuration and information for the managed `external-secrets` operand deployment. Set the name to `cluster` as `externalSecretsConfig` object allows only one instance per cluster.

</div>

Creating an `externalSecretsConfig` object triggers the deployment of the `external-secrets` operand and maintains the desired state.

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `apiVersion` | *string* | The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1`. |  |  |
| `kind` | *string* | `kind` specifies the type of the object, which is `externalSecrets` for this object. |  |  |
| `metadata` | [*ObjectMeta*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#objectmeta-v1-meta) | Refer to Kubernetes API documentation for details about the `metadata` fields. |  |  |
| `spec` | *object* | `spec` contains the specifications of the desired behavior of the `externalSecrets` object. |  |  |
| `status` | *object* | `status` displays the most recently observed status of the `externalSecrets` object. |  |  |

# Listing fields in External Secrets Operator for Red Hat OpenShift APIs

The following fields apply to the External Secrets Operator for Red Hat OpenShift APIs.

# externalSecretsManagerSpec

<div wrapper="1" role="_abstract">

The `externalSecretsManagerSpec` field defines the desired behavior of the `externalSecretsManager` object.

</div>

| Field | type | Description | Default | Validation |
|----|----|----|----|----|
| `globalConfig` | *object* | `globalConfig` configures the behavior of deployments that External Secrets Operator manages. |  | Optional |

# externalSecretsManagerStatus

<div wrapper="1" role="_abstract">

The `externalSecretsManagerStatus` field shows the most recently observed status of the `externalSecretsManager` object.

</div>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>controllerStatuses</code></p></td>
<td style="text-align: left;"><p><em>array</em></p></td>
<td style="text-align: left;"><p><code>controllerStatuses</code> holds the observed conditions of the controllers used by the Operator.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>lastTransitionTime</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#time-v1-meta"><em>Time</em></a></p></td>
<td style="text-align: left;"><p><code>lastTransitionTime</code> records the most recent time the status of the condition changed.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Format: date-time</p>
<p>Type: string</p></td>
</tr>
</tbody>
</table>

# externalSecretsConfigSpec

<div wrapper="1" role="_abstract">

The `externalSecretsConfigSpec` field defines the desired behavior of the `externalSecrets` object.

</div>

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `appConfig` | *object* | `appConfig` configures the behavior of the `external-secrets` operand. |  | Optional |
| `plugins` | *object* | `plugins` configures the optional provider plugins. |  | Optional |
| `controllerConfig` | *object* | `controllerConfig` configures the controller to set up defaults that enable `external-secrets` operand. |  | Optional |

# externalSecretsConfigStatus

<div wrapper="1" role="_abstract">

The `externalSecretsConfigStatus` field shows the most recently observed status of the `externalSecretsConfig` Object.

</div>

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `conditions` | [*Condition*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#condition-v1-meta) *array* | `conditions` contains information about the current state of deployment. |  |  |
| `externalSecretsImage` | *string* | `externalSecretsImage` specifies the image name and tag used for deploy `external-secrets` operand. |  |  |
| `bitwardenSDKServerImage` | *string* | `bitwardenSDKServerImage` specifies the name of the image and tag used for deploying the `bitwarden-sdk-server`. |  |  |

# globalConfig

<div wrapper="1" role="_abstract">

The `globalConfig` field configures the behavior of the External Secrets Operator.

</div>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>labels</code></p></td>
<td style="text-align: left;"><p><em>integer</em></p></td>
<td style="text-align: left;"><p><code>labels</code> applies to all resources created by the Operator. This field can have a maximum of 20 entries</p></td>
<td style="text-align: left;"><p>1</p></td>
<td style="text-align: left;"><p>The maximum number of properties is 20</p>
<p>The minimum number of properties is 0</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>logLevel</code></p></td>
<td style="text-align: left;"><p><em>integer</em></p></td>
<td style="text-align: left;"><p><code>logLevel</code> supports a range of values as defined in the <a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-instrumentation/logging.md#what-method-to-use">kubernetes logging guidelines</a>.</p></td>
<td style="text-align: left;"><p>1</p></td>
<td style="text-align: left;"><p>The maximum range value is 5</p>
<p>The minimum range value is 1</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#resourcerequirements-v1-core"><em>ResourceRequirements</em></a></p></td>
<td style="text-align: left;"><p><code>resources</code> defines the resource requirements. You cannot change the value of this field after setting it initially. For more information, see <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>affinity</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#affinity-v1-core"><em>Affinity</em></a></p></td>
<td style="text-align: left;"><p><code>affinity</code> sets the scheduling affinity rules. For more information, see <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/">https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#toleration-v1-core"><em>Toleration</em></a> <em>array</em></p></td>
<td style="text-align: left;"><p><code>tolerations</code> sets the pod tolerations. For more information, see <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/">https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of items is 50</p>
<p>The minimum number of items is 0</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeSelector</code></p></td>
<td style="text-align: left;"><p><em>object (keys:string, values:string)</em></p></td>
<td style="text-align: left;"><p><code>nodeSelector</code> defines the scheduling criteria by using the node labels. For more information, see <a href="https://kubernetes.io/docs/concepts/configuration/assign-pod-node/">https://kubernetes.io/docs/concepts/configuration/assign-pod-node/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of properties is 50</p>
<p>The minimum number of properties is 0</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxy</code></p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><p><code>proxy</code> sets the proxy configurations available in the operand containers managed by the Operator as environment variables.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Optional</p></td>
</tr>
</tbody>
</table>

# controllerConfig

<div wrapper="1" role="_abstract">

The `controllerConfig` specifies the configurations used by the controller when installing the `external-secrets` operand and the plugins.

</div>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>certProvider</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>certProvider</code> defines the configuration for the certificate providers used to manage TLS certificates for webhook and plugins.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>labels</code></p></td>
<td style="text-align: left;"><p><em>object (keys:string, values:string)</em></p></td>
<td style="text-align: left;"><p><code>labels</code> field applies labels to all resources created for the <code>external-secrets</code> operand deployment.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of properties is 20.</p>
<p>The minimum number of properties is 0.</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>annotations</code></p></td>
<td style="text-align: left;"><p><em>object (keys:string, values:string)</em></p></td>
<td style="text-align: left;"><p><code>annotations</code> add custom annotations to all the resources created for the <code>external-secrets</code> deployment. The annotations are merged with any default annotations set by the Operator. User-specified annotations take precedence over defaults in case of conflicts. Annotation keys containing the reserved domains <code>kubernetes.io/</code>, <code>openshift.io/</code>, <code>k8s.io/</code>, or <code>cert-manager.io/</code> (including subdomains like <code>*.kubernetes.io/</code>) are not allowed.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of properties is 20.</p>
<p>The minimum number of properties is 0.</p>
<p>Optional</p></td>
</tr>
</tbody>
</table>

# controllerStatus

<div wrapper="1" role="_abstract">

The `controllerStatus` field contains the observed conditions of the controllers used by the Operator.

</div>

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `name` | *string* | `name` specifies the name of the controller for which the observed condition is recorded. |  | Required |
| `conditions` | *array* | `conditions` contains information about the current state of the External Secrets Operator controllers. |  |  |
| `observedGeneration` | *integer* | `observedGeneration` represents the `.metadata.generation` on the observed resource. |  | The minimum number of observed resources is 0. |

# applicationConfig

<div wrapper="1" role="_abstract">

The `applicationConfig` specifies the configurations for the `external-secrets` operand.

</div>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>logLevel</code></p></td>
<td style="text-align: left;"><p><em>integer</em></p></td>
<td style="text-align: left;"><p><code>logLevel</code> supports a range of values as defined in the <a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-instrumentation/logging.md#what-method-to-use">kubernetes logging guidelines</a>.</p></td>
<td style="text-align: left;"><p>1</p></td>
<td style="text-align: left;"><p>The maximum range value is 5</p>
<p>The minimum range value is 1</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operatingNamespace</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>operatingNamespace</code> restricts the <code>external-secrets</code> operand operations to the provided namespace. Enabling this field disables <code>ClusterSecretStore</code> and <code>ClusterExternalSecret</code>.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 63</p>
<p>The minimum length is 1</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>webhookConfig</code></p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><p><code>webhookConfig</code> configures webhook specifics of the <code>external-secrets</code> operand.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#resourcerequirements-v1-core"><em>ResourceRequirements</em></a></p></td>
<td style="text-align: left;"><p><code>resources</code> defines the resource requirements. You cannot change the value of this field after setting it initially. For more information, see <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>affinity</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#affinity-v1-core"><em>Affinity</em></a></p></td>
<td style="text-align: left;"><p><code>affinity</code> sets the scheduling affinity rules. For more information, see <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/">https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#toleration-v1-core"><em>Toleration</em></a> <em>array</em></p></td>
<td style="text-align: left;"><p><code>tolerations</code> sets the pod tolerations. For more information, see <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/">https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of items is 50</p>
<p>The minimum number of items is 0</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeSelector</code></p></td>
<td style="text-align: left;"><p><em>object (keys:string, values:string)</em></p></td>
<td style="text-align: left;"><p><code>nodeSelector</code> defines the scheduling criteria by using node labels. For more information, see <a href="https://kubernetes.io/docs/concepts/configuration/assign-pod-node/">https://kubernetes.io/docs/concepts/configuration/assign-pod-node/</a></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of properties is 50</p>
<p>The minimum number of properties is 0</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxy</code></p></td>
<td style="text-align: left;"><p><em>object (keys:string, values:string)</em></p></td>
<td style="text-align: left;"><p><code>proxy</code> sets the proxy configurations available in operand containers managed by the Operator as environment variables.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Optional</p></td>
</tr>
</tbody>
</table>

# bitwardenSecretManagerProvider

<div wrapper="1" role="_abstract">

The `bitwardenSecretManagerProvider` field enables the Bitwarden secrets manager provider and sets up the additional service required to connect to the Bitwarden server.

</div>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>mode</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>mode</code> field enables the <code>bitwardenSecretManagerProvider</code> provider state, which can be set to <code>Enabled</code> or <code>Disabled</code>. If set to <code>Enabled</code>, the Operator ensures the plugin is deployed and synchronized. If set to <code>Disabled</code>, the Bitwarden provider plugin reconciliation is disabled. The plugin and resources remain in their current state, and are not managed by the Operator.</p></td>
<td style="text-align: left;"><p><code>Disabled</code></p></td>
<td style="text-align: left;"><p>enum: [Enabled Disabled]</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secretRef</code></p></td>
<td style="text-align: left;"><p><em>SecretReference</em></p></td>
<td style="text-align: left;"><p><code>SecretRef</code> specifies the Kubernetes secret that contains the TLS key pair for the Bitwarden server. If this reference is not provided and the <code>certManagerConfig</code> field is configured, the issuer defined in <code>certManagerConfig</code> generates the required certificate. The secret must use <code>tls.crt</code> for certificate, <code>tls.key</code> for the private key, and <code>ca.crt</code> for CA certificate.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Optional</p></td>
</tr>
</tbody>
</table>

# webhookConfig

<div wrapper="1" role="_abstract">

The `webhookConfig` field configures the specifics of the `external-secrets` application webhook.

</div>

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `certificateCheckInterval` | [*Duration*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#duration-v1-meta) | `certificateCheckInterval` configures the polling interval to check certificate validity. | 5m | Optional |

# certManagerConfig

<div wrapper="1" role="_abstract">

The `certManagerConfig` field configures the `cert-manager` Operator settings.

</div>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>mode</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>mode</code> specifies whether to use cert-manager for certificate management instead of the built-in <code>cert-controller</code> which can be indicated by setting either <code>Enabled</code> or <code>Disabled</code>. If set to <code>Enabled</code>, uses <code>cert-manager</code> for obtaining the certificates for the webhook server and other components. If set to <code>Disabled</code>, uses the <code>cert-controller</code> for obtaining the certificates for the webhook server. <code>Disabled</code> is the default behavior.</p></td>
<td style="text-align: left;"><p>false</p></td>
<td style="text-align: left;"><p>enum: [true false]</p>
<p>Required</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>injectAnnotations</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>injectAnnotations</code> adds the <code>cert-manager.io/inject-ca-from</code> annotation to the webhooks and custom resource definitions (CRDs) to automatically configure the webhook with the <code>cert-manager</code> Operator certificate authority (CA). This requires CA Injector to be enabled in <code>cert-manager</code> Operator. Set this field to <code>true</code> or <code>false</code>. When set, this field cannot be changed.</p></td>
<td style="text-align: left;"><p>false</p></td>
<td style="text-align: left;"><p>enum: [true false]</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>issuerRef</code></p></td>
<td style="text-align: left;"><p><em>ObjectReference</em></p></td>
<td style="text-align: left;"><p><code>issuerRef</code> contains details of the referenced object used for obtaining certificates. The object must exist in the <code>external-secrets</code> namespace unless a cluster-scoped <code>cert-manager</code> Operator issuer is used.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Required</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>certificateDuration</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#duration-v1-meta"><em>Duration</em></a></p></td>
<td style="text-align: left;"><p><code>certificateDuration</code> sets the validity period of the webhook certificate.</p></td>
<td style="text-align: left;"><p>8760h</p></td>
<td style="text-align: left;"><p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>certificateRenewBefore</code></p></td>
<td style="text-align: left;"><p><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#duration-v1-meta"><em>Duration</em></a></p></td>
<td style="text-align: left;"><p><code>certificateRenewBefore</code> sets the ahead time to renew the webhook certificate before expiry.</p></td>
<td style="text-align: left;"><p>30m</p></td>
<td style="text-align: left;"><p>Optional</p></td>
</tr>
</tbody>
</table>

# certProvidersConfig

<div wrapper="1" role="_abstract">

The `certProvidersConfig` defines the configuration for the certificate providers used to manage TLS certificates for webhook and plugins.

</div>

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `certManager` | *object* | `certManager` defines the configuration for `cert-manager` provider specifics. |  | Optional |

# objectReference

The `ObjectReference` field refers to an object by its name, kind, and group.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>name</code> specifies the name of the resource being referred to.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 253 characters.</p>
<p>The minimum length is 1 character.</p>
<p>Required</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>kind</code> specifies the kind of the resource being referred to.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 253 characters.</p>
<p>The minimum length is 1 character.</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>group</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>group</code> specifies the group of the resource being referred to.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 253 characters.</p>
<p>The minimum length is 1 character.</p>
<p>Optional</p></td>
</tr>
</tbody>
</table>

# secretReference

<div wrapper="1" role="_abstract">

The `secretReference` field refers to a secret with the given name in the same namespace where it used.

</div>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>name</code> specifies the name of the secret resource being referred to.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 253.</p>
<p>The minimum length is 1.</p>
<p>Required</p></td>
</tr>
</tbody>
</table>

# condition

<div wrapper="1" role="_abstract">

The `condition` field holds information about the condition of the `external-secrets` deployment.

</div>

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `type` | *string* | `type` contains the condition of the deployment. |  | Required |
| `status` | [*ConditionStatus*](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#conditionstatus-v1-meta) | `status` contains the status of the condition of the deployment |  |  |
| `message` | *string* | `message` provides details on the state of the deployment |  |  |

# conditionalStatus

<div wrapper="1" role="_abstract">

The `conditionalStatus` field holds information about the current state of the `external-secrets` deployment.

</div>

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `conditions` | *array* | `conditions` contains information on the current state of the deployment. |  |  |

# mode

<div wrapper="1" role="_abstract">

The `mode` field indicates the operational state of the optional features.

</div>

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `Enabled` |  | `Enabled` indicates the optional configuration is enabled. |  |  |
| `Disabled` |  | `Disabled` indicates the optional configuration is disabled. |  |  |

# pluginsConfig

<div wrapper="1" role="_abstract">

The `pluginsConfig` configures the optional plugins.

</div>

| Field | Type | Description | Default | Validation |
|----|----|----|----|----|
| `bitwardenSecretManagerProvider` | *object* | `bitwardenSecretManagerProvider` enables the `bitwarden-secrets-manager` provider plugin for connecting with the 'bitwarden-secrets-manager'. |  | Optional |

# proxyConfig

<div wrapper="1" role="_abstract">

The `proxyConfig` holds the proxy configurations which are made available in the operand containers and managed by the Operator as environment variables.

</div>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>httpProxy</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p>The <code>httpProxy</code> field contains the URL of the proxy for HTTP requests. This field can have a maximum of 2048 characters.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 2048 characters.</p>
<p>The minimum length is 0 characters.</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpsProxy</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p>The <code>httpsProxy</code> field contains the URL of the proxy for HTTPS requests. This field can have a maximum of 2048 characters.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 2048 characters.</p>
<p>The minimum length is 0 characters.</p>
<p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>noProxy</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p>The <code>noProxy</code> field is a comma-separated list of hostnames, classless inter-domain routings (CIDRs), and IP addresses or a combination of the three for which the proxy should not be used. This field can have a maximum of 4096 characters.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum length is 4096 characters.</p>
<p>The minimum length is 0 characters.</p>
<p>Optional</p></td>
</tr>
</tbody>
</table>

# componentConfig

<div wrapper="1" role="_abstract">

The `componentConfig` field defines configuration overrides for a specific `external-secrets` component.

</div>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>componentName</code></p></td>
<td style="text-align: left;"><p><em>string</em></p></td>
<td style="text-align: left;"><p><code>componentName</code> identifies which <code>external-secrets</code> component this configuration applies to. Valid values are <code>ExternalSecretsCoreController</code>, <code>Webhook</code>, <code>CertController</code>, and <code>BitwardenSDKServer</code>.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Enum: [<code>ExternalSecretsCoreController</code>, <code>Webhook</code>, <code>CertController</code>, <code>BitwardenSDKServer</code>]</p>
<p>Required</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deploymentConfigs</code></p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><p><code>deploymentConfigs</code> specifies overrides for the Kubernetes Deployment resource of this component.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Optional</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>overrideEnv</code></p></td>
<td style="text-align: left;"><p><strong>EnvVar</strong></p>
<p><em>array</em></p></td>
<td style="text-align: left;"><p><code>overrideEnv</code> specifies custom environment variables for this component’s container. These are merged with operator-managed environment variables, with user-defined values taking precedence. Environment variable names starting with <code>HOSTNAME</code>, <code>KUBERNETES_</code> or <code>EXTERNAL_SECRETS_</code> are reserved and are not allowed.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The maximum number of items is 50.</p>
<p>Optional</p></td>
</tr>
</tbody>
</table>

# deploymentConfig

<div wrapper="1" role="_abstract">

The `deploymentConfig` field defines configuration overrides for a Kubernetes Deployment resource.

</div>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>revisionHistoryLimit</code></p></td>
<td style="text-align: left;"><p><em>integer</em></p></td>
<td style="text-align: left;"><p><code>revisionHistoryLimit</code> specifies the number of old <code>ReplicaSets</code> to retain for rollback purposes. This allows rolling back to previous deployment versions using the command <code>oc rollout undo</code>. Must be at least 1 to ensure rollback capability.</p></td>
<td style="text-align: left;"><p>10</p></td>
<td style="text-align: left;"><p>The minimum value is 1.</p>
<p>The maximum value is 50.</p>
<p>Optional</p></td>
</tr>
</tbody>
</table>
