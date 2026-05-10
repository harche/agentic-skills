# Install Drivers and Allocate Devices with DRA

FEATURE STATE:
`Kubernetes v1.34 [stable]`(enabled by default)

This tutorial shows you how to install [Dynamic Resource Allocation (DRA)](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/ "A Kubernetes feature for requesting and sharing resources, like hardware accelerators, among Pods.") drivers in your cluster and how to
use them in conjunction with the DRA APIs to allocate [devices](/docs/reference/glossary/?all=true#term-device "Any resource that's directly or indirectly attached your cluster's nodes, like GPUs or circuit boards.") to Pods. This page is intended for cluster administrators.

[Dynamic Resource Allocation (DRA)](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/ "A Kubernetes feature for requesting and sharing resources, like hardware accelerators, among Pods.")
lets a cluster manage availability and allocation of hardware resources to
satisfy Pod-based claims for hardware requirements and preferences. To support
this, a mixture of Kubernetes built-in components (like the Kubernetes
scheduler, kubelet, and kube-controller-manager) and third-party drivers from
device owners (called DRA drivers) share the responsibility to advertise,
allocate, prepare, mount, healthcheck, unprepare, and cleanup resources
throughout the Pod lifecycle. These components share information via a series of
DRA specific APIs in the `resource.k8s.io` API group including [DeviceClasses](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#deviceclass "A category of devices in the cluster. Users can claim specific devices in a DeviceClass."), [ResourceSlices](/docs/reference/kubernetes-api/workload-resources/resource-slice-v1beta1/ "Represents one or more infrastructure resources, like devices, in a pool of similar resources."), [ResourceClaims](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#resourceclaims-templates "Describes the resources that a workload needs, such as devices. ResourceClaims can request devices from DeviceClasses."), as well as
new fields in the Pod spec itself.

### Objectives

* Deploy an example DRA driver
* Deploy a Pod requesting a hardware claim using DRA APIs
* Delete a Pod that has a claim

## Before you begin

Your cluster should support [RBAC](/docs/reference/access-authn-authz/rbac/).
You can try this tutorial with a cluster using a different authorization
mechanism, but in that case you will have to adapt the steps around defining
roles and permissions.

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [KodeKloud](https://kodekloud.com/public-playgrounds)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)

This tutorial has been tested with Linux nodes, though it may also work with
other types of nodes.

Your Kubernetes server must be version v1.34.

To check the version, enter `kubectl version`.

If your cluster is not currently running Kubernetes 1.34 then please check the documentation for the version of Kubernetes that you
plan to use.

## Explore the initial cluster state

You can spend some time to observe the initial state of a cluster with DRA
enabled, especially if you have not used these APIs extensively before. If you
set up a new cluster for this tutorial, with no driver installed and no Pod
claims yet to satisfy, the output of these commands won't show any resources.

1. Get a list of [DeviceClasses](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#deviceclass "A category of devices in the cluster. Users can claim specific devices in a DeviceClass."):

   ```
   kubectl get deviceclasses
   ```

   The output is similar to this:

   ```
   No resources found
   ```
2. Get a list of [ResourceSlices](/docs/reference/kubernetes-api/workload-resources/resource-slice-v1beta1/ "Represents one or more infrastructure resources, like devices, in a pool of similar resources."):

   ```
   kubectl get resourceslices
   ```

   The output is similar to this:

   ```
   No resources found
   ```
3. Get a list of [ResourceClaims](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#resourceclaims-templates "Describes the resources that a workload needs, such as devices. ResourceClaims can request devices from DeviceClasses.") and [ResourceClaimTemplates](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#resourceclaims-templates "Defines a template for Kubernetes to create ResourceClaims. Used to provide per-Pod access to separate, similar resources.")

   ```
   kubectl get resourceclaims -A
   kubectl get resourceclaimtemplates -A
   ```

   The output is similar to this:

   ```
   No resources found
   No resources found
   ```

At this point, you have confirmed that DRA is enabled and configured properly in
the cluster, and that no DRA drivers have advertised any resources to the DRA
APIs yet.

## Install an example DRA driver

DRA drivers are third-party applications that run on each node of your cluster
to interface with the hardware of that node and Kubernetes' built-in DRA
components. The installation procedure depends on the driver you choose, but is
likely deployed as a [DaemonSet](/docs/concepts/workloads/controllers/daemonset "Ensures a copy of a Pod is running across a set of nodes in a cluster.") to all or a
selection of the nodes (using [selectors](/docs/concepts/overview/working-with-objects/labels/ "Allows users to filter a list of resources based on labels.") or similar mechanisms) in your cluster.

Check your driver's documentation for specific installation instructions, which
might include a Helm chart, a set of manifests, or other deployment tooling.

This tutorial uses an example driver which can be found in the
[kubernetes-sigs/dra-example-driver](https://github.com/kubernetes-sigs/dra-example-driver)
repository to demonstrate driver installation. This example driver advertises
simulated GPUs to Kubernetes for your Pods to interact with.

### Prepare your cluster for driver installation

To simplify cleanup, create a namespace named dra-tutorial:

1. Create the namespace:

   ```
   kubectl create namespace dra-tutorial
   ```

In a production environment, you would likely be using a previously released or
qualified image from the driver vendor or your own organization, and your nodes
would need to have access to the image registry where the driver image is
hosted. In this tutorial, you will use a publicly released image of the
dra-example-driver to simulate access to a DRA driver image.

1. Confirm your nodes have access to the image by running the following
   from within one of your cluster's nodes:

   ```
   docker pull registry.k8s.io/dra-example-driver/dra-example-driver:v0.2.0
   ```

### Deploy the DRA driver components

For this tutorial, you will install the critical example resource driver
components individually with `kubectl`.

1. Create the DeviceClass representing the device types this DRA driver
   supports:

   [`dra/driver-install/deviceclass.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/dra/driver-install/deviceclass.yaml)![](/images/copycode.svg "Copy dra/driver-install/deviceclass.yaml to clipboard")

   ```
   apiVersion: resource.k8s.io/v1
   kind: DeviceClass
   metadata:
     name: gpu.example.com
   spec:
     selectors:
     - cel:
         expression: "device.driver == 'gpu.example.com'"
   ```

   ```
   kubectl apply --server-side -f http://k8s.io/examples/dra/driver-install/deviceclass.yaml
   ```
2. Create the ServiceAccount, ClusterRole and ClusterRoleBinding that will
   be used by the driver to gain permissions to interact with the Kubernetes API
   on this cluster:

   1. Create the Service Account:

      [`dra/driver-install/serviceaccount.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/dra/driver-install/serviceaccount.yaml)![](/images/copycode.svg "Copy dra/driver-install/serviceaccount.yaml to clipboard")

      ```
      apiVersion: v1
      kind: ServiceAccount
      metadata:
        name: dra-example-driver-service-account
        namespace: dra-tutorial
        labels:
          app.kubernetes.io/name: dra-example-driver
          app.kubernetes.io/instance: dra-example-driver
      ```

      ```
      kubectl apply --server-side -f http://k8s.io/examples/dra/driver-install/serviceaccount.yaml
      ```
   2. Create the ClusterRole:

      [`dra/driver-install/clusterrole.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/dra/driver-install/clusterrole.yaml)![](/images/copycode.svg "Copy dra/driver-install/clusterrole.yaml to clipboard")

      ```
      apiVersion: rbac.authorization.k8s.io/v1
      kind: ClusterRole
      metadata:
        name: dra-example-driver-role
      rules:
      - apiGroups: ["resource.k8s.io"]
        resources: ["resourceclaims"]
        verbs: ["get"]
      - apiGroups: [""]
        resources: ["nodes"]
        verbs: ["get"]
      - apiGroups: ["resource.k8s.io"]
        resources: ["resourceslices"]
        verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
      ```

      ```
      kubectl apply --server-side -f http://k8s.io/examples/dra/driver-install/clusterrole.yaml
      ```
   3. Create the ClusterRoleBinding:

      [`dra/driver-install/clusterrolebinding.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/dra/driver-install/clusterrolebinding.yaml)![](/images/copycode.svg "Copy dra/driver-install/clusterrolebinding.yaml to clipboard")

      ```
      apiVersion: rbac.authorization.k8s.io/v1
      kind: ClusterRoleBinding
      metadata:
        name: dra-example-driver-role-binding
      subjects:
      - kind: ServiceAccount
        name: dra-example-driver-service-account
        namespace: dra-tutorial
      roleRef:
        kind: ClusterRole
        name: dra-example-driver-role
        apiGroup: rbac.authorization.k8s.io
      ```

      ```
      kubectl apply --server-side -f http://k8s.io/examples/dra/driver-install/clusterrolebinding.yaml
      ```
3. Create a [PriorityClass](/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass "A mapping from a class name to the scheduling priority that a Pod should have.") for the DRA
   driver. The PriorityClass prevents preemption of th DRA driver component,
   which is responsible for important lifecycle operations for Pods with
   claims. Learn more about [pod priority and preemption
   here](/docs/concepts/scheduling-eviction/pod-priority-preemption/).

   [`dra/driver-install/priorityclass.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/dra/driver-install/priorityclass.yaml)![](/images/copycode.svg "Copy dra/driver-install/priorityclass.yaml to clipboard")

   ```
   apiVersion: scheduling.k8s.io/v1
   kind: PriorityClass
   metadata:
     name: dra-driver-high-priority
   value: 1000000
   globalDefault: false
   description: "This priority class should be used for DRA driver pods only."
   ```

   ```
   kubectl apply --server-side -f http://k8s.io/examples/dra/driver-install/priorityclass.yaml
   ```
4. Deploy the actual DRA driver as a DaemonSet configured to run the example
   driver binary with the permissions provisioned above. The DaemonSet has the
   permissions that you granted to the ServiceAccount in the previous steps.

   [`dra/driver-install/daemonset.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/dra/driver-install/daemonset.yaml)![](/images/copycode.svg "Copy dra/driver-install/daemonset.yaml to clipboard")

   ```
   apiVersion: apps/v1
   kind: DaemonSet
   metadata:
     name: dra-example-driver-kubeletplugin
     namespace: dra-tutorial
     labels:
       app.kubernetes.io/name: dra-example-driver
   spec:
     selector:
       matchLabels:
         app.kubernetes.io/name: dra-example-driver
     updateStrategy:
       type: RollingUpdate
     template:
       metadata:
         labels:
           app.kubernetes.io/name: dra-example-driver
       spec:
         priorityClassName: dra-driver-high-priority
         serviceAccountName: dra-example-driver-service-account
         securityContext:
           {}
         containers:
         - name: plugin
           securityContext:
             privileged: true
           image: registry.k8s.io/dra-example-driver/dra-example-driver:v0.2.0
           imagePullPolicy: IfNotPresent
           command: ["dra-example-kubeletplugin"]
           resources:
             {}
           # Production drivers should always implement a liveness probe
           # For the tutorial we simply omit it
           # livenessProbe:
           #   grpc:
           #     port: 51515
           #     service: liveness
           #   failureThreshold: 3
           #   periodSeconds: 10
           env:
           - name: CDI_ROOT
             value: /var/run/cdi
           - name: KUBELET_REGISTRAR_DIRECTORY_PATH
             value: "/var/lib/kubelet/plugins_registry"
           - name: KUBELET_PLUGINS_DIRECTORY_PATH
             value: "/var/lib/kubelet/plugins"
           - name: NODE_NAME
             valueFrom:
               fieldRef:
                 fieldPath: spec.nodeName
           - name: NAMESPACE
             valueFrom:
               fieldRef:
                 fieldPath: metadata.namespace
           # Simulated number of devices the example driver will pretend to have.
           - name: NUM_DEVICES
             value: "9"
           - name: HEALTHCHECK_PORT
             value: "51515"
           volumeMounts:
           - name: plugins-registry
             mountPath: "/var/lib/kubelet/plugins_registry"
           - name: plugins
             mountPath: "/var/lib/kubelet/plugins"
           - name: cdi
             mountPath: /var/run/cdi
         volumes:
         - name: plugins-registry
           hostPath:
             path: "/var/lib/kubelet/plugins_registry"
         - name: plugins
           hostPath:
             path: "/var/lib/kubelet/plugins"
         - name: cdi
           hostPath:
             path: /var/run/cdi
   ```

   ```
   kubectl apply --server-side -f http://k8s.io/examples/dra/driver-install/daemonset.yaml
   ```

   The DaemonSet is configured with
   the volume mounts necessary to interact with the underlying Container Device
   Interface (CDI) directory, and to expose its socket to `kubelet` via the
   `kubelet/plugins` directory.

### Verify the DRA driver installation

1. Get a list of the Pods of the DRA driver DaemonSet across all worker nodes:

   ```
   kubectl get pod -l app.kubernetes.io/name=dra-example-driver -n dra-tutorial
   ```

   The output is similar to this:

   ```
   NAME                                     READY   STATUS    RESTARTS   AGE
   dra-example-driver-kubeletplugin-4sk2x   1/1     Running   0          13s
   dra-example-driver-kubeletplugin-cttr2   1/1     Running   0          13s
   ```
2. The initial responsibility of each node's local DRA driver is to update the
   cluster with what devices are available to Pods on that node, by publishing its
   metadata to the ResourceSlices API. You can check that API to see that each node
   with a driver is advertising the device class it represents.

   Check for available ResourceSlices:

   ```
   kubectl get resourceslices
   ```

   The output is similar to this:

   ```
   NAME                                 NODE           DRIVER            POOL           AGE
   kind-worker-gpu.example.com-k69gd    kind-worker    gpu.example.com   kind-worker    19s
   kind-worker2-gpu.example.com-qdgpn   kind-worker2   gpu.example.com   kind-worker2   19s
   ```

At this point, you have successfully installed the example DRA driver, and
confirmed its initial configuration. You're now ready to use DRA to schedule
Pods.

## Claim resources and deploy a Pod

To request resources using DRA, you create ResourceClaims or
ResourceClaimTemplates that define the resources that your Pods need. In the
example driver, a memory capacity attribute is exposed for mock GPU devices.
This section shows you how to use [Common Expression Language](https://cel.dev "An expression language that's designed to be safe for executing user code.") to
express your requirements in a ResourceClaim, select that ResourceClaim in a Pod
specification, and observe the resource allocation.

This tutorial showcases only one basic example of a DRA ResourceClaim. Read
[Dynamic Resource
Allocation](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/) to
learn more about ResourceClaims.

### Create the ResourceClaim

In this section, you create a ResourceClaim and reference it in a Pod. Whatever
the claim, the `deviceClassName` is a required field, narrowing down the scope
of the request to a specific device class. The request itself can include a [Common Expression Language](https://cel.dev "An expression language that's designed to be safe for executing user code.") expression that references attributes that
may be advertised by the driver managing that device class.

In this example, you will create a request for any GPU advertising over 10Gi
memory capacity. The attribute exposing capacity from the example driver takes
the form `device.capacity['gpu.example.com'].memory`. Note also that the name of
the claim is set to `some-gpu`.

[`dra/driver-install/example/resourceclaim.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/dra/driver-install/example/resourceclaim.yaml)![](/images/copycode.svg "Copy dra/driver-install/example/resourceclaim.yaml to clipboard")

```
apiVersion: resource.k8s.io/v1
kind: ResourceClaim
metadata:
 name: some-gpu
 namespace: dra-tutorial
spec:
   devices:
     requests:
     - name: some-gpu
       exactly:
         deviceClassName: gpu.example.com
         selectors:
         - cel:
             expression: "device.capacity['gpu.example.com'].memory.compareTo(quantity('10Gi')) >= 0"
```

```
kubectl apply --server-side -f http://k8s.io/examples/dra/driver-install/example/resourceclaim.yaml
```

### Create the Pod that references that ResourceClaim

Below is the Pod manifest referencing the ResourceClaim you just made,
`some-gpu`, in the `spec.resourceClaims.resourceClaimName` field. The local name
for that claim, `gpu`, is then used in the
`spec.containers.resources.claims.name` field to allocate the claim to the Pod's
underlying container.

[`dra/driver-install/example/pod.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples/dra/driver-install/example/pod.yaml)![](/images/copycode.svg "Copy dra/driver-install/example/pod.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: pod0
  namespace: dra-tutorial
  labels:
    app: pod
spec:
  containers:
  - name: ctr0
    image: ubuntu:24.04
    command: ["bash", "-c"]
    args: ["export; trap 'exit 0' TERM; sleep 9999 & wait"]
    resources:
      claims:
      - name: gpu
  resourceClaims:
  - name: gpu
    resourceClaimName: some-gpu
```

```
kubectl apply --server-side -f http://k8s.io/examples/dra/driver-install/example/pod.yaml
```

1. Confirm the pod has deployed:

   ```
   kubectl get pod pod0 -n dra-tutorial
   ```

   The output is similar to this:

   ```
   NAME   READY   STATUS    RESTARTS   AGE
   pod0   1/1     Running   0          9s
   ```

### Explore the DRA state

After you create the Pod, the cluster tries to schedule that Pod to a node where
Kubernetes can satisfy the ResourceClaim. In this tutorial, the DRA driver is
deployed on all nodes, and is advertising mock GPUs on all nodes, all of which
have enough capacity advertised to satisfy the Pod's claim, so Kubernetes can
schedule this Pod on any node and can allocate any of the mock GPUs on that
node.

When Kubernetes allocates a mock GPU to a Pod, the example driver adds
environment variables in each container it is allocated to in order to indicate
which GPUs *would* have been injected into them by a real resource driver and
how they would have been configured, so you can check those environment
variables to see how the Pods have been handled by the system.

1. Check the Pod logs, which report the name of the mock GPU that was allocated:

   ```
   kubectl logs pod0 -c ctr0 -n dra-tutorial | grep -E "GPU_DEVICE_[0-9]+=" | grep -v "RESOURCE_CLAIM"
   ```

   The output is similar to this:

   ```
   declare -x GPU_DEVICE_0="gpu-0"
   ```
2. Check the state of the ResourceClaim object:

   ```
   kubectl get resourceclaims -n dra-tutorial
   ```

   The output is similar to this:

   ```
   NAME       STATE                AGE
   some-gpu   allocated,reserved   34s
   ```

   In this output, the `STATE` column shows that the ResourceClaim is allocated
   and reserved.
3. Check the details of the `some-gpu` ResourceClaim. The `status` stanza of
   the ResourceClaim has information about the allocated device and the Pod it
   has been reserved for:

   ```
   kubectl get resourceclaim some-gpu -n dra-tutorial -o yaml
   ```

   The output is similar to this:

   ```
    1apiVersion: resource.k8s.io/v1
    2kind: ResourceClaim
    3metadata:
    4    creationTimestamp: "2025-08-20T18:17:31Z"
    5    finalizers:
    6    - resource.kubernetes.io/delete-protection
    7    name: some-gpu
    8    namespace: dra-tutorial
    9    resourceVersion: "2326"
   10    uid: d3e48dbf-40da-47c3-a7b9-f7d54d1051c3
   11spec:
   12    devices:
   13        requests:
   14        - exactly:
   15            allocationMode: ExactCount
   16            count: 1
   17            deviceClassName: gpu.example.com
   18            selectors:
   19            - cel:
   20                expression: device.capacity['gpu.example.com'].memory.compareTo(quantity('10Gi'))
   21                >= 0
   22        name: some-gpu
   23status:
   24    allocation:
   25        devices:
   26        results:
   27        - device: gpu-0
   28            driver: gpu.example.com
   29            pool: kind-worker
   30            request: some-gpu
   31        nodeSelector:
   32        nodeSelectorTerms:
   33        - matchFields:
   34            - key: metadata.name
   35            operator: In
   36            values:
   37            - kind-worker
   38    reservedFor:
   39    - name: pod0
   40        resource: pods
   41        uid: c4dadf20-392a-474d-a47b-ab82080c8bd7
   ```
4. To check how the driver handled device allocation, get the logs for the
   driver DaemonSet Pods:

   ```
   kubectl logs -l app.kubernetes.io/name=dra-example-driver -n dra-tutorial
   ```

   The output is similar to this:

   ```
   I0820 18:17:44.131324       1 driver.go:106] PrepareResourceClaims is called: number of claims: 1
   I0820 18:17:44.135056       1 driver.go:133] Returning newly prepared devices for claim 'd3e48dbf-40da-47c3-a7b9-f7d54d1051c3': [{[some-gpu] kind-worker gpu-0 [k8s.gpu.example.com/gpu=common k8s.gpu.example.com/gpu=d3e48dbf-40da-47c3-a7b9-f7d54d1051c3-gpu-0]}]
   ```

You have now successfully deployed a Pod that claims devices using DRA, verified
that the Pod was scheduled to an appropriate node, and saw that the associated
DRA APIs kinds were updated with the allocation status.

## Delete a Pod that has a claim

When a Pod with a claim is deleted, the DRA driver deallocates the resource so
it can be available for future scheduling. To validate this behavior, delete the
Pod that you created in the previous steps and watch the corresponding changes
to the ResourceClaim and driver.

1. Delete the `pod0` Pod:

   ```
   kubectl delete pod pod0 -n dra-tutorial
   ```

   The output is similar to this:

   ```
   pod "pod0" deleted
   ```

### Observe the DRA state

When the Pod is deleted, the driver deallocates the device from the
ResourceClaim and updates the ResourceClaim resource in the Kubernetes API. The
ResourceClaim has a `pending` state until it's referenced in a new Pod.

1. Check the state of the `some-gpu` ResourceClaim:

   ```
   kubectl get resourceclaims -n dra-tutorial
   ```

   The output is similar to this:

   ```
   NAME       STATE     AGE
   some-gpu   pending   76s
   ```
2. Verify that the driver has processed unpreparing the device for this claim by
   checking the driver logs:

   ```
   kubectl logs -l app.kubernetes.io/name=dra-example-driver -n dra-tutorial
   ```

   The output is similar to this:

   ```
   I0820 18:22:15.629376       1 driver.go:138] UnprepareResourceClaims is called: number of claims: 1
   ```

You have now deleted a Pod that had a claim, and observed that the driver took
action to unprepare the underlying hardware resource and update the DRA APIs to
reflect that the resource is available again for future scheduling.

## Cleaning up

To clean up the resources that you created in this tutorial, follow these steps:

```
kubectl delete namespace dra-tutorial
kubectl delete deviceclass gpu.example.com
kubectl delete clusterrole dra-example-driver-role
kubectl delete clusterrolebinding dra-example-driver-role-binding
kubectl delete priorityclass dra-driver-high-priority
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
