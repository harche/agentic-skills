<div wrapper="1" role="_abstract">

You can access a virtual machine (VM) that is connected to the default internal pod network on a stable fully qualified domain name (FQDN) by using headless services. A Kubernetes *headless service* creates a DNS record for each pod associated with the service instead of providing a single virtual IP address for the service. You can expose a VM through its FQDN without having to expose a specific TCP or UDP port.

</div>

> [!IMPORTANT]
> If you created a VM by using the OpenShift Container Platform web console, you can find its internal FQDN listed in the **Network** tile on the **Overview** tab of the **VirtualMachine details** page.

# Creating a headless service in a project by using the CLI

<div wrapper="1" role="_abstract">

To create a headless service in a namespace, add the `clusterIP: None` parameter to the service YAML definition.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `Service` manifest to expose the VM, such as the following example:

    ``` yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: mysubdomain
    spec:
      selector:
        expose: me
      clusterIP: None
      ports:
      - protocol: TCP
        port: 1234
        targetPort: 1234
    ```

    - The name of the service. This must match the `spec.subdomain` attribute in the `VirtualMachine` manifest file.

    - This service selector must match the `expose:me` label in the `VirtualMachine` manifest file.

    - Specifies a headless service.

    - The list of ports that are exposed by the service. You must define at least one port. This can be any arbitrary value as it does not affect the headless service.

2.  Save the `Service` manifest file.

3.  Create the service by running the following command:

    ``` terminal
    $ oc create -f headless_service.yaml
    ```

</div>

# Mapping a virtual machine to a headless service by using the CLI

<div wrapper="1" role="_abstract">

To connect to a virtual machine (VM) from within the cluster by using its internal fully qualified domain name (FQDN), you must first map the VM to a headless service. Set the `spec.hostname` and `spec.subdomain` parameters in the VM configuration file.

</div>

If a headless service exists with a name that matches the subdomain, a unique DNS A record is created for the VM in the form of `<vm.spec.hostname>.<vm.spec.subdomain>.<vm.metadata.namespace>.svc.cluster.local`.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `VirtualMachine` manifest to add the service selector label and subdomain by running the following command:

    ``` terminal
    $ oc edit vm <vm_name>
    ```

    Example `VirtualMachine` manifest file:

    ``` yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      name: vm-fedora
    spec:
      template:
        metadata:
          labels:
            expose: me
        spec:
          hostname: "myvm"
          subdomain: "mysubdomain"
    # ...
    ```

    - The `expose:me` label must match the `spec.selector` attribute of the `Service` manifest that you previously created.

    - If this attribute is not specified, the resulting DNS A record takes the form of `<vm.metadata.name>.<vm.spec.subdomain>.<vm.metadata.namespace>.svc.cluster.local`.

    - The `spec.subdomain` attribute must match the `metadata.name` value of the `Service` object.

2.  Save your changes and exit the editor.

3.  Restart the VM to apply the changes.

</div>

# Connecting to a virtual machine by using its internal FQDN

<div wrapper="1" role="_abstract">

You can connect to a virtual machine (VM) by using its internal fully qualified domain name (FQDN).

</div>

<div>

<div class="title">

Prerequisites

</div>

- You have installed the `virtctl` tool.

- You have identified the internal FQDN of the VM from the web console or by mapping the VM to a headless service. The internal FQDN has the format `<vm.spec.hostname>.<vm.spec.subdomain>.<vm.metadata.namespace>.svc.cluster.local`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Connect to the VM console by entering the following command:

    ``` terminal
    $ virtctl console vm-fedora
    ```

2.  To connect to the VM by using the requested FQDN, run the following command:

    ``` terminal
    $ ping myvm.mysubdomain.<namespace>.svc.cluster.local
    ```

    Example output:

    ``` terminal
    PING myvm.mysubdomain.default.svc.cluster.local (10.244.0.57) 56(84) bytes of data.
    64 bytes from myvm.mysubdomain.default.svc.cluster.local (10.244.0.57): icmp_seq=1 ttl=64 time=0.029 ms
    ```

    In the preceding example, the DNS entry for `myvm.mysubdomain.default.svc.cluster.local` points to `10.244.0.57`, which is the cluster IP address that is currently assigned to the VM.

</div>

# Additional resources

- [Exposing a VM by using a service](../../virt/vm_networking/virt-exposing-vm-with-service.xml#virt-exposing-vm-with-service)
