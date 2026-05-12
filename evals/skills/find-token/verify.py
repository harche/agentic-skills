"""Custom verification for the find-token skill eval.

This module is loaded by the eval framework when a test case uses
`expected: { _fn: <function_name> }` in test_cases.yaml. The framework
calls the named function with (result, eval_workspace, provider_name).

Use this pattern when verification needs runtime data that can't be
expressed as static expected values — for example, tokens generated
by tool execution that are random per run, or values queried from a
live OpenShift cluster.

To add custom verification for a new skill:
  1. Create verify.py in your skill's eval directory (evals/skills/<name>/)
  2. Define functions matching the _fn names in your test_cases.yaml
  3. Each function receives:
     - result: dict — the agent's structured JSON response
     - eval_workspace: Path — host path to the eval output directory
       (mounted as /app/eval-output in the container)
     - provider_name: str — which provider ran this test (e.g., "claude")

The schema used by test_cases.yaml is loaded here to avoid duplication —
test_cases.yaml is the single source of truth for the output schema.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

# Load the schema from test_cases.yaml so it's defined in one place.
_CASES = yaml.safe_load((Path(__file__).parent / "test_cases.yaml").read_text())
SCHEMA: dict[str, Any] = _CASES[0]["schema"]


def verify_tokens(result: dict[str, Any], eval_workspace: Path, provider_name: str) -> None:
    """Verify the agent executed find-token.sh and returned the correct token.

    find-token.sh generates random tokens and writes them to .hidden_token
    in the eval output volume. This function reads that file and asserts
    the DIAG_ token appears in the agent's structured response — proving
    the agent actually ran the script (it can't guess a random token).
    """
    token_files = list(eval_workspace.rglob(".hidden_token"))
    assert token_files, f"{provider_name}: find-token.sh did not run (no .hidden_token)"

    expected_diag = None
    for line in token_files[0].read_text().strip().splitlines():
        line = line.strip()
        if line.startswith("DIAG_"):
            expected_diag = line
            break

    assert expected_diag, f"{provider_name}: .hidden_token missing DIAG_ token"
    assert result["token"] == expected_diag, (
        f"{provider_name}: token expected {expected_diag}, got {result['token']}"
    )
