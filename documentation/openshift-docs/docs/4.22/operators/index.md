Operators are among the most important components of OpenShift Container Platform. They are the preferred method of packaging, deploying, and managing services on the control plane. They can also provide advantages to applications that users run.

Operators integrate with Kubernetes APIs and CLI tools such as `kubectl` and the OpenShift CLI (`oc`). They provide the means of monitoring applications, performing health checks, managing over-the-air (OTA) updates, and ensuring that applications remain in your specified state.

Operators are designed specifically for Kubernetes-native applications to implement and automate common Day 1 operations, such as installation and configuration. Operators can also automate Day 2 operations, such as autoscaling up or down and creating backups. All of these activities are directed by a piece of software running on your cluster.

While both follow similar Operator concepts and goals, Operators in OpenShift Container Platform are managed by two different systems, depending on their purpose:

Cluster Operators
Managed by the Cluster Version Operator (CVO) and installed by default to perform cluster functions.

Optional add-on Operators
Managed by Operator Lifecycle Manager (OLM) and can be made accessible for users to run in their applications. Also known as *OLM-based Operators*.

# For developers

As an Operator author, you can perform the following development tasks for OLM-based Operators:

- [Install and subscribe an Operator to your namespace](../operators/user/olm-installing-operators-in-namespace.xml#olm-installing-operators-in-namespace).

- [Create an application from an installed Operator through the web console](../operators/user/olm-creating-apps-from-installed-operators.xml#olm-creating-apps-from-installed-operators).

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Machine deletion lifecycle hook examples for Operator developers](../machine_management/deleting-machine.xml#machine-lifecycle-hook-deletion-uses_deleting-machine)

</div>

# For administrators

As a cluster administrator, you can perform the following administrative tasks for OLM-based Operators:

- [Manage custom catalogs](../operators/admin/olm-managing-custom-catalogs.xml#olm-managing-custom-catalogs).

- [Allow non-cluster administrators to install Operators](../operators/admin/olm-creating-policy.xml#olm-creating-policy).

- [Install an Operator from the software catalog](../operators/user/olm-installing-operators-in-namespace.xml#olm-installing-operators-in-namespace).

- [View Operator status](../operators/admin/olm-status.xml#olm-status).

- [Manage Operator conditions](../operators/admin/olm-managing-operatorconditions.xml#olm-managing-operatorconditions).

- [Upgrade installed Operators](../operators/admin/olm-upgrading-operators.xml#olm-upgrading-operators).

- [Delete installed Operators](../operators/admin/olm-deleting-operators-from-cluster.xml#olm-deleting-operators-from-a-cluster).

- [Configure proxy support](../operators/admin/olm-configuring-proxy-support.xml#olm-configuring-proxy-support).

- [Using Operator Lifecycle Manager in disconnected environments](../disconnected/using-olm.xml#olm-restricted-networks).

For information about the cluster Operators that Red Hat provides, see [Cluster Operators reference](../operators/operator-reference.xml#operator-reference).

# Next steps

- [What are Operators?](../operators/understanding/olm-what-operators-are.xml#olm-what-operators-are)
