# Handling retriable and non-retriable pod failures with Pod failure policy

FEATURE STATE:
`Kubernetes v1.31 [stable]`(enabled by default)

This document shows you how to use the
[Pod failure policy](/docs/concepts/workloads/controllers/job/#pod-failure-policy),
in combination with the default
[Pod backoff failure policy](/docs/concepts/workloads/controllers/job/#pod-backoff-failure-policy),
to improve the control over the handling of container- or Pod-level failure
within a [Job](/docs/concepts/workloads/controllers/job/ "A finite or batch task that runs to completion.").

The definition of Pod failure policy may help you to:

* better utilize the computational resources by avoiding unnecessary Pod retries.
* avoid Job failures due to Pod disruptions (such [preemption](/docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption "Preemption logic in Kubernetes helps a pending Pod to find a suitable Node by evicting low priority Pods existing on that Node."),
  [API-initiated eviction](/docs/concepts/scheduling-eviction/api-eviction/ "API-initiated eviction is the process by which you use the Eviction API to create an Eviction object that triggers graceful pod termination.")
  or [taint](/docs/concepts/scheduling-eviction/taint-and-toleration/ "A core object consisting of three required properties: key, value, and effect. Taints prevent the scheduling of pods on nodes or node groups.")-based eviction).

## Before you begin

You should already be familiar with the basic use of [Job](/docs/concepts/workloads/controllers/job/).

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [KodeKloud](https://kodekloud.com/public-playgrounds)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)

Your Kubernetes server must be at or later than version v1.25.

To check the version, enter `kubectl version`.

## Usage scenarios

Consider the following usage scenarios for Jobs that define a Pod failure policy :

* [Avoiding unnecessary Pod retries](#pod-failure-policy-failjob)
* [Ignoring Pod disruptions](#pod-failure-policy-ignore)
* [Avoiding unnecessary Pod retries based on custom Pod Conditions](#pod-failure-policy-config-issue)
* [Avoiding unnecessary Pod retries per index](#backoff-limit-per-index-failindex)

### Using Pod failure policy to avoid unnecessary Pod retries

With the following example, you can learn how to use Pod failure policy to
avoid unnecessary Pod restarts when a Pod failure indicates a non-retriable
software bug.

1. Examine the following manifest:

   [`/controllers/job-pod-failure-policy-failjob.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples//controllers/job-pod-failure-policy-failjob.yaml)![](/images/copycode.svg "Copy /controllers/job-pod-failure-policy-failjob.yaml to clipboard")

   ```
   apiVersion: batch/v1
   kind: Job
   metadata:
     name: job-pod-failure-policy-failjob
   spec:
     completions: 8
     parallelism: 2
     template:
       spec:
         restartPolicy: Never
         containers:
         - name: main
           image: docker.io/library/bash:5
           command: ["bash"]
           args:
           - -c
           - echo "Hello world! I'm going to exit with 42 to simulate a software bug." && sleep 30 && exit 42
     backoffLimit: 6
     podFailurePolicy:
       rules:
       - action: FailJob
         onExitCodes:
           containerName: main
           operator: In
           values: [42]
   ```
2. Apply the manifest:

   ```
   kubectl create -f https://k8s.io/examples/controllers/job-pod-failure-policy-failjob.yaml
   ```
3. After around 30 seconds the entire Job should be terminated. Inspect the status of the Job by running:

   ```
   kubectl get jobs -l job-name=job-pod-failure-policy-failjob -o yaml
   ```

   In the Job status, the following conditions display:

   * `FailureTarget` condition: has a `reason` field set to `PodFailurePolicy` and
     a `message` field with more information about the termination, like
     `Container main for pod default/job-pod-failure-policy-failjob-8ckj8 failed with exit code 42 matching FailJob rule at index 0`.
     The Job controller adds this condition as soon as the Job is considered a failure.
     For details, see [Termination of Job Pods](/docs/concepts/workloads/controllers/job/#termination-of-job-pods).
   * `Failed` condition: same `reason` and `message` as the `FailureTarget`
     condition. The Job controller adds this condition after all of the Job's Pods
     are terminated.

   For comparison, if the Pod failure policy was disabled it would take 6 retries
   of the Pod, taking at least 2 minutes.

#### Clean up

Delete the Job you created:

```
kubectl delete jobs/job-pod-failure-policy-failjob
```

The cluster automatically cleans up the Pods.

### Using Pod failure policy to ignore Pod disruptions

With the following example, you can learn how to use Pod failure policy to
ignore Pod disruptions from incrementing the Pod retry counter towards the
`.spec.backoffLimit` limit.

> **Caution:**
> Timing is important for this example, so you may want to read the steps before
> execution. In order to trigger a Pod disruption it is important to drain the
> node while the Pod is running on it (within 90s since the Pod is scheduled).

1. Examine the following manifest:

   [`/controllers/job-pod-failure-policy-ignore.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples//controllers/job-pod-failure-policy-ignore.yaml)![](/images/copycode.svg "Copy /controllers/job-pod-failure-policy-ignore.yaml to clipboard")

   ```
   apiVersion: batch/v1
   kind: Job
   metadata:
     name: job-pod-failure-policy-ignore
   spec:
     completions: 4
     parallelism: 2
     template:
       spec:
         restartPolicy: Never
         containers:
         - name: main
           image: docker.io/library/bash:5
           command: ["bash"]
           args:
           - -c
           - echo "Hello world! I'm going to exit with 0 (success)." && sleep 90 && exit 0
     backoffLimit: 0
     podFailurePolicy:
       rules:
       - action: Ignore
         onPodConditions:
         - type: DisruptionTarget
   ```
2. Apply the manifest:

   ```
   kubectl create -f https://k8s.io/examples/controllers/job-pod-failure-policy-ignore.yaml
   ```
3. Run this command to check the `nodeName` the Pod is scheduled to:

   ```
   nodeName=$(kubectl get pods -l job-name=job-pod-failure-policy-ignore -o jsonpath='{.items[0].spec.nodeName}')
   ```
4. Drain the node to evict the Pod before it completes (within 90s):

   ```
   kubectl drain nodes/$nodeName --ignore-daemonsets --grace-period=0
   ```
5. Inspect the `.status.failed` to check the counter for the Job is not incremented:

   ```
   kubectl get jobs -l job-name=job-pod-failure-policy-ignore -o yaml
   ```
6. Uncordon the node:

   ```
   kubectl uncordon nodes/$nodeName
   ```

The Job resumes and succeeds.

For comparison, if the Pod failure policy was disabled the Pod disruption would
result in terminating the entire Job (as the `.spec.backoffLimit` is set to 0).

#### Cleaning up

Delete the Job you created:

```
kubectl delete jobs/job-pod-failure-policy-ignore
```

The cluster automatically cleans up the Pods.

### Using Pod failure policy to avoid unnecessary Pod retries based on custom Pod Conditions

With the following example, you can learn how to use Pod failure policy to
avoid unnecessary Pod restarts based on custom Pod Conditions.

> **Note:**
> The example below works since version 1.27 as it relies on transitioning of
> deleted pods, in the `Pending` phase, to a terminal phase
> (see: [Pod Phase](/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase)).

1. Examine the following manifest:

   [`/controllers/job-pod-failure-policy-config-issue.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples//controllers/job-pod-failure-policy-config-issue.yaml)![](/images/copycode.svg "Copy /controllers/job-pod-failure-policy-config-issue.yaml to clipboard")

   ```
   apiVersion: batch/v1
   kind: Job
   metadata:
     name: job-pod-failure-policy-config-issue
   spec:
     completions: 8
     parallelism: 2
     template:
       spec:
         restartPolicy: Never
         containers:
         - name: main
           image: "non-existing-repo/non-existing-image:example"
     backoffLimit: 6
     podFailurePolicy:
       rules:
       - action: FailJob
         onPodConditions:
         - type: ConfigIssue
   ```
2. Apply the manifest:

   ```
   kubectl create -f https://k8s.io/examples/controllers/job-pod-failure-policy-config-issue.yaml
   ```

   Note that, the image is misconfigured, as it does not exist.
3. Inspect the status of the job's Pods by running:

   ```
   kubectl get pods -l job-name=job-pod-failure-policy-config-issue -o yaml
   ```

   You will see output similar to this:

   ```
   containerStatuses:
   - image: non-existing-repo/non-existing-image:example
      ...
      state:
      waiting:
         message: Back-off pulling image "non-existing-repo/non-existing-image:example"
         reason: ImagePullBackOff
         ...
   phase: Pending
   ```

   Note that the pod remains in the `Pending` phase as it fails to pull the
   misconfigured image. This, in principle, could be a transient issue and the
   image could get pulled. However, in this case, the image does not exist so
   we indicate this fact by a custom condition.
4. Add the custom condition. First prepare the patch by running:

   ```
   cat <<EOF > patch.yaml
   status:
     conditions:
     - type: ConfigIssue
       status: "True"
       reason: "NonExistingImage"
       lastTransitionTime: "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
   EOF
   ```

   Second, select one of the pods created by the job by running:

   ```
   podName=$(kubectl get pods -l job-name=job-pod-failure-policy-config-issue -o jsonpath='{.items[0].metadata.name}')
   ```

   Then, apply the patch on one of the pods by running the following command:

   ```
   kubectl patch pod $podName --subresource=status --patch-file=patch.yaml
   ```

   If applied successfully, you will get a notification like this:

   ```
   pod/job-pod-failure-policy-config-issue-k6pvp patched
   ```
5. Delete the pod to transition it to `Failed` phase, by running the command:

   ```
   kubectl delete pods/$podName
   ```
6. Inspect the status of the Job by running:

   ```
   kubectl get jobs -l job-name=job-pod-failure-policy-config-issue -o yaml
   ```

   In the Job status, see a job `Failed` condition with the field `reason`
   equal `PodFailurePolicy`. Additionally, the `message` field contains a
   more detailed information about the Job termination, such as:
   `Pod default/job-pod-failure-policy-config-issue-k6pvp has condition ConfigIssue matching FailJob rule at index 0`.

> **Note:**
> In a production environment, the steps 3 and 4 should be automated by a
> user-provided controller.

#### Cleaning up

Delete the Job you created:

```
kubectl delete jobs/job-pod-failure-policy-config-issue
```

The cluster automatically cleans up the Pods.

### Using Pod Failure Policy to avoid unnecessary Pod retries per index

To avoid unnecessary Pod restarts per index, you can use the *Pod failure policy* and
*backoff limit per index* features. This section of the page shows how to use these features
together.

1. Examine the following manifest:

   [`/controllers/job-backoff-limit-per-index-failindex.yaml`](https://raw.githubusercontent.com/kubernetes/website/release-1.34/content/en/examples//controllers/job-backoff-limit-per-index-failindex.yaml)![](/images/copycode.svg "Copy /controllers/job-backoff-limit-per-index-failindex.yaml to clipboard")

   ```
   apiVersion: batch/v1
   kind: Job
   metadata:
     name: job-backoff-limit-per-index-failindex
   spec:
     completions: 4
     parallelism: 2
     completionMode: Indexed
     backoffLimitPerIndex: 1
     template:
       spec:
         restartPolicy: Never
         containers:
         - name: main
           image: docker.io/library/python:3
           command:
             # The script:
             # - fails the Pod with index 0 with exit code 1, which results in one retry;
             # - fails the Pod with index 1 with exit code 42 which results
             #   in failing the index without retry.
             # - succeeds Pods with any other index.
             - python3
             - -c
             - |
               import os, sys
               index = int(os.environ.get("JOB_COMPLETION_INDEX"))
               if index == 0:
                 sys.exit(1)
               elif index == 1:
                 sys.exit(42)
               else:
                 sys.exit(0)
     backoffLimit: 6
     podFailurePolicy:
       rules:
       - action: FailIndex
         onExitCodes:
           containerName: main
           operator: In
           values: [42]
   ```
2. Apply the manifest:

   ```
   kubectl create -f https://k8s.io/examples/controllers/job-backoff-limit-per-index-failindex.yaml
   ```
3. After around 15 seconds, inspect the status of the Pods for the Job. You can do that by running:

   ```
   kubectl get pods -l job-name=job-backoff-limit-per-index-failindex -o yaml
   ```

   You will see output similar to this:

   ```
   NAME                                            READY   STATUS      RESTARTS   AGE
   job-backoff-limit-per-index-failindex-0-4g4cm   0/1     Error       0          4s
   job-backoff-limit-per-index-failindex-0-fkdzq   0/1     Error       0          15s
   job-backoff-limit-per-index-failindex-1-2bgdj   0/1     Error       0          15s
   job-backoff-limit-per-index-failindex-2-vs6lt   0/1     Completed   0          11s
   job-backoff-limit-per-index-failindex-3-s7s47   0/1     Completed   0          6s
   ```

   Note that the output shows the following:

   * Two Pods have index 0, because of the backoff limit allowed for one retry
     of the index.
   * Only one Pod has index 1, because the exit code of the failed Pod matched
     the Pod failure policy with the `FailIndex` action.
4. Inspect the status of the Job by running:

   ```
   kubectl get jobs -l job-name=job-backoff-limit-per-index-failindex -o yaml
   ```

   In the Job status, see that the `failedIndexes` field shows "0,1", because
   both indexes failed. Because the index 1 was not retried the number of failed
   Pods, indicated by the status field "failed" equals 3.

#### Cleaning up

Delete the Job you created:

```
kubectl delete jobs/job-backoff-limit-per-index-failindex
```

The cluster automatically cleans up the Pods.

## Alternatives

You could rely solely on the
[Pod backoff failure policy](/docs/concepts/workloads/controllers/job/#pod-backoff-failure-policy),
by specifying the Job's `.spec.backoffLimit` field. However, in many situations
it is problematic to find a balance between setting a low value for `.spec.backoffLimit`
to avoid unnecessary Pod retries, yet high enough to make sure the Job would
not be terminated by Pod disruptions.

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
