This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/concepts/extend-kubernetes/compute-storage-net/).

# Compute, Storage, and Networking Extensions

* 1: [Network Plugins](#pg-1ac2260db9ecccbf0303a899bc27ce6d)
* 2: [Device Plugins](#pg-53e1ea8892ceca307ba19e8d6a7b8d32)

This section covers extensions to your cluster that do not come as part as Kubernetes itself.
You can use these extensions to enhance the nodes in your cluster, or to provide the network
fabric that links Pods together.

* [CSI](/docs/concepts/storage/volumes/#csi) and [FlexVolume](/docs/concepts/storage/volumes/#flexvolume) storage plugins

  [Container Storage Interface](/docs/concepts/storage/volumes/#csi "The Container Storage Interface (CSI) defines a standard interface to expose storage systems to containers.") (CSI) plugins
  provide a way to extend Kubernetes with supports for new kinds of volumes. The volumes can
  be backed by durable external storage, or provide ephemeral storage, or they might offer a
  read-only interface to information using a filesystem paradigm.

  Kubernetes also includes support for [FlexVolume](/docs/concepts/storage/volumes/#flexvolume)
  plugins, which are deprecated since Kubernetes v1.23 (in favour of CSI).

  FlexVolume plugins allow users to mount volume types that aren't natively
  supported by Kubernetes. When you run a Pod that relies on FlexVolume
  storage, the kubelet calls a binary plugin to mount the volume. The archived
  [FlexVolume](https://git.k8s.io/design-proposals-archive/storage/flexvolume-deployment.md)
  design proposal has more detail on this approach.

  The [Kubernetes Volume Plugin FAQ for Storage Vendors](https://github.com/kubernetes/community/blob/master/sig-storage/volume-plugin-faq.md#kubernetes-volume-plugin-faq-for-storage-vendors)
  includes general information on storage plugins.
* [Device plugins](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)

  Device plugins allow a node to discover new Node facilities (in addition to the
  built-in node resources such as `cpu` and `memory`), and provide these custom node-local
  facilities to Pods that request them.
* [Network plugins](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)

  Network plugins allow Kubernetes to work with different networking topologies and technologies.
  Your Kubernetes cluster needs a *network plugin* in order to have a working Pod network
  and to support other aspects of the Kubernetes network model.

  Kubernetes 1.34 is compatible with [CNI](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/ "Container network interface (CNI) plugins are a type of Network plugin that adheres to the appc/CNI specification.")
  network plugins.
