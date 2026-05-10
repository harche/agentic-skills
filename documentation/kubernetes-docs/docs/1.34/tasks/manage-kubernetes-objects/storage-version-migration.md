# Migrate Kubernetes Objects Using Storage Version Migration

FEATURE STATE:
`Kubernetes v1.30 [alpha]`(disabled by default)

Kubernetes relies on API data being actively re-written, to support some
maintenance activities related to at rest storage. Two prominent examples are
the versioned schema of stored resources (that is, the preferred storage schema
changing from v1 to v2 for a given resource) and encryption at rest
(that is, rewriting stale data based on a change in how the data should be encrypted).

## Before you begin

Install [`kubectl`](/docs/tasks/tools/#kubectl).

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [KodeKloud](https://kodekloud.com/public-playgrounds)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)

Your Kubernetes server must be at or later than version v1.30.

To check the version, enter `kubectl version`.

Ensure that your cluster has the `StorageVersionMigrator` and `InformerResourceVersion`
[feature gates](/docs/reference/command-line-tools-reference/feature-gates/)
enabled. You will need control plane administrator access to make that change.

Enable storage version migration REST api by setting runtime config
`storagemigration.k8s.io/v1alpha1` to `true` for the API server. For more information on
how to do that,
read [enable or disable a Kubernetes API](/docs/tasks/administer-cluster/enable-disable-api/).

## Re-encrypt Kubernetes secrets using storage version migration

* To begin with, [configure KMS provider](/docs/tasks/administer-cluster/kms-provider/)
  to encrypt data at rest in etcd using following encryption configuration.

  ```
  kind: EncryptionConfiguration
  apiVersion: apiserver.config.k8s.io/v1
  resources:
  - resources:
    - secrets
    providers:
    - aescbc:
        keys:
        - name: key1
          secret: c2VjcmV0IGlzIHNlY3VyZQ==
  ```

  Make sure to enable automatic reload of encryption
  configuration file by setting `--encryption-provider-config-automatic-reload` to true.
* Create a Secret using kubectl.

  ```
  kubectl create secret generic my-secret --from-literal=key1=supersecret
  ```
* [Verify](/docs/tasks/administer-cluster/kms-provider/#verifying-that-the-data-is-encrypted)
  the serialized data for that Secret object is prefixed with `k8s:enc:aescbc:v1:key1`.
* Update the encryption configuration file as follows to rotate the encryption key.

  ```
  kind: EncryptionConfiguration
  apiVersion: apiserver.config.k8s.io/v1
  resources:
  - resources:
    - secrets
    providers:
    - aescbc:
        keys:
        - name: key2
          secret: c2VjcmV0IGlzIHNlY3VyZSwgaXMgaXQ/
    - aescbc:
        keys:
        - name: key1
          secret: c2VjcmV0IGlzIHNlY3VyZQ==
  ```
* To ensure that previously created secret `my-secret` is re-encrypted
  with new key `key2`, you will use *Storage Version Migration*.
* Create a StorageVersionMigration manifest named `migrate-secret.yaml` as follows:

  ```
  kind: StorageVersionMigration
  apiVersion: storagemigration.k8s.io/v1alpha1
  metadata:
    name: secrets-migration
  spec:
    resource:
      group: ""
      version: v1
      resource: secrets
  ```

  Create the object using *kubectl* as follows:

  ```
  kubectl apply -f migrate-secret.yaml
  ```
* Monitor migration of Secrets by checking the `.status` of the StorageVersionMigration.
  A successful migration should have its
  `Succeeded` condition set to true. Get the StorageVersionMigration object as follows:

  ```
  kubectl get storageversionmigration.storagemigration.k8s.io/secrets-migration -o yaml
  ```

  The output is similar to:

  ```
  kind: StorageVersionMigration
  apiVersion: storagemigration.k8s.io/v1alpha1
  metadata:
    name: secrets-migration
    uid: 628f6922-a9cb-4514-b076-12d3c178967c
    resourceVersion: "90"
    creationTimestamp: "2024-03-12T20:29:45Z"
  spec:
    resource:
      group: ""
      version: v1
      resource: secrets
  status:
    conditions:
    - type: Running
      status: "False"
      lastUpdateTime: "2024-03-12T20:29:46Z"
      reason: StorageVersionMigrationInProgress
    - type: Succeeded
      status: "True"
      lastUpdateTime: "2024-03-12T20:29:46Z"
      reason: StorageVersionMigrationSucceeded
    resourceVersion: "84"
  ```
* [Verify](/docs/tasks/administer-cluster/kms-provider/#verifying-that-the-data-is-encrypted)
  the stored secret is now prefixed with `k8s:enc:aescbc:v1:key2`.

## Update the preferred storage schema of a CRD

Consider a scenario where a [CustomResourceDefinition](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/ "Custom code that defines a resource to add to your Kubernetes API server without building a complete custom server.")
(CRD) is created to serve custom resources (CRs) and is set as the preferred storage schema. When it's time
to introduce v2 of the CRD, it can be added for serving only with a conversion
webhook. This enables a smoother transition where users can create CRs using
either the v1 or v2 schema, with the webhook in place to perform the necessary
schema conversion between them. Before setting v2 as the preferred storage schema
version, it's important to ensure that all existing CRs stored as v1 are migrated to v2.
This migration can be achieved through *Storage Version Migration* to migrate all CRs from v1 to v2.

* Create a manifest for the CRD, named `test-crd.yaml`, as follows:

  ```
  apiVersion: apiextensions.k8s.io/v1
  kind: CustomResourceDefinition
  metadata:
    name: selfierequests.stable.example.com
  spec:
    group: stable.example.com
    names:
      plural: SelfieRequests
      singular: SelfieRequest
      kind: SelfieRequest
      listKind: SelfieRequestList
    scope: Namespaced
    versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            hostPort:
              type: string
    conversion:
      strategy: Webhook
      webhook:
        clientConfig:
          url: "https://127.0.0.1:9443/crdconvert"
          caBundle: <CABundle info>
      conversionReviewVersions:
      - v1
      - v2
  ```

  Create CRD using kubectl:

  ```
  kubectl apply -f test-crd.yaml
  ```
* Create a manifest for an example testcrd. Name the manifest `cr1.yaml` and use these contents:

  ```
  apiVersion: stable.example.com/v1
  kind: SelfieRequest
  metadata:
    name: cr1
    namespace: default
  ```

  Create CR using kubectl:

  ```
  kubectl apply -f cr1.yaml
  ```
* Verify that CR is written and stored as v1 by getting the object from etcd.

  ```
  ETCDCTL_API=3 etcdctl get /kubernetes.io/stable.example.com/testcrds/default/cr1 [...] | hexdump -C
  ```

  where `[...]` contains the additional arguments for connecting to the etcd server.
* Update the CRD `test-crd.yaml` to include v2 version for serving and storage
  and v1 as serving only, as follows:

  ```
  apiVersion: apiextensions.k8s.io/v1
  kind: CustomResourceDefinition
  metadata:
  name: selfierequests.stable.example.com
  spec:
    group: stable.example.com
    names:
      plural: SelfieRequests
      singular: SelfieRequest
      kind: SelfieRequest
      listKind: SelfieRequestList
    scope: Namespaced
    versions:
      - name: v2
        served: true
        storage: true
        schema:
          openAPIV3Schema:
            type: object
            properties:
              host:
                type: string
              port:
                type: string
      - name: v1
        served: true
        storage: false
        schema:
          openAPIV3Schema:
            type: object
            properties:
              hostPort:
                type: string
    conversion:
      strategy: Webhook
      webhook:
        clientConfig:
          url: "https://127.0.0.1:9443/crdconvert"
          caBundle: <CABundle info>
        conversionReviewVersions:
          - v1
          - v2
  ```

  Update CRD using kubectl:

  ```
  kubectl apply -f test-crd.yaml
  ```
* Create CR resource file with name `cr2.yaml` as follows:

  ```
  apiVersion: stable.example.com/v2
  kind: SelfieRequest
  metadata:
    name: cr2
    namespace: default
  ```
* Create CR using kubectl:

  ```
  kubectl apply -f cr2.yaml
  ```
* Verify that CR is written and stored as v2 by getting the object from etcd.

  ```
  ETCDCTL_API=3 etcdctl get /kubernetes.io/stable.example.com/testcrds/default/cr2 [...] | hexdump -C
  ```

  where `[...]` contains the additional arguments for connecting to the etcd server.
* Create a StorageVersionMigration manifest named `migrate-crd.yaml`, with the contents as follows:

  ```
  kind: StorageVersionMigration
  apiVersion: storagemigration.k8s.io/v1alpha1
  metadata:
    name: crdsvm
  spec:
    resource:
      group: stable.example.com
      version: v1
      resource: SelfieRequest
  ```

  Create the object using *kubectl* as follows:

  ```
  kubectl apply -f migrate-crd.yaml
  ```
* Monitor migration of secrets using status. Successful migration should have
  `Succeeded` condition set to "True" in the status field. Get the migration resource
  as follows:

  ```
  kubectl get storageversionmigration.storagemigration.k8s.io/crdsvm -o yaml
  ```

  The output is similar to:

  ```
  kind: StorageVersionMigration
  apiVersion: storagemigration.k8s.io/v1alpha1
  metadata:
    name: crdsvm
    uid: 13062fe4-32d7-47cc-9528-5067fa0c6ac8
    resourceVersion: "111"
    creationTimestamp: "2024-03-12T22:40:01Z"
  spec:
    resource:
      group: stable.example.com
      version: v1
      resource: testcrds
  status:
    conditions:
      - type: Running
        status: "False"
        lastUpdateTime: "2024-03-12T22:40:03Z"
        reason: StorageVersionMigrationInProgress
      - type: Succeeded
        status: "True"
        lastUpdateTime: "2024-03-12T22:40:03Z"
        reason: StorageVersionMigrationSucceeded
    resourceVersion: "106"
  ```
* Verify that previously created cr1 is now written and stored as v2 by getting the object from etcd.

  ```
  ETCDCTL_API=3 etcdctl get /kubernetes.io/stable.example.com/testcrds/default/cr1 [...] | hexdump -C
  ```

  where `[...]` contains the additional arguments for connecting to the etcd server.

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
