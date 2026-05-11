# Cloud Controller Manager Administration

FEATURE STATE:
`Kubernetes v1.11 [beta]`

Since cloud providers develop and release at a different pace compared to the
Kubernetes project, abstracting the provider-specific code to the
`cloud-controller-manager`
binary allows cloud vendors to evolve independently from the core Kubernetes code.

The `cloud-controller-manager` can be linked to any cloud provider that satisfies
[cloudprovider.Interface](https://github.com/kubernetes/cloud-provider/blob/master/cloud.go).
For backwards compatibility, the
[cloud-controller-manager](https://github.com/kubernetes/kubernetes/tree/master/cmd/cloud-controller-manager)
provided in the core Kubernetes project uses the same cloud libraries as `kube-controller-manager`.
Cloud providers already supported in Kubernetes core are expected to use the in-tree
cloud-controller-manager to transition out of Kubernetes core.

## Administration

### Requirements

Every cloud has their own set of requirements for running their own cloud provider
integration, it should not be too different from the requirements when running
`kube-controller-manager`. As a general rule of thumb you'll need:

* cloud authentication/authorization: your cloud may require a token or IAM rules
  to allow access to their APIs
* kubernetes authentication/authorization: cloud-controller-manager may need RBAC
  rules set to speak to the kubernetes apiserver
* high availability: like kube-controller-manager, you may want a high available
  setup for cloud controller manager using leader election (on by default).

### Running cloud-controller-manager

Successfully running cloud-controller-manager requires some changes to your cluster configuration.

* `kubelet`, `kube-apiserver`, and `kube-controller-manager` must be set according to the
  user's usage of external CCM. If the user has an external CCM (not the internal cloud
  controller loops in the Kubernetes Controller Manager), then `--cloud-provider=external`
  must be specified. Otherwise, it should not be specified.

Keep in mind that setting up your cluster to use cloud controller manager will
change your cluster behaviour in a few ways:

* Components that specify `--cloud-provider=external` will add a taint
  `node.cloudprovider.kubernetes.io/uninitialized` with an effect `NoSchedule`
  during initialization. This marks the node as needing a second initialization
  from an external controller before it can be scheduled work. Note that in the
  event that cloud controller manager is not available, new nodes in the cluster
  will be left unschedulable. The taint is important since the scheduler may
  require cloud specific information about nodes such as their region or type
  (high cpu, gpu, high memory, spot instance, etc).
* cloud information about nodes in the cluster will no longer be retrieved using
  local metadata, but instead all API calls to retrieve node information will go
  through cloud controller manager. This may mean you can restrict access to your
  cloud API on the kubelets for better security. For larger clusters you may want
  to consider if cloud controller manager will hit rate limits since it is now
  responsible for almost all API calls to your cloud from within the cluster.

The cloud controller manager can implement:

* Node controller - responsible for updating kubernetes nodes using cloud APIs
  and deleting kubernetes nodes that were deleted on your cloud.
* Service controller - responsible for loadbalancers on your cloud against
  services of type LoadBalancer.
* Route controller - responsible for setting up network routes on your cloud
* any other features you would like to implement if you are running an out-of-tree provider.

## Examples

If you are using a cloud that is currently supported in Kubernetes core and would
like to adopt cloud controller manager, see the
[cloud controller manager in kubernetes core](https://github.com/kubernetes/kubernetes/tree/master/cmd/cloud-controller-manager).

For cloud controller managers not in Kubernetes core, you can find the respective
projects in repositories maintained by cloud vendors or by SIGs.

For providers already in Kubernetes core, you can run the in-tree cloud controller
manager as a DaemonSet in your cluster, use the following as a guideline:

[`admin/cloud/ccm-example.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/admin/cloud/ccm-example.yaml)![](/images/copycode.svg "Copy admin/cloud/ccm-example.yaml to clipboard")

```
# This is an example of how to set up cloud-controller-manager as a Daemonset in your cluster.
# It assumes that your masters can run pods and has the role node-role.kubernetes.io/master
# Note that this Daemonset will not work straight out of the box for your cloud, this is
# meant to be a guideline.

---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: cloud-controller-manager
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: system:cloud-controller-manager
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: cloud-controller-manager
  namespace: kube-system
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  labels:
    k8s-app: cloud-controller-manager
  name: cloud-controller-manager
  namespace: kube-system
spec:
  selector:
    matchLabels:
      k8s-app: cloud-controller-manager
  template:
    metadata:
      labels:
        k8s-app: cloud-controller-manager
    spec:
      serviceAccountName: cloud-controller-manager
      containers:
      - name: cloud-controller-manager
        # for in-tree providers we use registry.k8s.io/cloud-controller-manager
        # this can be replaced with any other image for out-of-tree providers
        image: registry.k8s.io/cloud-controller-manager:v1.8.0
        command:
        - /usr/local/bin/cloud-controller-manager
        - --cloud-provider=[YOUR_CLOUD_PROVIDER]  # Add your own cloud provider here!
        - --leader-elect=true
        - --use-service-account-credentials
        # these flags will vary for every cloud provider
        - --allocate-node-cidrs=true
        - --configure-cloud-routes=true
        - --cluster-cidr=172.17.0.0/16
      tolerations:
      # this is required so CCM can bootstrap itself
      - key: node.cloudprovider.kubernetes.io/uninitialized
        value: "true"
        effect: NoSchedule
      # these tolerations are to have the daemonset runnable on control plane nodes
      # remove them if your control plane nodes should not run pods
      - key: node-role.kubernetes.io/control-plane
        operator: Exists
        effect: NoSchedule
      - key: node-role.kubernetes.io/master
        operator: Exists
        effect: NoSchedule
      # this is to restrict CCM to only run on master nodes
      # the node selector may vary depending on your cluster setup
      nodeSelector:
        node-role.kubernetes.io/master: ""
```

## Limitations

Running cloud controller manager comes with a few possible limitations. Although
these limitations are being addressed in upcoming releases, it's important that
you are aware of these limitations for production workloads.

### Support for Volumes

Cloud controller manager does not implement any of the volume controllers found
in `kube-controller-manager` as the volume integrations also require coordination
with kubelets. As we evolve CSI (container storage interface) and add stronger
support for flex volume plugins, necessary support will be added to cloud
controller manager so that clouds can fully integrate with volumes. Learn more
about out-of-tree CSI volume plugins [here](https://github.com/kubernetes/features/issues/178).

### Scalability

The cloud-controller-manager queries your cloud provider's APIs to retrieve
information for all nodes. For very large clusters, consider possible
bottlenecks such as resource requirements and API rate limiting.

### Chicken and Egg

The goal of the cloud controller manager project is to decouple development
of cloud features from the core Kubernetes project. Unfortunately, many aspects
of the Kubernetes project has assumptions that cloud provider features are tightly
integrated into the project. As a result, adopting this new architecture can create
several situations where a request is being made for information from a cloud provider,
but the cloud controller manager may not be able to return that information without
the original request being complete.

A good example of this is the TLS bootstrapping feature in the Kubelet.
TLS bootstrapping assumes that the Kubelet has the ability to ask the cloud provider
(or a local metadata service) for all its address types (private, public, etc)
but cloud controller manager cannot set a node's address types without being
initialized in the first place which requires that the kubelet has TLS certificates
to communicate with the apiserver.

As this initiative evolves, changes will be made to address these issues in upcoming releases.

## What's next

To build and develop your own cloud controller manager, read
[Developing Cloud Controller Manager](/docs/tasks/administer-cluster/developing-cloud-controller-manager/).

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
