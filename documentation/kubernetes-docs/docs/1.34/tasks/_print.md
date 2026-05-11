This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/tasks/).

# Tasks

* 1: [Install Tools](#pg-57bf66f59d9a642b82eebeabbc66470b)

+ 1.1: [Install and Set Up kubectl on Linux](#pg-37b6179f23c8ad977cb9daa6d2da748a)
+ 1.2: [Install and Set Up kubectl on macOS](#pg-961fc70b732cb8df4fd11a3463b6545c)
+ 1.3: [Install and Set Up kubectl on Windows](#pg-2cc93d3011d707aeb6564bab02048f7a)

* 2: [Administer a Cluster](#pg-34a810f1516ad9d99b2697e36e9b0d0f)

+ 2.1: [Administration with kubeadm](#pg-8e16d69617b175d61e2e7a6e1642c9d6)

- 2.1.1: [Adding Linux worker nodes](#pg-ab410152d969657c1c07d398a77bef0b)
- 2.1.2: [Adding Windows worker nodes](#pg-9133578f1e75663bb031e5a377ca896d)
- 2.1.3: [Upgrading kubeadm clusters](#pg-2e173356df5179cab9eec90a606f0aa4)
- 2.1.4: [Upgrading Linux nodes](#pg-6b7736cc39850c701167d0fd223469bf)
- 2.1.5: [Upgrading Windows nodes](#pg-e805c7d8d4ad6195cb82dbbc843bfc29)
- 2.1.6: [Configuring a cgroup driver](#pg-6134c5061298affa145ddb801b5c29da)
- 2.1.7: [Certificate Management with kubeadm](#pg-f62fba1de4084f3be070785757c8079c)
- 2.1.8: [Reconfiguring a kubeadm cluster](#pg-98530eb3653d28fef34bff4543364aa7)
- 2.1.9: [Changing The Kubernetes Package Repository](#pg-8052e6a03822da79296372cc4c4327ed)

+ 2.2: [Overprovision Node Capacity For A Cluster](#pg-441c19c30fcb31ea652d3ffa3100d79f)
+ 2.3: [Migrating from dockershim](#pg-adb6c52e773f4d890595e14a9251f59b)

- 2.3.1: [Changing the Container Runtime on a Node from Docker Engine to containerd](#pg-b8acce0768c2f92cdb8eaa31e8072353)
- 2.3.2: [Find Out What Container Runtime is Used on a Node](#pg-d79db9ed1698f75ec5f2228987290e49)
- 2.3.3: [Troubleshooting CNI plugin-related errors](#pg-c4b5bb78bc6c59690d21c44e41f12270)
- 2.3.4: [Check whether dockershim removal affects you](#pg-cbd252cc297e67c1b73a84d5882474fb)
- 2.3.5: [Migrating telemetry and security agents from dockershim](#pg-eb3e279a6c5e1224e744080a52ee3f28)

+ 2.4: [Generate Certificates Manually](#pg-7743f043c43f7b12e8654e2227dbc658)
+ 2.5: [Manage Memory, CPU, and API Resources](#pg-47be5dd51f686017f1766e6ec7aa6f41)

- 2.5.1: [Configure Default Memory Requests and Limits for a Namespace](#pg-337620c76587e4aeb32009cb23be46de)
- 2.5.2: [Configure Default CPU Requests and Limits for a Namespace](#pg-320af95e480962c538ebef7ae205845c)
- 2.5.3: [Configure Minimum and Maximum Memory Constraints for a Namespace](#pg-adb489b1ab985c9215657b0d4c6ae92b)
- 2.5.4: [Configure Minimum and Maximum CPU Constraints for a Namespace](#pg-a87cbd1f9379dac7a48ae320da68a9ad)
- 2.5.5: [Configure Memory and CPU Quotas for a Namespace](#pg-fe3283559a3df299aae3ee00ecea2fad)
- 2.5.6: [Configure a Pod Quota for a Namespace](#pg-40e30a9209e0c9f4153707e43243e9d7)

+ 2.6: [Install a Network Policy Provider](#pg-8c31aafd38fad5b0de0bd191758d6f93)

- 2.6.1: [Use Antrea for NetworkPolicy](#pg-b4418905b0c14630e4e9cb1368241534)
- 2.6.2: [Use Calico for NetworkPolicy](#pg-1239a77618c6278373832a142cd85519)
- 2.6.3: [Use Cilium for NetworkPolicy](#pg-95039241255a31df196beaa405b68eba)
- 2.6.4: [Use Kube-router for NetworkPolicy](#pg-505a0a6a7e6eff361bbb3be81c84b2e0)
- 2.6.5: [Romana for NetworkPolicy](#pg-2842eac98aa0e229a5c6755c4c83d2a7)
- 2.6.6: [Weave Net for NetworkPolicy](#pg-ac075c3fdfd0d41aa753cc70e42be064)

+ 2.7: [Access Clusters Using the Kubernetes API](#pg-e77685d5b88d2db5c7631a27b9472eea)
+ 2.8: [Enable Or Disable Feature Gates](#pg-8e39522181537d5660d43707151d397e)
+ 2.9: [Advertise Extended Resources for a Node](#pg-a8f6511197efcd7d0db80ade49620f9d)
+ 2.10: [Autoscale the DNS Service in a Cluster](#pg-966cd1cc69c69410d8698b3ac74abce2)
+ 2.11: [Change the Access Mode of a PersistentVolume to ReadWriteOncePod](#pg-a4f6143cfa799506d621a375eebf5fd7)
+ 2.12: [Change the default StorageClass](#pg-2bffd7f3571cdd609bd97fb2e1bdb2fe)
+ 2.13: [Switching from Polling to CRI Event-based Updates to Container Status](#pg-7dce416b39aa1a960c6fd5200a06f3e1)
+ 2.14: [Change the Reclaim Policy of a PersistentVolume](#pg-fbc9136f53eccd6eb8c80f4bbea3b8f4)
+ 2.15: [Cloud Controller Manager Administration](#pg-ce4cd28c8feb9faa783e79b48af37961)
+ 2.16: [Configure a kubelet image credential provider](#pg-c4ee04bf3b927d6ab82ae9ac4c4fc228)
+ 2.17: [Configure Quotas for API Objects](#pg-5e59f5575dce11fdaed640afdbeedfc1)
+ 2.18: [Control CPU Management Policies on the Node](#pg-7127e6b7344b315b30b1ce8c4d8bfc55)
+ 2.19: [Control Topology Management Policies on a node](#pg-8060aed5bf1172fa62199a4c306a4cd1)
+ 2.20: [Customizing DNS Service](#pg-3d0cd7d2f13d4759094f281504cf57b8)
+ 2.21: [Debugging DNS Resolution](#pg-8bcf4aeb5bbb6d6969a146e5ab97557b)
+ 2.22: [Declare Network Policy](#pg-a3790dfb57271d13517e549dffa805b9)
+ 2.23: [Developing Cloud Controller Manager](#pg-9585dc0efb0450fd68728e7511754717)
+ 2.24: [Enable Or Disable A Kubernetes API](#pg-09cc2cf3e0f23a3996e6cb31dc4d867c)
+ 2.25: [Encrypting Confidential Data at Rest](#pg-6b4e7ca6586f448c8533a120c29bdd25)
+ 2.26: [Decrypt Confidential Data that is Already Encrypted at Rest](#pg-af46c44ff97eb039902495caa336779b)
+ 2.27: [Guaranteed Scheduling For Critical Add-On Pods](#pg-4a02bcca41439e16655f43fa37c81da4)
+ 2.28: [IP Masquerade Agent User Guide](#pg-b45f024608e1b367cdacb1fd9d77278a)
+ 2.29: [Limit Storage Consumption](#pg-a02f35804917d7a269c38d7e2c475005)
+ 2.30: [Migrate Replicated Control Plane To Use Cloud Controller Manager](#pg-a24171610b6ea75a142cb9c8c7882390)
+ 2.31: [Operating etcd clusters for Kubernetes](#pg-c4d0832845adc92b7ccd54aed63fc932)
+ 2.32: [Reserve Compute Resources for System Daemons](#pg-b64a1d2bb3f4ed9f7021134e09a75c36)
+ 2.33: [Running Kubernetes Node Components as a Non-root User](#pg-f6f3b8f9789fda4286bf410b8e108f69)
+ 2.34: [Safely Drain a Node](#pg-b35b8ddb9bbc15620ce9636f4346c05c)
+ 2.35: [Securing a Cluster](#pg-12001be83d15fcd7f3242313a55777df)
+ 2.36: [Set Kubelet Parameters Via A Configuration File](#pg-f58763cc9447491b6c40f939a02d441d)
+ 2.37: [Share a Cluster with Namespaces](#pg-1e966f5d0540bbee0876f9d0d08d54dc)
+ 2.38: [Upgrade A Cluster](#pg-fe6b50655c29ab0b7c1ee549ff64c138)
+ 2.39: [Use Cascading Deletion in a Cluster](#pg-4e9de5bc3973e5d2bb8f09ff940c3319)
+ 2.40: [Using a KMS provider for data encryption](#pg-669c88964b4a9eb2b040057266e4b60d)
+ 2.41: [Using CoreDNS for Service Discovery](#pg-e1afcdac8d5e8458274b3c481c5ebcda)
+ 2.42: [Using NodeLocal DNSCache in Kubernetes Clusters](#pg-9ceed97f912df7289ed8872e290cfbad)
+ 2.43: [Using sysctls in a Kubernetes Cluster](#pg-fe5ad73163d38596340536ec03a205f0)
+ 2.44: [Utilizing the NUMA-aware Memory Manager](#pg-778055e4a4415ca195169b42cd42ddf9)
+ 2.45: [Verify Signed Kubernetes Artifacts](#pg-6019e3a8a90c485fd4ffbd38936c8e1b)

* 3: [Configure Pods and Containers](#pg-f5da33b976758a9183018c421eb83f58)

+ 3.1: [Assign Memory Resources to Containers and Pods](#pg-e6dd9300cf3a955f7cdfe77fb5d15292)
+ 3.2: [Assign CPU Resources to Containers and Pods](#pg-8555af270ae7122cc0464bab3f5d1609)
+ 3.3: [Assign Devices to Pods and Containers](#pg-623121ceae1a33b10931a6819ce8fd50)

- 3.3.1: [Set Up DRA in a Cluster](#pg-0c600fbd5e9d67ec311681ace8bc3f05)
- 3.3.2: [Allocate Devices to Workloads with DRA](#pg-538ca6a26f823f9c623e4fe4714e3866)

+ 3.4: [Assign Pod-level CPU and memory resources](#pg-ddbf912e657a0d1d6a141990dfcd5b82)
+ 3.5: [Configure GMSA for Windows Pods and containers](#pg-aa522472483f900008124a2809f2114b)
+ 3.6: [Resize CPU and Memory Resources assigned to Containers](#pg-4f86216939dcc979768c43d90d3dfde6)
+ 3.7: [Configure RunAsUserName for Windows pods and containers](#pg-f5da7517bee8a8807431d9fc65263b39)
+ 3.8: [Create a Windows HostProcess Pod](#pg-3fbf113e9e5f4b46f8ccb91a048509c0)
+ 3.9: [Configure Quality of Service for Pods](#pg-904cea8c8efd5c0d33adbfe579ec2dd2)
+ 3.10: [Assign Extended Resources to a Container](#pg-4219ac6ab56a3b88d20305083d57d03c)
+ 3.11: [Configure a Pod to Use a Volume for Storage](#pg-484833fb880d1e179cc2965d15f84da5)
+ 3.12: [Configure a Pod to Use a PersistentVolume for Storage](#pg-528d2422215cb9632b7b45e886b023b5)
+ 3.13: [Configure a Pod to Use a Projected Volume for Storage](#pg-4621938ba53c04a77f51b5938a583439)
+ 3.14: [Configure a Security Context for a Pod or Container](#pg-abd895c0803315e9717e6ff9ec4e3d30)
+ 3.15: [Configure Service Accounts for Pods](#pg-2c0d882359718c4c69c67099bed2156c)
+ 3.16: [Pull an Image from a Private Registry](#pg-d385b86a7cb496d3b1c3b2a47280ca70)
+ 3.17: [Configure Liveness, Readiness and Startup Probes](#pg-eb54daf87df373096b5e830680194dfc)
+ 3.18: [Assign Pods to Nodes](#pg-bbc17480da6d051c696489654c64064a)
+ 3.19: [Assign Pods to Nodes using Node Affinity](#pg-fc3f4777ae8ea685d2b54e175277ac01)
+ 3.20: [Configure Pod Initialization](#pg-1e7baac1825631a5af5d2aebcf059249)
+ 3.21: [Attach Handlers to Container Lifecycle Events](#pg-efbc43486296f0439d1a89c12d944d94)
+ 3.22: [Configure a Pod to Use a ConfigMap](#pg-ed34e761c3dbd00fa79577fa78e30020)
+ 3.23: [Share Process Namespace between Containers in a Pod](#pg-3d7b9cb24a647c36ba63f7a02ec49010)
+ 3.24: [Use a User Namespace With a Pod](#pg-18935633a984586fbb68b727f3f339bb)
+ 3.25: [Use an Image Volume With a Pod](#pg-50d70040f877c4d1bd51b99626e3c169)
+ 3.26: [Create static Pods](#pg-42a59b878d4c58e5c6f4bb87483dda93)
+ 3.27: [Translate a Docker Compose File to Kubernetes Resources](#pg-1bb997c61a85de753d9994e7a312a291)
+ 3.28: [Enforce Pod Security Standards by Configuring the Built-in Admission Controller](#pg-108be708e50a97cae1cc0b67d5f360b7)
+ 3.29: [Enforce Pod Security Standards with Namespace Labels](#pg-9c9966a13899846a35113763603cd6db)
+ 3.30: [Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller](#pg-0a91fdc1445a8c7f3563c41a9b9b3370)

* 4: [Monitoring, Logging, and Debugging](#pg-61e6bd39c782b924943d60fc8387afe4)

+ 4.1: [Logging in Kubernetes](#pg-76e5c9a3748b8e55436a260715029cc3)

+ 4.2: [Monitoring in Kubernetes](#pg-6b5c06161a775b26439d3fa0cba53f5c)

+ 4.3: [Troubleshooting Applications](#pg-4a26f4e7f9ffe4b86dea8b77906d3d5c)

- 4.3.1: [Debug Pods](#pg-abb72792fa997869a6d241ca28ea225e)
- 4.3.2: [Debug Services](#pg-68c4fd0542b7d39f8d36435ef83bd57b)
- 4.3.3: [Debug a StatefulSet](#pg-089001d4003f033e21602adcb11cd277)
- 4.3.4: [Determine the Reason for Pod Failure](#pg-655b47c523b6f1b52d25e520625abccb)
- 4.3.5: [Debug Init Containers](#pg-43445f3208669d4078e87dbdbeed8473)
- 4.3.6: [Debug Running Pods](#pg-132acc7efbd72bd677945eda3b6c6d38)
- 4.3.7: [Get a Shell to a Running Container](#pg-09530217eead8a801ead3ef165c2f591)

+ 4.4: [Troubleshooting Clusters](#pg-ce321f5c35198a1d9b64d52a98ba705c)

- 4.4.1: [Troubleshooting kubectl](#pg-a63c7f412c1d137412ccee9f854d3a0c)
- 4.4.2: [Resource metrics pipeline](#pg-5ff0cdcf7701f887e45d629f5cfe0424)
- 4.4.3: [Tools for Monitoring Resources](#pg-cb9e28c208c6cfbabdb15ba2e42e9ef0)
- 4.4.4: [Monitor Node Health](#pg-20165c8269bed123bfb94fb6e7f85643)
- 4.4.5: [Debugging Kubernetes nodes with crictl](#pg-6ca4f22ef4d1713577ada4815f0a3b5a)
- 4.4.6: [Auditing](#pg-38387ad04dd284933cb502944ea3515b)
- 4.4.7: [Debugging Kubernetes Nodes With Kubectl](#pg-0480b8ee5cb8facb546b471bc739286d)
- 4.4.8: [Developing and debugging services locally using telepresence](#pg-60dca0ec8d41f0045e7d73e1d6bd7bce)
- 4.4.9: [Windows debugging tips](#pg-34f51c9306a166418b33355c09e672be)

* 5: [Manage Kubernetes Objects](#pg-aa0731e8aa8e2f6cc9e3c1a5e9895863)

+ 5.1: [Declarative Management of Kubernetes Objects Using Configuration Files](#pg-df206392be6f4d19bd8da41cee7170fa)
+ 5.2: [Declarative Management of Kubernetes Objects Using Kustomize](#pg-11aa6950fcb203094823c8e2cbdd517f)
+ 5.3: [Managing Kubernetes Objects Using Imperative Commands](#pg-80c83fe9b80d0fef2681c8d59c0aa197)
+ 5.4: [Imperative Management of Kubernetes Objects Using Configuration Files](#pg-b18886277c410fc6f32ce068e2160537)
+ 5.5: [Update API Objects in Place Using kubectl patch](#pg-d4d4414dc91b63cfe0f65ca4f0c2fe31)
+ 5.6: [Migrate Kubernetes Objects Using Storage Version Migration](#pg-b6b58b128f676092f348d3ba37d29b21)

* 6: [Managing Secrets](#pg-94f49ece137035764368f22a98942872)

+ 6.1: [Managing Secrets using kubectl](#pg-0ed63ce3c9665aed7ff5a560ff1da843)
+ 6.2: [Managing Secrets using Configuration File](#pg-e841cf91fd3566db1e86143ed7a9e13c)
+ 6.3: [Managing Secrets using Kustomize](#pg-a0ff2e3ba8af5670d5dc3d94c4bd0a68)

* 7: [Inject Data Into Applications](#pg-866924fa095f897ede8dfdcab9e97942)

+ 7.1: [Define a Command and Arguments for a Container](#pg-c9af1e81bb6e109f6c41febe44f0931b)
+ 7.2: [Define Dependent Environment Variables](#pg-eff97c25c917cdb414eda016df0e2bca)
+ 7.3: [Define Environment Variables for a Container](#pg-82c93897176489678232542102daea40)
+ 7.4: [Define Environment Variable Values Using An Init Container](#pg-fada84b3b423edd5bd735c352fbd4a84)
+ 7.5: [Expose Pod Information to Containers Through Environment Variables](#pg-66c0456fdbef5e5116dd606d1e6f73cc)
+ 7.6: [Expose Pod Information to Containers Through Files](#pg-bcf93d1cd019501fd0b7649e9fbcaf60)
+ 7.7: [Distribute Credentials Securely Using Secrets](#pg-7f9454a1e775548c23ee5b300a9218a3)

* 8: [Run Applications](#pg-a78a5e7e765fd8c49c8f7c0d72499f72)

+ 8.1: [Run a Stateless Application Using a Deployment](#pg-790ea02857492b3a822e981e93e3a98b)
+ 8.2: [Run a Single-Instance Stateful Application](#pg-43398a6f5dc7ce19df59f5f4c2e7922d)
+ 8.3: [Run a Replicated Stateful Application](#pg-95b3d561509c573e53bec2368264cf6a)
+ 8.4: [Scale a StatefulSet](#pg-7a9b5779e228083ba3fdeaf414fe704e)
+ 8.5: [Delete a StatefulSet](#pg-c43537b0ee1da992ecb7488f87e6c934)
+ 8.6: [Force Delete StatefulSet Pods](#pg-f5f2f7a74377a9d45325c5253353fa8f)
+ 8.7: [Horizontal Pod Autoscaling](#pg-0c0bb1bd76d2a9069e50e2cec6d20c2a)
+ 8.8: [HorizontalPodAutoscaler Walkthrough](#pg-8138226ce9660ac8e3e82ff86fff8ad2)
+ 8.9: [Specifying a Disruption Budget for your Application](#pg-fbe2744f00d1aa4df4cdf4eea6a082d4)
+ 8.10: [Accessing the Kubernetes API from a Pod](#pg-52cd10ee3fc7c74a6c31043a2d489878)

* 9: [Run Jobs](#pg-ca3bc4e31dfe46d5044a3b93eb804ee9)

+ 9.1: [Running Automated Tasks with a CronJob](#pg-964bdff888520740e5e221695245678d)
+ 9.2: [Coarse Parallel Processing Using a Work Queue](#pg-1058efa4d70f13c015e6a2094ff85068)
+ 9.3: [Fine Parallel Processing Using a Work Queue](#pg-457c9dd93aed2b05615ed28dc38075d3)
+ 9.4: [Indexed Job for Parallel Processing with Static Work Assignment](#pg-9e63850014876afaebd1561f70bb8f6b)
+ 9.5: [Job with Pod-to-Pod Communication](#pg-d65c40e1d2df81b94a09634c2432b055)
+ 9.6: [Parallel Processing using Expansions](#pg-da7c2b067953d239eb4457e8978ad8f6)
+ 9.7: [Handling retriable and non-retriable pod failures with Pod failure policy](#pg-ecb5ec00bbce2e57292c6687437beae0)

* 10: [Access Applications in a Cluster](#pg-b74b959f5a531003dd0653dfbfc2e88b)

+ 10.1: [Deploy and Access the Kubernetes Dashboard](#pg-777447042cd4e81df3fa5beb3357a485)
+ 10.2: [Accessing Clusters](#pg-6a8d9e9e05f2b6825afbb8889c957370)
+ 10.3: [Configure Access to Multiple Clusters](#pg-5a233e14205d77fe1294917d2da6f876)
+ 10.4: [Use Port Forwarding to Access Applications in a Cluster](#pg-72d3dddbc0c166c9a364e753d2b31ff0)
+ 10.5: [Use a Service to Access an Application in a Cluster](#pg-312f29f850826b74618634cd877aa065)
+ 10.6: [Connect a Frontend to a Backend Using Services](#pg-f3dac629bea950fc026d920306f09fb4)
+ 10.7: [Create an External Load Balancer](#pg-21cd8f87563675fb0278d3694ba9ecb0)
+ 10.8: [List All Container Images Running in a Cluster](#pg-48e8f306f919c5b81265e265a2b76ab4)
+ 10.9: [Communicate Between Containers in the Same Pod Using a Shared Volume](#pg-7c319a9981586e5fbcfa21b392720650)
+ 10.10: [Configure DNS for a Cluster](#pg-322786b38586b210fab68f785259c5f6)
+ 10.11: [Access Services Running on Clusters](#pg-43591bb11cc02c39e278cf07f6546810)

* 11: [Extend Kubernetes](#pg-11a6d16334428909c99e7208ab8fa5e9)

+ 11.1: [Configure the Aggregation Layer](#pg-2bd28753e62a14a597073fa8ea18a5d8)
+ 11.2: [Use Custom Resources](#pg-8f1f7f0d3a1cc21537506bd4f9103a29)

- 11.2.1: [Extend the Kubernetes API with CustomResourceDefinitions](#pg-dc64883f1fd119402b112d3ff6733452)
- 11.2.2: [Versions in CustomResourceDefinitions](#pg-7d2e2400f208b1637530752794e5a3bd)

+ 11.3: [Set up an Extension API Server](#pg-c4798e42eaccc051e396542befb3c57b)
+ 11.4: [Configure Multiple Schedulers](#pg-c00a2767fac9dbfafce583cf489cc423)
+ 11.5: [Use an HTTP Proxy to Access the Kubernetes API](#pg-1707517970dd390995f760308c2e2de6)
+ 11.6: [Use a SOCKS5 Proxy to Access the Kubernetes API](#pg-46417c7cdd2da2c530aaeddca1861e5c)
+ 11.7: [Set up Konnectivity service](#pg-61cf1f2f0fbe98e7635fce65f04a775f)

* 12: [TLS](#pg-d3c88a8663f58e9ec0bed73faff5b670)

+ 12.1: [Issue a Certificate for a Kubernetes API Client Using A CertificateSigningRequest](#pg-44794ecd49af6675e02bdd8eb7eba5ec)
+ 12.2: [Configure Certificate Rotation for the Kubelet](#pg-1272b18ac0c008f6ffc2c62a29fa929f)
+ 12.3: [Manage TLS Certificates in a Cluster](#pg-9a87de8ee8332cb487f34a05debb1125)
+ 12.4: [Manual Rotation of CA Certificates](#pg-43d5e2b1fc2a7e104e66d481d08578dc)

* 13: [Manage Cluster Daemons](#pg-ba58efa15c6d46f10e34d799be220965)

+ 13.1: [Building a Basic DaemonSet](#pg-4c10d304f68febdf95ee7ab4b6b77a96)
+ 13.2: [Perform a Rolling Update on a DaemonSet](#pg-bcfd795e4b59420f7db275a0482af37c)
+ 13.3: [Perform a Rollback on a DaemonSet](#pg-f1bf7e426f482a85e1a417d1fd9ea7b7)
+ 13.4: [Running Pods on Only Some Nodes](#pg-9f4e3502e32b35c9804dd5a30b65b4cc)

* 14: [Networking](#pg-a701e71f3b32dae474c63ae4c596c856)

+ 14.1: [Adding entries to Pod /etc/hosts with HostAliases](#pg-2edb5b02ea1e646c333c9fe4d5f02ff1)
+ 14.2: [Extend Service IP Ranges](#pg-7c1bc7e4ee00dfcfb4f9a01b6b52cc38)
+ 14.3: [Kubernetes Default ServiceCIDR Reconfiguration](#pg-5d46e15e7173cda06f3f73011e711d5f)
+ 14.4: [Validate IPv4/IPv6 dual-stack](#pg-eebac062766222247063d6513f95c7b2)

* 15: [Extend kubectl with plugins](#pg-f34d6e348a8e677d6c6eb155cd1a99aa)
* 16: [Manage HugePages](#pg-fdfb2a2cba62a1e624897eaebac0168e)
* 17: [Schedule GPUs](#pg-5ab7bc7f14942c5c4b29d19f4a87271c)

This section of the Kubernetes documentation contains pages that
show how to do individual tasks. A task page shows how to do a
single thing, typically by giving a short sequence of steps.

If you would like to write a task page, see
[Creating a Documentation Pull Request](/docs/contribute/new-content/open-a-pr/).
