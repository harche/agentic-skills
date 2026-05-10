This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/tasks/debug/).

# Monitoring, Logging, and Debugging

Set up monitoring and logging to troubleshoot a cluster, or debug a containerized application.

* 1: [Logging in Kubernetes](#pg-76e5c9a3748b8e55436a260715029cc3)

* 2: [Monitoring in Kubernetes](#pg-6b5c06161a775b26439d3fa0cba53f5c)

* 3: [Troubleshooting Applications](#pg-4a26f4e7f9ffe4b86dea8b77906d3d5c)

+ 3.1: [Debug Pods](#pg-abb72792fa997869a6d241ca28ea225e)
+ 3.2: [Debug Services](#pg-68c4fd0542b7d39f8d36435ef83bd57b)
+ 3.3: [Debug a StatefulSet](#pg-089001d4003f033e21602adcb11cd277)
+ 3.4: [Determine the Reason for Pod Failure](#pg-655b47c523b6f1b52d25e520625abccb)
+ 3.5: [Debug Init Containers](#pg-43445f3208669d4078e87dbdbeed8473)
+ 3.6: [Debug Running Pods](#pg-132acc7efbd72bd677945eda3b6c6d38)
+ 3.7: [Get a Shell to a Running Container](#pg-09530217eead8a801ead3ef165c2f591)

* 4: [Troubleshooting Clusters](#pg-ce321f5c35198a1d9b64d52a98ba705c)

+ 4.1: [Troubleshooting kubectl](#pg-a63c7f412c1d137412ccee9f854d3a0c)
+ 4.2: [Resource metrics pipeline](#pg-5ff0cdcf7701f887e45d629f5cfe0424)
+ 4.3: [Tools for Monitoring Resources](#pg-cb9e28c208c6cfbabdb15ba2e42e9ef0)
+ 4.4: [Monitor Node Health](#pg-20165c8269bed123bfb94fb6e7f85643)
+ 4.5: [Debugging Kubernetes nodes with crictl](#pg-6ca4f22ef4d1713577ada4815f0a3b5a)
+ 4.6: [Auditing](#pg-38387ad04dd284933cb502944ea3515b)
+ 4.7: [Debugging Kubernetes Nodes With Kubectl](#pg-0480b8ee5cb8facb546b471bc739286d)
+ 4.8: [Developing and debugging services locally using telepresence](#pg-60dca0ec8d41f0045e7d73e1d6bd7bce)
+ 4.9: [Windows debugging tips](#pg-34f51c9306a166418b33355c09e672be)

Sometimes things go wrong. This guide helps you gather the relevant information and resolve issues. It has four sections:

* [Debugging your application](/docs/tasks/debug/debug-application/) - Useful
  for users who are deploying code into Kubernetes and wondering why it is not working.
* [Debugging your cluster](/docs/tasks/debug/debug-cluster/) - Useful
  for cluster administrators and operators troubleshooting issues with the Kubernetes cluster itself.
* [Logging in Kubernetes](/docs/tasks/debug/logging/) - Useful
  for cluster administrators who want to set up and manage logging in Kubernetes.
* [Monitoring in Kubernetes](/docs/tasks/debug/monitoring/) - Useful
  for cluster administrators who want to enable monitoring in a Kubernetes cluster.

You should also check the known issues for the [release](https://github.com/kubernetes/kubernetes/releases)
you're using.

## Getting help

If your problem isn't answered by any of the guides above, there are variety of
ways for you to get help from the Kubernetes community.

### Questions

The documentation on this site has been structured to provide answers to a wide
range of questions. [Concepts](/docs/concepts/) explain the Kubernetes
architecture and how each component works, while [Setup](/docs/setup/) provides
practical instructions for getting started. [Tasks](/docs/tasks/) show how to
accomplish commonly used tasks, and [Tutorials](/docs/tutorials/) are more
comprehensive walkthroughs of real-world, industry-specific, or end-to-end
development scenarios. The [Reference](/docs/reference/) section provides
detailed documentation on the [Kubernetes API](/docs/reference/generated/kubernetes-api/v1.34/)
and command-line interfaces (CLIs), such as [`kubectl`](/docs/reference/kubectl/).

## Help! My question isn't covered! I need help now!

### Stack Exchange, Stack Overflow, or Server Fault

If you have questions related to *software development* for your containerized app,
you can ask those on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes).

If you have Kubernetes questions related to *cluster management* or *configuration*,
you can ask those on
[Server Fault](https://serverfault.com/questions/tagged/kubernetes).

There are also several more specific Stack Exchange network sites which might
be the right place to ask Kubernetes questions in areas such as
[DevOps](https://devops.stackexchange.com/questions/tagged/kubernetes),
[Software Engineering](https://softwareengineering.stackexchange.com/questions/tagged/kubernetes),
or [InfoSec](https://security.stackexchange.com/questions/tagged/kubernetes).

Someone else from the community may have already asked a similar question or
may be able to help with your problem.

The Kubernetes team will also monitor
[posts tagged Kubernetes](https://stackoverflow.com/questions/tagged/kubernetes).
If there aren't any existing questions that help, **please ensure that your question
is [on-topic on Stack Overflow](https://stackoverflow.com/help/on-topic),
[Server Fault](https://serverfault.com/help/on-topic), or the Stack Exchange
Network site you're asking on**, and read through the guidance on
[how to ask a new question](https://stackoverflow.com/help/how-to-ask),
before asking a new one!

### Slack

Many people from the Kubernetes community hang out on Kubernetes Slack in the `#kubernetes-users` channel.
Slack requires registration; you can [request an invitation](https://slack.kubernetes.io),
and registration is open to everyone). Feel free to come and ask any and all questions.
Once registered, access the [Kubernetes organisation in Slack](https://kubernetes.slack.com)
via your web browser or via Slack's own dedicated app.

Once you are registered, browse the growing list of channels for various subjects of
interest. For example, people new to Kubernetes may also want to join the
[`#kubernetes-novice`](https://kubernetes.slack.com/messages/kubernetes-novice) channel. As another example, developers should join the
[`#kubernetes-contributors`](https://kubernetes.slack.com/messages/kubernetes-contributors) channel.

There are also many country specific / local language channels. Feel free to join
these channels for localized support and info:

Country / language specific Slack channels

| Country | Channels |
| --- | --- |
| China | [`#cn-users`](https://kubernetes.slack.com/messages/cn-users), [`#cn-events`](https://kubernetes.slack.com/messages/cn-events) |
| Finland | [`#fi-users`](https://kubernetes.slack.com/messages/fi-users) |
| France | [`#fr-users`](https://kubernetes.slack.com/messages/fr-users), [`#fr-events`](https://kubernetes.slack.com/messages/fr-events) |
| Germany | [`#de-users`](https://kubernetes.slack.com/messages/de-users), [`#de-events`](https://kubernetes.slack.com/messages/de-events) |
| India | [`#in-users`](https://kubernetes.slack.com/messages/in-users), [`#in-events`](https://kubernetes.slack.com/messages/in-events) |
| Italy | [`#it-users`](https://kubernetes.slack.com/messages/it-users), [`#it-events`](https://kubernetes.slack.com/messages/it-events) |
| Japan | [`#jp-users`](https://kubernetes.slack.com/messages/jp-users), [`#jp-events`](https://kubernetes.slack.com/messages/jp-events) |
| Korea | [`#kr-users`](https://kubernetes.slack.com/messages/kr-users) |
| Netherlands | [`#nl-users`](https://kubernetes.slack.com/messages/nl-users) |
| Norway | [`#norw-users`](https://kubernetes.slack.com/messages/norw-users) |
| Poland | [`#pl-users`](https://kubernetes.slack.com/messages/pl-users) |
| Russia | [`#ru-users`](https://kubernetes.slack.com/messages/ru-users) |
| Spain | [`#es-users`](https://kubernetes.slack.com/messages/es-users) |
| Sweden | [`#se-users`](https://kubernetes.slack.com/messages/se-users) |
| Turkey | [`#tr-users`](https://kubernetes.slack.com/messages/tr-users), [`#tr-events`](https://kubernetes.slack.com/messages/tr-events) |

### Forum

You're welcome to join the official Kubernetes Forum: [discuss.kubernetes.io](https://discuss.kubernetes.io).

### Bugs and feature requests

If you have what looks like a bug, or you would like to make a feature request,
please use the [GitHub issue tracking system](https://github.com/kubernetes/kubernetes/issues).

Before you file an issue, please search existing issues to see if your issue is
already covered.

If filing a bug, please include detailed information about how to reproduce the
problem, such as:

* Kubernetes version: `kubectl version`
* Cloud provider, OS distro, network configuration, and container runtime version
* Steps to reproduce the problem
