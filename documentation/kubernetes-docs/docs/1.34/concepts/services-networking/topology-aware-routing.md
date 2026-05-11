# Topology Aware Routing

*Topology Aware Routing* provides a mechanism to help keep network traffic within the zone where it originated. Preferring same-zone traffic between Pods in your cluster can help with reliability, performance (network latency and throughput), or cost.

FEATURE STATE:
`Kubernetes v1.23 [beta]`

> **Note:**
> Prior to Kubernetes 1.27, this feature was known as *Topology Aware Hints*.

*Topology Aware Routing* adjusts routing behavior to prefer keeping traffic in
the zone it originated from. In some cases this can help reduce costs or improve
network performance.

## Motivation

Kubernetes clusters are increasingly deployed in multi-zone environments.
*Topology Aware Routing* provides a mechanism to help keep traffic within the
zone it originated from. When calculating the endpoints for a [Service](/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service."), the EndpointSlice controller considers
the topology (region and zone) of each endpoint and populates the hints field to
allocate it to a zone. Cluster components such as [kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/ "kube-proxy is a network proxy that runs on each node in the cluster.") can then consume those hints, and use
them to influence how the traffic is routed (favoring topologically closer
endpoints).

## Enabling Topology Aware Routing

> **Note:**
> Prior to Kubernetes 1.27, this behavior was controlled using the
> `service.kubernetes.io/topology-aware-hints` annotation.

You can enable Topology Aware Routing for a Service by setting the
`service.kubernetes.io/topology-mode` annotation to `Auto`. When there are
enough endpoints available in each zone, Topology Hints will be populated on
EndpointSlices to allocate individual endpoints to specific zones, resulting in
traffic being routed closer to where it originated from.

## When it works best

This feature works best when:

### 1. Incoming traffic is evenly distributed

If a large proportion of traffic is originating from a single zone, that traffic
could overload the subset of endpoints that have been allocated to that zone.
This feature is not recommended when incoming traffic is expected to originate
from a single zone.

### 2. The Service has 3 or more endpoints per zone

In a three zone cluster, this means 9 or more endpoints. If there are fewer than
3 endpoints per zone, there is a high (≈50%) probability that the EndpointSlice
controller will not be able to allocate endpoints evenly and instead will fall
back to the default cluster-wide routing approach.

## How It Works

The "Auto" heuristic attempts to proportionally allocate a number of endpoints
to each zone. Note that this heuristic works best for Services that have a
significant number of endpoints.

### EndpointSlice controller

The EndpointSlice controller is responsible for setting hints on EndpointSlices
when this heuristic is enabled. The controller allocates a proportional amount of
endpoints to each zone. This proportion is based on the
[allocatable](/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable)
CPU cores for nodes running in that zone. For example, if one zone had 2 CPU
cores and another zone only had 1 CPU core, the controller would allocate twice
as many endpoints to the zone with 2 CPU cores.

The following example shows what an EndpointSlice looks like when hints have
been populated:

```
apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: example-hints
  labels:
    kubernetes.io/service-name: example-svc
addressType: IPv4
ports:
  - name: http
    protocol: TCP
    port: 80
endpoints:
  - addresses:
      - "10.1.2.3"
    conditions:
      ready: true
    hostname: pod-1
    zone: zone-a
    hints:
      forZones:
        - name: "zone-a"
```

### kube-proxy

The kube-proxy component filters the endpoints it routes to based on the hints set by
the EndpointSlice controller. In most cases, this means that the kube-proxy is able
to route traffic to endpoints in the same zone. Sometimes the controller allocates endpoints
from a different zone to ensure more even distribution of endpoints between zones.
This would result in some traffic being routed to other zones.

## Safeguards

The Kubernetes control plane and the kube-proxy on each node apply some
safeguard rules before using Topology Aware Hints. If these don't check out,
the kube-proxy selects endpoints from anywhere in your cluster, regardless of the
zone.

1. **Insufficient number of endpoints:** If there are less endpoints than zones
   in a cluster, the controller will not assign any hints.
2. **Impossible to achieve balanced allocation:** In some cases, it will be
   impossible to achieve a balanced allocation of endpoints among zones. For
   example, if zone-a is twice as large as zone-b, but there are only 2
   endpoints, an endpoint allocated to zone-a may receive twice as much traffic
   as zone-b. The controller does not assign hints if it can't get this "expected
   overload" value below an acceptable threshold for each zone. Importantly this
   is not based on real-time feedback. It is still possible for individual
   endpoints to become overloaded.
3. **One or more Nodes has insufficient information:** If any node does not have
   a `topology.kubernetes.io/zone` label or is not reporting a value for
   allocatable CPU, the control plane does not set any topology-aware endpoint
   hints and so kube-proxy does not filter endpoints by zone.
4. **One or more endpoints does not have a zone hint:** When this happens,
   the kube-proxy assumes that a transition from or to Topology Aware Hints is
   underway. Filtering endpoints for a Service in this state would be dangerous
   so the kube-proxy falls back to using all endpoints.
5. **A zone is not represented in hints:** If the kube-proxy is unable to find
   at least one endpoint with a hint targeting the zone it is running in, it falls
   back to using endpoints from all zones. This is most likely to happen as you add
   a new zone into your existing cluster.

## Constraints

* Topology Aware Hints are not used when `internalTrafficPolicy` is set to `Local`
  on a Service. It is possible to use both features in the same cluster on different
  Services, just not on the same Service.
* This approach will not work well for Services that have a large proportion of
  traffic originating from a subset of zones. Instead this assumes that incoming
  traffic will be roughly proportional to the capacity of the Nodes in each
  zone.
* The EndpointSlice controller ignores unready nodes as it calculates the
  proportions of each zone. This could have unintended consequences if a large
  portion of nodes are unready.
* The EndpointSlice controller ignores nodes with the
  `node-role.kubernetes.io/control-plane` or `node-role.kubernetes.io/master`
  label set. This could be problematic if workloads are also running on those
  nodes.
* The EndpointSlice controller does not take into account [tolerations](/docs/concepts/scheduling-eviction/taint-and-toleration/ "A core object consisting of three required properties: key, value, and effect. Tolerations enable the scheduling of pods on nodes or node groups that have a matching taint.") when deploying or calculating the
  proportions of each zone. If the Pods backing a Service are limited to a
  subset of Nodes in the cluster, this will not be taken into account.
* This may not work well with autoscaling. For example, if a lot of traffic is
  originating from a single zone, only the endpoints allocated to that zone will
  be handling that traffic. That could result in [Horizontal Pod Autoscaler](/docs/tasks/run-application/horizontal-pod-autoscale/ "Object that automatically scales the number of pod replicas based on targeted resource utilization or custom metric targets.")
  either not picking up on this event, or newly added pods starting in a
  different zone.

## Custom heuristics

Kubernetes is deployed in many different ways, there is no single heuristic for
allocating endpoints to zones will work for every use case. A key goal of this
feature is to enable custom heuristics to be developed if the built in heuristic
does not work for your use case. The first steps to enable custom heuristics
were included in the 1.27 release. This is a limited implementation that may not
yet cover some relevant and plausible situations.

## What's next

* Follow the [Connecting Applications with Services](/docs/tutorials/services/connect-applications-service/) tutorial
* Learn about the
  [trafficDistribution](/docs/concepts/services-networking/service/#traffic-distribution)
  field, which is closely related to the `service.kubernetes.io/topology-mode`
  annotation and provides flexible options for traffic routing within
  Kubernetes.

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
