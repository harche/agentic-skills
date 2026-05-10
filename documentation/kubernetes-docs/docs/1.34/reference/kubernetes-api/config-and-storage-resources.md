# Config and Storage Resources

---

##### [ConfigMap](/docs/reference/kubernetes-api/config-and-storage-resources/config-map-v1/)

ConfigMap holds configuration data for pods to consume.

##### [Secret](/docs/reference/kubernetes-api/config-and-storage-resources/secret-v1/)

Secret holds secret data of a certain type.

##### [CSIDriver](/docs/reference/kubernetes-api/config-and-storage-resources/csi-driver-v1/)

CSIDriver captures information about a Container Storage Interface (CSI) volume driver deployed on the cluster.

##### [CSINode](/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/)

CSINode holds information about all CSI drivers installed on a node.

##### [CSIStorageCapacity](/docs/reference/kubernetes-api/config-and-storage-resources/csi-storage-capacity-v1/)

CSIStorageCapacity stores the result of one CSI GetCapacity call.

##### [PersistentVolumeClaim](/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/)

PersistentVolumeClaim is a user's request for and claim to a persistent volume.

##### [PersistentVolume](/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/)

PersistentVolume (PV) is a storage resource provisioned by an administrator.

##### [StorageClass](/docs/reference/kubernetes-api/config-and-storage-resources/storage-class-v1/)

StorageClass describes the parameters for a class of storage for which PersistentVolumes can be dynamically provisioned.

##### [StorageVersionMigration v1alpha1](/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/)

StorageVersionMigration represents a migration of stored data to the latest storage version.

##### [Volume](/docs/reference/kubernetes-api/config-and-storage-resources/volume/)

Volume represents a named volume in a pod that may be accessed by any container in the pod.

##### [VolumeAttachment](/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/)

VolumeAttachment captures the intent to attach or detach the specified volume to/from the specified node.

##### [VolumeAttributesClass](/docs/reference/kubernetes-api/config-and-storage-resources/volume-attributes-class-v1/)

VolumeAttributesClass represents a specification of mutable volume attributes defined by the CSI driver.

This page is automatically generated.

If you plan to report an issue with this page, mention that the page is auto-generated in your issue description. The fix may need to happen elsewhere in the Kubernetes project.

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
