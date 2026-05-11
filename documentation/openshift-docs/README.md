# OpenShift Documentation Skill

This skill provides pre-generated OpenShift Container Platform documentation in GitHub-Flavored Markdown, converted from the official [openshift/openshift-docs](https://github.com/openshift/openshift-docs) AsciiDoc source.

## Why We Convert

The upstream OpenShift documentation is written in AsciiDoc (`.adoc`), not Markdown. Unlike Kubernetes docs (which are already Markdown with minor Hugo shortcodes), the raw AsciiDoc source is **not usable without conversion**:

- **`include::` directives** — Top-level files are skeletons that `include::` actual content from separate module files under `modules/`. Without resolving these, you see almost no content.
- **Conditional blocks** — `ifndef::openshift-rosa,openshift-dedicated[]` / `endif::` filter content by distro (OCP vs ROSA vs OKD). Without processing, all variants are mixed together.
- **Attribute substitution** — `{product-title}`, `{product-version}`, etc. need to be resolved to actual values like "OpenShift Container Platform".
- **AsciiDoc syntax** — `=` headings, `[id="..."]` anchors, `xref:` cross-references, `toc::[]` macros — it's a fundamentally different format from Markdown.

The published docs at `docs.redhat.com` are JavaScript-rendered and return no content when fetched by HTTP clients. This conversion pipeline produces clean, self-contained GitHub-Flavored Markdown that AI agents can read directly.

## Prerequisites

- Python 3.12+
- [asciidoctor](https://asciidoctor.org/) (Ruby gem): `gem install asciidoctor`
- [pandoc](https://pandoc.org/): `brew install pandoc` (macOS) or `apt install pandoc` (Linux)
- pyyaml: `pip install -r requirements.txt`

## Generating Docs

```bash
make docs VERSION=4.22
```

This will:
1. Shallow-clone `openshift/openshift-docs` (if not already cloned)
2. Check out the `enterprise-4.22` branch
3. Convert all AsciiDoc files to Markdown using `convert.py`
4. Write output to `docs/4.22/` with an `AGENTS.md` index

The generated `docs/` directory should be committed to the repository.

## Cleanup

```bash
# Remove the cloned openshift-docs source (keeps generated docs)
make clean-source

# Remove everything (source clone + generated docs)
make clean
```

## How It Works

The conversion pipeline in `convert.py` runs in two stages:

1. **AsciiDoc to DocBook XML** via `asciidoctor -b docbook5`
2. **DocBook XML to GFM Markdown** via `pandoc -f docbook -t gfm`

Post-processing cleans up pandoc artifacts (empty divs, admonition formatting, excessive blank lines). An `AGENTS.md` index is generated with a compressed pipe-delimited map of all documentation files for efficient topic lookup.
