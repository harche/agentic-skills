This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/tutorials/).

# Tutorials

* 1: [Hello Minikube](#pg-5e3051fff9e84735871d9fb5e7b93f33)
* 2: [Learn Kubernetes Basics](#pg-058fd6f16ab24cfdea90f9f3a8e38a52)

+ 2.1: [Create a Cluster](#pg-7df66040311338d6098ebeab43ba9afb)

- 2.1.1: [Using Minikube to Create a Cluster](#pg-7504b651f82e9be0608d9333b22fd510)

+ 2.2: [Deploy an App](#pg-76d78b3fba507f7ed33cef14a35b631d)

- 2.2.1: [Using kubectl to Create a Deployment](#pg-c25ede4d5765ac3754880e57201fed09)

+ 2.3: [Explore Your App](#pg-250d620a73ec8be7e1f7d835574c4596)

- 2.3.1: [Viewing Pods and Nodes](#pg-313d88a4a9dfd0081258b7e678927895)

+ 2.4: [Expose Your App Publicly](#pg-4b0e31c9e0eae68bbb0a358b4042ada9)

- 2.4.1: [Using a Service to Expose Your App](#pg-d800561759ec98c182a096c480b7f148)

+ 2.5: [Scale Your App](#pg-be4996c93fb39c459a30b6669569d423)

- 2.5.1: [Running Multiple Instances of Your App](#pg-b85f668d0b569a6b09dd15ca5c709b63)

+ 2.6: [Update Your App](#pg-62b8b17dadfb55f1801cf8439e944e58)

- 2.6.1: [Performing a Rolling Update](#pg-53ee0e1ff68c4d10d6fd07600b80e6fe)

* 3: [Configuration](#pg-a3a0f1c6af19fc89ce24d8cd42c0249f)

+ 3.1: [Updating Configuration via a ConfigMap](#pg-b8268dd408000835b485de3a4f3343ab)
+ 3.2: [Configuring Redis using a ConfigMap](#pg-2efe621cc085b350c8c4574e6f7f1311)
+ 3.3: [Adopting Sidecar Containers](#pg-f7dcafe033a10939f2a0291617626575)

* 4: [Security](#pg-fe7e92bed8fb92872b139f12c4568cdb)

+ 4.1: [Apply Pod Security Standards at the Cluster Level](#pg-d5f847bcdb6f7efbfc9c8a180d73e29a)
+ 4.2: [Apply Pod Security Standards at the Namespace Level](#pg-31a6c137cfc5bfea9d88f4b109109465)
+ 4.3: [Restrict a Container's Access to Resources with AppArmor](#pg-fca078b8ac6b82352ed52187a2da91b7)
+ 4.4: [Restrict a Container's Syscalls with seccomp](#pg-8b105172a11322c70d0223bc9dff1904)

* 5: [Stateless Applications](#pg-1efbbc2c3015389f835b1661d5effb29)

+ 5.1: [Exposing an External IP Address to Access an Application in a Cluster](#pg-62caf420877232190a7404b8d93c6724)
+ 5.2: [Example: Deploying PHP Guestbook application with Redis](#pg-8c56795c6614cc5f52434ecc756448ac)

* 6: [Stateful Applications](#pg-d6336d9712aa433eb5f0fb8cbed6bef7)

+ 6.1: [StatefulSet Basics](#pg-42e39658021b706bcc9478c8cc73c4a3)
+ 6.2: [Example: Deploying WordPress and MySQL with Persistent Volumes](#pg-27580b3f65f3c2da07fc0f83be69da75)
+ 6.3: [Example: Deploying Cassandra with a StatefulSet](#pg-bf0d8e08fddd6e0282709b9fef8b5f67)
+ 6.4: [Running ZooKeeper, A Distributed System Coordinator](#pg-4bfac214b5eb9ebddaf1f3811901d327)

* 7: [Cluster Management](#pg-f4c0cdc5efc0b99d834a7ed2753ed1eb)

+ 7.1: [Running Kubelet in Standalone Mode](#pg-d4134e0b428e3d8466977e543f95303d)
+ 7.2: [Configuring swap memory on Kubernetes nodes](#pg-fc63f6eff8e2eb9b04591cb44af2cc01)
+ 7.3: [Install Drivers and Allocate Devices with DRA](#pg-73e6722f9775407ddbc0fb86de62a184)
+ 7.4: [Namespaces Walkthrough](#pg-8cf61420856e8d9c10e7144b22ad0532)

* 8: [Services](#pg-97489f0aa8ac2df31a0d6b444a7bde62)

+ 8.1: [Connecting Applications with Services](#pg-bc0a2760d2865e91c501bc2467cd1a4b)
+ 8.2: [Using Source IP](#pg-5642e8c51749e4fe2e6a2ccc207f1fab)
+ 8.3: [Explore Termination Behavior for Pods And Their Endpoints](#pg-3cecc68ef365a9d2ee0b4860dc74cacc)

This section of the Kubernetes documentation contains tutorials.
A tutorial shows how to accomplish a goal that is larger than a single
[task](/docs/tasks/). Typically a tutorial has several sections,
each of which has a sequence of steps.
Before walking through each tutorial, you may want to bookmark the
[Standardized Glossary](/docs/reference/glossary/) page for later references.

## Basics

* [Kubernetes Basics](/docs/tutorials/kubernetes-basics/) is an in-depth interactive tutorial that helps you understand the Kubernetes system and try out some basic Kubernetes features.
* [Introduction to Kubernetes (edX)](https://www.edx.org/course/introduction-kubernetes-linuxfoundationx-lfs158x)
* [Hello Minikube](/docs/tutorials/hello-minikube/)

## Configuration

* [Configuring Redis Using a ConfigMap](/docs/tutorials/configuration/configure-redis-using-configmap/)

## Authoring Pods

* [Adopting Sidecar Containers](/docs/tutorials/configuration/pod-sidecar-containers/)

## Stateless Applications

* [Exposing an External IP Address to Access an Application in a Cluster](/docs/tutorials/stateless-application/expose-external-ip-address/)
* [Example: Deploying PHP Guestbook application with Redis](/docs/tutorials/stateless-application/guestbook/)

## Stateful Applications

* [StatefulSet Basics](/docs/tutorials/stateful-application/basic-stateful-set/)
* [Example: WordPress and MySQL with Persistent Volumes](/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/)
* [Example: Deploying Cassandra with Stateful Sets](/docs/tutorials/stateful-application/cassandra/)
* [Running ZooKeeper, A CP Distributed System](/docs/tutorials/stateful-application/zookeeper/)

## Services

* [Connecting Applications with Services](/docs/tutorials/services/connect-applications-service/)
* [Using Source IP](/docs/tutorials/services/source-ip/)

## Security

* [Apply Pod Security Standards at Cluster level](/docs/tutorials/security/cluster-level-pss/)
* [Apply Pod Security Standards at Namespace level](/docs/tutorials/security/ns-level-pss/)
* [Restrict a Container's Access to Resources with AppArmor](/docs/tutorials/security/apparmor/)
* [Seccomp](/docs/tutorials/security/seccomp/)

## Cluster Management

* [Configuring Swap Memory on Kubernetes Nodes](/docs/tutorials/cluster-management/provision-swap-memory/)
* [Running Kubelet in Standalone Mode](/docs/tutorials/cluster-management/kubelet-standalone/)
* [Install Drivers and Allocate Devices with DRA](/docs/tutorials/cluster-management/install-use-dra/)

## What's next

If you would like to write a tutorial, see
[Content Page Types](/docs/contribute/style/page-content-types/)
for information about the tutorial page type.
