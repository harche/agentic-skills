<div wrapper="1" role="_abstract">

Extensions add capabilities to the Collector. For example, authentication can be added to the receivers and exporters automatically.

</div>

Currently, the following General Availability and Technology Preview extensions are available for the Red Hat build of OpenTelemetry:

# BearerTokenAuth Extension

<div wrapper="1" role="_abstract">

The BearerTokenAuth Extension is an authenticator for receivers and exporters that are based on the HTTP and the gRPC protocol. You can use the OpenTelemetry Collector custom resource to configure client authentication and server authentication for the BearerTokenAuth Extension on the receiver and exporter side. This extension supports traces, metrics, and logs.

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with client and server authentication configured for the BearerTokenAuth Extension

</div>

``` yaml
# ...
  config:
    extensions:
      bearertokenauth:
        scheme: "Bearer"
        token: "<token>"
        filename: "<token_file>"

    receivers:
      otlp:
        protocols:
          http:
            auth:
              authenticator: bearertokenauth
    exporters:
      otlp:
        auth:
          authenticator: bearertokenauth

    service:
      extensions: [bearertokenauth]
      pipelines:
        traces:
          receivers: [otlp]
          exporters: [otlp]
# ...
```

</div>

- You can configure the BearerTokenAuth Extension to send a custom `scheme`. The default is `Bearer`.

- You can add the BearerTokenAuth Extension token as metadata to identify a message.

- Path to a file that contains an authorization token that is transmitted with every message.

- You can assign the authenticator configuration to an OTLP Receiver.

- You can assign the authenticator configuration to an OTLP Exporter.

# OAuth2Client Extension

<div wrapper="1" role="_abstract">

The OAuth2Client Extension is an authenticator for exporters that are based on the HTTP and the gRPC protocol. Client authentication for the OAuth2Client Extension is configured in a separate section in the OpenTelemetry Collector custom resource. This extension supports traces, metrics, and logs.

</div>

> [!IMPORTANT]
> The OAuth2Client Extension is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with client authentication configured for the OAuth2Client Extension

</div>

``` yaml
# ...
  config:
    extensions:
      oauth2client:
        client_id: <client_id>
        client_secret: <client_secret>
        endpoint_params:
          audience: <audience>
        token_url: https://example.com/oauth2/default/v1/token
        scopes: ["api.metrics"]
        # tls settings for the token client
        tls:
          insecure: true
          ca_file: /var/lib/mycert.pem
          cert_file: <cert_file>
          key_file: <key_file>
        timeout: 2s

    receivers:
      otlp:
        protocols:
          http: {}

    exporters:
      otlp:
        auth:
          authenticator: oauth2client

    service:
      extensions: [oauth2client]
      pipelines:
        traces:
          receivers: [otlp]
          exporters: [otlp]
# ...
```

</div>

- Client identifier, which is provided by the identity provider.

- Confidential key used to authenticate the client to the identity provider.

- Further metadata, in the key-value pair format, which is transferred during authentication. For example, `audience` specifies the intended audience for the access token, indicating the recipient of the token.

- The URL of the OAuth2 token endpoint, where the Collector requests access tokens.

- The scopes define the specific permissions or access levels requested by the client.

- The Transport Layer Security (TLS) settings for the token client, which is used to establish a secure connection when requesting tokens.

- When set to `true`, configures the Collector to use an insecure or non-verified TLS connection to call the configured token endpoint.

- The path to a Certificate Authority (CA) file that is used to verify the server’s certificate during the TLS handshake.

- The path to the client certificate file that the client must use to authenticate itself to the OAuth2 server if required.

- The path to the client’s private key file that is used with the client certificate if needed for authentication.

- Sets a timeout for the token client’s request.

- You can assign the authenticator configuration to an OTLP exporter.

# File Storage Extension

<div wrapper="1" role="_abstract">

The File Storage Extension supports traces, metrics, and logs. This extension can persist the state to the local file system. This extension persists the sending queue for the OpenTelemetry Protocol (OTLP) exporters that are based on the HTTP and the gRPC protocols. This extension requires the read and write access to a directory. This extension can use a default directory, but the default directory must already exist.

</div>

> [!IMPORTANT]
> The File Storage Extension is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with a configured File Storage Extension that persists an OTLP sending queue

</div>

``` yaml
# ...
  config:
    extensions:
      file_storage/all_settings:
        directory: /var/lib/otelcol/mydir
        timeout: 1s
        compaction:
          on_start: true
          directory: /tmp/
          max_transaction_size: 65_536
        fsync: false

    exporters:
      otlp:
        sending_queue:
          storage: file_storage/all_settings

    service:
      extensions: [file_storage/all_settings]
      pipelines:
        traces:
          receivers: [otlp]
          exporters: [otlp]
# ...
```

</div>

- Specifies the directory in which the telemetry data is stored.

- Specifies the timeout time interval for opening the stored files.

- Starts compaction when the Collector starts. If omitted, the default is `false`.

- Specifies the directory in which the compactor stores the telemetry data.

- Defines the maximum size of the compaction transaction. To ignore the transaction size, set to zero. If omitted, the default is `65536` bytes.

- When set, forces the database to perform an `fsync` call after each write operation. This helps to ensure database integrity if there is an interruption to the database process, but at the cost of performance.

- Buffers the OTLP Exporter data on the local file system.

- Starts the File Storage Extension by the Collector.

# OIDC Auth Extension

<div wrapper="1" role="_abstract">

The OIDC Auth Extension authenticates incoming requests to receivers by using the OpenID Connect (OIDC) protocol. It validates the ID token in the authorization header against the issuer and updates the authentication context of the incoming request.

</div>

> [!IMPORTANT]
> The OIDC Auth Extension is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the configured OIDC Auth Extension

</div>

``` yaml
# ...
  config:
    extensions:
      oidc:
        attribute: authorization
        issuer_url: https://example.com/auth/realms/opentelemetry
        issuer_ca_path: /var/run/tls/issuer.pem
        audience: otel-collector
        username_claim: email
    receivers:
      otlp:
        protocols:
          grpc:
            auth:
              authenticator: oidc
    exporters:
      debug: {}
    service:
      extensions: [oidc]
      pipelines:
        traces:
          receivers: [otlp]
          exporters: [debug]
# ...
```

</div>

- The name of the header that contains the ID token. The default name is `authorization`.

- The base URL of the OIDC provider.

- Optional: The path to the issuer’s CA certificate.

- The audience for the token.

- The name of the claim that contains the username. The default name is `sub`.

# Jaeger Remote Sampling Extension

<div wrapper="1" role="_abstract">

The Jaeger Remote Sampling Extension enables serving sampling strategies after Jaeger’s remote sampling API. You can configure this extension to proxy requests to a backing remote sampling server such as a Jaeger collector down the pipeline or to a static JSON file from the local file system.

</div>

> [!IMPORTANT]
> The Jaeger Remote Sampling Extension is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with a configured Jaeger Remote Sampling Extension

</div>

``` yaml
# ...
  config:
    extensions:
      jaegerremotesampling:
        source:
          reload_interval: 30s
          remote:
            endpoint: jaeger-collector:14250
          file: /etc/otelcol/sampling_strategies.json

    receivers:
      otlp:
        protocols:
          http: {}

    exporters:
      debug: {}

    service:
      extensions: [jaegerremotesampling]
      pipelines:
        traces:
          receivers: [otlp]
          exporters: [debug]
# ...
```

</div>

- The time interval at which the sampling configuration is updated.

- The endpoint for reaching the Jaeger remote sampling strategy provider.

- The path to a local file that contains a sampling strategy configuration in the JSON format.

<div class="formalpara">

<div class="title">

Example of a Jaeger Remote Sampling strategy file

</div>

``` json
{
  "service_strategies": [
    {
      "service": "foo",
      "type": "probabilistic",
      "param": 0.8,
      "operation_strategies": [
        {
          "operation": "op1",
          "type": "probabilistic",
          "param": 0.2
        },
        {
          "operation": "op2",
          "type": "probabilistic",
          "param": 0.4
        }
      ]
    },
    {
      "service": "bar",
      "type": "ratelimiting",
      "param": 5
    }
  ],
  "default_strategy": {
    "type": "probabilistic",
    "param": 0.5,
    "operation_strategies": [
      {
        "operation": "/health",
        "type": "probabilistic",
        "param": 0.0
      },
      {
        "operation": "/metrics",
        "type": "probabilistic",
        "param": 0.0
      }
    ]
  }
}
```

</div>

# Performance Profiler Extension

<div wrapper="1" role="_abstract">

The Performance Profiler Extension enables the Go `net/http/pprof` endpoint. Developers use this extension to collect performance profiles and investigate issues with the service.

</div>

> [!IMPORTANT]
> The Performance Profiler Extension is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the configured Performance Profiler Extension

</div>

``` yaml
# ...
  config:
    extensions:
      pprof:
        endpoint: localhost:1777
        block_profile_fraction: 0
        mutex_profile_fraction: 0
        save_to_file: test.pprof

    receivers:
      otlp:
        protocols:
          http: {}

    exporters:
      debug: {}

    service:
      extensions: [pprof]
      pipelines:
        traces:
          receivers: [otlp]
          exporters: [debug]
# ...
```

</div>

- The endpoint at which this extension listens. Use `localhost:` to make it available only locally or `":"` to make it available on all network interfaces. The default value is `localhost:1777`.

- Sets a fraction of blocking events to be profiled. To disable profiling, set this to `0` or a negative integer. See the [documentation](https://golang.org/pkg/runtime/#SetBlockProfileRate) for the `runtime` package. The default value is `0`.

- Set a fraction of mutex contention events to be profiled. To disable profiling, set this to `0` or a negative integer. See the [documentation](https://golang.org/pkg/runtime/#SetMutexProfileFraction) for the `runtime` package. The default value is `0`.

- The name of the file in which the CPU profile is to be saved. Profiling starts when the Collector starts. Profiling is saved to the file when the Collector is terminated.

# Health Check Extension

<div wrapper="1" role="_abstract">

The Health Check Extension provides an HTTP URL for checking the status of the OpenTelemetry Collector. You can use this extension as a liveness and readiness probe on OpenShift.

</div>

> [!IMPORTANT]
> The Health Check Extension is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the configured Health Check Extension

</div>

``` yaml
# ...
  config:
    extensions:
      health_check:
        endpoint: "0.0.0.0:13133"
        tls:
          ca_file: "/path/to/ca.crt"
          cert_file: "/path/to/cert.crt"
          key_file: "/path/to/key.key"
        path: "/health/status"
        check_collector_pipeline:
          enabled: true
          interval: "5m"
          exporter_failure_threshold: 5

    receivers:
      otlp:
        protocols:
          http: {}

    exporters:
      debug: {}

    service:
      extensions: [health_check]
      pipelines:
        traces:
          receivers: [otlp]
          exporters: [debug]
# ...
```

</div>

- The target IP address for publishing the health check status. The default is `0.0.0.0:13133`.

- The TLS server-side configuration. Defines paths to TLS certificates. If omitted, the TLS is disabled.

- The path for the health check server. The default is `/`.

- Settings for the Collector pipeline health check.

- Enables the Collector pipeline health check. The default is `false`.

- The time interval for checking the number of failures. The default is `5m`.

- The threshold of multiple failures until which a container is still marked as healthy. The default is `5`.

# zPages Extension

<div wrapper="1" role="_abstract">

The zPages Extension provides an HTTP endpoint that serves live data for debugging instrumented components in real time. You can use this extension for in-process diagnostics and insights into traces and metrics without relying on an external backend. With this extension, you can monitor and troubleshoot the behavior of the OpenTelemetry Collector and related components by watching the diagnostic information at the provided endpoint.

</div>

> [!IMPORTANT]
> The zPages Extension is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the configured zPages Extension

</div>

``` yaml
# ...
  config:
    extensions:
      zpages:
        endpoint: "localhost:55679"

    receivers:
      otlp:
        protocols:
          http: {}
    exporters:
      debug: {}

    service:
      extensions: [zpages]
      pipelines:
        traces:
          receivers: [otlp]
          exporters: [debug]
# ...
```

</div>

- Specifies the HTTP endpoint for serving the zPages extension. The default is `localhost:55679`.

> [!IMPORTANT]
> Accessing the HTTP endpoint requires port-forwarding because the Red Hat build of OpenTelemetry Operator does not expose this route.
>
> You can enable port-forwarding by running the following `oc` command:
>
> ``` terminal
> $ oc port-forward pod/$(oc get pod -l app.kubernetes.io/name=instance-collector -o=jsonpath='{.items[0].metadata.name}') 55679
> ```

The Collector provides the following zPages for diagnostics:

**ServiceZ**
Shows an overview of the Collector services and links to the following zPages: **PipelineZ**, **ExtensionZ**, and **FeatureZ**. This page also displays information about the build version and runtime. An example of this page’s URL is `http://localhost:55679/debug/servicez`.

**PipelineZ**
Shows detailed information about the active pipelines in the Collector. This page displays the pipeline type, whether data are modified, and the associated receivers, processors, and exporters for each pipeline. An example of this page’s URL is `http://localhost:55679/debug/pipelinez`.

**ExtensionZ**
Shows the currently active extensions in the Collector. An example of this page’s URL is `http://localhost:55679/debug/extensionz`.

**FeatureZ**
Shows the feature gates enabled in the Collector along with their status and description. An example of this page’s URL is `http://localhost:55679/debug/featurez`.

**TraceZ**
Shows spans categorized by latency. Available time ranges include 0 µs, 10 µs, 100 µs, 1 ms, 10 ms, 100 ms, 1 s, 10 s, 1 m. This page also allows for quick inspection of error samples. An example of this page’s URL is `http://localhost:55679/debug/tracez`.

# Additional resources

- [OpenTelemetry Documentation: OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/)
