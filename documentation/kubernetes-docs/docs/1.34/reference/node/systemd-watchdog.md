# Kubelet Systemd Watchdog

FEATURE STATE:
`Kubernetes v1.32 [beta]`(enabled by default)

On Linux nodes, Kubernetes 1.34 supports integrating with
[systemd](https://systemd.io/) to allow the operating system supervisor to recover
a failed kubelet. This integration is not enabled by default.
It can be used as an alternative to periodically requesting
the kubelet's `/healthz` endpoint for health checks. If the kubelet
does not respond to the watchdog within the timeout period, the watchdog
will kill the kubelet.

The systemd watchdog works by requiring the service to periodically send
a *keep-alive* signal to the systemd process. If the signal is not received
within a specified timeout period, the service is considered unresponsive
and is terminated. The service can then be restarted according to the configuration.

## Configuration

Using the systemd watchdog requires configuring the `WatchdogSec` parameter
in the `[Service]` section of the kubelet service unit file:

```
[Service]
WatchdogSec=30s
```

Setting `WatchdogSec=30s` indicates a service watchdog timeout of 30 seconds.
Within the kubelet, the `sd_notify()` function is invoked, at intervals of \( WatchdogSec \div 2\). to send
`WATCHDOG=1` (a keep-alive message). If the watchdog is not fed
within the timeout period, the kubelet will be killed. Setting `Restart`
to "always", "on-failure", "on-watchdog", or "on-abnormal" will ensure that the service
is automatically restarted.

Some details about the systemd configuration:

1. If you set the systemd value for `WatchdogSec` to 0, or omit setting it, the systemd watchdog is not
   enabled for this unit.
2. The kubelet supports a minimum watchdog period of 1.0 seconds; this is to prevent the kubelet
   from being killed unexpectedly. You can set the value of `WatchdogSec` in a systemd unit definition
   to a period shorter than 1 second, but Kubernetes does not support any shorter interval.
   The timeout does not have to be a whole integer number of seconds.
3. The Kubernetes project suggests setting `WatchdogSec` to approximately a 15s period.
   Periods longer than 10 minutes are supported but explicitly **not** recommended.

### Example Configuration

```
[Unit]
Description=kubelet: The Kubernetes Node Agent
Documentation=https://kubernetes.io/docs/home/
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/bin/kubelet
# Configures the watchdog timeout
WatchdogSec=30s
Restart=on-failure
StartLimitInterval=0
RestartSec=10

[Install]
WantedBy=multi-user.target
```

## What's next

For more details about systemd configuration, refer to the
[systemd documentation](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html#WatchdogSec=)

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
