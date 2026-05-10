<div wrapper="1" role="_abstract">

The Red Hat build of OpenTelemetry Operator uses a custom resource definition (CRD) file that defines the architecture and configuration settings to be used when creating and deploying the Red Hat build of OpenTelemetry resources. You can install the default configuration or modify the file.

</div>

# Deployment modes

<div wrapper="1" role="_abstract">

The `OpenTelemetryCollector` custom resource allows you to specify one of the following deployment modes for the OpenTelemetry Collector:

</div>

Deployment
The default.

StatefulSet
If you need to run stateful workloads, for example when using the Collector’s File Storage Extension or Tail Sampling Processor, use the StatefulSet deployment mode.

DaemonSet
If you need to scrape telemetry data from every node, for example by using the Collector’s Filelog Receiver to read container logs, use the DaemonSet deployment mode.

Sidecar
If you need access to log files inside a container, inject the Collector as a sidecar, and use the Collector’s Filelog Receiver and a shared volume such as `emptyDir`.

If you need to configure an application to send telemetry data via `localhost`, inject the Collector as a sidecar, and set up the Collector to forward the telemetry data to an external service via an encrypted and authenticated connection. The Collector runs in the same pod as the application when injected as a sidecar.

> [!NOTE]
> If you choose the sidecar deployment mode, then in addition to setting the `spec.mode: sidecar` field in the `OpenTelemetryCollector` custom resource CR, you must also set the `sidecar.opentelemetry.io/inject` annotation as a pod annotation or namespace annotation. If you set this annotation on both the pod and namespace, the pod annotation takes precedence if it is set to either `false` or the `OpenTelemetryCollector` CR name.
>
> As a pod annotation, the `sidecar.opentelemetry.io/inject` annotation supports several values:
>
> ``` yaml
> apiVersion: v1
> kind: Pod
> metadata:
>   ...
>   annotations:
>     sidecar.opentelemetry.io/inject: "<supported_value>"
> ...
> ```
>
> - Supported values:
>
>   `false`
>   Does not inject the Collector. This is the default if the annotation is missing.
>
>   `true`
>   Injects the Collector with the configuration of the `OpenTelemetryCollector` CR in the same namespace.
>
>   `<collector_name>`
>   Injects the Collector with the configuration of the `<collector_name>` `OpenTelemetryCollector` CR in the same namespace.
>
>   `<namespace>/<collector_name>`
>   Injects the Collector with the configuration of the `<collector_name>` `OpenTelemetryCollector` CR in the `<namespace>` namespace.

# OpenTelemetry Collector configuration options

<div wrapper="1" role="_abstract">

The OpenTelemetry Collector consists of five types of components that access telemetry data:

</div>

- Receivers

- Processors

- Exporters

- Connectors

- Extensions

You can define multiple instances of components in a custom resource YAML file. When configured, these components must be enabled through pipelines defined in the `spec.config.service` section of the YAML file. As a best practice, only enable the components that you need.

<div class="formalpara">

<div class="title">

Example of the OpenTelemetry Collector custom resource file

</div>

``` yaml
apiVersion: opentelemetry.io/v1beta1
kind: OpenTelemetryCollector
metadata:
  name: cluster-collector
  namespace: tracing-system
spec:
  mode: deployment
  observability:
    metrics:
      enableMetrics: true
  config:
    receivers:
      otlp:
        protocols:
          grpc: {}
          http: {}
    processors: {}
    exporters:
      otlp:
        endpoint: otel-collector-headless.tracing-system.svc:4317
        tls:
          ca_file: "/var/run/secrets/kubernetes.io/serviceaccount/service-ca.crt"
      prometheus:
        endpoint: 0.0.0.0:8889
        resource_to_telemetry_conversion:
          enabled: true # by default resource attributes are dropped
    service:
      pipelines:
        traces:
          receivers: [otlp]
          processors: []
          exporters: [otlp]
        metrics:
          receivers: [otlp]
          processors: []
          exporters: [prometheus]
```

</div>

- If a component is configured but not defined in the `service` section, the component is not enabled.

<table>
<caption>Parameters used by the Operator to define the OpenTelemetry Collector</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Values</th>
<th style="text-align: left;">Default</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>receivers:</code></pre></td>
<td style="text-align: left;"><p>A receiver is how data gets into the Collector. By default, no receivers are configured. There must be at least one enabled receiver for a configuration to be considered valid. Receivers are enabled by being added to a pipeline.</p></td>
<td style="text-align: left;"><p><code>otlp</code>, <code>jaeger</code>, <code>prometheus</code>, <code>zipkin</code>, <code>kafka</code>, <code>opencensus</code></p></td>
<td style="text-align: left;"><p>None</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>processors:</code></pre></td>
<td style="text-align: left;"><p>Processors run through the received data before it is exported. By default, no processors are enabled.</p></td>
<td style="text-align: left;"><p><code>batch</code>, <code>memory_limiter</code>, <code>resourcedetection</code>, <code>attributes</code>, <code>span</code>, <code>k8sattributes</code>, <code>filter</code>, <code>routing</code></p></td>
<td style="text-align: left;"><p>None</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>exporters:</code></pre></td>
<td style="text-align: left;"><p>An exporter sends data to one or more back ends or destinations. By default, no exporters are configured. There must be at least one enabled exporter for a configuration to be considered valid. Exporters are enabled by being added to a pipeline. Exporters might be used with their default settings, but many require configuration to specify at least the destination and security settings.</p></td>
<td style="text-align: left;"><p><code>otlp</code>, <code>otlphttp</code>, <code>debug</code>, <code>prometheus</code>, <code>kafka</code></p></td>
<td style="text-align: left;"><p>None</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>connectors:</code></pre></td>
<td style="text-align: left;"><p>Connectors join pairs of pipelines by consuming data as end-of-pipeline exporters and emitting data as start-of-pipeline receivers. Connectors can be used to summarize, replicate, or route consumed data.</p></td>
<td style="text-align: left;"><p><code>spanmetrics</code></p></td>
<td style="text-align: left;"><p>None</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>extensions:</code></pre></td>
<td style="text-align: left;"><p>Optional components for tasks that do not involve processing telemetry data.</p></td>
<td style="text-align: left;"><p><code>bearertokenauth</code>, <code>oauth2client</code>, <code>pprof</code>, <code>health_check</code>, <code>memory_ballast</code>, <code>zpages</code></p></td>
<td style="text-align: left;"><p>None</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>service:
  pipelines:</code></pre></td>
<td style="text-align: left;"><p>Components are enabled by adding them to a pipeline under <code>services.pipeline</code>.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>service:
  pipelines:
    traces:
      receivers:</code></pre></td>
<td style="text-align: left;"><p>You enable receivers for tracing by adding them under <code>service.pipelines.traces</code>.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>None</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>service:
  pipelines:
    traces:
      processors:</code></pre></td>
<td style="text-align: left;"><p>You enable processors for tracing by adding them under <code>service.pipelines.traces</code>.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>None</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>service:
  pipelines:
    traces:
      exporters:</code></pre></td>
<td style="text-align: left;"><p>You enable exporters for tracing by adding them under <code>service.pipelines.traces</code>.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>None</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>service:
  pipelines:
    metrics:
      receivers:</code></pre></td>
<td style="text-align: left;"><p>You enable receivers for metrics by adding them under <code>service.pipelines.metrics</code>.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>None</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>service:
  pipelines:
    metrics:
      processors:</code></pre></td>
<td style="text-align: left;"><p>You enable processors for metircs by adding them under <code>service.pipelines.metrics</code>.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>None</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>service:
  pipelines:
    metrics:
      exporters:</code></pre></td>
<td style="text-align: left;"><p>You enable exporters for metrics by adding them under <code>service.pipelines.metrics</code>.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>None</p></td>
</tr>
</tbody>
</table>

# Profile signal

<div wrapper="1" role="_abstract">

The Profile signal is an emerging telemetry data format for observing code execution and resource consumption.

</div>

> [!IMPORTANT]
> The Profile signal is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

The Profile signal allows you to pinpoint inefficient code down to specific functions. Such profiling allows you to precisely identify performance bottlenecks and resource inefficiencies down to the specific line of code. By correlating such high-fidelity profile data with traces, metrics, and logs, it enables comprehensive performance analysis and targeted code optimization in production environments.

Profiling can target an application or operating system:

- Using profiling to observe an application can help developers validate code performance, prevent regressions, and monitor resource consumption such as memory and CPU usage, and thus identify and improve inefficient code.

- Using profiling to observe operating systems can provide insights into the infrastructure, system calls, kernel operations, and I/O wait times, and thus help in optimizing infrastructure for efficiency and cost savings.

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled Profile signal

</div>

``` yaml
apiVersion: opentelemetry.io/v1beta1
kind: OpenTelemetryCollector
metadata:
name: otel-profiles-collector
  namespace: otel-profile
spec:
 args:
   feature-gates: service.profilesSupport
  config:
    receivers:
      otlp:
        protocols:
          grpc:
           endpoint: '0.0.0.0:4317'
          http:
           endpoint: '0.0.0.0:4318'
    exporters:
       otlp/pyroscope:
           endpoint: "pyroscope.pyroscope-monitoring.svc.cluster.local:4317"
    service:
      pipelines:
         profiles:
           receivers: [otlp]
           exporters: [otlp/pyroscope]
# ...
```

</div>

- Enables profiles by setting the `feature-gates` field as shown here.

- Configures the OTLP Receiver to set up the OpenTelemetry Collector to receive profile data via the OTLP.

- Configures where to export profiles to, such as a storage.

- Defines a profiling pipeline, including a configuration for forwarding the received profile data to an OTLP-compatible profiling back end such as Grafana Pyroscope.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [OpenTelemetry Profiles](https://opentelemetry.io/docs/specs/otel/profiles/)

- [Profiles attributes](https://opentelemetry.io/docs/specs/semconv/general/profiles/)

</div>

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

# Target Allocator

<div wrapper="1" role="_abstract">

The Target Allocator is an optional component of the OpenTelemetry Operator that shards scrape targets across the deployed fleet of OpenTelemetry Collector instances. The Target Allocator integrates with the Prometheus `PodMonitor` and `ServiceMonitor` custom resources (CR). When the Target Allocator is enabled, the OpenTelemetry Operator adds the `http_sd_config` field to the enabled `prometheus` receiver that connects to the Target Allocator service.

</div>

> [!IMPORTANT]
> The Target Allocator is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

Example OpenTelemetryCollector CR with the enabled Target Allocator

</div>

``` yaml
apiVersion: opentelemetry.io/v1beta1
kind: OpenTelemetryCollector
metadata:
  name: otel
  namespace: observability
spec:
  mode: statefulset
  targetAllocator:
    enabled: true
    serviceAccount:
    prometheusCR:
      enabled: true
      scrapeInterval: 10s
      serviceMonitorSelector:
        name: app1
      podMonitorSelector:
        name: app2
  config:
    receivers:
      prometheus:
        config:
          scrape_configs: []
    processors:
    exporters:
      debug: {}
    service:
      pipelines:
        metrics:
          receivers: [prometheus]
          processors: []
          exporters: [debug]
# ...
```

</div>

- When the Target Allocator is enabled, the deployment mode must be set to `statefulset`.

- Enables the Target Allocator. Defaults to `false`.

- The service account name of the Target Allocator deployment. The service account needs to have RBAC to get the `ServiceMonitor`, `PodMonitor` custom resources, and other objects from the cluster to properly set labels on scraped metrics. The default service name is `<collector_name>-targetallocator`.

- Enables integration with the Prometheus `PodMonitor` and `ServiceMonitor` custom resources.

- Label selector for the Prometheus `ServiceMonitor` custom resources. When left empty, enables all service monitors.

- Label selector for the Prometheus `PodMonitor` custom resources. When left empty, enables all pod monitors.

- Prometheus receiver with the minimal, empty `scrape_config: []` configuration option.

The Target Allocator deployment uses the Kubernetes API to get relevant objects from the cluster, so it requires a custom RBAC configuration.

<div class="formalpara">

<div class="title">

RBAC configuration for the Target Allocator service account

</div>

``` yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: otel-targetallocator
rules:
  - apiGroups: [""]
    resources:
      - services
      - pods
      - namespaces
    verbs: ["get", "list", "watch"]
  - apiGroups: ["monitoring.coreos.com"]
    resources:
      - servicemonitors
      - podmonitors
      - scrapeconfigs
      - probes
    verbs: ["get", "list", "watch"]
  - apiGroups: ["discovery.k8s.io"]
    resources:
      - endpointslices
    verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: otel-targetallocator
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: otel-targetallocator
subjects:
  - kind: ServiceAccount
    name: otel-targetallocator
    namespace: observability
# ...
```

</div>

- The name of the Target Allocator service account.

- The namespace of the Target Allocator service account.
