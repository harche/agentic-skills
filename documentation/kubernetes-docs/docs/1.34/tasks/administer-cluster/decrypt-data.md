# Decrypt Confidential Data that is Already Encrypted at Rest

All of the APIs in Kubernetes that let you write persistent API resource data support
at-rest encryption. For example, you can enable at-rest encryption for
[Secrets](/docs/concepts/configuration/secret/ "Stores sensitive information, such as passwords, OAuth tokens, and ssh keys.").
This at-rest encryption is additional to any system-level encryption for the
etcd cluster or for the filesystem(s) on hosts where you are running the
kube-apiserver.

This page shows how to switch from encryption of API data at rest, so that API data
are stored unencrypted. You might want to do this to improve performance; usually,
though, if it was a good idea to encrypt some data, it's also a good idea to leave them
encrypted.

> **Note:**
> This task covers encryption for resource data stored using the
> [Kubernetes API](/docs/concepts/overview/kubernetes-api/ "The application that serves Kubernetes functionality through a RESTful interface and stores the state of the cluster."). For example, you can
> encrypt Secret objects, including the key-value data they contain.
>
> If you wanted to manage encryption for data in filesystems that are mounted into containers, you instead
> need to either:
>
> * use a storage integration that provides encrypted
> [volumes](/docs/concepts/storage/volumes/ "A directory containing data, accessible to the containers in a pod.")
> * encrypt the data within your own application

## Before you begin

* You need to have a Kubernetes cluster, and the kubectl command-line tool must
  be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
  cluster, you can create one by using
  [minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
  or you can use one of these Kubernetes playgrounds:

  + [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
  + [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
  + [KodeKloud](https://kodekloud.com/public-playgrounds)
  + [Play with Kubernetes](https://labs.play-with-k8s.com/)
* This task assumes that you are running the Kubernetes API server as a
  [static pod](/docs/tasks/configure-pod-container/static-pod/ "A pod managed directly by the kubelet daemon on a specific node.") on each control
  plane node.
* Your cluster's control plane **must** use etcd v3.x (major version 3, any minor version).
* To encrypt a custom resource, your cluster must be running Kubernetes v1.26 or newer.
* You should have some API data that are already encrypted.

To check the version, enter `kubectl version`.

## Determine whether encryption at rest is already enabled

By default, the API server uses an `identity` provider that stores plain-text representations
of resources.
**The default `identity` provider does not provide any confidentiality protection.**

The `kube-apiserver` process accepts an argument `--encryption-provider-config`
that specifies a path to a configuration file. The contents of that file, if you specify one,
control how Kubernetes API data is encrypted in etcd.
If it is not specified, you do not have encryption at rest enabled.

The format of that configuration file is YAML, representing a configuration API kind named
[`EncryptionConfiguration`](/docs/reference/config-api/apiserver-config.v1/).
You can see an example configuration
in [Encryption at rest configuration](/docs/tasks/administer-cluster/encrypt-data/#understanding-the-encryption-at-rest-configuration).

If `--encryption-provider-config` is set, check which resources (such as `secrets`) are
configured for encryption, and what provider is used.
Make sure that the preferred provider for that resource type is **not** `identity`; you
only set `identity` (*no encryption*) as default when you want to disable encryption at
rest.
Verify that the first-listed provider for a resource is something **other** than `identity`,
which means that any new information written to resources of that type will be encrypted as
configured. If you do see `identity` as the first-listed provider for any resource, this
means that those resources are being written out to etcd without encryption.

## Decrypt all data

This example shows how to stop encrypting the Secret API at rest. If you are encrypting
other API kinds, adjust the steps to match.

### Locate the encryption configuration file

First, find the API server configuration files. On each control plane node, static Pod manifest
for the kube-apiserver specifies a command line argument, `--encryption-provider-config`.
You are likely to find that this file is mounted into the static Pod using a
[`hostPath`](/docs/concepts/storage/volumes/#hostpath) volume mount. Once you locate the volume
you can find the file on the node filesystem and inspect it.

### Configure the API server to decrypt objects

To disable encryption at rest, place the `identity` provider as the first
entry in your encryption configuration file.

For example, if your existing EncryptionConfiguration file reads:

```
---
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
      - secrets
    providers:
      - aescbc:
          keys:
            # Do not use this (invalid) example key for encryption
            - name: example
              secret: 2KfZgdiq2K0g2YrYpyDYs9mF2LPZhQ==
```

then change it to:

```
---
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
      - secrets
    providers:
      - identity: {} # add this line
      - aescbc:
          keys:
            - name: example
              secret: 2KfZgdiq2K0g2YrYpyDYs9mF2LPZhQ==
```

and restart the kube-apiserver Pod on this node.

### Reconfigure other control plane hosts

If you have multiple API servers in your cluster, you should deploy the changes in turn to each API server.

Make sure that you use the same encryption configuration on each control plane host.

### Force decryption

Then run the following command to force decryption of all Secrets:

```
# If you are decrypting a different kind of object, change "secrets" to match.
kubectl get secrets --all-namespaces -o json | kubectl replace -f -
```

Once you have replaced **all** existing encrypted resources with backing data that
don't use encryption, you can remove the encryption settings from the
`kube-apiserver`.

The command line options to remove are:

* `--encryption-provider-config`
* `--encryption-provider-config-automatic-reload`

Restart the kube-apiserver Pod again to apply the new configuration.

### Reconfigure other control plane hosts

If you have multiple API servers in your cluster, you should again deploy the changes in turn to each API server.

Make sure that you use the same encryption configuration on each control plane host.

## What's next

* Learn more about the [EncryptionConfiguration configuration API (v1)](/docs/reference/config-api/apiserver-config.v1/).

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
