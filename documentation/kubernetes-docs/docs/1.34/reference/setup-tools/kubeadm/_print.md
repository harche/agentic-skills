This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/reference/setup-tools/kubeadm/).

# Kubeadm

* 1: [Kubeadm Generated](#pg-36c22b52e8447eb3d2452d4f56fbea9b)

+ 1.1:
+ 1.2:

- 1.2.1:
- 1.2.2:
- 1.2.3:
- 1.2.4:
- 1.2.5:
- 1.2.6:
- 1.2.7:
- 1.2.8:
- 1.2.9:
- 1.2.10:
- 1.2.11:
- 1.2.12:
- 1.2.13:
- 1.2.14:
- 1.2.15:
- 1.2.16:

+ 1.3:

+ 1.4:

- 1.4.1:
- 1.4.2:
- 1.4.3:
- 1.4.4:
- 1.4.5:
- 1.4.6:
- 1.4.7:
- 1.4.8:
- 1.4.9:
- 1.4.10:

+ 1.5:

- 1.5.1:
- 1.5.2:
- 1.5.3:
- 1.5.4:
- 1.5.5:
- 1.5.6:
- 1.5.7:
- 1.5.8:
- 1.5.9:
- 1.5.10:
- 1.5.11:
- 1.5.12:
- 1.5.13:
- 1.5.14:
- 1.5.15:
- 1.5.16:
- 1.5.17:
- 1.5.18:
- 1.5.19:
- 1.5.20:
- 1.5.21:
- 1.5.22:
- 1.5.23:
- 1.5.24:
- 1.5.25:
- 1.5.26:
- 1.5.27:
- 1.5.28:
- 1.5.29:
- 1.5.30:
- 1.5.31:
- 1.5.32:
- 1.5.33:
- 1.5.34:
- 1.5.35:
- 1.5.36:
- 1.5.37:
- 1.5.38:
- 1.5.39:
- 1.5.40:
- 1.5.41:
- 1.5.42:
- 1.5.43:
- 1.5.44:
- 1.5.45:
- 1.5.46:

+ 1.6:

- 1.6.1:
- 1.6.2:
- 1.6.3:
- 1.6.4:
- 1.6.5:
- 1.6.6:
- 1.6.7:
- 1.6.8:
- 1.6.9:
- 1.6.10:
- 1.6.11:
- 1.6.12:
- 1.6.13:
- 1.6.14:

+ 1.7:

- 1.7.1:

+ 1.8:

- 1.8.1:
- 1.8.2:
- 1.8.3:
- 1.8.4:

+ 1.9:

- 1.9.1:
- 1.9.2:
- 1.9.3:
- 1.9.4:

+ 1.10:

- 1.10.1:
- 1.10.2:
- 1.10.3:
- 1.10.4:
- 1.10.5:
- 1.10.6:
- 1.10.7:
- 1.10.8:
- 1.10.9:
- 1.10.10:
- 1.10.11:
- 1.10.12:
- 1.10.13:
- 1.10.14:
- 1.10.15:
- 1.10.16:
- 1.10.17:
- 1.10.18:
- 1.10.19:
- 1.10.20:
- 1.10.21:
- 1.10.22:
- 1.10.23:
- 1.10.24:
- 1.10.25:
- 1.10.26:
- 1.10.27:

+ 1.11:

+ 1.12:

* 2: [kubeadm init](#pg-82b2fcf985bae77dcb754387a9fcc64f)
* 3: [kubeadm join](#pg-2a2b5f34806b4b1bd2c12682ac170d68)
* 4: [kubeadm upgrade](#pg-2c20539d9fabf5982e2dd931742714bd)
* 5: [kubeadm upgrade phases](#pg-dfd085b5ab706bd84dda15847dd27f1b)
* 6: [kubeadm config](#pg-5042dc49c5348b3674d3878f37f7670b)
* 7: [kubeadm reset](#pg-6eb5bc1e7114609930a76c683cc27c2b)
* 8: [kubeadm token](#pg-516f4705fb2f5f62c76c7742772726a3)
* 9: [kubeadm version](#pg-34c4af6f36d969ed08ba840e7fb64c6d)
* 10: [kubeadm alpha](#pg-92a39c69c3689119dd5fa12886cb73a3)
* 11: [kubeadm certs](#pg-6a1fed09235bbf3644c804339928f10e)
* 12: [kubeadm init phase](#pg-fbe8dcd222ce5795a5c325670a26b067)
* 13: [kubeadm join phase](#pg-62a742c564b0b5b7ac12a95e67cc425a)
* 14: [kubeadm kubeconfig](#pg-1ab2d643d770ca684548de4ddbc7d8c4)
* 15: [kubeadm reset phase](#pg-b969d0033ce5d9036463521fb1f150b3)
* 16: [Implementation details](#pg-455b6412a275b743ee8ad90f35808393)

![](/images/kubeadm-stacked-color.png)Kubeadm is a tool built to provide `kubeadm init` and `kubeadm join` as best-practice "fast paths" for creating Kubernetes clusters.

kubeadm performs the actions necessary to get a minimum viable cluster up and running. By design, it cares only about bootstrapping, not about provisioning machines. Likewise, installing various nice-to-have addons, like the Kubernetes Dashboard, monitoring solutions, and cloud-specific addons, is not in scope.

Instead, we expect higher-level and more tailored tooling to be built on top of kubeadm, and ideally, using kubeadm as the basis of all deployments will make it easier to create conformant clusters.

## How to install

To install kubeadm, see the [installation guide](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/).

## What's next

* [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) to bootstrap a Kubernetes control-plane node
* [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) to bootstrap a Kubernetes worker node and join it to the cluster
* [kubeadm upgrade](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/) to upgrade a Kubernetes cluster to a newer version
* [kubeadm config](/docs/reference/setup-tools/kubeadm/kubeadm-config/) if you initialized your cluster using kubeadm v1.7.x or lower, to configure your cluster for `kubeadm upgrade`
* [kubeadm token](/docs/reference/setup-tools/kubeadm/kubeadm-token/) to manage tokens for `kubeadm join`
* [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) to revert any changes made to this host by `kubeadm init` or `kubeadm join`
* [kubeadm certs](/docs/reference/setup-tools/kubeadm/kubeadm-certs/) to manage Kubernetes certificates
* [kubeadm kubeconfig](/docs/reference/setup-tools/kubeadm/kubeadm-kubeconfig/) to manage kubeconfig files
* [kubeadm version](/docs/reference/setup-tools/kubeadm/kubeadm-version/) to print the kubeadm version
* [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha/) to preview a set of features made available for gathering feedback from the community
