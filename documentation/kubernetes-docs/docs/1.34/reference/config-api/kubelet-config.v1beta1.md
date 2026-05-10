# Kubelet Configuration (v1beta1)

## Resource Types

* [CredentialProviderConfig](#kubelet-config-k8s-io-v1beta1-CredentialProviderConfig)
* [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)
* [SerializedNodeConfigSource](#kubelet-config-k8s-io-v1beta1-SerializedNodeConfigSource)

## `FormatOptions`

**Appears in:**

* [LoggingConfiguration](#LoggingConfiguration)

FormatOptions contains options for the different logging formats.

| Field | Description |
| --- | --- |
| `text` **[Required]**  [`TextOptions`](#TextOptions) | [Alpha] Text contains options for logging format "text". Only available when the LoggingAlphaOptions feature gate is enabled. |
| `json` **[Required]**  [`JSONOptions`](#JSONOptions) | [Alpha] JSON contains options for logging format "json". Only available when the LoggingAlphaOptions feature gate is enabled. |

## `JSONOptions`

**Appears in:**

* [FormatOptions](#FormatOptions)

JSONOptions contains options for logging format "json".

| Field | Description |
| --- | --- |
| `OutputRoutingOptions` **[Required]**  [`OutputRoutingOptions`](#OutputRoutingOptions) | (Members of `OutputRoutingOptions` are embedded into this type.) No description provided. |

## `LogFormatFactory`

LogFormatFactory provides support for a certain additional,
non-default log format.

## `LoggingConfiguration`

**Appears in:**

* [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)

LoggingConfiguration contains logging options.

| Field | Description |
| --- | --- |
| `format` **[Required]**  `string` | Format Flag specifies the structure of log messages. default value of format is `text` |
| `flushFrequency` **[Required]**  [`TimeOrMetaDuration`](#TimeOrMetaDuration) | Maximum time between log flushes. If a string, parsed as a duration (i.e. "1s") If an int, the maximum number of nanoseconds (i.e. 1s = 1000000000). Ignored if the selected logging backend writes log messages without buffering. |
| `verbosity` **[Required]**  [`VerbosityLevel`](#VerbosityLevel) | Verbosity is the threshold that determines which log messages are logged. Default is zero which logs only the most important messages. Higher values enable additional messages. Error messages are always logged. |
| `vmodule` **[Required]**  [`VModuleConfiguration`](#VModuleConfiguration) | VModule overrides the verbosity threshold for individual files. Only supported for "text" log format. |
| `options` **[Required]**  [`FormatOptions`](#FormatOptions) | [Alpha] Options holds additional parameters that are specific to the different logging formats. Only the options for the selected format get used, but all of them get validated. Only available when the LoggingAlphaOptions feature gate is enabled. |

## `LoggingOptions`

LoggingOptions can be used with ValidateAndApplyWithOptions to override
certain global defaults.

| Field | Description |
| --- | --- |
| `ErrorStream` **[Required]**  [`io.Writer`](https://pkg.go.dev/io#Writer) | ErrorStream can be used to override the os.Stderr default. |
| `InfoStream` **[Required]**  [`io.Writer`](https://pkg.go.dev/io#Writer) | InfoStream can be used to override the os.Stdout default. |

## `OutputRoutingOptions`

**Appears in:**

* [JSONOptions](#JSONOptions)
* [TextOptions](#TextOptions)

OutputRoutingOptions contains options that are supported by both "text" and "json".

| Field | Description |
| --- | --- |
| `splitStream` **[Required]**  `bool` | [Alpha] SplitStream redirects error messages to stderr while info messages go to stdout, with buffering. The default is to write both to stdout, without buffering. Only available when the LoggingAlphaOptions feature gate is enabled. |
| `infoBufferSize` **[Required]**  [`k8s.io/apimachinery/pkg/api/resource.QuantityValue`](https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#QuantityValue) | [Alpha] InfoBufferSize sets the size of the info stream when using split streams. The default is zero, which disables buffering. Only available when the LoggingAlphaOptions feature gate is enabled. |

## `TextOptions`

**Appears in:**

* [FormatOptions](#FormatOptions)

TextOptions contains options for logging format "text".

| Field | Description |
| --- | --- |
| `OutputRoutingOptions` **[Required]**  [`OutputRoutingOptions`](#OutputRoutingOptions) | (Members of `OutputRoutingOptions` are embedded into this type.) No description provided. |

## `TimeOrMetaDuration`

**Appears in:**

* [LoggingConfiguration](#LoggingConfiguration)

TimeOrMetaDuration is present only for backwards compatibility for the
flushFrequency field, and new fields should use metav1.Duration.

| Field | Description |
| --- | --- |
| `Duration` **[Required]**  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | Duration holds the duration |
| `-` **[Required]**  `bool` | SerializeAsString controls whether the value is serialized as a string or an integer |

## `TracingConfiguration`

**Appears in:**

* [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)

TracingConfiguration provides versioned configuration for OpenTelemetry tracing clients.

| Field | Description |
| --- | --- |
| `endpoint`  `string` | Endpoint of the collector this component will report traces to. The connection is insecure, and does not currently support TLS. Recommended is unset, and endpoint is the otlp grpc default, localhost:4317. |
| `samplingRatePerMillion`  `int32` | SamplingRatePerMillion is the number of samples to collect per million spans. Recommended is unset. If unset, sampler respects its parent span's sampling rate, but otherwise never samples. |

## `VModuleConfiguration`

(Alias of `[]k8s.io/component-base/logs/api/v1.VModuleItem`)

**Appears in:**

* [LoggingConfiguration](#LoggingConfiguration)

VModuleConfiguration is a collection of individual file names or patterns
and the corresponding verbosity threshold.

## `VerbosityLevel`

(Alias of `uint32`)

**Appears in:**

* [LoggingConfiguration](#LoggingConfiguration)

VerbosityLevel represents a klog or logr verbosity threshold.

## `CredentialProviderConfig`

CredentialProviderConfig is the configuration containing information about
each exec credential provider. Kubelet reads this configuration from disk and enables
each provider as specified by the CredentialProvider type.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubelet.config.k8s.io/v1beta1` |
| `kind` string | `CredentialProviderConfig` |
| `providers` **[Required]**  [`[]CredentialProvider`](#kubelet-config-k8s-io-v1beta1-CredentialProvider) | providers is a list of credential provider plugins that will be enabled by the kubelet. Multiple providers may match against a single image, in which case credentials from all providers will be returned to the kubelet. If multiple providers are called for a single image, the results are combined. If providers return overlapping auth keys, the value from the provider earlier in this list is attempted first. |

## `KubeletConfiguration`

KubeletConfiguration contains the configuration for the Kubelet

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubelet.config.k8s.io/v1beta1` |
| `kind` string | `KubeletConfiguration` |
| `enableServer` **[Required]**  `bool` | enableServer enables Kubelet's secured server. Note: Kubelet's insecure port is controlled by the readOnlyPort option. Default: true |
| `staticPodPath`  `string` | staticPodPath is the path to the directory containing local (static) pods to run, or the path to a single static pod file. Default: "" |
| `podLogsDir`  `string` | podLogsDir is a custom root directory path kubelet will use to place pod's log files. Default: "/var/log/pods/" Note: it is not recommended to use the temp folder as a log directory as it may cause unexpected behavior in many places. |
| `syncFrequency`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | syncFrequency is the max period between synchronizing running containers and config. Default: "1m" |
| `fileCheckFrequency`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | fileCheckFrequency is the duration between checking config files for new data. Default: "20s" |
| `httpCheckFrequency`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | httpCheckFrequency is the duration between checking http for new data. Default: "20s" |
| `staticPodURL`  `string` | staticPodURL is the URL for accessing static pods to run. Default: "" |
| `staticPodURLHeader`  `map[string][]string` | staticPodURLHeader is a map of slices with HTTP headers to use when accessing the podURL. Default: nil |
| `address`  `string` | address is the IP address for the Kubelet to serve on (set to 0.0.0.0 for all interfaces). Default: "0.0.0.0" |
| `port`  `int32` | port is the port for the Kubelet to serve on. The port number must be between 1 and 65535, inclusive. Default: 10250 |
| `readOnlyPort`  `int32` | readOnlyPort is the read-only port for the Kubelet to serve on with no authentication/authorization. The port number must be between 1 and 65535, inclusive. Setting this field to 0 disables the read-only service. Default: 0 (disabled) |
| `tlsCertFile`  `string` | tlsCertFile is the file containing x509 Certificate for HTTPS. (CA cert, if any, concatenated after server cert). If tlsCertFile and tlsPrivateKeyFile are not provided, a self-signed certificate and key are generated for the public address and saved to the directory passed to the Kubelet's --cert-dir flag. Default: "" |
| `tlsPrivateKeyFile`  `string` | tlsPrivateKeyFile is the file containing x509 private key matching tlsCertFile. Default: "" |
| `tlsCipherSuites`  `[]string` | tlsCipherSuites is the list of allowed cipher suites for the server. Note that TLS 1.3 ciphersuites are not configurable. Values are from tls package constants (https://golang.org/pkg/crypto/tls/#pkg-constants). Default: nil |
| `tlsMinVersion`  `string` | tlsMinVersion is the minimum TLS version supported. Values are from tls package constants (https://golang.org/pkg/crypto/tls/#pkg-constants). Default: "" |
| `rotateCertificates`  `bool` | rotateCertificates enables client certificate rotation. The Kubelet will request a new certificate from the certificates.k8s.io API. This requires an approver to approve the certificate signing requests. Default: false |
| `serverTLSBootstrap`  `bool` | serverTLSBootstrap enables server certificate bootstrap. Instead of self signing a serving certificate, the Kubelet will request a certificate from the 'certificates.k8s.io' API. This requires an approver to approve the certificate signing requests (CSR). The RotateKubeletServerCertificate feature must be enabled when setting this field. Default: false |
| `authentication`  [`KubeletAuthentication`](#kubelet-config-k8s-io-v1beta1-KubeletAuthentication) | authentication specifies how requests to the Kubelet's server are authenticated. Defaults: anonymous: enabled: false webhook: enabled: true cacheTTL: "2m" |
| `authorization`  [`KubeletAuthorization`](#kubelet-config-k8s-io-v1beta1-KubeletAuthorization) | authorization specifies how requests to the Kubelet's server are authorized. Defaults: mode: Webhook webhook: cacheAuthorizedTTL: "5m" cacheUnauthorizedTTL: "30s" |
| `registryPullQPS`  `int32` | registryPullQPS is the limit of registry pulls per second. The value must not be a negative number. Setting it to 0 means no limit. Default: 5 |
| `registryBurst`  `int32` | registryBurst is the maximum size of bursty pulls, temporarily allows pulls to burst to this number, while still not exceeding registryPullQPS. The value must not be a negative number. Only used if registryPullQPS is greater than 0. Default: 10 |
| `imagePullCredentialsVerificationPolicy`  [`ImagePullCredentialsVerificationPolicy`](#kubelet-config-k8s-io-v1beta1-ImagePullCredentialsVerificationPolicy) | imagePullCredentialsVerificationPolicy determines how credentials should be verified when pod requests an image that is already present on the node:   * NeverVerify   + anyone on a node can use any image present on the node * NeverVerifyPreloadedImages   + images that were pulled to the node by something else than the kubelet     can be used without reverifying pull credentials * NeverVerifyAllowlistedImages   + like "NeverVerifyPreloadedImages" but only node images from     `preloadedImagesVerificationAllowlist` don't require reverification * AlwaysVerify   + all images require credential reverification |
| `preloadedImagesVerificationAllowlist`  `[]string` | preloadedImagesVerificationAllowlist specifies a list of images that are exempted from credential reverification for the "NeverVerifyAllowlistedImages" `imagePullCredentialsVerificationPolicy`. The list accepts a full path segment wildcard suffix "/*". Only use image specs without an image tag or digest. |
| `eventRecordQPS`  `int32` | eventRecordQPS is the maximum event creations per second. If 0, there is no limit enforced. The value cannot be a negative number. Default: 50 |
| `eventBurst`  `int32` | eventBurst is the maximum size of a burst of event creations, temporarily allows event creations to burst to this number, while still not exceeding eventRecordQPS. This field canot be a negative number and it is only used when eventRecordQPS > 0. Default: 100 |
| `enableDebuggingHandlers`  `bool` | enableDebuggingHandlers enables server endpoints for log access and local running of containers and commands, including the exec, attach, logs, and portforward features. Default: true |
| `enableContentionProfiling`  `bool` | enableContentionProfiling enables block profiling, if enableDebuggingHandlers is true. Default: false |
| `healthzPort`  `int32` | healthzPort is the port of the localhost healthz endpoint (set to 0 to disable). A valid number is between 1 and 65535. Default: 10248 |
| `healthzBindAddress`  `string` | healthzBindAddress is the IP address for the healthz server to serve on. Default: "127.0.0.1" |
| `oomScoreAdj`  `int32` | oomScoreAdj is The oom-score-adj value for kubelet process. Values must be within the range [-1000, 1000]. Default: -999 |
| `clusterDomain`  `string` | clusterDomain is the DNS domain for this cluster. If set, kubelet will configure all containers to search this domain in addition to the host's search domains. Default: "" |
| `clusterDNS`  `[]string` | clusterDNS is a list of IP addresses for the cluster DNS server. If set, kubelet will configure all containers to use this for DNS resolution instead of the host's DNS servers. Default: nil |
| `streamingConnectionIdleTimeout`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | streamingConnectionIdleTimeout is the maximum time a streaming connection can be idle before the connection is automatically closed. Deprecated: no longer has any effect. Default: "4h" |
| `nodeStatusUpdateFrequency`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | nodeStatusUpdateFrequency is the frequency that kubelet computes node status. If node lease feature is not enabled, it is also the frequency that kubelet posts node status to master. Note: When node lease feature is not enabled, be cautious when changing the constant, it must work with nodeMonitorGracePeriod in nodecontroller. Default: "10s" |
| `nodeStatusReportFrequency`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | nodeStatusReportFrequency is the frequency that kubelet posts node status to master if node status does not change. Kubelet will ignore this frequency and post node status immediately if any change is detected. It is only used when node lease feature is enabled. nodeStatusReportFrequency's default value is 5m. But if nodeStatusUpdateFrequency is set explicitly, nodeStatusReportFrequency's default value will be set to nodeStatusUpdateFrequency for backward compatibility. Default: "5m" |
| `nodeLeaseDurationSeconds`  `int32` | nodeLeaseDurationSeconds is the duration the Kubelet will set on its corresponding Lease. NodeLease provides an indicator of node health by having the Kubelet create and periodically renew a lease, named after the node, in the kube-node-lease namespace. If the lease expires, the node can be considered unhealthy. The lease is currently renewed every 10s, per KEP-0009. In the future, the lease renewal interval may be set based on the lease duration. The field value must be greater than 0. Default: 40 |
| `imageMinimumGCAge`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | imageMinimumGCAge is the minimum age for an unused image before it is garbage collected. Default: "2m" |
| `imageMaximumGCAge`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | imageMaximumGCAge is the maximum age an image can be unused before it is garbage collected. The default of this field is "0s", which disables this field--meaning images won't be garbage collected based on being unused for too long. Default: "0s" (disabled) |
| `imageGCHighThresholdPercent`  `int32` | imageGCHighThresholdPercent is the percent of disk usage after which image garbage collection is always run. The percent is calculated by dividing this field value by 100, so this field must be between 0 and 100, inclusive. When specified, the value must be greater than imageGCLowThresholdPercent. Default: 85 |
| `imageGCLowThresholdPercent`  `int32` | imageGCLowThresholdPercent is the percent of disk usage before which image garbage collection is never run. Lowest disk usage to garbage collect to. The percent is calculated by dividing this field value by 100, so the field value must be between 0 and 100, inclusive. When specified, the value must be less than imageGCHighThresholdPercent. Default: 80 |
| `volumeStatsAggPeriod`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | volumeStatsAggPeriod is the frequency for calculating and caching volume disk usage for all pods. Default: "1m" |
| `kubeletCgroups`  `string` | kubeletCgroups is the absolute name of cgroups to isolate the kubelet in Default: "" |
| `systemCgroups`  `string` | systemCgroups is absolute name of cgroups in which to place all non-kernel processes that are not already in a container. Empty for no container. Rolling back the flag requires a reboot. The cgroupRoot must be specified if this field is not empty. Default: "" |
| `cgroupRoot`  `string` | cgroupRoot is the root cgroup to use for pods. This is handled by the container runtime on a best effort basis. |
| `cgroupsPerQOS`  `bool` | cgroupsPerQOS enable QoS based CGroup hierarchy: top level CGroups for QoS classes and all Burstable and BestEffort Pods are brought up under their specific top level QoS CGroup. Default: true |
| `cgroupDriver`  `string` | cgroupDriver is the driver kubelet uses to manipulate CGroups on the host (cgroupfs or systemd). Default: "cgroupfs" |
| `cpuManagerPolicy`  `string` | cpuManagerPolicy is the name of the policy to use. Default: "None" |
| `singleProcessOOMKill`  `bool` | singleProcessOOMKill, if true, will prevent the `memory.oom.group` flag from being set for container cgroups in cgroups v2. This causes processes in the container to be OOM killed individually instead of as a group. It means that if true, the behavior aligns with the behavior of cgroups v1. The default value is determined automatically when you don't specify. On non-linux such as windows, only null / absent is allowed. On cgroup v1 linux, only null / absent and true are allowed. On cgroup v2 linux, null / absent, true and false are allowed. The default value is false. |
| `cpuManagerPolicyOptions`  `map[string]string` | cpuManagerPolicyOptions is a set of key=value which allows to set extra options to fine tune the behaviour of the cpu manager policies. Default: nil |
| `cpuManagerReconcilePeriod`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | cpuManagerReconcilePeriod is the reconciliation period for the CPU Manager. Default: "10s" |
| `memoryManagerPolicy`  `string` | memoryManagerPolicy is the name of the policy to use by memory manager. Requires the MemoryManager feature gate to be enabled. Default: "none" |
| `topologyManagerPolicy`  `string` | topologyManagerPolicy is the name of the topology manager policy to use. Valid values include:   * `restricted`: kubelet only allows pods with optimal NUMA node alignment for   requested resources; * `best-effort`: kubelet will favor pods with NUMA alignment of CPU and device   resources; * `none`: kubelet has no knowledge of NUMA alignment of a pod's CPU and device resources. * `single-numa-node`: kubelet only allows pods with a single NUMA alignment   of CPU and device resources.   Default: "none" |
| `topologyManagerScope`  `string` | topologyManagerScope represents the scope of topology hint generation that topology manager requests and hint providers generate. Valid values include:   * `container`: topology policy is applied on a per-container basis. * `pod`: topology policy is applied on a per-pod basis.   Default: "container" |
| `topologyManagerPolicyOptions`  `map[string]string` | TopologyManagerPolicyOptions is a set of key=value which allows to set extra options to fine tune the behaviour of the topology manager policies. Requires both the "TopologyManager" and "TopologyManagerPolicyOptions" feature gates to be enabled. Default: nil |
| `qosReserved`  `map[string]string` | qosReserved is a set of resource name to percentage pairs that specify the minimum percentage of a resource reserved for exclusive use by the guaranteed QoS tier. Currently supported resources: "memory" Requires the QOSReserved feature gate to be enabled. Default: nil |
| `runtimeRequestTimeout`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | runtimeRequestTimeout is the timeout for all runtime requests except long running requests - pull, logs, exec and attach. Default: "2m" |
| `hairpinMode`  `string` | hairpinMode specifies how the Kubelet should configure the container bridge for hairpin packets. Setting this flag allows endpoints in a Service to loadbalance back to themselves if they should try to access their own Service. Values:   * "promiscuous-bridge": make the container bridge promiscuous. * "hairpin-veth": set the hairpin flag on container veth interfaces. * "none": do nothing.   Generally, one must set `--hairpin-mode=hairpin-veth to` achieve hairpin NAT, because promiscuous-bridge assumes the existence of a container bridge named cbr0. Default: "promiscuous-bridge" |
| `maxPods`  `int32` | maxPods is the maximum number of Pods that can run on this Kubelet. The value must be a non-negative integer. Default: 110 |
| `podCIDR`  `string` | podCIDR is the CIDR to use for pod IP addresses, only used in standalone mode. In cluster mode, this is obtained from the control plane. Default: "" |
| `podPidsLimit`  `int64` | podPidsLimit is the maximum number of PIDs in any pod. Default: -1 |
| `resolvConf`  `string` | resolvConf is the resolver configuration file used as the basis for the container DNS resolution configuration. If set to the empty string, will override the default and effectively disable DNS lookups. Default: "/etc/resolv.conf" |
| `runOnce`  `bool` | runOnce causes the Kubelet to check the API server once for pods, run those in addition to the pods specified by static pod files, and exit. Default: false |
| `cpuCFSQuota`  `bool` | cpuCFSQuota enables CPU CFS quota enforcement for containers that specify CPU limits. Default: true |
| `cpuCFSQuotaPeriod`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | cpuCFSQuotaPeriod is the CPU CFS quota period value, `cpu.cfs_period_us`. The value must be between 1 ms and 1 second, inclusive. Requires the CustomCPUCFSQuotaPeriod feature gate to be enabled. Default: "100ms" |
| `nodeStatusMaxImages`  `int32` | nodeStatusMaxImages caps the number of images reported in Node.status.images. The value must be greater than -2. Note: If -1 is specified, no cap will be applied. If 0 is specified, no image is returned. Default: 50 |
| `maxOpenFiles`  `int64` | maxOpenFiles is Number of files that can be opened by Kubelet process. The value must be a non-negative number. Default: 1000000 |
| `contentType`  `string` | contentType is contentType of requests sent to apiserver. Default: "application/vnd.kubernetes.protobuf" |
| `kubeAPIQPS`  `int32` | kubeAPIQPS is the QPS to use while talking with kubernetes apiserver. Default: 50 |
| `kubeAPIBurst`  `int32` | kubeAPIBurst is the burst to allow while talking with kubernetes API server. This field cannot be a negative number. Default: 100 |
| `serializeImagePulls`  `bool` | serializeImagePulls when enabled, tells the Kubelet to pull images one at a time. We recommend *not* changing the default value on nodes that run docker daemon with version < 1.9 or an Aufs storage backend. Issue #10959 has more details. Default: true |
| `maxParallelImagePulls`  `int32` | MaxParallelImagePulls sets the maximum number of image pulls in parallel. This field cannot be set if SerializeImagePulls is true. Setting it to nil means no limit. Default: nil |
| `evictionHard`  `map[string]string` | evictionHard is a map of signal names to quantities that defines hard eviction thresholds. For example: `{"memory.available": "300Mi"}`. To explicitly disable, pass a 0% or 100% threshold on an arbitrary resource. Default: memory.available: "100Mi" nodefs.available: "10%" nodefs.inodesFree: "5%" imagefs.available: "15%" |
| `evictionSoft`  `map[string]string` | evictionSoft is a map of signal names to quantities that defines soft eviction thresholds. For example: `{"memory.available": "300Mi"}`. Default: nil |
| `evictionSoftGracePeriod`  `map[string]string` | evictionSoftGracePeriod is a map of signal names to quantities that defines grace periods for each soft eviction signal. For example: `{"memory.available": "30s"}`. Default: nil |
| `evictionPressureTransitionPeriod`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | evictionPressureTransitionPeriod is the duration for which the kubelet has to wait before transitioning out of an eviction pressure condition. A duration of 0s will be converted to the default value of 5m Default: "5m" |
| `evictionMaxPodGracePeriod`  `int32` | evictionMaxPodGracePeriod is the maximum allowed grace period (in seconds) to use when terminating pods in response to a soft eviction threshold being met. This value effectively caps the Pod's terminationGracePeriodSeconds value during soft evictions. The pod's effective grace period is calculated as: min(evictionMaxPodGracePeriod, pod.terminationGracePeriodSeconds). Note: A negative value will cause pods to be terminated immediately, as if the value was 0. Default: 0 |
| `evictionMinimumReclaim`  `map[string]string` | evictionMinimumReclaim is a map of signal names to quantities that defines minimum reclaims, which describe the minimum amount of a given resource the kubelet will reclaim when performing a pod eviction while that resource is under pressure. For example: `{"imagefs.available": "2Gi"}`. Default: nil |
| `mergeDefaultEvictionSettings`  `bool` | mergeDefaultEvictionSettings indicates that defaults for the evictionHard, evictionSoft, evictionSoftGracePeriod, and evictionMinimumReclaim fields should be merged into values specified for those fields in this configuration. Signals specified in this configuration take precedence. Signals not specified in this configuration inherit their defaults. If false, and if any signal is specified in this configuration then other signals that are not specified in this configuration will be set to 0. It applies to merging the fields for which the default exists, and currently only evictionHard has default values. Default: false |
| `podsPerCore`  `int32` | podsPerCore is the maximum number of pods per core. Cannot exceed maxPods. The value must be a non-negative integer. If 0, there is no limit on the number of Pods. Default: 0 |
| `enableControllerAttachDetach`  `bool` | enableControllerAttachDetach enables the Attach/Detach controller to manage attachment/detachment of volumes scheduled to this node, and disables kubelet from executing any attach/detach operations. Note: attaching/detaching CSI volumes is not supported by the kubelet, so this option needs to be true for that use case. Default: true |
| `protectKernelDefaults`  `bool` | protectKernelDefaults, if true, causes the Kubelet to error if kernel flags are not as it expects. Otherwise the Kubelet will attempt to modify kernel flags to match its expectation. Default: false |
| `makeIPTablesUtilChains`  `bool` | makeIPTablesUtilChains, if true, causes the Kubelet to create the KUBE-IPTABLES-HINT chain in iptables as a hint to other components about the configuration of iptables on the system. Default: true |
| `iptablesMasqueradeBit`  `int32` | iptablesMasqueradeBit formerly controlled the creation of the KUBE-MARK-MASQ chain. Deprecated: no longer has any effect. Default: 14 |
| `iptablesDropBit`  `int32` | iptablesDropBit formerly controlled the creation of the KUBE-MARK-DROP chain. Deprecated: no longer has any effect. Default: 15 |
| `featureGates`  `map[string]bool` | featureGates is a map of feature names to bools that enable or disable experimental features. This field modifies piecemeal the built-in default values from "k8s.io/kubernetes/pkg/features/kube_features.go". Default: nil |
| `failSwapOn`  `bool` | failSwapOn tells the Kubelet to fail to start if swap is enabled on the node. Default: true |
| `memorySwap`  [`MemorySwapConfiguration`](#kubelet-config-k8s-io-v1beta1-MemorySwapConfiguration) | memorySwap configures swap memory available to container workloads. |
| `containerLogMaxSize`  `string` | containerLogMaxSize is a quantity defining the maximum size of the container log file before it is rotated. For example: "5Mi" or "256Ki". Default: "10Mi" |
| `containerLogMaxFiles`  `int32` | containerLogMaxFiles specifies the maximum number of container log files that can be present for a container. Default: 5 |
| `containerLogMaxWorkers`  `int32` | ContainerLogMaxWorkers specifies the maximum number of concurrent workers to spawn for performing the log rotate operations. Set this count to 1 for disabling the concurrent log rotation workflows Default: 1 |
| `containerLogMonitorInterval`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | ContainerLogMonitorInterval specifies the duration at which the container logs are monitored for performing the log rotate operation. This defaults to 10 * time.Seconds. But can be customized to a smaller value based on the log generation rate and the size required to be rotated against Default: 10s |
| `configMapAndSecretChangeDetectionStrategy`  [`ResourceChangeDetectionStrategy`](#kubelet-config-k8s-io-v1beta1-ResourceChangeDetectionStrategy) | configMapAndSecretChangeDetectionStrategy is a mode in which ConfigMap and Secret managers are running. Valid values include:   * `Get`: kubelet fetches necessary objects directly from the API server; * `Cache`: kubelet uses TTL cache for object fetched from the API server; * `Watch`: kubelet uses watches to observe changes to objects that are in its interest.   Default: "Watch" |
| `systemReserved`  `map[string]string` | systemReserved is a set of ResourceName=ResourceQuantity (e.g. cpu=200m,memory=150G) pairs that describe resources reserved for non-kubernetes components. Currently only cpu and memory are supported. See https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources for more detail. Default: nil |
| `kubeReserved`  `map[string]string` | kubeReserved is a set of ResourceName=ResourceQuantity (e.g. cpu=200m,memory=150G) pairs that describe resources reserved for kubernetes system components. Currently cpu, memory and local storage for root file system are supported. See https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources for more details. Default: nil |
| `reservedSystemCPUs` **[Required]**  `string` | The reservedSystemCPUs option specifies the CPU list reserved for the host level system threads and kubernetes related threads. This provide a "static" CPU list rather than the "dynamic" list by systemReserved and kubeReserved. This option does not support systemReservedCgroup or kubeReservedCgroup. |
| `showHiddenMetricsForVersion`  `string` | showHiddenMetricsForVersion is the previous version for which you want to show hidden metrics. Only the previous minor version is meaningful, other values will not be allowed. The format is `<major>.<minor>`, e.g.: `1.16`. The purpose of this format is make sure you have the opportunity to notice if the next release hides additional metrics, rather than being surprised when they are permanently removed in the release after that. Default: "" |
| `systemReservedCgroup`  `string` | systemReservedCgroup helps the kubelet identify absolute name of top level CGroup used to enforce `systemReserved` compute resource reservation for OS system daemons. Refer to [Node Allocatable](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable) doc for more information. Default: "" |
| `kubeReservedCgroup`  `string` | kubeReservedCgroup helps the kubelet identify absolute name of top level CGroup used to enforce `KubeReserved` compute resource reservation for Kubernetes node system daemons. Refer to [Node Allocatable](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable) doc for more information. Default: "" |
| `enforceNodeAllocatable`  `[]string` | This flag specifies the various Node Allocatable enforcements that Kubelet needs to perform. This flag accepts a list of options. Acceptable options are `none`, `pods`, `system-reserved` and `kube-reserved`. If `none` is specified, no other options may be specified. When `system-reserved` is in the list, systemReservedCgroup must be specified. When `kube-reserved` is in the list, kubeReservedCgroup must be specified. This field is supported only when `cgroupsPerQOS` is set to true. Refer to [Node Allocatable](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable) for more information. Default: ["pods"] |
| `allowedUnsafeSysctls`  `[]string` | A comma separated whitelist of unsafe sysctls or sysctl patterns (ending in `*`). Unsafe sysctl groups are `kernel.shm*`, `kernel.msg*`, `kernel.sem`, `fs.mqueue.*`, and `net.*`. For example: "`kernel.msg*,net.ipv4.route.min_pmtu`" Default: [] |
| `volumePluginDir`  `string` | volumePluginDir is the full path of the directory in which to search for additional third party volume plugins. Default: "/usr/libexec/kubernetes/kubelet-plugins/volume/exec/" |
| `providerID`  `string` | providerID, if set, sets the unique ID of the instance that an external provider (i.e. cloudprovider) can use to identify a specific node. Default: "" |
| `kernelMemcgNotification`  `bool` | kernelMemcgNotification, if set, instructs the kubelet to integrate with the kernel memcg notification for determining if memory eviction thresholds are exceeded rather than polling. Default: false |
| `logging` **[Required]**  [`LoggingConfiguration`](#LoggingConfiguration) | logging specifies the options of logging. Refer to [Logs Options](https://github.com/kubernetes/component-base/blob/master/logs/options.go) for more information. Default: Format: text |
| `enableSystemLogHandler`  `bool` | enableSystemLogHandler enables system logs via web interface host:port/logs/ Default: true |
| `enableSystemLogQuery`  `bool` | enableSystemLogQuery enables the node log query feature on the /logs endpoint. EnableSystemLogHandler has to be enabled in addition for this feature to work. Enabling this feature has security implications. The recommendation is to enable it on a need basis for debugging purposes and disabling otherwise. Default: false |
| `shutdownGracePeriod`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | shutdownGracePeriod specifies the total duration that the node should delay the shutdown and total grace period for pod termination during a node shutdown. Default: "0s" |
| `shutdownGracePeriodCriticalPods`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | shutdownGracePeriodCriticalPods specifies the duration used to terminate critical pods during a node shutdown. This should be less than shutdownGracePeriod. For example, if shutdownGracePeriod=30s, and shutdownGracePeriodCriticalPods=10s, during a node shutdown the first 20 seconds would be reserved for gracefully terminating normal pods, and the last 10 seconds would be reserved for terminating critical pods. Default: "0s" |
| `shutdownGracePeriodByPodPriority`  [`[]ShutdownGracePeriodByPodPriority`](#kubelet-config-k8s-io-v1beta1-ShutdownGracePeriodByPodPriority) | shutdownGracePeriodByPodPriority specifies the shutdown grace period for Pods based on their associated priority class value. When a shutdown request is received, the Kubelet will initiate shutdown on all pods running on the node with a grace period that depends on the priority of the pod, and then wait for all pods to exit. Each entry in the array represents the graceful shutdown time a pod with a priority class value that lies in the range of that value and the next higher entry in the list when the node is shutting down. For example, to allow critical pods 10s to shutdown, priority>=10000 pods 20s to shutdown, and all remaining pods 30s to shutdown.  shutdownGracePeriodByPodPriority:   * priority: 2000000000   shutdownGracePeriodSeconds: 10 * priority: 10000   shutdownGracePeriodSeconds: 20 * priority: 0   shutdownGracePeriodSeconds: 30   The time the Kubelet will wait before exiting will at most be the maximum of all shutdownGracePeriodSeconds for each priority class range represented on the node. When all pods have exited or reached their grace periods, the Kubelet will release the shutdown inhibit lock. Requires the GracefulNodeShutdown feature gate to be enabled. This configuration must be empty if either ShutdownGracePeriod or ShutdownGracePeriodCriticalPods is set. Default: nil |
| `crashLoopBackOff`  [`CrashLoopBackOffConfig`](#kubelet-config-k8s-io-v1beta1-CrashLoopBackOffConfig) | CrashLoopBackOff contains config to modify node-level parameters for container restart behavior |
| `reservedMemory`  [`[]MemoryReservation`](#kubelet-config-k8s-io-v1beta1-MemoryReservation) | reservedMemory specifies a comma-separated list of memory reservations for NUMA nodes. The parameter makes sense only in the context of the memory manager feature. The memory manager will not allocate reserved memory for container workloads. For example, if you have a NUMA0 with 10Gi of memory and the reservedMemory was specified to reserve 1Gi of memory at NUMA0, the memory manager will assume that only 9Gi is available for allocation. You can specify a different amount of NUMA node and memory types. You can omit this parameter at all, but you should be aware that the amount of reserved memory from all NUMA nodes should be equal to the amount of memory specified by the [node allocatable](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable). If at least one node allocatable parameter has a non-zero value, you will need to specify at least one NUMA node. Also, avoid specifying:   1. Duplicates, the same NUMA node, and memory type, but with a different value. 2. zero limits for any memory type. 3. NUMAs nodes IDs that do not exist under the machine. 4. memory types except for memory and hugepages-   Default: nil |
| `enableProfilingHandler`  `bool` | enableProfilingHandler enables profiling via web interface host:port/debug/pprof/ Default: true |
| `enableDebugFlagsHandler`  `bool` | enableDebugFlagsHandler enables flags endpoint via web interface host:port/debug/flags/v Default: true |
| `seccompDefault`  `bool` | SeccompDefault enables the use of `RuntimeDefault` as the default seccomp profile for all workloads. Default: false |
| `memoryThrottlingFactor`  `float64` | MemoryThrottlingFactor specifies the factor multiplied by the memory limit or node allocatable memory when setting the cgroupv2 memory.high value to enforce MemoryQoS. Decreasing this factor will set lower high limit for container cgroups and put heavier reclaim pressure while increasing will put less reclaim pressure. See https://kep.k8s.io/2570 for more details. Default: 0.9 |
| `registerWithTaints`  [`[]core/v1.Taint`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#taint-v1-core) | registerWithTaints are an array of taints to add to a node object when the kubelet registers itself. This only takes effect when registerNode is true and upon the initial registration of the node. Default: nil |
| `registerNode`  `bool` | registerNode enables automatic registration with the apiserver. Default: true |
| `tracing`  [`TracingConfiguration`](#TracingConfiguration) | Tracing specifies the versioned configuration for OpenTelemetry tracing clients. See https://kep.k8s.io/2832 for more details. Default: nil |
| `localStorageCapacityIsolation`  `bool` | LocalStorageCapacityIsolation enables local ephemeral storage isolation feature. The default setting is true. This feature allows users to set request/limit for container's ephemeral storage and manage it in a similar way as cpu and memory. It also allows setting sizeLimit for emptyDir volume, which will trigger pod eviction if disk usage from the volume exceeds the limit. This feature depends on the capability of detecting correct root file system disk usage. For certain systems, such as kind rootless, if this capability cannot be supported, the feature LocalStorageCapacityIsolation should be disabled. Once disabled, user should not set request/limit for container's ephemeral storage, or sizeLimit for emptyDir. Default: true |
| `containerRuntimeEndpoint` **[Required]**  `string` | ContainerRuntimeEndpoint is the endpoint of container runtime. Unix Domain Sockets are supported on Linux, while npipe and tcp endpoints are supported on Windows. Examples:'unix:///path/to/runtime.sock', 'npipe:////./pipe/runtime' |
| `imageServiceEndpoint`  `string` | ImageServiceEndpoint is the endpoint of container image service. Unix Domain Socket are supported on Linux, while npipe and tcp endpoints are supported on Windows. Examples:'unix:///path/to/runtime.sock', 'npipe:////./pipe/runtime'. If not specified, the value in containerRuntimeEndpoint is used. |
| `failCgroupV1`  `bool` | FailCgroupV1 prevents the kubelet from starting on hosts that use cgroup v1. By default, this is set to 'false', meaning the kubelet is allowed to start on cgroup v1 hosts unless this option is explicitly enabled. Default: false |
| `userNamespaces`  [`UserNamespaces`](#kubelet-config-k8s-io-v1beta1-UserNamespaces) | UserNamespaces contains User Namespace configurations. |

## `SerializedNodeConfigSource`

SerializedNodeConfigSource allows us to serialize v1.NodeConfigSource.
This type is used internally by the Kubelet for tracking checkpointed dynamic configs.
It exists in the kubeletconfig API group because it is classified as a versioned input to the Kubelet.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubelet.config.k8s.io/v1beta1` |
| `kind` string | `SerializedNodeConfigSource` |
| `source`  [`core/v1.NodeConfigSource`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#nodeconfigsource-v1-core) | source is the source that we are serializing. |

## `CrashLoopBackOffConfig`

**Appears in:**

* [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)

| Field | Description |
| --- | --- |
| `maxContainerRestartPeriod`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | maxContainerRestartPeriod is the maximum duration the backoff delay can accrue to for container restarts, minimum 1 second, maximum 300 seconds. If not set, defaults to the internal crashloopbackoff maximum (300s). |

## `CredentialProvider`

**Appears in:**

* [CredentialProviderConfig](#kubelet-config-k8s-io-v1beta1-CredentialProviderConfig)

CredentialProvider represents an exec plugin to be invoked by the kubelet. The plugin is only
invoked when an image being pulled matches the images handled by the plugin (see matchImages).

| Field | Description |
| --- | --- |
| `name` **[Required]**  `string` | name is the required name of the credential provider. It must match the name of the provider executable as seen by the kubelet. The executable must be in the kubelet's bin directory (set by the --image-credential-provider-bin-dir flag). Required to be unique across all providers. |
| `matchImages` **[Required]**  `[]string` | matchImages is a required list of strings used to match against images in order to determine if this provider should be invoked. If one of the strings matches the requested image from the kubelet, the plugin will be invoked and given a chance to provide credentials. Images are expected to contain the registry domain and URL path.  Each entry in matchImages is a pattern which can optionally contain a port and a path. Globs can be used in the domain, but not in the port or the path. Globs are supported as subdomains like '*.k8s.io' or 'k8s.*.io', and top-level-domains such as 'k8s.*'. Matching partial subdomains like 'app*.k8s.io' is also supported. Each glob can only match a single subdomain segment, so *.io does not match *.k8s.io.  A match exists between an image and a matchImage when all of the below are true:   * Both contain the same number of domain parts and each part matches. * The URL path of an imageMatch must be a prefix of the target image URL path. * If the imageMatch contains a port, then the port must match in the image as well.   Example values of matchImages:   * 123456789.dkr.ecr.us-east-1.amazonaws.com * *.azurecr.io * gcr.io * *.*.registry.io * registry.io:8080/path |
| `defaultCacheDuration` **[Required]**  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | defaultCacheDuration is the default duration the plugin will cache credentials in-memory if a cache duration is not provided in the plugin response. This field is required. |
| `apiVersion` **[Required]**  `string` | Required input version of the exec CredentialProviderRequest. The returned CredentialProviderResponse MUST use the same encoding version as the input. Current supported values are:   * credentialprovider.kubelet.k8s.io/v1beta1 |
| `args`  `[]string` | Arguments to pass to the command when executing it. |
| `env`  [`[]ExecEnvVar`](#kubelet-config-k8s-io-v1beta1-ExecEnvVar) | Env defines additional environment variables to expose to the process. These are unioned with the host's environment, as well as variables client-go uses to pass argument to the plugin. |

## `ExecEnvVar`

**Appears in:**

* [CredentialProvider](#kubelet-config-k8s-io-v1beta1-CredentialProvider)

ExecEnvVar is used for setting environment variables when executing an exec-based
credential plugin.

| Field | Description |
| --- | --- |
| `name` **[Required]**  `string` | No description provided. |
| `value` **[Required]**  `string` | No description provided. |

## `ImagePullCredentialsVerificationPolicy`

(Alias of `string`)

**Appears in:**

* [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)

ImagePullCredentialsVerificationPolicy is an enum for the policy that is enforced
when pod is requesting an image that appears on the system

## `KubeletAnonymousAuthentication`

**Appears in:**

* [KubeletAuthentication](#kubelet-config-k8s-io-v1beta1-KubeletAuthentication)

| Field | Description |
| --- | --- |
| `enabled`  `bool` | enabled allows anonymous requests to the kubelet server. Requests that are not rejected by another authentication method are treated as anonymous requests. Anonymous requests have a username of `system:anonymous`, and a group name of `system:unauthenticated`. |

## `KubeletAuthentication`

**Appears in:**

* [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)

| Field | Description |
| --- | --- |
| `x509`  [`KubeletX509Authentication`](#kubelet-config-k8s-io-v1beta1-KubeletX509Authentication) | x509 contains settings related to x509 client certificate authentication. |
| `webhook`  [`KubeletWebhookAuthentication`](#kubelet-config-k8s-io-v1beta1-KubeletWebhookAuthentication) | webhook contains settings related to webhook bearer token authentication. |
| `anonymous`  [`KubeletAnonymousAuthentication`](#kubelet-config-k8s-io-v1beta1-KubeletAnonymousAuthentication) | anonymous contains settings related to anonymous authentication. |

## `KubeletAuthorization`

**Appears in:**

* [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)

| Field | Description |
| --- | --- |
| `mode`  [`KubeletAuthorizationMode`](#kubelet-config-k8s-io-v1beta1-KubeletAuthorizationMode) | mode is the authorization mode to apply to requests to the kubelet server. Valid values are `AlwaysAllow` and `Webhook`. Webhook mode uses the SubjectAccessReview API to determine authorization. |
| `webhook`  [`KubeletWebhookAuthorization`](#kubelet-config-k8s-io-v1beta1-KubeletWebhookAuthorization) | webhook contains settings related to Webhook authorization. |

## `KubeletAuthorizationMode`

(Alias of `string`)

**Appears in:**

* [KubeletAuthorization](#kubelet-config-k8s-io-v1beta1-KubeletAuthorization)

## `KubeletWebhookAuthentication`

**Appears in:**

* [KubeletAuthentication](#kubelet-config-k8s-io-v1beta1-KubeletAuthentication)

| Field | Description |
| --- | --- |
| `enabled`  `bool` | enabled allows bearer token authentication backed by the tokenreviews.authentication.k8s.io API. |
| `cacheTTL`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | cacheTTL enables caching of authentication results |

## `KubeletWebhookAuthorization`

**Appears in:**

* [KubeletAuthorization](#kubelet-config-k8s-io-v1beta1-KubeletAuthorization)

| Field | Description |
| --- | --- |
| `cacheAuthorizedTTL`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | cacheAuthorizedTTL is the duration to cache 'authorized' responses from the webhook authorizer. |
| `cacheUnauthorizedTTL`  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | cacheUnauthorizedTTL is the duration to cache 'unauthorized' responses from the webhook authorizer. |

## `KubeletX509Authentication`

**Appears in:**

* [KubeletAuthentication](#kubelet-config-k8s-io-v1beta1-KubeletAuthentication)

| Field | Description |
| --- | --- |
| `clientCAFile`  `string` | clientCAFile is the path to a PEM-encoded certificate bundle. If set, any request presenting a client certificate signed by one of the authorities in the bundle is authenticated with a username corresponding to the CommonName, and groups corresponding to the Organization in the client certificate. |

## `MemoryReservation`

**Appears in:**

* [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)

MemoryReservation specifies the memory reservation of different types for each NUMA node

| Field | Description |
| --- | --- |
| `numaNode` **[Required]**  `int32` | No description provided. |
| `limits` **[Required]**  [`core/v1.ResourceList`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#resourcelist-v1-core) | No description provided. |

## `MemorySwapConfiguration`

**Appears in:**

* [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)

| Field | Description |
| --- | --- |
| `swapBehavior`  `string` | swapBehavior configures swap memory available to container workloads. May be one of "", "NoSwap": workloads can not use swap, default option. "LimitedSwap": workload swap usage is limited. The swap limit is proportionate to the container's memory request. |

## `ResourceChangeDetectionStrategy`

(Alias of `string`)

**Appears in:**

* [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)

ResourceChangeDetectionStrategy denotes a mode in which internal
managers (secret, configmap) are discovering object changes.

## `ShutdownGracePeriodByPodPriority`

**Appears in:**

* [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)

ShutdownGracePeriodByPodPriority specifies the shutdown grace period for Pods based on their associated priority class value

| Field | Description |
| --- | --- |
| `priority` **[Required]**  `int32` | priority is the priority value associated with the shutdown grace period |
| `shutdownGracePeriodSeconds` **[Required]**  `int64` | shutdownGracePeriodSeconds is the shutdown grace period in seconds |

## `UserNamespaces`

**Appears in:**

* [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)

UserNamespaces contains User Namespace configurations.

| Field | Description |
| --- | --- |
| `idsPerPod`  `int64` | IDsPerPod is the mapping length of UIDs and GIDs. The length must be a multiple of 65536, and must be less than 1<<32. On non-linux such as windows, only null / absent is allowed.  Changing the value may require recreating all containers on the node.  Default: 65536 |

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
