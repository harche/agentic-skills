# Mapping PodSecurityPolicies to Pod Security Standards

The tables below enumerate the configuration parameters on
`PodSecurityPolicy` objects, whether the field mutates
and/or validates pods, and how the configuration values map to the
[Pod Security Standards](/docs/concepts/security/pod-security-standards/).

For each applicable parameter, the allowed values for the
[Baseline](/docs/concepts/security/pod-security-standards/#baseline) and
[Restricted](/docs/concepts/security/pod-security-standards/#restricted) profiles are listed.
Anything outside the allowed values for those profiles would fall under the
[Privileged](/docs/concepts/security/pod-security-standards/#privileged) profile. "No opinion"
means all values are allowed under all Pod Security Standards.

For a step-by-step migration guide, see
[Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller](/docs/tasks/configure-pod-container/migrate-from-psp/).

## PodSecurityPolicy Spec

The fields enumerated in this table are part of the `PodSecurityPolicySpec`, which is specified
under the `.spec` field path.

Mapping PodSecurityPolicySpec fields to Pod Security Standards

| `PodSecurityPolicySpec` | Type | Pod Security Standards Equivalent |
| --- | --- | --- |
| `privileged` | Validating | **Baseline & Restricted**: `false` / undefined / nil |
| `defaultAddCapabilities` | Mutating & Validating | Requirements match `allowedCapabilities` below. |
| `allowedCapabilities` | Validating | **Baseline**: subset of   * `AUDIT_WRITE` * `CHOWN` * `DAC_OVERRIDE` * `FOWNER` * `FSETID` * `KILL` * `MKNOD` * `NET_BIND_SERVICE` * `SETFCAP` * `SETGID` * `SETPCAP` * `SETUID` * `SYS_CHROOT`   **Restricted**: empty / undefined / nil OR a list containing *only* `NET_BIND_SERVICE` |
| `requiredDropCapabilities` | Mutating & Validating | **Baseline**: no opinion  **Restricted**: must include `ALL` |
| `volumes` | Validating | **Baseline**: anything except   * `hostPath` * `*`   **Restricted**: subset of   * `configMap` * `csi` * `downwardAPI` * `emptyDir` * `ephemeral` * `persistentVolumeClaim` * `projected` * `secret` |
| `hostNetwork` | Validating | **Baseline & Restricted**: `false` / undefined / nil |
| `hostPorts` | Validating | **Baseline & Restricted**: undefined / nil / empty |
| `hostPID` | Validating | **Baseline & Restricted**: `false` / undefined / nil |
| `hostIPC` | Validating | **Baseline & Restricted**: `false` / undefined / nil |
| `seLinux` | Mutating & Validating | **Baseline & Restricted**: `seLinux.rule` is `MustRunAs`, with the following `options`   * `user` is unset (`""` / undefined / nil) * `role` is unset (`""` / undefined / nil) * `type` is unset or one of: `container_t, container_init_t, container_kvm_t, container_engine_t` * `level` is anything |
| `runAsUser` | Mutating & Validating | **Baseline**: Anything  **Restricted**: `rule` is `MustRunAsNonRoot` |
| `runAsGroup` | Mutating (MustRunAs) & Validating | *No opinion* |
| `supplementalGroups` | Mutating & Validating | *No opinion* |
| `fsGroup` | Mutating & Validating | *No opinion* |
| `readOnlyRootFilesystem` | Mutating & Validating | *No opinion* |
| `defaultAllowPrivilegeEscalation` | Mutating | *No opinion (non-validating)* |
| `allowPrivilegeEscalation` | Mutating & Validating | *Only mutating if set to `false`*  **Baseline**: No opinion  **Restricted**: `false` |
| `allowedHostPaths` | Validating | *No opinion (volumes takes precedence)* |
| `allowedFlexVolumes` | Validating | *No opinion (volumes takes precedence)* |
| `allowedCSIDrivers` | Validating | *No opinion (volumes takes precedence)* |
| `allowedUnsafeSysctls` | Validating | **Baseline & Restricted**: undefined / nil / empty |
| `forbiddenSysctls` | Validating | *No opinion* |
| `allowedProcMountTypes` *(alpha feature)* | Validating | **Baseline & Restricted**: `["Default"]` OR undefined / nil / empty |
| `runtimeClass` `.defaultRuntimeClassName` | Mutating | *No opinion* |
| `runtimeClass` `.allowedRuntimeClassNames` | Validating | *No opinion* |

## PodSecurityPolicy annotations

The [annotations](/docs/concepts/overview/working-with-objects/annotations/) enumerated in this
table can be specified under `.metadata.annotations` on the PodSecurityPolicy object.

Mapping PodSecurityPolicy annotations to Pod Security Standards

| `PSP Annotation` | Type | Pod Security Standards Equivalent |
| --- | --- | --- |
| `seccomp.security.alpha.kubernetes.io` `/defaultProfileName` | Mutating | *No opinion* |
| `seccomp.security.alpha.kubernetes.io` `/allowedProfileNames` | Validating | **Baseline**: `"runtime/default,"` *(Trailing comma to allow unset)*  **Restricted**: `"runtime/default"` *(No trailing comma)*  *`localhost/*` values are also permitted for both Baseline & Restricted.* |
| `apparmor.security.beta.kubernetes.io` `/defaultProfileName` | Mutating | *No opinion* |
| `apparmor.security.beta.kubernetes.io` `/allowedProfileNames` | Validating | **Baseline**: `"runtime/default,"` *(Trailing comma to allow unset)*  **Restricted**: `"runtime/default"` *(No trailing comma)*  *`localhost/*` values are also permitted for both Baseline & Restricted.* |

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
