# Kubernetes Documentation Skill

This skill provides pre-generated Kubernetes documentation in GitHub-Flavored Markdown, converted from the official [kubernetes/website](https://github.com/kubernetes/website) Hugo source.

## Why We Convert

The upstream Kubernetes documentation is already written in Markdown, but it's authored for [Hugo](https://gohugo.io/) (a static site generator) and contains Hugo-specific markup that adds noise when reading raw source:

- **Hugo shortcodes** (~4% of lines) — `{{< glossary_tooltip text="container" >}}`, `{{< note >}}...{{< /note >}}`, `{{< feature-state >}}` badges, etc. While an LLM can mostly read past these, they add friction.
- **`{{% code_sample file="..." %}}` references** (~330 occurrences) — the actual code examples live in separate files under `examples/` and aren't inlined in the source Markdown.
- **`{{< include >}}` directives** (~160 occurrences) — referenced content from other files isn't available without Hugo rendering.
- **YAML frontmatter** — reviewer lists, API metadata, content types, and weights that aren't relevant for reading.

The raw Markdown source *would* be roughly usable without conversion (unlike OpenShift's AsciiDoc, which is completely unusable raw), but converting via Hugo produces cleaner output with all shortcodes resolved, code examples inlined, and glossary terms rendered as plain text.

## Prerequisites

- [Hugo extended](https://gohugo.io/installation/) (v0.133.0+): `brew install hugo` (macOS) or `snap install hugo` (Linux)
- Node.js 20+ and npm (for the Docsy theme)
- Python 3.12+ with markdownify: `pip install -r requirements.txt`

## Generating Docs

```bash
make docs VERSION=1.34
```

This will:
1. Shallow-clone `kubernetes/website` (if not already cloned)
2. Check out the `release-1.34` branch
3. Install npm dependencies and build the Hugo site
4. Convert rendered HTML to Markdown using `convert.py` and `markdownify`
5. Write output to `docs/1.34/` with an `AGENTS.md` index

The generated `docs/` directory should be committed to the repository.

## Cleanup

```bash
# Remove the cloned kubernetes-website source (keeps generated docs)
make clean-source

# Remove everything (source clone + generated docs)
make clean
```

## How It Works

The conversion pipeline runs in two stages:

1. **Hugo build** — renders the full Kubernetes documentation site to HTML, resolving all Hugo shortcodes, glossary tooltips, and templated content
2. **HTML to Markdown** — `convert.py` uses BeautifulSoup to extract the article content (`td-content` div) from each HTML page and `markdownify` to convert it back to clean GitHub-Flavored Markdown

Post-processing cleans up HTML comments, excessive blank lines, and formats admonition blocks as blockquotes. An `AGENTS.md` index is generated with a compressed pipe-delimited map of all documentation files.
