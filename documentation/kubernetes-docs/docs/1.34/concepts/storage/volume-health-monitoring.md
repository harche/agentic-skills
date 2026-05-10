# Volume Health Monitoring

FEATURE STATE:
`Kubernetes v1.21 [alpha]`

[CSI](/docs/concepts/storage/volumes/#csi "The Container Storage Interface (CSI) defines a standard interface to expose storage systems to containers.") volume health monitoring allows
CSI Drivers to detect abnormal volume conditions from the underlying storage systems
and report them as events on [PVCs](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims "Claims storage resources defined in a PersistentVolume so that it can be mounted as a volume in a container.")
or [Pods](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.").

## Volume health monitoring

Kubernetes *volume health monitoring* is part of how Kubernetes implements the
Container Storage Interface (CSI). Volume health monitoring feature is implemented
in two components: an External Health Monitor controller, and the
[kubelet](/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.").

If a CSI Driver supports Volume Health Monitoring feature from the controller side,
an event will be reported on the related
[PersistentVolumeClaim](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims "Claims storage resources defined in a PersistentVolume so that it can be mounted as a volume in a container.") (PVC)
when an abnormal volume condition is detected on a CSI volume.

The External Health Monitor [controller](/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.")
also watches for node failure events. You can enable node failure monitoring by setting
the `enable-node-watcher` flag to true. When the external health monitor detects a node
failure event, the controller reports an Event will be reported on the PVC to indicate
that pods using this PVC are on a failed node.

If a CSI Driver supports Volume Health Monitoring feature from the node side,
an Event will be reported on every Pod using the PVC when an abnormal volume
condition is detected on a CSI volume. In addition, Volume Health information
is exposed as Kubelet VolumeStats metrics. A new metric kubelet_volume_stats_health_status_abnormal
is added. This metric includes two labels: `namespace` and `persistentvolumeclaim`.
The count is either 1 or 0. 1 indicates the volume is unhealthy, 0 indicates volume
is healthy. For more information, please check
[KEP](https://github.com/kubernetes/enhancements/tree/master/keps/sig-storage/1432-volume-health-monitor#kubelet-metrics-changes).

> **Note:**
> You need to enable the `CSIVolumeHealth` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/)
> to use this feature from the node side.

## What's next

See the [CSI driver documentation](https://kubernetes-csi.github.io/docs/drivers.html)
to find out which CSI drivers have implemented this feature.

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
