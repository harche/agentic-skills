# JSONPath Support

The [kubectl](/docs/reference/kubectl/ "A command line tool for communicating with a Kubernetes cluster.") tool supports JSONPath templates as an output format.

A *JSONPath template* is composed of JSONPath expressions enclosed by curly braces: `{` and `}`.
Kubectl uses JSONPath expressions to filter on specific fields in the JSON object and format the output.
In addition to the original JSONPath template syntax, the following functions and syntax are valid:

1. Use double quotes to quote text inside JSONPath expressions.
2. Use the `range`, `end` operators to iterate lists.
3. Use negative slice indices to step backwards through a list.
   Negative indices do *not* "wrap around" a list and are valid as long as \( ( - index + listLength ) \ge 0 \).

> **Note:**
> * The `$` operator is optional since the expression always starts from the root object by default.
> * The result object is printed as its `String()` function.

## Functions in Kubernetes JSONPath

Given the JSON input:

```
{
  "kind": "List",
  "items":[
    {
      "kind":"None",
      "metadata":{
        "name":"127.0.0.1",
        "labels":{
          "kubernetes.io/hostname":"127.0.0.1"
        }
      },
      "status":{
        "capacity":{"cpu":"4"},
        "addresses":[{"type": "LegacyHostIP", "address":"127.0.0.1"}]
      }
    },
    {
      "kind":"None",
      "metadata":{"name":"127.0.0.2"},
      "status":{
        "capacity":{"cpu":"8"},
        "addresses":[
          {"type": "LegacyHostIP", "address":"127.0.0.2"},
          {"type": "another", "address":"127.0.0.3"}
        ]
      }
    }
  ],
  "users":[
    {
      "name": "myself",
      "user": {}
    },
    {
      "name": "e2e",
      "user": {"username": "admin", "password": "secret"}
    }
  ]
}
```

Functions, their parameters, an example invocation, and the result

| Function | Description | Example | Result |
| --- | --- | --- | --- |
| `text` | the plain text | `kind is {.kind}` | `kind is List` |
| `@` | the current object | `{@}` | the same as input |
| `.` or `[]` | child operator | `{.kind}`, `{['kind']}` or `{['name\.type']}` | `List` |
| `..` | recursive descent | `{..name}` | `127.0.0.1 127.0.0.2 myself e2e` |
| `*` | wildcard. Get all objects | `{.items[*].metadata.name}` | `[127.0.0.1 127.0.0.2]` |
| `[start:end:step]` | subscript operator | `{.users[0].name}` | `myself` |
| `[,]` | union operator | `{.items[*]['metadata.name', 'status.capacity']}` | `127.0.0.1 127.0.0.2 map[cpu:4] map[cpu:8]` |
| `?()` | filter | `{.users[?(@.name=="e2e")].user.password}` | `secret` |
| `range`, `end` | iterate list | `{range .items[*]}[{.metadata.name}, {.status.capacity}] {end}` | `[127.0.0.1, map[cpu:4]] [127.0.0.2, map[cpu:8]]` |
| `''` | quote interpreted string | `{range .items[*]}{.metadata.name}{'\t'}{end}` | `127.0.0.1 127.0.0.2` |
| `\` | escape termination character | `{.items[0].metadata.labels.kubernetes\.io/hostname}` | `127.0.0.1` |

## Using JSONPath expressions with kubectl

Examples using `kubectl` and JSONPath expressions:

```
kubectl get pods -o json
kubectl get pods -o=jsonpath='{@}'
kubectl get pods -o=jsonpath='{.items[0]}'
kubectl get pods -o=jsonpath='{.items[0].metadata.name}'
kubectl get pods -o=jsonpath="{.items[*]['metadata.name', 'status.capacity']}"
kubectl get pods -o=jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.startTime}{"\n"}{end}'
kubectl get pods -o=jsonpath='{.items[0].metadata.labels.kubernetes\.io/hostname}'
```

Or, with a "my_pod" and "my_namespace" (adjust these names to your environment):

```
kubectl get pod/my_pod -n my_namespace -o=jsonpath='{@}'
kubectl get pod/my_pod -n my_namespace -o=jsonpath='{.metadata.name}'
kubectl get pod/my_pod -n my_namespace -o=jsonpath='{.status}'
```

> **Note:**
> On Windows, you must *double* quote any JSONPath template that contains spaces (not single quote as shown above for bash). This in turn means that you must use a single quote or escaped double quote around any literals in the template. For example:
>
> ```
> kubectl get pods -o=jsonpath="{range .items[*]}{.metadata.name}{'\t'}{.status.startTime}{'\n'}{end}"
> kubectl get pods -o=jsonpath="{range .items[*]}{.metadata.name}{\"\t\"}{.status.startTime}{\"\n\"}{end}"
> ```

## Regular expressions in JSONPath

JSONPath regular expressions are not supported. If you want to match using regular expressions, you can use a tool such as `jq`.

```
# kubectl does not support regular expressions for JSONpath output
# The following command does not work
kubectl get pods -o jsonpath='{.items[?(@.metadata.name=~/^test$/)].metadata.name}'

# The following command achieves the desired result
kubectl get pods -o json | jq -r '.items[] | select(.metadata.name | test("test-")).metadata.name'
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
