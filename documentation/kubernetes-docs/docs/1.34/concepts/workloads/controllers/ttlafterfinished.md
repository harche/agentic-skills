# Automatic Cleanup for Finished Jobs

A time-to-live mechanism to clean up old Jobs that have finished execution.

FEATURE STATE:
`Kubernetes v1.23 [stable]`

When your Job has finished, it's useful to keep that Job in the API (and not immediately delete the Job)
so that you can tell whether the Job succeeded or failed.

Kubernetes' TTL-after-finished [controller](/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") provides a
TTL (time to live) mechanism to limit the lifetime of Job objects that
have finished execution.

## Cleanup for finished Jobs

The TTL-after-finished controller is only supported for Jobs. You can use this mechanism to clean
up finished Jobs (either `Complete` or `Failed`) automatically by specifying the
`.spec.ttlSecondsAfterFinished` field of a Job, as in this
[example](/docs/concepts/workloads/controllers/job/#clean-up-finished-jobs-automatically).

The TTL-after-finished controller assumes that a Job is eligible to be cleaned up
TTL seconds after the Job has finished. The timer starts once the
status condition of the Job changes to show that the Job is either `Complete` or `Failed`; once the TTL has
expired, that Job becomes eligible for
[cascading](/docs/concepts/architecture/garbage-collection/#cascading-deletion) removal. When the
TTL-after-finished controller cleans up a job, it will delete it cascadingly, that is to say it will delete
its dependent objects together with it.

Kubernetes honors object lifecycle guarantees on the Job, such as waiting for
[finalizers](/docs/concepts/overview/working-with-objects/finalizers/).

You can set the TTL seconds at any time. Here are some examples for setting the
`.spec.ttlSecondsAfterFinished` field of a Job:

* Specify this field in the Job manifest, so that a Job can be cleaned up
  automatically some time after it finishes.
* Manually set this field of existing, already finished Jobs, so that they become eligible
  for cleanup.
* Use a
  [mutating admission webhook](/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook)
  to set this field dynamically at Job creation time. Cluster administrators can
  use this to enforce a TTL policy for finished jobs.
* Use a
  [mutating admission webhook](/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook)
  to set this field dynamically after the Job has finished, and choose
  different TTL values based on job status, labels. For this case, the webhook needs
  to detect changes to the `.status` of the Job and only set a TTL when the Job
  is being marked as completed.
* Write your own controller to manage the cleanup TTL for Jobs that match a particular
  [selector](/docs/concepts/overview/working-with-objects/labels/ "Allows users to filter a list of resources based on labels.").

## Caveats

### Updating TTL for finished Jobs

You can modify the TTL period, e.g. `.spec.ttlSecondsAfterFinished` field of Jobs,
after the job is created or has finished. If you extend the TTL period after the
existing `ttlSecondsAfterFinished` period has expired, Kubernetes doesn't guarantee
to retain that Job, even if an update to extend the TTL returns a successful API
response.

### Time skew

Because the TTL-after-finished controller uses timestamps stored in the Kubernetes jobs to
determine whether the TTL has expired or not, this feature is sensitive to time
skew in your cluster, which may cause the control plane to clean up Job objects
at the wrong time.

Clocks aren't always correct, but the difference should be
very small. Please be aware of this risk when setting a non-zero TTL.

## What's next

* Read [Clean up Jobs automatically](/docs/concepts/workloads/controllers/job/#clean-up-finished-jobs-automatically)
* Refer to the [Kubernetes Enhancement Proposal](https://github.com/kubernetes/enhancements/blob/master/keps/sig-apps/592-ttl-after-finish/README.md)
  (KEP) for adding this mechanism.

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
