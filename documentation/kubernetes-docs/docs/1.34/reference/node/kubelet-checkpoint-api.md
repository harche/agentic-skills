# Kubelet Checkpoint API

FEATURE STATE:
`Kubernetes v1.30 [beta]`(enabled by default)

Checkpointing a container is the functionality to create a stateful copy of a
running container. Once you have a stateful copy of a container, you could
move it to a different computer for debugging or similar purposes.

If you move the checkpointed container data to a computer that's able to restore
it, that restored container continues to run at exactly the same
point it was checkpointed. You can also inspect the saved data, provided that you
have suitable tools for doing so.

Creating a checkpoint of a container might have security implications. Typically
a checkpoint contains all memory pages of all processes in the checkpointed
container. This means that everything that used to be in memory is now available
on the local disk. This includes all private data and possibly keys used for
encryption. The underlying CRI implementations (the container runtime on that node)
should create the checkpoint archive to be only accessible by the `root` user. It
is still important to remember if the checkpoint archive is transferred to another
system all memory pages will be readable by the owner of the checkpoint archive.

## Operations

### `post` checkpoint the specified container

Tell the kubelet to checkpoint a specific container from the specified Pod.

Consult the [Kubelet authentication/authorization reference](/docs/reference/access-authn-authz/kubelet-authn-authz/)
for more information about how access to the kubelet checkpoint interface is
controlled.

The kubelet will request a checkpoint from the underlying
[CRI](/docs/concepts/architecture/cri "Protocol for communication between the kubelet and the local container runtime.") implementation. In the checkpoint
request the kubelet will specify the name of the checkpoint archive as
`checkpoint-<podFullName>-<containerName>-<timestamp>.tar` and also request to
store the checkpoint archive in the `checkpoints` directory below its root
directory (as defined by `--root-dir`). This defaults to
`/var/lib/kubelet/checkpoints`.

The checkpoint archive is in *tar* format, and could be listed using an implementation of
[`tar`](https://pubs.opengroup.org/onlinepubs/7908799/xcu/tar.html). The contents of the
archive depend on the underlying CRI implementation (the container runtime on that node).

#### HTTP Request

POST /checkpoint/{namespace}/{pod}/{container}

#### Parameters

* **namespace** (*in path*): string, required

  [Namespace](/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster.")
* **pod** (*in path*): string, required

  [Pod](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.")
* **container** (*in path*): string, required

  [Container](/docs/concepts/containers/ "A lightweight and portable executable image that contains software and all of its dependencies.")
* **timeout** (*in query*): integer

  Timeout in seconds to wait until the checkpoint creation is finished.
  If zero or no timeout is specified the default [CRI](/docs/concepts/architecture/cri "Protocol for communication between the kubelet and the local container runtime.") timeout value will be used. Checkpoint
  creation time depends directly on the used memory of the container.
  The more memory a container uses the more time is required to create
  the corresponding checkpoint.

#### Response

200: OK

401: Unauthorized

404: Not Found (if the `ContainerCheckpoint` feature gate is disabled)

404: Not Found (if the specified `namespace`, `pod` or `container` cannot be found)

500: Internal Server Error (if the CRI implementation encounter an error during checkpointing (see error message for further details))

500: Internal Server Error (if the CRI implementation does not implement the checkpoint CRI API (see error message for further details))

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
