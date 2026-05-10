# Volume Snapshot Classes

This document describes the concept of VolumeSnapshotClass in Kubernetes. Familiarity
with [volume snapshots](/docs/concepts/storage/volume-snapshots/) and
[storage classes](/docs/concepts/storage/storage-classes/) is suggested.

## Introduction

Just like StorageClass provides a way for administrators to describe the "classes"
of storage they offer when provisioning a volume, VolumeSnapshotClass provides a
way to describe the "classes" of storage when provisioning a volume snapshot.

## The VolumeSnapshotClass Resource

Each VolumeSnapshotClass contains the fields `driver`, `deletionPolicy`, and `parameters`,
which are used when a VolumeSnapshot belonging to the class needs to be
dynamically provisioned.

The name of a VolumeSnapshotClass object is significant, and is how users can
request a particular class. Administrators set the name and other parameters
of a class when first creating VolumeSnapshotClass objects, and the objects cannot
be updated once they are created.

> **Note:**
> Installation of the CRDs is the responsibility of the Kubernetes distribution.
> Without the required CRDs present, the creation of a VolumeSnapshotClass fails.

```
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: csi-hostpath-snapclass
driver: hostpath.csi.k8s.io
deletionPolicy: Delete
parameters:
```

Administrators can specify a default VolumeSnapshotClass for VolumeSnapshots
that don't request any particular class to bind to by adding the
`snapshot.storage.kubernetes.io/is-default-class: "true"` annotation:

```
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: csi-hostpath-snapclass
  annotations:
    snapshot.storage.kubernetes.io/is-default-class: "true"
driver: hostpath.csi.k8s.io
deletionPolicy: Delete
parameters:
```

If multiple CSI drivers exist, a default VolumeSnapshotClass can be specified
for each of them.

### VolumeSnapshotClass dependencies

When you create a VolumeSnapshot without specifying a VolumeSnapshotClass, Kubernetes
automatically selects a default VolumeSnapshotClass that has a CSI driver matching
the CSI driver of the PVC’s StorageClass.

This behavior allows multiple default VolumeSnapshotClass objects to coexist in a cluster, as long as
each one is associated with a unique CSI driver.

Always ensure that there is only one default VolumeSnapshotClass for each CSI driver. If
multiple default VolumeSnapshotClass objects are created using the same CSI driver,
a VolumeSnapshot creation will fail because Kubernetes cannot determine which one to use.

### Driver

Volume snapshot classes have a driver that determines what CSI volume plugin is
used for provisioning VolumeSnapshots. This field must be specified.

### DeletionPolicy

Volume snapshot classes have a [deletionPolicy](/docs/concepts/storage/volume-snapshots/#delete).
It enables you to configure what happens to a VolumeSnapshotContent when the VolumeSnapshot
object it is bound to is to be deleted. The deletionPolicy of a volume snapshot class can
either be `Retain` or `Delete`. This field must be specified.

If the deletionPolicy is `Delete`, then the underlying storage snapshot will be
deleted along with the VolumeSnapshotContent object. If the deletionPolicy is `Retain`,
then both the underlying snapshot and VolumeSnapshotContent remain.

## Parameters

Volume snapshot classes have parameters that describe volume snapshots belonging to
the volume snapshot class. Different parameters may be accepted depending on the
`driver`.

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
