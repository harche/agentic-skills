# kubeadm kubeconfig

`kubeadm kubeconfig` provides utilities for managing kubeconfig files.

For examples on how to use `kubeadm kubeconfig user` see
[Generating kubeconfig files for additional users](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#kubeconfig-additional-users).

## kubeadm kubeconfig

* overview

### Synopsis

Kubeconfig file utilities.

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

## kubeadm kubeconfig user

This command can be used to output a kubeconfig file for an additional user.

* user

### Synopsis

Output a kubeconfig file for an additional user.

```
kubeadm kubeconfig user [flags]
```

### Examples

```
  # Output a kubeconfig file for an additional user named foo
  kubeadm kubeconfig user --client-name=foo

  # Output a kubeconfig file for an additional user named foo using a kubeadm config file bar
  kubeadm kubeconfig user --client-name=foo --config=bar
```

### Options

|  |  |
| --- | --- |
| --client-name string | |
|  | The name of user. It will be used as the CN if client certificates are created |
| --config string | |
|  | Path to a kubeadm configuration file. |
| -h, --help | |
|  | help for user |
| --org strings | |
|  | The organizations of the client certificate. It will be used as the O if client certificates are created |
| --token string | |
|  | The token that should be used as the authentication mechanism for this kubeconfig, instead of client certificates |
| --validity-period duration     Default: 8760h0m0s | |
|  | The validity period of the client certificate. It is an offset from the current time. |

### Options inherited from parent commands

|  |  |
| --- | --- |
| --rootfs string | |
|  | The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path. |

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
