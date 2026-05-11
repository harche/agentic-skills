This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/concepts/services-networking/).

# Services, Load Balancing, and Networking

Concepts and resources behind networking in Kubernetes.

* 1: [Service](#pg-5701136fd2ce258047b6ddc389112352)
* 2: [Ingress](#pg-199bcc92443dbc9bed44819467d7eb75)
* 3: [Ingress Controllers](#pg-5a8edeb1f2dc8e38cd6d561bb08b0d78)
* 4: [Gateway API](#pg-253904bd7754b4c2b34c262f42175a50)
* 5: [EndpointSlices](#pg-f51db1097575de8072afe1f5b156a70c)
* 6: [Network Policies](#pg-ded1daafdcd293023ee333728007ca61)
* 7: [DNS for Services and Pods](#pg-91cb8a4438b003df11bc1c426a81b756)
* 8: [IPv4/IPv6 dual-stack](#pg-21f8d19c60c33914baab66224c3d46a7)
* 9: [Topology Aware Routing](#pg-8df2ab57df3ee82a73ffaada69bcd178)
* 10: [Networking on Windows](#pg-9092684b3a27432bc9041d56b7a4a8ba)
* 11: [Service ClusterIP allocation](#pg-439738e82e994f627155bff468d35404)
* 12: [Service Internal Traffic Policy](#pg-cd7657b1056ad32451974db57a951ba5)

## The Kubernetes network model

The Kubernetes network model is built out of several pieces:

* Each [pod](/docs/concepts/workloads/pods/) in a cluster gets its
  own unique cluster-wide IP address.

  + A pod has its own private network namespace which is shared by
    all of the containers within the pod. Processes running in
    different containers in the same pod can communicate with each
    other over `localhost`.
* The *pod network* (also called a cluster network) handles communication
  between pods. It ensures that (barring intentional network segmentation):

  + All pods can communicate with all other pods, whether they are
    on the same [node](/docs/concepts/architecture/nodes/) or on
    different nodes. Pods can communicate with each other
    directly, without the use of proxies or address translation (NAT).

    On Windows, this rule does not apply to host-network pods.
  + Agents on a node (such as system daemons, or kubelet) can
    communicate with all pods on that node.
* The [Service](/docs/concepts/services-networking/service/) API
  lets you provide a stable (long lived) IP address or hostname for a service implemented
  by one or more backend pods, where the individual pods making up
  the service can change over time.

  + Kubernetes automatically manages
    [EndpointSlice](/docs/concepts/services-networking/endpoint-slices/)
    objects to provide information about the pods currently backing a Service.
  + A service proxy implementation monitors the set of Service and
    EndpointSlice objects, and programs the data plane to route
    service traffic to its backends, by using operating system or
    cloud provider APIs to intercept or rewrite packets.
* The [Gateway](/docs/concepts/services-networking/gateway/) API
  (or its predecessor, [Ingress](/docs/concepts/services-networking/ingress/))
  allows you to make Services accessible to clients that are outside the cluster.

  + A simpler, but less-configurable, mechanism for cluster
    ingress is available via the Service API's
    [`type: LoadBalancer`](/docs/concepts/services-networking/service/#loadbalancer),
    when using a supported [Cloud Provider](/docs/reference/glossary/?all=true#term-cloud-provider "An organization that offers a cloud computing platform.").
* [NetworkPolicy](/docs/concepts/services-networking/network-policies/) is a built-in
  Kubernetes API that allows you to control traffic between pods, or between pods and
  the outside world.

In older container systems, there was no automatic connectivity
between containers on different hosts, and so it was often necessary
to explicitly create links between containers, or to map container
ports to host ports to make them reachable by containers on other
hosts. This is not needed in Kubernetes; Kubernetes's model is that
pods can be treated much like VMs or physical hosts from the
perspectives of port allocation, naming, service discovery, load
balancing, application configuration, and migration.

Only a few parts of this model are implemented by Kubernetes itself.
For the other parts, Kubernetes defines the APIs, but the
corresponding functionality is provided by external components, some
of which are optional:

* Pod network namespace setup is handled by system-level software implementing the
  [Container Runtime Interface](/docs/concepts/containers/cri/).
* The pod network itself is managed by a
  [pod network implementation](/docs/concepts/cluster-administration/addons/#networking-and-network-policy).
  On Linux, most container runtimes use the
  [Container Networking Interface (CNI)](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/ "Container network interface (CNI) plugins are a type of Network plugin that adheres to the appc/CNI specification.")
  to interact with the pod network implementation, so these
  implementations are often called *CNI plugins*.
* Kubernetes provides a default implementation of service proxying,
  called [kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/ "kube-proxy is a network proxy that runs on each node in the cluster."), but some pod
  network implementations instead use their own service proxy that
  is more tightly integrated with the rest of the implementation.
* NetworkPolicy is generally also implemented by the pod network
  implementation. (Some simpler pod network implementations don't
  implement NetworkPolicy, or an administrator may choose to
  configure the pod network without NetworkPolicy support. In these
  cases, the API will still be present, but it will have no effect.)
* There are many [implementations of the Gateway API](https://gateway-api.sigs.k8s.io/implementations/),
  some of which are specific to particular cloud environments, some more
  focused on "bare metal" environments, and others more generic.

## What's next

The [Connecting Applications with Services](/docs/tutorials/services/connect-applications-service/)
tutorial lets you learn about Services and Kubernetes networking with a hands-on example.

[Cluster Networking](/docs/concepts/cluster-administration/networking/) explains how to set
up networking for your cluster, and also provides an overview of the technologies involved.
