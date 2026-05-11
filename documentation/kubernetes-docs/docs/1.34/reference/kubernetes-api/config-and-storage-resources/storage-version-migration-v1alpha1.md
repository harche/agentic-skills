# StorageVersionMigration v1alpha1

StorageVersionMigration represents a migration of stored data to the latest storage version.

`apiVersion: storagemigration.k8s.io/v1alpha1`

`import "k8s.io/api/storagemigration/v1alpha1"`

## StorageVersionMigration

StorageVersionMigration represents a migration of stored data to the latest storage version.

---

* **apiVersion**: storagemigration.k8s.io/v1alpha1
* **kind**: StorageVersionMigration
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  Standard object metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **spec** ([StorageVersionMigrationSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigrationSpec))

  Specification of the migration.
* **status** ([StorageVersionMigrationStatus](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigrationStatus))

  Status of the migration.

## StorageVersionMigrationSpec

Spec of the storage version migration.

---

* **continueToken** (string)

  The token used in the list options to get the next chunk of objects to migrate. When the .status.conditions indicates the migration is "Running", users can use this token to check the progress of the migration.
* **resource** (GroupVersionResource), required

  The resource that is being migrated. The migrator sends requests to the endpoint serving the resource. Immutable.

  *The names of the group, the version, and the resource.*

  + **resource.group** (string)

    The name of the group.
  + **resource.resource** (string)

    The name of the resource.
  + **resource.version** (string)

    The name of the version.

## StorageVersionMigrationStatus

Status of the storage version migration.

---

* **conditions** ([]MigrationCondition)

  *Patch strategy: merge on key `type`*

  *Map: unique values on key type will be kept during a merge*

  The latest available observations of the migration's current state.

  *Describes the state of a migration at a certain point.*

  + **conditions.status** (string), required

    Status of the condition, one of True, False, Unknown.
  + **conditions.type** (string), required

    Type of the condition.
  + **conditions.lastUpdateTime** (Time)

    The last time this condition was updated.

    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
  + **conditions.message** (string)

    A human readable message indicating details about the transition.
  + **conditions.reason** (string)

    The reason for the condition's last transition.
* **resourceVersion** (string)

  ResourceVersion to compare with the GC cache for performing the migration. This is the current resource version of given group, version and resource when kube-controller-manager first observes this StorageVersionMigration resource.

## StorageVersionMigrationList

StorageVersionMigrationList is a collection of storage version migrations.

---

* **apiVersion**: storagemigration.k8s.io/v1alpha1
* **kind**: StorageVersionMigrationList
* **metadata** ([ListMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/#ListMeta))

  Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>
* **items** ([][StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration)), required

  *Patch strategy: merge on key `type`*

  *Map: unique values on key type will be kept during a merge*

  Items is the list of StorageVersionMigration

## Operations

---

### `get` read the specified StorageVersionMigration

#### HTTP Request

GET /apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the StorageVersionMigration
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration)): OK

401: Unauthorized

### `get` read status of the specified StorageVersionMigration

#### HTTP Request

GET /apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the StorageVersionMigration
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration)): OK

401: Unauthorized

### `list` list or watch objects of kind StorageVersionMigration

#### HTTP Request

GET /apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations

#### Parameters

* **allowWatchBookmarks** (*in query*): boolean

  [allowWatchBookmarks](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#allowWatchBookmarks)
* **continue** (*in query*): string

  [continue](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#continue)
* **fieldSelector** (*in query*): string

  [fieldSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldSelector)
* **labelSelector** (*in query*): string

  [labelSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#labelSelector)
* **limit** (*in query*): integer

  [limit](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#limit)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)
* **resourceVersion** (*in query*): string

  [resourceVersion](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#resourceVersion)
* **resourceVersionMatch** (*in query*): string

  [resourceVersionMatch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#resourceVersionMatch)
* **sendInitialEvents** (*in query*): boolean

  [sendInitialEvents](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#sendInitialEvents)
* **timeoutSeconds** (*in query*): integer

  [timeoutSeconds](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#timeoutSeconds)
* **watch** (*in query*): boolean

  [watch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#watch)

#### Response

200 ([StorageVersionMigrationList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigrationList)): OK

401: Unauthorized

### `create` create a StorageVersionMigration

#### HTTP Request

POST /apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations

#### Parameters

* **body**: [StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration)): OK

201 ([StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration)): Created

202 ([StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration)): Accepted

401: Unauthorized

### `update` replace the specified StorageVersionMigration

#### HTTP Request

PUT /apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the StorageVersionMigration
* **body**: [StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration)): OK

201 ([StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration)): Created

401: Unauthorized

### `update` replace status of the specified StorageVersionMigration

#### HTTP Request

PUT /apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the StorageVersionMigration
* **body**: [StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration)): OK

201 ([StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration)): Created

401: Unauthorized

### `patch` partially update the specified StorageVersionMigration

#### HTTP Request

PATCH /apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the StorageVersionMigration
* **body**: [Patch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/patch/#Patch), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **force** (*in query*): boolean

  [force](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#force)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration)): OK

201 ([StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration)): Created

401: Unauthorized

### `patch` partially update status of the specified StorageVersionMigration

#### HTTP Request

PATCH /apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the StorageVersionMigration
* **body**: [Patch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/patch/#Patch), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **force** (*in query*): boolean

  [force](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#force)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration)): OK

201 ([StorageVersionMigration](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1alpha1/#StorageVersionMigration)): Created

401: Unauthorized

### `delete` delete a StorageVersionMigration

#### HTTP Request

DELETE /apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the StorageVersionMigration
* **body**: [DeleteOptions](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/delete-options/#DeleteOptions)
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **gracePeriodSeconds** (*in query*): integer

  [gracePeriodSeconds](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#gracePeriodSeconds)
* **ignoreStoreReadErrorWithClusterBreakingPotential** (*in query*): boolean

  [ignoreStoreReadErrorWithClusterBreakingPotential](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#ignoreStoreReadErrorWithClusterBreakingPotential)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)
* **propagationPolicy** (*in query*): string

  [propagationPolicy](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#propagationPolicy)

#### Response

200 ([Status](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/status/#Status)): OK

202 ([Status](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/status/#Status)): Accepted

401: Unauthorized

### `deletecollection` delete collection of StorageVersionMigration

#### HTTP Request

DELETE /apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations

#### Parameters

* **body**: [DeleteOptions](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/delete-options/#DeleteOptions)
* **continue** (*in query*): string

  [continue](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#continue)
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldSelector** (*in query*): string

  [fieldSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldSelector)
* **gracePeriodSeconds** (*in query*): integer

  [gracePeriodSeconds](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#gracePeriodSeconds)
* **ignoreStoreReadErrorWithClusterBreakingPotential** (*in query*): boolean

  [ignoreStoreReadErrorWithClusterBreakingPotential](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#ignoreStoreReadErrorWithClusterBreakingPotential)
* **labelSelector** (*in query*): string

  [labelSelector](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#labelSelector)
* **limit** (*in query*): integer

  [limit](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#limit)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)
* **propagationPolicy** (*in query*): string

  [propagationPolicy](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#propagationPolicy)
* **resourceVersion** (*in query*): string

  [resourceVersion](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#resourceVersion)
* **resourceVersionMatch** (*in query*): string

  [resourceVersionMatch](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#resourceVersionMatch)
* **sendInitialEvents** (*in query*): boolean

  [sendInitialEvents](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#sendInitialEvents)
* **timeoutSeconds** (*in query*): integer

  [timeoutSeconds](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#timeoutSeconds)

#### Response

200 ([Status](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/status/#Status)): OK

401: Unauthorized

This page is automatically generated.

If you plan to report an issue with this page, mention that the page is auto-generated in your issue description. The fix may need to happen elsewhere in the Kubernetes project.

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
