# Client Libraries

This page contains an overview of the client libraries for using the Kubernetes
API from various programming languages.

To write applications using the [Kubernetes REST API](/docs/reference/using-api/),
you do not need to implement the API calls and request/response types yourself.
You can use a client library for the programming language you are using.

Client libraries often handle common tasks such as authentication for you.
Most client libraries can discover and use the Kubernetes Service Account to
authenticate if the API client is running inside the Kubernetes cluster, or can
understand the [kubeconfig file](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)
format to read the credentials and the API Server address.

## Officially-supported Kubernetes client libraries

The following client libraries are officially maintained by
[Kubernetes SIG API Machinery](https://github.com/kubernetes/community/tree/master/sig-api-machinery).

| Language | Client Library | Sample Programs |
| --- | --- | --- |
| C | [github.com/kubernetes-client/c](https://github.com/kubernetes-client/c/) | [browse](https://github.com/kubernetes-client/c/tree/master/examples) |
| dotnet | [github.com/kubernetes-client/csharp](https://github.com/kubernetes-client/csharp) | [browse](https://github.com/kubernetes-client/csharp/tree/master/examples) |
| Go | [github.com/kubernetes/client-go/](https://github.com/kubernetes/client-go/) | [browse](https://github.com/kubernetes/client-go/tree/master/examples) |
| Haskell | [github.com/kubernetes-client/haskell](https://github.com/kubernetes-client/haskell) | [browse](https://github.com/kubernetes-client/haskell/tree/master/kubernetes-client/example) |
| Java | [github.com/kubernetes-client/java](https://github.com/kubernetes-client/java/) | [browse](https://github.com/kubernetes-client/java/tree/master/examples) |
| JavaScript | [github.com/kubernetes-client/javascript](https://github.com/kubernetes-client/javascript) | [browse](https://github.com/kubernetes-client/javascript/tree/master/examples) |
| Perl | [github.com/kubernetes-client/perl/](https://github.com/kubernetes-client/perl/) | [browse](https://github.com/kubernetes-client/perl/tree/master/examples) |
| Python | [github.com/kubernetes-client/python/](https://github.com/kubernetes-client/python/) | [browse](https://github.com/kubernetes-client/python/tree/master/examples) |
| Ruby | [github.com/kubernetes-client/ruby/](https://github.com/kubernetes-client/ruby/) | [browse](https://github.com/kubernetes-client/ruby/tree/master/examples) |

## Community-maintained client libraries

> **Note:**
> **Note:** This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](/docs/contribute/style/content-guide/#third-party-content) before submitting a change. [More information.](#third-party-content-disclaimer)

The following Kubernetes API client libraries are provided and maintained by
their authors, not the Kubernetes team.

| Language | Client Library |
| --- | --- |
| Clojure | [github.com/yanatan16/clj-kubernetes-api](https://github.com/yanatan16/clj-kubernetes-api) |
| DotNet | [github.com/tonnyeremin/kubernetes_gen](https://github.com/tonnyeremin/kubernetes_gen) |
| DotNet (RestSharp) | [github.com/masroorhasan/Kubernetes.DotNet](https://github.com/masroorhasan/Kubernetes.DotNet) |
| Elixir | [github.com/obmarg/kazan](https://github.com/obmarg/kazan/) |
| Elixir | [github.com/coryodaniel/k8s](https://github.com/coryodaniel/k8s) |
| Java (OSGi) | [bitbucket.org/amdatulabs/amdatu-kubernetes](https://bitbucket.org/amdatulabs/amdatu-kubernetes) |
| Java (Fabric8, OSGi) | [github.com/fabric8io/kubernetes-client](https://github.com/fabric8io/kubernetes-client) |
| Java | [github.com/manusa/yakc](https://github.com/manusa/yakc) |
| Lisp | [github.com/brendandburns/cl-k8s](https://github.com/brendandburns/cl-k8s) |
| Lisp | [github.com/xh4/cube](https://github.com/xh4/cube) |
| Node.js (TypeScript) | [github.com/Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) |
| Node.js | [github.com/ajpauwels/easy-k8s](https://github.com/ajpauwels/easy-k8s) |
| Node.js | [github.com/godaddy/kubernetes-client](https://github.com/godaddy/kubernetes-client) |
| Node.js | [github.com/tenxcloud/node-kubernetes-client](https://github.com/tenxcloud/node-kubernetes-client) |
| Perl | [metacpan.org/pod/Net::Kubernetes](https://metacpan.org/pod/Net::Kubernetes) |
| PHP | [github.com/allansun/kubernetes-php-client](https://github.com/allansun/kubernetes-php-client) |
| PHP | [github.com/maclof/kubernetes-client](https://github.com/maclof/kubernetes-client) |
| PHP | [github.com/travisghansen/kubernetes-client-php](https://github.com/travisghansen/kubernetes-client-php) |
| PHP | [github.com/renoki-co/php-k8s](https://github.com/renoki-co/php-k8s) |
| Python | [github.com/cloudcoil/cloudcoil](https://github.com/cloudcoil/cloudcoil) |
| Python | [github.com/fiaas/k8s](https://github.com/fiaas/k8s) |
| Python | [github.com/gtsystem/lightkube](https://github.com/gtsystem/lightkube) |
| Python | [github.com/kr8s-org/kr8s](https://github.com/kr8s-org/kr8s) |
| Python | [github.com/mnubo/kubernetes-py](https://github.com/mnubo/kubernetes-py) |
| Python | [github.com/tomplus/kubernetes_asyncio](https://github.com/tomplus/kubernetes_asyncio) |
| Python | [github.com/Frankkkkk/pykorm](https://github.com/Frankkkkk/pykorm) |
| Ruby | [github.com/abonas/kubeclient](https://github.com/abonas/kubeclient) |
| Ruby | [github.com/k8s-ruby/k8s-ruby](https://github.com/k8s-ruby/k8s-ruby) |
| Ruby | [github.com/kontena/k8s-client](https://github.com/kontena/k8s-client) |
| Rust | [github.com/kube-rs/kube](https://github.com/kube-rs/kube) |
| Rust | [github.com/ynqa/kubernetes-rust](https://github.com/ynqa/kubernetes-rust) |
| Scala | [github.com/hagay3/skuber](https://github.com/hagay3/skuber) |
| Scala | [github.com/hnaderi/scala-k8s](https://github.com/hnaderi/scala-k8s) |
| Scala | [github.com/joan38/kubernetes-client](https://github.com/joan38/kubernetes-client) |
| Swift | [github.com/swiftkube/client](https://github.com/swiftkube/client) |

Items on this page refer to third party products or projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for those third-party products or projects. See the [CNCF website guidelines](https://github.com/cncf/foundation/blob/master/website-guidelines.md) for more details.

You should read the [content guide](/docs/contribute/style/content-guide/#third-party-content) before proposing a change that adds an extra third-party link.

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
