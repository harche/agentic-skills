# Contributing new content

This section contains information you should know before contributing new
content.

There are also dedicated pages about submitting [case studies](/docs/contribute/new-content/case-studies/)
and [blog articles](/docs/contribute/blog/).

## New content task flow

```
flowchart LR
    subgraph second[Before you begin]
    direction TB
    S[ ] -.-
    A[Sign the CNCF CLA] --> B[Choose Git branch]
    B --> C[One language per PR]
    C --> F[Check out
contributor tools]
    end
    subgraph first[Contributing Basics]
    direction TB
       T[ ] -.-
       D[Write docs in markdown
and build site with Hugo] --- E[source in GitHub]
       E --- G['/content/../docs' folder contains docs
for multiple languages]
       G --- H[Review Hugo page content
types and shortcodes]
    end

    first ----> second

classDef grey fill:#dddddd,stroke:#ffffff,stroke-width:px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:px,color:#000,font-weight:bold
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
class A,B,C,D,E,F,G,H grey
class S,T spacewhite
class first,second white
```

***Figure - Contributing new content preparation***

The figure above depicts the information you should know
prior to submitting new content. The information details follow.

## Contributing basics

* Write Kubernetes documentation in Markdown and build the Kubernetes site
  using [Hugo](https://gohugo.io/).
* Kubernetes documentation uses [CommonMark](https://commonmark.org/) as its flavor of Markdown.
* The source is in [GitHub](https://github.com/kubernetes/website). You can find
  Kubernetes documentation at `/content/en/docs/`. Some of the reference
  documentation is automatically generated from scripts in
  the `update-imported-docs/` directory.
* [Page content types](/docs/contribute/style/page-content-types/) describe the
  presentation of documentation content in Hugo.
* You can use [Docsy shortcodes](https://www.docsy.dev/docs/adding-content/shortcodes/) or [custom Hugo shortcodes](/docs/contribute/style/hugo-shortcodes/) to contribute to Kubernetes documentation.
* In addition to the standard Hugo shortcodes, we use a number of
  [custom Hugo shortcodes](/docs/contribute/style/hugo-shortcodes/) in our
  documentation to control the presentation of content.
* Documentation source is available in multiple languages in `/content/`. Each
  language has its own folder with a two-letter code determined by the
  [ISO 639-1 standard](https://www.loc.gov/standards/iso639-2/php/code_list.php)
  . For example, English documentation source is stored in `/content/en/docs/`.
* For more information about contributing to documentation in multiple languages
  or starting a new translation,
  see [localization](/docs/contribute/localization/).

## Before you begin

### Sign the CNCF CLA

All Kubernetes contributors **must** read
the [Contributor guide](https://github.com/kubernetes/community/blob/master/contributors/guide/README.md)
and [sign the Contributor License Agreement (CLA)](https://github.com/kubernetes/community/blob/master/CLA.md)
.

Pull requests from contributors who haven't signed the CLA fail the automated
tests. The name and email you provide must match those found in
your `git config`, and your git name and email must match those used for the
CNCF CLA.

### Choose which Git branch to use

When opening a pull request, you need to know in advance which branch to base
your work on.

| Scenario | Branch |
| --- | --- |
| Existing or new English language content for the current release | `main` |
| Content for a feature change release | The branch which corresponds to the major and minor version the feature change is in, using the pattern `dev-<version>`. For example, if a feature changes in the `v1.37` release, then add documentation changes to the `dev-1.37` branch. |
| Content in other languages (localizations) | Use the localization's convention. See the [Localization branching strategy](/docs/contribute/localization/#branch-strategy) for more information. |

If you're still not sure which branch to choose, ask in `#sig-docs` on Slack.

> **Note:**
> If you already submitted your pull request and you know that the
> base branch was wrong, you (and only you, the submitter) can change it.

### Languages per PR

Limit pull requests to one language per PR. If you need to make an identical
change to the same code sample in multiple languages, open a separate PR for
each language.

## Tools for contributors

The [doc contributors tools](https://github.com/kubernetes/website/tree/main/content/en/docs/doc-contributor-tools)
directory in the `kubernetes/website` repository contains tools to help your
contribution journey go more smoothly.

## What's next

* Read about submitting [blog articles](/docs/contribute/blog/article-submission/).

* [Opening a pull request](/docs/contribute/new-content/open-a-pr/)
* [Documenting a feature for a release](/docs/contribute/new-content/new-features/)
* [Submitting case studies](/docs/contribute/new-content/case-studies/)

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
