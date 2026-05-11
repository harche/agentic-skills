# Manual Rotation of CA Certificates

This page shows how to manually rotate the certificate authority (CA) certificates.

## Before you begin

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [KodeKloud](https://kodekloud.com/public-playgrounds)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)

* For more information about authentication in Kubernetes, see
  [Authenticating](/docs/reference/access-authn-authz/authentication/).
* For more information about best practices for CA certificates, see
  [Single root CA](/docs/setup/best-practices/certificates/#single-root-ca).

## Rotate the CA certificates manually

> **Caution:**
> Make sure to back up your certificate directory along with configuration files and any other necessary files.
>
> This approach assumes operation of the Kubernetes control plane in a HA configuration with multiple API servers.
> Graceful termination of the API server is also assumed so clients can cleanly disconnect from one API server and
> reconnect to another.
>
> Configurations with a single API server will experience unavailability while the API server is being restarted.

1. Distribute the new CA certificates and private keys (for example: `ca.crt`, `ca.key`, `front-proxy-ca.crt`,
   and `front-proxy-ca.key`) to all your control plane nodes in the Kubernetes certificates directory.
2. Update the `--root-ca-file` flag for the [kube-controller-manager](/docs/reference/command-line-tools-reference/kube-controller-manager/ "Control Plane component that runs controller processes.") to include
   both old and new CA, then restart the kube-controller-manager.

   Any [ServiceAccount](/docs/tasks/configure-pod-container/configure-service-account/ "Provides an identity for processes that run in a Pod.") created after this point will get
   Secrets that include both old and new CAs.

   > **Note:**
   > The files specified by the kube-controller-manager flags `--client-ca-file` and `--cluster-signing-cert-file`
   > cannot be CA bundles. If these flags and `--root-ca-file` point to the same `ca.crt` file which is now a
   > bundle (includes both old and new CA) you will face an error. To workaround this problem you can copy the new CA
   > to a separate file and make the flags `--client-ca-file` and `--cluster-signing-cert-file` point to the copy.
   > Once `ca.crt` is no longer a bundle you can restore the problem flags to point to `ca.crt` and delete the copy.
   >
   > [Issue 1350](https://github.com/kubernetes/kubeadm/issues/1350) for kubeadm tracks an bug with the
   > kube-controller-manager being unable to accept a CA bundle.
3. Wait for the controller manager to update `ca.crt` in the service account Secrets to include both old and new CA certificates.

   If any Pods are started before new CA is used by API servers, the new Pods get this update and will trust both
   old and new CAs.
4. Restart all pods using in-cluster configurations (for example: kube-proxy, CoreDNS, etc) so they can use the
   updated certificate authority data from Secrets that link to ServiceAccounts.

   * Make sure CoreDNS, kube-proxy and other Pods using in-cluster configurations are working as expected.
5. Append the both old and new CA to the file against `--client-ca-file` and `--kubelet-certificate-authority`
   flag in the `kube-apiserver` configuration.
6. Append the both old and new CA to the file against `--client-ca-file` flag in the `kube-scheduler` configuration.
7. Update certificates for user accounts by replacing the content of `client-certificate-data` and `client-key-data`
   respectively.

   For information about creating certificates for individual user accounts, see
   [Configure certificates for user accounts](/docs/setup/best-practices/certificates/#configure-certificates-for-user-accounts).

   Additionally, update the `certificate-authority-data` section in the kubeconfig files,
   respectively with Base64-encoded old and new certificate authority data
8. Update the `--root-ca-file` flag for the [Cloud Controller Manager](/docs/concepts/architecture/cloud-controller/ "Control plane component that integrates Kubernetes with third-party cloud providers.") to include
   both old and new CA, then restart the cloud-controller-manager.

   > **Note:**
   > If your cluster does not have a cloud-controller-manager, you can skip this step.
9. Follow the steps below in a rolling fashion.

   1. Restart any other
      [aggregated API servers](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) or
      webhook handlers to trust the new CA certificates.
   2. Restart the kubelet by update the file against `clientCAFile` in kubelet configuration and
      `certificate-authority-data` in `kubelet.conf` to use both the old and new CA on all nodes.

      If your kubelet is not using client certificate rotation, update `client-certificate-data` and
      `client-key-data` in `kubelet.conf` on all nodes along with the kubelet client certificate file
      usually found in `/var/lib/kubelet/pki`.
   3. Restart API servers with the certificates (`apiserver.crt`, `apiserver-kubelet-client.crt` and
      `front-proxy-client.crt`) signed by new CA.
      You can use the existing private keys or new private keys.
      If you changed the private keys then update these in the Kubernetes certificates directory as well.

      Since the Pods in your cluster trust both old and new CAs, there will be a momentarily disconnection
      after which pods' Kubernetes clients reconnect to the new API server.
      The new API server uses a certificate signed by the new CA.

      * Restart the [kube-scheduler](/docs/reference/command-line-tools-reference/kube-scheduler/ "Control plane component that watches for newly created pods with no assigned node, and selects a node for them to run on.") to use and
        trust the new CAs.
      * Make sure control plane components logs no TLS errors.

      > **Note:**
      > ```
      > To generate certificates and private keys for your cluster using the `openssl` command line tool,
      > see [Certificates (`openssl`)](/docs/tasks/administer-cluster/certificates/#openssl).
      > You can also use [`cfssl`](/docs/tasks/administer-cluster/certificates/#cfssl).
      > ```
   4. Annotate any DaemonSets and Deployments to trigger pod replacement in a safer rolling fashion.

   ```
   for namespace in $(kubectl get namespace -o jsonpath='{.items[*].metadata.name}'); do
       for name in $(kubectl get deployments -n $namespace -o jsonpath='{.items[*].metadata.name}'); do
           kubectl patch deployment -n ${namespace} ${name} -p '{"spec":{"template":{"metadata":{"annotations":{"ca-rotation": "1"}}}}}';
       done
       for name in $(kubectl get daemonset -n $namespace -o jsonpath='{.items[*].metadata.name}'); do
           kubectl patch daemonset -n ${namespace} ${name} -p '{"spec":{"template":{"metadata":{"annotations":{"ca-rotation": "1"}}}}}';
       done
   done
   ```

   > **Note:**
   > ```
   > To limit the number of concurrent disruptions that your application experiences,
   > see [configure pod disruption budget](/docs/tasks/run-application/configure-pdb/).
   > ```

   ```
    Depending on how you use StatefulSets you may also need to perform similar rolling replacement.
   ```
10. If your cluster is using bootstrap tokens to join nodes, update the ConfigMap `cluster-info` in the `kube-public`
    namespace with new CA.

    ```
    base64_encoded_ca="$(base64 -w0 /etc/kubernetes/pki/ca.crt)"

    kubectl get cm/cluster-info --namespace kube-public -o yaml | \
        /bin/sed "s/\(certificate-authority-data:\).*/\1 ${base64_encoded_ca}/" | \
        kubectl apply -f -
    ```
11. Verify the cluster functionality.

    1. Check the logs from control plane components, along with the kubelet and the kube-proxy.
       Ensure those components are not reporting any TLS errors; see
       [looking at the logs](/docs/tasks/debug/debug-cluster/#looking-at-logs) for more details.
    2. Validate logs from any aggregated api servers and pods using in-cluster config.
12. Once the cluster functionality is successfully verified:

    1. Update all service account tokens to include new CA certificate only.

       * All pods using an in-cluster kubeconfig will eventually need to be restarted to pick up the new Secret,
         so that no Pods are relying on the old cluster CA.
    2. Restart the control plane components by removing the old CA from the kubeconfig files and the files against
       `--client-ca-file`, `--root-ca-file` flags resp.
    3. On each node, restart the kubelet by removing the old CA from file against the `clientCAFile` flag
       and from the kubelet kubeconfig file. You should carry this out as a rolling update.

       If your cluster lets you make this change, you can also roll it out by replacing nodes rather than
       reconfiguring them.

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
