# Kubelet Configuration Directory Merging

When using the kubelet's `--config-dir` flag to specify a drop-in directory for
configuration, there is some specific behavior on how different types are
merged.

Here are some examples of how different data types behave during configuration merging:

### Structure Fields

There are two types of structure fields in a YAML structure: singular (or a
scalar type) and embedded (structures that contain scalar types).
The configuration merging process handles the overriding of singular and embedded struct fields to create a resulting kubelet configuration.

For instance, you may want a baseline kubelet configuration for all nodes, but you may want to customize the `address` and `authorization` fields.
This can be done as follows:

Main kubelet configuration file contents:

```
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
port: 20250
authorization:
  mode: Webhook
  webhook:
    cacheAuthorizedTTL: "5m"
    cacheUnauthorizedTTL: "30s"
serializeImagePulls: false
address: "192.168.0.1"
```

Contents of a file in `--config-dir` directory:

```
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
authorization:
  mode: AlwaysAllow
  webhook:
    cacheAuthorizedTTL: "8m"
    cacheUnauthorizedTTL: "45s"
address: "192.168.0.8"
```

The resulting configuration will be as follows:

```
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
port: 20250
serializeImagePulls: false
authorization:
  mode: AlwaysAllow
  webhook:
    cacheAuthorizedTTL: "8m"
    cacheUnauthorizedTTL: "45s"
address: "192.168.0.8"
```

### Lists

You can override the slices/lists values of the kubelet configuration.
However, the entire list gets overridden during the merging process.
For example, you can override the `clusterDNS` list as follows:

Main kubelet configuration file contents:

```
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
port: 20250
serializeImagePulls: false
clusterDNS:
  - "192.168.0.9"
  - "192.168.0.8"
```

Contents of a file in `--config-dir` directory:

```
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
clusterDNS:
  - "192.168.0.2"
  - "192.168.0.3"
  - "192.168.0.5"
```

The resulting configuration will be as follows:

```
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
port: 20250
serializeImagePulls: false
clusterDNS:
  - "192.168.0.2"
  - "192.168.0.3"
  - "192.168.0.5"
```

### Maps, including Nested Structures

Individual fields in maps, regardless of their value types (boolean, string, etc.), can be selectively overridden.
However, for `map[string][]string`, the entire list associated with a specific field gets overridden.
Let's understand this better with an example, particularly on fields like `featureGates` and `staticPodURLHeader`:

Main kubelet configuration file contents:

```
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
port: 20250
serializeImagePulls: false
featureGates:
  AllAlpha: false
  MemoryQoS: true
staticPodURLHeader:
  kubelet-api-support:
  - "Authorization: 234APSDFA"
  - "X-Custom-Header: 123"
  custom-static-pod:
  - "Authorization: 223EWRWER"
  - "X-Custom-Header: 456"
```

Contents of a file in `--config-dir` directory:

```
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
featureGates:
  MemoryQoS: false
  KubeletTracing: true
  DynamicResourceAllocation: true
staticPodURLHeader:
  custom-static-pod:
  - "Authorization: 223EWRWER"
  - "X-Custom-Header: 345"
```

The resulting configuration will be as follows:

```
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
port: 20250
serializeImagePulls: false
featureGates:
  AllAlpha: false
  MemoryQoS: false
  KubeletTracing: true
  DynamicResourceAllocation: true
staticPodURLHeader:
  kubelet-api-support:
  - "Authorization: 234APSDFA"
  - "X-Custom-Header: 123"
  custom-static-pod:
  - "Authorization: 223EWRWER"
  - "X-Custom-Header: 345"
```

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
