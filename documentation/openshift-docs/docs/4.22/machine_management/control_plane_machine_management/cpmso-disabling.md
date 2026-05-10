<div wrapper="1" role="_abstract">

Disable the control plane machine set if you need to manually manage control plane machines or troubleshoot Operator behavior.

</div>

The `.spec.state` field in an activated `ControlPlaneMachineSet` custom resource (CR) cannot be changed from `Active` to `Inactive`. To disable the control plane machine set, you must delete the CR so that it is removed from the cluster.

When you delete the CR, the Control Plane Machine Set Operator performs cleanup operations and disables the control plane machine set. The Operator then removes the CR from the cluster and creates an inactive control plane machine set with default settings.

# Deleting the control plane machine set

<div wrapper="1" role="_abstract">

To stop managing control plane machines with the control plane machine set on your cluster, you must delete the `ControlPlaneMachineSet` custom resource (CR).

</div>

<div>

<div class="title">

Procedure

</div>

- Delete the control plane machine set CR by running the following command:

  ``` terminal
  $ oc delete controlplanemachineset.machine.openshift.io cluster \
    -n openshift-machine-api
  ```

</div>

<div>

<div class="title">

Verification

</div>

- Check the control plane machine set custom resource state. A result of `Inactive` indicates that the removal and replacement process is successful. A `ControlPlaneMachineSet` CR exists but is not activated.

</div>

# Checking the control plane machine set custom resource state

<div wrapper="1" role="_abstract">

Check the state of the control plane machine set custom resource to determine if it is active, inactive, or missing before making configuration changes.

</div>

<div>

<div class="title">

Procedure

</div>

- Determine the state of the CR by running the following command:

  ``` terminal
  $ oc get controlplanemachineset.machine.openshift.io cluster \
    --namespace openshift-machine-api
  ```

  - A result of `Active` indicates that the `ControlPlaneMachineSet` CR exists and is activated. No administrator action is required.

  - A result of `Inactive` indicates that a `ControlPlaneMachineSet` CR exists but is not activated.

  - A result of `NotFound` indicates that there is no existing `ControlPlaneMachineSet` CR.

</div>

# Re-enabling the control plane machine set

<div wrapper="1" role="_abstract">

Restore automated control plane management after previously disabling the control plane machine set.

</div>

To re-enable the control plane machine set, you must ensure that the configuration in the CR is correct for your cluster and activate it.

For more information, see "Activating the control plane machine set custom resource".

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Activating the control plane machine set custom resource](../../machine_management/control_plane_machine_management/cpmso-getting-started.xml#cpmso-activating_cpmso-getting-started)

</div>
