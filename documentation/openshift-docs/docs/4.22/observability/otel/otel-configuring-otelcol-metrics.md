The following list shows some of these metrics:

- Collector memory usage

- CPU utilization

- Number of active traces and spans processed

- Dropped spans, logs, or metrics

- Exporter and receiver statistics

The Red Hat build of OpenTelemetry Operator automatically creates a service named `<instance_name>-collector-monitoring` that exposes the Collector’s internal metrics. This service listens on port `8888` by default.

You can use these metrics for monitoring the Collector’s performance, resource consumption, and other internal behaviors. You can also use a Prometheus instance or another monitoring tool to scrape these metrics from the mentioned `<instance_name>-collector-monitoring` service.

> [!NOTE]
> When the `spec.observability.metrics.enableMetrics` field in the `OpenTelemetryCollector` custom resource (CR) is set to `true`, the `OpenTelemetryCollector` CR automatically creates a Prometheus `ServiceMonitor` or `PodMonitor` CR to enable Prometheus to scrape your metrics.

<div>

<div class="title">

Prerequisites

</div>

- Monitoring for user-defined projects is enabled in the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

- To enable metrics of an OpenTelemetry Collector instance, set the `spec.observability.metrics.enableMetrics` field to `true`:

  ``` yaml
  apiVersion: opentelemetry.io/v1beta1
  kind: OpenTelemetryCollector
  metadata:
    name: <name>
  spec:
    observability:
      metrics:
        enableMetrics: true
  ```

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

You can use the **Administrator** view of the web console to verify successful configuration:

</div>

1.  Go to **Observe** → **Targets**.

2.  Filter by **Source: User**.

3.  Check that the **ServiceMonitors** or **PodMonitors** in the `opentelemetry-collector-<instance_name>` format have the **Up** status.

<div>

<div class="title">

Additional resources

</div>

- [Enabling monitoring for user-defined projects](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.21/html/configuring_user_workload_monitoring/preparing-to-configure-the-monitoring-stack-uwm#enabling-monitoring-for-user-defined-projects-uwm_preparing-to-configure-the-monitoring-stack-uwm)

</div>
