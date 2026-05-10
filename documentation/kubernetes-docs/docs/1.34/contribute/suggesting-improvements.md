# Suggesting content improvements

If you notice an issue with Kubernetes documentation or have an idea for new content, then open an issue. All you need is a [GitHub account](https://github.com/join) and a web browser.

In most cases, new work on Kubernetes documentation begins with an issue in GitHub. Kubernetes contributors
then review, categorize and tag issues as needed. Next, you or another member
of the Kubernetes community open a pull request with changes to resolve the issue.

## Opening an issue

If you want to suggest improvements to existing content or notice an error, then open an issue.

1. Click the **Create an issue** link on the right sidebar. This redirects you
   to a GitHub issue page pre-populated with some headers.
2. Describe the issue or suggestion for improvement. Provide as many details as you can.
3. Click **Submit new issue**.

After submitting, check in on your issue occasionally or turn on GitHub notifications.
Reviewers and other community members might ask questions before
they can take action on your issue.

## Suggesting new content

If you have an idea for new content, but you aren't sure where it should go, you can
still file an issue. Either:

* Choose an existing page in the section you think the content belongs in and click **Create an issue**.
* Go to [GitHub](https://github.com/kubernetes/website/issues/new/) and file the issue directly.

## How to file great issues

Keep the following in mind when filing an issue:

* Provide a clear issue description. Describe what specifically is missing, out of date,
  wrong, or needs improvement.
* Explain the specific impact the issue has on users.
* Limit the scope of a given issue to a reasonable unit of work. For problems
  with a large scope, break them down into smaller issues. For example, "Fix the security docs"
  is too broad, but "Add details to the 'Restricting network access' topic" is specific enough
  to be actionable.
* Search the existing issues to see if there's anything related or similar to the
  new issue.
* If the new issue relates to another issue or pull request, refer to it
  either by its full URL or by the issue or pull request number prefixed
  with a `#` character. For example, `Introduced by #987654`.
* Follow the [Code of Conduct](/community/code-of-conduct/). Respect your
  fellow contributors. For example, "The docs are terrible" is not
  helpful or polite feedback.

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
