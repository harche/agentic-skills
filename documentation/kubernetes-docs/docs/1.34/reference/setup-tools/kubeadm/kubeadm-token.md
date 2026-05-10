# kubeadm token

Bootstrap tokens are used for establishing bidirectional trust between a node joining
the cluster and a control-plane node, as described in [authenticating with bootstrap tokens](/docs/reference/access-authn-authz/bootstrap-tokens/).

`kubeadm init` creates an initial token with a 24-hour TTL. The following commands allow you to manage
such a token and also to create and manage new ones.

## kubeadm token create

Create bootstrap tokens on the server

### Synopsis

This command will create a bootstrap token for you.
You can specify the usages for this token, the "time to live" and an optional human friendly description.

The [token] is the actual token to write.
This should be a securely generated random token of the form "[a-z0-9]{6}.[a-z0-9]{16}".
If no [token] is given, kubeadm will generate a random token instead.

```
kubeadm token create [token]
```

### Options

|  |  |
| --- | --- |
| --certificate-key string | |
|  | When used together with '--print-join-command', print the full 'kubeadm join' flag needed to join the cluster as a control-plane. To create a new certificate key you must use 'kubeadm init phase upload-certs --upload-certs'. |
| --config string | |
|  | Path to a kubeadm configuration file. |
| --description string | |
|  | A human friendly description of how this token is used. |
| --groups strings     Default: "system:bootstrappers:kubeadm:default-node-token" | |
|  | Extra groups that this token will authenticate as when used for authentication. Must match "\Asystem:bootstrappers:[a-z0-9:-]{0,255}[a-z0-9]\z" |
| -h, --help | |
|  | help for create |
| --print-join-command | |
|  | Instead of printing only the token, print the full 'kubeadm join' flag needed to join the cluster using the token. |
| --ttl duration     Default: 24h0m0s | |
|  | The duration before the token is automatically deleted (e.g. 1s, 2m, 3h). If set to '0', the token will never expire |
| --usages strings     Default: "signing,authentication" | |
|  | Describes the ways in which this token can be used. You can pass --usages multiple times or provide a comma separated list of options. Valid options: [signing,authentication] |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --dry-run | |
|  | Whether to enable dry-run mode or not |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm token delete

Delete bootstrap tokens on the server

### Synopsis

This command will delete a list of bootstrap tokens for you.

The [token-value] is the full Token of the form "[a-z0-9]{6}.[a-z0-9]{16}" or the
Token ID of the form "[a-z0-9]{6}" to delete.

```
kubeadm token delete [token-value] ...
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for delete |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --dry-run | |
|  | Whether to enable dry-run mode or not |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm token generate

Generate and print a bootstrap token, but do not create it on the server

### Synopsis

This command will print out a randomly-generated bootstrap token that can be used with
the "init" and "join" commands.

You don't have to use this command in order to generate a token. You can do so
yourself as long as it is in the format "[a-z0-9]{6}.[a-z0-9]{16}". This
command is provided for convenience to generate tokens in the given format.

You can also use "kubeadm init" without specifying a token and it will
generate and print one for you.

```
kubeadm token generate [flags]
```

### Options

|  |  |
| --- | --- |
| -h, --help | |
|  | help for generate |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --dry-run | |
|  | Whether to enable dry-run mode or not |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## kubeadm token list

List bootstrap tokens on the server

### Synopsis

This command will list all bootstrap tokens for you.

```
kubeadm token list [flags]
```

### Options

|  |  |
| --- | --- |
| --allow-missing-template-keys     Default: true | |
|  | If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats. |
| -h, --help | |
|  | help for list |
| -o, --output string     Default: "text" | |
|  | Output format. One of: text|json|yaml|go-template|go-template-file|template|templatefile|jsonpath|jsonpath-as-json|jsonpath-file. |
| --show-managed-fields | |
|  | If true, keep the managedFields when printing objects in JSON or YAML format. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --dry-run | |
|  | Whether to enable dry-run mode or not |
| --kubeconfig string     Default: "/etc/kubernetes/admin.conf" | |
|  | The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file. |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

## What's next

* [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) to bootstrap a Kubernetes worker node and join it to the cluster

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
