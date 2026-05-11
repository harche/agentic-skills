# Changing the Container Runtime on a Node from Docker Engine to containerd

This task outlines the steps needed to update your container runtime to containerd from Docker. It
is applicable for cluster operators running Kubernetes 1.23 or earlier. This also covers an
example scenario for migrating from dockershim to containerd. Alternative container runtimes
can be picked from this [page](/docs/setup/production-environment/container-runtimes/).

## Before you begin

> **Note:**
> **Note:** This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](/docs/contribute/style/content-guide/#third-party-content) before submitting a change. [More information.](#third-party-content-disclaimer)

Install containerd. For more information see
[containerd's installation documentation](https://containerd.io/docs/getting-started/)
and for specific prerequisite follow
[the containerd guide](/docs/setup/production-environment/container-runtimes/#containerd).

## Drain the node

```
kubectl drain <node-to-drain> --ignore-daemonsets
```

Replace `<node-to-drain>` with the name of your node you are draining.

## Stop the Docker daemon

```
systemctl stop kubelet
systemctl disable docker.service --now
```

## Install Containerd

Follow the [guide](/docs/setup/production-environment/container-runtimes/#containerd)
for detailed steps to install containerd.

* Linux
  * Windows (PowerShell)

1. Install the `containerd.io` package from the official Docker repositories.
   Instructions for setting up the Docker repository for your respective Linux distribution and
   installing the `containerd.io` package can be found at
   [Getting started with containerd](https://github.com/containerd/containerd/blob/main/docs/getting-started.md).
2. Configure containerd:

   ```
   sudo mkdir -p /etc/containerd
   containerd config default | sudo tee /etc/containerd/config.toml
   ```
3. Restart containerd:

   ```
   sudo systemctl restart containerd
   ```

Start a Powershell session, set `$Version` to the desired version (ex: `$Version="1.4.3"`), and
then run the following commands:

1. Download containerd:

   ```
   curl.exe -L https://github.com/containerd/containerd/releases/download/v$Version/containerd-$Version-windows-amd64.tar.gz -o containerd-windows-amd64.tar.gz
   tar.exe xvf .\containerd-windows-amd64.tar.gz
   ```
2. Extract and configure:

   ```
   Copy-Item -Path ".\bin\" -Destination "$Env:ProgramFiles\containerd" -Recurse -Force
   cd $Env:ProgramFiles\containerd\
   .\containerd.exe config default | Out-File config.toml -Encoding ascii

   # Review the configuration. Depending on setup you may want to adjust:
   # - the sandbox_image (Kubernetes pause image)
   # - cni bin_dir and conf_dir locations
   Get-Content config.toml

   # (Optional - but highly recommended) Exclude containerd from Windows Defender Scans
   Add-MpPreference -ExclusionProcess "$Env:ProgramFiles\containerd\containerd.exe"
   ```
3. Start containerd:

   ```
   .\containerd.exe --register-service
   Start-Service containerd
   ```

## Configure the kubelet to use containerd as its container runtime

Edit the file `/var/lib/kubelet/kubeadm-flags.env` and add the containerd runtime to the flags;
`--container-runtime-endpoint=unix:///run/containerd/containerd.sock`.

Users using kubeadm should be aware that the kubeadm tool stores the host's CRI socket in the

`/var/lib/kubelet/instance-config.yaml` file on each node. You can create this `/var/lib/kubelet/instance-config.yaml` file on the node.

The `/var/lib/kubelet/instance-config.yaml` file allows setting the `containerRuntimeEndpoint` parameter.

You can set this parameter's value to the path of your chosen CRI socket (for example `unix:///run/containerd/containerd.sock`).

## Restart the kubelet

```
systemctl start kubelet
```

## Verify that the node is healthy

Run `kubectl get nodes -o wide` and containerd appears as the runtime for the node we just changed.

## Remove Docker Engine

> **Note:**
> **Note:** This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](/docs/contribute/style/content-guide/#third-party-content) before submitting a change. [More information.](#third-party-content-disclaimer)

If the node appears healthy, remove Docker.

* CentOS
  * Debian
    * Fedora
      * Ubuntu

```
sudo yum remove docker-ce docker-ce-cli
```

```
sudo apt-get purge docker-ce docker-ce-cli
```

```
sudo dnf remove docker-ce docker-ce-cli
```

```
sudo apt-get purge docker-ce docker-ce-cli
```

The preceding commands don't remove images, containers, volumes, or customized configuration files on your host.
To delete them, follow Docker's instructions to [Uninstall Docker Engine](https://docs.docker.com/engine/install/ubuntu/#uninstall-docker-engine).

> **Caution:**
> Docker's instructions for uninstalling Docker Engine create a risk of deleting containerd. Be careful when executing commands.

## Uncordon the node

```
kubectl uncordon <node-to-uncordon>
```

Replace `<node-to-uncordon>` with the name of your node you previously drained.

Items on this page refer to third party products or projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for those third-party products or projects. See the [CNCF website guidelines](https://github.com/cncf/foundation/blob/master/website-guidelines.md) for more details.

You should read the [content guide](/docs/contribute/style/content-guide/#third-party-content) before proposing a change that adds an extra third-party link.

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
