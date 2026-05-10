<div wrapper="1" role="_abstract">

Data volume (DV) annotations allow you to manage pod behavior. You can add one or more annotations to a data volume, which then propagates to the created importer pods.

</div>

# Example: Data volume annotations

<div wrapper="1" role="_abstract">

This example shows how you can configure data volume (DV) annotations to control which network the importer pod uses. The `v1.multus-cni.io/default-network: bridge-network` annotation causes the pod to use the Multus network named `bridge-network` as its default network.

</div>

If you want the importer pod to use both the default network from the cluster and the secondary Multus network, use the `k8s.v1.cni.cncf.io/networks: <network_name>` annotation.

<div class="example">

<div class="title">

Multus network annotation example

</div>

``` yaml
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: datavolume-example
  annotations:
    v1.multus-cni.io/default-network: bridge-network
# ...
```

- Multus network annotation

</div>
