This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/reference/).

# Reference

* 1: [Glossary](#pg-2b03679960950df772fb4fe7d78427b9)
* 2: [API Overview](#pg-882c82a32bfb4d7946585a93a966b442)

+ 2.1: [Declarative API Validation](#pg-55e3e828cf0a62d4d6cb59517678b254)
+ 2.2: [Kubernetes API Concepts](#pg-2b5428a2ff6f4831fd972ef50e12b3eb)
+ 2.3: [Server-Side Apply](#pg-040d9484db673074f1b8ba3465be9d91)
+ 2.4: [Client Libraries](#pg-79880efc25dc8cb3b6962ad78a964319)
+ 2.5: [Common Expression Language in Kubernetes](#pg-f0fd9899edb7b5a099fe73472c94f83b)
+ 2.6: [Kubernetes Deprecation Policy](#pg-8d2ce3e7b2223cda0ccd428f4d5ea24b)
+ 2.7: [Deprecated API Migration Guide](#pg-2479c39af50fd55b898a3bcfb5988077)
+ 2.8: [Kubernetes API health endpoints](#pg-e4dbb59f8f23854d7b7d574e169923c4)

* 3: [API Access Control](#pg-99b26586d8a33ec06996dcf7892a9683)

+ 3.1: [Authenticating](#pg-a6264859a5ad6e2f4a6e4cff9ce4fa8b)
+ 3.2: [Authenticating with Bootstrap Tokens](#pg-de45b6ca7419a0e308044425b2ac52bb)
+ 3.3: [Authorization](#pg-342be69d36f174f762c36f4fe11fcb20)
+ 3.4: [Using RBAC Authorization](#pg-954776b47f2d90515f375623a0ce98e1)
+ 3.5: [Using Node Authorization](#pg-9cbb97d4d9f08d67931a1baae4e6519c)
+ 3.6: [Webhook Mode](#pg-215c25173044b8f97e9b0494b0c7e53f)
+ 3.7: [Using ABAC Authorization](#pg-a5bdc757c01991e5e6ab1a82b90639ea)
+ 3.8: [Admission Control in Kubernetes](#pg-518807b9b00bda46d7c7e6e0b17c18f8)
+ 3.9: [Dynamic Admission Control](#pg-d04751f776f1faa6a82bbb7f0a200950)
+ 3.10: [Managing Service Accounts](#pg-bea207258f3576b8ec7444a20d498e1d)
+ 3.11: [Certificates and Certificate Signing Requests](#pg-3d0c14d1e3cfade38febc343cd044c73)
+ 3.12: [Mapping PodSecurityPolicies to Pod Security Standards](#pg-643e4cec52a8577e9454649bdaac84d0)
+ 3.13: [Kubelet authentication/authorization](#pg-36e1423f0b5caa8eafeb6f53c175d13c)
+ 3.14: [TLS bootstrapping](#pg-d17c42b1760f6d5c333fc91ca9b453f4)
+ 3.15: [Mutating Admission Policy](#pg-d3609999485b1c57de7445f9a47d9799)
+ 3.16: [Validating Admission Policy](#pg-7b9fccf8215aea0edc5c97e72f1f72e4)

* 4: [Well-Known Labels, Annotations and Taints](#pg-e7512a333ae98d32429d24b2290eb15a)

+ 4.1: [Audit Annotations](#pg-0adf63217075ed2dc0a3030d9673e75e)

* 5: [Kubernetes API](#pg-60a16da3955f1de774f1f8dd756f2251)

+ 5.1: [Workload Resources](#pg-5037aed176781855678f89b4c21626ac)

- 5.1.1: [Pod](#pg-9cfc6ce767da10486ac184e3cf34abd4)
- 5.1.2: [Binding](#pg-c553e5f0b22c985719b26560b2dbe883)
- 5.1.3: [PodTemplate](#pg-af1995b54121f96a81a8c51fecc4f6f7)
- 5.1.4: [ReplicationController](#pg-888377326f4cd6e3d527f8dbb5ba81a0)
- 5.1.5: [ReplicaSet](#pg-803e8dd9be7ea099609d5c9af16d670f)
- 5.1.6: [Deployment](#pg-2c16e10bbf4113c1d2bb657311819771)
- 5.1.7: [StatefulSet](#pg-eb1ab4c03629d6617cc006c8c38b7424)
- 5.1.8: [ControllerRevision](#pg-203ad280adf3207ae06a933d6a78e464)
- 5.1.9: [DaemonSet](#pg-4efed40f98f8b85058d5aa64c1b40b99)
- 5.1.10: [Job](#pg-83b80f201ab5dccbbde519b7edc641ea)
- 5.1.11: [CronJob](#pg-661762555507aff4c6bde1090179871f)
- 5.1.12: [HorizontalPodAutoscaler](#pg-dc6f15a65358762dd1015f9f080829a0)
- 5.1.13: [HorizontalPodAutoscaler](#pg-6f6ef06d1cb2905e654485f2aeb99500)
- 5.1.14: [PriorityClass](#pg-707d238ce24c4c3026aa7ef29968e3f7)
- 5.1.15: [DeviceTaintRule v1alpha3](#pg-a98f48cbb209f59cc24ced6639a05617)
- 5.1.16: [ResourceClaim](#pg-f355e198d9a2dac379939d68cbd551b6)
- 5.1.17: [ResourceClaimTemplate](#pg-0c6741023480dfe4f4fe8dcf4ff799ca)
- 5.1.18: [ResourceSlice](#pg-fedca46b95ce3331f7a821c150868d3d)

+ 5.2: [Service Resources](#pg-54e55c546ba2153921dc8b78bafd699e)

- 5.2.1: [Service](#pg-106baf3be98dce0a42ad9ea7df796679)
- 5.2.2: [Endpoints](#pg-3f9a97d28a4b596c8d33d230e2b3dd6e)
- 5.2.3: [EndpointSlice](#pg-c9e5f15a68e325ce17ea168bcabd33e5)
- 5.2.4: [Ingress](#pg-734ceb8f9e59bff318dc526882eb5dcd)
- 5.2.5: [IngressClass](#pg-3420962b87b77851810c3aa8baad9578)

+ 5.3: [Config and Storage Resources](#pg-ef67581d88f69ea15be11159c033f33b)

- 5.3.1: [ConfigMap](#pg-109fa09dec8516f460dc1668c66df57c)
- 5.3.2: [Secret](#pg-7d0599aac497db82ee78fddbc549c01d)
- 5.3.3: [CSIDriver](#pg-e9fc1d0635b78d89359345fdb7789971)
- 5.3.4: [CSINode](#pg-e54ab698c244de7268acca37e4e6e97e)
- 5.3.5: [CSIStorageCapacity](#pg-ef7970bd9ecd532052dd386f88184c25)
- 5.3.6: [PersistentVolumeClaim](#pg-b0df9d7d300647dc0b5ebef6492f379c)
- 5.3.7: [PersistentVolume](#pg-876f3f471c6ce2412361e722f45723ce)
- 5.3.8: [StorageClass](#pg-6594b40b9d2889c78aa24c990663c227)
- 5.3.9: [StorageVersionMigration v1alpha1](#pg-dbe3aa619201b74ef9be9b542d63033f)
- 5.3.10: [Volume](#pg-21d04f929a407332d3e23a09718e07f6)
- 5.3.11: [VolumeAttachment](#pg-4bfa6511c37446f7b8f7ff7643983981)
- 5.3.12: [VolumeAttributesClass](#pg-543251f0d516d271b298c891f3850a1c)

+ 5.4: [Authentication Resources](#pg-6a5e06a0dc59d104938425c049f2f29b)

- 5.4.1: [ServiceAccount](#pg-6449724e786cbecd0cecfaa5a486e64a)
- 5.4.2: [TokenRequest](#pg-71bfa3e84f86650d855ced711edc8b41)
- 5.4.3: [TokenReview](#pg-4140627880f82c11a5e16b3c4043cfdb)
- 5.4.4: [CertificateSigningRequest](#pg-f9925c52e71befd56d9a92b04add148d)
- 5.4.5: [ClusterTrustBundle v1beta1](#pg-29cb58ecb38bd10360cfc10bc0672dbb)
- 5.4.6: [SelfSubjectReview](#pg-131d5179e884781bffb630c57b460b4c)
- 5.4.7: [PodCertificateRequest v1alpha1](#pg-ddbd52c4ab3aa6f027680a7da22d3bd3)

+ 5.5: [Authorization Resources](#pg-5362c9a7583eca653d4a705ba4e460ff)

- 5.5.1: [LocalSubjectAccessReview](#pg-253b0f85df0c0013b6476358e72b05f6)
- 5.5.2: [SelfSubjectAccessReview](#pg-3798a3911313b78a780825aa1a00827d)
- 5.5.3: [SelfSubjectRulesReview](#pg-ea1fed61553ac63709679a375b1ec442)
- 5.5.4: [SubjectAccessReview](#pg-5a4c4b387f450c2b81962bec144749fc)
- 5.5.5: [ClusterRole](#pg-4701a95c93d869e797bb11d9fc883748)
- 5.5.6: [ClusterRoleBinding](#pg-c05906bc1a365bcc4d4d92b4b3f4f192)
- 5.5.7: [Role](#pg-f0f12b8c869ff195f7b0b0388a88e76c)
- 5.5.8: [RoleBinding](#pg-337599e35c879ffc4ba442b2e98758e1)

+ 5.6: [Policy Resources](#pg-d8857a338d5c6dc04752576100c946d9)

- 5.6.1: [FlowSchema](#pg-110abb753da28a0607f71caf16be4fdb)
- 5.6.2: [LimitRange](#pg-0831e36c3a644ba6bb53595de785976d)
- 5.6.3: [ResourceQuota](#pg-10c2069205c27f566d7476dc73169165)
- 5.6.4: [NetworkPolicy](#pg-1e1d84ecddba19848ff49b8f10e5b3bc)
- 5.6.5: [PodDisruptionBudget](#pg-2e75f782721e263954f44aea4709a9d5)
- 5.6.6: [PriorityLevelConfiguration](#pg-eea647273acdc1d9223858cfe8f21d61)
- 5.6.7: [ValidatingAdmissionPolicy](#pg-fd6cee67d7f5c2d826beb614a7c8ccc8)
- 5.6.8: [ValidatingAdmissionPolicyBinding](#pg-64dfb2746a324d26e79583faefc60b21)
- 5.6.9: [MutatingAdmissionPolicy v1beta1](#pg-23d8ea73ec22d927ea142b80402279f4)
- 5.6.10: [MutatingAdmissionPolicyBinding v1alpha1](#pg-8edf917eb9494589bf9565c70671f0c5)

+ 5.7: [Extend Resources](#pg-020d8f776dea9802131630c210dc4c0a)

- 5.7.1: [CustomResourceDefinition](#pg-0a375cb95d28aa4cec341c561ccf6e83)
- 5.7.2: [DeviceClass](#pg-6f7b816bd453b6cde8f788547fbbb55c)
- 5.7.3: [MutatingWebhookConfiguration](#pg-ad24d230da8fe5a5c54bc6bff4169d24)
- 5.7.4: [ValidatingWebhookConfiguration](#pg-ad9945bc57d13986240173bdc1448f1b)

+ 5.8: [Cluster Resources](#pg-692a25c0f0c88fc9b8c1e82cd0b0ee9e)

- 5.8.1: [APIService](#pg-311b31c9ea6c6923cab8e14e36e62fbe)
- 5.8.2: [ComponentStatus](#pg-4fd67a09c76a0614445c034348adc0a7)
- 5.8.3: [Event](#pg-e034843297b0ae20140d70f0d6df2378)
- 5.8.4: [IPAddress](#pg-369adf9b113507e69a67ff98b4cf5612)
- 5.8.5: [Lease](#pg-7ac923a0ef2a5ce2605b428b72f9e5eb)
- 5.8.6: [LeaseCandidate v1beta1](#pg-13d5385e4e9d5c8af253f82fd5c4be50)
- 5.8.7: [Namespace](#pg-a96e40f7c68d5bb9604dcaa7f5b69d0b)
- 5.8.8: [Node](#pg-3ca7e8e10d76640701a022f9bac5e958)
- 5.8.9: [RuntimeClass](#pg-d1a53525d01a18b0dc630fcbc2411a03)
- 5.8.10: [ServiceCIDR](#pg-2a256669f171363c8a18e21f50eb2c3f)

+ 5.9: [Common Definitions](#pg-0a260d85a5da2504fce8c56b77c45024)

- 5.9.1: [DeleteOptions](#pg-9eba5edb3c1d93f9a74827e3a71014dd)
- 5.9.2: [LabelSelector](#pg-26234b02eb0546f7a178da9c373cb197)
- 5.9.3: [ListMeta](#pg-dbe3b11fb1cfde0aac65f945d84b11d6)
- 5.9.4: [LocalObjectReference](#pg-026383e0b43a68744a8b27a82bb4926d)
- 5.9.5: [NodeSelectorRequirement](#pg-deb2d19043a047688f72480af2f1b1e0)
- 5.9.6: [ObjectFieldSelector](#pg-47b6e1916665dd55bbeb2b33847653ed)
- 5.9.7: [ObjectMeta](#pg-77f040b7d1c00efcedc11902ed78fc08)
- 5.9.8: [ObjectReference](#pg-cf854f859540243f660c2798d641498c)
- 5.9.9: [Patch](#pg-1997570a6710a3eaf78270f2e2535167)
- 5.9.10: [Quantity](#pg-51b0e3fdb6e89030bd9e49dbb990918c)
- 5.9.11: [ResourceFieldSelector](#pg-406fd6938a5a3283ee7a816347603389)
- 5.9.12: [Status](#pg-b86f72d0a9c9625228b55ff79c154b63)
- 5.9.13: [TypedLocalObjectReference](#pg-ad5a39cd0d4233c0afb2a1daf17b95b3)

+ 5.10: [Other Resources](#pg-6ed026223d3453a6d1242c579dfbf000)

- 5.10.1: [MutatingAdmissionPolicyBindingList v1beta1](#pg-b6a8b05b60848f88f4446e5becc55301)

+ 5.11: [Common Parameters](#pg-6fbe4a9bf41cfee30909689bd978c45f)

* 6: [Instrumentation](#pg-be6e1435ecc8558659daa3f812da13cf)

+ 6.1: [Kubernetes Component SLI Metrics](#pg-d5514661bd5474ed823c8310529da4f4)
+ 6.2: [CRI Pod & Container Metrics](#pg-01fb8cecbb2dcedb719ff107091f2316)
+ 6.3: [Node metrics data](#pg-f80c94e2a1fba0c24275841ffe8ec997)
+ 6.4: [Understand Pressure Stall Information (PSI) Metrics](#pg-615447142024c1e5c2d46570dd6178bc)
+ 6.5: [Kubernetes z-pages](#pg-886a18c12183fc10f2fc6a45f692d79c)
+ 6.6: [Kubernetes Metrics Reference](#pg-cd2218537081bed07d532466e39c5c36)

* 7: [Kubernetes Issues and Security](#pg-af7c1f9168ec67f957edc504f43faf9a)

+ 7.1: [Kubernetes Issue Tracker](#pg-980c0542a3b195a20cfd4358792e2a38)
+ 7.2: [Kubernetes Security and Disclosure Information](#pg-1f7dc06f1cc1ea2cdde4480e54d5fb34)
+ 7.3: [Official CVE Feed](#pg-f8584cd3b29b891198316c53d71b787c)

* 8: [Node Reference Information](#pg-75e3b4b5f680fdd081dc8af8060a2bf7)

+ 8.1: [Kubelet Checkpoint API](#pg-e9c91b750d5dd5acbbdb9e49c89d35ad)
+ 8.2: [Linux Kernel Version Requirements](#pg-e9a4493b142cccdd4fcb813365f400bd)
+ 8.3: [Articles on dockershim Removal and on Using CRI-compatible Runtimes](#pg-26e96c9d268f9c39dfc525b98f477a12)
+ 8.4: [Node Labels Populated By The Kubelet](#pg-634210635d8574632684e291be646c98)
+ 8.5: [Local Files And Paths Used By The Kubelet](#pg-20fd618b4c6abae0d0bfdc090d8e6903)
+ 8.6: [Kubelet Configuration Directory Merging](#pg-c18723255166e0d71cef8eef93e5392c)
+ 8.7: [Kubelet Device Manager API Versions](#pg-a8efd942edb7bc78148bce3c5ec6db99)
+ 8.8: [Kubelet Systemd Watchdog](#pg-dee45174a808078522a57e09f33b8c43)
+ 8.9: [Node Status](#pg-8cc3d980ae362cd0e958120dd2072673)
+ 8.10: [Seccomp and Kubernetes](#pg-7bf7723707a2688483a1bde842667722)
+ 8.11: [Linux Node Swap Behaviors](#pg-cb8754a33c0f537d16742b006b8ff78f)

* 9: [Networking Reference](#pg-d423b2c0f223b2af56295d6ee5c3fb24)

+ 9.1: [Protocols for Services](#pg-a097017db59d2768c0422adcd3f79efd)
+ 9.2: [Ports and Protocols](#pg-5927c7cb60e78293efad3e86e45df77f)
+ 9.3: [Virtual IPs and Service Proxies](#pg-d59bf31808ffbe549a5b9ecfc354cfad)

* 10: [Setup tools](#pg-5bbbc5163b35431b3bff029ab9ec57d3)

+ 10.1: [Kubeadm](#pg-f351ced098abbb076bc8c4be1053672b)

- 10.1.1: [Kubeadm Generated](#pg-36c22b52e8447eb3d2452d4f56fbea9b)

* 10.1.1.1:
* 10.1.1.2:

+ 10.1.1.2.1:
+ 10.1.1.2.2:
+ 10.1.1.2.3:
+ 10.1.1.2.4:
+ 10.1.1.2.5:
+ 10.1.1.2.6:
+ 10.1.1.2.7:
+ 10.1.1.2.8:
+ 10.1.1.2.9:
+ 10.1.1.2.10:
+ 10.1.1.2.11:
+ 10.1.1.2.12:
+ 10.1.1.2.13:
+ 10.1.1.2.14:
+ 10.1.1.2.15:
+ 10.1.1.2.16:

* 10.1.1.3:

* 10.1.1.4:

+ 10.1.1.4.1:
+ 10.1.1.4.2:
+ 10.1.1.4.3:
+ 10.1.1.4.4:
+ 10.1.1.4.5:
+ 10.1.1.4.6:
+ 10.1.1.4.7:
+ 10.1.1.4.8:
+ 10.1.1.4.9:
+ 10.1.1.4.10:

* 10.1.1.5:

+ 10.1.1.5.1:
+ 10.1.1.5.2:
+ 10.1.1.5.3:
+ 10.1.1.5.4:
+ 10.1.1.5.5:
+ 10.1.1.5.6:
+ 10.1.1.5.7:
+ 10.1.1.5.8:
+ 10.1.1.5.9:
+ 10.1.1.5.10:
+ 10.1.1.5.11:
+ 10.1.1.5.12:
+ 10.1.1.5.13:
+ 10.1.1.5.14:
+ 10.1.1.5.15:
+ 10.1.1.5.16:
+ 10.1.1.5.17:
+ 10.1.1.5.18:
+ 10.1.1.5.19:
+ 10.1.1.5.20:
+ 10.1.1.5.21:
+ 10.1.1.5.22:
+ 10.1.1.5.23:
+ 10.1.1.5.24:
+ 10.1.1.5.25:
+ 10.1.1.5.26:
+ 10.1.1.5.27:
+ 10.1.1.5.28:
+ 10.1.1.5.29:
+ 10.1.1.5.30:
+ 10.1.1.5.31:
+ 10.1.1.5.32:
+ 10.1.1.5.33:
+ 10.1.1.5.34:
+ 10.1.1.5.35:
+ 10.1.1.5.36:
+ 10.1.1.5.37:
+ 10.1.1.5.38:
+ 10.1.1.5.39:
+ 10.1.1.5.40:
+ 10.1.1.5.41:
+ 10.1.1.5.42:
+ 10.1.1.5.43:
+ 10.1.1.5.44:
+ 10.1.1.5.45:
+ 10.1.1.5.46:

* 10.1.1.6:

+ 10.1.1.6.1:
+ 10.1.1.6.2:
+ 10.1.1.6.3:
+ 10.1.1.6.4:
+ 10.1.1.6.5:
+ 10.1.1.6.6:
+ 10.1.1.6.7:
+ 10.1.1.6.8:
+ 10.1.1.6.9:
+ 10.1.1.6.10:
+ 10.1.1.6.11:
+ 10.1.1.6.12:
+ 10.1.1.6.13:
+ 10.1.1.6.14:

* 10.1.1.7:

+ 10.1.1.7.1:

* 10.1.1.8:

+ 10.1.1.8.1:
+ 10.1.1.8.2:
+ 10.1.1.8.3:
+ 10.1.1.8.4:

* 10.1.1.9:

+ 10.1.1.9.1:
+ 10.1.1.9.2:
+ 10.1.1.9.3:
+ 10.1.1.9.4:

* 10.1.1.10:

+ 10.1.1.10.1:
+ 10.1.1.10.2:
+ 10.1.1.10.3:
+ 10.1.1.10.4:
+ 10.1.1.10.5:
+ 10.1.1.10.6:
+ 10.1.1.10.7:
+ 10.1.1.10.8:
+ 10.1.1.10.9:
+ 10.1.1.10.10:
+ 10.1.1.10.11:
+ 10.1.1.10.12:
+ 10.1.1.10.13:
+ 10.1.1.10.14:
+ 10.1.1.10.15:
+ 10.1.1.10.16:
+ 10.1.1.10.17:
+ 10.1.1.10.18:
+ 10.1.1.10.19:
+ 10.1.1.10.20:
+ 10.1.1.10.21:
+ 10.1.1.10.22:
+ 10.1.1.10.23:
+ 10.1.1.10.24:
+ 10.1.1.10.25:
+ 10.1.1.10.26:
+ 10.1.1.10.27:

* 10.1.1.11:

* 10.1.1.12:

- 10.1.2: [kubeadm init](#pg-82b2fcf985bae77dcb754387a9fcc64f)
- 10.1.3: [kubeadm join](#pg-2a2b5f34806b4b1bd2c12682ac170d68)
- 10.1.4: [kubeadm upgrade](#pg-2c20539d9fabf5982e2dd931742714bd)
- 10.1.5: [kubeadm upgrade phases](#pg-dfd085b5ab706bd84dda15847dd27f1b)
- 10.1.6: [kubeadm config](#pg-5042dc49c5348b3674d3878f37f7670b)
- 10.1.7: [kubeadm reset](#pg-6eb5bc1e7114609930a76c683cc27c2b)
- 10.1.8: [kubeadm token](#pg-516f4705fb2f5f62c76c7742772726a3)
- 10.1.9: [kubeadm version](#pg-34c4af6f36d969ed08ba840e7fb64c6d)
- 10.1.10: [kubeadm alpha](#pg-92a39c69c3689119dd5fa12886cb73a3)
- 10.1.11: [kubeadm certs](#pg-6a1fed09235bbf3644c804339928f10e)
- 10.1.12: [kubeadm init phase](#pg-fbe8dcd222ce5795a5c325670a26b067)
- 10.1.13: [kubeadm join phase](#pg-62a742c564b0b5b7ac12a95e67cc425a)
- 10.1.14: [kubeadm kubeconfig](#pg-1ab2d643d770ca684548de4ddbc7d8c4)
- 10.1.15: [kubeadm reset phase](#pg-b969d0033ce5d9036463521fb1f150b3)
- 10.1.16: [Implementation details](#pg-455b6412a275b743ee8ad90f35808393)

* 11: [Command line tool (kubectl)](#pg-03460a7254c6c73eb2a1bb3dd7d25910)

+ 11.1: [Introduction to kubectl](#pg-b2faf0db34da634aff4d681164922d6a)
+ 11.2: [kubectl Quick Reference](#pg-0437e83631175effa44e8c516c5adbda)
+ 11.3: [kubectl reference](#pg-e1b5cca32613cabad88dbdcefd80e2c9)

- 11.3.1: [kubectl](#pg-402909613e0ae370b616c0caac29621f)
- 11.3.2: [kubectl annotate](#pg-36ff86c01e1c63f208a2d2d1db6b6a4f)

- 11.3.3: [kubectl api-resources](#pg-8ecdd5ca9c4f7724f144aa46a98e0ec9)

- 11.3.4: [kubectl api-versions](#pg-5f872ac31510d52a53ab72cea7fa29cf)

- 11.3.5: [kubectl apply](#pg-3eea9e13de34e9bb4ad11c9c30bd249c)

* 11.3.5.1: [kubectl apply edit-last-applied](#pg-641acfde6e8164afe190eb62ae5c205d)
* 11.3.5.2: [kubectl apply set-last-applied](#pg-e1a3553640a80681da6b4bbe66760ab3)
* 11.3.5.3: [kubectl apply view-last-applied](#pg-c4d0a4727091a0e42ffa9cf8a0ad2329)

- 11.3.6: [kubectl attach](#pg-0e29e49eae92a6e42de742686ece8e59)

- 11.3.7: [kubectl auth](#pg-5c6cdd7674d19af1f0ed5161db1abb07)

* 11.3.7.1: [kubectl auth can-i](#pg-9fd383dbd061a4bd429962c0884141dc)
* 11.3.7.2: [kubectl auth reconcile](#pg-b63cd4df7b8fc6f18e4e048aca007433)
* 11.3.7.3: [kubectl auth whoami](#pg-55334cff1ad1de8913da0e79bd424c99)

- 11.3.8: [kubectl autoscale](#pg-b4d81752c4bebc716cf5a6621248ddbf)

- 11.3.9: [kubectl certificate](#pg-b0655c69bc929ffef16ad59fb060e9b0)

* 11.3.9.1: [kubectl certificate approve](#pg-7470128dc60bc72d430ee382f36ef6d3)
* 11.3.9.2: [kubectl certificate deny](#pg-c27805149b129dc7843215976f95fc68)

- 11.3.10: [kubectl cluster-info](#pg-35437a08dd53ca5d9e79117020a6856a)

* 11.3.10.1: [kubectl cluster-info dump](#pg-2b6cbcd733c21832d8ebf57781964754)

- 11.3.11: [kubectl completion](#pg-1c563fdb012166230fcf8d4b4ae572cd)

- 11.3.12: [kubectl config](#pg-e93d0796f4e6f7df1ab6fe9f32d32af3)

* 11.3.12.1: [kubectl config current-context](#pg-5014b54facef233a63885234ce91c3aa)
* 11.3.12.2: [kubectl config delete-cluster](#pg-aecc079c7de2d3be561601daf1d6684c)
* 11.3.12.3: [kubectl config delete-context](#pg-b5f24b4e3009ebba0a0f4ad35af0d4ab)
* 11.3.12.4: [kubectl config delete-user](#pg-d77b4cbd068f250f86cff5c2e75dabda)
* 11.3.12.5: [kubectl config get-clusters](#pg-1176518e0a720b52609f27e88abef8eb)
* 11.3.12.6: [kubectl config get-contexts](#pg-f96682991dc356384f3888c21b013cd6)
* 11.3.12.7: [kubectl config get-users](#pg-3a4916efcdffdb896b4619a1a5cbd87b)
* 11.3.12.8: [kubectl config rename-context](#pg-4f49ec6f9e1def05f72cfd83d8e26f34)
* 11.3.12.9: [kubectl config set](#pg-fddfa538835c3f9a09666f6713f07278)
* 11.3.12.10: [kubectl config set-cluster](#pg-c6f09b5a087eb07fce8acb3d3db38e22)
* 11.3.12.11: [kubectl config set-context](#pg-2500189be627eaffa4b161af5dd9a178)
* 11.3.12.12: [kubectl config set-credentials](#pg-b3b6ccdb55698e26fcd43bf215002c58)
* 11.3.12.13: [kubectl config unset](#pg-f82900d692231ec20a5fc6465c06e298)
* 11.3.12.14: [kubectl config use-context](#pg-f6ec7b5627422d529c65ee106681fea2)
* 11.3.12.15: [kubectl config view](#pg-3bfacbe2914206676749a842aa0d00f2)

- 11.3.13: [kubectl cordon](#pg-114515632079608ac9c1631e3bd46aaa)

- 11.3.14: [kubectl cp](#pg-281884941d738cd8fa58091afa664824)

- 11.3.15: [kubectl create](#pg-953771ff28f42694f3cccf8b294bbee0)

* 11.3.15.1: [kubectl create clusterrole](#pg-bc9f354d308d4b7b92bd1e2c199dd4d1)
* 11.3.15.2: [kubectl create clusterrolebinding](#pg-b580bc796e16cf5c330344854759b767)
* 11.3.15.3: [kubectl create configmap](#pg-d7a078683e8028884681580d3da9c355)
* 11.3.15.4: [kubectl create cronjob](#pg-8623e760bcd816213276f920925c7c9f)
* 11.3.15.5: [kubectl create deployment](#pg-85938a5e506af5d05edc154a7ba45ee7)
* 11.3.15.6: [kubectl create ingress](#pg-454f37b7a4a10acbcb73ee1faefe7ba6)
* 11.3.15.7: [kubectl create job](#pg-962e637e4ac9ca350d8717c056c77268)
* 11.3.15.8: [kubectl create namespace](#pg-8b99d360d189a763d8828d8dad70db8a)
* 11.3.15.9: [kubectl create poddisruptionbudget](#pg-1e27a1c88d08b9addd57196b0559c087)
* 11.3.15.10: [kubectl create priorityclass](#pg-ba25e70aa569d978cd2bec9f32ce0dba)
* 11.3.15.11: [kubectl create quota](#pg-e28159f2e6cb8aa3120d1e88a2e3e404)
* 11.3.15.12: [kubectl create role](#pg-01fc591ca5a786b8d3ed390ef6b72ad5)
* 11.3.15.13: [kubectl create rolebinding](#pg-df4b1aa40a6f6a6f8645261cacb35972)
* 11.3.15.14: [kubectl create secret](#pg-de61418fe2b7a032a7336d6c27fb27be)
* 11.3.15.15: [kubectl create secret docker-registry](#pg-76970ddfe96bc2cf910756946387250e)
* 11.3.15.16: [kubectl create secret generic](#pg-68b32a259fda3582817081388caa0330)
* 11.3.15.17: [kubectl create secret tls](#pg-4033b20aaa417f9e2081d96419a6ee45)
* 11.3.15.18: [kubectl create service](#pg-e0cf2bf7674d167398f315e6a67e1379)
* 11.3.15.19: [kubectl create service clusterip](#pg-8b94cb3a05077a406591bf6b1886edc2)
* 11.3.15.20: [kubectl create service externalname](#pg-d5f597b1de53f09bf2bea1855a981247)
* 11.3.15.21: [kubectl create service loadbalancer](#pg-a1edd453dd57d18385eb35c8e33431a4)
* 11.3.15.22: [kubectl create service nodeport](#pg-a0df1e98366de5c5261e1414770c68f9)
* 11.3.15.23: [kubectl create serviceaccount](#pg-811bd5ff9c057c6c3e7755acabbc824a)
* 11.3.15.24: [kubectl create token](#pg-ee534c7541a0919bdd14e6411d8067b8)

- 11.3.16: [kubectl debug](#pg-b034a7678879340ad25bafdd9551d22a)

- 11.3.17: [kubectl delete](#pg-ab346c76d590e8ad07e20fccaa45c980)

- 11.3.18: [kubectl describe](#pg-b2c625f46a85287d2c0551154b769024)

- 11.3.19: [kubectl diff](#pg-7eaa64344ffe7b4fb8fb0752f1b97d9f)

- 11.3.20: [kubectl drain](#pg-aa964bf4ff4621badcc87e1cd0e32681)

- 11.3.21: [kubectl edit](#pg-8cf21077f8795e0b16fde83d11567578)

- 11.3.22: [kubectl events](#pg-a88e5c3601e2bf7b0293034f5e81e821)

- 11.3.23: [kubectl exec](#pg-882aa52820297ac9293dd44da8672f3e)

- 11.3.24: [kubectl explain](#pg-41e90bac90aec872d864dcc94d5b90f8)

- 11.3.25: [kubectl expose](#pg-5775bf192e6208ef0a2b85dfc8a7d38a)

- 11.3.26: [kubectl get](#pg-34144509b7c5215e39120b601448cc40)

- 11.3.27: [kubectl kustomize](#pg-92353483fed3c33db48f9bc79e3d023c)

- 11.3.28: [kubectl label](#pg-f5c069064e2fcd06616d62599428f308)

- 11.3.29: [kubectl logs](#pg-ac35b1a6ed39fbe561feef25dc882275)

- 11.3.30: [kubectl options](#pg-b2b46c4956d34ec270e4c76b5d05c493)

- 11.3.31: [kubectl patch](#pg-30e2662613e2fd6dd67f08bc734a6ad5)

- 11.3.32: [kubectl plugin](#pg-997eb0d8f0bb60112e8d0b0b0d46ef14)

* 11.3.32.1: [kubectl plugin list](#pg-4025c6d57b4a953ffeb1dbaf8a201201)

- 11.3.33: [kubectl port-forward](#pg-6d0ce5cb4810fe1ec32c075d9b8e31ba)

- 11.3.34: [kubectl proxy](#pg-9133e2fab485b02227c141ef2c8b86f1)

- 11.3.35: [kubectl replace](#pg-836e50cbd85466dc75e3134956ff3aea)

- 11.3.36: [kubectl rollout](#pg-e8086f0539497d9723d72fa8b5f54952)

* 11.3.36.1: [kubectl rollout history](#pg-feee355d0921a2dae193326b4569c1c4)
* 11.3.36.2: [kubectl rollout pause](#pg-a45554a76bb1970815575b0d0eb8eb78)
* 11.3.36.3: [kubectl rollout restart](#pg-dff2e5df7176c0f397625767a6624bf4)
* 11.3.36.4: [kubectl rollout resume](#pg-a2718a937a9d531c87d0c31ba738c112)
* 11.3.36.5: [kubectl rollout status](#pg-5162a0abebfda06de0129978dff33fa3)
* 11.3.36.6: [kubectl rollout undo](#pg-decea050af73d7440fc036efb9ff569f)

- 11.3.37: [kubectl run](#pg-7e05911b36fcf1c8870f9debcb704446)

- 11.3.38: [kubectl scale](#pg-e363c273030dec7915a0dcd2f0e5a4f0)

- 11.3.39: [kubectl set](#pg-366c76c7b3d5aaa4bfbb45015d99bf15)

* 11.3.39.1: [kubectl set env](#pg-8efccafb687ee15419a3c10a01f52499)
* 11.3.39.2: [kubectl set image](#pg-5f280fa194c35dcc401bf7a8b16df02d)
* 11.3.39.3: [kubectl set resources](#pg-bd8b811c676cdb149ca3cad198624d9f)
* 11.3.39.4: [kubectl set selector](#pg-affb9944665fc880f3ebb6edf7673214)
* 11.3.39.5: [kubectl set serviceaccount](#pg-3118ff763cfaafe03d807a502e48e967)
* 11.3.39.6: [kubectl set subject](#pg-e9c5704d912a656bcc627016d1045699)

- 11.3.40: [kubectl taint](#pg-584242a5667621cd3d0ce458d12e10bc)

- 11.3.41: [kubectl top](#pg-de8407a2eccd93c98c5b0eca954fb881)

* 11.3.41.1: [kubectl top node](#pg-24aaff2b409245e171479e8dd8790013)
* 11.3.41.2: [kubectl top pod](#pg-765f5bf8510a311aaa87e1027328a2ef)

- 11.3.42: [kubectl uncordon](#pg-8c1849e7de1aec914e31a94c032a0f6a)

- 11.3.43: [kubectl version](#pg-ad13feebe933b7228fb9472fc822a3c0)

- 11.3.44: [kubectl wait](#pg-1bf01c4ed4581610178c3f20a5cd043f)

+ 11.4: [kubectl Commands](#pg-d7ffbf04ffbefb241fd0722423b80f5a)
+ 11.5: [kubectl](#pg-4d3e62632c189fcc3c1357cd8fb8799c)
+ 11.6: [JSONPath Support](#pg-a938176c695852fe70362c29cf615f1c)
+ 11.7: [kubectl for Docker Users](#pg-a7abc09192597e614b58f8b552b682f5)
+ 11.8: [kubectl Usage Conventions](#pg-8de6aceb8bf692c06cced446bac5bc92)
+ 11.9: [Kubectl user preferences (kuberc)](#pg-0fb24477397db8dd277afb2477c199dd)

* 12: [Component tools](#pg-54e562dd1441d0195970a6526b0055cc)

+ 12.1: [Feature Gates](#pg-1436dcc6f9d8b5fe35487f0066837d64)
+ 12.2: [Feature Gates (removed)](#pg-96fc6f4d1ede7ee94aca236cb6d46ed7)
+ 12.3: [kube-apiserver](#pg-ec8ff2888d36f533a57bc9704ccc84e0)
+ 12.4: [kube-controller-manager](#pg-8a37271ec8fd36a3a1ce07c4c58533d9)
+ 12.5: [kube-proxy](#pg-a727de6cb5a090d5f115f88a8606c438)
+ 12.6: [kube-scheduler](#pg-57e59e5ddd9db63da6c9d27cc0e2f254)
+ 12.7: [kubelet](#pg-29e506a6018204679ef5459653a7aa1f)

* 13: [Debug cluster](#pg-f5e3f59e47a573df1635ccb70c8f8cad)

+ 13.1: [Flow control](#pg-9cfe3b0b8b8f3f9e554a1e2ee560a46b)

* 14: [Configuration APIs](#pg-a6ae13190e147ef3922315c2091fc258)

+ 14.1: [Client Authentication (v1)](#pg-eee842643d4d2c372827920430a15614)
+ 14.2: [Client Authentication (v1beta1)](#pg-2896357fe4f62fe85522254410e0be7d)
+ 14.3: [Event Rate Limit Configuration (v1alpha1)](#pg-a63fdf5efd92a82e9c74e1e086e59c3e)
+ 14.4: [Image Policy API (v1alpha1)](#pg-3359f37c1d47e9efe5555937171c3227)
+ 14.5: [kube-apiserver Admission (v1)](#pg-ef75124a98543fc30b338602545da70a)
+ 14.6: [kube-apiserver Audit Configuration (v1)](#pg-8f61883225b6bed85530d1904e148392)
+ 14.7: [kube-apiserver Configuration (v1)](#pg-fd52840184e93a463355aa21a234f263)
+ 14.8: [kube-apiserver Configuration (v1alpha1)](#pg-e9edd8df1106a991be062e37a9ef87b5)
+ 14.9: [kube-apiserver Configuration (v1beta1)](#pg-d92eb02c31646417b35f1898c493a36c)
+ 14.10: [kube-controller-manager Configuration (v1alpha1)](#pg-80f3f227cdfc44d67208fbe8001af13b)
+ 14.11: [kube-proxy Configuration (v1alpha1)](#pg-d8644f8d8b33ff33a31c8b55065eaf37)
+ 14.12: [kube-scheduler Configuration (v1)](#pg-456399fc52f4b81000285e4118542dfc)
+ 14.13: [kubeadm Configuration (v1beta3)](#pg-675226e13e76ef189fe0156f7e52353a)
+ 14.14: [kubeadm Configuration (v1beta4)](#pg-96ac0666f26a002755c81158ce435e6e)
+ 14.15: [kubeconfig (v1)](#pg-963f6a9661fe1ce08bf0c65359b64f2a)
+ 14.16: [Kubelet Configuration (v1)](#pg-6f5d995aeb7dcbb37b50b6689cee9a2c)
+ 14.17: [Kubelet Configuration (v1alpha1)](#pg-f0a175531432662368ed2e01f663b35f)
+ 14.18: [Kubelet Configuration (v1beta1)](#pg-aaa2b8b78fe84a05914c155652d10956)
+ 14.19: [Kubelet CredentialProvider (v1)](#pg-bc515669f6b02d98ca764bff45029cc1)
+ 14.20: [kuberc (v1alpha1)](#pg-05447aa481aeb4888a9a7ec4366d44f6)
+ 14.21: [kuberc (v1beta1)](#pg-3e22ef4b89afba585ddcc7ee3f173db3)
+ 14.22: [WebhookAdmission Configuration (v1)](#pg-74f43b2a33c21414f1ed8c359b37d326)

* 15: [External APIs](#pg-0fd8e15a5e53d7690dca14e42d45d583)

+ 15.1: [Kubernetes Custom Metrics (v1beta2)](#pg-f1c8b4f958fda36c18b6c443756e3292)
+ 15.2: [Kubernetes External Metrics (v1beta1)](#pg-a241970449621c942f37d58d1e3cc348)
+ 15.3: [Kubernetes Metrics (v1beta1)](#pg-9979560e9d76a835617d8d8e775f58fb)

* 16: [Scheduling](#pg-f8b023454daa9497b7eea35b7d35c075)

+ 16.1: [Scheduler Configuration](#pg-ef4fb938b6b63c95f5f26f9b1cec3054)
+ 16.2: [Scheduling Policies](#pg-5a0a68fb6a7ffefb6d5f861100fa0ae3)

* 17: [Other Tools](#pg-c808ce38575e73f72835d7ed02b03780)

This section of the Kubernetes documentation contains references.

## API Reference

* [Glossary](/docs/reference/glossary/) - a comprehensive, standardized list of Kubernetes terminology
* [Kubernetes API Reference](/docs/reference/kubernetes-api/)
* [One-page API Reference for Kubernetes v1.34](/docs/reference/generated/kubernetes-api/v1.34/)
* [Using The Kubernetes API](/docs/reference/using-api/) - overview of the API for Kubernetes.
* [API access control](/docs/reference/access-authn-authz/) - details on how Kubernetes controls API access
* [Well-Known Labels, Annotations and Taints](/docs/reference/labels-annotations-taints/)

## Officially supported client libraries

To call the Kubernetes API from a programming language, you can use
[client libraries](/docs/reference/using-api/client-libraries/). Officially supported
client libraries:

* [Kubernetes Go client library](https://github.com/kubernetes/client-go/)
* [Kubernetes Python client library](https://github.com/kubernetes-client/python)
* [Kubernetes Java client library](https://github.com/kubernetes-client/java)
* [Kubernetes JavaScript client library](https://github.com/kubernetes-client/javascript)
* [Kubernetes C# client library](https://github.com/kubernetes-client/csharp)
* [Kubernetes Haskell client library](https://github.com/kubernetes-client/haskell)

## CLI

* [kubectl](/docs/reference/kubectl/) - Main CLI tool for running commands and managing Kubernetes clusters.
  + [JSONPath](/docs/reference/kubectl/jsonpath/) - Syntax guide for using [JSONPath expressions](https://goessner.net/articles/JsonPath/) with kubectl.
* [kubeadm](/docs/reference/setup-tools/kubeadm/) - CLI tool to easily provision a secure Kubernetes cluster.

## Components

* [kubelet](/docs/reference/command-line-tools-reference/kubelet/) - The
  primary agent that runs on each node. The kubelet takes a set of PodSpecs
  and ensures that the described containers are running and healthy.
* [kube-apiserver](/docs/reference/command-line-tools-reference/kube-apiserver/) -
  REST API that validates and configures data for API objects such as pods,
  services, replication controllers.
* [kube-controller-manager](/docs/reference/command-line-tools-reference/kube-controller-manager/) -
  Daemon that embeds the core control loops shipped with Kubernetes.
* [kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/) - Can
  do simple TCP/UDP stream forwarding or round-robin TCP/UDP forwarding across
  a set of back-ends.
* [kube-scheduler](/docs/reference/command-line-tools-reference/kube-scheduler/) -
  Scheduler that manages availability, performance, and capacity.

  + [Scheduler Policies](/docs/reference/scheduling/policies/)
  + [Scheduler Profiles](/docs/reference/scheduling/config/#profiles)
* List of [ports and protocols](/docs/reference/networking/ports-and-protocols/) that
  should be open on control plane and worker nodes

## Config APIs

This section hosts the documentation for "unpublished" APIs which are used to
configure kubernetes components or tools. Most of these APIs are not exposed
by the API server in a RESTful way though they are essential for a user or an
operator to use or manage a cluster.

* [kubeconfig (v1)](/docs/reference/config-api/kubeconfig.v1/)
* [kuberc (v1alpha1)](/docs/reference/config-api/kuberc.v1alpha1/) and
  [kuberc (v1beta1)](/docs/reference/config-api/kuberc.v1beta1/)
* [kube-apiserver admission (v1)](/docs/reference/config-api/apiserver-admission.v1/)
* [kube-apiserver configuration (v1alpha1)](/docs/reference/config-api/apiserver-config.v1alpha1/) and
  [kube-apiserver configuration (v1beta1)](/docs/reference/config-api/apiserver-config.v1beta1/) and
  [kube-apiserver configuration (v1)](/docs/reference/config-api/apiserver-config.v1/)
* [kube-apiserver event rate limit (v1alpha1)](/docs/reference/config-api/apiserver-eventratelimit.v1alpha1/)
* [kubelet configuration (v1alpha1)](/docs/reference/config-api/kubelet-config.v1alpha1/) and
  [kubelet configuration (v1beta1)](/docs/reference/config-api/kubelet-config.v1beta1/) and
  [kubelet configuration (v1)](/docs/reference/config-api/kubelet-config.v1/)
* [kubelet credential providers (v1)](/docs/reference/config-api/kubelet-credentialprovider.v1/)
* [kube-scheduler configuration (v1)](/docs/reference/config-api/kube-scheduler-config.v1/)
* [kube-controller-manager configuration (v1alpha1)](/docs/reference/config-api/kube-controller-manager-config.v1alpha1/)
* [kube-proxy configuration (v1alpha1)](/docs/reference/config-api/kube-proxy-config.v1alpha1/)
* [`audit.k8s.io/v1` API](/docs/reference/config-api/apiserver-audit.v1/)
* [Client authentication API (v1beta1)](/docs/reference/config-api/client-authentication.v1beta1/) and
  [Client authentication API (v1)](/docs/reference/config-api/client-authentication.v1/)
* [WebhookAdmission configuration (v1)](/docs/reference/config-api/apiserver-webhookadmission.v1/)
* [ImagePolicy API (v1alpha1)](/docs/reference/config-api/imagepolicy.v1alpha1/)

## Config API for kubeadm

* [v1beta3](/docs/reference/config-api/kubeadm-config.v1beta3/)
* [v1beta4](/docs/reference/config-api/kubeadm-config.v1beta4/)

## External APIs

These are the APIs defined by the Kubernetes project, but are not implemented
by the core project:

* [Metrics API (v1beta1)](/docs/reference/external-api/metrics.v1beta1/)
* [Custom Metrics API (v1beta2)](/docs/reference/external-api/custom-metrics.v1beta2/)
* [External Metrics API (v1beta1)](/docs/reference/external-api/external-metrics.v1beta1/)

## Design Docs

An archive of the design docs for Kubernetes functionality. Good starting points are
[Kubernetes Architecture](https://git.k8s.io/design-proposals-archive/architecture/architecture.md) and
[Kubernetes Design Overview](https://git.k8s.io/design-proposals-archive).
