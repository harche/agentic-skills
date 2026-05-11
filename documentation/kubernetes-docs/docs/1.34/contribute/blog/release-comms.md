# Post-release communications

The Kubernetes *Release Comms* team (part of
[SIG Release](https://github.com/kubernetes/community/tree/master/sig-release))
looks after release announcements, which go onto the
[main project blog](/docs/contribute/blog/#main-blog).

After each release, the Release Comms team take over the main blog for a period
and publish a series of additional articles to explain or announce changes related to
that release. These additional articles are termed *post-release comms*.

## Opting in to post-release comms

During a release cycle, as a contributor, you can opt in to post-release comms about an
upcoming change to Kubernetes.

To opt in you open a draft, *placeholder* [pull request](https://www.k8s.dev/docs/guide/pull-requests/) (PR)
against [k/website](https://github.com/kubernetes/website). Initially, this can be an
empty commit. Mention the KEP issue or other Kubernetes improvement issue in the description
of your placeholder PR.

When you open the **draft** pull request, you open it against *main* as the base branch
and not against the `dev-1.37` branch. This is different from
the [process](/docs/contribute/new-content/new-features/#open-a-placeholder-pr) for upcoming release changes and new features.

You should also leave a comment on the related [kubernetes/enhancements](https://github.com/kubernetes/enhancements)
issue with a link to the PR to notify the Release Comms team managing this release. Your comment
helps the team see that the change needs announcing and that your SIG has opted in.

As well as the above, you should ideally contact the Release Comms team via Slack
(channel [`#release-comms`](https://kubernetes.slack.com/archives/CNT9Y603D)) to let them
know that you have done this and would like to opt in.

## Preparing the article content

You should follow the usual [article submission](/docs/contribute/blog/article-submission/)
process to turn your placeholder PR into something ready for review. However, for
post-release comms, you may not have a *writing buddy*; instead, the Release Comms team
may assign a member of the team to help guide what you're doing.

You should [squash](https://www.k8s.dev/docs/guide/pull-requests/#squashing) the commits
in your pull request; if you're not sure how to, it's absolutely OK to ask Release Comms or
the blog team for help.

Provided that your article is flagged as a draft (`draft: true`) in the
[front matter](https://gohugo.io/content-management/front-matter/), the PR can merge at any
time during the release cycle.

## Publication

Ahead of the actual release, the Release Comms team check what content is ready (if it's
not ready by the deadline, and you didn't get an exception, then the announcement won't
be included). They build a schedule for the articles that will go out and open new
pull requests to turn those articles from draft to published.

> **Caution:**
> All these pull requests to actually publish post-release articles **must** be held
> (Prow command `/hold`) until the release has actually happened.

The blog team approvers still provide final sign off on promoting the content from draft
to accepted for publication. Ahead of release day, the PR (or PRs) for publishing these
announcements should have LGTM (“looks good to me”) and approved labels, along with the
**do-not-merge/hold** label to ensure the PR doesn't merge too early.

Release Comms / the Release Team can then *unhold* that PR (or set of PRs) as soon as the
website Git repository is unfrozen after the actual release.

On the day each article is scheduled to publish, automation triggers a website build and that
article becomes visible.

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
