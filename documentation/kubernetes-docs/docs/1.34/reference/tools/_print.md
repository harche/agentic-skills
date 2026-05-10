This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/reference/tools/).

# Other Tools

Kubernetes contains several tools to help you work with the Kubernetes system.

## crictl

[`crictl`](https://github.com/kubernetes-sigs/cri-tools) is a command-line
interface for inspecting and debugging [CRI](/docs/concepts/architecture/cri "Protocol for communication between the kubelet and the local container runtime.")-compatible
container runtimes.

## Dashboard

[`Dashboard`](/docs/tasks/access-application-cluster/web-ui-dashboard/), the web-based user interface of Kubernetes, allows you to deploy containerized applications
to a Kubernetes cluster, troubleshoot them, and manage the cluster and its
resources itself.

## Helm

> **Note:**
> 🛇 This item links to a third party project or product that is not part of Kubernetes itself. [More information](#third-party-content-disclaimer)

[Helm](https://helm.sh/) is a tool for managing packages of pre-configured
Kubernetes resources. These packages are known as *Helm charts*.

Use Helm to:

* Find and use popular software packaged as Kubernetes charts
* Share your own applications as Kubernetes charts
* Create reproducible builds of your Kubernetes applications
* Intelligently manage your Kubernetes manifest files
* Manage releases of Helm packages

## Kompose

[`Kompose`](https://github.com/kubernetes/kompose) is a tool to help Docker Compose users move to Kubernetes.

Use Kompose to:

* Translate a Docker Compose file into Kubernetes objects
* Go from local Docker development to managing your application via Kubernetes
* Convert v1 or v2 Docker Compose `yaml` files or [Distributed Application Bundles](https://docs.docker.com/compose/bundles/)

## Kui

[`Kui`](https://github.com/kubernetes-sigs/kui) is a GUI tool that takes your normal
`kubectl` command line requests and responds with graphics.

Kui takes the normal `kubectl` command line requests and responds with graphics. Instead
of ASCII tables, Kui provides a GUI rendering with tables that you can sort.

Kui lets you:

* Directly click on long, auto-generated resource names instead of copying and pasting
* Type in `kubectl` commands and see them execute, even sometimes faster than `kubectl` itself
* Query a [Job](/docs/concepts/workloads/controllers/job/ "A finite or batch task that runs to completion.") and see its execution rendered
  as a waterfall diagram
* Click through resources in your cluster using a tabbed UI

## Minikube

[`minikube`](https://minikube.sigs.k8s.io/docs/) is a tool that
runs a single-node Kubernetes cluster locally on your workstation for
development and testing purposes.
