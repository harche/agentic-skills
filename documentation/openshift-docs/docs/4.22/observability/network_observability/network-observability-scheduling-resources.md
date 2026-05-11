<div wrapper="1" role="_abstract">

Taints and tolerations help you control which nodes host certain pods. Use these tools, along with node selectors, to guide the placement of network observability components.

</div>

A node selector specifies a map of key/value pairs that are defined using custom labels on nodes and selectors specified in pods.

For the pod to be eligible to run on a node, the pod must have the same key/value node selector as the label on the node.

# Network observability deployment in specific nodes

<div wrapper="1" role="_abstract">

Configure the `FlowCollector` resource using scheduling specifications, including `NodeSelector`, `Tolerations`, and `Affinity`, to control the deployment of network observability components on specific nodes.

</div>

The `spec.agent.ebpf.advanced.scheduling`, `spec.processor.advanced.scheduling`, and `spec.consolePlugin.advanced.scheduling` specifications have the following configurable settings:

- `NodeSelector`

- `Tolerations`

- `Affinity`

- `PriorityClassName`

<div class="formalpara">

<div class="title">

Sample `FlowCollector` resource for `spec.<component>.advanced.scheduling`

</div>

``` yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
# ...
advanced:
  scheduling:
    tolerations:
    - key: "<taint key>"
      operator: "Equal"
      value: "<taint value>"
      effect: "<taint effect>"
      nodeSelector:
        <key>: <value>
      affinity:
        nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: name
              operator: In
              values:
              - app-worker-node
      priorityClassName: """
# ...
```

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Understanding taints and tolerations](../../nodes/scheduling/nodes-scheduler-taints-tolerations.xml#nodes-scheduler-taints-tolerations-about_nodes-scheduler-taints-tolerations)

- [Assign Pods to Nodes (Kubernetes documentation)](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)

- [Pod Priority and Preemption (Kubernetes documentation)](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass)

</div>
