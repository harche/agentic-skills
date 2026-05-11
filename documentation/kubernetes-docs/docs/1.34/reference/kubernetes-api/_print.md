This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/reference/kubernetes-api/).

# Kubernetes API

* 1: [Workload Resources](#pg-5037aed176781855678f89b4c21626ac)

+ 1.1: [Pod](#pg-9cfc6ce767da10486ac184e3cf34abd4)
+ 1.2: [Binding](#pg-c553e5f0b22c985719b26560b2dbe883)
+ 1.3: [PodTemplate](#pg-af1995b54121f96a81a8c51fecc4f6f7)
+ 1.4: [ReplicationController](#pg-888377326f4cd6e3d527f8dbb5ba81a0)
+ 1.5: [ReplicaSet](#pg-803e8dd9be7ea099609d5c9af16d670f)
+ 1.6: [Deployment](#pg-2c16e10bbf4113c1d2bb657311819771)
+ 1.7: [StatefulSet](#pg-eb1ab4c03629d6617cc006c8c38b7424)
+ 1.8: [ControllerRevision](#pg-203ad280adf3207ae06a933d6a78e464)
+ 1.9: [DaemonSet](#pg-4efed40f98f8b85058d5aa64c1b40b99)
+ 1.10: [Job](#pg-83b80f201ab5dccbbde519b7edc641ea)
+ 1.11: [CronJob](#pg-661762555507aff4c6bde1090179871f)
+ 1.12: [HorizontalPodAutoscaler](#pg-dc6f15a65358762dd1015f9f080829a0)
+ 1.13: [HorizontalPodAutoscaler](#pg-6f6ef06d1cb2905e654485f2aeb99500)
+ 1.14: [PriorityClass](#pg-707d238ce24c4c3026aa7ef29968e3f7)
+ 1.15: [DeviceTaintRule v1alpha3](#pg-a98f48cbb209f59cc24ced6639a05617)
+ 1.16: [ResourceClaim](#pg-f355e198d9a2dac379939d68cbd551b6)
+ 1.17: [ResourceClaimTemplate](#pg-0c6741023480dfe4f4fe8dcf4ff799ca)
+ 1.18: [ResourceSlice](#pg-fedca46b95ce3331f7a821c150868d3d)

* 2: [Service Resources](#pg-54e55c546ba2153921dc8b78bafd699e)

+ 2.1: [Service](#pg-106baf3be98dce0a42ad9ea7df796679)
+ 2.2: [Endpoints](#pg-3f9a97d28a4b596c8d33d230e2b3dd6e)
+ 2.3: [EndpointSlice](#pg-c9e5f15a68e325ce17ea168bcabd33e5)
+ 2.4: [Ingress](#pg-734ceb8f9e59bff318dc526882eb5dcd)
+ 2.5: [IngressClass](#pg-3420962b87b77851810c3aa8baad9578)

* 3: [Config and Storage Resources](#pg-ef67581d88f69ea15be11159c033f33b)

+ 3.1: [ConfigMap](#pg-109fa09dec8516f460dc1668c66df57c)
+ 3.2: [Secret](#pg-7d0599aac497db82ee78fddbc549c01d)
+ 3.3: [CSIDriver](#pg-e9fc1d0635b78d89359345fdb7789971)
+ 3.4: [CSINode](#pg-e54ab698c244de7268acca37e4e6e97e)
+ 3.5: [CSIStorageCapacity](#pg-ef7970bd9ecd532052dd386f88184c25)
+ 3.6: [PersistentVolumeClaim](#pg-b0df9d7d300647dc0b5ebef6492f379c)
+ 3.7: [PersistentVolume](#pg-876f3f471c6ce2412361e722f45723ce)
+ 3.8: [StorageClass](#pg-6594b40b9d2889c78aa24c990663c227)
+ 3.9: [StorageVersionMigration v1alpha1](#pg-dbe3aa619201b74ef9be9b542d63033f)
+ 3.10: [Volume](#pg-21d04f929a407332d3e23a09718e07f6)
+ 3.11: [VolumeAttachment](#pg-4bfa6511c37446f7b8f7ff7643983981)
+ 3.12: [VolumeAttributesClass](#pg-543251f0d516d271b298c891f3850a1c)

* 4: [Authentication Resources](#pg-6a5e06a0dc59d104938425c049f2f29b)

+ 4.1: [ServiceAccount](#pg-6449724e786cbecd0cecfaa5a486e64a)
+ 4.2: [TokenRequest](#pg-71bfa3e84f86650d855ced711edc8b41)
+ 4.3: [TokenReview](#pg-4140627880f82c11a5e16b3c4043cfdb)
+ 4.4: [CertificateSigningRequest](#pg-f9925c52e71befd56d9a92b04add148d)
+ 4.5: [ClusterTrustBundle v1beta1](#pg-29cb58ecb38bd10360cfc10bc0672dbb)
+ 4.6: [SelfSubjectReview](#pg-131d5179e884781bffb630c57b460b4c)
+ 4.7: [PodCertificateRequest v1alpha1](#pg-ddbd52c4ab3aa6f027680a7da22d3bd3)

* 5: [Authorization Resources](#pg-5362c9a7583eca653d4a705ba4e460ff)

+ 5.1: [LocalSubjectAccessReview](#pg-253b0f85df0c0013b6476358e72b05f6)
+ 5.2: [SelfSubjectAccessReview](#pg-3798a3911313b78a780825aa1a00827d)
+ 5.3: [SelfSubjectRulesReview](#pg-ea1fed61553ac63709679a375b1ec442)
+ 5.4: [SubjectAccessReview](#pg-5a4c4b387f450c2b81962bec144749fc)
+ 5.5: [ClusterRole](#pg-4701a95c93d869e797bb11d9fc883748)
+ 5.6: [ClusterRoleBinding](#pg-c05906bc1a365bcc4d4d92b4b3f4f192)
+ 5.7: [Role](#pg-f0f12b8c869ff195f7b0b0388a88e76c)
+ 5.8: [RoleBinding](#pg-337599e35c879ffc4ba442b2e98758e1)

* 6: [Policy Resources](#pg-d8857a338d5c6dc04752576100c946d9)

+ 6.1: [FlowSchema](#pg-110abb753da28a0607f71caf16be4fdb)
+ 6.2: [LimitRange](#pg-0831e36c3a644ba6bb53595de785976d)
+ 6.3: [ResourceQuota](#pg-10c2069205c27f566d7476dc73169165)
+ 6.4: [NetworkPolicy](#pg-1e1d84ecddba19848ff49b8f10e5b3bc)
+ 6.5: [PodDisruptionBudget](#pg-2e75f782721e263954f44aea4709a9d5)
+ 6.6: [PriorityLevelConfiguration](#pg-eea647273acdc1d9223858cfe8f21d61)
+ 6.7: [ValidatingAdmissionPolicy](#pg-fd6cee67d7f5c2d826beb614a7c8ccc8)
+ 6.8: [ValidatingAdmissionPolicyBinding](#pg-64dfb2746a324d26e79583faefc60b21)
+ 6.9: [MutatingAdmissionPolicy v1beta1](#pg-23d8ea73ec22d927ea142b80402279f4)
+ 6.10: [MutatingAdmissionPolicyBinding v1alpha1](#pg-8edf917eb9494589bf9565c70671f0c5)

* 7: [Extend Resources](#pg-020d8f776dea9802131630c210dc4c0a)

+ 7.1: [CustomResourceDefinition](#pg-0a375cb95d28aa4cec341c561ccf6e83)
+ 7.2: [DeviceClass](#pg-6f7b816bd453b6cde8f788547fbbb55c)
+ 7.3: [MutatingWebhookConfiguration](#pg-ad24d230da8fe5a5c54bc6bff4169d24)
+ 7.4: [ValidatingWebhookConfiguration](#pg-ad9945bc57d13986240173bdc1448f1b)

* 8: [Cluster Resources](#pg-692a25c0f0c88fc9b8c1e82cd0b0ee9e)

+ 8.1: [APIService](#pg-311b31c9ea6c6923cab8e14e36e62fbe)
+ 8.2: [ComponentStatus](#pg-4fd67a09c76a0614445c034348adc0a7)
+ 8.3: [Event](#pg-e034843297b0ae20140d70f0d6df2378)
+ 8.4: [IPAddress](#pg-369adf9b113507e69a67ff98b4cf5612)
+ 8.5: [Lease](#pg-7ac923a0ef2a5ce2605b428b72f9e5eb)
+ 8.6: [LeaseCandidate v1beta1](#pg-13d5385e4e9d5c8af253f82fd5c4be50)
+ 8.7: [Namespace](#pg-a96e40f7c68d5bb9604dcaa7f5b69d0b)
+ 8.8: [Node](#pg-3ca7e8e10d76640701a022f9bac5e958)
+ 8.9: [RuntimeClass](#pg-d1a53525d01a18b0dc630fcbc2411a03)
+ 8.10: [ServiceCIDR](#pg-2a256669f171363c8a18e21f50eb2c3f)

* 9: [Common Definitions](#pg-0a260d85a5da2504fce8c56b77c45024)

+ 9.1: [DeleteOptions](#pg-9eba5edb3c1d93f9a74827e3a71014dd)
+ 9.2: [LabelSelector](#pg-26234b02eb0546f7a178da9c373cb197)
+ 9.3: [ListMeta](#pg-dbe3b11fb1cfde0aac65f945d84b11d6)
+ 9.4: [LocalObjectReference](#pg-026383e0b43a68744a8b27a82bb4926d)
+ 9.5: [NodeSelectorRequirement](#pg-deb2d19043a047688f72480af2f1b1e0)
+ 9.6: [ObjectFieldSelector](#pg-47b6e1916665dd55bbeb2b33847653ed)
+ 9.7: [ObjectMeta](#pg-77f040b7d1c00efcedc11902ed78fc08)
+ 9.8: [ObjectReference](#pg-cf854f859540243f660c2798d641498c)
+ 9.9: [Patch](#pg-1997570a6710a3eaf78270f2e2535167)
+ 9.10: [Quantity](#pg-51b0e3fdb6e89030bd9e49dbb990918c)
+ 9.11: [ResourceFieldSelector](#pg-406fd6938a5a3283ee7a816347603389)
+ 9.12: [Status](#pg-b86f72d0a9c9625228b55ff79c154b63)
+ 9.13: [TypedLocalObjectReference](#pg-ad5a39cd0d4233c0afb2a1daf17b95b3)

* 10: [Other Resources](#pg-6ed026223d3453a6d1242c579dfbf000)

+ 10.1: [MutatingAdmissionPolicyBindingList v1beta1](#pg-b6a8b05b60848f88f4446e5becc55301)

* 11: [Common Parameters](#pg-6fbe4a9bf41cfee30909689bd978c45f)

Kubernetes' API is the application that serves Kubernetes functionality through a RESTful interface and stores the state of the cluster.

Kubernetes resources and "records of intent" are all stored as API objects, and modified via RESTful calls to the API. The API allows configuration to be managed in a declarative way. Users can interact with the Kubernetes API directly, or via tools like `kubectl`. The core Kubernetes API is flexible and can also be extended to support custom resources.
