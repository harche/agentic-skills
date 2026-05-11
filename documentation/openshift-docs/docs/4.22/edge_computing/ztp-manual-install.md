You can deploy a managed single-node OpenShift cluster by using Red Hat Advanced Cluster Management (RHACM) and the assisted service.

> [!NOTE]
> If you are creating multiple managed clusters, use the `ClusterInstance` method described in [Deploying far edge sites with ZTP](../edge_computing/ztp-deploying-far-edge-sites.xml#ztp-deploying-far-edge-sites).

> [!IMPORTANT]
> The target bare-metal host must meet the networking, firmware, and hardware requirements listed in [Recommended cluster configuration for vDU application workloads](../edge_computing/ztp-reference-cluster-configuration-for-vdu.xml#sno-configure-for-vdu).

# Extracting reference and example CRs from the ztp-site-generate container

Use the `ztp-site-generate` container to extract reference custom resources (CRs) and example `ClusterInstance` CRs to prepare for cluster installation and Day 2 configuration.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to the hub cluster as a user with `cluster-admin` privileges.

- You installed `podman`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an output folder by running the following command:

    ``` terminal
    $ mkdir -p ./out
    ```

2.  Log in to the Ecosystem container registry with your credentials by running the following command:

    ``` terminal
    $ podman login registry.redhat.io
    ```

3.  Extract the reference and example CRs from the `ztp-site-generate` container image by running the following command:

    ``` terminal
    $ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.17 extract /home/ztp --tar | tar x -C ./out
    ```

    The `./out` directory contains the reference `PolicyGenerator` and `ClusterInstance` CRs in the `out/argocd/example/` folder.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    out
     └── argocd
          └── example
               ├── acmpolicygenerator
               │     ├── {policy-prefix}common-ranGen.yaml
               │     ├── {policy-prefix}example-sno-site.yaml
               │     ├── {policy-prefix}group-du-sno-ranGen.yaml
               │     ├── ...
               │     ├── kustomization.yaml
               │     └── ns.yaml
               └── clusterinstance
                     ├── example-sno.yaml
                     ├── example-3node.yaml
                     ├── example-standard.yaml
                     └── ...
    ```

    </div>

4.  Create a `ClusterInstance` CR for your cluster.

    Use the example `ClusterInstance` CRs in the `out/argocd/example/clusterinstance/` folder that you previously extracted from the `ztp-site-generate` container as a reference. The folder includes example files for single node, three-node, and standard clusters:

    - `example-sno.yaml`

    - `example-3node.yaml`

    - `example-standard.yaml`

      Change the cluster and host details in the example file to match the type of cluster you want to install. For example:

      <div class="formalpara">

      <div class="title">

      Example single-node OpenShift ClusterInstance CR

      </div>

      ``` yaml
      # example-node1-bmh-secret & assisted-deployment-pull-secret need to be created under same namespace example-ai-sno
      ---
      apiVersion: siteconfig.open-cluster-management.io/v1alpha1
      kind: ClusterInstance
      metadata:
        name: "example-ai-sno"
        namespace: "example-ai-sno"
      spec:
        baseDomain: "example.com"
        pullSecretRef:
          name: "assisted-deployment-pull-secret"
        clusterImageSetNameRef: "openshift-4.21"
        sshPublicKey: "ssh-rsa AAAA..."
        clusterName: "example-ai-sno"
        networkType: "OVNKubernetes"
        # installConfigOverrides is a generic way of passing install-config
        # parameters through the siteConfig.  The 'capabilities' field configures
        # the composable openshift feature.  In this 'capabilities' setting, we
        # remove all the optional set of components.
        # Notes:
        # - OperatorLifecycleManager is needed for 4.15 and later
        # - NodeTuning is needed for 4.13 and later, not for 4.12 and earlier
        # - Ingress is needed for 4.16 and later
        installConfigOverrides: |
          {
            "capabilities": {
              "baselineCapabilitySet": "None",
              "additionalEnabledCapabilities": [
                "NodeTuning",
                "OperatorLifecycleManager",
                "Ingress"
              ]
            }
          }
        # Include references to extraManifest ConfigMaps.
        extraManifestsRefs:
          - name: sno-extra-manifest-configmap
        extraLabels:
          ManagedCluster:
            # These example cluster labels correspond to the bindingRules in the PolicyGenTemplate examples
            du-profile: "latest"
            # These example cluster labels correspond to the bindingRules in the PolicyGenTemplate examples in ../policygentemplates:
            # ../policygentemplates/common-ranGen.yaml will apply to all clusters with 'common: true'
            common: "true"
            # ../policygentemplates/group-du-sno-ranGen.yaml will apply to all clusters with 'group-du-sno: ""'
            group-du-sno: ""
            # ../policygentemplates/example-sno-site.yaml will apply to all clusters with 'sites: "example-sno"'
            # Normally this should match or contain the cluster name so it only applies to a single cluster
            sites : "example-sno"
        clusterNetwork:
          - cidr: 1001:1::/48
            hostPrefix: 64
        machineNetwork:
          - cidr: 1111:2222:3333:4444::/64
        serviceNetwork:
          - cidr: 1001:2::/112
        additionalNTPSources:
          - 1111:2222:3333:4444::2
        # Initiates the cluster for workload partitioning. Setting specific reserved/isolated CPUSets is done via PolicyTemplate
        # please see Workload Partitioning Feature for a complete guide.
        cpuPartitioningMode: AllNodes
        templateRefs:
          - name: ai-cluster-templates-v1
            namespace: open-cluster-management
        nodes:
          - hostName: "example-node1.example.com"
            role: "master"
            bmcAddress: "idrac-virtualmedia+https://[1111:2222:3333:4444::bbbb:1]/redfish/v1/Systems/System.Embedded.1"
            bmcCredentialsName:
              name: "example-node1-bmh-secret"
            bootMACAddress: "AA:BB:CC:DD:EE:11"
            # Use UEFISecureBoot to enable secure boot, UEFI to disable.
            bootMode: "UEFISecureBoot"
            rootDeviceHints:
              deviceName: "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0"
            # disk partition at `/var/lib/containers` with ignitionConfigOverride. Some values must be updated. See DiskPartitionContainer.md in argocd folder for more details
            ignitionConfigOverride: |
              {
                "ignition": {
                  "version": "3.2.0"
                },
                "storage": {
                  "disks": [
                    {
                      "device": "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0",
                      "partitions": [
                        {
                          "label": "var-lib-containers",
                          "sizeMiB": 0,
                          "startMiB": 250000
                        }
                      ],
                      "wipeTable": false
                    }
                  ],
                  "filesystems": [
                    {
                      "device": "/dev/disk/by-partlabel/var-lib-containers",
                      "format": "xfs",
                      "mountOptions": [
                        "defaults",
                        "prjquota"
                      ],
                      "path": "/var/lib/containers",
                      "wipeFilesystem": true
                    }
                  ]
                },
                "systemd": {
                  "units": [
                    {
                      "contents": "# Generated by Butane\n[Unit]\nRequires=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\nAfter=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\n\n[Mount]\nWhere=/var/lib/containers\nWhat=/dev/disk/by-partlabel/var-lib-containers\nType=xfs\nOptions=defaults,prjquota\n\n[Install]\nRequiredBy=local-fs.target",
                      "enabled": true,
                      "name": "var-lib-containers.mount"
                    }
                  ]
                }
              }
            nodeNetwork:
              interfaces:
                - name: eno1
                  macAddress: "AA:BB:CC:DD:EE:11"
              config:
                interfaces:
                  - name: eno1
                    type: ethernet
                    state: up
                    ipv4:
                      enabled: false
                    ipv6:
                      enabled: true
                      address:
                      # For SNO sites with static IP addresses, the node-specific,
                      # API and Ingress IPs should all be the same and configured on
                      # the interface
                      - ip: 1111:2222:3333:4444::aaaa:1
                        prefix-length: 64
                dns-resolver:
                  config:
                    search:
                    - example.com
                    server:
                    - 1111:2222:3333:4444::2
                routes:
                  config:
                  - destination: ::/0
                    next-hop-interface: eno1
                    next-hop-address: 1111:2222:3333:4444::1
                    table-id: 254
            templateRefs:
              - name: ai-node-templates-v1
                namespace: open-cluster-management
      ```

      </div>

      > [!NOTE]
      > Optional: To provision additional install-time manifests on the provisioned cluster, create the extra manifest CRs and apply them to the hub cluster. Then reference them in the `extraManifestsRefs` field of the `ClusterInstance` CR. For more information, see "Customizing extra installation manifests in the GitOps ZTP pipeline".

5.  Optional: Generate Day 2 configuration CRs from the reference `PolicyGenerator` CRs:

    1.  Create an output folder for the configuration CRs by running the following command:

        ``` terminal
        $ mkdir -p ./ref
        ```

    2.  Generate the configuration CRs by running the following command:

        ``` terminal
        $ podman run -it --rm -v `pwd`/out/argocd/example/policygentemplates:/resources:Z -v `pwd`/ref:/output:Z,U registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.17 generator config -N . /output
        ```

        The command generates example group and cluster-specific configuration CRs in the `./ref` folder. You can apply these CRs to the cluster after installation is complete.

</div>

# Creating the managed bare-metal host secrets

Add the required `Secret` custom resources (CRs) for the managed bare-metal host to the hub cluster. You need a secret for the GitOps Zero Touch Provisioning (ZTP) pipeline to access the Baseboard Management Controller (BMC) and a secret for the assisted installer service to pull cluster installation images from the registry.

> [!NOTE]
> The secrets are referenced from the `ClusterInstance` CR by name. The namespace must match the `ClusterInstance` namespace.

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML secret file containing credentials for the host Baseboard Management Controller (BMC) and a pull secret required for installing OpenShift and all add-on cluster Operators:

    1.  Save the following YAML as the file `example-sno-secret.yaml`:

        ``` yaml
        apiVersion: v1
        kind: Secret
        metadata:
          name: example-sno-bmc-secret
          namespace: example-sno
        data:
          password: <base64_password>
          username: <base64_username>
        type: Opaque
        ---
        apiVersion: v1
        kind: Secret
        metadata:
          name: pull-secret
          namespace: example-sno
        data:
          .dockerconfigjson: <pull_secret>
        type: kubernetes.io/dockerconfigjson
        ```

        - Must match the namespace configured in the related `ClusterInstance` CR

        - Base64-encoded values for `password` and `username`

        - Must match the namespace configured in the related `ClusterInstance` CR

        - Base64-encoded pull secret

2.  Add the relative path to `example-sno-secret.yaml` to the `kustomization.yaml` file that you use to install the cluster.

</div>

# Configuring Discovery ISO kernel arguments for manual installations using GitOps ZTP

The GitOps Zero Touch Provisioning (ZTP) workflow uses the Discovery ISO as part of the OpenShift Container Platform installation process on managed bare-metal hosts. You can edit the `InfraEnv` resource to specify kernel arguments for the Discovery ISO. This is useful for cluster installations with specific environmental requirements. For example, configure the `rd.net.timeout.carrier` kernel argument for the Discovery ISO to facilitate static networking for the cluster or to receive a DHCP address before downloading the root file system during installation.

> [!NOTE]
> In OpenShift Container Platform 4.17, you can only add kernel arguments. You can not replace or delete kernel arguments.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (oc).

- You have logged in to the hub cluster as a user with cluster-admin privileges.

- You have applied a `ClusterInstance` CR to the hub cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `spec.kernelArguments` specification in the `InfraEnv` CR to configure kernel arguments:

</div>

``` yaml
apiVersion: agent-install.openshift.io/v1beta1
kind: InfraEnv
metadata:
  name: <cluster_name>
  namespace: <cluster_name>
spec:
  kernelArguments:
    - operation: append
      value: audit=0
    - operation: append
      value: trace=1
  clusterRef:
    name: <cluster_name>
    namespace: <cluster_name>
  pullSecretRef:
    name: pull-secret
```

- Specify the append operation to add a kernel argument.

- Specify the kernel argument you want to configure. This example configures the audit kernel argument and the trace kernel argument.

> [!NOTE]
> The `ClusterInstance` CR generates the `InfraEnv` resource as part of the day-0 installation CRs.

<div class="formalpara">

<div class="title">

Verification

</div>

To verify that the kernel arguments are applied, after the Discovery image verifies that OpenShift Container Platform is ready for installation, you can SSH to the target host before the installation process begins. At that point, you can view the kernel arguments for the Discovery ISO in the `/proc/cmdline` file.

</div>

1.  Begin an SSH session with the target host:

    ``` terminal
    $ ssh -i /path/to/privatekey core@<host_name>
    ```

2.  View the system’s kernel arguments by using the following command:

    ``` terminal
    $ cat /proc/cmdline
    ```

# Installing a single managed cluster

You can manually deploy a single managed cluster using the assisted service and Red Hat Advanced Cluster Management (RHACM).

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to the hub cluster as a user with `cluster-admin` privileges.

- You have extracted the reference and example CRs from the `ztp-site-generate` container and you configured the `ClusterInstance` CR.

- You have created the baseboard management controller (BMC) `Secret` and the image pull-secret `Secret` custom resources (CRs). See "Creating the managed bare-metal host secrets" for details.

- Your target bare-metal host meets the networking and hardware requirements for managed clusters.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `ClusterImageSet` for each specific cluster version to be deployed, for example `clusterImageSet-4.17.yaml`. A `ClusterImageSet` has the following format:

    ``` yaml
    apiVersion: hive.openshift.io/v1
    kind: ClusterImageSet
    metadata:
      name: openshift-4.17.0
    spec:
       releaseImage: quay.io/openshift-release-dev/ocp-release:4.17.0-x86_64
    ```

    - The descriptive version that you want to deploy.

    - Specifies the `releaseImage` to deploy and determines the operating system image version. The discovery ISO is based on the image version as set by `releaseImage`, or the latest version if the exact version is unavailable.

2.  Apply the `clusterImageSet` CR:

    ``` terminal
    $ oc apply -f clusterImageSet-4.17.yaml
    ```

3.  Create the `Namespace` CR in the `cluster-namespace.yaml` file:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
         name: <cluster_name>
         labels:
            name: <cluster_name>
    ```

    - The name of the managed cluster to provision.

4.  Apply the `Namespace` CR by running the following command:

    ``` terminal
    $ oc apply -f cluster-namespace.yaml
    ```

5.  Apply the `ClusterInstance` CR that you configured to the hub cluster by running the following command:

    ``` terminal
    $ oc apply -f clusterinstance.yaml
    ```

    The SiteConfig Operator processes the `ClusterInstance` CR and automatically generates the required installation CRs, including `BareMetalHost`, `AgentClusterInstall`, `ClusterDeployment`, `InfraEnv`, and `NMStateConfig`. The assisted service then begins the cluster installation.

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [BMC addressing](../installing/installing_bare_metal/ipi/ipi-install-installation-workflow.xml#bmc-addressing_ipi-install-installation-workflow)

- [About root device hints](../installing/installing_with_agent_based_installer/preparing-to-install-with-agent-based-installer.xml#root-device-hints_preparing-to-install-with-agent-based-installer)

- [Single-node OpenShift ClusterInstance CR installation reference](../edge_computing/ztp-deploying-far-edge-sites.xml#ztp-clusterinstance-config-reference_ztp-deploying-far-edge-sites)

- [Connectivity prerequisites for managed cluster networks](../edge_computing/ztp-reference-cluster-configuration-for-vdu.xml#ztp-managed-cluster-network-prereqs_sno-configure-for-vdu)

- [Deploying LVM Storage on single-node OpenShift clusters](../storage/persistent_storage_local/persistent-storage-using-lvms.xml#lvms-preface-sno-ran_logical-volume-manager-storage)

- [Configuring LVM Storage using PolicyGenerator CRs](../edge_computing/policygenerator_for_ztp/ztp-advanced-policygenerator-config.xml#ztp-provisioning-lvm-storage_ztp-advanced-policy-config)

- [Configuring managed cluster policies by using PolicyGenerator resources](../edge_computing/policygenerator_for_ztp/ztp-configuring-managed-clusters-policygenerator.xml#ztp-configuring-managed-clusters-policygenerator)

</div>

# Monitoring the managed cluster installation status

Ensure that cluster provisioning was successful by checking the cluster status.

<div>

<div class="title">

Prerequisites

</div>

- All of the custom resources have been configured and provisioned, and the `Agent` custom resource is created on the hub for the managed cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check the status of the managed cluster:

    ``` terminal
    $ oc get managedcluster
    ```

    `True` indicates the managed cluster is ready.

2.  Check the agent status:

    ``` terminal
    $ oc get agent -n <cluster_name>
    ```

3.  Use the `describe` command to provide an in-depth description of the agent’s condition. Statuses to be aware of include `BackendError`, `InputError`, `ValidationsFailing`, `InstallationFailed`, and `AgentIsConnected`. These statuses are relevant to the `Agent` and `AgentClusterInstall` custom resources.

    ``` terminal
    $ oc describe agent -n <cluster_name>
    ```

4.  Check the cluster provisioning status:

    ``` terminal
    $ oc get agentclusterinstall -n <cluster_name>
    ```

5.  Use the `describe` command to provide an in-depth description of the cluster provisioning status:

    ``` terminal
    $ oc describe agentclusterinstall -n <cluster_name>
    ```

6.  Check the status of the managed cluster’s add-on services:

    ``` terminal
    $ oc get managedclusteraddon -n <cluster_name>
    ```

7.  Retrieve the authentication information of the `kubeconfig` file for the managed cluster:

    ``` terminal
    $ oc get secret -n <cluster_name> <cluster_name>-admin-kubeconfig -o jsonpath={.data.kubeconfig} | base64 -d > <directory>/<cluster_name>-kubeconfig
    ```

</div>

# Troubleshooting the managed cluster

Use this procedure to diagnose any installation issues that might occur with the managed cluster.

<div>

<div class="title">

Procedure

</div>

1.  Check the status of the managed cluster:

    ``` terminal
    $ oc get managedcluster
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME            HUB ACCEPTED   MANAGED CLUSTER URLS   JOINED   AVAILABLE   AGE
    SNO-cluster     true                                   True     True      2d19h
    ```

    </div>

    If the status in the `AVAILABLE` column is `True`, the managed cluster is being managed by the hub.

    If the status in the `AVAILABLE` column is `Unknown`, the managed cluster is not being managed by the hub. Use the following steps to continue checking to get more information.

2.  Check the `AgentClusterInstall` install status:

    ``` terminal
    $ oc get clusterdeployment -n <cluster_name>
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME        PLATFORM            REGION   CLUSTERTYPE   INSTALLED    INFRAID    VERSION  POWERSTATE AGE
    Sno0026    agent-baremetal                               false                          Initialized
    2d14h
    ```

    </div>

    If the status in the `INSTALLED` column is `false`, the installation was unsuccessful.

3.  If the installation failed, enter the following command to review the status of the `AgentClusterInstall` resource:

    ``` terminal
    $ oc describe agentclusterinstall -n <cluster_name> <cluster_name>
    ```

4.  Resolve the errors and reset the cluster:

    1.  Remove the cluster’s managed cluster resource:

        ``` terminal
        $ oc delete managedcluster <cluster_name>
        ```

    2.  Remove the cluster’s namespace:

        ``` terminal
        $ oc delete namespace <cluster_name>
        ```

        This deletes all of the namespace-scoped custom resources created for this cluster. You must wait for the `ManagedCluster` CR deletion to complete before proceeding.

    3.  Recreate the custom resources for the managed cluster.

</div>

# RHACM generated cluster installation CRs reference

Red Hat Advanced Cluster Management (RHACM) supports deploying OpenShift Container Platform on single-node clusters, three-node clusters, and standard clusters with a specific set of installation custom resources (CRs) that you generate using `ClusterInstance` CRs for each cluster.

> [!NOTE]
> Every managed cluster has its own namespace, and all of the installation CRs except for `ManagedCluster` and `ClusterImageSet` are under that namespace. `ManagedCluster` and `ClusterImageSet` are cluster-scoped, not namespace-scoped. The namespace and the CR names match the cluster name.

The following table lists the installation CRs that are automatically applied by the RHACM assisted service when it installs clusters using the `ClusterInstance` CRs that you configure.

<table>
<caption>Cluster installation CRs generated by RHACM</caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 42%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">CR</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Usage</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>BareMetalHost</code></p></td>
<td style="text-align: left;"><p>Contains the connection information for the Baseboard Management Controller (BMC) of the target bare-metal host.</p></td>
<td style="text-align: left;"><p>Provides access to the BMC to load and start the discovery image on the target server by using the Redfish protocol.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>InfraEnv</code></p></td>
<td style="text-align: left;"><p>Contains information for installing OpenShift Container Platform on the target bare-metal host.</p></td>
<td style="text-align: left;"><p>Used with <code>ClusterDeployment</code> to generate the discovery ISO for the managed cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>AgentClusterInstall</code></p></td>
<td style="text-align: left;"><p>Specifies details of the managed cluster configuration such as networking and the number of control plane nodes. Displays the cluster <code>kubeconfig</code> and credentials when the installation is complete.</p></td>
<td style="text-align: left;"><p>Specifies the managed cluster configuration information and provides status during the installation of the cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ClusterDeployment</code></p></td>
<td style="text-align: left;"><p>References the <code>AgentClusterInstall</code> CR to use.</p></td>
<td style="text-align: left;"><p>Used with <code>InfraEnv</code> to generate the discovery ISO for the managed cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>NMStateConfig</code></p></td>
<td style="text-align: left;"><p>Provides network configuration information such as <code>MAC</code> address to <code>IP</code> mapping, DNS server, default route, and other network settings.</p></td>
<td style="text-align: left;"><p>Sets up a static IP address for the managed cluster’s Kube API server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Agent</code></p></td>
<td style="text-align: left;"><p>Contains hardware information about the target bare-metal host.</p></td>
<td style="text-align: left;"><p>Created automatically on the hub when the target machine’s discovery image boots.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ManagedCluster</code></p></td>
<td style="text-align: left;"><p>When a cluster is managed by the hub, it must be imported and known. This Kubernetes object provides that interface.</p></td>
<td style="text-align: left;"><p>The hub uses this resource to manage and show the status of managed clusters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>KlusterletAddonConfig</code></p></td>
<td style="text-align: left;"><p>Contains the list of services provided by the hub to be deployed to the <code>ManagedCluster</code> resource.</p></td>
<td style="text-align: left;"><p>Tells the hub which addon services to deploy to the <code>ManagedCluster</code> resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Namespace</code></p></td>
<td style="text-align: left;"><p>Logical space for <code>ManagedCluster</code> resources existing on the hub. Unique per site.</p></td>
<td style="text-align: left;"><p>Propagates resources to the <code>ManagedCluster</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Secret</code></p></td>
<td style="text-align: left;"><p>Two CRs are created: <code>BMC Secret</code> and <code>Image Pull Secret</code>.</p></td>
<td style="text-align: left;"><ul>
<li><p><code>BMC Secret</code> authenticates into the target bare-metal host using its username and password.</p></li>
<li><p><code>Image Pull Secret</code> contains authentication information for the OpenShift Container Platform image installed on the target bare-metal host.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ClusterImageSet</code></p></td>
<td style="text-align: left;"><p>Contains OpenShift Container Platform image information such as the repository and image name.</p></td>
<td style="text-align: left;"><p>Passed into resources to provide OpenShift Container Platform images.</p></td>
</tr>
</tbody>
</table>
