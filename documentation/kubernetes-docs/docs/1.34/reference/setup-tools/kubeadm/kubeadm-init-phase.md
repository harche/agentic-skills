# kubeadm init phase

`kubeadm init phase` enables you to invoke atomic steps of the bootstrap process.
Hence, you can let kubeadm do some of the work and you can fill in the gaps
if you wish to apply customization.

`kubeadm init phase` is consistent with the [kubeadm init workflow](/docs/reference/setup-tools/kubeadm/kubeadm-init/#init-workflow),
and behind the scene both use the same code.

## kubeadm init phase preflight

Using this command you can execute preflight checks on a control-plane node.

* preflight

### Synopsis

Run pre-flight checks for kubeadm init.

```
kubeadm init phase preflight [flags]
```

### Examples

```
  # Run pre-flight checks for kubeadm init using a config file.
  kubeadm init phase preflight --config kubeadm-config.yaml
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --cri-socket string | |
|  | Path to the CRI socket to connect. If empty kubeadm will try to auto-detect this value; use this option only if you have more than one CRI installed or if you have non-standard CRI socket. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for preflight |
| --ignore-preflight-errors strings | |
|  | A list of checks whose errors will be shown as warnings. Example: 'IsPrivilegedUser,Swap'. Value 'all' ignores errors from all checks. |
| --image-repository string     Default: "registry.k8s.io" | |
|  | Choose a container registry to pull control plane images from |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm init phase kubelet-start

This phase will write the kubelet configuration file and environment file and then start the kubelet.

* kubelet-start

Write kubelet settings and (re)start the kubelet

### Synopsis

Write a file with KubeletConfiguration and an environment file with node specific kubelet settings, and then (re)start kubelet.

```
kubeadm init phase kubelet-start [flags]
```

### Examples

```
  # Writes a dynamic environment file with kubelet flags from a InitConfiguration file.
  kubeadm init phase kubelet-start --config config.yaml
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --cri-socket string | |
|  | Path to the CRI socket to connect. If empty kubeadm will try to auto-detect this value; use this option only if you have more than one CRI installed or if you have non-standard CRI socket. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for kubelet-start |
| --image-repository string     Default: "registry.k8s.io" | |
|  | Choose a container registry to pull control plane images from |
| --node-name string | |
|  | Specify the node name. |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm init phase certs

Can be used to create all required certificates by kubeadm.

* certs
  * all
    * ca
      * apiserver
        * apiserver-kubelet-client
          * front-proxy-ca
            * front-proxy-client
              * etcd-ca
                * etcd-server
                  * etcd-peer
                    * healthcheck-client
                      * apiserver-etcd-client
                        * sa

### Synopsis

Certificate generation

```
kubeadm init phase certs [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for certs |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate all certificates

```
kubeadm init phase certs all [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | The IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-cert-extra-sans strings | |
|  | Optional extra Subject Alternative Names (SANs) to use for the API Server serving certificate. Can be both IP addresses and DNS names. |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane-endpoint string | |
|  | Specify a stable IP address or DNS name for the control plane. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for all |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |
| --service-cidr string     Default: "10.96.0.0/12" | |
|  | Use alternative range of IP address for service VIPs. |
| --service-dns-domain string     Default: "cluster.local" | |
|  | Use alternative domain for services, e.g. "myorg.internal". |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate the self-signed Kubernetes CA to provision identities for other Kubernetes components, and save them into ca.crt and ca.key files.

If both files already exist, kubeadm skips the generation step and existing files will be used.

```
kubeadm init phase certs ca [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for ca |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate the certificate for serving the Kubernetes API, and save them into apiserver.crt and apiserver.key files.

If both files already exist, kubeadm skips the generation step and existing files will be used.

```
kubeadm init phase certs apiserver [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | The IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-cert-extra-sans strings | |
|  | Optional extra Subject Alternative Names (SANs) to use for the API Server serving certificate. Can be both IP addresses and DNS names. |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane-endpoint string | |
|  | Specify a stable IP address or DNS name for the control plane. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for apiserver |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |
| --service-cidr string     Default: "10.96.0.0/12" | |
|  | Use alternative range of IP address for service VIPs. |
| --service-dns-domain string     Default: "cluster.local" | |
|  | Use alternative domain for services, e.g. "myorg.internal". |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate the certificate for the API server to connect to kubelet, and save them into apiserver-kubelet-client.crt and apiserver-kubelet-client.key files.

If both files already exist, kubeadm skips the generation step and existing files will be used.

```
kubeadm init phase certs apiserver-kubelet-client [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for apiserver-kubelet-client |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate the self-signed CA to provision identities for front proxy, and save them into front-proxy-ca.crt and front-proxy-ca.key files.

If both files already exist, kubeadm skips the generation step and existing files will be used.

```
kubeadm init phase certs front-proxy-ca [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for front-proxy-ca |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate the certificate for the front proxy client, and save them into front-proxy-client.crt and front-proxy-client.key files.

If both files already exist, kubeadm skips the generation step and existing files will be used.

```
kubeadm init phase certs front-proxy-client [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for front-proxy-client |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate the self-signed CA to provision identities for etcd, and save them into etcd/ca.crt and etcd/ca.key files.

If both files already exist, kubeadm skips the generation step and existing files will be used.

```
kubeadm init phase certs etcd-ca [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for etcd-ca |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate the certificate for serving etcd, and save them into etcd/server.crt and etcd/server.key files.

Default SANs are localhost, 127.0.0.1, 127.0.0.1, ::1

If both files already exist, kubeadm skips the generation step and existing files will be used.

```
kubeadm init phase certs etcd-server [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for etcd-server |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate the certificate for etcd nodes to communicate with each other, and save them into etcd/peer.crt and etcd/peer.key files.

Default SANs are localhost, 127.0.0.1, 127.0.0.1, ::1

If both files already exist, kubeadm skips the generation step and existing files will be used.

```
kubeadm init phase certs etcd-peer [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for etcd-peer |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate the certificate for liveness probes to healthcheck etcd, and save them into etcd/healthcheck-client.crt and etcd/healthcheck-client.key files.

If both files already exist, kubeadm skips the generation step and existing files will be used.

```
kubeadm init phase certs etcd-healthcheck-client [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for etcd-healthcheck-client |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate the certificate the apiserver uses to access etcd, and save them into apiserver-etcd-client.crt and apiserver-etcd-client.key files.

If both files already exist, kubeadm skips the generation step and existing files will be used.

```
kubeadm init phase certs apiserver-etcd-client [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for apiserver-etcd-client |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

Generate a private key for signing service account tokens along with its public key

### Synopsis

Generate the private key for signing service account tokens along with its public key, and save them into sa.key and sa.pub files.

If both files already exist, kubeadm skips the generation step and existing files will be used.

```
kubeadm init phase certs sa [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for sa |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm init phase kubeconfig

You can create all required kubeconfig files by calling the `all` subcommand or call them individually.

* kubeconfig
  * all
    * admin
      * kubelet
        * controller-manager
          * scheduler
            * super-admin

### Synopsis

Generate all kubeconfig files necessary to establish the control plane and the admin kubeconfig file

```
kubeadm init phase kubeconfig [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for kubeconfig |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate all kubeconfig files

```
kubeadm init phase kubeconfig all [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | The IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-bind-port int32     Default: 6443 | |
|  | Port for the API Server to bind to. |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane-endpoint string | |
|  | Specify a stable IP address or DNS name for the control plane. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for all |
| --kubeconfig-dir string     Default: "/etc/kubernetes" | |
|  | The path where to save the kubeconfig file. |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |
| --node-name string | |
|  | Specify the node name. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

Generate a kubeconfig file for the admin to use and for kubeadm itself

### Synopsis

Generate the kubeconfig file for the admin and for kubeadm itself, and save it to admin.conf file.

```
kubeadm init phase kubeconfig admin [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | The IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-bind-port int32     Default: 6443 | |
|  | Port for the API Server to bind to. |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane-endpoint string | |
|  | Specify a stable IP address or DNS name for the control plane. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for admin |
| --kubeconfig-dir string     Default: "/etc/kubernetes" | |
|  | The path where to save the kubeconfig file. |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

Generate a kubeconfig file for the kubelet to use *only* for cluster bootstrapping purposes

### Synopsis

Generate the kubeconfig file for the kubelet to use and save it to kubelet.conf file.

Please note that this should *only* be used for cluster bootstrapping purposes. After your control plane is up, you should request all kubelet credentials from the CSR API.

```
kubeadm init phase kubeconfig kubelet [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | The IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-bind-port int32     Default: 6443 | |
|  | Port for the API Server to bind to. |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane-endpoint string | |
|  | Specify a stable IP address or DNS name for the control plane. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for kubelet |
| --kubeconfig-dir string     Default: "/etc/kubernetes" | |
|  | The path where to save the kubeconfig file. |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |
| --node-name string | |
|  | Specify the node name. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

Generate a kubeconfig file for the controller manager to use

### Synopsis

Generate the kubeconfig file for the controller manager to use and save it to controller-manager.conf file

```
kubeadm init phase kubeconfig controller-manager [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | The IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-bind-port int32     Default: 6443 | |
|  | Port for the API Server to bind to. |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane-endpoint string | |
|  | Specify a stable IP address or DNS name for the control plane. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for controller-manager |
| --kubeconfig-dir string     Default: "/etc/kubernetes" | |
|  | The path where to save the kubeconfig file. |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

Generate a kubeconfig file for the scheduler to use

### Synopsis

Generate the kubeconfig file for the scheduler to use and save it to scheduler.conf file.

```
kubeadm init phase kubeconfig scheduler [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | The IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-bind-port int32     Default: 6443 | |
|  | Port for the API Server to bind to. |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane-endpoint string | |
|  | Specify a stable IP address or DNS name for the control plane. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for scheduler |
| --kubeconfig-dir string     Default: "/etc/kubernetes" | |
|  | The path where to save the kubeconfig file. |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate a kubeconfig file for the super-admin, and save it to super-admin.conf file.

```
kubeadm init phase kubeconfig super-admin [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | The IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-bind-port int32     Default: 6443 | |
|  | Port for the API Server to bind to. |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane-endpoint string | |
|  | Specify a stable IP address or DNS name for the control plane. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for super-admin |
| --kubeconfig-dir string     Default: "/etc/kubernetes" | |
|  | The path where to save the kubeconfig file. |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm init phase control-plane

Using this phase you can create all required static Pod files for the control plane components.

* control-plane
  * all
    * apiserver
      * controller-manager
        * scheduler

### Synopsis

Generate all static Pod manifest files necessary to establish the control plane

```
kubeadm init phase control-plane [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for control-plane |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate all static Pod manifest files

```
kubeadm init phase control-plane all [flags]
```

### Examples

```
  # Generates all static Pod manifest files for control plane components,
  # functionally equivalent to what is generated by kubeadm init.
  kubeadm init phase control-plane all

  # Generates all static Pod manifest files using options read from a configuration file.
  kubeadm init phase control-plane all --config config.yaml
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | The IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-bind-port int32     Default: 6443 | |
|  | Port for the API Server to bind to. |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane-endpoint string | |
|  | Specify a stable IP address or DNS name for the control plane. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| --feature-gates string | |
|  | A set of key=value pairs that describe feature gates for various features. Options are: ControlPlaneKubeletLocalMode=true|false (BETA - default=true) NodeLocalCRISocket=true|false (BETA - default=true) PublicKeysECDSA=true|false (DEPRECATED - default=false) RootlessControlPlane=true|false (ALPHA - default=false) WaitForAllControlPlaneComponents=true|false (default=true) |
| -h, --help | |
|  | help for all |
| --image-repository string     Default: "registry.k8s.io" | |
|  | Choose a container registry to pull control plane images from |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |
| --pod-network-cidr string | |
|  | Specify range of IP addresses for the pod network. If set, the control plane will automatically allocate CIDRs for every node. |
| --service-cidr string     Default: "10.96.0.0/12" | |
|  | Use alternative range of IP address for service VIPs. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generates the kube-apiserver static Pod manifest

```
kubeadm init phase control-plane apiserver [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | The IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-bind-port int32     Default: 6443 | |
|  | Port for the API Server to bind to. |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane-endpoint string | |
|  | Specify a stable IP address or DNS name for the control plane. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| --feature-gates string | |
|  | A set of key=value pairs that describe feature gates for various features. Options are: ControlPlaneKubeletLocalMode=true|false (BETA - default=true) NodeLocalCRISocket=true|false (BETA - default=true) PublicKeysECDSA=true|false (DEPRECATED - default=false) RootlessControlPlane=true|false (ALPHA - default=false) WaitForAllControlPlaneComponents=true|false (default=true) |
| -h, --help | |
|  | help for apiserver |
| --image-repository string     Default: "registry.k8s.io" | |
|  | Choose a container registry to pull control plane images from |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |
| --service-cidr string     Default: "10.96.0.0/12" | |
|  | Use alternative range of IP address for service VIPs. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generates the kube-controller-manager static Pod manifest

```
kubeadm init phase control-plane controller-manager [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for controller-manager |
| --image-repository string     Default: "registry.k8s.io" | |
|  | Choose a container registry to pull control plane images from |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |
| --pod-network-cidr string | |
|  | Specify range of IP addresses for the pod network. If set, the control plane will automatically allocate CIDRs for every node. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generates the kube-scheduler static Pod manifest

```
kubeadm init phase control-plane scheduler [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for scheduler |
| --image-repository string     Default: "registry.k8s.io" | |
|  | Choose a container registry to pull control plane images from |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm init phase etcd

Use the following phase to create a local etcd instance based on a static Pod file.

* etcd
  * local

### Synopsis

Generate static Pod manifest file for local etcd

```
kubeadm init phase etcd [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for etcd |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Generate the static Pod manifest file for a local, single-node local etcd instance

```
kubeadm init phase etcd local [flags]
```

### Examples

```
  # Generates the static Pod manifest file for etcd, functionally
  # equivalent to what is generated by kubeadm init.
  kubeadm init phase etcd local

  # Generates the static Pod manifest file for etcd using options
  # read from a configuration file.
  kubeadm init phase etcd local --config config.yaml
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for local |
| --image-repository string     Default: "registry.k8s.io" | |
|  | Choose a container registry to pull control plane images from |
| --patches string | |
|  | Path to a directory that contains files named "target[suffix][+patchtype].extension". For example, "kube-apiserver0+merge.yaml" or just "etcd.json". "target" can be one of "kube-apiserver", "kube-controller-manager", "kube-scheduler", "etcd", "kubeletconfiguration", "corednsdeployment". "patchtype" can be one of "strategic", "merge" or "json" and they match the patch formats supported by kubectl. The default "patchtype" is "strategic". "extension" must be either "json" or "yaml". "suffix" is an optional string that can be used to determine which patches are applied first alpha-numerically. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm init phase upload-config

You can use this command to upload the kubeadm configuration to your cluster.
Alternatively, you can use [kubeadm config](/docs/reference/setup-tools/kubeadm/kubeadm-config/).

* upload-config
  * all
    * kubeadm
      * kubelet

### Synopsis

Upload the kubeadm and kubelet configuration to a ConfigMap

```
kubeadm init phase upload-config [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for upload-config |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Upload all configuration to a config map

```
kubeadm init phase upload-config all [flags]
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --cri-socket string | |
|  | Path to the CRI socket to connect. If empty kubeadm will try to auto-detect this value; use this option only if you have more than one CRI installed or if you have non-standard CRI socket. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for all |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Upload the kubeadm ClusterConfiguration to a ConfigMap called kubeadm-config in the kube-system namespace. This enables correct configuration of system components and a seamless user experience when upgrading.

Alternatively, you can use kubeadm config.

```
kubeadm init phase upload-config kubeadm [flags]
```

### Examples

```
  # upload the configuration of your cluster
  kubeadm init phase upload-config kubeadm --config=myConfig.yaml
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --cri-socket string | |
|  | Path to the CRI socket to connect. If empty kubeadm will try to auto-detect this value; use this option only if you have more than one CRI installed or if you have non-standard CRI socket. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for kubeadm |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

Upload the kubelet component config to a ConfigMap

### Synopsis

Upload the kubelet configuration extracted from the kubeadm InitConfiguration object to a kubelet-config ConfigMap in the cluster

```
kubeadm init phase upload-config kubelet [flags]
```

### Examples

```
  # Upload the kubelet configuration from the kubeadm Config file to a ConfigMap in the cluster.
  kubeadm init phase upload-config kubelet --config kubeadm.yaml
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --cri-socket string | |
|  | Path to the CRI socket to connect. If empty kubeadm will try to auto-detect this value; use this option only if you have more than one CRI installed or if you have non-standard CRI socket. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for kubelet |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm init phase upload-certs

Use the following phase to upload control-plane certificates to the cluster.
By default the certs and encryption key expire after two hours.

* upload-certs

Upload certificates to kubeadm-certs

### Synopsis

Upload control plane certificates to the kubeadm-certs Secret

```
kubeadm init phase upload-certs [flags]
```

### Options

|  |  |
| --- | --- |
| --certificate-key string | |
|  | Key used to encrypt the control-plane certificates in the kubeadm-certs Secret. The certificate key is a hex encoded string that is an AES key of size 32 bytes. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for upload-certs |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --skip-certificate-key-print | |
|  | Don't print the key used to encrypt the control-plane certificates. |
| --upload-certs | |
|  | Upload control-plane certificates to the kubeadm-certs Secret. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm init phase mark-control-plane

Use the following phase to label and taint the node as a control plane node.

* mark-control-plane

### Synopsis

Mark a node as a control-plane

```
kubeadm init phase mark-control-plane [flags]
```

### Examples

```
  # Applies control-plane label and taint to the current node, functionally equivalent to what executed by kubeadm init.
  kubeadm init phase mark-control-plane --config config.yaml

  # Applies control-plane label and taint to a specific node
  kubeadm init phase mark-control-plane --node-name myNode
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for mark-control-plane |
| --node-name string | |
|  | Specify the node name. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm init phase bootstrap-token

Use the following phase to configure bootstrap tokens.

* bootstrap-token

Generates bootstrap tokens used to join a node to a cluster

### Synopsis

Bootstrap tokens are used for establishing bidirectional trust between a node joining the cluster and a control-plane node.

This command makes all the configurations required to make bootstrap tokens works and then creates an initial token.

```
kubeadm init phase bootstrap-token [flags]
```

### Examples

```
  # Make all the bootstrap token configurations and create an initial token, functionally
  # equivalent to what generated by kubeadm init.
  kubeadm init phase bootstrap-token
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for bootstrap-token |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --skip-token-print | |
|  | Skip printing of the default bootstrap token generated by 'kubeadm init'. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm init phase kubelet-finalize

Use the following phase to update settings relevant to the kubelet after TLS
bootstrap. You can use the `all` subcommand to run all `kubelet-finalize`
phases.

* kubelet-finalize
  * kubelet-finalize-all
    * kubelet-finalize-enable-client-cert-rotation

### Synopsis

Updates settings relevant to the kubelet after TLS bootstrap

```
kubeadm init phase kubelet-finalize [flags]
```

### Examples

```
  # Updates settings relevant to the kubelet after TLS bootstrap"
  kubeadm init phase kubelet-finalize all --config
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for kubelet-finalize |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Run all kubelet-finalize phases

```
kubeadm init phase kubelet-finalize all [flags]
```

### Examples

```
  # Updates settings relevant to the kubelet after TLS bootstrap"
  kubeadm init phase kubelet-finalize all --config
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for all |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Enable kubelet client certificate rotation

```
kubeadm init phase kubelet-finalize enable-client-cert-rotation [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save and store the certificates. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for enable-client-cert-rotation |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm init phase addon

You can install all the available addons with the `all` subcommand, or
install them selectively.

* addon
  * all
    * coredns
      * kube-proxy

### Synopsis

Install required addons for passing conformance tests

```
kubeadm init phase addon [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for addon |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Install all the addons

```
kubeadm init phase addon all [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | The IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-bind-port int32     Default: 6443 | |
|  | Port for the API Server to bind to. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane-endpoint string | |
|  | Specify a stable IP address or DNS name for the control plane. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| --feature-gates string | |
|  | A set of key=value pairs that describe feature gates for various features. Options are: ControlPlaneKubeletLocalMode=true|false (BETA - default=true) NodeLocalCRISocket=true|false (BETA - default=true) PublicKeysECDSA=true|false (DEPRECATED - default=false) RootlessControlPlane=true|false (ALPHA - default=false) WaitForAllControlPlaneComponents=true|false (default=true) |
| -h, --help | |
|  | help for all |
| --image-repository string     Default: "registry.k8s.io" | |
|  | Choose a container registry to pull control plane images from |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |
| --pod-network-cidr string | |
|  | Specify range of IP addresses for the pod network. If set, the control plane will automatically allocate CIDRs for every node. |
| --service-cidr string     Default: "10.96.0.0/12" | |
|  | Use alternative range of IP address for service VIPs. |
| --service-dns-domain string     Default: "cluster.local" | |
|  | Use alternative domain for services, e.g. "myorg.internal". |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

Install the CoreDNS addon to a Kubernetes cluster

### Synopsis

Install the CoreDNS addon components via the API server. Please note that although the DNS server is deployed, it will not be scheduled until CNI is installed.

```
kubeadm init phase addon coredns [flags]
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| --feature-gates string | |
|  | A set of key=value pairs that describe feature gates for various features. Options are: ControlPlaneKubeletLocalMode=true|false (BETA - default=true) NodeLocalCRISocket=true|false (BETA - default=true) PublicKeysECDSA=true|false (DEPRECATED - default=false) RootlessControlPlane=true|false (ALPHA - default=false) WaitForAllControlPlaneComponents=true|false (default=true) |
| -h, --help | |
|  | help for coredns |
| --image-repository string     Default: "registry.k8s.io" | |
|  | Choose a container registry to pull control plane images from |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |
| --print-manifest | |
|  | Print the addon manifests to STDOUT instead of installing them |
| --service-cidr string     Default: "10.96.0.0/12" | |
|  | Use alternative range of IP address for service VIPs. |
| --service-dns-domain string     Default: "cluster.local" | |
|  | Use alternative domain for services, e.g. "myorg.internal". |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

Install the kube-proxy addon to a Kubernetes cluster

### Synopsis

Install the kube-proxy addon components via the API server.

```
kubeadm init phase addon kube-proxy [flags]
```

### Options

|  |  |
| --- | --- |
| --apiserver-advertise-address string | |
|  | The IP address the API Server will advertise it's listening on. If not set the default network interface will be used. |
| --apiserver-bind-port int32     Default: 6443 | |
|  | Port for the API Server to bind to. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --control-plane-endpoint string | |
|  | Specify a stable IP address or DNS name for the control plane. |
| --dry-run | |
|  | Don't apply any changes; just output what would be done. |
| -h, --help | |
|  | help for kube-proxy |
| --image-repository string     Default: "registry.k8s.io" | |
|  | Choose a container registry to pull control plane images from |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |
| --pod-network-cidr string | |
|  | Specify range of IP addresses for the pod network. If set, the control plane will automatically allocate CIDRs for every node. |
| --print-manifest | |
|  | Print the addon manifests to STDOUT instead of installing them |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

For more details on each field in the `v1beta4` configuration you can navigate to our
[API reference pages.](/docs/reference/config-api/kubeadm-config.v1beta4/)

## What's next

* [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) to bootstrap a Kubernetes control-plane node
* [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) to connect a node to the cluster
* [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) to revert any changes made to this host by `kubeadm init` or `kubeadm join`
* [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha/) to try experimental functionality

## Feedback

Was this page helpful?

Yes
No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on
[Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes).
Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to
[report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io)
or
[suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

const yes = document.querySelector('.feedback--yes');
const no = document.querySelector('.feedback--no');
document.querySelectorAll('.feedback--link').forEach(link => {
link.href = link.href + window.location.pathname;
});
const sendFeedback = (value) => {
if (!gtag) { console.log('!gtag'); }
gtag('event', 'click', {
'event_category': 'Helpful',
'event_label': window.location.pathname,
value
});
};
const disableButtons = () => {
yes.disabled = true;
yes.classList.add('feedback--button__disabled');
no.disabled = true;
no.classList.add('feedback--button__disabled');
};
yes.addEventListener('click', () => {
sendFeedback(1);
disableButtons();
document.querySelector('.feedback--response').classList.remove('feedback--response__hidden');
});
no.addEventListener('click', () => {
sendFeedback(0);
disableButtons();
document.querySelector('.feedback--response').classList.remove('feedback--response__hidden');
});

Last modified April 23, 2026 at 2:12 AM PST: [Merge pull request #55450 from sayanchowdhury/update-release-1.34-hugo.toml (d1f313a)](https://github.com/kubernetes/website/commit/d1f313a65f45bd4882d05fe9b6bea162fa2fdc16)
