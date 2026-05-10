# Generating Reference Documentation for Metrics

This page demonstrates the generation of metrics reference documentation.

## Before you begin

### Requirements:

* You need a machine that is running Linux or macOS.
* You need to have these tools installed:

  + [Python](https://www.python.org/downloads/) v3.7.x+
  + [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  + [Golang](https://go.dev/dl/) version 1.13+
  + [Pip](https://pypi.org/project/pip/) used to install PyYAML
  + [PyYAML](https://pyyaml.org/) v5.1.2
  + [make](https://www.gnu.org/software/make/)
  + [gcc compiler/linker](https://gcc.gnu.org/)
  + [Docker](https://docs.docker.com/engine/installation/) (Required only for `kubectl` command reference)
* Your `PATH` environment variable must include the required build tools, such as the `Go` binary and `python`.
* You need to know how to create a pull request to a GitHub repository.
  This involves creating your own fork of the repository. For more
  information, see [Work from a local clone](/docs/contribute/new-content/open-a-pr/#fork-the-repo).

## Clone the Kubernetes repository

The metric generation happens in the Kubernetes repository.
To clone the repository, change directories to where you want the clone to exist.

Then, execute the following command:

```
git clone https://www.github.com/kubernetes/kubernetes
```

This creates a `kubernetes` folder in your current working directory.

## Generate the metrics

Inside the cloned Kubernetes repository, locate the
`test/instrumentation/documentation` directory.
The metrics documentation is generated in this directory.

With each release, new metrics are added.
After you run the metrics documentation generator script, copy the
metrics documentation to the Kubernetes website and
publish the updated metrics documentation.

To generate the latest metrics, make sure you are in the root of the cloned Kubernetes directory.
Then, execute the following command:

```
./test/instrumentation/update-documentation.sh
```

To check for changes, execute:

```
git status
```

The output is similar to:

```
./test/instrumentation/documentation/documentation.md
./test/instrumentation/documentation/documentation-list.yaml
```

## Copy the generated metrics documentation file to the Kubernetes website repository

1. Set the Kubernetes website root environment variable.

   Execute the following command to set the website root:

   ```
   export WEBSITE_ROOT=<path to website root>
   ```
2. Copy the generated metrics file to the Kubernetes website repository.

   ```
   cp ./test/instrumentation/documentation/documentation.md "${WEBSITE_ROOT}/content/en/docs/reference/instrumentation/metrics.md"
   ```

   > **Note:**
   > If you get an error, check that you have permission to copy the file.
   > You can use `chown` to change the file ownership back to your own user.

## Create a pull request

To create a pull request, follow the instructions in [Opening a pull request](/docs/contribute/new-content/open-a-pr/).

## What's next

* [Contribute-upstream](/docs/contribute/generate-ref-docs/contribute-upstream/)
* [Generating Reference Docs for Kubernetes Components and Tools](/docs/contribute/generate-ref-docs/kubernetes-components/)
* [Generating Reference Documentation for kubectl Commands](/docs/contribute/generate-ref-docs/kubectl/)

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
