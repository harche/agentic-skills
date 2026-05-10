# Enabling tab completion

You can enable tab completion for the Bash or Zsh shells.

## Enabling tab completion for Bash

<div wrapper="1" role="_abstract">

After you install the OpenShift CLI (`oc`), you can enable tab completion to automatically complete `oc` commands or suggest options when you press Tab. The following procedure enables tab completion for the Bash shell.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You must have the OpenShift CLI (`oc`) installed.

- You must have the package `bash-completion` installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Save the Bash completion code to a file:

    ``` terminal
    $ oc completion bash > oc_bash_completion
    ```

2.  Copy the file to `/etc/bash_completion.d/`:

    ``` terminal
    $ sudo cp oc_bash_completion /etc/bash_completion.d/
    ```

    You can also save the file to a local directory and source it from your `.bashrc` file instead. Tab completion is enabled when you open a new terminal.

</div>

## Enabling tab completion for Zsh

<div wrapper="1" role="_abstract">

After you install the OpenShift CLI (`oc`), you can enable tab completion to automatically complete `oc` commands or suggest options when you press Tab. The following procedure enables tab completion for the Zsh shell.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You must have the OpenShift CLI (`oc`) installed.

</div>

<div>

<div class="title">

Procedure

</div>

- To add tab completion for `oc` to your `.zshrc` file, run the following command:

  ``` terminal
  $ cat >>~/.zshrc<<EOF
  autoload -Uz compinit
  compinit
  if [ $commands[oc] ]; then
    source <(oc completion zsh)
    compdef _oc oc
  fi
  EOF
  ```

  Tab completion is enabled when you open a new terminal.

</div>

# Accessing kubeconfig by using the oc CLI

You can use the `oc` CLI to log in to your OpenShift cluster and retrieve a kubeconfig file for accessing the cluster from the command line.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform web console or API server endpoint.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to your OpenShift cluster by running the following command:

    ``` terminal
    $ oc login <api-server-url> -u <username> -p <password>
    ```

    - Specify the full API server URL. For example: `https://api.my-cluster.example.com:6443`.

    - Specify a valid username. For example: `kubeadmin`.

    - Provide the password for the specified user. For example, the `kubeadmin` password generated during cluster installation.

2.  Save the cluster configuration to a local file by running the following command:

    ``` terminal
    $ oc config view --raw > kubeconfig
    ```

3.  Set the `KUBECONFIG` environment variable to point to the exported file by running the following command:

    ``` terminal
    $ export KUBECONFIG=./kubeconfig
    ```

4.  Use `oc` to interact with your OpenShift cluster by running the following command:

    ``` terminal
    $ oc get nodes
    ```

</div>

> [!NOTE]
> If you plan to reuse the exported `kubeconfig` file across sessions or machines, store it securely and avoid committing it to source control.
