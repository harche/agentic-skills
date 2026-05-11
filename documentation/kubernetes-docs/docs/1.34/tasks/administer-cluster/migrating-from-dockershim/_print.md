This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/tasks/administer-cluster/migrating-from-dockershim/).

# Migrating from dockershim

* 1: [Changing the Container Runtime on a Node from Docker Engine to containerd](#pg-b8acce0768c2f92cdb8eaa31e8072353)
* 2: [Find Out What Container Runtime is Used on a Node](#pg-d79db9ed1698f75ec5f2228987290e49)
* 3: [Troubleshooting CNI plugin-related errors](#pg-c4b5bb78bc6c59690d21c44e41f12270)
* 4: [Check whether dockershim removal affects you](#pg-cbd252cc297e67c1b73a84d5882474fb)
* 5: [Migrating telemetry and security agents from dockershim](#pg-eb3e279a6c5e1224e744080a52ee3f28)

This section presents information you need to know when migrating from
dockershim to other container runtimes.

Since the announcement of [dockershim deprecation](/blog/2020/12/08/kubernetes-1-20-release-announcement/#dockershim-deprecation)
in Kubernetes 1.20, there were questions on how this will affect various workloads and Kubernetes
installations. Our [Dockershim Removal FAQ](/blog/2022/02/17/dockershim-faq/) is there to help you
to understand the problem better.

Dockershim was removed from Kubernetes with the release of v1.24.
If you use Docker Engine via dockershim as your container runtime and wish to upgrade to v1.24,
it is recommended that you either migrate to another runtime or find an alternative means to obtain Docker Engine support.
Check out the [container runtimes](/docs/setup/production-environment/container-runtimes/)
section to know your options.

The version of Kubernetes with dockershim (1.23) is out of support and the v1.24
will run out of support [soon](/releases/#release-v1-24). Make sure to
[report issues](https://github.com/kubernetes/kubernetes/issues) you encountered
with the migration so the issues can be fixed in a timely manner and your cluster would be
ready for dockershim removal. After v1.24 running out of support, you will need
to contact your Kubernetes provider for support or upgrade multiple versions at a time
if there are critical issues affecting your cluster.

Your cluster might have more than one kind of node, although this is not a common
configuration.

These tasks will help you to migrate:

* [Check whether Dockershim removal affects you](/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/)
* [Migrating telemetry and security agents from dockershim](/docs/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents/)

## What's next

* Check out [container runtimes](/docs/setup/production-environment/container-runtimes/)
  to understand your options for an alternative.
* If you find a defect or other technical concern relating to migrating away from dockershim,
  you can [report an issue](https://github.com/kubernetes/kubernetes/issues/new/choose)
  to the Kubernetes project.
