This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/setup/).

# Getting started

* 1: [Learning environment](#pg-0b597086a9d1382f86abadcfeab657d6)

* 2: [Production environment](#pg-4e14853fdaa3bd273f31a60112b9b5ac)

+ 2.1: [Container Runtimes](#pg-a77d3feb6e6d9978f32fa14622642e9a)
+ 2.2: [Installing Kubernetes with deployment tools](#pg-00e1646f68aeb89f9722cf6f6cfcad94)

- 2.2.1: [Bootstrapping clusters with kubeadm](#pg-a16f59f325a17cdeed324d5c889f7f73)

* 2.2.1.1: [Installing kubeadm](#pg-29e59491dd6118b23072dfe9ebb93323)
* 2.2.1.2: [Troubleshooting kubeadm](#pg-c3689df4b0c61a998e79d91a865aa244)
* 2.2.1.3: [Creating a cluster with kubeadm](#pg-134ed1f6142a98e6ac681a1ba4920e53)
* 2.2.1.4: [Customizing components with the kubeadm API](#pg-4c656c5eda3e1c06ad1aedebdc04a211)
* 2.2.1.5: [Options for Highly Available Topology](#pg-015edbc7cc688d31b1d1edce7c186135)
* 2.2.1.6: [Creating Highly Available Clusters with kubeadm](#pg-3941d5c3409342219bf7e03128b8ecb6)
* 2.2.1.7: [Set up a High Availability etcd Cluster with kubeadm](#pg-8160424c22d24f7d2d63c521e107dbf8)
* 2.2.1.8: [Configuring each kubelet in your cluster using kubeadm](#pg-07709e71de6b4ac2573041c31213dbeb)
* 2.2.1.9: [Dual-stack support with kubeadm](#pg-df2f3f20d404ebe2b03fcda1fcee50e7)

+ 2.3: [Turnkey Cloud Solutions](#pg-d2f55eefe7222b7c637875af9c3ec199)

* 3: [Best practices](#pg-84b6491601d6a2b3da4cd5a105c866ba)

+ 3.1: [Considerations for large clusters](#pg-c797ee17120176c685455db89ae091a9)
+ 3.2: [Running in multiple zones](#pg-970615c97499e3651fd3a98e0387cefc)
+ 3.3: [Validate node setup](#pg-f89867de1d34943f1524f67a241f5cc9)
+ 3.4: [Enforcing Pod Security Standards](#pg-92a61cf5b0575aa3500f7665b68127d1)
+ 3.5: [PKI certificates and requirements](#pg-0394f813094b7a35058dffe5b8bacd20)

This section lists the different ways to set up and run Kubernetes.
When you install Kubernetes, choose an installation type based on: ease of maintenance, security,
control, available resources, and expertise required to operate and manage a cluster.

You can [download Kubernetes](/releases/download/) to deploy a Kubernetes cluster
on a local machine, into the cloud, or for your own datacenter.

Several [Kubernetes components](/docs/concepts/overview/components/) such as [kube-apiserver](/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API.") or [kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/ "kube-proxy is a network proxy that runs on each node in the cluster.") can also be
deployed as [container images](/releases/download/#container-images) within the cluster.

It is **recommended** to run Kubernetes components as container images wherever
that is possible, and to have Kubernetes manage those components.
Components that run containers - notably, the kubelet - can't be included in this category.

If you don't want to manage a Kubernetes cluster yourself, you could pick a managed service, including
[certified platforms](/docs/setup/production-environment/turnkey-solutions/).
There are also other standardized and custom solutions across a wide range of cloud and
bare metal environments.

## Learning environment

If you're learning Kubernetes, use the tools supported by the Kubernetes community,
or tools in the ecosystem to set up a Kubernetes cluster on a local machine.
See [Install tools](/docs/tasks/tools/).

## Production environment

When evaluating a solution for a
[production environment](/docs/setup/production-environment/), consider which aspects of
operating a Kubernetes cluster (or *abstractions*) you want to manage yourself and which you
prefer to hand off to a provider.

For a cluster you're managing yourself, the officially supported tool
for deploying Kubernetes is [kubeadm](/docs/setup/production-environment/tools/kubeadm/).

## What's next

* [Download Kubernetes](/releases/download/)
* Download and [install tools](/docs/tasks/tools/) including `kubectl`
* Select a [container runtime](/docs/setup/production-environment/container-runtimes/) for your new cluster
* Learn about [best practices](/docs/setup/best-practices/) for cluster setup

Kubernetes is designed for its [control plane](/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.") to
run on Linux. Within your cluster you can run applications on Linux or other operating systems, including
Windows.

* Learn to [set up clusters with Windows nodes](/docs/concepts/windows/)
