# Issue Wranglers

Alongside the [PR Wrangler](/docs/contribute/participate/pr-wranglers/), formal approvers,
reviewers and members of SIG Docs take week-long shifts
[triaging and categorising issues](/docs/contribute/review/for-approvers/#triage-and-categorize-issues)
for the repository.

## Duties

Each day in a week-long shift the Issue Wrangler will be responsible for:

* Triaging and tagging incoming issues daily. See
  [Triage and categorize issues](/docs/contribute/review/for-approvers/#triage-and-categorize-issues)
  for guidelines on how SIG Docs uses metadata.
* Keeping an eye on stale & rotten issues within the kubernetes/website repository.
* Maintenance of the [Issues board](https://github.com/orgs/kubernetes/projects/72/views/1).

## Requirements

* Must be an active member of the Kubernetes organization.
* A minimum of 15 [non-trivial](https://www.kubernetes.dev/docs/guide/pull-requests/#trivial-edits)
  contributions to Kubernetes (of which a certain amount should be directed towards kubernetes/website).
* Performing the role in an informal capacity already.

## Helpful Prow commands for wranglers

Below are some commonly used commands for Issue Wranglers:

```
# reopen an issue
/reopen

# transfer issues that don't fit in k/website to another repository
/transfer[-issue]

# change the state of rotten issues
/remove-lifecycle rotten

# change the state of stale issues
/remove-lifecycle stale

# assign sig to an issue
/sig <sig_name>

# add specific area
/area <area_name>

# for beginner friendly issues
/good-first-issue

# issues that needs help
/help wanted

# tagging issue as support specific
/kind support

# to accept triaging for an issue
/triage accepted

# closing an issue we won't be working on and haven't fixed yet
/close not-planned
```

To find more Prow commands, refer to the [Command Help](https://prow.k8s.io/command-help) documentation.

## When to close Issues

For an open source project to succeed, good issue management is crucial.
But it is also critical to resolve issues in order to maintain the repository
and communicate clearly with contributors and users.

Close issues when:

* A similar issue is reported more than once. You will first need to tag it as `/triage duplicate`;
  link it to the main issue & then close it. It is also advisable to direct the users to the original issue.
* It is very difficult to understand and address the issue presented by the author with the information provided.
  However, encourage the user to provide more details or reopen the issue if they can reproduce it later.
* The same functionality is implemented elsewhere. One can close this issue and direct user to the appropriate place.
* The reported issue is not currently planned or aligned with the project's goals.
* If the issue appears to be spam and is clearly unrelated.
* If the issue is related to an external limitation or dependency and is beyond the control of the project.

To close an issue, leave a `/close` comment on the issue.

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
