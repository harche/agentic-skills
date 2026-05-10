<div wrapper="1" role="_abstract">

Processors process the data between it is received and exported. Processors are optional. By default, no processors are enabled. Processors must be enabled for every data source. Not all processors support all data sources. Depending on the data source, multiple processors might be enabled. Note that the order of processors matters.

</div>

Currently, the following General Availability and Technology Preview processors are available for the Red Hat build of OpenTelemetry:

# Batch Processor

<div wrapper="1" role="_abstract">

The Batch Processor batches traces and metrics to reduce the number of outgoing connections needed to transfer the telemetry information.

</div>

<div class="formalpara">

<div class="title">

Example of the OpenTelemetry Collector custom resource when using the Batch Processor

</div>

``` yaml
# ...
  config:
    processors:
      batch:
        timeout: 5s
        send_batch_max_size: 10000
    service:
      pipelines:
        traces:
          processors: [batch]
        metrics:
          processors: [batch]
# ...
```

</div>

| Parameter | Description | Default |
|----|----|----|
| `timeout` | Sends the batch after a specific time duration and irrespective of the batch size. | `200ms` |
| `send_batch_size` | Sends the batch of telemetry data after the specified number of spans or metrics. | `8192` |
| `send_batch_max_size` | The maximum allowable size of the batch. Must be equal or greater than the `send_batch_size`. | `0` |
| `metadata_keys` | When activated, a batcher instance is created for each unique set of values found in the `client.Metadata`. | `[]` |
| `metadata_cardinality_limit` | When the `metadata_keys` are populated, this configuration restricts the number of distinct metadata key-value combinations processed throughout the duration of the process. | `1000` |

Parameters used by the Batch Processor

# Memory Limiter Processor

<div wrapper="1" role="_abstract">

The Memory Limiter Processor periodically checks the Collector’s memory usage and pauses data processing when the soft memory limit is reached. This processor supports traces, metrics, and logs. The preceding component, which is typically a receiver, is expected to retry sending the same data and may apply a backpressure to the incoming data. When memory usage exceeds the hard limit, the Memory Limiter Processor forces garbage collection to run.

</div>

<div class="formalpara">

<div class="title">

Example of the OpenTelemetry Collector custom resource when using the Memory Limiter Processor

</div>

``` yaml
# ...
  config:
    processors:
      memory_limiter:
        check_interval: 1s
        limit_mib: 4000
        spike_limit_mib: 800
    service:
      pipelines:
        traces:
          processors: [batch]
        metrics:
          processors: [batch]
# ...
```

</div>

| Parameter | Description | Default |
|----|----|----|
| `check_interval` | Time between memory usage measurements. The optimal value is `1s`. For spiky traffic patterns, you can decrease the `check_interval` or increase the `spike_limit_mib`. | `0s` |
| `limit_mib` | The hard limit, which is the maximum amount of memory in MiB allocated on the heap. Typically, the total memory usage of the OpenTelemetry Collector is about 50 MiB greater than this value. | `0` |
| `spike_limit_mib` | Spike limit, which is the maximum expected spike of memory usage in MiB. The optimal value is approximately 20% of `limit_mib`. To calculate the soft limit, subtract the `spike_limit_mib` from the `limit_mib`. | 20% of `limit_mib` |
| `limit_percentage` | Same as the `limit_mib` but expressed as a percentage of the total available memory. The `limit_mib` setting takes precedence over this setting. | `0` |
| `spike_limit_percentage` | Same as the `spike_limit_mib` but expressed as a percentage of the total available memory. Intended to be used with the `limit_percentage` setting. | `0` |

Parameters used by the Memory Limiter Processor

# Resource Detection Processor

<div wrapper="1" role="_abstract">

The Resource Detection Processor identifies host resource details in alignment with OpenTelemetry’s resource semantic standards. Using the detected information, this processor can add or replace the resource values in telemetry data. This processor supports traces and metrics. You can use this processor with multiple detectors such as the Docket metadata detector or the `OTEL_RESOURCE_ATTRIBUTES` environment variable detector.

</div>

> [!IMPORTANT]
> The Resource Detection Processor is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenShift Container Platform permissions required for the Resource Detection Processor

</div>

``` yaml
kind: ClusterRole
metadata:
  name: otel-collector
rules:
- apiGroups: ["config.openshift.io"]
  resources: ["infrastructures", "infrastructures/status"]
  verbs: ["get", "watch", "list"]
# ...
```

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector using the Resource Detection Processor

</div>

``` yaml
# ...
  config:
    processors:
      resourcedetection:
        detectors: [openshift]
        override: true
    service:
      pipelines:
        traces:
          processors: [resourcedetection]
        metrics:
          processors: [resourcedetection]
# ...
```

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector using the Resource Detection Processor with an environment variable detector

</div>

``` yaml
# ...
  config:
    processors:
      resourcedetection/env:
        detectors: [env]
        timeout: 2s
        override: false
# ...
```

</div>

- Specifies which detector to use. In this example, the environment detector is specified.

# Attributes Processor

<div wrapper="1" role="_abstract">

The Attributes Processor can modify attributes of a span, log, or metric. You can configure this processor to filter and match input data and include or exclude such data for specific actions.

</div>

This processor operates on a list of actions, executing them in the order specified in the configuration. The following actions are supported:

Insert
Inserts a new attribute into the input data when the specified key does not already exist.

Update
Updates an attribute in the input data if the key already exists.

Upsert
Combines the insert and update actions: Inserts a new attribute if the key does not exist yet. Updates the attribute if the key already exists.

Delete
Removes an attribute from the input data.

Hash
Hashes an existing attribute value as SHA1.

Extract
Extracts values by using a regular expression rule from the input key to the target keys defined in the rule. If a target key already exists, it is overridden similarly to the Span Processor’s `to_attributes` setting with the existing attribute as the source.

Convert
Converts an existing attribute to a specified type.

<div class="formalpara">

<div class="title">

OpenTelemetry Collector using the Attributes Processor

</div>

``` yaml
# ...
  config:
    processors:
      attributes/example:
        actions:
          - key: db.table
            action: delete
          - key: redacted_span
            value: true
            action: upsert
          - key: copy_key
            from_attribute: key_original
            action: update
          - key: account_id
            value: 2245
            action: insert
          - key: account_password
            action: delete
          - key: account_email
            action: hash
          - key: http.status_code
            action: convert
            converted_type: int
# ...
```

</div>

# Resource Processor

<div wrapper="1" role="_abstract">

The Resource Processor applies changes to the resource attributes. This processor supports traces, metrics, and logs.

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector using the Resource Processor

</div>

``` yaml
# ...
  config:
    processors:
      attributes:
      - key: cloud.availability_zone
        value: "zone-1"
        action: upsert
      - key: k8s.cluster.name
        from_attribute: k8s-cluster
        action: insert
      - key: redundant-attribute
        action: delete
# ...
```

</div>

Attributes represent the actions that are applied to the resource attributes, such as delete the attribute, insert the attribute, or upsert the attribute.

# Span Processor

<div wrapper="1" role="_abstract">

The Span Processor modifies the span name based on its attributes or extracts the span attributes from the span name. This processor can also change the span status and include or exclude spans. This processor supports traces.

</div>

Span renaming requires specifying attributes for the new name by using the `from_attributes` configuration.

> [!IMPORTANT]
> The Span Processor is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector using the Span Processor for renaming a span

</div>

``` yaml
# ...
  config:
    processors:
      span:
        name:
          from_attributes: [<key1>, <key2>, ...]
          separator: <value>
# ...
```

</div>

- Defines the keys to form the new span name.

- An optional separator.

You can use this processor to extract attributes from the span name.

<div class="formalpara">

<div class="title">

OpenTelemetry Collector using the Span Processor for extracting attributes from a span name

</div>

``` yaml
# ...
  config:
    processors:
      span/to_attributes:
        name:
          to_attributes:
            rules:
              - ^\/api\/v1\/document\/(?P<documentId>.*)\/update$
# ...
```

</div>

- This rule defines how the extraction is to be executed. You can define more rules: for example, in this case, if the regular expression matches the name, a `documentID` attribute is created. In this example, if the input span name is `/api/v1/document/12345678/update`, this results in the `/api/v1/document/{documentId}/update` output span name, and a new `"documentId"="12345678"` attribute is added to the span.

You can have the span status modified.

<div class="formalpara">

<div class="title">

OpenTelemetry Collector using the Span Processor for status change

</div>

``` yaml
# ...
  config:
    processors:
      span/set_status:
        status:
          code: Error
          description: "<error_description>"
# ...
```

</div>

# Kubernetes Attributes Processor

<div wrapper="1" role="_abstract">

The Kubernetes Attributes Processor enables automatic configuration of spans, metrics, and log resource attributes by using the Kubernetes metadata. This processor supports traces, metrics, and logs. This processor automatically identifies the Kubernetes resources, extracts the metadata from them, and incorporates this extracted metadata as resource attributes into relevant spans, metrics, and logs. It utilizes the Kubernetes API to discover all pods operating within a cluster, maintaining records of their IP addresses, pod UIDs, and other relevant metadata.

</div>

<div class="formalpara">

<div class="title">

Minimum OpenShift Container Platform permissions required for the Kubernetes Attributes Processor

</div>

``` yaml
kind: ClusterRole
metadata:
  name: otel-collector
rules:
  - apiGroups: ['']
    resources: ['pods', 'namespaces']
    verbs: ['get', 'watch', 'list']
  - apiGroups: ['apps']
    resources: ['replicasets']
    verbs: ['get', 'watch', 'list']
# ...
```

</div>

<div class="formalpara">

<div class="title">

OpenTelemetry Collector using the Kubernetes Attributes Processor

</div>

``` yaml
# ...
  config:
    processors:
         k8sattributes:
             filter:
                 node_from_env_var: KUBE_NODE_NAME
# ...
```

</div>

# Filter Processor

<div wrapper="1" role="_abstract">

The Filter Processor leverages the OpenTelemetry Transformation Language to establish criteria for discarding telemetry data. If any of these conditions are satisfied, the telemetry data are discarded. You can combine the conditions by using the logical OR operator. This processor supports traces, metrics, and logs.

</div>

> [!IMPORTANT]
> The Filter Processor is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

OpenTelemetry Collector custom resource with an enabled Filter Processor

</div>

``` yaml
# ...
  config:
    processors:
      filter/ottl:
        error_mode: ignore
        traces:
          span:
          - 'attributes["container.name"] == "app_container_1"'
          - 'resource.attributes["host.name"] == "localhost"'
# ...
```

</div>

- Defines the error mode. When set to `ignore`, ignores errors returned by conditions. When set to `propagate`, returns the error up the pipeline. An error causes the payload to be dropped from the Collector.

- Filters the spans that have the `container.name == app_container_1` attribute.

- Filters the spans that have the `host.name == localhost` resource attribute.

# Cumulative-to-Delta Processor

<div wrapper="1" role="_abstract">

The Cumulative-to-Delta Processor converts monotonic, cumulative-sum, and histogram metrics to monotonic delta metrics.

</div>

You can filter metrics by using the `include:` or `exclude:` fields and specifying the `strict` or `regexp` metric name matching.

Because this processor calculates delta by storing the previous value of a metric, you must set up the metric source to send the metric data to a single stateful Collector instance rather than a deployment of multiple Collectors.

This processor does not convert non-monotonic sums and exponential histograms.

> [!IMPORTANT]
> The Cumulative-to-Delta Processor is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

Example of an OpenTelemetry Collector custom resource with an enabled Cumulative-to-Delta Processor

</div>

``` yaml
# ...
mode: sidecar
config:
  processors:
    cumulativetodelta:
      include:
        match_type: strict
        metrics:
        - <metric_1_name>
        - <metric_2_name>
      exclude:
        match_type: regexp
        metrics:
        - "<regular_expression_for_metric_names>"
# ...
```

</div>

- To tie the Collector’s lifecycle to the metric source, you can run the Collector as a sidecar to the application that emits the cumulative temporality metrics.

- Optional: You can limit which metrics the processor converts by explicitly defining which metrics you want converted in this stanza. If you omit this field, the processor converts all metrics, except the metrics that are listed in the `exclude` field.

- Defines the value that you provided in the `metrics` field as an exact match by using the `strict` parameter or a regular expression by using the `regex` parameter.

- Lists the names of the metrics that you want to convert. The processor converts exact matches or matches for regular expressions. If a metric matches both the `include` and `exclude` filters, the `exclude` filter takes precedence.

- Optional: You can exclude certain metrics from conversion by explicitly defining them here.

# Group-by-Attributes Processor

<div wrapper="1" role="_abstract">

The Group-by-Attributes Processor groups all spans, log records, and metric datapoints that share the same attributes by reassigning them to a Resource that matches those attributes.

</div>

> [!IMPORTANT]
> The Group-by-Attributes Processor is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

At minimum, configuring this processor involves specifying an array of attribute keys to be used to group spans, log records, or metric datapoints together, as in the following example:

<div class="formalpara">

<div class="title">

Example of the OpenTelemetry Collector custom resource when using the Group-by-Attributes Processor

</div>

``` yaml
# ...
  config:
    processors:
      groupbyattrs:
        keys:
          - <key1>
          - <key2>
# ...
```

</div>

- Specifies attribute keys to group by.

- If a processed span, log record, or metric datapoint contains at least one of the specified attribute keys, it is reassigned to a Resource that shares the same attribute values; and if no such Resource exists, a new one is created. If none of the specified attribute keys is present in the processed span, log record, or metric datapoint, then it remains associated with its current Resource. Multiple instances of the same Resource are consolidated.

# Transform Processor

<div wrapper="1" role="_abstract">

The Transform Processor enables modification of telemetry data according to specified rules and in the [OpenTelemetry Transformation Language (OTTL)](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/pkg/ottl). For each signal type, the processor processes a series of conditions and statements associated with a specific OTTL Context type and then executes them in sequence on incoming telemetry data as specified in the configuration. Each condition and statement can access and modify telemetry data by using various functions, allowing conditions to dictate if a function is to be executed.

</div>

All statements are written in the OTTL. You can configure multiple context statements for different signals, traces, metrics, and logs. The value of the `context` type specifies which OTTL Context the processor must use when interpreting the associated statements.

> [!IMPORTANT]
> The Transform Processor is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div class="formalpara">

<div class="title">

Configuration summary

</div>

``` yaml
# ...
config:
    processors:
      transform:
        error_mode: ignore
        <trace|metric|log>_statements:
          - context: <string>
            conditions:
              - <string>
              - <string>
            statements:
              - <string>
              - <string>
              - <string>
          - context: <string>
            statements:
              - <string>
              - <string>
              - <string>
# ...
```

</div>

- Optional: See the following table "Values for the optional `error_mode` field".

- Indicates a signal to be transformed.

- See the following table "Values for the `context` field".

- Optional: Conditions for performing a transformation.

<div class="formalpara">

<div class="title">

Example of the OpenTelemetry Collector custom resource when using the Transform Processor

</div>

``` yaml
# ...
  config:
    transform:
      error_mode: ignore
      trace_statements:
        - context: resource
          statements:
            - keep_keys(attributes, ["service.name", "service.namespace", "cloud.region", "process.command_line"])
            - replace_pattern(attributes["process.command_line"], "password\\=[^\\s]*(\\s?)", "password=***")
            - limit(attributes, 100, [])
            - truncate_all(attributes, 4096)
        - context: span
          statements:
            - set(status.code, 1) where attributes["http.path"] == "/health"
            - set(name, attributes["http.route"])
            - replace_match(attributes["http.target"], "/user/*/list/*", "/user/{userId}/list/{listId}")
            - limit(attributes, 100, [])
            - truncate_all(attributes, 4096)
# ...
```

</div>

- Transforms a trace signal.

- Keeps keys on the resources.

- Replaces attributes and replaces string characters in password fields with asterisks.

- Performs transformations at the span level.

| Signal Statement    | Valid Contexts                             |
|---------------------|--------------------------------------------|
| `trace_statements`  | `resource`, `scope`, `span`, `spanevent`   |
| `metric_statements` | `resource`, `scope`, `metric`, `datapoint` |
| `log_statements`    | `resource`, `scope`, `log`                 |

Values for the `context` field

| Value | Description |
|----|----|
| `ignore` | Ignores and logs errors returned by statements and then continues to the next statement. |
| `silent` | Ignores and doesn’t log errors returned by statements and then continues to the next statement. |
| `propagate` | Returns errors up the pipeline and drops the payload. Implicit default. |

Values for the optional `error_mode` field

# Tail Sampling Processor

<div wrapper="1" role="_abstract">

The Tail Sampling Processor samples traces according to user-defined policies when all of the spans are completed. Tail-based sampling enables you to filter the traces of interest and reduce your data ingestion and storage costs.

</div>

> [!IMPORTANT]
> The Tail Sampling Processor is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

This processor reassembles spans into new batches and strips spans of their original context.

> [!TIP]
> - In pipelines, place this processor downstream of any processors that rely on context: for example, after the Kubernetes Attributes Processor.
>
> - If scaling the Collector, ensure that one Collector instance receives all spans of the same trace so that this processor makes correct sampling decisions based on the specified sampling policies. You can achieve this by setting up two layers of Collectors: the first layer of Collectors with the Load Balancing Exporter, and the second layer of Collectors with the Tail Sampling Processor.

<div class="formalpara">

<div class="title">

Example of the OpenTelemetry Collector custom resource when using the Tail Sampling Processor

</div>

``` yaml
# ...
config:
  processors:
    tail_sampling:
      decision_wait: 30s
      num_traces: 50000
      expected_new_traces_per_sec: 10
      policies:
        [
          {
            <definition_of_policy_1>
          },
          {
            <definition_of_policy_2>
          },
          {
            <definition_of_policy_3>
          },
        ]
# ...
```

</div>

- Processor name.

- Optional: Decision delay time, counted from the time of the first span, before the processor makes a sampling decision on each trace. Defaults to `30s`.

- Optional: The number of traces kept in memory. Defaults to `50000`.

- Optional: The expected number of new traces per second, which is helpful for allocating data structures. Defaults to `0`.

- Definitions of the policies for trace evaluation. The processor evaluates each trace against all of the specified policies and then either samples or drops the trace.

You can choose and combine policies from the following list:

- The following policy samples all traces:

  ``` yaml
  # ...
        policies:
          [
            {
              name: <always_sample_policy>,
              type: always_sample,
            },
          ]
  # ...
  ```

- The following policy samples only traces of a duration that is within a specified range:

  ``` yaml
  # ...
        policies:
          [
            {
              name: <latency_policy>,
              type: latency,
              latency: {threshold_ms: 5000, upper_threshold_ms: 10000}
            },
          ]
  # ...
  ```

  - The provided `5000` and `10000` values are examples. You can estimate the desired latency values by looking at the earliest start time value and latest end time value. If you omit the `upper_threshold_ms` field, this policy samples all latencies greater than the specified `threshold_ms` value.

- The following policy samples traces by numeric value matches for resource and record attributes:

  ``` yaml
  # ...
        policies:
          [
            {
              name: <numeric_attribute_policy>,
              type: numeric_attribute,
              numeric_attribute: {key: <key1>, min_value: 50, max_value: 100}
            },
          ]
  # ...
  ```

  - The provided `50` and `100` values are examples.

- The following policy samples only a percentage of traces:

  ``` yaml
  # ...
        policies:
          [
            {
              name: <probabilistic_policy>,
              type: probabilistic,
              probabilistic: {sampling_percentage: 10}
            },
          ]
  # ...
  ```

  - The provided `10` value is an example.

- The following policy samples traces by the status code: `OK`, `ERROR`, or `UNSET`:

  ``` yaml
  # ...
        policies:
          [
            {
              name: <status_code_policy>,
              type: status_code,
              status_code: {status_codes: [ERROR, UNSET]}
            },
          ]
  # ...
  ```

- The following policy samples traces by string value matches for resource and record attributes:

  ``` yaml
  # ...
        policies:
          [
            {
              name: <string_attribute_policy>,
              type: string_attribute,
              string_attribute: {key: <key2>, values: [<value1>, <val>*], enabled_regex_matching: true, cache_max_size: 10}
            },
          ]
  # ...
  ```

  - This policy definition supports both exact and regular-expression value matches. The provided `10` value in the `cache_max_size` field is an example.

- The following policy samples traces by the rate of spans per second:

  ``` yaml
  # ...
        policies:
          [
            {
              name: <rate_limiting_policy>,
              type: rate_limiting,
              rate_limiting: {spans_per_second: 35}
            },
          ]
  # ...
  ```

  - The provided `35` value is an example.

- The following policy samples traces by the minimum and maximum number of spans inclusively:

  ``` yaml
  # ...
        policies:
          [
            {
              name: <span_count_policy>,
              type: span_count,
              span_count: {min_spans: 2, max_spans: 20}
            },
          ]
  # ...
  ```

  - If the sum of all spans in the trace is outside the range threshold, the trace is not sampled. The provided `2` and `20` values are examples.

- The following policy samples traces by `TraceState` value matches:

  ``` yaml
  # ...
        policies:
          [
            {
              name: <trace_state_policy>,
              type: trace_state,
              trace_state: { key: <key3>, values: [<value1>, <value2>] }
            },
          ]
  # ...
  ```

- The following policy samples traces by a boolean attribute (resource and record):

  ``` yaml
  # ...
        policies:
          [
            {
              name: <bool_attribute_policy>,
              type: boolean_attribute,
              boolean_attribute: {key: <key4>, value: true}
            },
          ]
  # ...
  ```

- The following policy samples traces by a given boolean OTTL condition for a span or span event:

  ``` yaml
  # ...
        policies:
          [
            {
              name: <ottl_policy>,
              type: ottl_condition,
              ottl_condition: {
                error_mode: ignore,
                span: [
                  "attributes[\"<test_attr_key_1>\"] == \"<test_attr_value_1>\"",
                  "attributes[\"<test_attr_key_2>\"] != \"<test_attr_value_1>\"",
                ],
                spanevent: [
                  "name != \"<test_span_event_name>\"",
                  "attributes[\"<test_event_attr_key_2>\"] != \"<test_event_attr_value_1>\"",
                ]
              }
            },
          ]
  # ...
  ```

- The following is an `AND` policy that samples traces based on a combination of multiple policies:

  ``` yaml
  # ...
        policies:
          [
            {
              name: <and_policy>,
              type: and,
              and: {
                and_sub_policy:
                [
                  {
                    name: <and_policy_1>,
                    type: numeric_attribute,
                    numeric_attribute: { key: <key1>, min_value: 50, max_value: 100 }
                  },
                  {
                    name: <and_policy_2>,
                    type: string_attribute,
                    string_attribute: { key: <key2>, values: [ <value1>, <value2> ] }
                  },
                ]
              }
            },
          ]
  # ...
  ```

  - The provided `50` and `100` values are examples.

- The following is a `DROP` policy that drops traces from sampling based on a combination of multiple policies:

  ``` yaml
  # ...
        policies:
          [
            {
              name: <drop_policy>,
              type: drop,
              drop: {
                drop_sub_policy:
                [
                  {
                    name: <drop_policy_1>,
                    type: string_attribute,
                    string_attribute: {key: url.path, values: [\/health, \/metrics], enabled_regex_matching: true}
                  }
                ]
              }
            },
          ]
  # ...
  ```

- The following policy samples traces by a combination of the previous samplers and with ordering and rate allocation per sampler:

  ``` yaml
  # ...
        policies:
          [
            {
              name: <composite_policy>,
              type: composite,
              composite:
                {
                  max_total_spans_per_second: 100,
                  policy_order: [<composite_policy_1>, <composite_policy_2>, <composite_policy_3>],
                  composite_sub_policy:
                    [
                      {
                        name: <composite_policy_1>,
                        type: numeric_attribute,
                        numeric_attribute: {key: <key1>, min_value: 50}
                      },
                      {
                        name: <composite_policy_2>,
                        type: string_attribute,
                        string_attribute: {key: <key2>, values: [<value1>, <value2>]}
                      },
                      {
                        name: <composite_policy_3>,
                        type: always_sample
                      }
                    ],
                    rate_allocation:
                    [
                      {
                        policy: <composite_policy_1>,
                        percent: 50
                      },
                      {
                        policy: <composite_policy_2>,
                        percent: 25
                      }
                    ]
                }
            },
          ]
  # ...
  ```

  - Allocates percentages of spans according to the order of applied policies. For example, if you set the `100` value in the `max_total_spans_per_second` field, you can set the following values in the `rate_allocation` section: the `50` percent value in the `policy: <composite_policy_1>` section to allocate 50 spans per second, and the `25` percent value in the `policy: <composite_policy_2>` section to allocate 25 spans per second. To fill the remaining capacity, you can set the `always_sample` value in the `type` field of the `name: <composite_policy_3>` section.

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [OpenTelemetry Blog: Tail Sampling with OpenTelemetry: Why it’s useful, how to do it, and what to consider](https://opentelemetry.io/blog/2022/tail-sampling/)

- [OpenTelemetry Documentation: Gateway](https://opentelemetry.io/docs/collector/deployment/gateway/)

</div>

# Probabilistic Sampling Processor

<div wrapper="1" role="_abstract">

If you handle high volumes of telemetry data and seek to reduce costs by reducing processed data volumes, you can use the Probabilistic Sampling Processor as an alternative to the Tail Sampling Processor.

</div>

> [!IMPORTANT]
> Probabilistic Sampling Processor is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

The processor samples a specified percentage of trace spans or log records statelessly and per request.

The processor adds the information about the used effective sampling probability into the telemetry data:

- In trace spans, the processor encodes the threshold and optional randomness information in the W3C Trace Context `tracestate` fields.

- In log records, the processor encodes the threshold and randomness information as attributes.

The following is an example `OpenTelemetryCollector` custom resource configuration for the Probabilistic Sampling Processor for sampling trace spans:

``` yaml
# ...
  config:
    processors:
      probabilistic_sampler:
        sampling_percentage: 15.3
        mode: "proportional"
        hash_seed: 22
        sampling_precision: 14
        fail_closed: true
# ...
service:
  pipelines:
    traces:
      processors: [probabilistic_sampler]
# ...
```

- For trace pipelines, the source of randomness is the hashed value of the span trace ID.

- Required. Accepts a 32-bit floating-point percentage value at which spans are to be sampled.

- Optional. Accepts a supported string value for a sampling logic mode: the default `hash_seed`, `proportional`, or `equalizing`. The `hash_seed` mode applies the Fowler–Noll–Vo (FNV) hash function to the trace ID and weighs the hashed value against the sampling percentage value. You can also use the `hash_seed` mode with units of telemetry other than the trace ID. The `proportional` mode samples a strict, probability-based ratio of the total span quantity, and is based on the OpenTelemetry and World Wide Web Consortium specifications. The `equalizing` mode is useful for lowering the sampling probability to a minimum value across a whole pipeline or applying a uniform sampling probability in Collector deployments where client SDKs have mixed sampling configurations.

- Optional. Accepts a 32-bit unsigned integer, which is used to compute the hash algorithm. When this field is not configured, the default seed value is `0`. If you use multiple tiers of Collector instances, you must configure all Collectors of the same tier to the same seed value.

- Optional. Determines the number of hexadecimal digits used to encode the sampling threshold. Accepts an integer value. The supported values are `1`-`14`. The default value `4` causes the threshold to be rounded if it contains more than 16 significant bits, which is the case of the `proportional` mode that uses 56 bits. If you select the `proportional` mode, use a greater value for the purpose of preserving precision applied by preceding samplers.

- Optional. Rejects spans with sampling errors. Accepts a boolean value. The default value is `true`.

The following is an example `OpenTelemetryCollector` custom resource configuration for the Probabilistic Sampling Processor for sampling log records:

``` yaml
# ...
  config:
    processors:
      probabilistic_sampler/logs:
        sampling_percentage: 15.3
        mode: "hash_seed"
        hash_seed: 22
        sampling_precision: 4
        attribute_source: "record"
        from_attribute: "<log_record_attribute_name>"
        fail_closed: true
# ...
service:
  pipelines:
    logs:
      processors: [ probabilistic_sampler/logs ]
# ...
```

- Required. Accepts a 32-bit floating-point percentage value at which spans are to be sampled.

- Optional. Accepts a supported string value for a sampling logic mode: the default `hash_seed`, `equalizing`, or `proportional`. The `hash_seed` mode applies the Fowler–Noll–Vo (FNV) hash function to the trace ID or a specified log record attribute and then weighs the hashed value against the sampling percentage value. You can also use `hash_seed` mode with other units of telemetry than trace ID, for example to use the `service.instance.id` resource attribute for collecting log records from a percentage of pods. The `equalizing` mode is useful for lowering the sampling probability to a minimum value across a whole pipeline or applying a uniform sampling probability in Collector deployments where client SDKs have mixed sampling configurations. The `proportional` mode samples a strict, probability-based ratio of the total span quantity, and is based on the OpenTelemetry and World Wide Web Consortium specifications.

- Optional. Accepts a 32-bit unsigned integer, which is used to compute the hash algorithm. When this field is not configured, the default seed value is `0`. If you use multiple tiers of Collector instances, you must configure all Collectors of the same tier to the same seed value.

- Optional. Determines the number of hexadecimal digits used to encode the sampling threshold. Accepts an integer value. The supported values are `1`-`14`. The default value `4` causes the threshold to be rounded if it contains more than 16 significant bits, which is the case of the `proportional` mode that uses 56 bits. If you select the `proportional` mode, use a greater value for the purpose of preserving precision applied by preceding samplers.

- Optional. Defines where to look for the log record attribute in `from_attribute`. The log record attribute is used as the source of randomness. Accept the default `traceID` value or the `record` value.

- Optional. The name of a log record attribute to be used to compute the sampling hash, such as a unique log record ID. Accepts a string value. The default value is `""`. Use this field only if you need to specify a log record attribute as the source of randomness in those situations where the trace ID is absent or trace ID sampling is disabled or the `attribute_source` field is set to the `record` value.

- Optional. Rejects spans with sampling errors. Accepts a boolean value. The default value is `true`.

# Additional resources

- [OpenTelemetry Documentation: OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/)
