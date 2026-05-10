# Learn Kubernetes Basics

## Objectives

This tutorial provides a walkthrough of the basics of the Kubernetes cluster orchestration
system. Each module contains some background information on major Kubernetes features
and concepts, and a tutorial for you to follow along.

Using the tutorials, you can learn to:

* Deploy a containerized application on a cluster.
* Scale the deployment.
* Update the containerized application with a new software version.
* Debug the containerized application.

## What can Kubernetes do for you?

With modern web services, users expect applications to be available 24/7, and developers
expect to deploy new versions of those applications several times a day. Containerization
helps package software to serve these goals, enabling applications to be released and updated
without downtime. Kubernetes helps you make sure those containerized applications run where
and when you want, and helps them find the resources and tools they need to work. Kubernetes
is a production-ready, open source platform designed with Google's accumulated experience in
container orchestration, combined with best-of-breed ideas from the community.

## Kubernetes Basics Modules

[![Module 1](/docs/tutorials/kubernetes-basics/public/images/module_01.svg?v=1469803628347)

##### 1. Create a Kubernetes cluster](/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/)

[![Module 2](/docs/tutorials/kubernetes-basics/public/images/module_02.svg?v=1469803628347)

##### 2. Deploy an app](/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)

[![Module 3](/docs/tutorials/kubernetes-basics/public/images/module_03.svg?v=1469803628347)

##### 3. Explore your app](/docs/tutorials/kubernetes-basics/explore/explore-intro/)

[![Module 4](/docs/tutorials/kubernetes-basics/public/images/module_04.svg?v=1469803628347)

##### 4. Expose your app publicly](/docs/tutorials/kubernetes-basics/expose/expose-intro/)

[![Module 5](/docs/tutorials/kubernetes-basics/public/images/module_05.svg?v=1469803628347)

##### 5. Scale up your app](/docs/tutorials/kubernetes-basics/scale/scale-intro/)

[![Module 6](/docs/tutorials/kubernetes-basics/public/images/module_06.svg?v=1469803628347)

##### 6. Update your app](/docs/tutorials/kubernetes-basics/update/update-intro/)

## What's next

* Tutorial [Using Minikube to Create a Cluster](/docs/tutorials/kubernetes-basics/create-cluster/)

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
