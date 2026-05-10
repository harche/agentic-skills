# kuberc (v1alpha1)

## Resource Types

* [Preference](#kubectl-config-k8s-io-v1alpha1-Preference)

## `Preference`

Preference stores elements of KubeRC configuration file

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubectl.config.k8s.io/v1alpha1` |
| `kind` string | `Preference` |
| `overrides` **[Required]**  [`[]CommandDefaults`](#kubectl-config-k8s-io-v1alpha1-CommandDefaults) | overrides allows changing default flag values of commands. This is especially useful, when user doesn't want to explicitly set flags each time. |
| `aliases` **[Required]**  [`[]AliasOverride`](#kubectl-config-k8s-io-v1alpha1-AliasOverride) | aliases allow defining command aliases for existing kubectl commands, with optional default flag values. If the alias name collides with a built-in command, built-in command always takes precedence. Flag overrides defined in the overrides section do NOT apply to aliases for the same command. kubectl [ALIAS NAME] [USER_FLAGS] [USER_EXPLICIT_ARGS] expands to kubectl [COMMAND] # built-in command alias points to [KUBERC_PREPEND_ARGS] [USER_FLAGS] [KUBERC_FLAGS] # rest of the flags that are not passed by user in [USER_FLAGS] [USER_EXPLICIT_ARGS] [KUBERC_APPEND_ARGS] e.g.   * name: runx   command: run   flags:   + name: image     default: nginx     appendArgs:    ---    + custom-arg1     For example, if user invokes "kubectl runx test-pod" command,     this will be expanded to "kubectl run --image=nginx test-pod -- custom-arg1" * name: getn   command: get   flags:   + name: output     default: wide     prependArgs:   + node     "kubectl getn control-plane-1" expands to "kubectl get node control-plane-1 --output=wide"     "kubectl getn control-plane-1 --output=json" expands to "kubectl get node --output=json control-plane-1" |

## `AliasOverride`

**Appears in:**

* [Preference](#kubectl-config-k8s-io-v1alpha1-Preference)

AliasOverride stores the alias definitions.

| Field | Description |
| --- | --- |
| `name` **[Required]**  `string` | name is the name of alias that can only include alphabetical characters If the alias name conflicts with the built-in command, built-in command will be used. |
| `command` **[Required]**  `string` | command is the single or set of commands to execute, such as "set env" or "create" |
| `prependArgs` **[Required]**  `[]string` | prependArgs stores the arguments such as resource names, etc. These arguments are inserted after the alias name. |
| `appendArgs` **[Required]**  `[]string` | appendArgs stores the arguments such as resource names, etc. These arguments are appended to the USER_ARGS. |
| `flags` **[Required]**  [`[]CommandOptionDefault`](#kubectl-config-k8s-io-v1alpha1-CommandOptionDefault) | flags is allocated to store the flag definitions of alias. flags only modifies the default value of the flag and if user explicitly passes a value, explicit one is used. |

## `CommandDefaults`

**Appears in:**

* [Preference](#kubectl-config-k8s-io-v1alpha1-Preference)

CommandDefaults stores the commands and their associated option's
default values.

| Field | Description |
| --- | --- |
| `command` **[Required]**  `string` | command refers to a command whose flag's default value is changed. |
| `flags` **[Required]**  [`[]CommandOptionDefault`](#kubectl-config-k8s-io-v1alpha1-CommandOptionDefault) | flags is a list of flags storing different default values. |

## `CommandOptionDefault`

**Appears in:**

* [AliasOverride](#kubectl-config-k8s-io-v1alpha1-AliasOverride)
* [CommandDefaults](#kubectl-config-k8s-io-v1alpha1-CommandDefaults)

CommandOptionDefault stores the name and the specified default
value of an option.

| Field | Description |
| --- | --- |
| `name` **[Required]**  `string` | Flag name (long form, without dashes). |
| `default` **[Required]**  `string` | In a string format of a default value. It will be parsed by kubectl to the compatible value of the flag. |

This page is automatically generated.

If you plan to report an issue with this page, mention that the page is auto-generated in your issue description. The fix may need to happen elsewhere in the Kubernetes project.

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
