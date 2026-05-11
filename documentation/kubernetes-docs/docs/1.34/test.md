# Docs smoke test page

#### Shutdown of interactive tutorials

The interactive tutorials previously on this website have been shut down.

Kubernetes is grateful to O'Reilly and Katacoda for many years of helping
people take their first steps in learning Kubernetes.

The shutdown followed O'Reilly Media's 2019
[acquisition](https://www.oreilly.com/content/oreilly-acquires-katacoda-and-a-new-way-for-2-5m-customers-to-learn/)
of Katacoda.

---

The tutorials ceased to function after the **31st of March,
2023**. You are seeing this notice because this particular page has not yet been updated
following that shutdown.

This page serves two purposes:

* Demonstrate how the Kubernetes documentation uses Markdown
* Provide a "smoke test" document we can use to test HTML, CSS, and template
  changes that affect the overall documentation.

## Heading levels

The above heading is an H2. The page title renders as an H1. The following
sections show H3 - H6.

```
### H3

This is in an H3 section.

#### H4

This is in an H4 section.

##### H5

This is in an H5 section.

###### H6

This is in an H6 section.
```

Produces:

### H3

This is in an H3 section.

#### H4

This is in an H4 section.

##### H5

This is in an H5 section.

###### H6

This is in an H6 section.

## Inline elements

Inline elements show up within the text of paragraph, list item, admonition, or
other block-level element.

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.

### Inline text styles

You can use different text styles in markdown like:

```
- **bold**
- _italic_
- ***bold italic***
- ~~strikethrough~~
- <u>underline</u>
- _<u>underline italic</u>_
- **<u>underline bold</u>**
- ***<u>underline bold italic</u>***
- `monospace text`
- **`monospace bold`**
```

Produces:

* **bold**
* *italic*
* ***bold italic***
* ~~strikethrough~~
* underline
* *underline italic*
* **underline bold**
* ***underline bold italic***
* `monospace text`
* **`monospace bold`**

## Lists

Markdown doesn't have strict rules about how to process lists. When we moved
from Jekyll to Hugo, we broke some lists. To fix them, keep the following in
mind:

* Make sure you indent sub-list items **2 spaces**.
* To end a list and start another, you need an HTML comment block on a new line
  between the lists, flush with the left-hand border. The first list won't end
  otherwise, no matter how many blank lines you put between it and the second.

### Bullet lists

You can add a bullet list in markdown like:

```
- This is a list item.
* This is another list item in the same list.
- You can mix `-` and `*`.
  - To make a sub-item, indent two spaces.
    - This is a sub-sub-item. Indent two more spaces.
  - Another sub-item.
```

Produces:

* This is a list item.

* This is another list item in the same list.

* You can mix `-` and `*`.
  + To make a sub-item, indent two spaces.
    - This is a sub-sub-item. Indent two more spaces.
  + Another sub-item.

Also,

* This is a new list. With Hugo, you need to use a HTML comment to separate two
  consecutive lists. **The HTML comment needs to be at the left margin.**
* Bullet lists can have paragraphs or block elements within them.

  Indent the content to be the same as the first line of the bullet point.
  **This paragraph and the code block line up with the first `B` in `Bullet`
  above.**

  ```
  ls -l
  ```

  + And a sub-list after some block-level content
* A bullet list item can contain a numbered list.

  1. Numbered sub-list item 1
  2. Numbered sub-list item 2

### Numbered lists

1. This is a list item.
2. This is another list item in the same list. The number you use in Markdown
   does not necessarily correlate to the number in the final output. By
   convention, we keep them in sync.

> **Note:**
> For single-digit numbered lists, using two spaces after the period makes
> interior block-level content line up better along tab-stops.

1. This is a new list. With Hugo, you need to use an HTML comment to separate
   two consecutive lists. **The HTML comment needs to be at the left margin.**
2. Numbered lists can have paragraphs or block elements within them.

   Indent the content to be the same as the first line of the bullet
   point. **This paragraph and the code block line up with the `N` in
   `Numbered` above.**

   ```
   ls -l
   ```

   * And a sub-list after some block-level content. This is at the same
     "level" as the paragraph and code block above, despite being indented
     more.

### Tab lists

Tab lists can be used to conditionally display content, e.g., when multiple
options must be documented that require distinct instructions or context.

* Choose one...
  * Formatting tab lists
    * Nested headers

Please select an option.

Tabs may also nest formatting styles.

1. Ordered
2. (Or unordered)
3. Lists

```
echo 'Tab lists may contain code blocks!'
```

### Header within a tab list

Nested header tags may also be included.

> **Warning:**
> Headers within tab lists will not appear in the Table of Contents.

### Checklists

Checklists are technically bullet lists, but the bullets are suppressed by CSS.

* This is a checklist item
* This is a selected checklist item

## Code blocks

You can create code blocks two different ways by surrounding the code block with
three back-tick characters on lines before and after the code block. **Only use
back-ticks (code fences) for code blocks.** This allows you to specify the
language of the enclosed code, which enables syntax highlighting. It is also more
predictable than using indentation.

```
this is a code block created by back-ticks
```

The back-tick method has some advantages.

* It works nearly every time.
* It is more compact when viewing the source code.
* It allows you to specify what language the code block is in, for syntax
  highlighting.
* It has a definite ending. Sometimes, the indentation method breaks with
  languages where spacing is significant, like Python or YAML.

To specify the language for the code block, put it directly after the first
grouping of back-ticks:

```
ls -l
```

Common languages used in Kubernetes documentation code blocks include:

* `bash` / `shell` (both work the same)
* `go`
* `json`
* `yaml`
* `xml`
* `none` (disables syntax highlighting for the block)

### Code blocks containing Hugo shortcodes

To show raw Hugo shortcodes as in the above example and prevent Hugo
from interpreting them, use C-style comments directly after the `<` and before
the `>` characters. The following example illustrates this (view the Markdown
source for this page).

```
{{< alert color="warning" >}}This is a warning.{{< /alert >}}
```

## Links

To format a link, put the link text inside square brackets, followed by the
link target in parentheses.

* `[Link to Kubernetes.io](https://kubernetes.io/)` or
* `[Relative link to Kubernetes.io](/)`

You can also use HTML, but it is not preferred.
For example, `<a href="https://kubernetes.io/">Link to Kubernetes.io</a>`.

## Images

To format an image, use similar syntax to [links](#links), but add a leading `!`
character. The square brackets contain the image's alt text. Try to always use
alt text so that people using screen readers can get some benefit from the
image.

```
![pencil icon](/images/pencil.png)
```

Produces:

![pencil icon](/images/pencil.png)

To specify extended attributes, such as width, title, caption, etc, use the
[figure shortcode](https://gohugo.io/content-management/shortcodes/#figure),
which is preferred to using a HTML `<img>` tag. Also, if you need the image to
also be a hyperlink, use the `link` attribute, rather than wrapping the whole
figure in Markdown link syntax as shown below.

![An image used to illustrate the figure shortcode](/images/pencil.png)

#### Pencil icon

An image used to illustrate the figure shortcode

Even if you choose not to use the figure shortcode, an image can also be a link. This
time the pencil icon links to the Kubernetes website. Outer square brackets enclose
the entire image tag, and the link target is in the parentheses at the end.

```
[![pencil icon](/images/pencil.png)](https://kubernetes.io)
```

Produces:

[![pencil icon](/images/pencil.png)](https://kubernetes.io)

You can also use HTML for images, but it is not preferred.

```
<img src="/images/pencil.png" alt="pencil icon" />
```

Produces:

![pencil icon](/images/pencil.png)

## Tables

Simple tables have one row per line, and columns are separated by `|`
characters. The header is separated from the body by cells containing nothing
but at least three `-` characters. For ease of maintenance, try to keep all the
cell separators even, even if you heed to use extra space.

| Heading cell 1 | Heading cell 2 |
| --- | --- |
| Body cell 1 | Body cell 2 |

The header is optional. Any text separated by `|` will render as a table.

Markdown tables have a hard time with block-level elements within cells, such as
list items, code blocks, or multiple paragraphs. For complex or very wide
tables, use HTML instead.

```
<table>
<thead>
  <tr>
    <th>Heading cell 1</th>
    <th>Heading cell 2</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Body cell 1</td>
    <td>Body cell 2</td>
  </tr>
</tbody>
</table>
```

Produces:

| Heading cell 1 | Heading cell 2 |
| --- | --- |
| Body cell 1 | Body cell 2 |

## Visualizations with Mermaid

You can use [Mermaid JS](https://mermaidjs.github.io) visualizations.
The Mermaid JS version is specified in [/layouts/partials/head.html](https://github.com/kubernetes/website/blob/main/layouts/partials/head.html)

```
{{< mermaid >}}
graph TD;
  A-->B;
  A-->C;
  B-->D;
  C-->D;
{{</ mermaid >}}
```

Produces:

```
graph TD;
  A-->B;
  A-->C;
  B-->D;
  C-->D;
```

```
{{< mermaid >}}
sequenceDiagram
    Alice ->> Bob: Hello Bob, how are you?
    Bob-->>John: How about you John?
    Bob--x Alice: I am good thanks!
    Bob-x John: I am good thanks!
    Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

    Bob-->Alice: Checking with John...
    Alice->John: Yes... John, how are you?
{{</ mermaid >}}
```

Produces:

```
sequenceDiagram
    Alice ->> Bob: Hello Bob, how are you?
    Bob-->>John: How about you John?
    Bob--x Alice: I am good thanks!
    Bob-x John: I am good thanks!
    Note right of John: Bob thinks a long
long time, so long
that the text does
not fit on a row.

    Bob-->Alice: Checking with John...
    Alice->John: Yes... John, how are you?
```

You can check more [examples](https://mermaid-js.github.io/mermaid/#/examples) from the official docs.

## Sidebars and Admonitions

Sidebars and admonitions provide ways to add visual importance to text. Use
them sparingly.

### Sidebars

A sidebar offsets text visually, but without the visual prominence of
[admonitions](#admonitions).

> This is a sidebar.
>
> You can have paragraphs and block-level elements within a sidebar.
>
> You can even have code blocks.
>
> ```
> sudo dmesg
> ```

### Admonitions

Admonitions (notes, warnings, etc) use Hugo shortcodes.

> **Note:**
> Notes catch the reader's attention without a sense of urgency.
>
> You can have multiple paragraphs and block-level elements inside an admonition.
>
> You can also add tables to organize and highlight key information.
>
> | Header 1 | Header 2 | Header 3 |
> | --- | --- | --- |
> | Data 1 | Data A | Info X |
> | Data 2 | Data B | Info Y |

> **Caution:**
> The reader should proceed with caution.

> **Warning:**
> Warnings point out something that could cause harm if ignored.

## Includes

To add shortcodes to includes.

> **Note:**
> You need to have a Kubernetes cluster, and the kubectl command-line tool must
> be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
> cluster, you can create one by using
> [minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
> or you can use one of these Kubernetes playgrounds:
>
> * [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
> * [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
> * [KodeKloud](https://kodekloud.com/public-playgrounds)
> * [Play with Kubernetes](https://labs.play-with-k8s.com/)

## Katacoda Embedded Live Environment

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
