# Documentation Content Guide

This page contains guidelines for Kubernetes documentation.

If you have questions about what's allowed, join the #sig-docs channel in
[Kubernetes Slack](https://slack.k8s.io/) and ask!

You can register for Kubernetes Slack at <https://slack.k8s.io/>.

For information on creating new content for the Kubernetes
docs, follow the [style guide](/docs/contribute/style/style-guide/).

## Overview

Source for the Kubernetes website, including the docs, resides in the
[kubernetes/website](https://github.com/kubernetes/website) repository.

Located in the `kubernetes/website/content/<language_code>/docs` folder, the
majority of Kubernetes documentation is specific to the [Kubernetes
project](https://github.com/kubernetes/kubernetes).

## What's allowed

Kubernetes docs allow content for third-party projects only when:

* Content documents software in the Kubernetes project
* Content documents software that's out of project but necessary for Kubernetes to function
* Content is canonical on kubernetes.io, or links to canonical content elsewhere

### Third party content

Kubernetes documentation includes applied examples of projects in the Kubernetes
project—projects that live in the [kubernetes](https://github.com/kubernetes) and
[kubernetes-sigs](https://github.com/kubernetes-sigs) GitHub organizations.

Links to active content in the Kubernetes project are always allowed.

Kubernetes requires some third party content to function. Examples include container runtimes (containerd, CRI-O, Docker),
[networking policy](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/) (CNI plugins),
[Ingress controllers](/docs/concepts/services-networking/ingress-controllers/),
and [logging](/docs/concepts/cluster-administration/logging/).

Docs can link to third-party open source software (OSS) outside the Kubernetes
project only if it's necessary for Kubernetes to function.

### Dual sourced content

Wherever possible, Kubernetes docs link to canonical sources instead of hosting
dual-sourced content.

Dual-sourced content requires double the effort (or more!) to maintain
and grows stale more quickly.

> **Note:**
> If you're a maintainer for a Kubernetes project and need help hosting your own docs,
> ask for help in [#sig-docs on Kubernetes Slack](https://kubernetes.slack.com/messages/C1J0BPD2M/).

### More information

If you have questions about allowed content, join the [Kubernetes Slack](https://slack.k8s.io/) #sig-docs channel and ask!

## What's next

* Read the [Style guide](/docs/contribute/style/style-guide/).

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
