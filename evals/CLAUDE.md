# Evals

## Quick Reference

```bash
# Run all evals (Claude opus-4-6, 4 parallel workers)
EVAL_PROVIDERS=claude ANTHROPIC_MODEL=claude-opus-4-6 PYTEST="python3 -m pytest -n 4" bash evals/run.sh -k "claude and not deepagents" -v

# Run one skill's evals
bash evals/run.sh -k "openshift-docs"
bash evals/run.sh -k "kubernetes-docs"

# Run a single test case
bash evals/run.sh -k "ignition_spec_version"

# Generate JSON report
bash evals/run.sh --eval-report=evals/report.json
```

## Before Running

- Container image must exist: `podman images lightspeed-agentic-sandbox` — if missing, build from [lightspeed-agentic-sandbox](https://github.com/openshift/lightspeed-agentic-sandbox) with `podman build -t lightspeed-agentic-sandbox:latest .`
- Clean up stale containers before re-running: `podman stop -a; podman rm -fa`

## After Running

- Always clean up: `podman stop -a; podman rm -fa; rm -rf .eval-workspaces`
- Check results with: `grep -E "PASSED|FAILED|passed|failed" <output>`

## Adding Test Cases

Test cases live in `evals/skills/<skill_name>/test_cases.yaml`. Each case needs:
- A natural-language `query`
- A `schema` with enum-constrained fields and a `description` containing `"Use the '<skill_name>' skill to find this."`
- An `expected` block with the correct values from the actual docs

Before adding a test case, read the relevant doc file to get the exact expected value. Use enums, booleans, and integers — never free-form text.

## Debugging Failures

When a test fails, the assertion shows the expected vs actual value. To investigate:
1. Verify the expected value is correct by checking the skill's source data
2. If the expected value is wrong, fix it in `test_cases.yaml`
3. If the agent returned wrong data, check if the query is ambiguous or if the schema description needs a stronger skill hint
