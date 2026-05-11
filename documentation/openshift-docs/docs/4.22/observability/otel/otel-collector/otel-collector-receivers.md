<div wrapper="1" role="_abstract">

Receivers get data into the Collector. A receiver can be push or pull based. Generally, a receiver accepts data in a specified format, translates it into the internal format, and passes it to processors and exporters defined in the applicable pipelines. By default, no receivers are configured. One or more receivers must be configured. Receivers support one or more data sources.

</div>

Currently, the following General Availability and Technology Preview receivers are available for the Red Hat build of OpenTelemetry:

# OTLP Receiver

<div wrapper="1" role="_abstract">

The OTLP Receiver ingests traces, metrics, and logs by using the OpenTelemetry Protocol (OTLP).

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with an enabled OTLP Receiver

</div>

``` yaml
# ...
  config:
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
            tls:
              ca_file: ca.pem
              cert_file: cert.pem
              key_file: key.pem
              client_ca_file: client.pem
              reload_interval: 1h
          http:
            endpoint: 0.0.0.0:4318
            tls: {}

    service:
      pipelines:
        traces:
          receivers: [otlp]
        metrics:
          receivers: [otlp]
# ...
```

</div>

- The OTLP gRPC endpoint. If omitted, the default `0.0.0.0:4317` is used.

- The server-side TLS configuration. Defines paths to TLS certificates. If omitted, the TLS is disabled.

- The path to the TLS certificate at which the server verifies a client certificate. This sets the value of `ClientCAs` and `ClientAuth` to `RequireAndVerifyClientCert` in the `TLSConfig`. For more information, see the [`Config` of the Golang TLS package](https://godoc.org/crypto/tls#Config).

- Specifies the time interval at which the certificate is reloaded. If the value is not set, the certificate is never reloaded. The `reload_interval` field accepts a string containing valid units of time such as `ns`, `us`, `ms`, `s`, `m`, `h`.

- The OTLP HTTP endpoint. The default value is `0.0.0.0:4318`.

- The server-side TLS configuration. For more information, see the `grpc` protocol configuration section.

# Jaeger Receiver

<div wrapper="1" role="_abstract">

The Jaeger Receiver ingests traces in the Jaeger formats.

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with an enabled Jaeger Receiver

</div>

``` yaml
# ...
  config:
    receivers:
      jaeger:
        protocols:
          grpc:
            endpoint: 0.0.0.0:14250
          thrift_http:
            endpoint: 0.0.0.0:14268
          thrift_compact:
            endpoint: 0.0.0.0:6831
          thrift_binary:
            endpoint: 0.0.0.0:6832
          tls: {}

    service:
      pipelines:
        traces:
          receivers: [jaeger]
# ...
```

</div>

- The Jaeger gRPC endpoint. If omitted, the default `0.0.0.0:14250` is used.

- The Jaeger Thrift HTTP endpoint. If omitted, the default `0.0.0.0:14268` is used.

- The Jaeger Thrift Compact endpoint. If omitted, the default `0.0.0.0:6831` is used.

- The Jaeger Thrift Binary endpoint. If omitted, the default `0.0.0.0:6832` is used.

- The server-side TLS configuration. See the OTLP Receiver configuration section for more details.

# Host Metrics Receiver

<div wrapper="1" role="_abstract">

The Host Metrics Receiver ingests metrics in the OTLP format.

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with an enabled Host Metrics Receiver

</div>

``` yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: otel-hostfs-daemonset
  namespace: <namespace>
# ...
---
apiVersion: security.openshift.io/v1
kind: SecurityContextConstraints
allowHostDirVolumePlugin: true
allowHostIPC: false
allowHostNetwork: false
allowHostPID: true
allowHostPorts: false
allowPrivilegeEscalation: true
allowPrivilegedContainer: true
allowedCapabilities: null
defaultAddCapabilities:
- SYS_ADMIN
fsGroup:
  type: RunAsAny
groups: []
metadata:
  name: otel-hostmetrics
readOnlyRootFilesystem: true
runAsUser:
  type: RunAsAny
seLinuxContext:
  type: RunAsAny
supplementalGroups:
  type: RunAsAny
users:
- system:serviceaccount:<namespace>:otel-hostfs-daemonset
volumes:
- configMap
- emptyDir
- hostPath
- projected
# ...
---
apiVersion: opentelemetry.io/v1beta1
kind: OpenTelemetryCollector
metadata:
  name: otel
  namespace: <namespace>
spec:
  serviceAccount: otel-hostfs-daemonset
  mode: daemonset
  volumeMounts:
    - mountPath: /hostfs
      name: host
      readOnly: true
  volumes:
    - hostPath:
        path: /
      name: host
  config:
    receivers:
      hostmetrics:
        collection_interval: 10s
        initial_delay: 1s
        root_path: /
        scrapers:
          cpu: {}
          memory: {}
          disk: {}
    service:
      pipelines:
        metrics:
          receivers: [hostmetrics]
# ...
```

</div>

- Sets the time interval for host metrics collection. If omitted, the default value is `1m`.

- Sets the initial time delay for host metrics collection. If omitted, the default value is `1s`.

- Configures the `root_path` so that the Host Metrics Receiver knows where the root filesystem is. If running multiple instances of the Host Metrics Receiver, set the same `root_path` value for each instance.

- Lists the enabled host metrics scrapers. Available scrapers are `cpu`, `disk`, `load`, `filesystem`, `memory`, `network`, `paging`, `processes`, and `process`.

# Kubernetes Objects Receiver

<div wrapper="1" role="_abstract">

The Kubernetes Objects Receiver pulls or watches objects to be collected from the Kubernetes API server. This receiver watches primarily Kubernetes events, but it can collect any type of Kubernetes objects. This receiver gathers telemetry for the cluster as a whole, so only one instance of this receiver suffices for collecting all the data.

</div>

> [!IMPORTANT]
> The Kubernetes Objects Receiver is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with an enabled Kubernetes Objects Receiver

</div>

``` yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: otel-k8sobj
  namespace: <namespace>
# ...
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: otel-k8sobj
  namespace: <namespace>
rules:
- apiGroups:
  - ""
  resources:
  - events
  - pods
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - "events.k8s.io"
  resources:
  - events
  verbs:
  - watch
  - list
# ...
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: otel-k8sobj
subjects:
  - kind: ServiceAccount
    name: otel-k8sobj
    namespace: <namespace>
roleRef:
  kind: ClusterRole
  name: otel-k8sobj
  apiGroup: rbac.authorization.k8s.io
# ...
---
apiVersion: opentelemetry.io/v1beta1
kind: OpenTelemetryCollector
metadata:
  name: otel-k8s-obj
  namespace: <namespace>
spec:
  serviceAccount: otel-k8sobj
  mode: deployment
  config:
    receivers:
      k8sobjects:
        auth_type: serviceAccount
        objects:
          - name: pods
            mode: pull
            interval: 30s
            label_selector:
            field_selector:
            namespaces: [<namespace>,...]
          - name: events
            mode: watch
    exporters:
      debug:
    service:
      pipelines:
        logs:
          receivers: [k8sobjects]
          exporters: [debug]
# ...
```

</div>

- The Resource name that this receiver observes: for example, `pods`, `deployments`, or `events`.

- The observation mode that this receiver uses: `pull` or `watch`.

- Only applicable to the pull mode. The request interval for pulling an object. If omitted, the default value is `1h`.

- The label selector to define targets.

- The field selector to filter targets.

- The list of namespaces to collect events from. If omitted, the default value is `all`.

# Kubelet Stats Receiver

<div wrapper="1" role="_abstract">

The Kubelet Stats Receiver extracts metrics related to nodes, pods, containers, and volumes from the kubelet’s API server. These metrics are then channeled through the metrics-processing pipeline for additional analysis.

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with an enabled Kubelet Stats Receiver

</div>

``` yaml
# ...
  config:
    receivers:
      kubeletstats:
        collection_interval: 20s
        auth_type: "serviceAccount"
        endpoint: "https://${env:K8S_NODE_NAME}:10250"
        insecure_skip_verify: true
    service:
      pipelines:
        metrics:
          receivers: [kubeletstats]
  env:
    - name: K8S_NODE_NAME
      valueFrom:
        fieldRef:
          fieldPath: spec.nodeName
# ...
```

</div>

- Sets the `K8S_NODE_NAME` to authenticate to the API.

The Kubelet Stats Receiver requires additional permissions for the service account used for running the OpenTelemetry Collector.

<div class="formalpara">

<div class="title">

Permissions required by the service account

</div>

``` yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: otel-collector
rules:
  - apiGroups: ['']
    resources: ['nodes/stats']
    verbs: ['get', 'watch', 'list']
  - apiGroups: [""]
    resources: ["nodes/proxy"]
    verbs: ["get"]
# ...
```

</div>

- The permissions required when using the `extra_metadata_labels` or `request_utilization` or `limit_utilization` metrics.

# Prometheus Receiver

<div wrapper="1" role="_abstract">

The Prometheus Receiver scrapes the metrics endpoints.

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with an enabled Prometheus Receiver

</div>

``` yaml
# ...
  config:
    receivers:
        prometheus:
          config:
            scrape_configs:
              - job_name: 'my-app'
                scrape_interval: 5s
                static_configs:
                  - targets: ['my-app.example.svc.cluster.local:8888']
    service:
      pipelines:
        metrics:
          receivers: [prometheus]
# ...
```

</div>

- Scrapes configurations using the Prometheus format.

- The Prometheus job name.

- The interval for scraping the metrics data. Accepts time units. The default value is `1m`.

- The targets at which the metrics are exposed. This example scrapes the metrics from a `my-app` application in the `example` project.

# OTLP JSON File Receiver

<div wrapper="1" role="_abstract">

The OTLP JSON File Receiver extracts pipeline information from files containing data in the [ProtoJSON](https://protobuf.dev/programming-guides/json/) format and conforming to the [OpenTelemetry Protocol](https://opentelemetry.io/docs/specs/otel/protocol/) specification. The receiver watches a specified directory for changes such as created or modified files to process.

</div>

> [!IMPORTANT]
> The OTLP JSON File Receiver is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled OTLP JSON File Receiver

</div>

``` yaml
# ...
  config:
    otlpjsonfile:
      include:
        - "/var/log/*.log"
      exclude:
        - "/var/log/test.log"
# ...
```

</div>

- The list of file path glob patterns to watch.

- The list of file path glob patterns to ignore.

# Zipkin Receiver

<div wrapper="1" role="_abstract">

The Zipkin Receiver ingests traces in the Zipkin v1 and v2 formats.

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled Zipkin Receiver

</div>

``` yaml
# ...
  config:
    receivers:
      zipkin:
        endpoint: 0.0.0.0:9411
        tls: {}
    service:
      pipelines:
        traces:
          receivers: [zipkin]
# ...
```

</div>

- The Zipkin HTTP endpoint. If omitted, the default `0.0.0.0:9411` is used.

- The server-side TLS configuration. See the OTLP Receiver configuration section for more details.

# Kafka Receiver

<div wrapper="1" role="_abstract">

The Kafka Receiver receives traces, metrics, and logs from Kafka in the OTLP format.

</div>

> [!IMPORTANT]
> The Kafka Receiver is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled Kafka Receiver

</div>

``` yaml
# ...
  config:
    receivers:
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
          receivers: [kafka]
# ...
```

</div>

- The list of Kafka brokers. The default is `localhost:9092`.

- The Kafka protocol version. For example, `2.0.0`. This is a required field.

- The name of the Kafka topic to read from. The default is `otlp_spans`.

- The plain text authentication configuration. If omitted, plain text authentication is disabled.

- The client-side TLS configuration. Defines paths to the TLS certificates. If omitted, TLS authentication is disabled.

- Disables verifying the server’s certificate chain and host name. The default is `false`.

- ServerName indicates the name of the server requested by the client to support virtual hosting.

# Kubernetes Cluster Receiver

<div wrapper="1" role="_abstract">

The Kubernetes Cluster Receiver gathers cluster metrics and entity events from the Kubernetes API server. It uses the Kubernetes API to receive information about updates. Authentication for this receiver is only supported through service accounts.

</div>

> [!IMPORTANT]
> The Kubernetes Cluster Receiver is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled Kubernetes Cluster Receiver

</div>

``` yaml
# ...
  config:
    receivers:
      k8s_cluster:
        distribution: openshift
        collection_interval: 10s
    exporters:
      debug: {}
    service:
      pipelines:
        metrics:
          receivers: [k8s_cluster]
          exporters: [debug]
        logs/entity_events:
          receivers: [k8s_cluster]
          exporters: [debug]
# ...
```

</div>

This receiver requires a configured service account, RBAC rules for the cluster role, and the cluster role binding that binds the RBAC with the service account.

<div class="formalpara">

<div class="title">

`ServiceAccount` object

</div>

``` yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  labels:
    app: otelcontribcol
  name: otelcontribcol
# ...
```

</div>

<div class="formalpara">

<div class="title">

RBAC rules for the `ClusterRole` object

</div>

``` yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: otelcontribcol
  labels:
    app: otelcontribcol
rules:
- apiGroups:
  - quota.openshift.io
  resources:
  - clusterresourcequotas
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - ""
  resources:
  - events
  - namespaces
  - namespaces/status
  - nodes
  - nodes/spec
  - pods
  - pods/status
  - replicationcontrollers
  - replicationcontrollers/status
  - resourcequotas
  - services
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - apps
  resources:
  - daemonsets
  - deployments
  - replicasets
  - statefulsets
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - extensions
  resources:
  - daemonsets
  - deployments
  - replicasets
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - batch
  resources:
  - jobs
  - cronjobs
  verbs:
  - get
  - list
  - watch
- apiGroups:
    - autoscaling
  resources:
    - horizontalpodautoscalers
  verbs:
    - get
    - list
    - watch
# ...
```

</div>

<div class="formalpara">

<div class="title">

`ClusterRoleBinding` object

</div>

``` yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: otelcontribcol
  labels:
    app: otelcontribcol
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: otelcontribcol
subjects:
- kind: ServiceAccount
  name: otelcontribcol
  namespace: default
# ...
```

</div>

# OpenCensus Receiver

<div wrapper="1" role="_abstract">

The OpenCensus Receiver provides backwards compatibility with the OpenCensus project for easier migration of instrumented codebases. It receives metrics and traces in the OpenCensus format via gRPC or HTTP and JSON.

</div>

> [!WARNING]
> The OpenCensus Receiver is deprecated and might be removed in a future release.

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled OpenCensus Receiver

</div>

``` yaml
# ...
  config:
    receivers:
      opencensus:
        endpoint: 0.0.0.0:9411
        tls:
        cors_allowed_origins:
          - https://*.<example>.com
    service:
      pipelines:
        traces:
          receivers: [opencensus]
# ...
```

</div>

- The OpenCensus endpoint. If omitted, the default is `0.0.0.0:55678`.

- The server-side TLS configuration. See the OTLP Receiver configuration section for more details.

- You can also use the HTTP JSON endpoint to optionally configure CORS, which is enabled by specifying a list of allowed CORS origins in this field. Wildcards with `*` are accepted under the `cors_allowed_origins`. To match any origin, enter only `*`.

# Filelog Receiver

<div wrapper="1" role="_abstract">

The Filelog Receiver tails and parses logs from files.

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with an enabled Filelog Receiver that tails a text file

</div>

``` yaml
# ...
  config:
    receivers:
      filelog:
        include: [ /simple.log ]
        operators:
          - type: regex_parser
            regex: '^(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<sev>[A-Z]*) (?P<msg>.*)$'
            timestamp:
              parse_from: attributes.time
              layout: '%Y-%m-%d %H:%M:%S'
            severity:
              parse_from: attributes.sev
# ...
```

</div>

- A list of file glob patterns that match the file paths to be read.

- An array of Operators. Each Operator performs a simple task such as parsing a timestamp or JSON. To process logs into a needed format, chain the Operators together.

The next example shows how to make the Filelog Receiver work within security context constraints.

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with an enabled Filelog Receiver that parses cluster logs

</div>

``` yaml
apiVersion: security.openshift.io/v1
kind: SecurityContextConstraints
metadata:
  name: otel-clusterlogs-collector-scc
allowPrivilegedContainer: false
requiredDropCapabilities:
- ALL
allowHostDirVolumePlugin: true
volumes:
- configMap
- emptyDir
- hostPath
- projected
- secret
defaultAllowPrivilegeEscalation: false
allowPrivilegeEscalation: false
runAsUser:
  type: RunAsAny
seLinuxContext:
  type: RunAsAny
readOnlyRootFilesystem: true
forbiddenSysctls:
- '*'
seccompProfiles:
- runtime/default
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: otel-clusterlogs-collector-scc
rules:
- apiGroups:
  - security.openshift.io
  resourceNames:
  - otel-clusterlogs-collector-scc
  resources:
  - securitycontextconstraints
  verbs:
  - use
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: otel-clusterlogs-collector-scc
  namespace: observability
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: otel-clusterlogs-collector-scc
subjects:
- kind: ServiceAccount
  name: clusterlogs-collector
  namespace: observability
---
apiVersion: opentelemetry.io/v1beta1
kind: OpenTelemetryCollector
metadata:
  name: clusterlogs
  namespace: observability
spec:
  mode: daemonset
  podAnnotations:
    openshift.io/required-scc: otel-clusterlogs-collector-scc
  tolerations:
  - key: node-role.kubernetes.io/control-plane
    operator: Exists
    effect: NoSchedule
  config:
    receivers:
      filelog:
        include:
        - "/var/log/pods/*/*/*.log"
        exclude:
        - "/var/log/pods/*/otc-container/*.log"
        - "/var/log/pods/*/*/*.gz"
        - "/var/log/pods/*/*/*.log.*"
        - "/var/log/pods/*/*/*.tmp"
        include_file_path: true
        include_file_name: false
        operators:
        - type: container
    exporters:
      debug:
        verbosity: detailed
    service:
      pipelines:
        logs:
          receivers: [filelog]
          exporters: [debug]
  securityContext:
    runAsUser: 0
    seLinuxOptions:
      type: spc_t
    readOnlyRootFilesystem: true
    allowPrivilegeEscalation: false
    seccompProfile:
      type: RuntimeDefault
    capabilities:
      drop:
      - ALL
  volumeMounts:
  - name: varlogpods
    mountPath: /var/log/pods
    readOnly: true
  volumes:
  - name: varlogpods
    hostPath:
      path: /var/log/pods
```

</div>

- Configure a security context constraint (SCC) to allow access to files on the host.

- The OpenTelemetry Operator created this service account for the Collector. Assign the SCC to this service account.

- Schedule the Collector on control plane nodes.

- Exclude logs from the Collector container.

You can use this receiver to collect logs from pod filesystems in one of two ways:

- Configuring the receiver in a sidecar container running alongside your application pod.

- Deploying the receiver as a DaemonSet on the host machine with appropriate permissions to access Kubernetes logs.

To collect logs from application containers, you can use this receiver with sidecar injection. The Red Hat build of OpenTelemetry Operator allows injecting an OpenTelemetry Collector as a sidecar container into an application pod. This approach is useful when your application writes logs to files within the container filesystem. This receiver can then tail log files and apply Operators to parse the logs.

To use this receiver in sidecar mode to collect logs from application containers, you must configure volume mounts in the `OpenTelemetryCollector` custom resource. Both the application container and the sidecar Collector must mount the same shared volume, such as `emptyDir`. Define the volume in the application’s `Pod` specification. See the following example:

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the Filelog Receiver configured in sidecar mode

</div>

``` yaml
apiVersion: opentelemetry.io/v1beta1
kind: OpenTelemetryCollector
metadata:
  name: filelog
  namespace: otel-logging
spec:
  mode: sidecar
  volumeMounts:
  - name: logs
    mountPath: /var/log/app
  config:
    receivers:
      filelog:
        include:
        - /var/log/app/*.log
        operators:
        - type: regex_parser
          regex: '^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(?P<level>\w+)\] (?P<message>.*)$'
          timestamp:
            parse_from: attributes.timestamp
            layout: '%Y-%m-%d %H:%M:%S'
    processors: {}
    exporters:
      debug:
        verbosity: detailed
    service:
      pipelines:
        logs:
          receivers: [filelog]
          processors: []
          exporters: [debug]
```

</div>

- Defines the volume mount that the sidecar Collector uses to access the target log files. This volume must match the volume name defined in the application deployment.

- Specifies file glob patterns for matching the log files to tail. This receiver watches these paths for new log entries.

# Journald Receiver

<div wrapper="1" role="_abstract">

The Journald Receiver parses **journald** events from the **systemd** journal and sends them as logs.

</div>

> [!IMPORTANT]
> The Journald Receiver is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled Journald Receiver

</div>

``` yaml
apiVersion: v1
kind: Namespace
metadata:
  name: otel-journald
  labels:
    security.openshift.io/scc.podSecurityLabelSync: "false"
    pod-security.kubernetes.io/enforce: "privileged"
    pod-security.kubernetes.io/audit: "privileged"
    pod-security.kubernetes.io/warn: "privileged"
# ...
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: privileged-sa
  namespace: otel-journald
# ...
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: otel-journald-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:openshift:scc:privileged
subjects:
- kind: ServiceAccount
  name: privileged-sa
  namespace: otel-journald
# ...
---
apiVersion: opentelemetry.io/v1beta1
kind: OpenTelemetryCollector
metadata:
  name: otel-journald-logs
  namespace: otel-journald
spec:
  mode: daemonset
  serviceAccount: privileged-sa
  securityContext:
    allowPrivilegeEscalation: false
    capabilities:
      drop:
      - CHOWN
      - DAC_OVERRIDE
      - FOWNER
      - FSETID
      - KILL
      - NET_BIND_SERVICE
      - SETGID
      - SETPCAP
      - SETUID
    readOnlyRootFilesystem: true
    seLinuxOptions:
      type: spc_t
    seccompProfile:
      type: RuntimeDefault
  config:
    receivers:
      journald:
        files: /var/log/journal/*/*
        priority: info
        units:
          - kubelet
          - crio
          - init.scope
          - dnsmasq
        all: true
        retry_on_failure:
          enabled: true
          initial_interval: 1s
          max_interval: 30s
          max_elapsed_time: 5m
    processors:
    exporters:
      debug: {}
    service:
      pipelines:
        logs:
          receivers: [journald]
          exporters: [debug]
  volumeMounts:
  - name: journal-logs
    mountPath: /var/log/journal/
    readOnly: true
  volumes:
  - name: journal-logs
    hostPath:
      path: /var/log/journal
  tolerations:
  - key: node-role.kubernetes.io/master
    operator: Exists
    effect: NoSchedule
# ...
```

</div>

- Filters output by message priorities or priority ranges. The default value is `info`.

- Lists the units to read entries from. If empty, entries are read from all units.

- Includes very long logs and logs with unprintable characters. The default value is `false`.

- If set to `true`, the receiver pauses reading a file and attempts to resend the current batch of logs when encountering an error from downstream components. The default value is `false`.

- The time interval to wait after the first failure before retrying. The default value is `1s`. The units are `ms`, `s`, `m`, `h`.

- The upper bound for the retry backoff interval. When this value is reached, the time interval between consecutive retry attempts remains constant at this value. The default value is `30s`. The supported units are `ms`, `s`, `m`, `h`.

- The maximum time interval, including retry attempts, for attempting to send a logs batch to a downstream consumer. When this value is reached, the data are discarded. If the set value is `0`, retrying never stops. The default value is `5m`. The supported units are `ms`, `s`, `m`, `h`.

# Kubernetes Events Receiver

<div wrapper="1" role="_abstract">

The Kubernetes Events Receiver collects events from the Kubernetes API server. The collected events are converted into logs.

</div>

> [!IMPORTANT]
> The Kubernetes Events Receiver is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenShift Container Platform permissions required for the Kubernetes Events Receiver

</div>

``` yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: otel-collector
  labels:
    app: otel-collector
rules:
- apiGroups:
  - ""
  resources:
  - events
  - namespaces
  - namespaces/status
  - nodes
  - nodes/spec
  - pods
  - pods/status
  - replicationcontrollers
  - replicationcontrollers/status
  - resourcequotas
  - services
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - apps
  resources:
  - daemonsets
  - deployments
  - replicasets
  - statefulsets
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - extensions
  resources:
  - daemonsets
  - deployments
  - replicasets
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - batch
  resources:
  - jobs
  - cronjobs
  verbs:
  - get
  - list
  - watch
- apiGroups:
    - autoscaling
  resources:
    - horizontalpodautoscalers
  verbs:
    - get
    - list
    - watch
# ...
```

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled Kubernetes Event Receiver

</div>

``` yaml
# ...
  serviceAccount: otel-collector
  config:
    receivers:
      k8s_events:
        namespaces: [project1, project2]
    service:
      pipelines:
        logs:
          receivers: [k8s_events]
# ...
```

</div>

- The service account of the Collector that has the required ClusterRole `otel-collector` RBAC.

- The list of namespaces to collect events from. The default value is empty, which means that all namespaces are collected.

# Prometheus Remote Write Receiver

<div wrapper="1" role="_abstract">

The Prometheus Remote Write Receiver receives metrics from Prometheus using the Remote Write protocol and converts them to the OpenTelemetry format. This receiver supports only the Prometheus Remote Write v2 protocol.

</div>

> [!IMPORTANT]
> The Prometheus Remote Write Receiver is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with the enabled Prometheus Remote Write Receiver

</div>

``` yaml
# ...
  config:
    receivers:
      prometheusremotewrite:
        endpoint: 0.0.0.0:9090
    # ...
    service:
      pipelines:
        metrics:
          receivers: [prometheusremotewrite]
# ...
```

</div>

- The endpoint where the receiver listens for Prometheus Remote Write requests.

The following are the prerequisites for using this receiver with Prometheus:

- Prometheus is started with the metadata WAL records feature flag enabled.

- Prometheus Remote Write v2 Protocol is enabled in the Prometheus remote write configuration.

- Native histograms are enabled in Prometheus by using the feature flag.

- Prometheus is configured to convert classic histograms into native histograms.

For more information about enabling these Prometheus features, see the Prometheus documentation.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Feature flags: Metadata WAL Records](https://prometheus.io/docs/prometheus/latest/feature_flags/#metadata-wal-records)

- [Prometheus Remote-Write 2.0 specification (EXPERIMENTAL)](https://prometheus.io/docs/specs/prw/remote_write_spec_2_0/)

- [Native Histograms](https://prometheus.io/docs/specs/native_histograms/)

- [Feature flags: Native Histograms](https://prometheus.io/docs/prometheus/latest/feature_flags/#native-histograms)

- [Prometheus Configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/)

</div>

# Additional resources

- [OpenTelemetry Documentation: OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/)
