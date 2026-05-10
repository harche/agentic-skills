# Changing The Kubernetes Package Repository

This page explains how to enable a package repository for the desired
Kubernetes minor release upon upgrading a cluster. This is only needed
for users of the community-owned package repositories hosted at `pkgs.k8s.io`.
Unlike the legacy package repositories, the community-owned package
repositories are structured in a way that there's a dedicated package
repository for each Kubernetes minor version.

> **Note:**
> This guide only covers a part of the Kubernetes upgrade process. Please see the
> [upgrade guide](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/) for
> more information about upgrading Kubernetes clusters.

> **Note:**
> This step is only needed upon upgrading a cluster to another **minor** release.
> If you're upgrading to another patch release within the same minor release (e.g.
> v1.34.5 to v1.34.7), you don't
> need to follow this guide. However, if you're still using the legacy package
> repositories, you'll need to migrate to the new community-owned package
> repositories before upgrading (see the next section for more details on how to
> do this).

## Before you begin

This document assumes that you're already using the community-owned
package repositories (`pkgs.k8s.io`). If that's not the case, it's strongly
recommended to migrate to the community-owned package repositories as described
in the [official announcement](/blog/2023/08/15/pkgs-k8s-io-introduction/).

> **Note:**
> **Note:** The legacy package repositories (`apt.kubernetes.io` and `yum.kubernetes.io`) have been
> [deprecated and frozen starting from September 13, 2023](/blog/2023/08/31/legacy-package-repository-deprecation/).
> **Using the [new package repositories hosted at `pkgs.k8s.io`](/blog/2023/08/15/pkgs-k8s-io-introduction/)
> is strongly recommended and required in order to install Kubernetes versions released after September 13, 2023.**
> The deprecated legacy repositories, and their contents, might be removed at any time in the future and without
> a further notice period. The new package repositories provide downloads for Kubernetes versions starting with v1.24.0.

### Verifying if the Kubernetes package repositories are used

If you're unsure whether you're using the community-owned package repositories or the
legacy package repositories, take the following steps to verify:

* Ubuntu, Debian or HypriotOS
  * CentOS, RHEL or Fedora
    * openSUSE or SLES

Print the contents of the file that defines the Kubernetes `apt` repository:

```
# On your system, this configuration file could have a different name
pager /etc/apt/sources.list.d/kubernetes.list
```

If you see a line similar to:

```
deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.33/deb/ /
```

**You're using the Kubernetes package repositories and this guide applies to you.**
Otherwise, it's strongly recommended to migrate to the Kubernetes package repositories
as described in the [official announcement](/blog/2023/08/15/pkgs-k8s-io-introduction/).

Print the contents of the file that defines the Kubernetes `yum` repository:

```
# On your system, this configuration file could have a different name
cat /etc/yum.repos.d/kubernetes.repo
```

If you see a `baseurl` similar to the `baseurl` in the output below:

```
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.33/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.33/rpm/repodata/repomd.xml.key
exclude=kubelet kubeadm kubectl
```

**You're using the Kubernetes package repositories and this guide applies to you.**
Otherwise, it's strongly recommended to migrate to the Kubernetes package repositories
as described in the [official announcement](/blog/2023/08/15/pkgs-k8s-io-introduction/).

Print the contents of the file that defines the Kubernetes `zypper` repository:

```
# On your system, this configuration file could have a different name
cat /etc/zypp/repos.d/kubernetes.repo
```

If you see a `baseurl` similar to the `baseurl` in the output below:

```
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.33/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.33/rpm/repodata/repomd.xml.key
exclude=kubelet kubeadm kubectl
```

**You're using the Kubernetes package repositories and this guide applies to you.**
Otherwise, it's strongly recommended to migrate to the Kubernetes package repositories
as described in the [official announcement](/blog/2023/08/15/pkgs-k8s-io-introduction/).

> **Note:**
> The URL used for the Kubernetes package repositories is not limited to `pkgs.k8s.io`,
> it can also be one of:
>
> * `pkgs.k8s.io`
> * `pkgs.kubernetes.io`
> * `packages.kubernetes.io`

## Switching to another Kubernetes package repository

This step should be done upon upgrading from one to another Kubernetes minor
release in order to get access to the packages of the desired Kubernetes minor
version.

* Ubuntu, Debian or HypriotOS
  * CentOS, RHEL or Fedora

1. Open the file that defines the Kubernetes `apt` repository using a text editor of your choice:

   ```
   nano /etc/apt/sources.list.d/kubernetes.list
   ```

   You should see a single line with the URL that contains your current Kubernetes
   minor version. For example, if you're using v1.33,
   you should see this:

   ```
   deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.33/deb/ /
   ```
2. Change the version in the URL to **the next available minor release**, for example:

   ```
   deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.34/deb/ /
   ```
3. Save the file and exit your text editor. Continue following the relevant upgrade instructions.

1. Open the file that defines the Kubernetes `yum` repository using a text editor of your choice:

   ```
   nano /etc/yum.repos.d/kubernetes.repo
   ```

   You should see a file with two URLs that contain your current Kubernetes
   minor version. For example, if you're using v1.33,
   you should see this:

   ```
   [kubernetes]
   name=Kubernetes
   baseurl=https://pkgs.k8s.io/core:/stable:/v1.33/rpm/
   enabled=1
   gpgcheck=1
   gpgkey=https://pkgs.k8s.io/core:/stable:/v1.33/rpm/repodata/repomd.xml.key
   exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
   ```
2. Change the version in these URLs to **the next available minor release**, for example:

   ```
   [kubernetes]
   name=Kubernetes
   baseurl=https://pkgs.k8s.io/core:/stable:/v1.34/rpm/
   enabled=1
   gpgcheck=1
   gpgkey=https://pkgs.k8s.io/core:/stable:/v1.34/rpm/repodata/repomd.xml.key
   exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
   ```
3. Save the file and exit your text editor. Continue following the relevant upgrade instructions.

## What's next

* See how to [Upgrade Linux nodes](/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes/).
* See how to [Upgrade Windows nodes](/docs/tasks/administer-cluster/kubeadm/upgrading-windows-nodes/).

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
