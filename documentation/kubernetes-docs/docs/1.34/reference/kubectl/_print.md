This is the multi-page printable view of this section.
[Click here to print](#).

[Return to the regular view of this page](/docs/reference/kubectl/).

# Command line tool (kubectl)

* 1: [Introduction to kubectl](#pg-b2faf0db34da634aff4d681164922d6a)
* 2: [kubectl Quick Reference](#pg-0437e83631175effa44e8c516c5adbda)
* 3: [kubectl reference](#pg-e1b5cca32613cabad88dbdcefd80e2c9)

+ 3.1: [kubectl](#pg-402909613e0ae370b616c0caac29621f)
+ 3.2: [kubectl annotate](#pg-36ff86c01e1c63f208a2d2d1db6b6a4f)

+ 3.3: [kubectl api-resources](#pg-8ecdd5ca9c4f7724f144aa46a98e0ec9)

+ 3.4: [kubectl api-versions](#pg-5f872ac31510d52a53ab72cea7fa29cf)

+ 3.5: [kubectl apply](#pg-3eea9e13de34e9bb4ad11c9c30bd249c)

- 3.5.1: [kubectl apply edit-last-applied](#pg-641acfde6e8164afe190eb62ae5c205d)
- 3.5.2: [kubectl apply set-last-applied](#pg-e1a3553640a80681da6b4bbe66760ab3)
- 3.5.3: [kubectl apply view-last-applied](#pg-c4d0a4727091a0e42ffa9cf8a0ad2329)

+ 3.6: [kubectl attach](#pg-0e29e49eae92a6e42de742686ece8e59)

+ 3.7: [kubectl auth](#pg-5c6cdd7674d19af1f0ed5161db1abb07)

- 3.7.1: [kubectl auth can-i](#pg-9fd383dbd061a4bd429962c0884141dc)
- 3.7.2: [kubectl auth reconcile](#pg-b63cd4df7b8fc6f18e4e048aca007433)
- 3.7.3: [kubectl auth whoami](#pg-55334cff1ad1de8913da0e79bd424c99)

+ 3.8: [kubectl autoscale](#pg-b4d81752c4bebc716cf5a6621248ddbf)

+ 3.9: [kubectl certificate](#pg-b0655c69bc929ffef16ad59fb060e9b0)

- 3.9.1: [kubectl certificate approve](#pg-7470128dc60bc72d430ee382f36ef6d3)
- 3.9.2: [kubectl certificate deny](#pg-c27805149b129dc7843215976f95fc68)

+ 3.10: [kubectl cluster-info](#pg-35437a08dd53ca5d9e79117020a6856a)

- 3.10.1: [kubectl cluster-info dump](#pg-2b6cbcd733c21832d8ebf57781964754)

+ 3.11: [kubectl completion](#pg-1c563fdb012166230fcf8d4b4ae572cd)

+ 3.12: [kubectl config](#pg-e93d0796f4e6f7df1ab6fe9f32d32af3)

- 3.12.1: [kubectl config current-context](#pg-5014b54facef233a63885234ce91c3aa)
- 3.12.2: [kubectl config delete-cluster](#pg-aecc079c7de2d3be561601daf1d6684c)
- 3.12.3: [kubectl config delete-context](#pg-b5f24b4e3009ebba0a0f4ad35af0d4ab)
- 3.12.4: [kubectl config delete-user](#pg-d77b4cbd068f250f86cff5c2e75dabda)
- 3.12.5: [kubectl config get-clusters](#pg-1176518e0a720b52609f27e88abef8eb)
- 3.12.6: [kubectl config get-contexts](#pg-f96682991dc356384f3888c21b013cd6)
- 3.12.7: [kubectl config get-users](#pg-3a4916efcdffdb896b4619a1a5cbd87b)
- 3.12.8: [kubectl config rename-context](#pg-4f49ec6f9e1def05f72cfd83d8e26f34)
- 3.12.9: [kubectl config set](#pg-fddfa538835c3f9a09666f6713f07278)
- 3.12.10: [kubectl config set-cluster](#pg-c6f09b5a087eb07fce8acb3d3db38e22)
- 3.12.11: [kubectl config set-context](#pg-2500189be627eaffa4b161af5dd9a178)
- 3.12.12: [kubectl config set-credentials](#pg-b3b6ccdb55698e26fcd43bf215002c58)
- 3.12.13: [kubectl config unset](#pg-f82900d692231ec20a5fc6465c06e298)
- 3.12.14: [kubectl config use-context](#pg-f6ec7b5627422d529c65ee106681fea2)
- 3.12.15: [kubectl config view](#pg-3bfacbe2914206676749a842aa0d00f2)

+ 3.13: [kubectl cordon](#pg-114515632079608ac9c1631e3bd46aaa)

+ 3.14: [kubectl cp](#pg-281884941d738cd8fa58091afa664824)

+ 3.15: [kubectl create](#pg-953771ff28f42694f3cccf8b294bbee0)

- 3.15.1: [kubectl create clusterrole](#pg-bc9f354d308d4b7b92bd1e2c199dd4d1)
- 3.15.2: [kubectl create clusterrolebinding](#pg-b580bc796e16cf5c330344854759b767)
- 3.15.3: [kubectl create configmap](#pg-d7a078683e8028884681580d3da9c355)
- 3.15.4: [kubectl create cronjob](#pg-8623e760bcd816213276f920925c7c9f)
- 3.15.5: [kubectl create deployment](#pg-85938a5e506af5d05edc154a7ba45ee7)
- 3.15.6: [kubectl create ingress](#pg-454f37b7a4a10acbcb73ee1faefe7ba6)
- 3.15.7: [kubectl create job](#pg-962e637e4ac9ca350d8717c056c77268)
- 3.15.8: [kubectl create namespace](#pg-8b99d360d189a763d8828d8dad70db8a)
- 3.15.9: [kubectl create poddisruptionbudget](#pg-1e27a1c88d08b9addd57196b0559c087)
- 3.15.10: [kubectl create priorityclass](#pg-ba25e70aa569d978cd2bec9f32ce0dba)
- 3.15.11: [kubectl create quota](#pg-e28159f2e6cb8aa3120d1e88a2e3e404)
- 3.15.12: [kubectl create role](#pg-01fc591ca5a786b8d3ed390ef6b72ad5)
- 3.15.13: [kubectl create rolebinding](#pg-df4b1aa40a6f6a6f8645261cacb35972)
- 3.15.14: [kubectl create secret](#pg-de61418fe2b7a032a7336d6c27fb27be)
- 3.15.15: [kubectl create secret docker-registry](#pg-76970ddfe96bc2cf910756946387250e)
- 3.15.16: [kubectl create secret generic](#pg-68b32a259fda3582817081388caa0330)
- 3.15.17: [kubectl create secret tls](#pg-4033b20aaa417f9e2081d96419a6ee45)
- 3.15.18: [kubectl create service](#pg-e0cf2bf7674d167398f315e6a67e1379)
- 3.15.19: [kubectl create service clusterip](#pg-8b94cb3a05077a406591bf6b1886edc2)
- 3.15.20: [kubectl create service externalname](#pg-d5f597b1de53f09bf2bea1855a981247)
- 3.15.21: [kubectl create service loadbalancer](#pg-a1edd453dd57d18385eb35c8e33431a4)
- 3.15.22: [kubectl create service nodeport](#pg-a0df1e98366de5c5261e1414770c68f9)
- 3.15.23: [kubectl create serviceaccount](#pg-811bd5ff9c057c6c3e7755acabbc824a)
- 3.15.24: [kubectl create token](#pg-ee534c7541a0919bdd14e6411d8067b8)

+ 3.16: [kubectl debug](#pg-b034a7678879340ad25bafdd9551d22a)

+ 3.17: [kubectl delete](#pg-ab346c76d590e8ad07e20fccaa45c980)

+ 3.18: [kubectl describe](#pg-b2c625f46a85287d2c0551154b769024)

+ 3.19: [kubectl diff](#pg-7eaa64344ffe7b4fb8fb0752f1b97d9f)

+ 3.20: [kubectl drain](#pg-aa964bf4ff4621badcc87e1cd0e32681)

+ 3.21: [kubectl edit](#pg-8cf21077f8795e0b16fde83d11567578)

+ 3.22: [kubectl events](#pg-a88e5c3601e2bf7b0293034f5e81e821)

+ 3.23: [kubectl exec](#pg-882aa52820297ac9293dd44da8672f3e)

+ 3.24: [kubectl explain](#pg-41e90bac90aec872d864dcc94d5b90f8)

+ 3.25: [kubectl expose](#pg-5775bf192e6208ef0a2b85dfc8a7d38a)

+ 3.26: [kubectl get](#pg-34144509b7c5215e39120b601448cc40)

+ 3.27: [kubectl kustomize](#pg-92353483fed3c33db48f9bc79e3d023c)

+ 3.28: [kubectl label](#pg-f5c069064e2fcd06616d62599428f308)

+ 3.29: [kubectl logs](#pg-ac35b1a6ed39fbe561feef25dc882275)

+ 3.30: [kubectl options](#pg-b2b46c4956d34ec270e4c76b5d05c493)

+ 3.31: [kubectl patch](#pg-30e2662613e2fd6dd67f08bc734a6ad5)

+ 3.32: [kubectl plugin](#pg-997eb0d8f0bb60112e8d0b0b0d46ef14)

- 3.32.1: [kubectl plugin list](#pg-4025c6d57b4a953ffeb1dbaf8a201201)

+ 3.33: [kubectl port-forward](#pg-6d0ce5cb4810fe1ec32c075d9b8e31ba)

+ 3.34: [kubectl proxy](#pg-9133e2fab485b02227c141ef2c8b86f1)

+ 3.35: [kubectl replace](#pg-836e50cbd85466dc75e3134956ff3aea)

+ 3.36: [kubectl rollout](#pg-e8086f0539497d9723d72fa8b5f54952)

- 3.36.1: [kubectl rollout history](#pg-feee355d0921a2dae193326b4569c1c4)
- 3.36.2: [kubectl rollout pause](#pg-a45554a76bb1970815575b0d0eb8eb78)
- 3.36.3: [kubectl rollout restart](#pg-dff2e5df7176c0f397625767a6624bf4)
- 3.36.4: [kubectl rollout resume](#pg-a2718a937a9d531c87d0c31ba738c112)
- 3.36.5: [kubectl rollout status](#pg-5162a0abebfda06de0129978dff33fa3)
- 3.36.6: [kubectl rollout undo](#pg-decea050af73d7440fc036efb9ff569f)

+ 3.37: [kubectl run](#pg-7e05911b36fcf1c8870f9debcb704446)

+ 3.38: [kubectl scale](#pg-e363c273030dec7915a0dcd2f0e5a4f0)

+ 3.39: [kubectl set](#pg-366c76c7b3d5aaa4bfbb45015d99bf15)

- 3.39.1: [kubectl set env](#pg-8efccafb687ee15419a3c10a01f52499)
- 3.39.2: [kubectl set image](#pg-5f280fa194c35dcc401bf7a8b16df02d)
- 3.39.3: [kubectl set resources](#pg-bd8b811c676cdb149ca3cad198624d9f)
- 3.39.4: [kubectl set selector](#pg-affb9944665fc880f3ebb6edf7673214)
- 3.39.5: [kubectl set serviceaccount](#pg-3118ff763cfaafe03d807a502e48e967)
- 3.39.6: [kubectl set subject](#pg-e9c5704d912a656bcc627016d1045699)

+ 3.40: [kubectl taint](#pg-584242a5667621cd3d0ce458d12e10bc)

+ 3.41: [kubectl top](#pg-de8407a2eccd93c98c5b0eca954fb881)

- 3.41.1: [kubectl top node](#pg-24aaff2b409245e171479e8dd8790013)
- 3.41.2: [kubectl top pod](#pg-765f5bf8510a311aaa87e1027328a2ef)

+ 3.42: [kubectl uncordon](#pg-8c1849e7de1aec914e31a94c032a0f6a)

+ 3.43: [kubectl version](#pg-ad13feebe933b7228fb9472fc822a3c0)

+ 3.44: [kubectl wait](#pg-1bf01c4ed4581610178c3f20a5cd043f)

* 4: [kubectl Commands](#pg-d7ffbf04ffbefb241fd0722423b80f5a)
* 5: [kubectl](#pg-4d3e62632c189fcc3c1357cd8fb8799c)
* 6: [JSONPath Support](#pg-a938176c695852fe70362c29cf615f1c)
* 7: [kubectl for Docker Users](#pg-a7abc09192597e614b58f8b552b682f5)
* 8: [kubectl Usage Conventions](#pg-8de6aceb8bf692c06cced446bac5bc92)
* 9: [Kubectl user preferences (kuberc)](#pg-0fb24477397db8dd277afb2477c199dd)

Kubernetes provides a command line tool for communicating with a Kubernetes cluster's
[control plane](/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers."),
using the Kubernetes API.

This tool is named `kubectl`.

For configuration, `kubectl` looks for a file named `config` in the `$HOME/.kube` directory.
You can specify other [kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
files by setting the `KUBECONFIG` environment variable or by setting the
[`--kubeconfig`](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) flag.

This overview covers `kubectl` syntax, describes the command operations, and provides common examples.
For details about each command, including all the supported flags and subcommands, see the
[kubectl](/docs/reference/kubectl/generated/kubectl/) reference documentation.

For installation instructions, see [Installing kubectl](/docs/tasks/tools/#kubectl);
for a quick guide, see the [cheat sheet](/docs/reference/kubectl/quick-reference/).
If you're used to using the `docker` command-line tool,
[`kubectl` for Docker Users](/docs/reference/kubectl/docker-cli-to-kubectl/) explains some equivalent commands for Kubernetes.

## Syntax

Use the following syntax to run `kubectl` commands from your terminal window:

```
kubectl [command] [TYPE] [NAME] [flags]
```

where `command`, `TYPE`, `NAME`, and `flags` are:

* `command`: Specifies the operation that you want to perform on one or more resources,
  for example `create`, `get`, `describe`, `delete`.
* `TYPE`: Specifies the [resource type](#resource-types). Resource types are case-insensitive and
  you can specify the singular, plural, or abbreviated forms.
  For example, the following commands produce the same output:

  ```
  kubectl get pod pod1
  kubectl get pods pod1
  kubectl get po pod1
  ```
* `NAME`: Specifies the name of the resource. Names are case-sensitive. If the name is omitted,
  details for all resources are displayed, for example `kubectl get pods`.

  When performing an operation on multiple resources, you can specify each resource by
  type and name or specify one or more files:

  + To specify resources by type and name:

    - To group resources if they are all the same type: `TYPE1 name1 name2 name<#>`.
      Example: `kubectl get pod example-pod1 example-pod2`
    - To specify multiple resource types individually: `TYPE1/name1 TYPE1/name2 TYPE2/name3 TYPE<#>/name<#>`.
      Example: `kubectl get pod/example-pod1 replicationcontroller/example-rc1`
  + To specify resources with one or more files: `-f file1 -f file2 -f file<#>`

    - Use YAML rather than JSON
      since YAML tends to be more user-friendly, especially for configuration files.
      Example: `kubectl get -f ./pod.yaml`
* `flags`: Specifies optional flags. For example, you can use the `-s` or `--server` flags
  to specify the address and port of the Kubernetes API server.

> **Caution:**
> Flags that you specify from the command line override default values and any corresponding environment variables.

If you need help, run `kubectl help` from the terminal window.

## In-cluster authentication and namespace overrides

By default `kubectl` will first determine if it is running within a pod, and thus in a cluster.
It starts by checking for the `KUBERNETES_SERVICE_HOST` and `KUBERNETES_SERVICE_PORT` environment
variables and the existence of a service account token file at `/var/run/secrets/kubernetes.io/serviceaccount/token`.
If all three are found in-cluster authentication is assumed.

To maintain backwards compatibility, if the `POD_NAMESPACE` environment variable is set
during in-cluster authentication it will override the default namespace from the
service account token. Any manifests or tools relying on namespace defaulting will be affected by this.

**`POD_NAMESPACE` environment variable**

If the `POD_NAMESPACE` environment variable is set, cli operations on namespaced resources
will default to the variable value. For example, if the variable is set to `seattle`,
`kubectl get pods` would return pods in the `seattle` namespace. This is because pods are
a namespaced resource, and no namespace was provided in the command. Review the output
of `kubectl api-resources` to determine if a resource is namespaced.

Explicit use of `--namespace <value>` overrides this behavior.

**How kubectl handles ServiceAccount tokens**

If:

* there is Kubernetes service account token file mounted at
  `/var/run/secrets/kubernetes.io/serviceaccount/token`, and
* the `KUBERNETES_SERVICE_HOST` environment variable is set, and
* the `KUBERNETES_SERVICE_PORT` environment variable is set, and
* you don't explicitly specify a namespace on the kubectl command line

then kubectl assumes it is running in your cluster. The kubectl tool looks up the
namespace of that ServiceAccount (this is the same as the namespace of the Pod)
and acts against that namespace. This is different from what happens outside of a
cluster; when kubectl runs outside a cluster and you don't specify a namespace,
the kubectl command acts against the namespace set for the current context in your
client configuration. To change the default namespace for your kubectl you can use the
following command:

```
kubectl config set-context --current --namespace=<namespace-name>
```

## Operations

The following table includes short descriptions and the general syntax for all of the `kubectl` operations:

| Operation | Syntax | Description |
| --- | --- | --- |
| `alpha` | `kubectl alpha SUBCOMMAND [flags]` | List the available commands that correspond to alpha features, which are not enabled in Kubernetes clusters by default. |
| `annotate` | `kubectl annotate (-f FILENAME | TYPE NAME | TYPE/NAME) KEY_1=VAL_1 ... KEY_N=VAL_N [--overwrite] [--all] [--resource-version=version] [flags]` | Add or update the annotations of one or more resources. |
| `api-resources` | `kubectl api-resources [flags]` | List the API resources that are available. |
| `api-versions` | `kubectl api-versions [flags]` | List the API versions that are available. |
| `apply` | `kubectl apply -f FILENAME [flags]` | Apply a configuration change to a resource from a file or stdin. |
| `attach` | `kubectl attach POD -c CONTAINER [-i] [-t] [flags]` | Attach to a running container either to view the output stream or interact with the container (stdin). |
| `auth` | `kubectl auth [flags] [options]` | Inspect authorization. |
| `autoscale` | `kubectl autoscale (-f FILENAME | TYPE NAME | TYPE/NAME) [--min=MINPODS] --max=MAXPODS [--cpu-percent=CPU] [flags]` | Automatically scale the set of pods that are managed by a replication controller. |
| `certificate` | `kubectl certificate SUBCOMMAND [options]` | Modify certificate resources. |
| `cluster-info` | `kubectl cluster-info [flags]` | Display endpoint information about the master and services in the cluster. |
| `completion` | `kubectl completion SHELL [options]` | Output shell completion code for the specified shell (bash or zsh). |
| `config` | `kubectl config SUBCOMMAND [flags]` | Modifies kubeconfig files. See the individual subcommands for details. |
| `convert` | `kubectl convert -f FILENAME [options]` | Convert config files between different API versions. Both YAML and JSON formats are accepted. Note - requires `kubectl-convert` plugin to be installed. |
| `cordon` | `kubectl cordon NODE [options]` | Mark node as unschedulable. |
| `cp` | `kubectl cp <file-spec-src> <file-spec-dest> [options]` | Copy files and directories to and from containers. |
| `create` | `kubectl create -f FILENAME [flags]` | Create one or more resources from a file or stdin. |
| `delete` | `kubectl delete (-f FILENAME | TYPE [NAME | /NAME | -l label | --all]) [flags]` | Delete resources either from a file, stdin, or specifying label selectors, names, resource selectors, or resources. |
| `describe` | `kubectl describe (-f FILENAME | TYPE [NAME_PREFIX | /NAME | -l label]) [flags]` | Display the detailed state of one or more resources. |
| `diff` | `kubectl diff -f FILENAME [flags]` | Diff file or stdin against live configuration. |
| `drain` | `kubectl drain NODE [options]` | Drain node in preparation for maintenance. |
| `edit` | `kubectl edit (-f FILENAME | TYPE NAME | TYPE/NAME) [flags]` | Edit and update the definition of one or more resources on the server by using the default editor. |
| `events` | `kubectl events` | List events |
| `exec` | `kubectl exec POD [-c CONTAINER] [-i] [-t] [flags] [-- COMMAND [args...]]` | Execute a command against a container in a pod. |
| `explain` | `kubectl explain TYPE [--recursive=false] [flags]` | Get documentation of various resources. For instance pods, nodes, services, etc. |
| `expose` | `kubectl expose (-f FILENAME | TYPE NAME | TYPE/NAME) [--port=port] [--protocol=TCP|UDP] [--target-port=number-or-name] [--name=name] [--external-ip=external-ip-of-service] [--type=type] [flags]` | Expose a replication controller, service, or pod as a new Kubernetes service. |
| `get` | `kubectl get (-f FILENAME | TYPE [NAME | /NAME | -l label]) [--watch] [--sort-by=FIELD] [[-o | --output]=OUTPUT_FORMAT] [flags]` | List one or more resources. |
| `kustomize` | `kubectl kustomize <dir> [flags] [options]` | List a set of API resources generated from instructions in a kustomization.yaml file. The argument must be the path to the directory containing the file, or a git repository URL with a path suffix specifying same with respect to the repository root. |
| `label` | `kubectl label (-f FILENAME | TYPE NAME | TYPE/NAME) KEY_1=VAL_1 ... KEY_N=VAL_N [--overwrite] [--all] [--resource-version=version] [flags]` | Add or update the labels of one or more resources. |
| `logs` | `kubectl logs POD [-c CONTAINER] [--follow] [flags]` | Print the logs for a container in a pod. |
| `options` | `kubectl options` | List of global command-line options, which apply to all commands. |
| `patch` | `kubectl patch (-f FILENAME | TYPE NAME | TYPE/NAME) --patch PATCH [flags]` | Update one or more fields of a resource by using the strategic merge patch process. |
| `plugin` | `kubectl plugin [flags] [options]` | Provides utilities for interacting with plugins. |
| `port-forward` | `kubectl port-forward POD [LOCAL_PORT:]REMOTE_PORT [...[LOCAL_PORT_N:]REMOTE_PORT_N] [flags]` | Forward one or more local ports to a pod. |
| `proxy` | `kubectl proxy [--port=PORT] [--www=static-dir] [--www-prefix=prefix] [--api-prefix=prefix] [flags]` | Run a proxy to the Kubernetes API server. |
| `replace` | `kubectl replace -f FILENAME` | Replace a resource from a file or stdin. |
| `rollout` | `kubectl rollout SUBCOMMAND [options]` | Manage the rollout of a resource. Valid resource types include: deployments, daemonsets and statefulsets. |
| `run` | `kubectl run NAME --image=image [--env="key=value"] [--port=port] [--dry-run=server|client|none] [--overrides=inline-json] [flags]` | Run a specified image on the cluster. |
| `scale` | `kubectl scale (-f FILENAME | TYPE NAME | TYPE/NAME) --replicas=COUNT [--resource-version=version] [--current-replicas=count] [flags]` | Update the size of the specified replication controller. |
| `set` | `kubectl set SUBCOMMAND [options]` | Configure application resources. |
| `taint` | `kubectl taint NODE NAME KEY_1=VAL_1:TAINT_EFFECT_1 ... KEY_N=VAL_N:TAINT_EFFECT_N [options]` | Update the taints on one or more nodes. |
| `top` | `kubectl top (POD | NODE) [flags] [options]` | Display Resource (CPU/Memory/Storage) usage of pod or node. |
| `uncordon` | `kubectl uncordon NODE [options]` | Mark node as schedulable. |
| `version` | `kubectl version [--client] [flags]` | Display the Kubernetes version running on the client and server. |
| `wait` | `kubectl wait ([-f FILENAME] | resource.group/resource.name | resource.group [(-l label | --all)]) [--for=delete|--for condition=available] [options]` | Experimental: Wait for a specific condition on one or many resources. |

To learn more about command operations, see the [kubectl](/docs/reference/kubectl/kubectl/) reference documentation.

## Resource types

The following table includes a list of all the supported resource types and their abbreviated aliases.

(This output can be retrieved from `kubectl api-resources`, and was accurate as of Kubernetes 1.25.0)

| NAME | SHORTNAMES | APIVERSION | NAMESPACED | KIND |
| --- | --- | --- | --- | --- |
| `bindings` |  | v1 | true | Binding |
| `componentstatuses` | `cs` | v1 | false | ComponentStatus |
| `configmaps` | `cm` | v1 | true | ConfigMap |
| `endpoints` | `ep` | v1 | true | Endpoints |
| `events` | `ev` | v1 | true | Event |
| `limitranges` | `limits` | v1 | true | LimitRange |
| `namespaces` | `ns` | v1 | false | Namespace |
| `nodes` | `no` | v1 | false | Node |
| `persistentvolumeclaims` | `pvc` | v1 | true | PersistentVolumeClaim |
| `persistentvolumes` | `pv` | v1 | false | PersistentVolume |
| `pods` | `po` | v1 | true | Pod |
| `podtemplates` |  | v1 | true | PodTemplate |
| `replicationcontrollers` | `rc` | v1 | true | ReplicationController |
| `resourcequotas` | `quota` | v1 | true | ResourceQuota |
| `secrets` |  | v1 | true | Secret |
| `serviceaccounts` | `sa` | v1 | true | ServiceAccount |
| `services` | `svc` | v1 | true | Service |
| `mutatingwebhookconfigurations` |  | admissionregistration.k8s.io/v1 | false | MutatingWebhookConfiguration |
| `validatingwebhookconfigurations` |  | admissionregistration.k8s.io/v1 | false | ValidatingWebhookConfiguration |
| `customresourcedefinitions` | `crd,crds` | apiextensions.k8s.io/v1 | false | CustomResourceDefinition |
| `apiservices` |  | apiregistration.k8s.io/v1 | false | APIService |
| `controllerrevisions` |  | apps/v1 | true | ControllerRevision |
| `daemonsets` | `ds` | apps/v1 | true | DaemonSet |
| `deployments` | `deploy` | apps/v1 | true | Deployment |
| `replicasets` | `rs` | apps/v1 | true | ReplicaSet |
| `statefulsets` | `sts` | apps/v1 | true | StatefulSet |
| `tokenreviews` |  | authentication.k8s.io/v1 | false | TokenReview |
| `localsubjectaccessreviews` |  | authorization.k8s.io/v1 | true | LocalSubjectAccessReview |
| `selfsubjectaccessreviews` |  | authorization.k8s.io/v1 | false | SelfSubjectAccessReview |
| `selfsubjectrulesreviews` |  | authorization.k8s.io/v1 | false | SelfSubjectRulesReview |
| `subjectaccessreviews` |  | authorization.k8s.io/v1 | false | SubjectAccessReview |
| `horizontalpodautoscalers` | `hpa` | autoscaling/v2 | true | HorizontalPodAutoscaler |
| `cronjobs` | `cj` | batch/v1 | true | CronJob |
| `jobs` |  | batch/v1 | true | Job |
| `certificatesigningrequests` | `csr` | certificates.k8s.io/v1 | false | CertificateSigningRequest |
| `leases` |  | coordination.k8s.io/v1 | true | Lease |
| `endpointslices` |  | discovery.k8s.io/v1 | true | EndpointSlice |
| `events` | `ev` | events.k8s.io/v1 | true | Event |
| `flowschemas` |  | flowcontrol.apiserver.k8s.io/v1beta2 | false | FlowSchema |
| `prioritylevelconfigurations` |  | flowcontrol.apiserver.k8s.io/v1beta2 | false | PriorityLevelConfiguration |
| `ingressclasses` |  | networking.k8s.io/v1 | false | IngressClass |
| `ingresses` | `ing` | networking.k8s.io/v1 | true | Ingress |
| `networkpolicies` | `netpol` | networking.k8s.io/v1 | true | NetworkPolicy |
| `runtimeclasses` |  | node.k8s.io/v1 | false | RuntimeClass |
| `poddisruptionbudgets` | `pdb` | policy/v1 | true | PodDisruptionBudget |
| `podsecuritypolicies` | `psp` | policy/v1beta1 | false | PodSecurityPolicy |
| `clusterrolebindings` |  | rbac.authorization.k8s.io/v1 | false | ClusterRoleBinding |
| `clusterroles` |  | rbac.authorization.k8s.io/v1 | false | ClusterRole |
| `rolebindings` |  | rbac.authorization.k8s.io/v1 | true | RoleBinding |
| `roles` |  | rbac.authorization.k8s.io/v1 | true | Role |
| `priorityclasses` | `pc` | scheduling.k8s.io/v1 | false | PriorityClass |
| `csidrivers` |  | storage.k8s.io/v1 | false | CSIDriver |
| `csinodes` |  | storage.k8s.io/v1 | false | CSINode |
| `csistoragecapacities` |  | storage.k8s.io/v1 | true | CSIStorageCapacity |
| `storageclasses` | `sc` | storage.k8s.io/v1 | false | StorageClass |
| `volumeattachments` |  | storage.k8s.io/v1 | false | VolumeAttachment |

## Output options

Use the following sections for information about how you can format or sort the output
of certain commands. For details about which commands support the various output options,
see the [kubectl](/docs/reference/kubectl/kubectl/) reference documentation.

### Formatting output

The default output format for all `kubectl` commands is the human readable plain-text format.
To output details to your terminal window in a specific format, you can add either the `-o`
or `--output` flags to a supported `kubectl` command.

#### Syntax

```
kubectl [command] [TYPE] [NAME] -o <output_format>
```

Depending on the `kubectl` operation, the following output formats are supported:

| Output format | Description |
| --- | --- |
| `-o custom-columns=<spec>` | Print a table using a comma separated list of [custom columns](#custom-columns). |
| `-o custom-columns-file=<filename>` | Print a table using the [custom columns](#custom-columns) template in the `<filename>` file. |
| `-o json` | Output a JSON formatted API object. |
| `-o jsonpath=<template>` | Print the fields defined in a [jsonpath](/docs/reference/kubectl/jsonpath/) expression. |
| `-o jsonpath-file=<filename>` | Print the fields defined by the [jsonpath](/docs/reference/kubectl/jsonpath/) expression in the `<filename>` file. |
| `-o kyaml` | Output a KYAML formatted API object (alpha, requires environment variable `KUBECTL_KYAML="true"`). |
| `-o name` | Print only the resource name and nothing else. |
| `-o wide` | Output in the plain-text format with any additional information. For pods, the node name is included. |
| `-o yaml` | Output a YAML formatted API object. KYAML is an experimental Kubernetes-specific dialect of YAML, and can be parsed as YAML. |

##### Example

In this example, the following command outputs the details for a single pod as a YAML formatted object:

```
kubectl get pod web-pod-13je7 -o yaml
```

Remember: See the [kubectl](/docs/reference/kubectl/kubectl/) reference documentation
for details about which output format is supported by each command.

#### Custom columns

To define custom columns and output only the details that you want into a table, you can use the `custom-columns` option.
You can choose to define the custom columns inline or use a template file: `-o custom-columns=<spec>` or `-o custom-columns-file=<filename>`.

##### Examples

Inline:

```
kubectl get pods <pod-name> -o custom-columns=NAME:.metadata.name,RSRC:.metadata.resourceVersion
```

Template file:

```
kubectl get pods <pod-name> -o custom-columns-file=template.txt
```

where the `template.txt` file contains:

```
NAME          RSRC
metadata.name metadata.resourceVersion
```

The result of running either command is similar to:

```
NAME           RSRC
submit-queue   610995
```

#### Server-side columns

`kubectl` supports receiving specific column information from the server about objects.
This means that for any given resource, the server will return columns and rows relevant to that resource, for the client to print.
This allows for consistent human-readable output across clients used against the same cluster, by having the server encapsulate the details of printing.

This feature is enabled by default. To disable it, add the
`--server-print=false` flag to the `kubectl get` command.

##### Examples

To print information about the status of a pod, use a command like the following:

```
kubectl get pods <pod-name> --server-print=false
```

The output is similar to:

```
NAME       AGE
pod-name   1m
```

### Sorting list objects

To output objects to a sorted list in your terminal window, you can add the `--sort-by` flag
to a supported `kubectl` command. Sort your objects by specifying any numeric or string field
with the `--sort-by` flag. To specify a field, use a [jsonpath](/docs/reference/kubectl/jsonpath/) expression.

#### Syntax

```
kubectl [command] [TYPE] [NAME] --sort-by=<jsonpath_exp>
```

##### Example

To print a list of pods sorted by name, you run:

```
kubectl get pods --sort-by=.metadata.name
```

## Examples: Common operations

Use the following set of examples to help you familiarize yourself with running the commonly used `kubectl` operations:

`kubectl apply` - Apply or Update a resource from a file or stdin.

```
# Create a service using the definition in example-service.yaml.
kubectl apply -f example-service.yaml

# Create a replication controller using the definition in example-controller.yaml.
kubectl apply -f example-controller.yaml

# Create the objects that are defined in any .yaml, .yml, or .json file within the <directory> directory.
kubectl apply -f <directory>
```

`kubectl get` - List one or more resources.

```
# List all pods in plain-text output format.
kubectl get pods

# List all pods in plain-text output format and include additional information (such as node name).
kubectl get pods -o wide

# List the replication controller with the specified name in plain-text output format. Tip: You can shorten and replace the 'replicationcontroller' resource type with the alias 'rc'.
kubectl get replicationcontroller <rc-name>

# List all replication controllers and services together in plain-text output format.
kubectl get rc,services

# List all daemon sets in plain-text output format.
kubectl get ds

# List all pods running on node server01
kubectl get pods --field-selector=spec.nodeName=server01
```

`kubectl describe` - Display detailed state of one or more resources, including the uninitialized ones by default.

```
# Display the details of the node with name <node-name>.
kubectl describe nodes <node-name>

# Display the details of the pod with name <pod-name>.
kubectl describe pods/<pod-name>

# Display the details of all the pods that are managed by the replication controller named <rc-name>.
# Remember: Any pods that are created by the replication controller get prefixed with the name of the replication controller.
kubectl describe pods <rc-name>

# Describe all pods
kubectl describe pods
```

> **Note:**
> The `kubectl get` command is usually used for retrieving one or more
> resources of the same resource type. It features a rich set of flags that allows
> you to customize the output format using the `-o` or `--output` flag, for example.
> You can specify the `-w` or `--watch` flag to start watching updates to a particular
> object. The `kubectl describe` command is more focused on describing the many
> related aspects of a specified resource. It may invoke several API calls to the
> API server to build a view for the user. For example, the `kubectl describe node`
> command retrieves not only the information about the node, but also a summary of
> the pods running on it, the events generated for the node etc.

`kubectl delete` - Delete resources either from a file, stdin, or specifying label selectors, names, resource selectors, or resources.

```
# Delete a pod using the type and name specified in the pod.yaml file.
kubectl delete -f pod.yaml

# Delete all the pods and services that have the label '<label-key>=<label-value>'.
kubectl delete pods,services -l <label-key>=<label-value>

# Delete all pods, including uninitialized ones.
kubectl delete pods --all
```

`kubectl exec` - Execute a command against a container in a pod.

```
# Get output from running 'date' from pod <pod-name>. By default, output is from the first container.
kubectl exec <pod-name> -- date

# Get output from running 'date' in container <container-name> of pod <pod-name>.
kubectl exec <pod-name> -c <container-name> -- date

# Get an interactive TTY and run /bin/bash from pod <pod-name>. By default, output is from the first container.
kubectl exec -ti <pod-name> -- /bin/bash
```

`kubectl logs` - Print the logs for a container in a pod.

```
# Return a snapshot of the logs from pod <pod-name>.
kubectl logs <pod-name>

# Start streaming the logs from pod <pod-name>. This is similar to the 'tail -f' Linux command.
kubectl logs -f <pod-name>
```

`kubectl diff` - View a diff of the proposed updates to a cluster.

```
# Diff resources included in "pod.json".
kubectl diff -f pod.json

# Diff file read from stdin.
cat service.yaml | kubectl diff -f -
```

## Examples: Creating and using plugins

Use the following set of examples to help you familiarize yourself with writing and using `kubectl` plugins:

```
# create a simple plugin in any language and name the resulting executable file
# so that it begins with the prefix "kubectl-"
cat ./kubectl-hello
```

```
#!/bin/sh

# this plugin prints the words "hello world"
echo "hello world"
```

With a plugin written, let's make it executable:

```
chmod a+x ./kubectl-hello

# and move it to a location in our PATH
sudo mv ./kubectl-hello /usr/local/bin
sudo chown root:root /usr/local/bin

# You have now created and "installed" a kubectl plugin.
# You can begin using this plugin by invoking it from kubectl as if it were a regular command
kubectl hello
```

```
hello world
```

```
# You can "uninstall" a plugin, by removing it from the folder in your
# $PATH where you placed it
sudo rm /usr/local/bin/kubectl-hello
```

In order to view all of the plugins that are available to `kubectl`, use
the `kubectl plugin list` subcommand:

```
kubectl plugin list
```

The output is similar to:

```
The following kubectl-compatible plugins are available:

/usr/local/bin/kubectl-hello
/usr/local/bin/kubectl-foo
/usr/local/bin/kubectl-bar
```

`kubectl plugin list` also warns you about plugins that are not
executable, or that are shadowed by other plugins; for example:

```
sudo chmod -x /usr/local/bin/kubectl-foo # remove execute permission
kubectl plugin list
```

```
The following kubectl-compatible plugins are available:

/usr/local/bin/kubectl-hello
/usr/local/bin/kubectl-foo
  - warning: /usr/local/bin/kubectl-foo identified as a plugin, but it is not executable
/usr/local/bin/kubectl-bar

error: one plugin warning was found
```

You can think of plugins as a means to build more complex functionality on top
of the existing kubectl commands:

```
cat ./kubectl-whoami
```

The next few examples assume that you already made `kubectl-whoami` have
the following contents:

```
#!/bin/bash

# this plugin makes use of the `kubectl config` command in order to output
# information about the current user, based on the currently selected context
kubectl config view --template='{{ range .contexts }}{{ if eq .name "'$(kubectl config current-context)'" }}Current user: {{ printf "%s\n" .context.user }}{{ end }}{{ end }}'
```

Running the above command gives you an output containing the user for the
current context in your KUBECONFIG file:

```
# make the file executable
sudo chmod +x ./kubectl-whoami

# and move it into your PATH
sudo mv ./kubectl-whoami /usr/local/bin

kubectl whoami
Current user: plugins-user
```

## What's next

* Read the `kubectl` reference documentation:
  + the kubectl [command reference](/docs/reference/kubectl/kubectl/)
  + the [command line arguments](/docs/reference/kubectl/generated/kubectl/) reference
* Learn about [`kubectl` usage conventions](/docs/reference/kubectl/conventions/)
* Read about [JSONPath support](/docs/reference/kubectl/jsonpath/) in kubectl
* Read about how to [extend kubectl with plugins](/docs/tasks/extend-kubectl/kubectl-plugins/)
  + To find out more about plugins, take a look at the [example CLI plugin](https://github.com/kubernetes/sample-cli-plugin).
