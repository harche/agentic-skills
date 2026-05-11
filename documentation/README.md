# Documentation Skills

This directory contains skills that help AI agents search and read Kubernetes and OpenShift Container Platform documentation locally, without requiring network access or API calls at runtime.

## Why Local Documentation?

AI agents need access to up-to-date platform documentation to give accurate answers. The challenge is that upstream docs aren't always in a format agents can easily consume:

- **OpenShift docs** ([openshift/openshift-docs](https://github.com/openshift/openshift-docs)) are written in AsciiDoc with heavy `include::` directives, conditional distro blocks, and attribute substitution. The raw source is unusable without the full AsciiBinder toolchain. The published docs at docs.redhat.com are JavaScript-rendered and return no content when fetched by HTTP clients.

- **Kubernetes docs** ([kubernetes/website](https://github.com/kubernetes/website)) are written in Markdown but authored for Hugo with shortcodes, embedded code references, and YAML frontmatter. The raw source is roughly readable but noisy.

We solve this by converting both doc sets to clean GitHub-Flavored Markdown and shipping them locally with the skills.

## Documentation Index and Progressive Disclosure

Each generated doc set includes an `AGENTS.md` index — a compressed, token-efficient map of all documentation files, inspired by [Vercel's AGENTS.md pattern](https://vercel.com/docs/agents). The index uses a pipe-delimited format:

```
|networking/network_security:{configuring-ipsec-ovn.md,network-policy-apis.md}
|storage/container_storage_interface:{persistent-storage-csi.md,csi-drivers.md}
```

This enables **progressive disclosure**: an agent scans the compact index first (~400 lines covering ~1,700 docs), finds the relevant file, and reads only that file. This avoids loading thousands of documents into the context window and keeps token usage efficient.

The workflow is:
1. `grep -i "topic" docs/4.22/AGENTS.md` — find the right file
2. `cat docs/4.22/networking/network_security/network-policy-apis.md` — read it

## Directory Structure

```
documentation/
├── README.md                 # This file
├── openshift-docs/                # OpenShift Container Platform docs
│   ├── SKILL.md              # Skill definition
│   ├── README.md             # How to generate, prerequisites, why we convert
│   ├── convert.py            # AsciiDoc → DocBook → Markdown pipeline
│   ├── Makefile              # make docs VERSION=4.22
│   └── docs/                 # Pre-generated markdown (committed)
│       └── 4.22/
│           ├── AGENTS.md     # Compressed doc index
│           └── ...           # ~1,700 markdown files
└── kubernetes-docs/               # Kubernetes docs
    ├── SKILL.md              # Skill definition
    ├── README.md             # How to generate, prerequisites, why we convert
    ├── convert.py            # Hugo HTML → Markdown pipeline
    ├── Makefile              # make docs VERSION=1.34
    └── docs/                 # Pre-generated markdown (committed)
        └── 1.34/
            ├── AGENTS.md     # Compressed doc index
            └── ...           # ~1,100 markdown files
```

## Generating Docs

Each skill has its own conversion pipeline. See the individual READMEs for prerequisites and usage:

- **OpenShift**: `cd openshift-docs && make docs VERSION=4.22` — converts AsciiDoc via asciidoctor + pandoc
- **Kubernetes**: `cd kubernetes-docs && make docs VERSION=1.34` — renders Hugo site, then converts HTML via markdownify

Generated docs are committed to the repository so agents can read them without running the conversion pipeline.
