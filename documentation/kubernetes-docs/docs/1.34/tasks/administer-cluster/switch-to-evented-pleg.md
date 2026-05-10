# Switching from Polling to CRI Event-based Updates to Container Status

FEATURE STATE:
`Kubernetes v1.26 [alpha]`(disabled by default)

This page shows how to migrate nodes to use event based updates for container status. The event-based
implementation reduces node resource consumption by the kubelet, compared to the legacy approach
that relies on polling.
You may know this feature as *evented Pod lifecycle event generator (PLEG)*. That's the name used
internally within the Kubernetes project for a key implementation detail.

The polling based approach is referred to as *generic PLEG*.

## Before you begin

* You need to run a version of Kubernetes that provides this feature.
  Kubernetes v1.27 includes beta support for event-based container
  status updates. The feature is beta but is *disabled* by default
  because it requires support from the container runtime.
* Your Kubernetes server must be at or later than version 1.26.

  To check the version, enter `kubectl version`.

  If you are running a different version of Kubernetes, check the documentation for that release.
* The container runtime in use must support container lifecycle events.
  The kubelet automatically switches back to the legacy generic PLEG
  mechanism if the container runtime does not announce support for
  container lifecycle events, even if you have this feature gate enabled.

## Why switch to Evented PLEG?

* The *Generic PLEG* incurs non-negligible overhead due to frequent polling of container statuses.
* This overhead is exacerbated by Kubelet's parallelized polling of container states, thus limiting
  its scalability and causing poor performance and reliability problems.
* The goal of *Evented PLEG* is to reduce unnecessary work during inactivity
  by replacing periodic polling.

## Switching to Evented PLEG

1. Start the Kubelet with the [feature gate](/docs/reference/command-line-tools-reference/feature-gates/)
   `EventedPLEG` enabled. You can manage the kubelet feature gates editing the kubelet
   [config file](/docs/tasks/administer-cluster/kubelet-config-file/) and restarting the kubelet service.
   You need to do this on each node where you are using this feature.
2. Make sure the node is [drained](/docs/tasks/administer-cluster/safely-drain-node/) before proceeding.
3. Start the container runtime with the container event generation enabled.

   * Containerd
     * CRI-O

   Version 1.7+

   Version 1.26+

   Check if the CRI-O is already configured to emit CRI events by verifying the configuration,

   ```
   crio config | grep enable_pod_events
   ```

   If it is enabled, the output should be similar to the following:

   ```
   enable_pod_events = true
   ```

   To enable it, start the CRI-O daemon with the flag `--enable-pod-events=true` or
   use a dropin config with the following lines:

   ```
   [crio.runtime]
   enable_pod_events: true
   ```

   Your Kubernetes server must be at or later than version 1.26.

   To check the version, enter `kubectl version`.
4. Verify that the kubelet is using event-based container stage change monitoring.
   To check, look for the term `EventedPLEG` in the kubelet logs.

   The output should be similar to this:

   ```
   I0314 11:10:13.909915 1105457 feature_gate.go:249] feature gates: &{map[EventedPLEG:true]}
   ```

   If you have set `--v` to 4 and above, you might see more entries that indicate
   that the kubelet is using event-based container state monitoring.

   ```
   I0314 11:12:42.009542 1110177 evented.go:238] "Evented PLEG: Generated pod status from the received event" podUID=3b2c6172-b112-447a-ba96-94e7022912dc
   I0314 11:12:44.623326 1110177 evented.go:238] "Evented PLEG: Generated pod status from the received event" podUID=b3fba5ea-a8c5-4b76-8f43-481e17e8ec40
   I0314 11:12:44.714564 1110177 evented.go:238] "Evented PLEG: Generated pod status from the received event" podUID=b3fba5ea-a8c5-4b76-8f43-481e17e8ec40
   ```

## What's next

* Learn more about the design in the Kubernetes Enhancement Proposal (KEP):
  [Kubelet Evented PLEG for Better Performance](https://github.com/kubernetes/enhancements/blob/5b258a990adabc2ffdc9d84581ea6ed696f7ce6c/keps/sig-node/3386-kubelet-evented-pleg/README.md).

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
