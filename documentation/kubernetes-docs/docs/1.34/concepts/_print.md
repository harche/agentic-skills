This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/concepts/).

# Concepts

* 1: [Overview](#pg-0554ac387412eaf4e6e89b2f847dacde)

+ 1.1: [Kubernetes Components](#pg-13b0f1dbe89228e3d76d2ac231e245f1)
+ 1.2: [Objects In Kubernetes](#pg-110f33530cf761140cb1dab536baef04)

- 1.2.1: [Kubernetes Object Management](#pg-6751db8ff5409476de8225d17d6c42dd)
- 1.2.2: [Object Names and IDs](#pg-f37749a83c2916b63279ea60f3cfe53e)
- 1.2.3: [Labels and Selectors](#pg-f1dec4557fb8ffbac9f11390aaaf9fa4)
- 1.2.4: [Namespaces](#pg-1127165f472b7181b9c1d5a0b187d620)
- 1.2.5: [Annotations](#pg-93cd7a1d4e1623e2bf01afc49a5af69c)
- 1.2.6: [Field Selectors](#pg-046c03090d47bc4b89b818dc645c3865)
- 1.2.7: [Finalizers](#pg-13ce5627ef1dc8cbb4530ed231cb7d38)
- 1.2.8: [Owners and Dependents](#pg-efaa7a58910b58892dafd50e3b43c93c)
- 1.2.9: [Recommended Labels](#pg-5dd62c6a4a481b4cf1ac50f6799eb581)

+ 1.3: [The Kubernetes API](#pg-0c745f42e623d2b70a53bc0e6db73d95)

* 2: [Cluster Architecture](#pg-2bf36ccd6b3dbeafecf87c39761b07c7)

+ 2.1: [Nodes](#pg-9ef2890698e773b6c0d24fd2c20146f5)
+ 2.2: [Communication between Nodes and the Control Plane](#pg-c0251def6da29b30afebfb04549f1703)
+ 2.3: [Controllers](#pg-ca8819042a505291540e831283da66df)
+ 2.4: [Leases](#pg-d5e64235fa89f107957072cd8a39e4c5)
+ 2.5: [Cloud Controller Manager](#pg-bc804b02614d67025b4c788f1ca87fbc)
+ 2.6: [About cgroup v2](#pg-c20ec7d296cc2c8668bb204c2af31180)
+ 2.7: [Kubernetes Self-Healing](#pg-f992b9b0f5b827e6fe522de5dde184cc)
+ 2.8: [Garbage Collection](#pg-44a2e2e592af0846101e970aff9243e5)
+ 2.9: [Mixed Version Proxy](#pg-93721154dcdc5837b4ff286b4d4202ea)

* 3: [Containers](#pg-a5f7383c83ab9eb9cd0e3c4c020b3ae6)

+ 3.1: [Images](#pg-16042b4652ad19e565c7263824029a43)
+ 3.2: [Container Environment](#pg-643212488f778acf04bebed65ba34441)
+ 3.3: [Runtime Class](#pg-a858027489648786a3b16264e451272b)
+ 3.4: [Container Lifecycle Hooks](#pg-e6941d969d81540208a3e78bc56f43bc)
+ 3.5: [Container Runtime Interface (CRI)](#pg-91a1e3e8127ccc7cf58937f1c5c1aea0)

* 4: [Workloads](#pg-d52aadda80edd9f8c514cfe2321363c2)

+ 4.1: [Pods](#pg-4d68b0ccf9c683e6368ffdcc40c838d4)

- 4.1.1: [Pod Lifecycle](#pg-c3c2b9cf30915ec9d46c147201da3332)
- 4.1.2: [Init Containers](#pg-1ccbd4eeded6ab138d98b59175bd557e)
- 4.1.3: [Sidecar Containers](#pg-31b32aaff870448be05e247a95c17a57)
- 4.1.4: [Ephemeral Containers](#pg-53a1005011e1bda2ce81819aad7c8b32)
- 4.1.5: [Disruptions](#pg-4aaf43c715cd764bc8ed4436f3537e68)
- 4.1.6: [Pod Hostname](#pg-268190c91963ce121c0de5a4894db118)
- 4.1.7: [Pod Quality of Service Classes](#pg-a77cbc10142789b7e0f78a222546ed1e)
- 4.1.8: [User Namespaces](#pg-868be91dc02aab6dc768102e4abf5eff)
- 4.1.9: [Downward API](#pg-420713565efe2f940e277f6b4824ad9a)

+ 4.2: [Workload Management](#pg-89637410cacae45a36ab1cc278c482eb)

- 4.2.1: [Deployments](#pg-a2dc0393e0c4079e1c504b6429844e86)
- 4.2.2: [ReplicaSet](#pg-d459b930218774655fa7fd1620625539)
- 4.2.3: [StatefulSets](#pg-6d72299952c37ca8cc61b416e5bdbcd4)
- 4.2.4: [DaemonSet](#pg-41600eb8b6631c88848156f381e9d588)
- 4.2.5: [Jobs](#pg-cc7cc3c4907039d9f863162e20bfbbef)
- 4.2.6: [Automatic Cleanup for Finished Jobs](#pg-4de50a37ebb6f2340484192126cb7a04)
- 4.2.7: [CronJob](#pg-2e4cec01c525b45eccd6010e21cc76d9)
- 4.2.8: [ReplicationController](#pg-27f1331d515d95f76aa1156088b4ad91)

+ 4.3: [Autoscaling Workloads](#pg-57dc30ff77a6b2871e15ed60c0bf61f0)
+ 4.4: [Managing Workloads](#pg-5921bd285837eed0aec7451e57f03654)
+ 4.5: [Vertical Pod Autoscaling](#pg-9452c7522847e65b263c3433561ab637)

* 5: [Services, Load Balancing, and Networking](#pg-0a0a7eca3e302a3c08f8c85e15d337fd)

+ 5.1: [Service](#pg-5701136fd2ce258047b6ddc389112352)
+ 5.2: [Ingress](#pg-199bcc92443dbc9bed44819467d7eb75)
+ 5.3: [Ingress Controllers](#pg-5a8edeb1f2dc8e38cd6d561bb08b0d78)
+ 5.4: [Gateway API](#pg-253904bd7754b4c2b34c262f42175a50)
+ 5.5: [EndpointSlices](#pg-f51db1097575de8072afe1f5b156a70c)
+ 5.6: [Network Policies](#pg-ded1daafdcd293023ee333728007ca61)
+ 5.7: [DNS for Services and Pods](#pg-91cb8a4438b003df11bc1c426a81b756)
+ 5.8: [IPv4/IPv6 dual-stack](#pg-21f8d19c60c33914baab66224c3d46a7)
+ 5.9: [Topology Aware Routing](#pg-8df2ab57df3ee82a73ffaada69bcd178)
+ 5.10: [Networking on Windows](#pg-9092684b3a27432bc9041d56b7a4a8ba)
+ 5.11: [Service ClusterIP allocation](#pg-439738e82e994f627155bff468d35404)
+ 5.12: [Service Internal Traffic Policy](#pg-cd7657b1056ad32451974db57a951ba5)

* 6: [Storage](#pg-f018f568c6723865753f150c3c59bdda)

+ 6.1: [Volumes](#pg-27795584640a03bd2024f1fe3b3ab754)
+ 6.2: [Persistent Volumes](#pg-ffd12528a12882b282e1bd19e29f9e75)
+ 6.3: [Projected Volumes](#pg-2db414b26d4daec3ebed19dd837830c3)
+ 6.4: [Ephemeral Volumes](#pg-df33eab51202c17bb0fe551d1d5cc5d2)
+ 6.5: [Storage Classes](#pg-f0276d05eef111249272a1c932a91e2c)
+ 6.6: [Volume Attributes Classes](#pg-2e186c3aca9aeef9a8cddd5adb5be7ef)
+ 6.7: [Dynamic Volume Provisioning](#pg-018f0a7fc6e2f6d16da37702fc39b4f3)
+ 6.8: [Volume Snapshots](#pg-c262af210c6828dec445d2f55a1d877a)
+ 6.9: [Volume Snapshot Classes](#pg-4d00116c86dade62bdd5be7dc2afa1ca)
+ 6.10: [CSI Volume Cloning](#pg-707ca81a34eb1ca202f34692e9917d1e)
+ 6.11: [Storage Capacity](#pg-00cd24f4570b7acaac75c2551c948bc7)
+ 6.12: [Node-specific Volume Limits](#pg-b2e4b16ac37988c678a3312a4a6639f8)
+ 6.13: [Local ephemeral storage](#pg-cd04c26518cc66fd0bbf6ef26a8ec233)
+ 6.14: [Volume Health Monitoring](#pg-4f40cb95a671e51b4f0156a409d95c6d)
+ 6.15: [Windows Storage](#pg-055a8df536f8ba8f3aa0217bd2db5437)

* 7: [Configuration](#pg-275bea454e1cf4c5adeca4058b5af988)

+ 7.1: [ConfigMaps](#pg-6b5ccadd699df0904e8e9917c5450c4b)
+ 7.2: [Secrets](#pg-e511ed821ada65d0053341dbd8ad2bb5)
+ 7.3: [Liveness, Readiness, and Startup Probes](#pg-dd30eec11fad0d212be01a17d72f7740)
+ 7.4: [Resource Management for Pods and Containers](#pg-436057b96151ecb8a4a9a9f456b5d0fc)
+ 7.5: [Organizing Cluster Access Using kubeconfig Files](#pg-ab6d20f33ad930a67ee7ef57bff6c75e)
+ 7.6: [Resource Management for Windows nodes](#pg-0f628478dbd58516389164933f9d7da2)

* 8: [Security](#pg-712cb3c03ff14a39e5a83a6d9b71d203)

+ 8.1: [Cloud Native Security and Kubernetes](#pg-ae7195710f528f7c066a1d3ed9ff96d5)
+ 8.2: [Pod Security Standards](#pg-1fb24c1dd155f43849da490a74c4b8c5)
+ 8.3: [Pod Security Admission](#pg-bc9934fccfeaf880eec6ea79025c0381)
+ 8.4: [Service Accounts](#pg-99657bdba0ee6a08e7d2d4dfcb211f37)
+ 8.5: [Pod Security Policies](#pg-ac71855bb20cbf21edc666e810f4103a)
+ 8.6: [Security For Linux Nodes](#pg-a8de8d26644e9854bc7b9f2d67dfad6c)
+ 8.7: [Security For Windows Nodes](#pg-9a68f631b6bc38c279bbc9a145e34ef2)
+ 8.8: [Controlling Access to the Kubernetes API](#pg-4d77d1ae4c06aa14f54b385191627881)
+ 8.9: [Role Based Access Control Good Practices](#pg-07f58aa0218d666795499c2e2306ff96)
+ 8.10: [Good practices for Kubernetes Secrets](#pg-a7863bfad3d69f33f5b318b9028eecb8)
+ 8.11: [Multi-tenancy](#pg-9dd9b8c71fa39ff803fd15b0e784069d)
+ 8.12: [Hardening Guide - Authentication Mechanisms](#pg-4612c25e260ec5f15e1ae95c1ae1e75f)
+ 8.13: [Hardening Guide - Scheduler Configuration](#pg-d789201f13c24b18714779216ed332ad)
+ 8.14: [Kubernetes API Server Bypass Risks](#pg-265c06c3d1349382453ced9f2a7ecfde)
+ 8.15: [Linux kernel security constraints for Pods and containers](#pg-6d284b4a386ae680f2a60f3a3668a287)
+ 8.16: [Security Checklist](#pg-6f8354561fd5286f997909e14b13110c)
+ 8.17: [Application Security Checklist](#pg-02379552399839bd27dc6742e7a5ff16)

* 9: [Policies](#pg-ac9161c6d952925b083ad9602b4e8e7f)

+ 9.1: [Limit Ranges](#pg-a935ff8c59eb116b43494255cc67f69a)
+ 9.2: [Resource Quotas](#pg-94ddc6e901c30f256138db11d09f05a3)
+ 9.3: [Process ID Limits And Reservations](#pg-7352434db5f5954d2f7656b46fe5a324)
+ 9.4: [Node Resource Managers](#pg-b528c4464c030f3f044124b38d778f04)

* 10: [Scheduling, Preemption and Eviction](#pg-c21d05f31057c5bcd2ebdd01f4e62a0e)

+ 10.1: [Kubernetes Scheduler](#pg-598f36d691ab197f9d995784574b0a12)
+ 10.2: [Assigning Pods to Nodes](#pg-21169f516071aea5d16734a4c27789a5)
+ 10.3: [Pod Overhead](#pg-da22fe2278df236f71efbe672f392677)
+ 10.4: [Pod Scheduling Readiness](#pg-d9483841860fd8701aee18ffb0759aef)
+ 10.5: [Pod Topology Spread Constraints](#pg-6b8c85a6a88f4a81e6b79e197c293c31)
+ 10.6: [Taints and Tolerations](#pg-ede4960b56a3529ee0bfe7c8fe2d09a5)
+ 10.7: [Scheduling Framework](#pg-602208c95fe7b1f1170310ce993f5814)
+ 10.8: [Dynamic Resource Allocation](#pg-132fdff5faea3a27f280f3acdf4f8b7d)
+ 10.9: [Scheduler Performance Tuning](#pg-d9574a30fcbc631b0d2a57850e161e89)
+ 10.10: [Resource Bin Packing](#pg-961126cd43559012893979e568396a49)
+ 10.11: [Pod Priority and Preemption](#pg-60e5a2861609e0848d58ce8bf99c4a31)
+ 10.12: [Node-pressure Eviction](#pg-78e0431b4b7516092662a7c289cbb304)
+ 10.13: [API-initiated Eviction](#pg-b87723bf81b079042860f0ebd37b0a64)

* 11: [Cluster Administration](#pg-285a3785fd3d20f437c28d87ca4dadca)

+ 11.1: [Node Shutdowns](#pg-16c1422c18d5129a279e2665c901e8c3)
+ 11.2: [Swap memory management](#pg-240bbf5f8a89640813a6d0052a7f25e1)
+ 11.3: [Node Autoscaling](#pg-4ae6e7bda71061ba22fc25b550862444)
+ 11.4: [Certificates](#pg-2bf9a93ab5ba014fb6ff70b22c29d432)
+ 11.5: [Cluster Networking](#pg-d649067a69d8d5c7e71564b42b96909e)
+ 11.6: [Observability](#pg-6dc1280c519a8fb0e17d2182a282f624)
+ 11.7: [Admission Webhook Good Practices](#pg-36267e27053712ce65663b894ebc8b3c)
+ 11.8: [Good practices for Dynamic Resource Allocation as a Cluster Admin](#pg-2b8f3836f8e444efb8b7997a89fd1e4e)
+ 11.9: [Logging Architecture](#pg-c4b1e87a84441f8a90699a345ce48d68)
+ 11.10: [Compatibility Version For Kubernetes Control Plane Components](#pg-ffefe4383ad78ecf6542f8d6943ad960)
+ 11.11: [Metrics For Kubernetes System Components](#pg-cbfd3654996eae9fcdef009f70fa83f0)
+ 11.12: [Metrics for Kubernetes Object States](#pg-0d497efe8a549d8f9ffeca15e365cf91)
+ 11.13: [System Logs](#pg-5cc31ecfba86467f8884856412cfb6b2)
+ 11.14: [Traces For Kubernetes System Components](#pg-3da54ad355f6fe6574d67bd9a9a42bcb)
+ 11.15: [Proxies in Kubernetes](#pg-08e94e6a480e0d6b2de72d84a1b97617)
+ 11.16: [API Priority and Fairness](#pg-31c9327d2332c585341b64ddafa19cdd)
+ 11.17: [Installing Addons](#pg-85d633ae590aa20ec024f1b7af1d74fc)
+ 11.18: [Coordinated Leader Election](#pg-9bbd2d79b9af3b1a869b28b010c515a6)

* 12: [Windows in Kubernetes](#pg-05a1231ecbfe48ec554e6d078818aca4)

+ 12.1: [Windows containers in Kubernetes](#pg-849246a35c3de66980f66e1b0944ceb4)
+ 12.2: [Guide for Running Windows Containers in Kubernetes](#pg-0d8bfd3be43b3580681c56f6fec9d6dc)

* 13: [Extending Kubernetes](#pg-7e0d97616b15e2c383c6a0a96ec442cb)

+ 13.1: [Compute, Storage, and Networking Extensions](#pg-c8937cdc9df96f3328becf04f8211292)

- 13.1.1: [Network Plugins](#pg-1ac2260db9ecccbf0303a899bc27ce6d)
- 13.1.2: [Device Plugins](#pg-53e1ea8892ceca307ba19e8d6a7b8d32)

+ 13.2: [Extending the Kubernetes API](#pg-0af41d3bd7c785621b58b7564793396a)

- 13.2.1: [Custom Resources](#pg-342388440304e19ce30c0f8ada1c77ce)
- 13.2.2: [Kubernetes API Aggregation Layer](#pg-1ea4977c0ebf97569bf54a477faa7fa5)

+ 13.3: [Operator pattern](#pg-3131452556176159fb269593c1a52012)

The Concepts section helps you learn about the parts of the Kubernetes system and the abstractions Kubernetes uses to represent your [cluster](/docs/reference/glossary/?all=true#term-cluster "A set of worker machines, called nodes, that run containerized applications. Every cluster has at least one worker node."), and helps you obtain a deeper understanding of how Kubernetes works.
