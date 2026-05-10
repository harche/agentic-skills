# Kubernetes z-pages

Provides runtime diagnostics for Kubernetes components, offering insights into component runtime status and configuration flags.

FEATURE STATE:
`Kubernetes v1.32 [alpha]`

Kubernetes core components can expose a suite of *z-endpoints* to make it easier for users
to debug their cluster and its components. These endpoints are strictly to be used for human
inspection to gain real time debugging information of a component binary.
Avoid automated scraping of data returned by these endpoints; in Kubernetes 1.34
these are an **alpha** feature and the response format may change in future releases.

## z-pages

Kubernetes v1.34 allows you to enable *z-pages* to help you troubleshoot
problems with its core control plane components. These special debugging endpoints provide internal
information about running components. For Kubernetes 1.34, components
serve the following endpoints (when enabled):

* [z-pages](#z-pages)
  + [statusz](#statusz)
  + [flagz](#flagz)

### statusz

Enabled using the `ComponentStatusz` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/),
the `/statusz` endpoint displays high level information about the component such as its Kubernetes version, emulation version, start time and more.

The `/statusz` response from the API server is similar to:

```
kube-apiserver statusz
Warning: This endpoint is not meant to be machine parseable, has no formatting compatibility guarantees and is for debugging purposes only.

Started: Wed Oct 16 21:03:43 UTC 2024
Up: 0 hr 00 min 16 sec
Go version: go1.23.2
Binary version: 1.32.0-alpha.0.1484&#43;5eeac4f21a491b-dirty
Emulation version: 1.32.0-alpha.0.1484
```

### flagz

Enabled using the `ComponentFlagz` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/), the `/flagz` endpoint shows you the command line arguments that were used to start a component.

The `/flagz` data for the API server looks something like:

```
kube-apiserver flags
Warning: This endpoint is not meant to be machine parseable, has no formatting compatibility guarantees and is for debugging purposes only.

advertise-address=192.168.8.2
contention-profiling=false
enable-priority-and-fairness=true
profiling=true
authorization-mode=[Node,RBAC]
authorization-webhook-cache-authorized-ttl=5m0s
authorization-webhook-cache-unauthorized-ttl=30s
authorization-webhook-version=v1beta1
default-watch-cache-size=100
```

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
