This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/tasks/administer-cluster/).

# Administer a Cluster

Learn common tasks for administering a cluster.

* 1: [Administration with kubeadm](#pg-8e16d69617b175d61e2e7a6e1642c9d6)

+ 1.1: [Adding Linux worker nodes](#pg-ab410152d969657c1c07d398a77bef0b)
+ 1.2: [Adding Windows worker nodes](#pg-9133578f1e75663bb031e5a377ca896d)
+ 1.3: [Upgrading kubeadm clusters](#pg-2e173356df5179cab9eec90a606f0aa4)
+ 1.4: [Upgrading Linux nodes](#pg-6b7736cc39850c701167d0fd223469bf)
+ 1.5: [Upgrading Windows nodes](#pg-e805c7d8d4ad6195cb82dbbc843bfc29)
+ 1.6: [Configuring a cgroup driver](#pg-6134c5061298affa145ddb801b5c29da)
+ 1.7: [Certificate Management with kubeadm](#pg-f62fba1de4084f3be070785757c8079c)
+ 1.8: [Reconfiguring a kubeadm cluster](#pg-98530eb3653d28fef34bff4543364aa7)
+ 1.9: [Changing The Kubernetes Package Repository](#pg-8052e6a03822da79296372cc4c4327ed)

* 2: [Overprovision Node Capacity For A Cluster](#pg-441c19c30fcb31ea652d3ffa3100d79f)
* 3: [Migrating from dockershim](#pg-adb6c52e773f4d890595e14a9251f59b)

+ 3.1: [Changing the Container Runtime on a Node from Docker Engine to containerd](#pg-b8acce0768c2f92cdb8eaa31e8072353)
+ 3.2: [Find Out What Container Runtime is Used on a Node](#pg-d79db9ed1698f75ec5f2228987290e49)
+ 3.3: [Troubleshooting CNI plugin-related errors](#pg-c4b5bb78bc6c59690d21c44e41f12270)
+ 3.4: [Check whether dockershim removal affects you](#pg-cbd252cc297e67c1b73a84d5882474fb)
+ 3.5: [Migrating telemetry and security agents from dockershim](#pg-eb3e279a6c5e1224e744080a52ee3f28)

* 4: [Generate Certificates Manually](#pg-7743f043c43f7b12e8654e2227dbc658)
* 5: [Manage Memory, CPU, and API Resources](#pg-47be5dd51f686017f1766e6ec7aa6f41)

+ 5.1: [Configure Default Memory Requests and Limits for a Namespace](#pg-337620c76587e4aeb32009cb23be46de)
+ 5.2: [Configure Default CPU Requests and Limits for a Namespace](#pg-320af95e480962c538ebef7ae205845c)
+ 5.3: [Configure Minimum and Maximum Memory Constraints for a Namespace](#pg-adb489b1ab985c9215657b0d4c6ae92b)
+ 5.4: [Configure Minimum and Maximum CPU Constraints for a Namespace](#pg-a87cbd1f9379dac7a48ae320da68a9ad)
+ 5.5: [Configure Memory and CPU Quotas for a Namespace](#pg-fe3283559a3df299aae3ee00ecea2fad)
+ 5.6: [Configure a Pod Quota for a Namespace](#pg-40e30a9209e0c9f4153707e43243e9d7)

* 6: [Install a Network Policy Provider](#pg-8c31aafd38fad5b0de0bd191758d6f93)

+ 6.1: [Use Antrea for NetworkPolicy](#pg-b4418905b0c14630e4e9cb1368241534)
+ 6.2: [Use Calico for NetworkPolicy](#pg-1239a77618c6278373832a142cd85519)
+ 6.3: [Use Cilium for NetworkPolicy](#pg-95039241255a31df196beaa405b68eba)
+ 6.4: [Use Kube-router for NetworkPolicy](#pg-505a0a6a7e6eff361bbb3be81c84b2e0)
+ 6.5: [Romana for NetworkPolicy](#pg-2842eac98aa0e229a5c6755c4c83d2a7)
+ 6.6: [Weave Net for NetworkPolicy](#pg-ac075c3fdfd0d41aa753cc70e42be064)

* 7: [Access Clusters Using the Kubernetes API](#pg-e77685d5b88d2db5c7631a27b9472eea)
* 8: [Enable Or Disable Feature Gates](#pg-8e39522181537d5660d43707151d397e)
* 9: [Advertise Extended Resources for a Node](#pg-a8f6511197efcd7d0db80ade49620f9d)
* 10: [Autoscale the DNS Service in a Cluster](#pg-966cd1cc69c69410d8698b3ac74abce2)
* 11: [Change the Access Mode of a PersistentVolume to ReadWriteOncePod](#pg-a4f6143cfa799506d621a375eebf5fd7)
* 12: [Change the default StorageClass](#pg-2bffd7f3571cdd609bd97fb2e1bdb2fe)
* 13: [Switching from Polling to CRI Event-based Updates to Container Status](#pg-7dce416b39aa1a960c6fd5200a06f3e1)
* 14: [Change the Reclaim Policy of a PersistentVolume](#pg-fbc9136f53eccd6eb8c80f4bbea3b8f4)
* 15: [Cloud Controller Manager Administration](#pg-ce4cd28c8feb9faa783e79b48af37961)
* 16: [Configure a kubelet image credential provider](#pg-c4ee04bf3b927d6ab82ae9ac4c4fc228)
* 17: [Configure Quotas for API Objects](#pg-5e59f5575dce11fdaed640afdbeedfc1)
* 18: [Control CPU Management Policies on the Node](#pg-7127e6b7344b315b30b1ce8c4d8bfc55)
* 19: [Control Topology Management Policies on a node](#pg-8060aed5bf1172fa62199a4c306a4cd1)
* 20: [Customizing DNS Service](#pg-3d0cd7d2f13d4759094f281504cf57b8)
* 21: [Debugging DNS Resolution](#pg-8bcf4aeb5bbb6d6969a146e5ab97557b)
* 22: [Declare Network Policy](#pg-a3790dfb57271d13517e549dffa805b9)
* 23: [Developing Cloud Controller Manager](#pg-9585dc0efb0450fd68728e7511754717)
* 24: [Enable Or Disable A Kubernetes API](#pg-09cc2cf3e0f23a3996e6cb31dc4d867c)
* 25: [Encrypting Confidential Data at Rest](#pg-6b4e7ca6586f448c8533a120c29bdd25)
* 26: [Decrypt Confidential Data that is Already Encrypted at Rest](#pg-af46c44ff97eb039902495caa336779b)
* 27: [Guaranteed Scheduling For Critical Add-On Pods](#pg-4a02bcca41439e16655f43fa37c81da4)
* 28: [IP Masquerade Agent User Guide](#pg-b45f024608e1b367cdacb1fd9d77278a)
* 29: [Limit Storage Consumption](#pg-a02f35804917d7a269c38d7e2c475005)
* 30: [Migrate Replicated Control Plane To Use Cloud Controller Manager](#pg-a24171610b6ea75a142cb9c8c7882390)
* 31: [Operating etcd clusters for Kubernetes](#pg-c4d0832845adc92b7ccd54aed63fc932)
* 32: [Reserve Compute Resources for System Daemons](#pg-b64a1d2bb3f4ed9f7021134e09a75c36)
* 33: [Running Kubernetes Node Components as a Non-root User](#pg-f6f3b8f9789fda4286bf410b8e108f69)
* 34: [Safely Drain a Node](#pg-b35b8ddb9bbc15620ce9636f4346c05c)
* 35: [Securing a Cluster](#pg-12001be83d15fcd7f3242313a55777df)
* 36: [Set Kubelet Parameters Via A Configuration File](#pg-f58763cc9447491b6c40f939a02d441d)
* 37: [Share a Cluster with Namespaces](#pg-1e966f5d0540bbee0876f9d0d08d54dc)
* 38: [Upgrade A Cluster](#pg-fe6b50655c29ab0b7c1ee549ff64c138)
* 39: [Use Cascading Deletion in a Cluster](#pg-4e9de5bc3973e5d2bb8f09ff940c3319)
* 40: [Using a KMS provider for data encryption](#pg-669c88964b4a9eb2b040057266e4b60d)
* 41: [Using CoreDNS for Service Discovery](#pg-e1afcdac8d5e8458274b3c481c5ebcda)
* 42: [Using NodeLocal DNSCache in Kubernetes Clusters](#pg-9ceed97f912df7289ed8872e290cfbad)
* 43: [Using sysctls in a Kubernetes Cluster](#pg-fe5ad73163d38596340536ec03a205f0)
* 44: [Utilizing the NUMA-aware Memory Manager](#pg-778055e4a4415ca195169b42cd42ddf9)
* 45: [Verify Signed Kubernetes Artifacts](#pg-6019e3a8a90c485fd4ffbd38936c8e1b)
