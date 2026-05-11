# Skill Evals

Eval framework for testing that AI agents can correctly use skills and return verifiable, structured answers. Test cases are defined as YAML files with enum-constrained JSON schemas — no code needed to add new evals.

## How It Works

Each test case sends a question to an agent running in a container, along with a JSON schema that constrains the response to enum values. The expected answer is a specific value derived from the actual documentation. If the agent reads the docs correctly, it picks the right enum value. If it relies on training data, it may pick a wrong one.

Example test case:

```yaml
- name: ignition_spec_version
  query: "What Ignition specification version does OpenShift 4.22 support for MachineConfig objects?"
  schema:
    type: object
    properties:
      ignition_version:
        type: string
        enum: ["3.1", "3.2", "3.3", "3.4", "3.5"]
        description: "Supported Ignition spec version. Use the 'openshift-docs' skill to find this."
    required: [ignition_version]
  expected:
    ignition_version: "3.5"
```

The agent must pick from the enum. Only `3.5` is correct per the docs.

## Prerequisites

- Container runtime: `podman` or `docker`
- Container image: `lightspeed-agentic-sandbox:latest` (build from [lightspeed-agentic-sandbox](https://github.com/openshift/lightspeed-agentic-sandbox))
- Python 3.12+ with: `pytest`, `pytest-asyncio`, `pytest-xdist`, `httpx`, `jsonschema`, `pyyaml`
- API key for at least one provider (e.g., `ANTHROPIC_API_KEY`)

## Running Evals

```bash
# All tests, default provider (Claude)
bash evals/run.sh

# Parallel execution (4 workers)
PYTEST="python3 -m pytest -n 4" bash evals/run.sh

# Specific skill only
bash evals/run.sh -k "openshift-docs"
bash evals/run.sh -k "kubernetes-docs"

# Specific test case
bash evals/run.sh -k "ignition_spec_version"

# Choose provider and model
EVAL_PROVIDERS=claude ANTHROPIC_MODEL=claude-opus-4-6 bash evals/run.sh

# Multiple providers (comma-separated)
EVAL_PROVIDERS=claude,gemini bash evals/run.sh

# Generate JSON report
bash evals/run.sh --eval-report=evals/report.json

# Verbose output
bash evals/run.sh -v
```

## Adding a New Test Case

Add an entry to `evals/skills/<skill_name>/test_cases.yaml`:

```yaml
- name: my_new_test
  query: "A natural question a user would ask"
  schema:
    type: object
    properties:
      my_field:
        type: string
        enum: ["option_a", "option_b", "option_c"]
        description: "What this field is. Use the '<skill_name>' skill to find this."
    required: [my_field]
  expected:
    my_field: "option_b"
```

Guidelines for good test cases:
- **Use enums only** — no free-form text fields. Every expected value must be constrained.
- **Get expected values from the skill** — run the skill's tools or read its data to find the correct answer. Don't guess or assume from training data.
- **Ask natural questions** — phrase queries like a real user would, not like "read file X and find Y".
- **Add the skill hint in the schema description** — include `"Use the '<skill_name>' skill to find this."` so the agent invokes the skill instead of relying on prior knowledge.
- **Use booleans and integers** where appropriate — `type: boolean` for yes/no questions, `type: integer` with enum for numeric values.

The framework auto-discovers new entries on the next run.

## Adding a New Skill

Two things are needed: eval definitions (what to test) and a workspace symlink (so the agent can access the skill inside the container).

### 1. Create eval definitions

Create a directory under `evals/skills/<skill_name>/` with a system prompt and test cases. See [`evals/skills/openshift-docs/`](skills/openshift-docs/) for a working example.

```
evals/skills/<skill_name>/
├── system_prompt.md      # System prompt for the agent
└── test_cases.yaml       # Test cases with schemas and expected values
```

### 2. Add a workspace symlink

The agent runs inside a container and needs access to the actual skill files (SKILL.md, docs, references, etc.). The workspace uses symlinks that point to the real skill directory in `documentation/`. At container startup, `run.sh` dereferences these symlinks and copies the real files into the container's workspace.

```bash
cd evals/workspace/skills
ln -s ../../../documentation/<skill_name> <skill_name>
```

Commit the symlink — it's tracked by git. The framework handles dereferencing and mounting automatically.

## Directory Structure

```
evals/
├── README.md
├── run.sh                  # Container orchestration (start/stop/health check)
├── pytest.ini              # pytest config
├── conftest.py             # Provider parametrization, fixtures
├── test_docs.py            # Test runner (discovers skills, validates schema + facts)
├── framework/              # Eval infrastructure (from lightspeed-agentic-sandbox)
│   ├── runner.py           # HTTP client with retry/backoff
│   ├── credentials.py      # Provider credential auto-detection
│   └── report.py           # JSON report plugin
├── skills/                 # Per-skill eval definitions
│   ├── openshift-docs/
│   │   ├── system_prompt.md
│   │   └── test_cases.yaml     # 12 test cases
│   └── kubernetes-docs/
│       ├── system_prompt.md
│       └── test_cases.yaml     # 12 test cases
└── workspace/
    └── skills/             # Symlinks to actual skills (mounted into containers)
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `EVAL_PROVIDERS` | `claude` | Comma-separated list of providers to start |
| `ANTHROPIC_MODEL` | `claude-sonnet-4-6` | Claude model override |
| `GEMINI_MODEL` | `gemini-3.1-pro-preview` | Gemini model override |
| `OPENAI_MODEL` | `gpt-5.4` | OpenAI model override |
| `EVAL_BASE_PORT` | `18080` | Starting port for provider containers |
| `EVAL_HEALTH_TIMEOUT` | `60` | Seconds to wait for container health check |
| `IMAGE` | `lightspeed-agentic-sandbox:latest` | Container image to use |
| `PYTEST` | `python3 -m pytest` | pytest command (set to `python3 -m pytest -n 4` for parallel) |
