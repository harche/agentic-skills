# Contributing to Kubernetes blogs

There are two official Kubernetes blogs, and the CNCF has [its own blog](https://www.cncf.io/blog/) where you can cover Kubernetes too.
For the main Kubernetes blog, we (the Kubernetes project) like to publish articles with different perspectives and special focuses, that have a link to Kubernetes.

With only a few special case exceptions, we only publish content that hasn't been submitted or published anywhere else.

Read the [blog guidelines](/docs/contribute/blog/guidelines/#what-we-publish) for more about that aspect.

## Official Kubernetes blogs

### Main blog

The main [Kubernetes blog](/blog/) is used by the project to communicate new features, community reports, and any
news that might be relevant to the Kubernetes community. This includes end users and developers.
Most of the blog's content is about things happening in the core project, but Kubernetes
as a project encourages you to submit about things happening elsewhere in the ecosystem too!

Anyone can write a blog post and submit it for publication. With only a few special case exceptions, we only publish content that hasn't been submitted or published anywhere else.

### Contributor blog

The [Kubernetes contributor blog](https://k8s.dev/blog/) is aimed at an audience of people who
work **on** Kubernetes more than people who work **with** Kubernetes. The Kubernetes project
deliberately publishes some articles to both blogs.

Anyone can write a blog post and submit it for review.

## Article updates and maintenance

The Kubernetes project does not maintain older articles for its blogs. This means that any
published article more than one year old will normally **not** be eligible for issues or pull
requests that ask for changes. To avoid establishing precedent, even technically correct pull
requests are likely to be rejected.

However, there are exceptions like the following:

* (updates to) articles marked as [evergreen](#maintenance-evergreen)
* removing or correcting articles giving advice that is now wrong and dangerous to follow
* fixes to ensure that an existing article still renders correctly

For any article that is over a year old and not marked as *evergreen*, the website automatically
displays a notice that the content may be stale.

### Evergreen articles

You can mark an article as evergreen by setting `evergreen: true` in the front matter.

We only mark blog articles as maintained (`evergreen: true` in front matter) if the Kubernetes project
can commit to maintaining them indefinitely. Some blog articles absolutely merit this; for example, the release comms team always marks official release announcements as evergreen.

## What's next

* Discover the official blogs:

  + [Kubernetes blog](/blog/)
  + [Kubernetes contributor blog](https://k8s.dev/blog/)
* Read about [reviewing blog pull requests](/docs/contribute/review/reviewing-prs/#blog)

* [Submitting articles to Kubernetes blogs](/docs/contribute/blog/article-submission/)
* [Blog guidelines](/docs/contribute/blog/guidelines/)
* [Blog article mirroring](/docs/contribute/blog/article-mirroring/)
* [Post-release communications](/docs/contribute/blog/release-comms/)
* [Helping as a blog writing buddy](/docs/contribute/blog/writing-buddy/)

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
