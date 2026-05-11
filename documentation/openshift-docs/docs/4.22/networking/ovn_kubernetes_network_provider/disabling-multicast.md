# Disabling multicast between pods

You can disable multicast between pods for your project.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- You must log in to the cluster with a user that has the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Disable multicast by running the following command:

  ``` terminal
  $ oc annotate namespace <namespace> \
      k8s.ovn.org/multicast-enabled-
  ```

  - The `namespace` for the project you want to disable multicast for.

    > [!TIP]
    > You can alternatively apply the following YAML to delete the annotation:
    >
    > ``` yaml
    > apiVersion: v1
    > kind: Namespace
    > metadata:
    >   name: <namespace>
    >   annotations:
    >     k8s.ovn.org/multicast-enabled: null
    > ```

</div>
