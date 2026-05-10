# PodCertificateRequest v1alpha1

PodCertificateRequest encodes a pod requesting a certificate from a given signer.

`apiVersion: certificates.k8s.io/v1alpha1`

`import "k8s.io/api/certificates/v1alpha1"`

## PodCertificateRequest

PodCertificateRequest encodes a pod requesting a certificate from a given signer.

Kubelets use this API to implement podCertificate projected volumes

---

* **apiVersion**: certificates.k8s.io/v1alpha1
* **kind**: PodCertificateRequest
* **metadata** ([ObjectMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta))

  metadata contains the object metadata.
* **spec** ([PodCertificateRequestSpec](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequestSpec)), required

  spec contains the details about the certificate being requested.
* **status** ([PodCertificateRequestStatus](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequestStatus))

  status contains the issued certificate, and a standard set of conditions.

## PodCertificateRequestSpec

PodCertificateRequestSpec describes the certificate request. All fields are immutable after creation.

---

* **nodeName** (string), required

  nodeName is the name of the node the pod is assigned to.
* **nodeUID** (string), required

  nodeUID is the UID of the node the pod is assigned to.
* **pkixPublicKey** ([]byte), required

  pkixPublicKey is the PKIX-serialized public key the signer will issue the certificate to.

  The key must be one of RSA3072, RSA4096, ECDSAP256, ECDSAP384, ECDSAP521, or ED25519. Note that this list may be expanded in the future.

  Signer implementations do not need to support all key types supported by kube-apiserver and kubelet. If a signer does not support the key type used for a given PodCertificateRequest, it must deny the request by setting a status.conditions entry with a type of "Denied" and a reason of "UnsupportedKeyType". It may also suggest a key type that it does support in the message field.
* **podName** (string), required

  podName is the name of the pod into which the certificate will be mounted.
* **podUID** (string), required

  podUID is the UID of the pod into which the certificate will be mounted.
* **proofOfPossession** ([]byte), required

  proofOfPossession proves that the requesting kubelet holds the private key corresponding to pkixPublicKey.

  It is contructed by signing the ASCII bytes of the pod's UID using `pkixPublicKey`.

  kube-apiserver validates the proof of possession during creation of the PodCertificateRequest.

  If the key is an RSA key, then the signature is over the ASCII bytes of the pod UID, using RSASSA-PSS from RFC 8017 (as implemented by the golang function crypto/rsa.SignPSS with nil options).

  If the key is an ECDSA key, then the signature is as described by [SEC 1, Version 2.0](https://www.secg.org/sec1-v2.pdf) (as implemented by the golang library function crypto/ecdsa.SignASN1)

  If the key is an ED25519 key, the the signature is as described by the [ED25519 Specification](https://ed25519.cr.yp.to/) (as implemented by the golang library crypto/ed25519.Sign).
* **serviceAccountName** (string), required

  serviceAccountName is the name of the service account the pod is running as.
* **serviceAccountUID** (string), required

  serviceAccountUID is the UID of the service account the pod is running as.
* **signerName** (string), required

  signerName indicates the requested signer.

  All signer names beginning with `kubernetes.io` are reserved for use by the Kubernetes project. There is currently one well-known signer documented by the Kubernetes project, `kubernetes.io/kube-apiserver-client-pod`, which will issue client certificates understood by kube-apiserver. It is currently unimplemented.
* **maxExpirationSeconds** (int32)

  maxExpirationSeconds is the maximum lifetime permitted for the certificate.

  If omitted, kube-apiserver will set it to 86400(24 hours). kube-apiserver will reject values shorter than 3600 (1 hour). The maximum allowable value is 7862400 (91 days).

  The signer implementation is then free to issue a certificate with any lifetime *shorter* than MaxExpirationSeconds, but no shorter than 3600 seconds (1 hour). This constraint is enforced by kube-apiserver. `kubernetes.io` signers will never issue certificates with a lifetime longer than 24 hours.

## PodCertificateRequestStatus

PodCertificateRequestStatus describes the status of the request, and holds the certificate data if the request is issued.

---

* **beginRefreshAt** (Time)

  beginRefreshAt is the time at which the kubelet should begin trying to refresh the certificate. This field is set via the /status subresource, and must be set at the same time as certificateChain. Once populated, this field is immutable.

  This field is only a hint. Kubelet may start refreshing before or after this time if necessary.

  *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
* **certificateChain** (string)

  certificateChain is populated with an issued certificate by the signer. This field is set via the /status subresource. Once populated, this field is immutable.

  If the certificate signing request is denied, a condition of type "Denied" is added and this field remains empty. If the signer cannot issue the certificate, a condition of type "Failed" is added and this field remains empty.

  Validation requirements:

  1. certificateChain must consist of one or more PEM-formatted certificates.
  2. Each entry must be a valid PEM-wrapped, DER-encoded ASN.1 Certificate as
     described in section 4 of RFC5280.

  If more than one block is present, and the definition of the requested spec.signerName does not indicate otherwise, the first block is the issued certificate, and subsequent blocks should be treated as intermediate certificates and presented in TLS handshakes. When projecting the chain into a pod volume, kubelet will drop any data in-between the PEM blocks, as well as any PEM block headers.
* **conditions** ([]Condition)

  *Patch strategy: merge on key `type`*

  *Map: unique values on key type will be kept during a merge*

  conditions applied to the request.

  The types "Issued", "Denied", and "Failed" have special handling. At most one of these conditions may be present, and they must have status "True".

  If the request is denied with `Reason=UnsupportedKeyType`, the signer may suggest a key type that will work in the message field.

  *Condition contains details for one aspect of the current state of this API Resource.*

  + **conditions.lastTransitionTime** (Time), required

    lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.

    *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
  + **conditions.message** (string), required

    message is a human readable message indicating details about the transition. This may be an empty string.
  + **conditions.reason** (string), required

    reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.
  + **conditions.status** (string), required

    status of the condition, one of True, False, Unknown.
  + **conditions.type** (string), required

    type of condition in CamelCase or in foo.example.com/CamelCase.
  + **conditions.observedGeneration** (int64)

    observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.
* **notAfter** (Time)

  notAfter is the time at which the certificate expires. The value must be the same as the notAfter value in the leaf certificate in certificateChain. This field is set via the /status subresource. Once populated, it is immutable. The signer must set this field at the same time it sets certificateChain.

  *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*
* **notBefore** (Time)

  notBefore is the time at which the certificate becomes valid. The value must be the same as the notBefore value in the leaf certificate in certificateChain. This field is set via the /status subresource. Once populated, it is immutable. The signer must set this field at the same time it sets certificateChain.

  *Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.*

## PodCertificateRequestList

PodCertificateRequestList is a collection of PodCertificateRequest objects

---

* **apiVersion**: certificates.k8s.io/v1alpha1
* **kind**: PodCertificateRequestList
* **metadata** ([ListMeta](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-definitions/list-meta/#ListMeta))

  metadata contains the list metadata.
* **items** ([][PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest)), required

  items is a collection of PodCertificateRequest objects

## Operations

---

### `get` read the specified PodCertificateRequest

#### HTTP Request

GET /apis/certificates.k8s.io/v1alpha1/namespaces/{namespace}/podcertificaterequests/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the PodCertificateRequest
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest)): OK

401: Unauthorized

### `get` read status of the specified PodCertificateRequest

#### HTTP Request

GET /apis/certificates.k8s.io/v1alpha1/namespaces/{namespace}/podcertificaterequests/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the PodCertificateRequest
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest)): OK

401: Unauthorized

### `list` list or watch objects of kind PodCertificateRequest

#### HTTP Request

GET /apis/certificates.k8s.io/v1alpha1/namespaces/{namespace}/podcertificaterequests

#### Parameters

* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
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

200 ([PodCertificateRequestList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequestList)): OK

401: Unauthorized

### `list` list or watch objects of kind PodCertificateRequest

#### HTTP Request

GET /apis/certificates.k8s.io/v1alpha1/podcertificaterequests

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

200 ([PodCertificateRequestList](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequestList)): OK

401: Unauthorized

### `create` create a PodCertificateRequest

#### HTTP Request

POST /apis/certificates.k8s.io/v1alpha1/namespaces/{namespace}/podcertificaterequests

#### Parameters

* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest)): OK

201 ([PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest)): Created

202 ([PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest)): Accepted

401: Unauthorized

### `update` replace the specified PodCertificateRequest

#### HTTP Request

PUT /apis/certificates.k8s.io/v1alpha1/namespaces/{namespace}/podcertificaterequests/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the PodCertificateRequest
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest)): OK

201 ([PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest)): Created

401: Unauthorized

### `update` replace status of the specified PodCertificateRequest

#### HTTP Request

PUT /apis/certificates.k8s.io/v1alpha1/namespaces/{namespace}/podcertificaterequests/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the PodCertificateRequest
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
* **body**: [PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest), required
* **dryRun** (*in query*): string

  [dryRun](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#dryRun)
* **fieldManager** (*in query*): string

  [fieldManager](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldManager)
* **fieldValidation** (*in query*): string

  [fieldValidation](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#fieldValidation)
* **pretty** (*in query*): string

  [pretty](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#pretty)

#### Response

200 ([PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest)): OK

201 ([PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest)): Created

401: Unauthorized

### `patch` partially update the specified PodCertificateRequest

#### HTTP Request

PATCH /apis/certificates.k8s.io/v1alpha1/namespaces/{namespace}/podcertificaterequests/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the PodCertificateRequest
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
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

200 ([PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest)): OK

201 ([PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest)): Created

401: Unauthorized

### `patch` partially update status of the specified PodCertificateRequest

#### HTTP Request

PATCH /apis/certificates.k8s.io/v1alpha1/namespaces/{namespace}/podcertificaterequests/{name}/status

#### Parameters

* **name** (*in path*): string, required

  name of the PodCertificateRequest
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
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

200 ([PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest)): OK

201 ([PodCertificateRequest](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1alpha1/#PodCertificateRequest)): Created

401: Unauthorized

### `delete` delete a PodCertificateRequest

#### HTTP Request

DELETE /apis/certificates.k8s.io/v1alpha1/namespaces/{namespace}/podcertificaterequests/{name}

#### Parameters

* **name** (*in path*): string, required

  name of the PodCertificateRequest
* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
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

### `deletecollection` delete collection of PodCertificateRequest

#### HTTP Request

DELETE /apis/certificates.k8s.io/v1alpha1/namespaces/{namespace}/podcertificaterequests

#### Parameters

* **namespace** (*in path*): string, required

  [namespace](https://v1-34.docs.kubernetes.io/docs/reference/kubernetes-api/common-parameters/common-parameters/#namespace)
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
