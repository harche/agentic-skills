# Kubelet Device Manager API Versions

This page provides details of version compatibility between the Kubernetes
[device plugin API](https://github.com/kubernetes/kubelet/tree/master/pkg/apis/deviceplugin),
and different versions of Kubernetes itself.

## Compatibility matrix

|  | `v1alpha1` | `v1beta1` |
| --- | --- | --- |
| Kubernetes 1.21 | - | ✓ |
| Kubernetes 1.22 | - | ✓ |
| Kubernetes 1.23 | - | ✓ |
| Kubernetes 1.24 | - | ✓ |
| Kubernetes 1.25 | - | ✓ |
| Kubernetes 1.26 | - | ✓ |

Key:

* `✓` Exactly the same features / API objects in both device plugin API and
  the Kubernetes version.
* `+` The device plugin API has features or API objects that may not be present in the
  Kubernetes cluster, either because the device plugin API has added additional new API
  calls, or that the server has removed an old API call. However, everything they have in
  common (most other APIs) will work. Note that alpha APIs may vanish or
  change significantly between one minor release and the next.
* `-` The Kubernetes cluster has features the device plugin API can't use,
  either because server has added additional API calls, or that device plugin API has
  removed an old API call. However, everything they share in common (most APIs) will work.

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
