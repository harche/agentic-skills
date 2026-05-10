# Install and Set Up kubectl on macOS

## Before you begin

You must use a kubectl version that is within one minor version difference of
your cluster. For example, a v1.34 client can communicate
with v1.33, v1.34,
and v1.35 control planes.
Using the latest compatible version of kubectl helps avoid unforeseen issues.

## Install kubectl on macOS

The following methods exist for installing kubectl on macOS:

* [Install kubectl on macOS](#install-kubectl-on-macos)
  + [Install kubectl binary with curl on macOS](#install-kubectl-binary-with-curl-on-macos)
  + [Install with Homebrew on macOS](#install-with-homebrew-on-macos)
  + [Install with Macports on macOS](#install-with-macports-on-macos)
* [Verify kubectl configuration](#verify-kubectl-configuration)
* [Optional kubectl configurations and plugins](#optional-kubectl-configurations-and-plugins)
  + [Enable shell autocompletion](#enable-shell-autocompletion)
  + [Install `kubectl convert` plugin](#install-kubectl-convert-plugin)

### Install kubectl binary with curl on macOS

1. Download the latest release:

   * Intel
     * Apple Silicon

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl"
   ```

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl"
   ```

   > **Note:**
   > To download a specific version, replace the `$(curl -L -s https://dl.k8s.io/release/stable.txt)`
   > portion of the command with the specific version.
   >
   > For example, to download version 1.34.0 on Intel macOS, type:
   >
   > ```
   > curl -LO "https://dl.k8s.io/release/v1.34.0/bin/darwin/amd64/kubectl"
   > ```
   >
   > And for macOS on Apple Silicon, type:
   >
   > ```
   > curl -LO "https://dl.k8s.io/release/v1.34.0/bin/darwin/arm64/kubectl"
   > ```
2. Validate the binary (optional)

   Download the kubectl checksum file:

   * Intel
     * Apple Silicon

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl.sha256"
   ```

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl.sha256"
   ```

   Validate the kubectl binary against the checksum file:

   ```
   echo "$(cat kubectl.sha256)  kubectl" | shasum -a 256 --check
   ```

   If valid, the output is:

   ```
   kubectl: OK
   ```

   If the check fails, `shasum` exits with nonzero status and prints output similar to:

   ```
   kubectl: FAILED
   shasum: WARNING: 1 computed checksum did NOT match
   ```

   > **Note:**
   > Download the same version of the binary and checksum.
3. Make the kubectl binary executable.

   ```
   chmod +x ./kubectl
   ```
4. Move the kubectl binary to a file location on your system `PATH`.

   ```
   sudo mv ./kubectl /usr/local/bin/kubectl
   sudo chown root: /usr/local/bin/kubectl
   ```

   > **Note:**
   > Make sure `/usr/local/bin` is in your PATH environment variable.
5. Test to ensure the version you installed is up-to-date:

   ```
   kubectl version --client
   ```

   Or use this for detailed view of version:

   ```
   kubectl version --client --output=yaml
   ```
6. After installing and validating kubectl, delete the checksum file:

   ```
   rm kubectl.sha256
   ```

### Install with Homebrew on macOS

If you are on macOS and using [Homebrew](https://brew.sh/) package manager,
you can install kubectl with Homebrew.

1. Run the installation command:

   ```
   brew install kubectl
   ```

   or

   ```
   brew install kubernetes-cli
   ```
2. Test to ensure the version you installed is up-to-date:

   ```
   kubectl version --client
   ```

### Install with Macports on macOS

If you are on macOS and using [Macports](https://macports.org/) package manager,
you can install kubectl with Macports.

1. Run the installation command:

   ```
   sudo port selfupdate
   sudo port install kubectl
   ```
2. Test to ensure the version you installed is up-to-date:

   ```
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

kubectl provides autocompletion support for Bash, Zsh, Fish, and PowerShell
which can save you a lot of typing.

Below are the procedures to set up autocompletion for Bash, Fish, and Zsh.

* Bash
  * Fish
    * Zsh

### Introduction

The kubectl completion script for Bash can be generated with `kubectl completion bash`.
Sourcing this script in your shell enables kubectl completion.

However, the kubectl completion script depends on
[**bash-completion**](https://github.com/scop/bash-completion) which you thus have to previously install.

> **Warning:**
> There are two versions of bash-completion, v1 and v2. V1 is for Bash 3.2
> (which is the default on macOS), and v2 is for Bash 4.1+. The kubectl completion
> script **doesn't work** correctly with bash-completion v1 and Bash 3.2.
> It requires **bash-completion v2** and **Bash 4.1+**. Thus, to be able to
> correctly use kubectl completion on macOS, you have to install and use
> Bash 4.1+ ([*instructions*](https://apple.stackexchange.com/a/292760)).
> The following instructions assume that you use Bash 4.1+
> (that is, any Bash version of 4.1 or newer).

### Upgrade Bash

The instructions here assume you use Bash 4.1+. You can check your Bash's version by running:

```
echo $BASH_VERSION
```

If it is too old, you can install/upgrade it using Homebrew:

```
brew install bash
```

Reload your shell and verify that the desired version is being used:

```
echo $BASH_VERSION $SHELL
```

Homebrew usually installs it at `/usr/local/bin/bash`.

### Install bash-completion

> **Note:**
> As mentioned, these instructions assume you use Bash 4.1+, which means you will
> install bash-completion v2 (in contrast to Bash 3.2 and bash-completion v1,
> in which case kubectl completion won't work).

You can test if you have bash-completion v2 already installed with `type _init_completion`.
If not, you can install it with Homebrew:

```
brew install bash-completion@2
```

As stated in the output of this command, add the following to your `~/.bash_profile` file:

```
brew_etc="$(brew --prefix)/etc" && [[ -r "${brew_etc}/profile.d/bash_completion.sh" ]] && . "${brew_etc}/profile.d/bash_completion.sh"
```

Reload your shell and verify that bash-completion v2 is correctly installed with `type _init_completion`.

### Enable kubectl autocompletion

You now have to ensure that the kubectl completion script gets sourced in all
your shell sessions. There are multiple ways to achieve this:

* Source the completion script in your `~/.bash_profile` file:

  ```
  echo 'source <(kubectl completion bash)' >>~/.bash_profile
  ```
* Add the completion script to the `/usr/local/etc/bash_completion.d` directory:

  ```
  kubectl completion bash >/usr/local/etc/bash_completion.d/kubectl
  ```
* If you have an alias for kubectl, you can extend shell completion to work with that alias:

  ```
  echo 'alias k=kubectl' >>~/.bash_profile
  echo 'complete -o default -F __start_kubectl k' >>~/.bash_profile
  ```
* If you installed kubectl with Homebrew (as explained
  [here](/docs/tasks/tools/install-kubectl-macos/#install-with-homebrew-on-macos)),
  then the kubectl completion script should already be in `/usr/local/etc/bash_completion.d/kubectl`.
  In that case, you don't need to do anything.

  > **Note:**
  > The Homebrew installation of bash-completion v2 sources all the files in the
  > `BASH_COMPLETION_COMPAT_DIR` directory, that's why the latter two methods work.

In any case, after reloading your shell, kubectl completion should be working.

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

   * Intel
     * Apple Silicon

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl-convert"
   ```

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl-convert"
   ```
2. Validate the binary (optional)

   Download the kubectl-convert checksum file:

   * Intel
     * Apple Silicon

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl-convert.sha256"
   ```

   ```
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl-convert.sha256"
   ```

   Validate the kubectl-convert binary against the checksum file:

   ```
   echo "$(cat kubectl-convert.sha256)  kubectl-convert" | shasum -a 256 --check
   ```

   If valid, the output is:

   ```
   kubectl-convert: OK
   ```

   If the check fails, `shasum` exits with nonzero status and prints output similar to:

   ```
   kubectl-convert: FAILED
   shasum: WARNING: 1 computed checksum did NOT match
   ```

   > **Note:**
   > Download the same version of the binary and checksum.
3. Make kubectl-convert binary executable

   ```
   chmod +x ./kubectl-convert
   ```
4. Move the kubectl-convert binary to a file location on your system `PATH`.

   ```
   sudo mv ./kubectl-convert /usr/local/bin/kubectl-convert
   sudo chown root: /usr/local/bin/kubectl-convert
   ```

   > **Note:**
   > Make sure `/usr/local/bin` is in your PATH environment variable.
5. Verify plugin is successfully installed

   ```
   kubectl convert --help
   ```

   If you do not see an error, it means the plugin is successfully installed.
6. After installing the plugin, clean up the installation files:

   ```
   rm kubectl-convert kubectl-convert.sha256
   ```

### Uninstall kubectl on macOS

Depending on how you installed `kubectl`, use one of the following methods.

### Uninstall kubectl using the command-line

1. Locate the `kubectl` binary on your system:

   ```
   which kubectl
   ```
2. Remove the `kubectl` binary:

   ```
   sudo rm <path>
   ```

   Replace `<path>` with the path to the `kubectl` binary from the previous step. For example, `sudo rm /usr/local/bin/kubectl`.

### Uninstall kubectl using homebrew

If you installed `kubectl` using Homebrew, run the following command:

```
brew remove kubectl
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
