# OpenShift Documentation Reference

Docs path: `docs/`
Versioning: Directories under `docs/` (e.g., `docs/4.22/`).
Source: Converted from [openshift/openshift-docs](https://github.com/openshift/openshift-docs) AsciiDoc via `convert.py`.

## Discovering Available Versions

```bash
# List available versions
ls docs/
```

Use the highest version by default unless the user specifies one.

## Using the Documentation Index

Each version has an `AGENTS.md` file that maps topics to documentation files. Always start here.

```bash
# Read the full index
cat docs/4.22/AGENTS.md
```

## Searching for Topics

```bash
# Search the index for a topic (case-insensitive)
grep -i "networking" docs/4.22/AGENTS.md

grep -i "storage" docs/4.22/AGENTS.md

grep -i "install" docs/4.22/AGENTS.md

# Find all docs mentioning a keyword
grep -rl "NetworkPolicy" docs/4.22/

# Find files by name
find docs/4.22/ -name "*.md" | grep -i network
```

## Reading Documentation Files

### Constructing File Paths

Index entries follow this format:
```
|section/subsection:{file1.md,file2.md}
```

Construct the local path:
```
docs/{VERSION}/{section}/{subsection}/{file.md}
```

### Examples

```bash
# Networking overview
cat docs/4.22/networking/index.md

# Installing on AWS (IPI)
cat docs/4.22/installing/installing_aws/ipi/installing-aws-default.md

# Persistent storage with CSI
cat docs/4.22/storage/container_storage_interface/persistent-storage-csi.md

# RBAC
cat docs/4.22/authentication/using-rbac.md

# Release notes
cat docs/4.22/release_notes/ocp-4-22-release-notes.md
```

## Listing Directory Contents

```bash
# List files in a directory
ls docs/4.22/networking/

# List all directories (topic sections)
ls -d docs/4.22/*/

# List all markdown files in a section
find docs/4.22/networking/ -name "*.md"
```

## Common Documentation Sections

| Section | Description |
|---------|-------------|
| `welcome` | Overview, glossary |
| `release_notes` | Version-specific release information |
| `architecture` | System design and components |
| `installing` | Installation guides (AWS, GCP, Azure, bare metal, vSphere, etc.) |
| `post_installation_configuration` | Post-install cluster setup |
| `updating` | Cluster upgrade processes |
| `networking` | Network configuration, DNS, ingress, routes, network policies |
| `storage` | Persistent storage, CSI, ephemeral storage |
| `security` | Certificates, audit logs, compliance |
| `authentication` | Identity providers, RBAC, service accounts |
| `nodes` | Node management, pods, scheduling, taints/tolerations |
| `machine_management` | Machine sets, autoscaling, machine health checks |
| `observability` | Monitoring, logging, distributed tracing |
| `applications` | Deployments, operators, Helm, quotas |
| `cicd` | Builds, pipelines, GitOps |
| `virt` | OpenShift Virtualization |
| `edge_computing` | Remote worker nodes, single-node OpenShift |
| `windows_containers` | Windows container support |

## Tips

- **Start with AGENTS.md**: It's a compressed index of all doc files — search it first.
- **Start broad, then narrow**: Search the index with a general term, then read the specific file.
- **Large files**: Some doc files are long. Use `grep` to find the relevant section first.
- **Cross-reference**: Complex topics may require reading from multiple sections.
- **Full-text search**: Use `grep -rl "keyword" docs/4.22/` to find all files mentioning a term.
