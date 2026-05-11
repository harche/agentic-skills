# Install and Set Up kubectl on Linux

## Before you begin

You must use a kubectl version that is within one minor version difference of
your cluster. For example, a v1.34 client can communicate
with v1.33, v1.34,
and v1.35 control planes.
Using the latest compatible version of kubectl helps avoid unforeseen issues.

## Install kubectl on Linux

The following methods exist for installing kubectl on Linux:

* [Install kubectl binary with curl on Linux](#install-kubectl-binary-with-curl-on-linux)
* [Install using native package management](#install-using-native-package-management)
* [Install using other package management](#install-using-other-package-management)

### Install kubectl binary with curl on Linux

1. Download the latest release with the command:

   * x86-64
     * ARM64

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
   ```

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl"
   ```

   > **Note:**
   > To download a specific version, replace the `$(curl -L -s https://dl.k8s.io/release/stable.txt)`
   > portion of the command with the specific version.
   >
   > For example, to download version 1.34.0 on Linux x86-64, type:
   >
   > ```
   > curl -LO https://dl.k8s.io/release/v1.34.0/bin/linux/amd64/kubectl
   > ```
   >
   > And for Linux ARM64, type:
   >
   > ```
   > curl -LO https://dl.k8s.io/release/v1.34.0/bin/linux/arm64/kubectl
   > ```
2. Validate the binary (optional)

   Download the kubectl checksum file:

   * x86-64
     * ARM64

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
   ```

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl.sha256"
   ```

   Validate the kubectl binary against the checksum file:

   ```
   echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
   ```

   If valid, the output is:

   ```
   kubectl: OK
   ```

   If the check fails, `sha256` exits with nonzero status and prints output similar to:

   ```
   kubectl: FAILED
   sha256sum: WARNING: 1 computed checksum did NOT match
   ```

   > **Note:**
   > Download the same version of the binary and checksum.
3. Install kubectl

   ```
   sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
   ```

   > **Note:**
   > If you do not have root access on the target system, you can still install
   > kubectl to the `~/.local/bin` directory:
   >
   > ```
   > chmod +x kubectl
   > mkdir -p ~/.local/bin
   > mv ./kubectl ~/.local/bin/kubectl
   > # and then append (or prepend) ~/.local/bin to $PATH
   > ```
4. Test to ensure the version you installed is up-to-date:

   ```
   kubectl version --client
   ```

   Or use this for detailed view of version:

   ```
   kubectl version --client --output=yaml
   ```

### Install using native package management

* Debian-based distributions
  * Red Hat-based distributions
    * SUSE-based distributions

1. Update the `apt` package index and install packages needed to use the Kubernetes `apt` repository:

   ```
   sudo apt-get update
   # apt-transport-https may be a dummy package; if so, you can skip that package
   sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
   ```
2. Download the public signing key for the Kubernetes package repositories. The same signing key is used for all repositories so you can disregard the version in the URL:

   ```
   # If the folder `/etc/apt/keyrings` does not exist, it should be created before the curl command, read the note below.
   # sudo mkdir -p -m 755 /etc/apt/keyrings
   curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.34/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
   sudo chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg # allow unprivileged APT programs to read this keyring
   ```

> **Note:**
> In releases older than Debian 12 and Ubuntu 22.04, folder `/etc/apt/keyrings` does not exist by default, and it should be created before the curl command.

3. Add the appropriate Kubernetes `apt` repository. If you want to use Kubernetes version different than v1.34,
   replace v1.34 with the desired minor version in the command below:

   ```
   # This overwrites any existing configuration in /etc/apt/sources.list.d/kubernetes.list
   echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.34/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
   sudo chmod 644 /etc/apt/sources.list.d/kubernetes.list   # helps tools such as command-not-found to work correctly
   ```

> **Note:**
> To upgrade kubectl to another minor release, you'll need to bump the version in `/etc/apt/sources.list.d/kubernetes.list` before running `apt-get update` and `apt-get upgrade`. This procedure is described in more detail in [Changing The Kubernetes Package Repository](/docs/tasks/administer-cluster/kubeadm/change-package-repository/).

4. Update `apt` package index, then install kubectl:

   ```
   sudo apt-get update
   sudo apt-get install -y kubectl
   ```

1. Add the Kubernetes `yum` repository. If you want to use Kubernetes version
   different than v1.34, replace v1.34 with
   the desired minor version in the command below.

   ```
   # This overwrites any existing configuration in /etc/yum.repos.d/kubernetes.repo
   cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
   [kubernetes]
   name=Kubernetes
   baseurl=https://pkgs.k8s.io/core:/stable:/v1.34/rpm/
   enabled=1
   gpgcheck=1
   gpgkey=https://pkgs.k8s.io/core:/stable:/v1.34/rpm/repodata/repomd.xml.key
   EOF
   ```

> **Note:**
> To upgrade kubectl to another minor release, you'll need to bump the version in `/etc/yum.repos.d/kubernetes.repo` before running `yum update`. This procedure is described in more detail in [Changing The Kubernetes Package Repository](/docs/tasks/administer-cluster/kubeadm/change-package-repository/).

2. Install kubectl using `yum`:

   ```
   sudo yum install -y kubectl
   ```

1. Add the Kubernetes `zypper` repository. If you want to use Kubernetes version
   different than v1.34, replace v1.34 with
   the desired minor version in the command below.

   ```
   # This overwrites any existing configuration in /etc/zypp/repos.d/kubernetes.repo
   cat <<EOF | sudo tee /etc/zypp/repos.d/kubernetes.repo
   [kubernetes]
   name=Kubernetes
   baseurl=https://pkgs.k8s.io/core:/stable:/v1.34/rpm/
   enabled=1
   gpgcheck=1
   gpgkey=https://pkgs.k8s.io/core:/stable:/v1.34/rpm/repodata/repomd.xml.key
   EOF
   ```

> **Note:**
> To upgrade kubectl to another minor release, you'll need to bump the version in `/etc/zypp/repos.d/kubernetes.repo`
> before running `zypper update`. This procedure is described in more detail in
> [Changing The Kubernetes Package Repository](/docs/tasks/administer-cluster/kubeadm/change-package-repository/).

2. Update `zypper` and confirm the new repo addition:

   ```
   sudo zypper update
   ```

   When this message appears, press 't' or 'a':

   ```
   New repository or package signing key received:

   Repository:       Kubernetes
   Key Fingerprint:  1111 2222 3333 4444 5555 6666 7777 8888 9999 AAAA
   Key Name:         isv:kubernetes OBS Project <isv:kubernetes@build.opensuse.org>
   Key Algorithm:    RSA 2048
   Key Created:      Thu 25 Aug 2022 01:21:11 PM -03
   Key Expires:      Sat 02 Nov 2024 01:21:11 PM -03 (expires in 85 days)
   Rpm Name:         gpg-pubkey-9a296436-6307a177

   Note: Signing data enables the recipient to verify that no modifications occurred after the data
   were signed. Accepting data with no, wrong or unknown signature can lead to a corrupted system
   and in extreme cases even to a system compromise.

   Note: A GPG pubkey is clearly identified by its fingerprint. Do not rely on the key's name. If
   you are not sure whether the presented key is authentic, ask the repository provider or check
   their web site. Many providers maintain a web page showing the fingerprints of the GPG keys they
   are using.

   Do you want to reject the key, trust temporarily, or trust always? [r/t/a/?] (r): a
   ```
3. Install kubectl using `zypper`:

   ```
   sudo zypper install -y kubectl
   ```

### Install using other package management

* Snap
  * Homebrew

If you are on Ubuntu or another Linux distribution that supports the
[snap](https://snapcraft.io/docs/core/install) package manager, kubectl
is available as a [snap](https://snapcraft.io/) application.

```
snap install kubectl --classic
kubectl version --client
```

If you are on Linux and using [Homebrew](https://docs.brew.sh/Homebrew-on-Linux)
package manager, kubectl is available for [installation](https://docs.brew.sh/Homebrew-on-Linux#install).

```
brew install kubectl
kubectl version --client
```

## Verify kubectl configuration

In order for kubectl to find and access a Kubernetes cluster, it needs a
[kubeconfig file](/docs/concepts/configuration/organize-cluster-access-kubeconfig/),
which is created automatically when you create a cluster using
[kube-up.sh](https://github.com/kubernetes/kubernetes/blob/master/cluster/kube-up.sh)
or successfully deploy a Minikube cluster.
By default, kubectl configuration is located at `~/.kube/config`.

Check that kubectl is properly configured by getting the cluster state:

```
kubectl cluster-info
```

If you see a URL response, kubectl is correctly configured to access your cluster.

If you see a message similar to the following, kubectl is not configured correctly
or is not able to connect to a Kubernetes cluster.

```
The connection to the server <server-name:port> was refused - did you specify the right host or port?
```

For example, if you are intending to run a Kubernetes cluster on your laptop (locally),
you will need a tool like [Minikube](https://minikube.sigs.k8s.io/docs/start/) to be
installed first and then re-run the commands stated above.

If `kubectl cluster-info` returns the url response, but you can't access your cluster,
check whether it is configured properly using the following command:

```
kubectl cluster-info dump
```

### Troubleshooting the 'No Auth Provider Found' error message

In Kubernetes 1.26, kubectl removed the built-in authentication for the following cloud
providers' managed Kubernetes offerings. These providers have released kubectl plugins
to provide the cloud-specific authentication. For instructions, refer to the following provider documentation:

* Azure AKS: [kubelogin plugin](https://azure.github.io/kubelogin/)
* Google Kubernetes Engine: [gke-gcloud-auth-plugin](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin)

There could also be other causes for the same error message that are unrelated
to that change.

## Optional kubectl configurations and plugins

### Enable shell autocompletion

kubectl provides autocompletion support for Bash, Zsh, Fish, and PowerShell,
which can save you a lot of typing.

Below are the procedures to set up autocompletion for Bash, Fish, and Zsh.

* Bash
  * Fish
    * Zsh

### Introduction

The kubectl completion script for Bash can be generated with the command `kubectl completion bash`.
Sourcing the completion script in your shell enables kubectl autocompletion.

However, the completion script depends on
[**bash-completion**](https://github.com/scop/bash-completion),
which means that you have to install this software first
(you can test if you have bash-completion already installed by running `type _init_completion`).

### Install bash-completion

bash-completion is provided by many package managers
(see [here](https://github.com/scop/bash-completion#installation)).
You can install it with `apt-get install bash-completion` or `yum install bash-completion`, etc.

The above commands create `/usr/share/bash-completion/bash_completion`,
which is the main script of bash-completion. Depending on your package manager,
you have to manually source this file in your `~/.bashrc` file.

To find out, reload your shell and run `type _init_completion`.
If the command succeeds, you're already set, otherwise add the following to your `~/.bashrc` file:

```
source /usr/share/bash-completion/bash_completion
```

Reload your shell and verify that bash-completion is correctly installed by typing `type _init_completion`.

### Enable kubectl autocompletion

#### Bash

You now need to ensure that the kubectl completion script gets sourced in all
your shell sessions. There are two ways in which you can do this:

* User
  * System

```
echo 'source <(kubectl completion bash)' >>~/.bashrc
```

```
kubectl completion bash | sudo tee /etc/bash_completion.d/kubectl > /dev/null
sudo chmod a+r /etc/bash_completion.d/kubectl
```

If you have an alias for kubectl, you can extend shell completion to work with that alias:

```
echo 'alias k=kubectl' >>~/.bashrc
echo 'complete -o default -F __start_kubectl k' >>~/.bashrc
```

> **Note:**
> bash-completion sources all completion scripts in `/etc/bash_completion.d`.

Both approaches are equivalent. After reloading your shell, kubectl autocompletion should be working.
To enable bash autocompletion in current session of shell, source the ~/.bashrc file:

```
source ~/.bashrc
```

> **Note:**
> Autocomplete for Fish requires kubectl 1.23 or later.

The kubectl completion script for Fish can be generated with the command `kubectl completion fish`. Sourcing the completion script in your shell enables kubectl autocompletion.

To do so in all your shell sessions, add the following line to your `~/.config/fish/config.fish` file:

```
kubectl completion fish | source
```

After reloading your shell, kubectl autocompletion should be working.

The kubectl completion script for Zsh can be generated with the command `kubectl completion zsh`. Sourcing the completion script in your shell enables kubectl autocompletion.

To do so in all your shell sessions, add the following to your `~/.zshrc` file:

```
source <(kubectl completion zsh)
```

If you have an alias for kubectl, kubectl autocompletion will automatically work with it.

After reloading your shell, kubectl autocompletion should be working.

If you get an error like `2: command not found: compdef`, then add the following to the beginning of your `~/.zshrc` file:

```
autoload -Uz compinit
compinit
```

### Configure kuberc

See [kuberc](/docs/reference/kubectl/kuberc/) for more information.

### Install `kubectl convert` plugin

A plugin for Kubernetes command-line tool `kubectl`, which allows you to convert manifests between different API
versions. This can be particularly helpful to migrate manifests to a non-deprecated api version with newer Kubernetes release.
For more info, visit [migrate to non deprecated apis](/docs/reference/using-api/deprecation-guide/#migrate-to-non-deprecated-apis)

1. Download the latest release with the command:

   * x86-64
     * ARM64

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl-convert"
   ```

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl-convert"
   ```
2. Validate the binary (optional)

   Download the kubectl-convert checksum file:

   * x86-64
     * ARM64

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl-convert.sha256"
   ```

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl-convert.sha256"
   ```

   Validate the kubectl-convert binary against the checksum file:

   ```
   echo "$(cat kubectl-convert.sha256) kubectl-convert" | sha256sum --check
   ```

   If valid, the output is:

   ```
   kubectl-convert: OK
   ```

   If the check fails, `sha256` exits with nonzero status and prints output similar to:

   ```
   kubectl-convert: FAILED
   sha256sum: WARNING: 1 computed checksum did NOT match
   ```

   > **Note:**
   > Download the same version of the binary and checksum.
3. Install kubectl-convert

   ```
   sudo install -o root -g root -m 0755 kubectl-convert /usr/local/bin/kubectl-convert
   ```
4. Verify plugin is successfully installed

   ```
   kubectl convert --help
   ```

   If you do not see an error, it means the plugin is successfully installed.
5. After installing the plugin, clean up the installation files:

   ```
   rm kubectl-convert kubectl-convert.sha256
   ```

## What's next

* [Install Minikube](https://minikube.sigs.k8s.io/docs/start/)
* See the [getting started guides](/docs/setup/) for more about creating clusters.
* [Learn how to launch and expose your application.](/docs/tasks/access-application-cluster/service-access-application-cluster/)
* If you need access to a cluster you didn't create, see the
  [Sharing Cluster Access document](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/).
* Read the [kubectl reference docs](/docs/reference/kubectl/kubectl/)

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
