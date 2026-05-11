# Set Up DRA in a Cluster

FEATURE STATE:
`Kubernetes v1.34 [stable]`(enabled by default)

This page shows you how to configure *dynamic resource allocation (DRA)* in a
Kubernetes cluster by enabling API groups and configuring classes of devices.
These instructions are for cluster administrators.

## About DRA

A Kubernetes feature that lets you request and share resources among Pods.
These resources are often attached
[devices](/docs/reference/glossary/?all=true#term-device "Any resource that's directly or indirectly attached your cluster's nodes, like GPUs or circuit boards.") like hardware
accelerators.

With DRA, device drivers and cluster admins define device *classes* that are
available to *claim* in workloads. Kubernetes allocates matching devices to
specific claims and places the corresponding Pods on nodes that can access the
allocated devices.

Ensure that you're familiar with how DRA works and with DRA terminology like
[DeviceClasses](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#deviceclass "A category of devices in the cluster. Users can claim specific devices in a DeviceClass."),
[ResourceClaims](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#resourceclaims-templates "Describes the resources that a workload needs, such as devices. ResourceClaims can request devices from DeviceClasses."), and
[ResourceClaimTemplates](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#resourceclaims-templates "Defines a template for Kubernetes to create ResourceClaims. Used to provide per-Pod access to separate, similar resources.").
For details, see
[Dynamic Resource Allocation (DRA)](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/).

## Before you begin

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [KodeKloud](https://kodekloud.com/public-playgrounds)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)

Your Kubernetes server must be version v1.34.

To check the version, enter `kubectl version`.

* Directly or indirectly attach devices to your cluster. To avoid potential
  issues with drivers, wait until you set up the DRA feature for your
  cluster before you install drivers.

## Optional: enable legacy DRA API groups

DRA graduated to stable in Kubernetes 1.34 and is enabled by default.
Some older DRA drivers or workloads might still need the
v1beta1 API from Kubernetes 1.30 or v1beta2 from Kubernetes 1.32.
If and only if support for those is desired, then enable the following
[API groups](/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning "A set of related paths in the Kubernetes API."):

```
* `resource.k8s.io/v1beta1`
* `resource.k8s.io/v1beta2`
```

For more information, see
[Enabling or disabling API groups](/docs/reference/using-api/#enabling-or-disabling).

## Verify that DRA is enabled

To verify that the cluster is configured correctly, try to list DeviceClasses:

```
kubectl get deviceclasses
```

If the component configuration was correct, the output is similar to the
following:

```
No resources found
```

If DRA isn't correctly configured, the output of the preceding command is
similar to the following:

```
error: the server doesn't have a resource type "deviceclasses"
```

Try the following troubleshooting steps:

1. Reconfigure and restart the `kube-apiserver` component.
2. If the complete `.spec.resourceClaims` field gets removed from Pods, or if
   Pods get scheduled without considering the ResourceClaims, then verify
   that the `DynamicResourceAllocation` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) is not turned off
   for kube-apiserver, kube-controller-manager, kube-scheduler or the kubelet.

## Install device drivers

After you enable DRA for your cluster, you can install the drivers for your
attached devices. For instructions, check the documentation of your device
owner or the project that maintains the device drivers. The drivers that you
install must be compatible with DRA.

To verify that your installed drivers are working as expected, list
ResourceSlices in your cluster:

```
kubectl get resourceslices
```

The output is similar to the following:

```
NAME                                                  NODE                DRIVER               POOL                             AGE
cluster-1-device-pool-1-driver.example.com-lqx8x      cluster-1-node-1    driver.example.com   cluster-1-device-pool-1-r1gc     7s
cluster-1-device-pool-2-driver.example.com-29t7b      cluster-1-node-2    driver.example.com   cluster-1-device-pool-2-446z     8s
```

Try the following troubleshooting steps:

1. Check the health of the DRA driver and look for error messages about
   publishing ResourceSlices in its log output. The vendor of the driver
   may have further instructions about installation and troubleshooting.

## Create DeviceClasses

You can define categories of devices that your application operators can
claim in workloads by creating
[DeviceClasses](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#deviceclass "A category of devices in the cluster. Users can claim specific devices in a DeviceClass."). Some device
driver providers might also instruct you to create DeviceClasses during driver
installation.

The ResourceSlices that your driver publishes contain information about the
devices that the driver manages, such as capacity, metadata, and attributes. You
can use [Common Expression Language](https://cel.dev "An expression language that's designed to be safe for executing user code.") to filter for properties in your
DeviceClasses, which can make finding devices easier for your workload
operators.

1. To find the device properties that you can select in DeviceClasses by using
   CEL expressions, get the specification of a ResourceSlice:

   ```
   kubectl get resourceslice <resourceslice-name> -o yaml
   ```

   The output is similar to the following:

   ```
   apiVersion: resource.k8s.io/v1
   kind: ResourceSlice
   # lines omitted for clarity
   spec:
     devices:
     - attributes:
         type:
           string: gpu
       capacity:
         memory:
           value: 64Gi
       name: gpu-0
     - attributes:
         type:
           string: gpu
       capacity:
         memory:
           value: 64Gi
       name: gpu-1
     driver: driver.example.com
     nodeName: cluster-1-node-1
   # lines omitted for clarity
   ```

   You can also check the driver provider's documentation for available
   properties and values.
2. Review the following example DeviceClass manifest, which selects any device
   that's managed by the `driver.example.com` device driver:

   [`dra/deviceclass.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/dra/deviceclass.yaml)![](/images/copycode.svg "Copy dra/deviceclass.yaml to clipboard")

   ```
   apiVersion: resource.k8s.io/v1
   kind: DeviceClass
   metadata:
     name: example-device-class
   spec:
     selectors:
     - cel:
         expression: |-
           device.driver == "driver.example.com"
   ```
3. Create the DeviceClass in your cluster:

   ```
   kubectl apply -f https://k8s.io/examples/dra/deviceclass.yaml
   ```

## Clean up

To delete the DeviceClass that you created in this task, run the following
command:

```
kubectl delete -f https://k8s.io/examples/dra/deviceclass.yaml
```

## What's next

* [Learn more about DRA](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)
* [Allocate Devices to Workloads with DRA](/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/)

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
