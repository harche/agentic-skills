# Node-specific Volume Limits

This page describes the maximum number of volumes that can be attached
to a Node for various cloud providers.

Cloud providers like Google, Amazon, and Microsoft typically have a limit on
how many volumes can be attached to a Node. It is important for Kubernetes to
respect those limits. Otherwise, Pods scheduled on a Node could get stuck
waiting for volumes to attach.

## Kubernetes default limits

The Kubernetes scheduler has default limits on the number of volumes
that can be attached to a Node:

| Cloud service | Maximum volumes per Node |
| --- | --- |
| [Amazon Elastic Block Store (EBS)](https://aws.amazon.com/ebs/) | 39 |
| [Google Persistent Disk](https://cloud.google.com/persistent-disk/) | 16 |
| [Microsoft Azure Disk Storage](https://azure.microsoft.com/en-us/services/storage/main-disks/) | 16 |

## Dynamic volume limits

FEATURE STATE:
`Kubernetes v1.17 [stable]`

Dynamic volume limits are supported for following volume types.

* Amazon EBS
* Google Persistent Disk
* Azure Disk
* CSI

For volumes managed by in-tree volume plugins, Kubernetes automatically determines the Node
type and enforces the appropriate maximum number of volumes for the node. For example:

* On
  [Google Compute Engine](https://cloud.google.com/compute/),
  up to 127 volumes can be attached to a node, [depending on the node
  type](https://cloud.google.com/compute/docs/disks/#pdnumberlimits).
* For Amazon EBS disks on M5,C5,R5,T3 and Z1D instance types, Kubernetes allows only 25
  volumes to be attached to a Node. For other instance types on
  [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/),
  Kubernetes allows 39 volumes to be attached to a Node.
* On Azure, up to 64 disks can be attached to a node, depending on the node type. For more details, refer to [Sizes for virtual machines in Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes).
* If a CSI storage driver advertises a maximum number of volumes for a Node (using `NodeGetInfo`), the [kube-scheduler](/docs/reference/command-line-tools-reference/kube-scheduler/ "Control plane component that watches for newly created pods with no assigned node, and selects a node for them to run on.") honors that limit.
  Refer to the [CSI specifications](https://github.com/container-storage-interface/spec/blob/master/spec.md#nodegetinfo) for details.
* For volumes managed by in-tree plugins that have been migrated to a CSI driver, the maximum number of volumes will be the one reported by the CSI driver.

### Mutable CSI Node Allocatable Count

FEATURE STATE:
`Kubernetes v1.34 [beta]`(disabled by default)

CSI drivers can dynamically adjust the maximum number of volumes that can be attached to a Node at runtime. This enhances scheduling accuracy and reduces pod scheduling failures due to changes in resource availability.

To use this feature, you must enable the `MutableCSINodeAllocatableCount` feature gate on the following components:

* `kube-apiserver`
* `kubelet`

#### Periodic Updates

When enabled, CSI drivers can request periodic updates to their volume limits by setting the `nodeAllocatableUpdatePeriodSeconds` field in the `CSIDriver` specification. For example:

```
apiVersion: storage.k8s.io/v1
kind: CSIDriver
metadata:
  name: hostpath.csi.k8s.io
spec:
  nodeAllocatableUpdatePeriodSeconds: 60
```

Kubelet will periodically call the corresponding CSI driver’s `NodeGetInfo` endpoint to refresh the maximum number of attachable volumes, using the interval specified in `nodeAllocatableUpdatePeriodSeconds`. The minimum allowed value for this field is 10 seconds.

If a volume attachment operation fails with a `ResourceExhausted` error (gRPC code 8), Kubernetes triggers an immediate update to the allocatable volume count for that Node. Additionally, kubelet marks affected pods as Failed, allowing their controllers to handle recreation. This prevents pods from getting stuck indefinitely in the `ContainerCreating` state.

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
