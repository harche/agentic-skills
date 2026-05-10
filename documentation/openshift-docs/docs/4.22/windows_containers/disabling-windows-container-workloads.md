You can disable the capability to run Windows container workloads by uninstalling the Windows Machine Config Operator (WMCO) and deleting the namespace that was added by default when you installed the WMCO.

# Uninstalling the Windows Machine Config Operator

You can uninstall the Windows Machine Config Operator (WMCO) from your cluster.

<div>

<div class="title">

Prerequisites

</div>

- Delete the Windows `Machine` objects hosting your Windows workloads.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From the **Ecosystem** → **Software Catalog** page, use the **Filter by keyword** box to search for `Red Hat Windows Machine Config Operator`.

2.  Click the **Red Hat Windows Machine Config Operator** tile. The Operator tile indicates it is installed.

3.  In the **Windows Machine Config Operator** descriptor page, click **Uninstall**.

</div>

# Deleting the Windows Machine Config Operator namespace

You can delete the namespace that was generated for the Windows Machine Config Operator (WMCO) by default.

<div>

<div class="title">

Prerequisites

</div>

- The WMCO is removed from your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Remove all Windows workloads that were created in the `openshift-windows-machine-config-operator` namespace:

    ``` terminal
    $ oc delete --all pods --namespace=openshift-windows-machine-config-operator
    ```

2.  Verify that all pods in the `openshift-windows-machine-config-operator` namespace are deleted or are reporting a terminating state:

    ``` terminal
    $ oc get pods --namespace openshift-windows-machine-config-operator
    ```

3.  Delete the `openshift-windows-machine-config-operator` namespace:

    ``` terminal
    $ oc delete namespace openshift-windows-machine-config-operator
    ```

</div>

# Additional resources

- [Deleting Operators from a cluster](../operators/admin/olm-deleting-operators-from-cluster.xml#olm-deleting-operators-from-a-cluster)

- [Removing Windows nodes](../windows_containers/removing-windows-nodes.xml#removing-windows-nodes)
