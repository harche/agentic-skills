This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/setup/production-environment/tools/).

# Installing Kubernetes with deployment tools

* 1: [Bootstrapping clusters with kubeadm](#pg-a16f59f325a17cdeed324d5c889f7f73)

+ 1.1: [Installing kubeadm](#pg-29e59491dd6118b23072dfe9ebb93323)
+ 1.2: [Troubleshooting kubeadm](#pg-c3689df4b0c61a998e79d91a865aa244)
+ 1.3: [Creating a cluster with kubeadm](#pg-134ed1f6142a98e6ac681a1ba4920e53)
+ 1.4: [Customizing components with the kubeadm API](#pg-4c656c5eda3e1c06ad1aedebdc04a211)
+ 1.5: [Options for Highly Available Topology](#pg-015edbc7cc688d31b1d1edce7c186135)
+ 1.6: [Creating Highly Available Clusters with kubeadm](#pg-3941d5c3409342219bf7e03128b8ecb6)
+ 1.7: [Set up a High Availability etcd Cluster with kubeadm](#pg-8160424c22d24f7d2d63c521e107dbf8)
+ 1.8: [Configuring each kubelet in your cluster using kubeadm](#pg-07709e71de6b4ac2573041c31213dbeb)
+ 1.9: [Dual-stack support with kubeadm](#pg-df2f3f20d404ebe2b03fcda1fcee50e7)

There are many methods and tools for setting up your own production Kubernetes cluster.
For example:

* [kubeadm](/docs/setup/production-environment/tools/kubeadm/)
* [Cluster API](https://cluster-api.sigs.k8s.io/): A Kubernetes sub-project focused on
  providing declarative APIs and tooling to simplify provisioning, upgrading, and operating
  multiple Kubernetes clusters.
* [kops](https://kops.sigs.k8s.io/): An automated cluster provisioning tool.
  For tutorials, best practices, configuration options and information on
  reaching out to the community, please check the
  [`kOps` website](https://kops.sigs.k8s.io/) for details.
* [kubespray](https://kubespray.io/):
  A composition of [Ansible](https://docs.ansible.com/) playbooks,
  [inventory](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/ansible/inventory.md),
  provisioning tools, and domain knowledge for generic OS/Kubernetes clusters configuration
  management tasks. You can reach out to the community on Slack channel
  [#kubespray](https://kubernetes.slack.com/messages/kubespray/).
