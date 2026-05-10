You can use the OpenTelemetry Collector to forward your telemetry data.

# Forwarding traces to a TempoStack instance

To configure forwarding traces to a TempoStack instance, you can deploy and configure the OpenTelemetry Collector. You can deploy the OpenTelemetry Collector in the deployment mode by using the specified processors, receivers, and exporters. For other modes, see the OpenTelemetry Collector documentation linked in *Additional resources*.

<div>

<div class="title">

Prerequisites

</div>

- The Red Hat build of OpenTelemetry Operator is installed.

- The Tempo Operator is installed.

- A TempoStack instance is deployed on the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a service account for the OpenTelemetry Collector.

    <div class="formalpara">

    <div class="title">

    Example ServiceAccount

    </div>

    ``` yaml
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: otel-collector-deployment
    ```

    </div>

2.  Create a cluster role for the service account.

    <div class="formalpara">

    <div class="title">

    Example ClusterRole

    </div>

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: otel-collector
    rules:
    - apiGroups: [""]
      resources: ["pods", "namespaces",]
      verbs: ["get", "watch", "list"]
    - apiGroups: ["apps"]
      resources: ["replicasets"]
      verbs: ["get", "watch", "list"]
    - apiGroups: ["config.openshift.io"]
      resources: ["infrastructures", "infrastructures/status"]
      verbs: ["get", "watch", "list"]
    ```

    </div>

    - This example uses the Kubernetes Attributes Processor, which requires these permissions for the `pods` and `namespaces` resources.

    - Also due to the Kubernetes Attributes Processor, these permissions are required for the `replicasets` resources.

    - This example also uses the Resource Detection Processor, which requires these permissions for the `infrastructures` and `status` resources.

3.  Bind the cluster role to the service account.

    <div class="formalpara">

    <div class="title">

    Example ClusterRoleBinding

    </div>

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: otel-collector
    subjects:
    - kind: ServiceAccount
      name: otel-collector-deployment
      namespace: otel-collector-example
    roleRef:
      kind: ClusterRole
      name: otel-collector
      apiGroup: rbac.authorization.k8s.io
    ```

    </div>

4.  Create the YAML file to define the `OpenTelemetryCollector` custom resource (CR).

    <div class="formalpara">

    <div class="title">

    Example OpenTelemetryCollector

    </div>

    ``` yaml
    apiVersion: opentelemetry.io/v1beta1
    kind: OpenTelemetryCollector
    metadata:
      name: otel
    spec:
      mode: deployment
      serviceAccount: otel-collector-deployment
      config:
        receivers:
          jaeger:
            protocols:
              grpc: {}
              thrift_binary: {}
              thrift_compact: {}
              thrift_http: {}
          opencensus: {}
          otlp:
            protocols:
              grpc: {}
              http: {}
          zipkin: {}
        processors:
          batch: {}
          k8sattributes: {}
          memory_limiter:
            check_interval: 1s
            limit_percentage: 50
            spike_limit_percentage: 30
          resourcedetection:
            detectors: [openshift]
        exporters:
          otlp:
            endpoint: "tempo-simplest-distributor:4317"
            tls:
              insecure: true
        service:
          pipelines:
            traces:
              receivers: [jaeger, opencensus, otlp, zipkin]
              processors: [memory_limiter, k8sattributes, resourcedetection, batch]
              exporters: [otlp]
    ```

    </div>

    - The Collector exporter is configured to export OTLP and points to the Tempo distributor endpoint, `"tempo-simplest-distributor:4317"` in this example, which is already created.

    - The Collector is configured with a receiver for Jaeger traces, OpenCensus traces over the OpenCensus protocol, Zipkin traces over the Zipkin protocol, and OTLP traces over the gRPC protocol.

</div>

> [!TIP]
> You can deploy `telemetrygen` as a test:
>
> ``` yaml
> apiVersion: batch/v1
> kind: Job
> metadata:
>   name: telemetrygen
> spec:
>   template:
>     spec:
>       containers:
>         - name: telemetrygen
>           image: ghcr.io/open-telemetry/opentelemetry-collector-contrib/telemetrygen:latest
>           args:
>             - traces
>             - --otlp-endpoint=otel-collector:4317
>             - --otlp-insecure
>             - --duration=30s
>             - --workers=1
>       restartPolicy: Never
>   backoffLimit: 4
> ```

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) (OpenTelemetry Documentation)

- [Deployment examples on GitHub](https://github.com/os-observability/redhat-rhosdt-samples) (GitHub)

</div>

# Forwarding logs to a LokiStack instance

You can deploy the OpenTelemetry Collector to forward logs to a `LokiStack` instance by using the `openshift-logging` tenants mode.

<div>

<div class="title">

Prerequisites

</div>

- The Red Hat build of OpenTelemetry Operator is installed.

- The Loki Operator is installed.

- A supported `LokiStack` instance is deployed on the cluster. For more information about the supported `LokiStack` configuration, see *Logging*.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a service account for the OpenTelemetry Collector.

    <div class="formalpara">

    <div class="title">

    Example `ServiceAccount` object

    </div>

    ``` yaml
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: otel-collector-deployment
      namespace: openshift-logging
    ```

    </div>

2.  Create a cluster role that grants the Collector’s service account the permissions to push logs to the `LokiStack` application tenant.

    <div class="formalpara">

    <div class="title">

    Example `ClusterRole` object

    </div>

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: otel-collector-logs-writer
    rules:
     - apiGroups: ["loki.grafana.com"]
       resourceNames: ["logs"]
       resources: ["application"]
       verbs: ["create"]
     - apiGroups: [""]
       resources: ["pods", "namespaces", "nodes"]
       verbs: ["get", "watch", "list"]
     - apiGroups: ["apps"]
       resources: ["replicasets"]
       verbs: ["get", "list", "watch"]
     - apiGroups: ["extensions"]
       resources: ["replicasets"]
       verbs: ["get", "list", "watch"]
    ```

    </div>

3.  Bind the cluster role to the service account.

    <div class="formalpara">

    <div class="title">

    Example `ClusterRoleBinding` object

    </div>

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: otel-collector-logs-writer
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: otel-collector-logs-writer
    subjects:
      - kind: ServiceAccount
        name: otel-collector-deployment
        namespace: openshift-logging
    ```

    </div>

4.  Create an `OpenTelemetryCollector` custom resource (CR) object.

    <div class="formalpara">

    <div class="title">

    Example `OpenTelemetryCollector` CR object

    </div>

    ``` yaml
    apiVersion: opentelemetry.io/v1beta1
    kind: OpenTelemetryCollector
    metadata:
      name: otel
      namespace: openshift-logging
    spec:
      serviceAccount: otel-collector-deployment
      config:
        extensions:
          bearertokenauth:
            filename: "/var/run/secrets/kubernetes.io/serviceaccount/token"
        receivers:
          otlp:
            protocols:
              grpc: {}
              http: {}
        processors:
          k8sattributes: {}
          resource:
            attributes:
              - key:  kubernetes.namespace_name
                from_attribute: k8s.namespace.name
                action: upsert
              - key:  kubernetes.pod_name
                from_attribute: k8s.pod.name
                action: upsert
              - key: kubernetes.container_name
                from_attribute: k8s.container.name
                action: upsert
              - key: log_type
                value: application
                action: upsert
          transform:
            log_statements:
              - context: log
                statements:
                  - set(attributes["level"], ConvertCase(severity_text, "lower"))
        exporters:
          otlphttp:
            endpoint: https://logging-loki-gateway-http.openshift-logging.svc.cluster.local:8080/api/logs/v1/application/otlp
            encoding: json
            tls:
              ca_file: "/var/run/secrets/kubernetes.io/serviceaccount/service-ca.crt"
            auth:
              authenticator: bearertokenauth
          debug:
            verbosity: detailed
        service:
          extensions: [bearertokenauth]
          pipelines:
            logs:
              receivers: [otlp]
              processors: [k8sattributes, transform, resource]
              exporters: [otlphttp]
            logs/test:
              receivers: [otlp]
              processors: []
              exporters: [debug]
    ```

    </div>

    - Provides the following resource attributes to be used by the web console: `kubernetes.namespace_name`, `kubernetes.pod_name`, `kubernetes.container_name`, and `log_type`.

    - Enables the BearerTokenAuth Extension that is required by the OTLP HTTP Exporter.

    - Enables the OTLP HTTP Exporter to export logs from the Collector.

</div>

> [!TIP]
> You can deploy `telemetrygen` as a test:
>
> ``` yaml
> apiVersion: batch/v1
> kind: Job
> metadata:
>   name: telemetrygen
> spec:
>   template:
>     spec:
>       containers:
>         - name: telemetrygen
>           image: ghcr.io/open-telemetry/opentelemetry-collector-contrib/telemetrygen:v0.106.1
>           args:
>             - logs
>             - --otlp-endpoint=otel-collector.openshift-logging.svc.cluster.local:4317
>             - --otlp-insecure
>             - --duration=180s
>             - --workers=1
>             - --logs=10
>             - --otlp-attributes=k8s.container.name="telemetrygen"
>       restartPolicy: Never
>   backoffLimit: 4
> ```

# Forwarding telemetry data to third-party systems

The OpenTelemetry Collector exports telemetry data by using the OTLP exporter via the OpenTelemetry Protocol (OTLP) that is implemented over the gRPC or HTTP transports. If you need to forward telemetry data to your third-party system and it does not support the OTLP or other supported protocol in the Red Hat build of OpenTelemetry, then you can deploy an unsupported custom OpenTelemetry Collector that can receive telemetry data via the OTLP and export it to your third-party system by using a custom exporter.

> [!WARNING]
> Red Hat does not support custom deployments.

<div>

<div class="title">

Prerequisites

</div>

- You have developed your own unsupported custom exporter that can export telemetry data via the OTLP to your third-party system.

</div>

<div>

<div class="title">

Procedure

</div>

- Deploy a custom Collector either through the OperatorHub or manually:

  - If your third-party system supports it, deploy the custom Collector by using the OperatorHub.

  - Deploy the custom Collector manually by using a config map, deployment, and service.

    <div class="formalpara">

    <div class="title">

    Example of a custom Collector deployment

    </div>

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: custom-otel-collector-config
    data:
      otel-collector-config.yaml: |
        receivers:
          otlp:
            protocols:
              grpc:
        exporters:
          debug: {}
          prometheus:
        service:
          pipelines:
            traces:
              receivers: [otlp]
              exporters: [debug]
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: custom-otel-collector-deployment
    spec:
      replicas: 1
      selector:
        matchLabels:
          component: otel-collector
      template:
        metadata:
          labels:
            component: otel-collector
        spec:
          containers:
          - name: opentelemetry-collector
            image: ghcr.io/open-telemetry/opentelemetry-collector-releases/opentelemetry-collector-contrib:latest
            command:
            - "/otelcol-contrib"
            - "--config=/conf/otel-collector-config.yaml"
            ports:
            - name: otlp
              containerPort: 4317
              protocol: TCP
            volumeMounts:
            - name: otel-collector-config-vol
              mountPath: /conf
              readOnly: true
          volumes:
          - name: otel-collector-config-vol
            configMap:
              name: custom-otel-collector-config
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: custom-otel-collector-service
      labels:
        component: otel-collector
    spec:
      type: ClusterIP
      ports:
      - name: otlp-grpc
        port: 4317
        targetPort: 4317
      selector:
        component: otel-collector
    ```

    </div>

    - Replace `debug` with the required exporter for your third-party system.

    - Replace the image with the required version of the OpenTelemetry Collector that has the required exporter for your third-party system.

    - The service name is used in the Red Hat build of OpenTelemetry Collector CR to configure the OTLP exporter.

</div>

# Forwarding telemetry data to AWS

<div wrapper="1" role="_abstract">

To forward telemetry data to AWS, use the OpenTelemetry Collector with the following exporters: AWS CloudWatch Logs Exporter for logs, AWS EMF Exporter for metrics, and AWS X-Ray Exporter for traces.

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Exporters](../../observability/otel/otel-collector/otel-collector-exporters.xml#otel-collector-exporters)

</div>

# Forwarding telemetry data to Google Cloud

<div wrapper="1" role="_abstract">

To forward telemetry data to Google Cloud Operations Suite, use the OpenTelemetry Collector with the Google Cloud Exporter. The exporter sends metrics to Google Cloud Monitoring, logs to Google Cloud Logging, and traces to Google Cloud Trace.

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Exporters](../../observability/otel/otel-collector/otel-collector-exporters.xml#otel-collector-exporters)

</div>

# Additional resources

- [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/)
