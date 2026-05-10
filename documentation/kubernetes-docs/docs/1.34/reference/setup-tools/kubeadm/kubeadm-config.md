# kubeadm config

During `kubeadm init`, kubeadm uploads the `ClusterConfiguration` object to your cluster
in a ConfigMap called `kubeadm-config` in the `kube-system` namespace. This configuration is then read during
`kubeadm join`, `kubeadm reset` and `kubeadm upgrade`.

You can use `kubeadm config print` to print the default static configuration that kubeadm
uses for `kubeadm init` and `kubeadm join`.

> **Note:**
> The output of the command is meant to serve as an example. You must manually edit the output
> of this command to adapt to your setup. Remove the fields that you are not certain about and kubeadm
> will try to default them on runtime by examining the host.

For more information on `init` and `join` navigate to
[Using kubeadm init with a configuration file](/docs/reference/setup-tools/kubeadm/kubeadm-init/#config-file)
or [Using kubeadm join with a configuration file](/docs/reference/setup-tools/kubeadm/kubeadm-join/#config-file).

For more information on using the kubeadm configuration API navigate to
[Customizing components with the kubeadm API](/docs/setup/production-environment/tools/kubeadm/control-plane-flags/).

You can use `kubeadm config migrate` to convert your old configuration files that contain a deprecated
API version to a newer, supported API version.

`kubeadm config validate` can be used for validating a configuration file.

`kubeadm config images list` and `kubeadm config images pull` can be used to list and pull the images
that kubeadm requires.

## kubeadm config print

Print configuration

### Synopsis

This command prints configurations for subcommands provided.
For details, see: <https://pkg.go.dev/k8s.io/kubernetes/cmd/kubeadm/app/apis/kubeadm#section-directories>

```
kubeadm config print [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for print |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm config print init-defaults

Print default init configuration, that can be used for 'kubeadm init'

### Synopsis

This command prints objects such as the default init configuration that is used for 'kubeadm init'.

Note that sensitive values like the Bootstrap Token fields are replaced with placeholder values like "abcdef.0123456789abcdef" in order to pass validation but
not perform the real computation for creating a token.

```
kubeadm config print init-defaults [flags]
```

### Options

|  |  |
| --- | --- |
| --component-configs strings | |
|  | A comma-separated list for component config API objects to print the default values for. Available values: [KubeProxyConfiguration KubeletConfiguration]. If this flag is not set, no component configs will be printed. |
| -h, --help | |
|  | help for init-defaults |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm config print join-defaults

Print default join configuration, that can be used for 'kubeadm join'

### Synopsis

This command prints objects such as the default join configuration that is used for 'kubeadm join'.

Note that sensitive values like the Bootstrap Token fields are replaced with placeholder values like "abcdef.0123456789abcdef" in order to pass validation but
not perform the real computation for creating a token.

```
kubeadm config print join-defaults [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for join-defaults |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm config migrate

Read an older version of the kubeadm configuration API types from a file, and output the similar config object for the newer version

### Synopsis

This command lets you convert configuration objects of older versions to the latest supported version,
locally in the CLI tool without ever touching anything in the cluster.
In this version of kubeadm, the following API versions are supported:

* kubeadm.k8s.io/v1beta4

Further, kubeadm can only write out config of version "kubeadm.k8s.io/v1beta4", but read both types.
So regardless of what version you pass to the --old-config parameter here, the API object will be
read, deserialized, defaulted, converted, validated, and re-serialized when written to stdout or
--new-config if specified.

In other words, the output of this command is what kubeadm actually would read internally if you
submitted this file to "kubeadm init"

```
kubeadm config migrate [flags]
```

### Options

|  |  |
| --- | --- |
| --allow-experimental-api | |
|  | Allow migration to experimental, unreleased APIs. |
| -h, --help | |
|  | help for migrate |
| --new-config string | |
|  | Path to the resulting equivalent kubeadm config file using the new API version. Optional, if not specified output will be sent to STDOUT. |
| --old-config string | |
|  | Path to the kubeadm config file that is using an old API version and should be converted. This flag is mandatory. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm config validate

Read a file containing the kubeadm configuration API and report any validation problems

### Synopsis

This command lets you validate a kubeadm configuration API file and report any warnings and errors.
If there are no errors the exit status will be zero, otherwise it will be non-zero.
Any unmarshaling problems such as unknown API fields will trigger errors. Unknown API versions and
fields with invalid values will also trigger errors. Any other errors or warnings may be reported
depending on contents of the input file.

In this version of kubeadm, the following API versions are supported:

* kubeadm.k8s.io/v1beta4

```
kubeadm config validate [flags]
```

### Options

|  |  |
| --- | --- |
| --allow-experimental-api | |
|  | Allow validation of experimental, unreleased APIs. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for validate |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm config images list

### Synopsis

Print a list of images kubeadm will use. The configuration file is used in case any images or image repositories are customized

```
kubeadm config images list [flags]
```

### Options

|  |  |
| --- | --- |
| --allow-missing-template-keys     Default: true | |
|  | If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --feature-gates string | |
|  | A set of key=value pairs that describe feature gates for various features. Options are: ControlPlaneKubeletLocalMode=true|false (BETA - default=true) NodeLocalCRISocket=true|false (BETA - default=true) PublicKeysECDSA=true|false (DEPRECATED - default=false) RootlessControlPlane=true|false (ALPHA - default=false) WaitForAllControlPlaneComponents=true|false (default=true) |
| -h, --help | |
|  | help for list |
| --image-repository string     Default: "registry.k8s.io" | |
|  | Choose a container registry to pull control plane images from |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |
| -o, --output string     Default: "text" | |
|  | Output format. One of: text|json|yaml|go-template|go-template-file|template|templatefile|jsonpath|jsonpath-as-json|jsonpath-file. |
| --show-managed-fields | |
|  | If true, keep the managedFields when printing objects in JSON or YAML format. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm config images pull

### Synopsis

Pull images used by kubeadm

```
kubeadm config images pull [flags]
```

### Options

|  |  |
| --- | --- |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --cri-socket string | |
|  | Path to the CRI socket to connect. If empty kubeadm will try to auto-detect this value; use this option only if you have more than one CRI installed or if you have non-standard CRI socket. |
| --feature-gates string | |
|  | A set of key=value pairs that describe feature gates for various features. Options are: ControlPlaneKubeletLocalMode=true|false (BETA - default=true) NodeLocalCRISocket=true|false (BETA - default=true) PublicKeysECDSA=true|false (DEPRECATED - default=false) RootlessControlPlane=true|false (ALPHA - default=false) WaitForAllControlPlaneComponents=true|false (default=true) |
| -h, --help | |
|  | help for pull |
| --image-repository string     Default: "registry.k8s.io" | |
|  | Choose a container registry to pull control plane images from |
| --kubernetes-version string     Default: "stable-1" | |
|  | Choose a specific Kubernetes version for the control plane. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## What's next

* [kubeadm upgrade](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/) to upgrade a Kubernetes cluster to a newer version

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
