# Generating Reference Documentation for the Kubernetes API

This page shows how to update the Kubernetes API reference documentation.

The Kubernetes API reference documentation is built from the
[Kubernetes OpenAPI spec](https://github.com/kubernetes/kubernetes/blob/master/api/openapi-spec/swagger.json)
using the [kubernetes-sigs/reference-docs](https://github.com/kubernetes-sigs/reference-docs) generation code.

If you find bugs in the generated documentation, you need to
[fix them upstream](/docs/contribute/generate-ref-docs/contribute-upstream/).

If you need only to regenerate the reference documentation from the
[OpenAPI](https://github.com/OAI/OpenAPI-Specification)
spec, continue reading this page.

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

## Set up the local repositories

Create a local workspace and set your `GOPATH`:

```
mkdir -p $HOME/<workspace>

export GOPATH=$HOME/<workspace>
```

Get a local clone of the following repositories:

```
git clone github.com/kubernetes-sigs/reference-docs
```

Move into the `gen-apidocs` directory of the `reference-docs` repository and install the required Go packages:

```
go get -u github.com/go-openapi/loads
go get -u github.com/go-openapi/spec
```

If you don't already have the kubernetes/website repository, get it now:

```
git clone https://github.com/<your-username>/website
```

Get a clone of the kubernetes/kubernetes repository:

```
git clone https://github.com/kubernetes/kubernetes
```

* The base directory of your clone of the
  [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) repository is
  `<your-path-to>/kubernetes/kubernetes.`
  The remaining steps refer to your base directory as `<k8s-base>`.
* The base directory of your clone of the
  [kubernetes/website](https://github.com/kubernetes/website) repository is
  `<your-path-to>/website`.
  The remaining steps refer to your base directory as `<web-base>`.
* The base directory of your clone of the
  [kubernetes-sigs/reference-docs](https://github.com/kubernetes-sigs/reference-docs)
  repository is `<your-path-to>/reference-docs`.
  The remaining steps refer to your base directory as `<rdocs-base>`.

## Generate the API reference docs

This section shows how to generate the
[published Kubernetes API reference documentation](/docs/reference/generated/kubernetes-api/v1.34/).

### Set build variables

* Set `K8S_ROOT` to `<k8s-base>`.
* Set `K8S_WEBROOT` to `<web-base>`.
* Set `K8S_RELEASE` to the version of the docs you want to build.
  For example, if you want to build docs for Kubernetes 1.17.0, set `K8S_RELEASE` to 1.17.0.

For example:

```
export K8S_WEBROOT=<your-path-to>/website
export K8S_ROOT=<your-path-to>/kubernetes
export K8S_RELEASE=1.17.0
```

### Create versioned directory and fetch Open API spec

The `updateapispec` build target creates the versioned build directory.
After the directory is created, the Open API spec is fetched from the
`<k8s-base>` repository. These steps ensure that the version
of the configuration files and Kubernetes Open API spec match the release version.
The versioned directory name follows the pattern of `v<major>_<minor>`.

In the `<rdocs-base>` directory, run the following build target:

```
cd <rdocs-base>
make updateapispec
```

### Build the API reference docs

The `copyapi` target builds the API reference and
copies the generated files to directories in `<web-base>`.
Run the following command in `<rdocs-base>`:

```
cd <rdocs-base>
make copyapi
```

Verify that these two files have been generated:

```
[ -e "<rdocs-base>/gen-apidocs/build/index.html" ] && echo "index.html built" || echo "no index.html"
[ -e "<rdocs-base>/gen-apidocs/build/navData.js" ] && echo "navData.js built" || echo "no navData.js"
```

Go to the base of your local `<web-base>`, and
view which files have been modified:

```
cd <web-base>
git status
```

The output is similar to:

```
static/docs/reference/generated/kubernetes-api/v1.34/css/bootstrap.min.css
static/docs/reference/generated/kubernetes-api/v1.34/css/font-awesome.min.css
static/docs/reference/generated/kubernetes-api/v1.34/css/stylesheet.css
static/docs/reference/generated/kubernetes-api/v1.34/fonts/FontAwesome.otf
static/docs/reference/generated/kubernetes-api/v1.34/fonts/fontawesome-webfont.eot
static/docs/reference/generated/kubernetes-api/v1.34/fonts/fontawesome-webfont.svg
static/docs/reference/generated/kubernetes-api/v1.34/fonts/fontawesome-webfont.ttf
static/docs/reference/generated/kubernetes-api/v1.34/fonts/fontawesome-webfont.woff
static/docs/reference/generated/kubernetes-api/v1.34/fonts/fontawesome-webfont.woff2
static/docs/reference/generated/kubernetes-api/v1.34/index.html
static/docs/reference/generated/kubernetes-api/v1.34/js/jquery.scrollTo.min.js
static/docs/reference/generated/kubernetes-api/v1.34/js/navData.js
static/docs/reference/generated/kubernetes-api/v1.34/js/scroll.js
```

## API reference location and versioning

The generated API reference files (HTML version) are copied to `<web-base>/static/docs/reference/generated/kubernetes-api/v1.34/`. This directory contains the standalone HTML API documentation.

> **Note:**
> The Markdown version of the API reference located at `<web-base>/content/en/docs/reference/kubernetes-api/`
> is generated separately using the [gen-resourcesdocs](https://github.com/kubernetes-sigs/reference-docs/tree/master/gen-resourcesdocs) generator.

## Locally test the API reference

Publish a local version of the API reference.
Verify the [local preview](http://localhost:1313/docs/reference/generated/kubernetes-api/v1.34/).

```
cd <web-base>
git submodule update --init --recursive --depth 1 # if not already done
make container-serve
```

## Commit the changes

In `<web-base>`, run `git add` and `git commit` to commit the change.

Submit your changes as a
[pull request](/docs/contribute/new-content/open-a-pr/) to the
[kubernetes/website](https://github.com/kubernetes/website) repository.
Monitor your pull request, and respond to reviewer comments as needed. Continue
to monitor your pull request until it has been merged.

## What's next

* [Generating Reference Documentation Quickstart](/docs/contribute/generate-ref-docs/quickstart/)
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
