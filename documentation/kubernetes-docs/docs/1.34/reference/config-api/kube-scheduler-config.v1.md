# kube-scheduler Configuration (v1)

## Resource Types

* [DefaultPreemptionArgs](#kubescheduler-config-k8s-io-v1-DefaultPreemptionArgs)
* [DynamicResourcesArgs](#kubescheduler-config-k8s-io-v1-DynamicResourcesArgs)
* [InterPodAffinityArgs](#kubescheduler-config-k8s-io-v1-InterPodAffinityArgs)
* [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)
* [NodeAffinityArgs](#kubescheduler-config-k8s-io-v1-NodeAffinityArgs)
* [NodeResourcesBalancedAllocationArgs](#kubescheduler-config-k8s-io-v1-NodeResourcesBalancedAllocationArgs)
* [NodeResourcesFitArgs](#kubescheduler-config-k8s-io-v1-NodeResourcesFitArgs)
* [PodTopologySpreadArgs](#kubescheduler-config-k8s-io-v1-PodTopologySpreadArgs)
* [VolumeBindingArgs](#kubescheduler-config-k8s-io-v1-VolumeBindingArgs)

## `ClientConnectionConfiguration`

**Appears in:**

* [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)

ClientConnectionConfiguration contains details for constructing a client.

| Field | Description |
| --- | --- |
| `kubeconfig` **[Required]**  `string` | kubeconfig is the path to a KubeConfig file. |
| `acceptContentTypes` **[Required]**  `string` | acceptContentTypes defines the Accept header sent by clients when connecting to a server, overriding the default value of 'application/json'. This field will control all connections to the server used by a particular client. |
| `contentType` **[Required]**  `string` | contentType is the content type used when sending data to the server from this client. |
| `qps` **[Required]**  `float32` | qps controls the number of queries per second allowed for this connection. |
| `burst` **[Required]**  `int32` | burst allows extra queries to accumulate when a client is exceeding its rate. |

## `DebuggingConfiguration`

**Appears in:**

* [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)

DebuggingConfiguration holds configuration for Debugging related features.

| Field | Description |
| --- | --- |
| `enableProfiling` **[Required]**  `bool` | enableProfiling enables profiling via web interface host:port/debug/pprof/ |
| `enableContentionProfiling` **[Required]**  `bool` | enableContentionProfiling enables block profiling, if enableProfiling is true. |

## `LeaderElectionConfiguration`

**Appears in:**

* [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)

LeaderElectionConfiguration defines the configuration of leader election
clients for components that can run with leader election enabled.

| Field | Description |
| --- | --- |
| `leaderElect` **[Required]**  `bool` | leaderElect enables a leader election client to gain leadership before executing the main loop. Enable this when running replicated components for high availability. |
| `leaseDuration` **[Required]**  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | leaseDuration is the duration that non-leader candidates will wait after observing a leadership renewal until attempting to acquire leadership of a led but unrenewed leader slot. This is effectively the maximum duration that a leader can be stopped before it is replaced by another candidate. This is only applicable if leader election is enabled. |
| `renewDeadline` **[Required]**  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | renewDeadline is the interval between attempts by the acting master to renew a leadership slot before it stops leading. This must be less than or equal to the lease duration. This is only applicable if leader election is enabled. |
| `retryPeriod` **[Required]**  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | retryPeriod is the duration the clients should wait between attempting acquisition and renewal of a leadership. This is only applicable if leader election is enabled. |
| `resourceLock` **[Required]**  `string` | resourceLock indicates the resource object type that will be used to lock during leader election cycles. |
| `resourceName` **[Required]**  `string` | resourceName indicates the name of resource object that will be used to lock during leader election cycles. |
| `resourceNamespace` **[Required]**  `string` | resourceName indicates the namespace of resource object that will be used to lock during leader election cycles. |

## `DefaultPreemptionArgs`

DefaultPreemptionArgs holds arguments used to configure the
DefaultPreemption plugin.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubescheduler.config.k8s.io/v1` |
| `kind` string | `DefaultPreemptionArgs` |
| `minCandidateNodesPercentage` **[Required]**  `int32` | MinCandidateNodesPercentage is the minimum number of candidates to shortlist when dry running preemption as a percentage of number of nodes. Must be in the range [0, 100]. Defaults to 10% of the cluster size if unspecified. |
| `minCandidateNodesAbsolute` **[Required]**  `int32` | MinCandidateNodesAbsolute is the absolute minimum number of candidates to shortlist. The likely number of candidates enumerated for dry running preemption is given by the formula: numCandidates = max(numNodes * minCandidateNodesPercentage, minCandidateNodesAbsolute) We say "likely" because there are other factors such as PDB violations that play a role in the number of candidates shortlisted. Must be at least 0 nodes. Defaults to 100 nodes if unspecified. |

## `DynamicResourcesArgs`

DynamicResourcesArgs holds arguments used to configure the DynamicResources plugin.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubescheduler.config.k8s.io/v1` |
| `kind` string | `DynamicResourcesArgs` |
| `filterTimeout` **[Required]**  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | FilterTimeout limits the amount of time that the filter operation may take per node to search for devices that can be allocated to scheduler a pod to that node.  In typical scenarios, this operation should complete in 10 to 200 milliseconds, but could also be longer depending on the number of requests per ResourceClaim, number of ResourceClaims, number of published devices in ResourceSlices, and the complexity of the requests. Other checks besides CEL evaluation also take time (usage checks, match attributes, etc.).  Therefore the scheduler plugin applies this timeout. If the timeout is reached, the Pod is considered unschedulable for the node. If filtering succeeds for some other node(s), those are picked instead. If filtering fails for all of them, the Pod is placed in the unschedulable queue. It will get checked again if changes in e.g. ResourceSlices or ResourceClaims indicate that another scheduling attempt might succeed. If this fails repeatedly, exponential backoff slows down future attempts.  The default is 10 seconds. This is sufficient to prevent worst-case scenarios while not impacting normal usage of DRA. However, slow filtering can slow down Pod scheduling also for Pods not using DRA. Administators can reduce the timeout after checking the `scheduler_framework_extension_point_duration_seconds` metrics.  Setting it to zero completely disables the timeout. |

## `InterPodAffinityArgs`

InterPodAffinityArgs holds arguments used to configure the InterPodAffinity plugin.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubescheduler.config.k8s.io/v1` |
| `kind` string | `InterPodAffinityArgs` |
| `hardPodAffinityWeight` **[Required]**  `int32` | HardPodAffinityWeight is the scoring weight for existing pods with a matching hard affinity to the incoming pod. |
| `ignorePreferredTermsOfExistingPods` **[Required]**  `bool` | IgnorePreferredTermsOfExistingPods configures the scheduler to ignore existing pods' preferred affinity rules when scoring candidate nodes, unless the incoming pod has inter-pod affinities. |

## `KubeSchedulerConfiguration`

KubeSchedulerConfiguration configures a scheduler

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubescheduler.config.k8s.io/v1` |
| `kind` string | `KubeSchedulerConfiguration` |
| `parallelism` **[Required]**  `int32` | Parallelism defines the amount of parallelism in algorithms for scheduling a Pods. Must be greater than 0. Defaults to 16 |
| `leaderElection` **[Required]**  [`LeaderElectionConfiguration`](#LeaderElectionConfiguration) | LeaderElection defines the configuration of leader election client. |
| `clientConnection` **[Required]**  [`ClientConnectionConfiguration`](#ClientConnectionConfiguration) | ClientConnection specifies the kubeconfig file and client connection settings for the proxy server to use when communicating with the apiserver. |
| `DebuggingConfiguration` **[Required]**  [`DebuggingConfiguration`](#DebuggingConfiguration) | (Members of `DebuggingConfiguration` are embedded into this type.) DebuggingConfiguration holds configuration for Debugging related features TODO: We might wanna make this a substruct like Debugging componentbaseconfigv1alpha1.DebuggingConfiguration |
| `percentageOfNodesToScore` **[Required]**  `int32` | PercentageOfNodesToScore is the percentage of all nodes that once found feasible for running a pod, the scheduler stops its search for more feasible nodes in the cluster. This helps improve scheduler's performance. Scheduler always tries to find at least "minFeasibleNodesToFind" feasible nodes no matter what the value of this flag is. Example: if the cluster size is 500 nodes and the value of this flag is 30, then scheduler stops finding further feasible nodes once it finds 150 feasible ones. When the value is 0, default percentage (5%--50% based on the size of the cluster) of the nodes will be scored. It is overridden by profile level PercentageOfNodesToScore. |
| `podInitialBackoffSeconds` **[Required]**  `int64` | PodInitialBackoffSeconds is the initial backoff for unschedulable pods. If specified, it must be greater than 0. If this value is null, the default value (1s) will be used. |
| `podMaxBackoffSeconds` **[Required]**  `int64` | PodMaxBackoffSeconds is the max backoff for unschedulable pods. If specified, it must be greater than podInitialBackoffSeconds. If this value is null, the default value (10s) will be used. |
| `profiles` **[Required]**  [`[]KubeSchedulerProfile`](#kubescheduler-config-k8s-io-v1-KubeSchedulerProfile) | Profiles are scheduling profiles that kube-scheduler supports. Pods can choose to be scheduled under a particular profile by setting its associated scheduler name. Pods that don't specify any scheduler name are scheduled with the "default-scheduler" profile, if present here. |
| `extenders` **[Required]**  [`[]Extender`](#kubescheduler-config-k8s-io-v1-Extender) | Extenders are the list of scheduler extenders, each holding the values of how to communicate with the extender. These extenders are shared by all scheduler profiles. |
| `delayCacheUntilActive` **[Required]**  `bool` | DelayCacheUntilActive specifies when to start caching. If this is true and leader election is enabled, the scheduler will wait to fill informer caches until it is the leader. Doing so will have slower failover with the benefit of lower memory overhead while waiting to become leader. Defaults to false. |

## `NodeAffinityArgs`

NodeAffinityArgs holds arguments to configure the NodeAffinity plugin.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubescheduler.config.k8s.io/v1` |
| `kind` string | `NodeAffinityArgs` |
| `addedAffinity`  [`core/v1.NodeAffinity`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#nodeaffinity-v1-core) | AddedAffinity is applied to all Pods additionally to the NodeAffinity specified in the PodSpec. That is, Nodes need to satisfy AddedAffinity AND .spec.NodeAffinity. AddedAffinity is empty by default (all Nodes match). When AddedAffinity is used, some Pods with affinity requirements that match a specific Node (such as Daemonset Pods) might remain unschedulable. |

## `NodeResourcesBalancedAllocationArgs`

NodeResourcesBalancedAllocationArgs holds arguments used to configure NodeResourcesBalancedAllocation plugin.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubescheduler.config.k8s.io/v1` |
| `kind` string | `NodeResourcesBalancedAllocationArgs` |
| `resources` **[Required]**  [`[]ResourceSpec`](#kubescheduler-config-k8s-io-v1-ResourceSpec) | Resources to be managed, the default is "cpu" and "memory" if not specified. |

## `NodeResourcesFitArgs`

NodeResourcesFitArgs holds arguments used to configure the NodeResourcesFit plugin.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubescheduler.config.k8s.io/v1` |
| `kind` string | `NodeResourcesFitArgs` |
| `ignoredResources` **[Required]**  `[]string` | IgnoredResources is the list of resources that NodeResources fit filter should ignore. This doesn't apply to scoring. |
| `ignoredResourceGroups` **[Required]**  `[]string` | IgnoredResourceGroups defines the list of resource groups that NodeResources fit filter should ignore. e.g. if group is ["example.com"], it will ignore all resource names that begin with "example.com", such as "example.com/aaa" and "example.com/bbb". A resource group name can't contain '/'. This doesn't apply to scoring. |
| `scoringStrategy` **[Required]**  [`ScoringStrategy`](#kubescheduler-config-k8s-io-v1-ScoringStrategy) | ScoringStrategy selects the node resource scoring strategy. The default strategy is LeastAllocated with an equal "cpu" and "memory" weight. |

## `PodTopologySpreadArgs`

PodTopologySpreadArgs holds arguments used to configure the PodTopologySpread plugin.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubescheduler.config.k8s.io/v1` |
| `kind` string | `PodTopologySpreadArgs` |
| `defaultConstraints`  [`[]core/v1.TopologySpreadConstraint`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.34/#topologyspreadconstraint-v1-core) | DefaultConstraints defines topology spread constraints to be applied to Pods that don't define any in `pod.spec.topologySpreadConstraints`. `.defaultConstraints[*].labelSelectors` must be empty, as they are deduced from the Pod's membership to Services, ReplicationControllers, ReplicaSets or StatefulSets. When not empty, .defaultingType must be "List". |
| `defaultingType`  [`PodTopologySpreadConstraintsDefaulting`](#kubescheduler-config-k8s-io-v1-PodTopologySpreadConstraintsDefaulting) | DefaultingType determines how .defaultConstraints are deduced. Can be one of "System" or "List".   * "System": Use kubernetes defined constraints that spread Pods among   Nodes and Zones. * "List": Use constraints defined in .defaultConstraints.   Defaults to "System". |

## `VolumeBindingArgs`

VolumeBindingArgs holds arguments used to configure the VolumeBinding plugin.

| Field | Description |
| --- | --- |
| `apiVersion` string | `kubescheduler.config.k8s.io/v1` |
| `kind` string | `VolumeBindingArgs` |
| `bindTimeoutSeconds` **[Required]**  `int64` | BindTimeoutSeconds is the timeout in seconds in volume binding operation. Value must be non-negative integer. The value zero indicates no waiting. If this value is nil, the default value (600) will be used. |
| `shape`  [`[]UtilizationShapePoint`](#kubescheduler-config-k8s-io-v1-UtilizationShapePoint) | Shape specifies the points defining the score function shape, which is used to score nodes based on the utilization of provisioned PVs. The utilization is calculated by dividing the total requested storage of the pod by the total capacity of feasible PVs on each node. Each point contains utilization (ranges from 0 to 100) and its associated score (ranges from 0 to 10). You can turn the priority by specifying different scores for different utilization numbers. The default shape points are:   1. 10 for 0 utilization 2. 0 for 100 utilization    All points must be sorted in increasing order by utilization. |

## `Extender`

**Appears in:**

* [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)

Extender holds the parameters used to communicate with the extender. If a verb is unspecified/empty,
it is assumed that the extender chose not to provide that extension.

| Field | Description |
| --- | --- |
| `urlPrefix` **[Required]**  `string` | URLPrefix at which the extender is available |
| `filterVerb` **[Required]**  `string` | Verb for the filter call, empty if not supported. This verb is appended to the URLPrefix when issuing the filter call to extender. |
| `preemptVerb` **[Required]**  `string` | Verb for the preempt call, empty if not supported. This verb is appended to the URLPrefix when issuing the preempt call to extender. |
| `prioritizeVerb` **[Required]**  `string` | Verb for the prioritize call, empty if not supported. This verb is appended to the URLPrefix when issuing the prioritize call to extender. |
| `weight` **[Required]**  `int64` | The numeric multiplier for the node scores that the prioritize call generates. The weight should be a positive integer |
| `bindVerb` **[Required]**  `string` | Verb for the bind call, empty if not supported. This verb is appended to the URLPrefix when issuing the bind call to extender. If this method is implemented by the extender, it is the extender's responsibility to bind the pod to apiserver. Only one extender can implement this function. |
| `enableHTTPS` **[Required]**  `bool` | EnableHTTPS specifies whether https should be used to communicate with the extender |
| `tlsConfig` **[Required]**  [`ExtenderTLSConfig`](#kubescheduler-config-k8s-io-v1-ExtenderTLSConfig) | TLSConfig specifies the transport layer security config |
| `httpTimeout` **[Required]**  [`meta/v1.Duration`](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration) | HTTPTimeout specifies the timeout duration for a call to the extender. Filter timeout fails the scheduling of the pod. Prioritize timeout is ignored, k8s/other extenders priorities are used to select the node. |
| `nodeCacheCapable` **[Required]**  `bool` | NodeCacheCapable specifies that the extender is capable of caching node information, so the scheduler should only send minimal information about the eligible nodes assuming that the extender already cached full details of all nodes in the cluster |
| `managedResources`  [`[]ExtenderManagedResource`](#kubescheduler-config-k8s-io-v1-ExtenderManagedResource) | ManagedResources is a list of extended resources that are managed by this extender.   * A pod will be sent to the extender on the Filter, Prioritize and Bind   (if the extender is the binder) phases iff the pod requests at least   one of the extended resources in this list. If empty or unspecified,   all pods will be sent to this extender. * If IgnoredByScheduler is set to true for a resource, kube-scheduler   will skip checking the resource in predicates. |
| `ignorable` **[Required]**  `bool` | Ignorable specifies if the extender is ignorable, i.e. scheduling should not fail when the extender returns an error or is not reachable. |

## `ExtenderManagedResource`

**Appears in:**

* [Extender](#kubescheduler-config-k8s-io-v1-Extender)

ExtenderManagedResource describes the arguments of extended resources
managed by an extender.

| Field | Description |
| --- | --- |
| `name` **[Required]**  `string` | Name is the extended resource name. |
| `ignoredByScheduler` **[Required]**  `bool` | IgnoredByScheduler indicates whether kube-scheduler should ignore this resource when applying predicates. |

## `ExtenderTLSConfig`

**Appears in:**

* [Extender](#kubescheduler-config-k8s-io-v1-Extender)

ExtenderTLSConfig contains settings to enable TLS with extender

| Field | Description |
| --- | --- |
| `insecure` **[Required]**  `bool` | Server should be accessed without verifying the TLS certificate. For testing only. |
| `serverName` **[Required]**  `string` | ServerName is passed to the server for SNI and is used in the client to check server certificates against. If ServerName is empty, the hostname used to contact the server is used. |
| `certFile` **[Required]**  `string` | Server requires TLS client certificate authentication |
| `keyFile` **[Required]**  `string` | Server requires TLS client certificate authentication |
| `caFile` **[Required]**  `string` | Trusted root certificates for server |
| `certData` **[Required]**  `[]byte` | CertData holds PEM-encoded bytes (typically read from a client certificate file). CertData takes precedence over CertFile |
| `keyData` **[Required]**  `[]byte` | KeyData holds PEM-encoded bytes (typically read from a client certificate key file). KeyData takes precedence over KeyFile |
| `caData` **[Required]**  `[]byte` | CAData holds PEM-encoded bytes (typically read from a root certificates bundle). CAData takes precedence over CAFile |

## `KubeSchedulerProfile`

**Appears in:**

* [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)

KubeSchedulerProfile is a scheduling profile.

| Field | Description |
| --- | --- |
| `schedulerName` **[Required]**  `string` | SchedulerName is the name of the scheduler associated to this profile. If SchedulerName matches with the pod's "spec.schedulerName", then the pod is scheduled with this profile. |
| `percentageOfNodesToScore` **[Required]**  `int32` | PercentageOfNodesToScore is the percentage of all nodes that once found feasible for running a pod, the scheduler stops its search for more feasible nodes in the cluster. This helps improve scheduler's performance. Scheduler always tries to find at least "minFeasibleNodesToFind" feasible nodes no matter what the value of this flag is. Example: if the cluster size is 500 nodes and the value of this flag is 30, then scheduler stops finding further feasible nodes once it finds 150 feasible ones. When the value is 0, default percentage (5%--50% based on the size of the cluster) of the nodes will be scored. It will override global PercentageOfNodesToScore. If it is empty, global PercentageOfNodesToScore will be used. |
| `plugins` **[Required]**  [`Plugins`](#kubescheduler-config-k8s-io-v1-Plugins) | Plugins specify the set of plugins that should be enabled or disabled. Enabled plugins are the ones that should be enabled in addition to the default plugins. Disabled plugins are any of the default plugins that should be disabled. When no enabled or disabled plugin is specified for an extension point, default plugins for that extension point will be used if there is any. If a QueueSort plugin is specified, the same QueueSort Plugin and PluginConfig must be specified for all profiles. |
| `pluginConfig` **[Required]**  [`[]PluginConfig`](#kubescheduler-config-k8s-io-v1-PluginConfig) | PluginConfig is an optional set of custom plugin arguments for each plugin. Omitting config args for a plugin is equivalent to using the default config for that plugin. |

## `Plugin`

**Appears in:**

* [PluginSet](#kubescheduler-config-k8s-io-v1-PluginSet)

Plugin specifies a plugin name and its weight when applicable. Weight is used only for Score plugins.

| Field | Description |
| --- | --- |
| `name` **[Required]**  `string` | Name defines the name of plugin |
| `weight` **[Required]**  `int32` | Weight defines the weight of plugin, only used for Score plugins. |

## `PluginConfig`

**Appears in:**

* [KubeSchedulerProfile](#kubescheduler-config-k8s-io-v1-KubeSchedulerProfile)

PluginConfig specifies arguments that should be passed to a plugin at the time of initialization.
A plugin that is invoked at multiple extension points is initialized once. Args can have arbitrary structure.
It is up to the plugin to process these Args.

| Field | Description |
| --- | --- |
| `name` **[Required]**  `string` | Name defines the name of plugin being configured |
| `args` **[Required]**  [`k8s.io/apimachinery/pkg/runtime.RawExtension`](https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime/#RawExtension) | Args defines the arguments passed to the plugins at the time of initialization. Args can have arbitrary structure. |

## `PluginSet`

**Appears in:**

* [Plugins](#kubescheduler-config-k8s-io-v1-Plugins)

PluginSet specifies enabled and disabled plugins for an extension point.
If an array is empty, missing, or nil, default plugins at that extension point will be used.

| Field | Description |
| --- | --- |
| `enabled` **[Required]**  [`[]Plugin`](#kubescheduler-config-k8s-io-v1-Plugin) | Enabled specifies plugins that should be enabled in addition to default plugins. If the default plugin is also configured in the scheduler config file, the weight of plugin will be overridden accordingly. These are called after default plugins and in the same order specified here. |
| `disabled` **[Required]**  [`[]Plugin`](#kubescheduler-config-k8s-io-v1-Plugin) | Disabled specifies default plugins that should be disabled. When all default plugins need to be disabled, an array containing only one "*" should be provided. |

## `Plugins`

**Appears in:**

* [KubeSchedulerProfile](#kubescheduler-config-k8s-io-v1-KubeSchedulerProfile)

Plugins include multiple extension points. When specified, the list of plugins for
a particular extension point are the only ones enabled. If an extension point is
omitted from the config, then the default set of plugins is used for that extension point.
Enabled plugins are called in the order specified here, after default plugins. If they need to
be invoked before default plugins, default plugins must be disabled and re-enabled here in desired order.

| Field | Description |
| --- | --- |
| `preEnqueue` **[Required]**  [`PluginSet`](#kubescheduler-config-k8s-io-v1-PluginSet) | PreEnqueue is a list of plugins that should be invoked before adding pods to the scheduling queue. |
| `queueSort` **[Required]**  [`PluginSet`](#kubescheduler-config-k8s-io-v1-PluginSet) | QueueSort is a list of plugins that should be invoked when sorting pods in the scheduling queue. |
| `preFilter` **[Required]**  [`PluginSet`](#kubescheduler-config-k8s-io-v1-PluginSet) | PreFilter is a list of plugins that should be invoked at "PreFilter" extension point of the scheduling framework. |
| `filter` **[Required]**  [`PluginSet`](#kubescheduler-config-k8s-io-v1-PluginSet) | Filter is a list of plugins that should be invoked when filtering out nodes that cannot run the Pod. |
| `postFilter` **[Required]**  [`PluginSet`](#kubescheduler-config-k8s-io-v1-PluginSet) | PostFilter is a list of plugins that are invoked after filtering phase, but only when no feasible nodes were found for the pod. |
| `preScore` **[Required]**  [`PluginSet`](#kubescheduler-config-k8s-io-v1-PluginSet) | PreScore is a list of plugins that are invoked before scoring. |
| `score` **[Required]**  [`PluginSet`](#kubescheduler-config-k8s-io-v1-PluginSet) | Score is a list of plugins that should be invoked when ranking nodes that have passed the filtering phase. |
| `reserve` **[Required]**  [`PluginSet`](#kubescheduler-config-k8s-io-v1-PluginSet) | Reserve is a list of plugins invoked when reserving/unreserving resources after a node is assigned to run the pod. |
| `permit` **[Required]**  [`PluginSet`](#kubescheduler-config-k8s-io-v1-PluginSet) | Permit is a list of plugins that control binding of a Pod. These plugins can prevent or delay binding of a Pod. |
| `preBind` **[Required]**  [`PluginSet`](#kubescheduler-config-k8s-io-v1-PluginSet) | PreBind is a list of plugins that should be invoked before a pod is bound. |
| `bind` **[Required]**  [`PluginSet`](#kubescheduler-config-k8s-io-v1-PluginSet) | Bind is a list of plugins that should be invoked at "Bind" extension point of the scheduling framework. The scheduler call these plugins in order. Scheduler skips the rest of these plugins as soon as one returns success. |
| `postBind` **[Required]**  [`PluginSet`](#kubescheduler-config-k8s-io-v1-PluginSet) | PostBind is a list of plugins that should be invoked after a pod is successfully bound. |
| `multiPoint` **[Required]**  [`PluginSet`](#kubescheduler-config-k8s-io-v1-PluginSet) | MultiPoint is a simplified config section to enable plugins for all valid extension points. Plugins enabled through MultiPoint will automatically register for every individual extension point the plugin has implemented. Disabling a plugin through MultiPoint disables that behavior. The same is true for disabling "*" through MultiPoint (no default plugins will be automatically registered). Plugins can still be disabled through their individual extension points.  In terms of precedence, plugin config follows this basic hierarchy   1. Specific extension points 2. Explicitly configured MultiPoint plugins 3. The set of default plugins, as MultiPoint plugins    This implies that a higher precedence plugin will run first and overwrite any settings within MultiPoint.    Explicitly user-configured plugins also take a higher precedence over default plugins.    Within this hierarchy, an Enabled setting takes precedence over Disabled. For example, if a plugin is    set in both `multiPoint.Enabled` and `multiPoint.Disabled`, the plugin will be enabled. Similarly,    including `multiPoint.Disabled = '*'` and `multiPoint.Enabled = pluginA` will still register that specific    plugin through MultiPoint. This follows the same behavior as all other extension point configurations. |

## `PodTopologySpreadConstraintsDefaulting`

(Alias of `string`)

**Appears in:**

* [PodTopologySpreadArgs](#kubescheduler-config-k8s-io-v1-PodTopologySpreadArgs)

PodTopologySpreadConstraintsDefaulting defines how to set default constraints
for the PodTopologySpread plugin.

## `RequestedToCapacityRatioParam`

**Appears in:**

* [ScoringStrategy](#kubescheduler-config-k8s-io-v1-ScoringStrategy)

RequestedToCapacityRatioParam define RequestedToCapacityRatio parameters

| Field | Description |
| --- | --- |
| `shape` **[Required]**  [`[]UtilizationShapePoint`](#kubescheduler-config-k8s-io-v1-UtilizationShapePoint) | Shape is a list of points defining the scoring function shape. |

## `ResourceSpec`

**Appears in:**

* [NodeResourcesBalancedAllocationArgs](#kubescheduler-config-k8s-io-v1-NodeResourcesBalancedAllocationArgs)
* [ScoringStrategy](#kubescheduler-config-k8s-io-v1-ScoringStrategy)

ResourceSpec represents a single resource.

| Field | Description |
| --- | --- |
| `name` **[Required]**  `string` | Name of the resource. |
| `weight` **[Required]**  `int64` | Weight of the resource. |

## `ScoringStrategy`

**Appears in:**

* [NodeResourcesFitArgs](#kubescheduler-config-k8s-io-v1-NodeResourcesFitArgs)

ScoringStrategy define ScoringStrategyType for node resource plugin

| Field | Description |
| --- | --- |
| `type` **[Required]**  [`ScoringStrategyType`](#kubescheduler-config-k8s-io-v1-ScoringStrategyType) | Type selects which strategy to run. |
| `resources` **[Required]**  [`[]ResourceSpec`](#kubescheduler-config-k8s-io-v1-ResourceSpec) | Resources to consider when scoring. The default resource set includes "cpu" and "memory" with an equal weight. Allowed weights go from 1 to 100. Weight defaults to 1 if not specified or explicitly set to 0. |
| `requestedToCapacityRatio` **[Required]**  [`RequestedToCapacityRatioParam`](#kubescheduler-config-k8s-io-v1-RequestedToCapacityRatioParam) | Arguments specific to RequestedToCapacityRatio strategy. |

## `ScoringStrategyType`

(Alias of `string`)

**Appears in:**

* [ScoringStrategy](#kubescheduler-config-k8s-io-v1-ScoringStrategy)

ScoringStrategyType the type of scoring strategy used in NodeResourcesFit plugin.

## `UtilizationShapePoint`

**Appears in:**

* [VolumeBindingArgs](#kubescheduler-config-k8s-io-v1-VolumeBindingArgs)
* [RequestedToCapacityRatioParam](#kubescheduler-config-k8s-io-v1-RequestedToCapacityRatioParam)

UtilizationShapePoint represents single point of priority function shape.

| Field | Description |
| --- | --- |
| `utilization` **[Required]**  `int32` | Utilization (x axis). Valid values are 0 to 100. Fully utilized node maps to 100. |
| `score` **[Required]**  `int32` | Score assigned to given utilization (y axis). Valid values are 0 to 10. |

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
