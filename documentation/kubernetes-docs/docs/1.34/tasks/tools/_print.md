This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/tasks/tools/).

# Install Tools

Set up Kubernetes tools on your computer.

* 1: [Install and Set Up kubectl on Linux](#pg-37b6179f23c8ad977cb9daa6d2da748a)
* 2: [Install and Set Up kubectl on macOS](#pg-961fc70b732cb8df4fd11a3463b6545c)
* 3: [Install and Set Up kubectl on Windows](#pg-2cc93d3011d707aeb6564bab02048f7a)

## kubectl

The Kubernetes command-line tool, [kubectl](/docs/reference/kubectl/kubectl/), allows
you to run commands against Kubernetes clusters.
You can use kubectl to deploy applications, inspect and manage cluster resources,
and view logs. For more information including a complete list of kubectl operations, see the
[`kubectl` reference documentation](/docs/reference/kubectl/).

kubectl is installable on a variety of Linux platforms, macOS and Windows.
Find your preferred operating system below.

* [Install kubectl on Linux](/docs/tasks/tools/install-kubectl-linux/)
* [Install kubectl on macOS](/docs/tasks/tools/install-kubectl-macos/)
* [Install kubectl on Windows](/docs/tasks/tools/install-kubectl-windows/)

## kind

[`kind`](https://kind.sigs.k8s.io/) lets you run Kubernetes on
your local computer. This tool requires that you have either
[Docker](https://www.docker.com/) or [Podman](https://podman.io/) installed.

The kind [Quick Start](https://kind.sigs.k8s.io/docs/user/quick-start/) page
shows you what you need to do to get up and running with kind.

[View kind Quick Start Guide](https://kind.sigs.k8s.io/docs/user/quick-start/)

## minikube

Like `kind`, [`minikube`](https://minikube.sigs.k8s.io/) is a tool that lets you run Kubernetes
locally. `minikube` runs an all-in-one or a multi-node local Kubernetes cluster on your personal
computer (including Windows, macOS and Linux PCs) so that you can try out
Kubernetes, or for daily development work.

You can follow the official
[Get Started!](https://minikube.sigs.k8s.io/docs/start/) guide if your focus is
on getting the tool installed.

[View minikube Get Started! Guide](https://minikube.sigs.k8s.io/docs/start/)

Once you have `minikube` working, you can use it to
[run a sample application](/docs/tutorials/hello-minikube/).

## kubeadm

You can use the [kubeadm](/docs/reference/setup-tools/kubeadm/ "A tool for quickly installing Kubernetes and setting up a secure cluster.") tool to create and manage Kubernetes clusters.
It performs the actions necessary to get a minimum viable, secure cluster up and running in a user friendly way.

[Installing kubeadm](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/) shows you how to install kubeadm.
Once installed, you can use it to [create a cluster](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/).

[View kubeadm Install Guide](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
