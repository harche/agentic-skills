# Articles on dockershim Removal and on Using CRI-compatible Runtimes

This is a list of articles and other pages that are either
about the Kubernetes' deprecation and removal of *dockershim*,
or about using CRI-compatible container runtimes,
in connection with that removal.

## Kubernetes project

* Kubernetes blog: [Dockershim Removal FAQ](/blog/2020/12/02/dockershim-faq/) (originally published 2020/12/02)
* Kubernetes blog: [Updated: Dockershim Removal FAQ](/blog/2022/02/17/dockershim-faq/) (updated published 2022/02/17)
* Kubernetes blog: [Kubernetes is Moving on From Dockershim: Commitments and Next Steps](/blog/2022/01/07/kubernetes-is-moving-on-from-dockershim/) (published 2022/01/07)
* Kubernetes blog: [Dockershim removal is coming. Are you ready?](/blog/2021/11/12/are-you-ready-for-dockershim-removal/) (published 2021/11/12)
* Kubernetes documentation: [Migrating from dockershim](/docs/tasks/administer-cluster/migrating-from-dockershim/)
* Kubernetes documentation: [Container Runtimes](/docs/setup/production-environment/container-runtimes/)
* Kubernetes enhancement proposal: [KEP-2221: Removing dockershim from kubelet](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/2221-remove-dockershim/README.md)
* Kubernetes enhancement proposal issue: [Removing dockershim from kubelet](https://github.com/kubernetes/enhancements/issues/2221) (*k/enhancements#2221*)

You can provide feedback via the GitHub issue [**Dockershim removal feedback & issues**](https://github.com/kubernetes/kubernetes/issues/106917). (*k/kubernetes/#106917*)

## External sources

* Amazon Web Services EKS documentation: [Amazon EKS is ending support for Dockershim](https://docs.aws.amazon.com/eks/latest/userguide/dockershim-deprecation.html)
* CNCF conference video: [Lessons Learned Migrating Kubernetes from Docker to containerd Runtime](https://www.youtube.com/watch?v=uDOu6rK4yOk) (Ana Caylin, at KubeCon Europe 2019)
* Docker.com blog: [What developers need to know about Docker, Docker Engine, and Kubernetes v1.20](https://www.docker.com/blog/what-developers-need-to-know-about-docker-docker-engine-and-kubernetes-v1-20/) (published 2020/12/04)
* "*Google Open Source*" channel on YouTube: [Learn Kubernetes with Google - Migrating from Dockershim to Containerd](https://youtu.be/fl7_4hjT52g)
* Microsoft Apps on Azure blog: [Dockershim deprecation and AKS](https://techcommunity.microsoft.com/t5/apps-on-azure-blog/dockershim-deprecation-and-aks/ba-p/3055902) (published 2022/01/21)
* Mirantis blog: [The Future of Dockershim is cri-dockerd](https://www.mirantis.com/blog/the-future-of-dockershim-is-cri-dockerd/) (published 2021/04/21)
* Mirantis: [Mirantis/cri-dockerd](https://mirantis.github.io/cri-dockerd/) Official Documentation
* Tripwire: [How Dockershim’s Forthcoming Deprecation Affects Your Kubernetes](https://www.tripwire.com/state-of-security/security-data-protection/cloud/how-dockershim-forthcoming-deprecation-affects-your-kubernetes/) (published 2021/07/01)

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
