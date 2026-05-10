When a host preinstalled with single-node OpenShift using an image-based installation arrives at a remote site, a technician can easily reconfigure and deploy the host in a matter of minutes.

For clusters with a hub-and-spoke architecture, to complete the deployment of a preinstalled host, you must first define site-specific configuration resources on the hub cluster for each host. These resources contain configuration information such as the properties of the bare-metal host, authentication details, and other deployment and networking information.

The Image Based Install (IBI) Operator creates a configuration ISO from these resources, and then boots the host with the configuration ISO attached. The host mounts the configuration ISO and runs the reconfiguration process. When the reconfiguration completes, the single-node OpenShift cluster is ready.

> [!NOTE]
> You must create distinct configuration resources for each bare-metal host.

See the following high-level steps to deploy a preinstalled host in a cluster with a hub-and-spoke architecture:

1.  Install the IBI Operator on the hub cluster.

2.  Create site-specific configuration resources in the hub cluster for each host.

3.  The IBI Operator creates a configuration ISO from these resources and boots the target host with the configuration ISO attached.

4.  The host mounts the configuration ISO and runs the reconfiguration process. When the reconfiguration completes, the single-node OpenShift cluster is ready.

> [!NOTE]
> Alternatively, you can manually deploy a preinstalled host for a cluster without using a hub cluster. You must define an `ImageBasedConfig` resource and an installation manifest, and provide these as inputs to the `openshift-install` installation program. For more information, see "Deploying a single-node OpenShift cluster using the `openshift-install` program".

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Deploying a single-node OpenShift cluster using the `openshift-install` program](../../../edge_computing/image_base_install/ibi_deploying_sno_clusters/ibi-edge-image-based-install-standalone.xml#create-standalone-config-iso_ibi-edge-image-based-install)

</div>

# Installing the Image Based Install Operator

The Image Based Install (IBI) Operator is part of the image-based deployment workflow for preinstalled single-node OpenShift on bare-metal hosts.

> [!NOTE]
> The IBI Operator is part of the multicluster engine for Kubernetes Operator from MCE version 2.7.

<div>

<div class="title">

Prerequisites

</div>

- You logged in as a user with `cluster-admin` privileges.

- You deployed a Red Hat Advanced Cluster Management (RHACM) hub cluster or you deployed the multicluster engine for Kubernetes Operator.

- You reviewed the required versions of software components in the section "Software prerequisites for an image-based installation".

</div>

<div>

<div class="title">

Procedure

</div>

- Set the `enabled` specification to `true` for the `image-based-install-operator` component in the `MultiClusterEngine` resource by running the following command:

  ``` terminal
  $ oc patch multiclusterengines.multicluster.openshift.io multiclusterengine --type json \
  --patch '[{"op": "add", "path":"/spec/overrides/components/-", "value": {"name":"image-based-install-operator","enabled": true}}]'
  ```

</div>

<div>

<div class="title">

Verification

</div>

- Check that the Image Based Install Operator pod is running by running the following command:

  ``` terminal
  $ oc get pods -A | grep image-based
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  multicluster-engine             image-based-install-operator-57fb8sc423-bxdj8             2/2     Running     0               5m
  ```

  </div>

</div>

# Deploying a managed single-node OpenShift cluster using the IBI Operator

Create the site-specific configuration resources in the hub cluster to initiate the image-based deployment of a preinstalled host.

When you create these configuration resources in the hub cluster, the Image Based Install (IBI) Operator generates a configuration ISO and attaches it to the target host to begin the site-specific configuration process. When the configuration process completes, the single-node OpenShift cluster is ready.

> [!NOTE]
> For more information about the configuration resources that you must configure in the hub cluster, see "Cluster configuration resources for deploying a preinstalled host".

<div>

<div class="title">

Prerequisites

</div>

- You preinstalled a host with single-node OpenShift using an image-based installation.

- You logged in as a user with `cluster-admin` privileges.

- You deployed a Red Hat Advanced Cluster Management (RHACM) hub cluster or you deployed the multicluster engine for Kubernetes operator (MCE).

- You installed the IBI Operator on the hub cluster.

- You created a pull secret to authenticate pull requests. For more information, see "Using image pull secrets".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `ibi-ns` namespace by running the following command:

    ``` terminal
    $ oc create namespace ibi-ns
    ```

2.  Create the `Secret` resource for your image registry:

    1.  Create a YAML file that defines the `Secret` resource for your image registry:

        <div class="formalpara">

        <div class="title">

        Example `secret-image-registry.yaml` file

        </div>

        ``` yaml
        apiVersion: v1
        kind: Secret
        metadata:
          name: ibi-image-pull-secret
          namespace: ibi-ns
        stringData:
          .dockerconfigjson: <base64-docker-auth-code>
        type: kubernetes.io/dockerconfigjson
        ```

        </div>

        - You must provide base64-encoded credential details. See the "Additional resources" section for more information about using image pull secrets.

    2.  Create the `Secret` resource for your image registry by running the following command:

        ``` terminal
        $ oc create -f secret-image-registry.yaml
        ```

3.  Optional: Configure static networking for the host:

    1.  Create a `Secret` resource containing the static network configuration in `nmstate` format:

        <div class="formalpara">

        <div class="title">

        Example `host-network-config-secret.yaml` file

        </div>

        ``` yaml
        apiVersion: v1
        kind: Secret
        metadata:
         name: host-network-config-secret
         namespace: ibi-ns
        type: Opaque
        stringData:
         nmstate: |
          interfaces:
            - name: ens1f0
              type: ethernet
              state: up
              ipv4:
                enabled: true
                address:
                  - ip: 192.168.200.25
                    prefix-length: 24
                dhcp: false
              ipv6:
                enabled: false
          dns-resolver:
            config:
              server:
                - 192.168.15.47
                - 192.168.15.48
          routes:
            config:
              - destination: 0.0.0.0/0
                metric: 150
                next-hop-address: 192.168.200.254
                next-hop-interface: ens1f0
                table-id: 254
        ```

        </div>

        - Specify the name for the `Secret` resource.

        - Define the static network configuration in `nmstate` format.

        - Specify the name of the interface on the host. The name of the interface must match the actual NIC name as shown in the operating system. To use your MAC address for NIC matching, set the `identifier` field to `mac-address`.

        - You must specify `dhcp: false` to ensure `nmstate` assigns the static IP address to the interface.

        - Specify one or more DNS servers that the system will use to resolve domain names.

        - In this example, the default route is configured through the `ens1f0` interface to the next hop IP address `192.168.200.254`.

4.  Create the `BareMetalHost` and `Secret` resources:

    1.  Create a YAML file that defines the `BareMetalHost` and `Secret` resources:

        <div class="formalpara">

        <div class="title">

        Example `ibi-bmh.yaml` file

        </div>

        ``` yaml
        apiVersion: metal3.io/v1alpha1
        kind: BareMetalHost
        metadata:
          name: ibi-bmh
          namespace: ibi-ns
        spec:
          online: false
          bootMACAddress: 00:a5:12:55:62:64
          bmc:
            address: redfish-virtualmedia+http://192.168.111.1:8000/redfish/v1/Systems/8a5babac-94d0-4c20-b282-50dc3a0a32b5
            credentialsName: ibi-bmh-bmc-secret
          preprovisioningNetworkDataName: host-network-config-secret
          automatedCleaningMode: disabled
          externallyProvisioned: true
        ---
        apiVersion: v1
        kind: Secret
        metadata:
          name: ibi-bmh-secret
          namespace: ibi-ns
        type: Opaque
        data:
          username: <user_name>
          password: <password>
        ```

        </div>

        - Specify the name for the `BareMetalHost` resource.

        - Specify if the host should be online.

        - Specify the host boot MAC address.

        - Specify the BMC address. You can only use bare-metal host drivers that support virtual media networking booting, for example redfish-virtualmedia and idrac-virtualmedia.

        - Specify the name of the bare-metal host `Secret` resource.

        - Optional: If you require static network configuration for the host, specify the name of the `Secret` resource containing the configuration.

        - You must specify `automatedCleaningMode:disabled` to prevent the provisioning service from deleting all preinstallation artifacts, such as the seed image, during disk inspection.

        - You must specify `externallyProvisioned: true` to enable the host to boot from the preinstalled disk, instead of the configuration ISO.

        - Specify the name for the `Secret` resource.

        - Specify the username.

        - Specify the password.

    2.  Create the `BareMetalHost` and `Secret` resources by running the following command:

        ``` terminal
        $ oc create -f ibi-bmh.yaml
        ```

5.  Create the `ClusterImageSet` resource:

    1.  Create a YAML file that defines the `ClusterImageSet` resource:

        <div class="formalpara">

        <div class="title">

        Example `ibi-cluster-image-set.yaml` file

        </div>

        ``` yaml
        apiVersion: hive.openshift.io/v1
        kind: ClusterImageSet
        metadata:
          name: ibi-img-version-arch
        spec:
          releaseImage: ibi.example.com:path/to/release/images:version-arch
        ```

        </div>

        - Specify the name for the `ClusterImageSet` resource.

        - Specify the address for the release image to use for the deployment. If you use a different image registry compared to the image registry used during seed image generation, ensure that the OpenShift Container Platform version for the release image remains the same.

    2.  Create the `ClusterImageSet` resource by running the following command:

        ``` terminal
        $ oc apply -f ibi-cluster-image-set.yaml
        ```

6.  Create the `ImageClusterInstall` resource:

    1.  Create a YAML file that defines the `ImageClusterInstall` resource:

        <div class="formalpara">

        <div class="title">

        Example `ibi-image-cluster-install.yaml` file

        </div>

        ``` yaml
        apiVersion: extensions.hive.openshift.io/v1alpha1
        kind: ImageClusterInstall
        metadata:
          name: ibi-image-install
          namespace: ibi-ns
        spec:
          bareMetalHostRef:
            name: ibi-bmh
            namespace: ibi-ns
          clusterDeploymentRef:
            name: ibi-cluster-deployment
          hostname: ibi-host
          imageSetRef:
            name: ibi-img-version-arch
          machineNetworks:
          - cidr: 10.0.0.0/24
          #- cidr: fd01::/64
          proxy:
            httpProxy: "http://proxy.example.com:8080"
            #httpsProxy: "http://proxy.example.com:8080"
            #noProxy: "no_proxy.example.com"
        ```

        </div>

        - Specify the name for the `ImageClusterInstall` resource.

        - Specify the `BareMetalHost` resource that you want to target for the image-based installation.

        - Specify the name of the `ClusterDeployment` resource that you want to use for the image-based installation of the target host.

        - Specify the hostname for the cluster.

        - Specify the name of the `ClusterImageSet` resource you used to define the container release images to use for deployment.

        - Specify the public Classless Inter-Domain Routing (CIDR) of the external network. For dual-stack networking, you can specify both IPv4 and IPv6 CIDRs using a list format. The first CIDR in the list is the primary address family and must match the primary address family of the seed cluster.

        - Optional: Specify a proxy to use for the cluster deployment.

          > [!IMPORTANT]
          > If your cluster deployment requires a proxy configuration, you must do the following:
          >
          > - Create a seed image from a seed cluster featuring a proxy configuration. The proxy configurations do not have to match.
          >
          > - Configure the `machineNetwork` field in your installation manifest.

    2.  Create the `ImageClusterInstall` resource by running the following command:

        ``` terminal
        $ oc create -f ibi-image-cluster-install.yaml
        ```

7.  Create the `ClusterDeployment` resource:

    1.  Create a YAML file that defines the `ClusterDeployment` resource:

        <div class="formalpara">

        <div class="title">

        Example `ibi-cluster-deployment.yaml` file

        </div>

        ``` yaml
        apiVersion: hive.openshift.io/v1
        kind: ClusterDeployment
        metadata:
          name: ibi-cluster-deployment
          namespace: ibi-ns
        spec:
          baseDomain: example.com
          clusterInstallRef:
            group: extensions.hive.openshift.io
            kind: ImageClusterInstall
            name: ibi-image-install
            version: v1alpha1
          clusterName: ibi-cluster
          platform:
            none: {}
          pullSecretRef:
            name: ibi-image-pull-secret
        ```

        </div>

        - Specify the name for the `ClusterDeployment` resource.

        - Specify the namespace for the `ClusterDeployment` resource.

        - Specify the base domain that the cluster should belong to.

        - Specify the name of the `ImageClusterInstall` in which you defined the container images to use for the image-based installation of the target host.

        - Specify a name for the cluster.

        - Specify the secret to use for pulling images from your image registry.

    2.  Create the `ClusterDeployment` resource by running the following command:

        ``` terminal
        $ oc apply -f ibi-cluster-deployment.yaml
        ```

8.  Create the `ManagedCluster` resource:

    1.  Create a YAML file that defines the `ManagedCluster` resource:

        <div class="formalpara">

        <div class="title">

        Example `ibi-managed.yaml` file

        </div>

        ``` yaml
        apiVersion: cluster.open-cluster-management.io/v1
        kind: ManagedCluster
        metadata:
          name: sno-ibi
        spec:
          hubAcceptsClient: true
        ```

        </div>

        - Specify the name for the `ManagedCluster` resource.

        - Specify `true` to enable RHACM to manage the cluster.

    2.  Create the `ManagedCluster` resource by running the following command:

        ``` terminal
        $ oc apply -f ibi-managed.yaml
        ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Check the status of the `ImageClusterInstall` in the hub cluster to monitor the progress of the target host installation by running the following command:

    ``` terminal
    $ oc get imageclusterinstall
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME       REQUIREMENTSMET           COMPLETED                     BAREMETALHOSTREF
    target-0   HostValidationSucceeded   ClusterInstallationSucceeded  ibi-bmh
    ```

    </div>

    > [!WARNING]
    > If the `ImageClusterInstall` resource is deleted, the IBI Operator reattaches the `BareMetalHost` resource and reboots the machine.

2.  When the installation completes, you can retrieve the `kubeconfig` secret to log in to the managed cluster by running the following command:

    ``` terminal
    $ oc extract secret/<cluster_name>-admin-kubeconfig -n <cluster_namespace>  --to - > <directory>/<cluster_name>-kubeconfig
    ```

    - `<cluster_name>` is the name of the cluster.

    - `<cluster_namespace>` is the namespace of the cluster.

    - `<directory>` is the directory in which to create the file.

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [Using image pull secrets](../../../openshift_images/managing_images/using-image-pull-secrets.xml)

- [Cluster configuration resources for deploying a preinstalled host](../../../edge_computing/image_base_install/ibi_deploying_sno_clusters/ibi-edge-image-based-install.xml#ibi-managed-cluster-config-resources_ibi-edge-image-based-install)

</div>

## Cluster configuration resources for deploying a preinstalled host

To complete a deployment for a preinstalled host at a remote site, you must configure the following site-specifc cluster configuration resources in the hub cluster for each bare-metal host.

| Resource | Description |
|----|----|
| `Namespace` | Namespace for the managed single-node OpenShift cluster. |
| `BareMetalHost` | Describes the physical host and its properties, such as the provisioning and hardware configuration. |
| `Secret` for the bare-metal host | Credentials for the host BMC. |
| `Secret` for the bare-metal host static network configuration | Optional: Describes static network configuration for the target host. |
| `Secret` for the image registry | Credentials for the image registry. The secret for the image registry must be of type `kubernetes.io/dockerconfigjson`. |
| `ImageClusterInstall` | References the bare-metal host, deployment, and image set resources. |
| `ClusterImageSet` | Describes the release images to use for the cluster. |
| `ClusterDeployment` | Describes networking, authentication, and platform-specific settings. |
| `ManagedCluster` | Describes cluster details to enable Red Hat Advanced Cluster Management (RHACM) to register and manage. |
| `ConfigMap` | Optional: Describes additional configurations for the cluster deployment, such as adding a bundle of trusted certificates for the host to ensure trusted communications for cluster services. |

Cluster configuration resources reference

## ImageClusterInstall resource API specifications

The following content describes the API specifications for the `ImageClusterInstall` resource. This resource is the endpoint for the Image Based Install Operator.

| Specification | Type | Description |
|----|----|----|
| `imageSetRef` | `string` | Specify the name of the `ClusterImageSet` resource that defines the release images for the deployment. |
| `hostname` | `string` | Specify the hostname for the cluster. |
| `sshKey` | `string` | Specify your SSH key to provide SSH access to the target host. |

Required specifications

<table>
<caption>Optional specifications</caption>
<colgroup>
<col style="width: 28%" />
<col style="width: 14%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Specification</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>clusterDeploymentRef</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specify the name of the <code>ClusterDeployment</code> resource that you want to use for the image-based installation of the target host.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>clusterMetadata</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>After the deployment completes, this specification is automatically populated with metadata information about the cluster, including the <code>cluster-admin</code> kubeconfig credentials for logging in to the cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imageDigestSources</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the sources or repositories for the release-image content, for example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">imageDigestSources</span><span class="kw">:</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="kw">-</span><span class="at"> </span><span class="fu">mirrors</span><span class="kw">:</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="kw">-</span><span class="at"> </span><span class="st">&quot;registry.example.com:5000/ocp4/openshift4&quot;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">source</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;quay.io/openshift-release-dev/ocp-release&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>extraManifestsRefs</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specify a <code>ConfigMap</code> resource containing additional manifests to be applied to the target cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bareMetalHostRef</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specify the <code>bareMetalHost</code> resource to use for the cluster deployment</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>machineNetworks</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specify the public Classless Inter-Domain Routing (CIDR) of the external network. For dual-stack networking, you can specify both IPv4 and IPv6 CIDRs using a list format. The first CIDR in the list is the primary address family and must match the primary address family of the seed cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies proxy settings for the cluster, for example:</p>
<div class="sourceCode" id="cb2"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">proxy</span><span class="kw">:</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">httpProxy</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;http://proxy.example.com:8080&quot;</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">httpsProxy</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;http://proxy.example.com:8080&quot;</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">noProxy</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;no_proxy.example.com&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>caBundleRef</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specify a <code>ConfigMap</code> resource containing the new bundle of trusted certificates for the host.</p></td>
</tr>
</tbody>
</table>

# ConfigMap resources for extra manifests

You can optionally create a `ConfigMap` resource to define additional manifests in an image-based deployment for managed single-node OpenShift clusters.

After you create the `ConfigMap` resource, reference it in the `ImageClusterInstall` resource. During deployment, the IBI Operator includes the extra manifests in the deployment.

## Creating a ConfigMap resource to add extra manifests in an image-based deployment

You can use a `ConfigMap` resource to add extra manifests to the image-based deployment for single-node OpenShift clusters.

The following example adds an single-root I/O virtualization (SR-IOV) network to the deployment.

> [!NOTE]
> Filenames for extra manifests must not exceed 30 characters. Longer filenames might cause deployment failures.

<div>

<div class="title">

Prerequisites

</div>

- You preinstalled a host with single-node OpenShift using an image-based installation.

- You logged in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `SriovNetworkNodePolicy` and `SriovNetwork` resources:

    1.  Create a YAML file that defines the resources:

        <div class="formalpara">

        <div class="title">

        Example `sriov-extra-manifest.yaml` file

        </div>

        ``` yaml
        apiVersion: sriovnetwork.openshift.io/v1
        kind: SriovNetworkNodePolicy
        metadata:
          name: "example-sriov-node-policy"
          namespace: openshift-sriov-network-operator
        spec:
          deviceType: vfio-pci
          isRdma: false
          nicSelector:
            pfNames: [ens1f0]
          nodeSelector:
            node-role.kubernetes.io/master: ""
          mtu: 1500
          numVfs: 8
          priority: 99
          resourceName: example-sriov-node-policy
        ---
        apiVersion: sriovnetwork.openshift.io/v1
        kind: SriovNetwork
        metadata:
          name: "example-sriov-network"
          namespace: openshift-sriov-network-operator
        spec:
          ipam: |-
            {
            }
          linkState: auto
          networkNamespace: sriov-namespace
          resourceName: example-sriov-node-policy
          spoofChk: "on"
          trust: "off"
        ```

        </div>

    2.  Create the `ConfigMap` resource by running the following command:

        ``` terminal
        $ oc create configmap sr-iov-extra-manifest --from-file=sriov-extra-manifest.yaml -n ibi-ns
        ```

        - Specify the namespace that has the `ImageClusterInstall` resource.

          <div class="formalpara">

          <div class="title">

          Example output

          </div>

          ``` terminal
          configmap/sr-iov-extra-manifest created
          ```

          </div>

          > [!NOTE]
          > If you add more than one extra manifest, and the manifests must be applied in a specific order, you must prefix the filenames of the manifests with numbers that represent the required order. For example, `00-namespace.yaml`, `01-sriov-extra-manifest.yaml`, and so on.

2.  Reference the `ConfigMap` resource in the `spec.extraManifestsRefs` field of the `ImageClusterInstall` resource:

    ``` yaml
    #...
      spec:
        extraManifestsRefs:
        - name: sr-iov-extra-manifest
    #...
    ```

</div>

## Creating a ConfigMap resource to add a CA bundle in an image-based deployment

You can use a `ConfigMap` resource to add a certificate authority (CA) bundle to the host to ensure trusted communications for cluster services.

After you create the `ConfigMap` resource, reference it in the `spec.caBundleRef` field of the `ImageClusterInstall` resource.

<div>

<div class="title">

Prerequisites

</div>

- You preinstalled a host with single-node OpenShift using an image-based installation.

- You logged in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a CA bundle file called `tls-ca-bundle.pem`:

    <div class="formalpara">

    <div class="title">

    Example `tls-ca-bundle.pem` file

    </div>

    ``` text
    -----BEGIN CERTIFICATE-----
    MIIDXTCCAkWgAwIBAgIJAKmjYKJbIyz3MA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV
    ...Custom CA certificate bundle...
    4WPl0Qb27Sb1xZyAsy1ww6MYb98EovazUSfjYr2EVF6ThcAPu4/sMxUV7He2J6Jd
    cA8SMRwpUbz3LXY=
    -----END CERTIFICATE-----
    ```

    </div>

2.  Create the `ConfigMap` object by running the following command:

    ``` terminal
    $ oc create configmap custom-ca --from-file=tls-ca-bundle.pem -n ibi-ns
    ```

    - `custom-ca` specifies the name for the `ConfigMap` resource.

    - `tls-ca-bundle.pem` defines the key for the `data` entry in the `ConfigMap` resource. You must include a `data` entry with the `tls-ca-bundle.pem` key.

    - `ibi-ns` specifies the namespace that has the `ImageClusterInstall` resource.

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      configmap/custom-ca created
      ```

      </div>

3.  Reference the `ConfigMap` resource in the `spec.caBundleRef` field of the `ImageClusterInstall` resource:

    ``` yaml
    #...
      spec:
        caBundleRef:
          name: custom-ca
    #...
    ```

</div>

<div role="_additional-resources" role="_additional-resources">

<div class="title">

Additional resources

</div>

- [About the BareMetalHost resource](../../../installing/installing_bare_metal/bare-metal-postinstallation-configuration.xml#bmo-about-the-baremetalhost-resource_bare-metal-postinstallation-configuration)

- [Using image pull secrets](../../../openshift_images/managing_images/using-image-pull-secrets.xml)

- [Reference specifications for the image-based-config.yaml manifest](../../../edge_computing/image_base_install/ibi-factory-image-based-install.xml#ibi-installer-installation-config_ibi-factory-image-based-install)

</div>
