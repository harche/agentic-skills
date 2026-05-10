# Migrating from dockershim

This section presents information you need to know when migrating from
dockershim to other container runtimes.

Since the announcement of [dockershim deprecation](/blog/2020/12/08/kubernetes-1-20-release-announcement/#dockershim-deprecation)
in Kubernetes 1.20, there were questions on how this will affect various workloads and Kubernetes
installations. Our [Dockershim Removal FAQ](/blog/2022/02/17/dockershim-faq/) is there to help you
to understand the problem better.

Dockershim was removed from Kubernetes with the release of v1.24.
If you use Docker Engine via dockershim as your container runtime and wish to upgrade to v1.24,
it is recommended that you either migrate to another runtime or find an alternative means to obtain Docker Engine support.
Check out the [container runtimes](/docs/setup/production-environment/container-runtimes/)
section to know your options.

The version of Kubernetes with dockershim (1.23) is out of support and the v1.24
will run out of support [soon](/releases/#release-v1-24). Make sure to
[report issues](https://github.com/kubernetes/kubernetes/issues) you encountered
with the migration so the issues can be fixed in a timely manner and your cluster would be
ready for dockershim removal. After v1.24 running out of support, you will need
to contact your Kubernetes provider for support or upgrade multiple versions at a time
if there are critical issues affecting your cluster.

Your cluster might have more than one kind of node, although this is not a common
configuration.

These tasks will help you to migrate:

* [Check whether Dockershim removal affects you](/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/)
* [Migrating telemetry and security agents from dockershim](/docs/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents/)

## What's next

* Check out [container runtimes](/docs/setup/production-environment/container-runtimes/)
  to understand your options for an alternative.
* If you find a defect or other technical concern relating to migrating away from dockershim,
  you can [report an issue](https://github.com/kubernetes/kubernetes/issues/new/choose)
  to the Kubernetes project.

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
