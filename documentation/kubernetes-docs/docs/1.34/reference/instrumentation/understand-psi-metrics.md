# Understand Pressure Stall Information (PSI) Metrics

Detailed explanation of Pressure Stall Information (PSI) metrics and how to use them to identify resource pressure in Kubernetes.

FEATURE STATE:
`Kubernetes v1.34 [beta]`

As a beta feature, Kubernetes lets you configure the kubelet to collect Linux kernel
[Pressure Stall Information](https://docs.kernel.org/accounting/psi.html)
(PSI) for CPU, memory, and I/O usage. The information is collected at node, pod and container level.
This feature is enabled by default by setting the `KubeletPSI` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/).

PSI metrics are exposed through two different sources:

* The kubelet's [Summary API](/docs/reference/config-api/kubelet-stats.v1alpha1/), which provides PSI data at the node, pod, and container level.
* The `/metrics/cadvisor` endpoint on the kubelet, which exposes PSI metrics in the [Prometheus format](/docs/concepts/cluster-administration/system-metrics/#psi-metrics).

### Requirements

Pressure Stall Information requires the following on your Linux nodes:

* The Linux kernel must be version **4.20 or newer**.
* The kernel must be compiled with the `CONFIG_PSI=y` option. Most modern distributions enable this by default. You can check your kernel's configuration by running `zgrep CONFIG_PSI /proc/config.gz`.
* Some Linux distributions may compile PSI into the kernel but disable it by default. If so, you need to enable it at boot time by adding the `psi=1` parameter to the kernel command line.
* The node must be using [cgroup v2](/docs/concepts/architecture/cgroups/).

## Understanding PSI Metrics

Pressure Stall Information (PSI) metrics are provided for three resources: CPU, memory, and I/O. They are categorized into two main types of pressure: `some` and `full`.

* **`some`**: This value indicates that some tasks (one or more) are stalled on a resource. For example, if some tasks are waiting for I/O, this metric will increase. This can be an early indicator of resource contention.
* **`full`**: This value indicates that *all* non-idle tasks are stalled on a resource simultaneously. This signifies a more severe resource shortage, where the entire system is unable to make progress.

Each pressure type provides four metrics: `avg10`, `avg60`, `avg300`, and `total`. The `avg` values represent the percentage of wall-clock time that tasks were stalled over 10-second, 60-second, and 3-minute moving averages. The `total` value is a cumulative counter in microseconds showing the total time tasks have been stalled.

## Example Scenarios

You can use a simple Pod with a stress-testing tool to generate resource pressure and observe the PSI metrics. The following examples use the `agnhost` container image, which includes the `stress` tool.

### Generating CPU Pressure

Create a Pod that generates CPU pressure using the `stress` utility. This workload will put a heavy load on one CPU core.

Create a file named `cpu-pressure-pod.yaml`:

```
apiVersion: v1
kind: Pod
metadata:
  name: cpu-pressure-pod
spec:
  restartPolicy: Never
  containers:
  - name: cpu-stress
    image: registry.k8s.io/e2e-test-images/agnhost:2.47
    args:
    - "stress"
    - "--cpus"
    - "1"
    resources:
      limits:
        cpu: "500m"
      requests:
        cpu: "500m"
```

Apply it to your cluster: `kubectl apply -f cpu-pressure-pod.yaml`

#### Observing CPU Pressure

After the Pod is running, you can observe the CPU pressure through either the Summary API or the Prometheus metrics endpoint.

**Using the Summary API:**

Watch the summary stats for your node. In a separate terminal, run:

```
# Replace <node-name> with the name of a node in your cluster
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/stats/summary" | jq '.pods[] | select(.podRef.name | contains("cpu-pressure-pod"))'
```

You will see the `some` PSI metrics for CPU increase in the summary API output. The `avg10` value for `some` pressure should rise above zero, indicating that tasks are spending time stalled on the CPU.

**Using the Prometheus metrics endpoint:**

Query the `/metrics/cadvisor` endpoint to see the `container_pressure_cpu_waiting_seconds_total` metric.

```
# Replace <node-name> with the name of the node where the pod is running
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/metrics/cadvisor" | \
    grep 'container_pressure_cpu_waiting_seconds_total{container="cpu-stress"'
```

The output should show an increasing value, indicating that the container is spending time stalled waiting for CPU resources.

#### Cleanup

Clean up the Pod when you are finished:

```
kubectl delete pod cpu-pressure-pod
```

### Generating Memory Pressure

This example creates a Pod that continuously writes to files in the container's writable layer, causing the kernel's page cache to grow and forcing memory reclamation, which generates pressure.

Create a file named `memory-pressure-pod.yaml`:

```
apiVersion: v1
kind: Pod
metadata:
  name: memory-pressure-pod
spec:
  restartPolicy: Never
  containers:
  - name: memory-stress
    image: registry.k8s.io/e2e-test-images/agnhost:2.47
    command: ["/bin/sh", "-c"]
    args:
    - "i=0; while true; do dd if=/dev/zero of=testfile.$i bs=1M count=50 &>/dev/null; i=$(((i+1)%5)); sleep 0.1; done"
    resources:
      limits:
        memory: "200M"
      requests:
        memory: "200M"
```

Apply it to your cluster: `kubectl apply -f memory-pressure-pod.yaml`

#### Observing Memory Pressure

**Using the Summary API:**

In the summary output, you will observe an increase in the `full` PSI metrics for memory, indicating that the system is under significant memory pressure.

```
# Replace <node-name> with the name of a node in your cluster
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/stats/summary" | jq '.pods[] | select(.podRef.name | contains("memory-pressure-pod"))'
```

**Using the Prometheus metrics endpoint:**

Query the `/metrics/cadvisor` endpoint to see the `container_pressure_memory_waiting_seconds_total` metric.

```
# Replace <node-name> with the name of the node where the pod is running
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/metrics/cadvisor" | \
    grep 'container_pressure_memory_waiting_seconds_total{container="memory-stress"'
```

In the output, you will observe an increasing value for the metric, indicating that the system is under significant memory pressure.

#### Cleanup

Clean up the Pod when you are finished:

```
kubectl delete pod memory-pressure-pod
```

### Generating I/O Pressure

This Pod generates I/O pressure by repeatedly writing a file to disk and using `sync` to flush the data from memory, which creates I/O stalls.

Create a file named `io-pressure-pod.yaml`:

```
apiVersion: v1
kind: Pod
metadata:
  name: io-pressure-pod
spec:
  restartPolicy: Never
  containers:
  - name: io-stress
    image: registry.k8s.io/e2e-test-images/agnhost:2.47
    command: ["/bin/sh", "-c"]
    args:
      - "while true; do dd if=/dev/zero of=testfile bs=1M count=128 &>/dev/null; sync; rm testfile &>/dev/null; done"
```

Apply this to your cluster: `kubectl apply -f io-pressure-pod.yaml`

#### Observing I/O Pressure

**Using the Summary API:**

You will see the `some` PSI metrics for I/O increase as the Pod continuously writes to disk.

```
# Replace <node-name> with the name of a node in your cluster
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/stats/summary" | jq '.pods[] | select(.podRef.name | contains("io-pressure-pod"))'
```

**Using the Prometheus metrics endpoint:**

Query the `/metrics/cadvisor` endpoint to see the `container_pressure_io_waiting_seconds_total` metric.

```
# Replace <node-name> with the name of the node where the pod is running
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/metrics/cadvisor" | \
    grep 'container_pressure_io_waiting_seconds_total{container="io-stress"'
```

You will see the metric's value increase as the Pod continuously writes to disk.

#### Cleanup

Clean up the Pod when you are finished:

```
kubectl delete pod io-pressure-pod
```

## What's next

The task pages for [Troubleshooting Clusters](/docs/tasks/debug/debug-cluster/) discuss
how to use a metrics pipeline that rely on these data.

## Feedback

Was this page helpful?

Yes
No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on
[Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes).
Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to
[report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io)
or
[suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

const yes = document.querySelector('.feedback--yes');
const no = document.querySelector('.feedback--no');
document.querySelectorAll('.feedback--link').forEach(link => {
link.href = link.href + window.location.pathname;
});
const sendFeedback = (value) => {
if (!gtag) { console.log('!gtag'); }
gtag('event', 'click', {
'event_category': 'Helpful',
'event_label': window.location.pathname,
value
});
};
const disableButtons = () => {
yes.disabled = true;
yes.classList.add('feedback--button__disabled');
no.disabled = true;
no.classList.add('feedback--button__disabled');
};
yes.addEventListener('click', () => {
sendFeedback(1);
disableButtons();
document.querySelector('.feedback--response').classList.remove('feedback--response__hidden');
});
no.addEventListener('click', () => {
sendFeedback(0);
disableButtons();
document.querySelector('.feedback--response').classList.remove('feedback--response__hidden');
});

Last modified April 23, 2026 at 2:12 AM PST: [Merge pull request #55450 from sayanchowdhury/update-release-1.34-hugo.toml (d1f313a)](https://github.com/kubernetes/website/commit/d1f313a65f45bd4882d05fe9b6bea162fa2fdc16)
