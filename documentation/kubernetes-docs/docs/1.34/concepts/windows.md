# Windows in Kubernetes

Kubernetes supports nodes that run Microsoft Windows.

Kubernetes supports worker [nodes](/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.")
running either Linux or Microsoft Windows.

> **Note:**
> 🛇 This item links to a third party project or product that is not part of Kubernetes itself. [More information](#third-party-content-disclaimer)

The CNCF and its parent the Linux Foundation take a vendor-neutral approach
towards compatibility. It is possible to join your [Windows server](https://www.microsoft.com/en-us/windows-server)
as a worker node to a Kubernetes cluster.

You can [install and set up kubectl on Windows](/docs/tasks/tools/install-kubectl-windows/)
no matter what operating system you use within your cluster.

If you are using Windows nodes, you can read:

* [Networking On Windows](/docs/concepts/services-networking/windows-networking/)
* [Windows Storage In Kubernetes](/docs/concepts/storage/windows-storage/)
* [Resource Management for Windows Nodes](/docs/concepts/configuration/windows-resource-management/)
* [Configure RunAsUserName for Windows Pods and Containers](/docs/tasks/configure-pod-container/configure-runasusername/)
* [Create A Windows HostProcess Pod](/docs/tasks/configure-pod-container/create-hostprocess-pod/)
* [Configure Group Managed Service Accounts for Windows Pods and Containers](/docs/tasks/configure-pod-container/configure-gmsa/)
* [Security For Windows Nodes](/docs/concepts/security/windows-security/)
* [Windows Debugging Tips](/docs/tasks/debug/debug-cluster/windows/)
* [Guide for Scheduling Windows Containers in Kubernetes](/docs/concepts/windows/user-guide/)

or, for an overview, read:

* [Windows containers in Kubernetes](/docs/concepts/windows/intro/)
* [Guide for Running Windows Containers in Kubernetes](/docs/concepts/windows/user-guide/)

Items on this page refer to third party products or projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for those third-party products or projects. See the [CNCF website guidelines](https://github.com/cncf/foundation/blob/master/website-guidelines.md) for more details.

You should read the [content guide](/docs/contribute/style/content-guide/#third-party-content) before proposing a change that adds an extra third-party link.

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
