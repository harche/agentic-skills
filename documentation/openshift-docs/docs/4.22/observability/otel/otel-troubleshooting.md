The OpenTelemetry Collector offers multiple ways to measure its health as well as investigate data ingestion issues.

# Collecting diagnostic data from the command line

When submitting a support case, it is helpful to include diagnostic information about your cluster to Red Hat Support. You can use the `oc adm must-gather` tool to gather diagnostic data for resources of various types, such as `OpenTelemetryCollector`, `Instrumentation`, and the created resources like `Deployment`, `Pod`, or `ConfigMap`. The `oc adm must-gather` tool creates a new pod that collects this data.

<div>

<div class="title">

Procedure

</div>

- From the directory where you want to save the collected data, run the `oc adm must-gather` command to collect the data:

  ``` terminal
  $ oc adm must-gather --image=ghcr.io/open-telemetry/opentelemetry-operator/must-gather -- \
  /usr/bin/must-gather --operator-namespace <operator_namespace>
  ```

  - The default namespace where the Operator is installed is `openshift-opentelemetry-operator`.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the new directory is created and contains the collected data.

</div>

# Getting the OpenTelemetry Collector logs

You can get the logs for the OpenTelemetry Collector as follows.

<div>

<div class="title">

Procedure

</div>

1.  Set the relevant log level in the `OpenTelemetryCollector` custom resource (CR):

    ``` yaml
      config:
        service:
          telemetry:
            logs:
              level: debug
    ```

    - Collector’s log level. Supported values include `info`, `warn`, `error`, or `debug`. Defaults to `info`.

2.  Use the `oc logs` command or the web console to retrieve the logs.

</div>

# Exposing the metrics

The OpenTelemetry Collector exposes the following metrics about the data volumes it has processed:

`otelcol_receiver_accepted_spans`
The number of spans successfully pushed into the pipeline.

`otelcol_receiver_refused_spans`
The number of spans that could not be pushed into the pipeline.

`otelcol_exporter_sent_spans`
The number of spans successfully sent to the destination.

`otelcol_exporter_enqueue_failed_spans`
The number of spans failed to be added to the sending queue.

`otelcol_receiver_accepted_logs`
The number of logs successfully pushed into the pipeline.

`otelcol_receiver_refused_logs`
The number of logs that could not be pushed into the pipeline.

`otelcol_exporter_sent_logs`
The number of logs successfully sent to the destination.

`otelcol_exporter_enqueue_failed_logs`
The number of logs failed to be added to the sending queue.

`otelcol_receiver_accepted_metrics`
The number of metrics successfully pushed into the pipeline.

`otelcol_receiver_refused_metrics`
The number of metrics that could not be pushed into the pipeline.

`otelcol_exporter_sent_metrics`
The number of metrics successfully sent to the destination.

`otelcol_exporter_enqueue_failed_metrics`
The number of metrics failed to be added to the sending queue.

You can use these metrics to troubleshoot issues with your Collector. For example, if the `otelcol_receiver_refused_spans` metric has a high value, it indicates that the Collector is not able to process incoming spans.

The Operator creates a `<cr_name>-collector-monitoring` telemetry service that you can use to scrape the metrics endpoint.

<div>

<div class="title">

Procedure

</div>

1.  Enable the telemetry service by adding the following lines in the `OpenTelemetryCollector` custom resource (CR):

    ``` yaml
    # ...
      config:
        service:
          telemetry:
            metrics:
              readers:
              - pull:
                  exporter:
                    prometheus:
                      host: 0.0.0.0
                      port: 8888
    # ...
    ```

    - The port at which the internal collector metrics are exposed. Defaults to `:8888`.

2.  Retrieve the metrics by running the following command, which uses the port-forwarding Collector pod:

    ``` terminal
    $ oc port-forward <collector_pod>
    ```

3.  In the `OpenTelemetryCollector` CR, set the `enableMetrics` field to `true` to scrape internal metrics:

    ``` yaml
    apiVersion: opentelemetry.io/v1beta1
    kind: OpenTelemetryCollector
    spec:
    # ...
      mode: deployment
      observability:
        metrics:
          enableMetrics: true
    # ...
    ```

    Depending on the deployment mode of the OpenTelemetry Collector, the internal metrics are scraped by using `PodMonitors` or `ServiceMonitors`.

    > [!NOTE]
    > Alternatively, if you do not set the `enableMetrics` field to `true`, you can access the metrics endpoint at `http://localhost:8888/metrics`.

4.  Optional: If the **User Workload Monitoring** feature is enabled in the web console, go to **Observe** → **Dashboards** in the web console, and then select the **OpenTelemetry Collector** dashboard from the drop-down list to view it. For more information about the **User Workload Monitoring** feature, see "Enabling monitoring for user-defined projects" in *Monitoring*.

    > [!TIP]
    > You can filter the visualized data such as spans or metrics by the Collector instance, namespace, or OpenTelemetry components such as processors, receivers, or exporters.

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Enabling monitoring for user-defined projects](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.21/html/configuring_user_workload_monitoring/preparing-to-configure-the-monitoring-stack-uwm#enabling-monitoring-for-user-defined-projects-uwm_preparing-to-configure-the-monitoring-stack-uwm)

</div>

# Debug Exporter

You can configure the Debug Exporter to export the collected data to the standard output.

<div>

<div class="title">

Procedure

</div>

1.  Configure the `OpenTelemetryCollector` custom resource as follows:

    ``` yaml
      config:
        exporters:
          debug:
            verbosity: detailed
        service:
          pipelines:
            traces:
              exporters: [debug]
            metrics:
              exporters: [debug]
            logs:
              exporters: [debug]
    ```

2.  Use the `oc logs` command or the web console to export the logs to the standard output.

</div>

# Disabling network policies

The Red Hat build of OpenTelemetry Operator creates network policies to control the traffic for the Operator and operands to improve security. By default, the network policies are enabled and configured to allow traffic to all the required components. No additional configuration is needed.

If you are experiencing traffic issues for the OpenTelemetry Collector or its Target Allocator component, the problem might be caused by the default network policy configuration. You can disable network policies for the OpenTelemetry Collector to troubleshoot the issue.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a cluster administrator with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Disable the network policy for the OpenTelemetry Collector by configuring the `OpenTelemetryCollector` custom resource (CR):

  ``` yaml
  apiVersion: opentelemetry.io/v1beta1
  kind: OpenTelemetryCollector
  metadata:
    name: otel
    namespace: observability
  spec:
    networkPolicy:
      enabled: false
    # ...
  ```

  - Specify whether to enable network policies by setting `networkPolicy.enabled` to `true` (default) or `false`. Setting it to `false` disables the creation of network policies.

</div>

# Using the Network Observability Operator for troubleshooting

You can debug the traffic between your observability components by visualizing it with the Network Observability Operator.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Network Observability Operator as explained in "Installing the Network Observability Operator".

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, go to **Observe** → **Network Traffic** → **Topology**.

2.  Select **Namespace** to filter the workloads by the namespace in which your OpenTelemetry Collector is deployed.

3.  Use the network traffic visuals to troubleshoot possible issues. See "Observing the network traffic from the Topology view" for more details.

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Installing the Network Observability Operator](../../observability/network_observability/installing-operators.xml#installing-network-observability-operators)

- [Observing the network traffic from the Topology view](../../observability/network_observability/observing-network-traffic.xml#nw-observe-network-traffic)

</div>

# Troubleshooting the instrumentation

To troubleshoot the instrumentation, look for any of the following issues:

- Issues with instrumentation injection into your workload

- Issues with data generation by the instrumentation libraries

## Troubleshooting instrumentation injection into your workload

To troubleshoot instrumentation injection, you can perform the following activities:

- Checking if the `Instrumentation` object was created

- Checking if the init-container started

- Checking if the resources were deployed in the correct order

- Searching for errors in the Operator logs

- Double-checking the pod annotations

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to verify that the `Instrumentation` object was successfully created:

    ``` terminal
    $ oc get instrumentation -n <workload_project>
    ```

    - The namespace where the instrumentation was created.

2.  Run the following command to verify that the `opentelemetry-auto-instrumentation` init-container successfully started, which is a prerequisite for instrumentation injection into workloads:

    ``` terminal
    $ oc get events -n <workload_project>
    ```

    - The namespace where the instrumentation is injected for workloads.

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      ... Created container opentelemetry-auto-instrumentation
      ... Started container opentelemetry-auto-instrumentation
      ```

      </div>

3.  Verify that the resources were deployed in the correct order for the auto-instrumentation to work correctly. The correct order is to deploy the `Instrumentation` custom resource (CR) before the application. For information about the `Instrumentation` CR, see the section "Configuring the instrumentation".

    > [!NOTE]
    > When the pod starts, the Red Hat build of OpenTelemetry Operator checks the `Instrumentation` CR for annotations containing instructions for injecting auto-instrumentation. Generally, the Operator then adds an init-container to the application’s pod that injects the auto-instrumentation and environment variables into the application’s container. If the `Instrumentation` CR is not available to the Operator when the application is deployed, the Operator is unable to inject the auto-instrumentation.

    Fixing the order of deployment requires the following steps:

    1.  Update the instrumentation settings.

    2.  Delete the instrumentation object.

    3.  Redeploy the application.

4.  Run the following command to inspect the Operator logs for instrumentation errors:

    ``` terminal
    $ oc logs -l app.kubernetes.io/name=opentelemetry-operator --container manager -n openshift-opentelemetry-operator --follow
    ```

5.  Troubleshoot pod annotations for the instrumentations for a specific programming language. See the required annotation fields and values in "Configuring the instrumentation".

    1.  Verify that the application pods that you are instrumenting are labeled with correct annotations and the appropriate auto-instrumentation settings have been applied.

        <div class="formalpara">

        <div class="title">

        Example

        </div>

            instrumentation.opentelemetry.io/inject-python="true"

        </div>

        <div class="formalpara">

        <div class="title">

        Example command to get pod annotations for an instrumented Python application

        </div>

        ``` terminal
        $ oc get pods -n <workload_project> -o jsonpath='{range .items[?(@.metadata.annotations["instrumentation.opentelemetry.io/inject-python"]=="true")]}{.metadata.name}{"\n"}{end}'
        ```

        </div>

    2.  Verify that the annotation applied to the instrumentation object is correct for the programming language that you are instrumenting.

    3.  If there are multiple instrumentations in the same namespace, specify the name of the `Instrumentation` object in their annotations.

        <div class="formalpara">

        <div class="title">

        Example

        </div>

            instrumentation.opentelemetry.io/inject-nodejs: "<instrumentation_object>"

        </div>

    4.  If the `Instrumentation` object is in a different namespace, specify the namespace in the annotation.

        <div class="formalpara">

        <div class="title">

        Example

        </div>

            instrumentation.opentelemetry.io/inject-nodejs: "<other_namespace>/<instrumentation_object>"

        </div>

    5.  Verify that the `OpenTelemetryCollector` custom resource specifies the auto-instrumentation annotations under `spec.template.metadata.annotations`. If the auto-instrumentation annotations are in `spec.metadata.annotations` instead, move them into `spec.template.metadata.annotations`.

</div>

## Troubleshooting telemetry data generation by the instrumentation libraries

You can troubleshoot telemetry data generation by the instrumentation libraries by checking the endpoint, looking for errors in your application logs, and verifying that the Collector is receiving the telemetry data.

<div>

<div class="title">

Procedure

</div>

1.  Verify that the instrumentation is transmitting data to the correct endpoint:

    ``` terminal
    $ oc get instrumentation <instrumentation_name> -n <workload_project> -o jsonpath='{.spec.endpoint}'
    ```

    The default endpoint `http://localhost:4317` for the `Instrumentation` object is only applicable to a Collector instance that is deployed as a sidecar in your application pod. If you are using an incorrect endpoint, correct it by editing the `Instrumentation` object and redeploying your application.

2.  Inspect your application logs for error messages that might indicate that the instrumentation is malfunctioning:

    ``` terminal
    $ oc logs <application_pod> -n <workload_project>
    ```

3.  If the application logs contain error messages that indicate that the instrumentation might be malfunctioning, install the OpenTelemetry SDK and libraries locally. Then run your application locally and troubleshoot for issues between the instrumentation libraries and your application without OpenShift Container Platform.

4.  Use the Debug Exporter to verify that the telemetry data is reaching the destination OpenTelemetry Collector instance. For more information, see "Debug Exporter".

</div>
