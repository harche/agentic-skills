# Administer a Cluster

Learn common tasks for administering a cluster.

---

##### [Administration with kubeadm](/docs/tasks/administer-cluster/kubeadm/)

##### [Overprovision Node Capacity For A Cluster](/docs/tasks/administer-cluster/node-overprovisioning/)

##### [Migrating from dockershim](/docs/tasks/administer-cluster/migrating-from-dockershim/)

##### [Generate Certificates Manually](/docs/tasks/administer-cluster/certificates/)

##### [Manage Memory, CPU, and API Resources](/docs/tasks/administer-cluster/manage-resources/)

##### [Install a Network Policy Provider](/docs/tasks/administer-cluster/network-policy-provider/)

##### [Access Clusters Using the Kubernetes API](/docs/tasks/administer-cluster/access-cluster-api/)

##### [Enable Or Disable Feature Gates](/docs/tasks/administer-cluster/configure-feature-gates/)

##### [Advertise Extended Resources for a Node](/docs/tasks/administer-cluster/extended-resource-node/)

##### [Autoscale the DNS Service in a Cluster](/docs/tasks/administer-cluster/dns-horizontal-autoscaling/)

##### [Change the Access Mode of a PersistentVolume to ReadWriteOncePod](/docs/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod/)

##### [Change the default StorageClass](/docs/tasks/administer-cluster/change-default-storage-class/)

##### [Switching from Polling to CRI Event-based Updates to Container Status](/docs/tasks/administer-cluster/switch-to-evented-pleg/)

##### [Change the Reclaim Policy of a PersistentVolume](/docs/tasks/administer-cluster/change-pv-reclaim-policy/)

##### [Cloud Controller Manager Administration](/docs/tasks/administer-cluster/running-cloud-controller/)

##### [Configure a kubelet image credential provider](/docs/tasks/administer-cluster/kubelet-credential-provider/)

##### [Configure Quotas for API Objects](/docs/tasks/administer-cluster/quota-api-object/)

##### [Control CPU Management Policies on the Node](/docs/tasks/administer-cluster/cpu-management-policies/)

##### [Control Topology Management Policies on a node](/docs/tasks/administer-cluster/topology-manager/)

##### [Customizing DNS Service](/docs/tasks/administer-cluster/dns-custom-nameservers/)

##### [Debugging DNS Resolution](/docs/tasks/administer-cluster/dns-debugging-resolution/)

##### [Declare Network Policy](/docs/tasks/administer-cluster/declare-network-policy/)

##### [Developing Cloud Controller Manager](/docs/tasks/administer-cluster/developing-cloud-controller-manager/)

##### [Enable Or Disable A Kubernetes API](/docs/tasks/administer-cluster/enable-disable-api/)

##### [Encrypting Confidential Data at Rest](/docs/tasks/administer-cluster/encrypt-data/)

##### [Decrypt Confidential Data that is Already Encrypted at Rest](/docs/tasks/administer-cluster/decrypt-data/)

##### [Guaranteed Scheduling For Critical Add-On Pods](/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/)

##### [IP Masquerade Agent User Guide](/docs/tasks/administer-cluster/ip-masq-agent/)

##### [Limit Storage Consumption](/docs/tasks/administer-cluster/limit-storage-consumption/)

##### [Migrate Replicated Control Plane To Use Cloud Controller Manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/)

##### [Operating etcd clusters for Kubernetes](/docs/tasks/administer-cluster/configure-upgrade-etcd/)

##### [Reserve Compute Resources for System Daemons](/docs/tasks/administer-cluster/reserve-compute-resources/)

##### [Running Kubernetes Node Components as a Non-root User](/docs/tasks/administer-cluster/kubelet-in-userns/)

##### [Safely Drain a Node](/docs/tasks/administer-cluster/safely-drain-node/)

##### [Securing a Cluster](/docs/tasks/administer-cluster/securing-a-cluster/)

##### [Set Kubelet Parameters Via A Configuration File](/docs/tasks/administer-cluster/kubelet-config-file/)

##### [Share a Cluster with Namespaces](/docs/tasks/administer-cluster/namespaces/)

##### [Upgrade A Cluster](/docs/tasks/administer-cluster/cluster-upgrade/)

##### [Use Cascading Deletion in a Cluster](/docs/tasks/administer-cluster/use-cascading-deletion/)

##### [Using a KMS provider for data encryption](/docs/tasks/administer-cluster/kms-provider/)

##### [Using CoreDNS for Service Discovery](/docs/tasks/administer-cluster/coredns/)

##### [Using NodeLocal DNSCache in Kubernetes Clusters](/docs/tasks/administer-cluster/nodelocaldns/)

##### [Using sysctls in a Kubernetes Cluster](/docs/tasks/administer-cluster/sysctl-cluster/)

##### [Utilizing the NUMA-aware Memory Manager](/docs/tasks/administer-cluster/memory-manager/)

##### [Verify Signed Kubernetes Artifacts](/docs/tasks/administer-cluster/verify-signed-artifacts/)

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
