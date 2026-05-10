# kubeadm certs

`kubeadm certs` provides utilities for managing certificates.
For more details on how these commands can be used, see
[Certificate Management with kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/).

## kubeadm certs

A collection of operations for operating Kubernetes certificates.

* overview

### Synopsis

Commands related to handling Kubernetes certificates

```
kubeadm certs [flags]
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

## kubeadm certs renew

You can renew all Kubernetes certificates using the `all` subcommand or renew them selectively.
For more details see [Manual certificate renewal](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#manual-certificate-renewal).

* renew
  * all
    * admin.conf
      * apiserver-etcd-client
        * apiserver-kubelet-client
          * apiserver
            * controller-manager.conf
              * etcd-healthcheck-client
                * etcd-peer
                  * etcd-server
                    * front-proxy-client
                      * scheduler.conf
                        * super-admin.conf

### Synopsis

Renew certificates for a Kubernetes cluster

```
kubeadm certs renew [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for renew |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

Renew all available certificates

### Synopsis

Renew all known certificates necessary to run the control plane. Renewals are run unconditionally, regardless of expiration date. Renewals can also be run individually for more control.

```
kubeadm certs renew all [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save the certificates |
| --config string | |
|  | Path to a kubeadm configuration file. |
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

Renew the certificate embedded in the kubeconfig file for the admin to use and for kubeadm itself.

Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them.

Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request.

After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere.

```
kubeadm certs renew admin.conf [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save the certificates |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for admin.conf |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Renew the certificate the apiserver uses to access etcd.

Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them.

Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request.

After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere.

```
kubeadm certs renew apiserver-etcd-client [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save the certificates |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for apiserver-etcd-client |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Renew the certificate for the API server to connect to kubelet.

Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them.

Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request.

After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere.

```
kubeadm certs renew apiserver-kubelet-client [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save the certificates |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for apiserver-kubelet-client |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Renew the certificate for serving the Kubernetes API.

Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them.

Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request.

After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere.

```
kubeadm certs renew apiserver [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save the certificates |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for apiserver |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Renew the certificate embedded in the kubeconfig file for the controller manager to use.

Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them.

Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request.

After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere.

```
kubeadm certs renew controller-manager.conf [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save the certificates |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for controller-manager.conf |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Renew the certificate for liveness probes to healthcheck etcd.

Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them.

Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request.

After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere.

```
kubeadm certs renew etcd-healthcheck-client [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save the certificates |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for etcd-healthcheck-client |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Renew the certificate for etcd nodes to communicate with each other.

Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them.

Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request.

After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere.

```
kubeadm certs renew etcd-peer [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save the certificates |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for etcd-peer |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Renew the certificate for serving etcd.

Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them.

Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request.

After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere.

```
kubeadm certs renew etcd-server [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save the certificates |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for etcd-server |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Renew the certificate for the front proxy client.

Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them.

Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request.

After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere.

```
kubeadm certs renew front-proxy-client [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save the certificates |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for front-proxy-client |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Renew the certificate embedded in the kubeconfig file for the scheduler manager to use.

Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them.

Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request.

After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere.

```
kubeadm certs renew scheduler.conf [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save the certificates |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for scheduler.conf |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

### Synopsis

Renew the certificate embedded in the kubeconfig file for the super-admin.

Renewals run unconditionally, regardless of certificate expiration date; extra attributes such as SANs will be based on the existing file/certificates, there is no need to resupply them.

Renewal by default tries to use the certificate authority in the local PKI managed by kubeadm; as alternative it is possible to use K8s certificate API for certificate renewal, or as a last option, to generate a CSR request.

After renewal, in order to make changes effective, is required to restart control-plane components and eventually re-distribute the renewed certificate in case the file is used elsewhere.

```
kubeadm certs renew super-admin.conf [flags]
```

### Options

|  |  |
| --- | --- |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save the certificates |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for super-admin.conf |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm certs certificate-key

This command can be used to generate a new control-plane certificate key.
The key can be passed as `--certificate-key` to [`kubeadm init`](/docs/reference/setup-tools/kubeadm/kubeadm-init/)
and [`kubeadm join`](/docs/reference/setup-tools/kubeadm/kubeadm-join/)
to enable the automatic copy of certificates when joining additional control-plane nodes.

* certificate-key

Generate certificate keys

### Synopsis

This command will print out a secure randomly-generated certificate key that can be used with
the "init" command.

You can also use "kubeadm init --upload-certs" without specifying a certificate key and it will
generate and print one for you.

```
kubeadm certs certificate-key [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for certificate-key |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm certs check-expiration

This command checks expiration for the certificates in the local PKI managed by kubeadm.
For more details see
[Check certificate expiration](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#check-certificate-expiration).

* check-expiration

Check certificates expiration for a Kubernetes cluster

### Synopsis

Checks expiration for the certificates in the local PKI managed by kubeadm.

```
kubeadm certs check-expiration [flags]
```

### Options

|  |  |
| --- | --- |
| --allow-missing-template-keys     Default: true | |
|  | If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats. |
| --cert-dir string     Default: "/etc/kubernetes/pki" | |
|  | The path where to save the certificates |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for check-expiration |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| -o, --output string     Default: "text" | |
|  | Output format. One of: text|json|yaml|go-template|go-template-file|template|templatefile|jsonpath|jsonpath-as-json|jsonpath-file. |
| --show-managed-fields | |
|  | If true, keep the managedFields when printing objects in JSON or YAML format. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm certs generate-csr

This command can be used to generate keys and CSRs for all control-plane certificates and kubeconfig files.
The user can then sign the CSRs with a CA of their choice. To read more information
on how to use the command see
[Signing certificate signing requests (CSR) generated by kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#signing-csr).

* generate-csr

Generate keys and certificate signing requests

### Synopsis

Generates keys and certificate signing requests (CSRs) for all the certificates required to run the control plane. This command also generates partial kubeconfig files with private key data in the "users > user > client-key-data" field, and for each kubeconfig file an accompanying ".csr" file is created.

This command is designed for use in [Kubeadm External CA Mode](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#external-ca-mode). It generates CSRs which you can then submit to your external certificate authority for signing.

The PEM encoded signed certificates should then be saved alongside the key files, using ".crt" as the file extension, or in the case of kubeconfig files, the PEM encoded signed certificate should be base64 encoded and added to the kubeconfig file in the "users > user > client-certificate-data" field.

```
kubeadm certs generate-csr [flags]
```

### Examples

```
  # The following command will generate keys and CSRs for all control-plane certificates and kubeconfig files:
  kubeadm certs generate-csr --kubeconfig-dir /tmp/etc-k8s --cert-dir /tmp/etc-k8s/pki
```

### Options

|  |  |
| --- | --- |
| --cert-dir string | |
|  | The path where to save the certificates |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for generate-csr |
| --kubeconfig-dir string     Default: "/etc/kubernetes" | |
|  | The path where to save the kubeconfig file. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## What's next

* [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) to bootstrap a Kubernetes control-plane node
* [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) to connect a node to the cluster
* [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) to revert any changes made to this host by `kubeadm init` or `kubeadm join`

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
