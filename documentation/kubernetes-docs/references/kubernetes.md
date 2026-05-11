# Kubernetes Documentation Reference

Docs path: `docs/`
Versioning: Directories under `docs/` (e.g., `docs/1.34/`).
Source: Converted from [kubernetes/website](https://github.com/kubernetes/website) Hugo site via `convert.py`.

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
cat docs/1.34/AGENTS.md
```

## Searching for Topics

```bash
# Search the index for a topic (case-insensitive)
grep -i "networking" docs/1.34/AGENTS.md

grep -i "storage" docs/1.34/AGENTS.md

grep -i "scheduling" docs/1.34/AGENTS.md

# Find all docs mentioning a keyword
grep -rl "NetworkPolicy" docs/1.34/

# Find files by name
find docs/1.34/ -name "*.md" | grep -i network
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
# Pods
cat docs/1.34/concepts/workloads/pods.md

# Services
cat docs/1.34/concepts/services-networking/service.md

# Network Policies
cat docs/1.34/concepts/services-networking/network-policies.md

# Persistent Volumes
cat docs/1.34/concepts/storage/persistent-volumes.md

# RBAC
cat docs/1.34/reference/access-authn-authz/rbac.md

# kubectl reference
cat docs/1.34/reference/kubectl.md
```

## Listing Directory Contents

```bash
# List files in a directory
ls docs/1.34/concepts/

# List all directories (topic sections)
ls -d docs/1.34/*/

# List all markdown files in a section
find docs/1.34/concepts/ -name "*.md"
```

## Doc Structure

| Section | Description |
|---------|-------------|
| `concepts` | Core Kubernetes concepts: workloads, networking, storage, security |
| `tasks` | Step-by-step how-tos: configure pods, debug, administer cluster |
| `tutorials` | Guided walkthroughs: basics, stateful/stateless apps |
| `reference` | API reference, kubectl commands, RBAC, config |
| `setup` | Cluster installation and configuration |

### Key Subsections

| Topic | Path |
|-------|------|
| Pods | `concepts/workloads/pods.md` |
| Deployments | `concepts/workloads/controllers.md` |
| Services | `concepts/services-networking/service.md` |
| Ingress | `concepts/services-networking/ingress.md` |
| Network Policies | `concepts/services-networking/network-policies.md` |
| Persistent Volumes | `concepts/storage/persistent-volumes.md` |
| ConfigMaps/Secrets | `concepts/configuration/` |
| RBAC | `reference/access-authn-authz/rbac.md` |
| Scheduling | `concepts/scheduling-eviction/` |
| Security | `concepts/security/` |
| Debugging | `tasks/debug/` |
| kubectl reference | `reference/kubectl/` |

## Tips

- **Start with AGENTS.md**: It's a compressed index of all doc files — search it first.
- **Start broad, then narrow**: Search the index with a general term, then read the specific file.
- **Large files**: Some doc files are long. Use `grep` to find the relevant section first.
- **Cross-reference**: Complex topics may require reading from multiple sections.
- **Full-text search**: Use `grep -rl "keyword" docs/1.34/` to find all files mentioning a term.
