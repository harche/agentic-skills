The Red Hat build of OpenTelemetry Operator uses an `Instrumentation` custom resource that defines the configuration of the instrumentation.

# Auto-instrumentation in the Red Hat build of OpenTelemetry Operator

Auto-instrumentation in the Red Hat build of OpenTelemetry Operator can automatically instrument an application without manual code changes. Developers and administrators can monitor applications with minimal effort and changes to the existing codebase.

Auto-instrumentation runs as follows:

1.  The Red Hat build of OpenTelemetry Operator injects an init-container, or a sidecar container for Go, to add the instrumentation libraries for the programming language of the instrumented application.

2.  The Red Hat build of OpenTelemetry Operator sets the required environment variables in the application’s runtime environment. These variables configure the auto-instrumentation libraries to collect traces, metrics, and logs and send them to the appropriate OpenTelemetry Collector or another telemetry backend.

3.  The injected libraries automatically instrument your application by connecting to known frameworks and libraries, such as web servers or database clients, to collect telemetry data. The source code of the instrumented application is not modified.

4.  Once the application is running with the injected instrumentation, the application automatically generates telemetry data, which is sent to a designated OpenTelemetry Collector or an external OTLP endpoint for further processing.

Auto-instrumentation enables you to start collecting telemetry data quickly without having to manually integrate the OpenTelemetry SDK into your application code. However, some applications might require specific configurations or custom manual instrumentation.

# OpenTelemetry instrumentation configuration options

The Red Hat build of OpenTelemetry injects and configures the OpenTelemetry auto-instrumentation libraries into your workloads. Currently, the Red Hat build of OpenTelemetry supports injecting instrumentation libraries for Go, Java, Node.js, Python, .NET, and the Apache HTTP Server (`httpd`).

> [!IMPORTANT]
> The Red Hat build of OpenTelemetry Operator only supports the injection mechanism of the instrumentation libraries but does not support instrumentation libraries or upstream images. Customers can build their own instrumentation images or use community images.

## Instrumentation options

Instrumentation options are specified in an `Instrumentation` custom resource (CR).

<div class="formalpara">

<div class="title">

Sample `Instrumentation` CR

</div>

``` yaml
apiVersion: opentelemetry.io/v1alpha1
kind: Instrumentation
metadata:
  name: instrumentation
spec:
  env:
    - name: OTEL_EXPORTER_OTLP_TIMEOUT
      value: "20"
  exporter:
    endpoint: http://production-collector.observability.svc.cluster.local:4317
  propagators:
    - tracecontext
    - baggage
  sampler:
    type: parentbased_traceidratio
    argument: "1"
  python:
    env:
      - name: OTEL_EXPORTER_OTLP_ENDPOINT
        value: http://production-collector.observability.svc.cluster.local:4318
  dotnet:
    env:
      - name: OTEL_EXPORTER_OTLP_ENDPOINT
        value: http://production-collector.observability.svc.cluster.local:4318
  go:
    env:
      - name: OTEL_EXPORTER_OTLP_ENDPOINT
        value: http://production-collector.observability.svc.cluster.local:4318
```

</div>

- Python auto-instrumentation uses protocol buffers over HTTP (HTTP/proto or HTTP/protobuf) by default.

- Required if endpoint is set to `:4317`.

- .NET auto-instrumentation uses protocol buffers over HTTP (HTTP/proto or HTTP/protobuf) by default.

- Required if endpoint is set to `:4317`.

- Go auto-instrumentation uses protocol buffers over HTTP (HTTP/proto or HTTP/protobuf) by default.

- Required if endpoint is set to `:4317`.

  For more information about procol buffers, see [Overview](https://protobuf.dev/overview/) (Protocol Buffers Documentation).

| Parameter | Description | Values |
|----|----|----|
| `env` | Definition of common environment variables for all instrumentation types. |  |
| `exporter` | Exporter configuration. |  |
| `propagators` | Propagators defines inter-process context propagation configuration. | `tracecontext`, `baggage`, `b3`, `b3multi`, `jaeger`, `ottrace`, `none` |
| `resource` | Resource attributes configuration. |  |
| `sampler` | Sampling configuration. |  |
| `apacheHttpd` | Configuration for the Apache HTTP Server instrumentation. |  |
| `dotnet` | Configuration for the .NET instrumentation. |  |
| `go` | Configuration for the Go instrumentation. |  |
| `java` | Configuration for the Java instrumentation. |  |
| `nodejs` | Configuration for the Node.js instrumentation. |  |
| `python` | Configuration for the Python instrumentation. | Depending on the programming language, environment variables might not work for configuring telemetry. For the SDKs that do not support environment variable configuration, you must add a similar configuration directly in the code. For more information, see [Environment Variable Specification](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/) (OpenTelemetry Documentation). |

Parameters used by the Operator to define the instrumentation

| Auto-instrumentation | Default protocol |
|----------------------|------------------|
| Java 1.x             | `otlp/grpc`      |
| Java 2.x             | `otlp/http`      |
| Python               | `otlp/http`      |
| .NET                 | `otlp/http`      |
| Go                   | `otlp/http`      |
| Apache HTTP Server   | `otlp/grpc`      |

Default protocol for auto-instrumentation

## Configuration of the OpenTelemetry SDK variables

You can use the `instrumentation.opentelemetry.io/inject-sdk` annotation in the OpenTelemetry Collector custom resource to instruct the Red Hat build of OpenTelemetry Operator to inject some of the following OpenTelemetry SDK environment variables, depending on the `Instrumentation` CR, into your pod:

- `OTEL_SERVICE_NAME`

- `OTEL_TRACES_SAMPLER`

- `OTEL_TRACES_SAMPLER_ARG`

- `OTEL_PROPAGATORS`

- `OTEL_RESOURCE_ATTRIBUTES`

- `OTEL_EXPORTER_OTLP_ENDPOINT`

- `OTEL_EXPORTER_OTLP_CERTIFICATE`

- `OTEL_EXPORTER_OTLP_CLIENT_CERTIFICATE`

- `OTEL_EXPORTER_OTLP_CLIENT_KEY`

| Value | Description |
|----|----|
| `"true"` | Injects the `Instrumentation` resource with the default name from the current namespace. |
| `"false"` | Injects no `Instrumentation` resource. |
| `"<instrumentation_name>"` | Specifies the name of the `Instrumentation` resource to inject from the current namespace. |
| `"<namespace>/<instrumentation_name>"` | Specifies the name of the `Instrumentation` resource to inject from another namespace. |

Values for the `instrumentation.opentelemetry.io/inject-sdk` annotation

## Exporter configuration

Although the `Instrumentation` custom resource supports setting up one or more exporters per signal, auto-instrumentation configures only the OTLP Exporter. So you must configure the endpoint to point to the OTLP Receiver on the Collector.

<div class="formalpara">

<div class="title">

Sample exporter TLS CA configuration using a config map

</div>

``` yaml
apiVersion: opentelemetry.io/v1alpha1
kind: Instrumentation
# ...
spec
# ...
  exporter:
    endpoint: https://production-collector.observability.svc.cluster.local:4317
    tls:
      configMapName: ca-bundle
      ca_file: service-ca.crt
# ...
```

</div>

- Specifies the OTLP endpoint using the HTTPS scheme and TLS.

- Specifies the name of the config map. The config map must already exist in the namespace of the pod injecting the auto-instrumentation.

- Points to the CA certificate in the config map or the absolute path to the certificate if the certificate is already present in the workload file system.

<div class="formalpara">

<div class="title">

Sample exporter mTLS configuration using a Secret

</div>

``` yaml
apiVersion: opentelemetry.io/v1alpha1
kind: Instrumentation
# ...
spec
# ...
  exporter:
    endpoint: https://production-collector.observability.svc.cluster.local:4317
    tls:
      secretName: serving-certs
      ca_file: service-ca.crt
      cert_file: tls.crt
      key_file: tls.key
# ...
```

</div>

- Specifies the OTLP endpoint using the HTTPS scheme and TLS.

- Specifies the name of the Secret for the `ca_file`, `cert_file`, and `key_file` values. The Secret must already exist in the namespace of the pod injecting the auto-instrumentation.

- Points to the CA certificate in the Secret or the absolute path to the certificate if the certificate is already present in the workload file system.

- Points to the client certificate in the Secret or the absolute path to the certificate if the certificate is already present in the workload file system.

- Points to the client key in the Secret or the absolute path to a key if the key is already present in the workload file system.

> [!NOTE]
> You can provide the CA certificate in a config map or Secret. If you provide it in both, the config map takes higher precedence than the Secret.

<div class="formalpara">

<div class="title">

Example configuration for CA bundle injection by using a config map and `Instrumentation` CR

</div>

``` yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: otelcol-cabundle
  namespace: tutorial-application
  annotations:
    service.beta.openshift.io/inject-cabundle: "true"
# ...
---
apiVersion: opentelemetry.io/v1alpha1
kind: Instrumentation
metadata:
  name: my-instrumentation
spec:
  exporter:
    endpoint: https://simplest-collector.tracing-system.svc.cluster.local:4317
    tls:
      configMapName: otelcol-cabundle
      ca: service-ca.crt
# ...
```

</div>

## Configuration of the Apache HTTP Server auto-instrumentation

> [!IMPORTANT]
> The Apache HTTP Server auto-instrumentation is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

| Name | Description | Default |
|----|----|----|
| `attrs` | Attributes specific to the Apache HTTP Server. |  |
| `configPath` | Location of the Apache HTTP Server configuration. | `/usr/local/apache2/conf` |
| `env` | Environment variables specific to the Apache HTTP Server. |  |
| `image` | Container image with the Apache SDK and auto-instrumentation. |  |
| `resourceRequirements` | The compute resource requirements. |  |
| `version` | Apache HTTP Server version. | `2.4` |

Parameters for the `.spec.apacheHttpd` field

<div class="formalpara">

<div class="title">

The `PodSpec` annotation to enable injection

</div>

``` yaml
instrumentation.opentelemetry.io/inject-apache-httpd: "true"
```

</div>

## Configuration of the .NET auto-instrumentation

> [!IMPORTANT]
> The .NET auto-instrumentation is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

> [!IMPORTANT]
> By default, this feature injects unsupported, upstream instrumentation libraries.

| Name | Description |
|----|----|
| `env` | Environment variables specific to .NET. |
| `image` | Container image with the .NET SDK and auto-instrumentation. |
| `resourceRequirements` | The compute resource requirements. |

For the .NET auto-instrumentation, the required `OTEL_EXPORTER_OTLP_ENDPOINT` environment variable must be set if the endpoint of the exporters is set to `4317`. The .NET autoinstrumentation uses `http/proto` by default, and the telemetry data must be set to the `4318` port.

<div class="formalpara">

<div class="title">

The `PodSpec` annotation to enable injection

</div>

``` yaml
instrumentation.opentelemetry.io/inject-dotnet: "true"
```

</div>

## Configuration of the Go auto-instrumentation

> [!IMPORTANT]
> The Go auto-instrumentation is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

> [!IMPORTANT]
> By default, this feature injects unsupported, upstream instrumentation libraries.

| Name | Description |
|----|----|
| `env` | Environment variables specific to Go. |
| `image` | Container image with the Go SDK and auto-instrumentation. |
| `resourceRequirements` | The compute resource requirements. |

<div class="formalpara">

<div class="title">

The `PodSpec` annotation to enable injection

</div>

``` yaml
instrumentation.opentelemetry.io/inject-go: "true"
instrumentation.opentelemetry.io/otel-go-auto-target-exe: "/<path>/<to>/<container>/<executable>"
```

</div>

- Sets the value for the required `OTEL_GO_AUTO_TARGET_EXE` environment variable.

<div class="formalpara">

<div class="title">

Permissions required for the Go auto-instrumentation in the OpenShift cluster

</div>

``` yaml
apiVersion: security.openshift.io/v1
kind: SecurityContextConstraints
metadata:
  name: otel-go-instrumentation-scc
allowHostDirVolumePlugin: true
allowPrivilegeEscalation: true
allowPrivilegedContainer: true
allowedCapabilities:
- "SYS_PTRACE"
fsGroup:
  type: RunAsAny
runAsUser:
  type: RunAsAny
seLinuxContext:
  type: RunAsAny
seccompProfiles:
- '*'
supplementalGroups:
  type: RunAsAny
```

</div>

> [!TIP]
> The CLI command for applying the permissions for the Go auto-instrumentation in the OpenShift cluster is as follows:
>
> ``` terminal
> $ oc adm policy add-scc-to-user otel-go-instrumentation-scc -z <service_account>
> ```

## Configuration of the Java auto-instrumentation

> [!IMPORTANT]
> The Java auto-instrumentation is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

> [!IMPORTANT]
> By default, this feature injects unsupported, upstream instrumentation libraries.

| Name | Description |
|----|----|
| `env` | Environment variables specific to Java. |
| `image` | Container image with the Java SDK and auto-instrumentation. |
| `resourceRequirements` | The compute resource requirements. |

<div class="formalpara">

<div class="title">

The `PodSpec` annotation to enable injection

</div>

``` yaml
instrumentation.opentelemetry.io/inject-java: "true"
```

</div>

## Configuration of the Node.js auto-instrumentation

> [!IMPORTANT]
> The Node.js auto-instrumentation is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

> [!IMPORTANT]
> By default, this feature injects unsupported, upstream instrumentation libraries.

| Name | Description |
|----|----|
| `env` | Environment variables specific to Node.js. |
| `image` | Container image with the Node.js SDK and auto-instrumentation. |
| `resourceRequirements` | The compute resource requirements. |

<div class="formalpara">

<div class="title">

The `PodSpec` annotations to enable injection

</div>

``` yaml
instrumentation.opentelemetry.io/inject-nodejs: "true"
```

</div>

## Configuration of the Python auto-instrumentation

> [!IMPORTANT]
> The Python auto-instrumentation is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

> [!IMPORTANT]
> By default, this feature injects unsupported, upstream instrumentation libraries.

| Name | Description |
|----|----|
| `env` | Environment variables specific to Python. |
| `image` | Container image with the Python SDK and auto-instrumentation. |
| `resourceRequirements` | The compute resource requirements. |

For Python auto-instrumentation, the `OTEL_EXPORTER_OTLP_ENDPOINT` environment variable must be set if the endpoint of the exporters is set to `4317`. Python auto-instrumentation uses `http/proto` by default, and the telemetry data must be set to the `4318` port.

<div class="formalpara">

<div class="title">

The `PodSpec` annotation to enable injection

</div>

``` yaml
instrumentation.opentelemetry.io/inject-python: "true"
```

</div>

## Multi-container pods

The instrumentation is injected to the first container that is available by default according to the pod specification. You can also specify the target container names for injection.

<div class="formalpara">

<div class="title">

Pod annotation

</div>

``` yaml
instrumentation.opentelemetry.io/container-names: "<container_1>,<container_2>"
```

</div>

- Use this annotation when you want to inject a single instrumentation in multiple containers.

> [!NOTE]
> The Go auto-instrumentation does not support multi-container auto-instrumentation injection.

## Multi-container pods with multiple instrumentations

Injecting instrumentation for an application language to one or more containers in a multi-container pod requires the following annotation:

``` yaml
instrumentation.opentelemetry.io/<application_language>-container-names: "<container_1>,<container_2>"
```

- You can inject instrumentation for only one language per container. For the list of supported `<application_language>` values, see the following table.

| Language    | Value for `<application_language>` |
|-------------|------------------------------------|
| ApacheHTTPD | `apache-httpd`                     |
| DotNet      | `dotnet`                           |
| Java        | `java`                             |
| NGINX       | `inject-nginx`                     |
| NodeJS      | `nodejs`                           |
| Python      | `python`                           |
| SDK         | `sdk`                              |

Supported values for the `<application_language>`

## Using the instrumentation CR with Service Mesh

When using the `Instrumentation` custom resource (CR) with Red Hat OpenShift Service Mesh, you must use the `b3multi` propagator.
