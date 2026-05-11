<div wrapper="1" role="_abstract">

You can boot a virtual machine (VM) in Unified Extensible Firmware Interface (UEFI) mode for faster boot times, the ability to boot to larger disks, and added security features.

</div>

# About UEFI mode for virtual machines

<div wrapper="1" role="_abstract">

Unified Extensible Firmware Interface (UEFI), like legacy BIOS, initializes hardware components and operating system image files when a computer starts. UEFI supports more modern features and customization options than BIOS, enabling faster boot times.

</div>

It stores all the information about initialization and startup in a file with a `.efi` extension, which is stored on a special partition called EFI System Partition (ESP). The ESP also contains the boot loader programs for the operating system that is installed on the computer.

# Booting virtual machines in UEFI mode

<div wrapper="1" role="_abstract">

You can configure a virtual machine to boot in UEFI mode by editing the `VirtualMachine` manifest.

</div>

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit or create a `VirtualMachine` manifest file. Use the `spec.firmware.bootloader` stanza to configure UEFI mode.

    Booting in UEFI mode with secure boot active:

</div>

    apiversion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      labels:
        special: vm-secureboot
      name: vm-secureboot
    spec:
      template:
        metadata:
          labels:
            special: vm-secureboot
        spec:
          domain:
            devices:
              disks:
              - disk:
                  bus: virtio
                name: containerdisk
            features:
              acpi: {}
              smm:
                enabled: true
            firmware:
              bootloader:
                efi:
                  secureBoot: true
    # ...

\+ \* You must set `spec.template.spec.domain.features.ssm.enabled` to have a value of `true`. \* If `spec.template.spec.domain.firmware.bootloader.efi.secureBoot` is set to `true`, then UEFI mode is required. However, you can enable UEFI mode without using Secure Boot.

1.  Apply the manifest to your cluster by running the following command:

    ``` terminal
    $ oc create -f <file_name>.yaml
    ```

# Enabling persistent EFI

<div wrapper="1" role="_abstract">

You can enable EFI persistence in a VM by configuring an RWX storage class at the cluster level and adjusting the settings in the EFI section of the VM.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You must have cluster administrator privileges.

- You must have a storage class that supports RWX access mode and FS volume mode.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- Enable the `VMPersistentState` feature gate by running the following command:

  ``` terminal
  $ oc patch hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv \
    --type json -p '[{"op":"replace","path":"/spec/featureGates/VMPersistentState", "value": true}]'
  ```

</div>

# Configuring VMs with persistent EFI

<div wrapper="1" role="_abstract">

You can configure a VM to have EFI persistence enabled by editing its manifest file.

</div>

<div>

<div class="title">

Prerequisites

</div>

- `VMPersistentState` feature gate enabled.

</div>

<div>

<div class="title">

Procedure

</div>

- Edit the VM manifest file and save to apply settings.

  ``` yaml
  apiVersion: kubevirt.io/v1
  kind: VirtualMachine
  metadata:
    name: vm
  spec:
    template:
      spec:
        domain:
          firmware:
            bootloader:
              efi:
                persistent: true
  # ...
  ```

</div>
