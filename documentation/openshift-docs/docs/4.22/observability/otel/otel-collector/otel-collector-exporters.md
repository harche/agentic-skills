<div wrapper="1" role="_abstract">

Exporters send data to one or more back ends or destinations. An exporter can be push or pull based. By default, no exporters are configured. One or more exporters must be configured. Exporters can support one or more data sources. Exporters might be used with their default settings, but many exporters require configuration to specify at least the destination and security settings.

</div>

Currently, the following General Availability and Technology Preview exporters are available for the Red Hat build of OpenTelemetry:

# OTLP Exporter

<div wrapper="1" role="_abstract">

The OTLP gRPC Exporter exports traces and metrics by using the OpenTelemetry protocol (OTLP).

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled OTLP Exporter

</div>

``` yaml
# ...
  config:
    exporters:
      otlp:
        endpoint: tempo-ingester:4317
        tls:
          ca_file: ca.pem
          cert_file: cert.pem
          key_file: key.pem
          insecure: false
          insecure_skip_verify: false #
          reload_interval: 1h
          server_name_override: <name>
        headers:
          X-Scope-OrgID: "dev"
    service:
      pipelines:
        traces:
          exporters: [otlp]
        metrics:
          exporters: [otlp]
# ...
```

</div>

- The OTLP gRPC endpoint. If the `https://` scheme is used, then client transport security is enabled and overrides the `insecure` setting in the `tls`.

- The client-side TLS configuration. Defines paths to TLS certificates.

- Disables client transport security when set to `true`. The default value is `false` by default.

- Skips verifying the certificate when set to `true`. The default value is `false`.

- Specifies the time interval at which the certificate is reloaded. If the value is not set, the certificate is never reloaded. The `reload_interval` accepts a string containing valid units of time such as `ns`, `us` or `µs`, `ms`, `s`, `m`, `h`.

- Overrides the virtual hostname of authority such as the authority header field in requests. You can use this for testing.

- Headers are sent for every request performed during an established connection.

# OTLP HTTP Exporter

<div wrapper="1" role="_abstract">

The OTLP HTTP Exporter exports traces and metrics by using the OpenTelemetry protocol (OTLP).

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled OTLP Exporter

</div>

``` yaml
# ...
  config:
    exporters:
      otlphttp:
        endpoint: http://tempo-ingester:4318
        tls:
        headers:
          X-Scope-OrgID: "dev"
        disable_keep_alives: false

    service:
      pipelines:
        traces:
          exporters: [otlphttp]
        metrics:
          exporters: [otlphttp]
# ...
```

</div>

- The OTLP HTTP endpoint. If the `https://` scheme is used, then client transport security is enabled and overrides the `insecure` setting in the `tls`.

- The client side TLS configuration. Defines paths to TLS certificates.

- Headers are sent in every HTTP request.

- If true, disables HTTP keep-alives. It will only use the connection to the server for a single HTTP request.

# Debug Exporter

<div wrapper="1" role="_abstract">

The Debug Exporter prints traces and metrics to the standard output.

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled Debug Exporter

</div>

``` yaml
# ...
  config:
    exporters:
      debug:
        verbosity: detailed
        sampling_initial: 5
        sampling_thereafter: 200
        use_internal_logger: true
    service:
      pipelines:
        traces:
          exporters: [debug]
        metrics:
          exporters: [debug]
# ...
```

</div>

- Verbosity of the debug export: `detailed`, `normal`, or `basic`. When set to `detailed`, pipeline data are verbosely logged. Defaults to `normal`.

- Initial number of messages logged per second. The default value is `2` messages per second.

- Sampling rate after the initial number of messages, the value in `sampling_initial`, has been logged. Disabled by default with the default `1` value. Sampling is enabled with values greater than `1`. For more information, see the page for the [sampler function in the `zapcore` package](https://pkg.go.dev/go.uber.org/zap/zapcore?utm_source=godoc#NewSamplerWithOptions) on the Go Project’s website.

- When set to `true`, enables output from the Collector’s internal logger for the exporter.

# Load Balancing Exporter

<div wrapper="1" role="_abstract">

The Load Balancing Exporter consistently exports spans, metrics, and logs according to the `routing_key` configuration.

</div>

> [!IMPORTANT]
> The Load Balancing Exporter is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled Load Balancing Exporter

</div>

``` yaml
# ...
  config:
    exporters:
      loadbalancing:
        routing_key: "service"
        protocol:
          otlp:
            timeout: 1s
        resolver:
          static:
            hostnames:
            - backend-1:4317
            - backend-2:4317
          dns:
            hostname: otelcol-headless.observability.svc.cluster.local
          k8s:
            service: lb-svc.kube-public
            ports:
              - 15317
              - 16317
# ...
```

</div>

- The `routing_key: service` exports spans for the same service name to the same Collector instance to provide accurate aggregation. The `routing_key: traceID` exports spans based on their `traceID`. The implicit default is `traceID` based routing.

- The OTLP is the only supported load balancing protocol. All options of the OTLP exporter are supported.

- You can configure only one resolver.

- The static resolver distributes the load across the listed endpoints.

- You can use the DNS resolver only with a Kubernetes headless service.

- The Kubernetes resolver is recommended.

# Prometheus Exporter

<div wrapper="1" role="_abstract">

The Prometheus Exporter exports metrics in the Prometheus or OpenMetrics formats.

</div>

> [!IMPORTANT]
> The Prometheus Exporter is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled Prometheus Exporter

</div>

``` yaml
# ...
  config:
    exporters:
      prometheus:
        endpoint: 0.0.0.0:8889
        tls:
          ca_file: ca.pem
          cert_file: cert.pem
          key_file: key.pem
        namespace: prefix
        const_labels:
          label1: value1
        enable_open_metrics: true
        resource_to_telemetry_conversion:
          enabled: true
        metric_expiration: 180m
        add_metric_suffixes: false
    service:
      pipelines:
        metrics:
          exporters: [prometheus]
# ...
```

</div>

- The network endpoint where the metrics are exposed. The Red Hat build of OpenTelemetry Operator automatically exposes the port specified in the `endpoint` field to the `<instance_name>-collector` service.

- The server-side TLS configuration. Defines paths to TLS certificates.

- If set, exports metrics under the provided value.

- Key-value pair labels that are applied for every exported metric.

- If `true`, metrics are exported by using the OpenMetrics format. Exemplars are only exported in the OpenMetrics format and only for histogram and monotonic sum metrics such as `counter`. Disabled by default.

- If `enabled` is `true`, all the resource attributes are converted to metric labels. Disabled by default.

- Defines how long metrics are exposed without updates. The default is `5m`.

- Adds the metrics types and units suffixes. Must be disabled if the monitor tab in the Jaeger console is enabled. The default is `true`.

> [!NOTE]
> When the `spec.observability.metrics.enableMetrics` field in the `OpenTelemetryCollector` custom resource (CR) is set to `true`, the `OpenTelemetryCollector` CR automatically creates a Prometheus `ServiceMonitor` or `PodMonitor` CR to enable Prometheus to scrape your metrics.

# Prometheus Remote Write Exporter

<div wrapper="1" role="_abstract">

The Prometheus Remote Write Exporter exports metrics to compatible back ends.

</div>

> [!IMPORTANT]
> The Prometheus Remote Write Exporter is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled Prometheus Remote Write Exporter

</div>

``` yaml
# ...
  config:
    exporters:
      prometheusremotewrite:
        endpoint: "https://my-prometheus:7900/api/v1/push"
        tls:
          ca_file: ca.pem
          cert_file: cert.pem
          key_file: key.pem
        target_info: true
        export_created_metric: true
        max_batch_size_bytes: 3000000
    service:
      pipelines:
        metrics:
          exporters: [prometheusremotewrite]
# ...
```

</div>

- Endpoint for sending the metrics.

- Server-side TLS configuration. Defines paths to TLS certificates.

- When set to `true`, creates a `target_info` metric for each resource metric.

- When set to `true`, exports a `_created` metric for the Summary, Histogram, and Monotonic Sum metric points.

- Maximum size of the batch of samples that is sent to the remote write endpoint. Exceeding this value results in batch splitting. The default value is `3000000`, which is approximately 2.861 megabytes.

> [!WARNING]
> - This exporter drops non-cumulative monotonic, histogram, and summary OTLP metrics.
>
> - You must enable the `--web.enable-remote-write-receiver` feature flag on the remote Prometheus instance. Without it, pushing the metrics to the instance using this exporter fails.

# Kafka Exporter

<div wrapper="1" role="_abstract">

The Kafka Exporter exports logs, metrics, and traces to Kafka. This exporter uses a synchronous producer that blocks and does not batch messages. You must use it with batch and queued retry processors for higher throughput and resiliency.

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled Kafka Exporter

</div>

``` yaml
# ...
  config:
    exporters:
      kafka:
        brokers: ["localhost:9092"]
        protocol_version: 2.0.0
        topic: otlp_spans
        auth:
          plain_text:
            username: example
            password: example
          tls:
            ca_file: ca.pem
            cert_file: cert.pem
            key_file: key.pem
            insecure: false
            server_name_override: kafka.example.corp
    service:
      pipelines:
        traces:
          exporters: [kafka]
# ...
```

</div>

- The list of Kafka brokers. The default is `localhost:9092`.

- The Kafka protocol version. For example, `2.0.0`. This is a required field.

- The name of the Kafka topic to read from. The following are the defaults: `otlp_spans` for traces, `otlp_metrics` for metrics, `otlp_logs` for logs.

- The plain text authentication configuration. If omitted, plain text authentication is disabled.

- The client-side TLS configuration. Defines paths to the TLS certificates. If omitted, TLS authentication is disabled.

- Disables verifying the server’s certificate chain and hostname. The default is `false`.

- ServerName indicates the name of the server requested by the client to support virtual hosting.

# AWS CloudWatch Logs Exporter

<div wrapper="1" role="_abstract">

The AWS CloudWatch Logs Exporter sends logs data to the Amazon CloudWatch Logs service and signs requests by using the AWS SDK for Go and the default credential provider chain.

</div>

> [!IMPORTANT]
> The AWS CloudWatch Logs Exporter is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled AWS CloudWatch Logs Exporter

</div>

``` yaml
# ...
  config:
    exporters:
      awscloudwatchlogs:
        log_group_name: "<group_name_of_amazon_cloudwatch_logs>"
        log_stream_name: "<log_stream_of_amazon_cloudwatch_logs>"
        region: <aws_region_of_log_stream>
        endpoint: <protocol><service_endpoint_of_amazon_cloudwatch_logs>
        log_retention: <supported_value_in_days>
        role_arn: "<iam_role>"
# ...
```

</div>

- Required. If the log group does not exist yet, it is automatically created.

- Required. If the log stream does not exist yet, it is automatically created.

- Optional. If the AWS region is not already set in the default credential chain, you must specify it.

- Optional. You can override the default Amazon CloudWatch Logs service endpoint to which the requests are forwarded. You must include the protocol, such as `https://`, as part of the endpoint value. For the list of service endpoints by region, see [Amazon CloudWatch Logs endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cwl_region.html) (AWS General Reference).

- Optional. With this parameter, you can set the log retention policy for new Amazon CloudWatch log groups. If this parameter is omitted or set to `0`, the logs never expire by default. Supported values for retention in days are `1`, `3`, `5`, `7`, `14`, `30`, `60`, `90`, `120`, `150`, `180`, `365`, `400`, `545`, `731`, `1827`, `2192`, `2557`, `2922`, `3288`, or `3653`.

- Optional. The AWS Identity and Access Management (IAM) role for uploading the log segments to a different account.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Amazon CloudWatch Logs User Guide: What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)

- [AWS SDK for Go Developer Guide: Specifying Credentials](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials)

- [AWS General Reference: Amazon CloudWatch Logs endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cwl_region.html)

</div>

# AWS EMF Exporter

<div wrapper="1" role="_abstract">

The AWS EMF Exporter converts the following OpenTelemetry metrics datapoints to the AWS CloudWatch Embedded Metric Format (EMF):

</div>

- `Int64DataPoints`

- `DoubleDataPoints`

- `SummaryDataPoints`

The EMF metrics are then sent directly to the Amazon CloudWatch Logs service by using the `PutLogEvents` API.

One of the benefits of using this exporter is the possibility to view logs and metrics in the Amazon CloudWatch console at <https://console.aws.amazon.com/cloudwatch/>.

> [!IMPORTANT]
> The AWS EMF Exporter is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled AWS EMF Exporter

</div>

``` yaml
# ...
  config:
    exporters:
      awsemf:
        log_group_name: "<group_name_of_amazon_cloudwatch_logs>"
        log_stream_name: "<log_stream_of_amazon_cloudwatch_logs>"
        resource_to_telemetry_conversion:
          enabled: true
        region: <region>
        endpoint: <protocol><endpoint>
        log_retention: <supported_value_in_days>
        namespace: <custom_namespace>
        role_arn: "<iam_role>"
# ...
```

</div>

- You can use the `log_group_name` parameter to customize the log group name or set the default `/metrics/default` value or the following placeholders:

  The `/aws/metrics/{ClusterName}` placeholder is for searching for the `ClusterName` or `aws.ecs.cluster.name` resource attribute in the metrics data and replacing it with the actual cluster name.

  The `{NodeName}` placeholder is for searching for the `NodeName` or `k8s.node.name` resource attribute.

  The `{TaskId}` placeholder is for searching for the `TaskId` or `aws.ecs.task.id` resource attribute.

  If no resource attribute is found in the resource attribute map, the placeholder is replaced by the `undefined` value.

- You can use the `log_stream_name` parameter to customize the log stream name or set the default `otel-stream` value or the following placeholders:

  The `{ClusterName}` placeholder is for searching for the `ClusterName` or `aws.ecs.cluster.name` resource attribute.

  The `{ContainerInstanceId}` placeholder is for searching for the `ContainerInstanceId` or `aws.ecs.container.instance.id` resource attribute. This resource attribute is valid only for the AWS ECS EC2 launch type.

  The `{NodeName}` placeholder is for searching for the `NodeName` or `k8s.node.name` resource attribute.

  The `{TaskDefinitionFamily}` placeholder is for searching for the `TaskDefinitionFamily` or `aws.ecs.task.family` resource attribute.

  The `{TaskId}` placeholder is for searching for the `TaskId` or `aws.ecs.task.id` resource attribute in the metrics data and replacing it with the actual task ID.

  If no resource attribute is found in the resource attribute map, the placeholder is replaced by the `undefined` value.

- Optional. Converts resource attributes to telemetry attributes such as metric labels. Disabled by default.

- The AWS region of the log stream. If a region is not already set in the default credential provider chain, you must specify the region.

- Optional. You can override the default Amazon CloudWatch Logs service endpoint to which the requests are forwarded. You must include the protocol, such as `https://`, as part of the endpoint value. For the list of service endpoints by region, see [Amazon CloudWatch Logs endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cwl_region.html) (AWS General Reference).

- Optional. With this parameter, you can set the log retention policy for new Amazon CloudWatch log groups. If this parameter is omitted or set to `0`, the logs never expire by default. Supported values for retention in days are `1`, `3`, `5`, `7`, `14`, `30`, `60`, `90`, `120`, `150`, `180`, `365`, `400`, `545`, `731`, `1827`, `2192`, `2557`, `2922`, `3288`, or `3653`.

- Optional. A custom namespace for the Amazon CloudWatch metrics.

- Optional. The AWS Identity and Access Management (IAM) role for uploading the metric segments to a different account.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Amazon CloudWatch User Guide: Specification: Embedded metric format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html)

- [Amazon CloudWatch Logs API Reference: PutLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html)

- [AWS General Reference: Amazon CloudWatch Logs endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cwl_region.html)

</div>

# AWS X-Ray Exporter

<div wrapper="1" role="_abstract">

The AWS X-Ray Exporter converts OpenTelemetry spans to AWS X-Ray Segment Documents and then sends them directly to the AWS X-Ray service. The AWS X-Ray Exporter uses the `PutTraceSegments` API and signs requests by using the AWS SDK for Go and the default credential provider chain.

</div>

> [!IMPORTANT]
> The AWS X-Ray Exporter is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled AWS X-Ray Exporter

</div>

``` yaml
# ...
  config:
    exporters:
      awsxray:
        region: "<region>"
        endpoint: <protocol><endpoint>
        resource_arn: "<aws_resource_arn>"
        role_arn: "<iam_role>"
        indexed_attributes: [ "<indexed_attr_0>", "<indexed_attr_1>" ]
        aws_log_groups: ["<group1>", "<group2>"]
        request_timeout_seconds: 120
# ...
```

</div>

- The destination region for the X-Ray segments sent to the AWS X-Ray service. For example, `eu-west-1`.

- Optional. You can override the default Amazon CloudWatch Logs service endpoint to which the requests are forwarded. You must include the protocol, such as `https://`, as part of the endpoint value. For the list of service endpoints by region, see [Amazon CloudWatch Logs endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cwl_region.html) (AWS General Reference).

- The Amazon Resource Name (ARN) of the AWS resource that is running the Collector.

- The AWS Identity and Access Management (IAM) role for uploading the X-Ray segments to a different account.

- The list of attribute names to be converted to X-Ray annotations.

- The list of log group names for Amazon CloudWatch Logs.

- Time duration in seconds before timing out a request. If omitted, the default value is `30`.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [AWS X-Ray Developer Guide: What is AWS X-Ray?](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)

- [AWS Documentation: AWS SDK for Go API Reference](https://docs.aws.amazon.com/sdk-for-go/api/index.html)

- [AWS SDK for Go Developer Guide: Specifying Credentials](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials)

- [AWS Identity and Access Management User Guide: IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

</div>

# File Exporter

<div wrapper="1" role="_abstract">

The File Exporter writes telemetry data to files in persistent storage and supports file operations such as rotation, compression, and writing to multiple files. With this exporter, you can also use a resource attribute to control file naming. The only required setting is `path`, which specifies the destination path for telemetry files in the persistent-volume file system.

</div>

> [!IMPORTANT]
> The File Exporter is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled File Exporter

</div>

``` yaml
# ...
  config: |
    exporters:
      file:
        path: /data/metrics.json
        rotation:
          max_megabytes: 10
          max_days: 3
          max_backups: 3
          localtime: true
        format: proto
        compression: zstd
        flush_interval: 5
# ...
```

</div>

- The file-system path where the data is to be written. There is no default.

- File rotation is an optional feature of this exporter. By default, telemetry data is exported to a single file. Add the `rotation` setting to enable file rotation.

- The `max_megabytes` setting is the maximum size a file is allowed to reach until it is rotated. The default is `100`.

- The `max_days` setting is for how many days a file is to be retained, counting from the timestamp in the file name. There is no default.

- The `max_backups` setting is for retaining several older files. The default is `100`.

- The `localtime` setting specifies the local-time format for the timestamp, which is appended to the file name in front of any extension, when the file is rotated. The default is the Coordinated Universal Time (UTC).

- The format for encoding the telemetry data before writing it to a file. The default format is `json`. The `proto` format is also supported.

- File compression is optional and not set by default. This setting defines the compression algorithm for the data that is exported to a file. Currently, only the `zstd` compression algorithm is supported. There is no default.

- The time interval between flushes. A value without a unit is set in nanoseconds. This setting is ignored when file rotation is enabled through the `rotation` settings.

# Google Cloud Exporter

<div wrapper="1" role="_abstract">

The Google Cloud Exporter sends telemetry data to Google Cloud Operations Suite. Using the Google Cloud Exporter, you can export metrics to Google Cloud Monitoring, logs to Google Cloud Logging, and traces to Google Cloud Trace.

</div>

> [!IMPORTANT]
> The Google Cloud Exporter is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled Google Cloud Exporter

</div>

``` yaml
# ...
  env:
    - name: GOOGLE_APPLICATION_CREDENTIALS
      value: /var/secrets/google/key.json
  volumeMounts:
    - name: google-application-credentials
      mountPath: /var/secrets/google
      readOnly: true
  volumes:
    - name: google-application-credentials
      secret:
        secretName: google-application-credentials
  config:
    exporters:
      googlecloud:
        project:
# ...
```

</div>

- The `GOOGLE_APPLICATION_CREDENTIALS` environment variable that points to the authentication `key.json` file. The `key.json` file is mounted as a secret volume to the OpenTelemetry Collector.

- Optional. The project identifier. If not specified, the project is automatically determined from the credentials.

  By default, the exporter sends telemetry data to the project specified in the `project` field of the exporter’s configuration. You can have an override set up on a per-metric basis by using the `gcp.project.id` resource attribute. For example, if a metric has a label project, you can use the Group-by-Attributes Processor to promote it to a resource label, and then use the Resource Processor to rename the attribute from `project` to `gcp.project.id`.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Google Cloud Monitoring](https://cloud.google.com/monitoring)

- [Google Cloud Logging](https://cloud.google.com/logging)

- [Google Cloud Trace](https://cloud.google.com/trace)

- [Google Cloud Guides: Configure Workload Identity Federation with Kubernetes](https://cloud.google.com/iam/docs/workload-identity-federation-with-kubernetes#deploy)

</div>

# Additional resources

- [OpenTelemetry Documentation: OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/)
