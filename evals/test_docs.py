"""Documentation skill evals.

Discovers skill eval definitions from evals/skills/<skill_name>/ directories.
Each test case defines its own schema with specific fields and expected values.
Validation is direct field comparison — no fuzzy matching.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path

import jsonschema
import pytest
import yaml

from .framework.runner import RunResult

EVALS_DIR = Path(__file__).parent / "skills"


def _discover_test_cases() -> list[pytest.param]:
    params = []
    for skill_dir in sorted(EVALS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue

        prompt_path = skill_dir / "system_prompt.md"
        cases_path = skill_dir / "test_cases.yaml"

        if not all(p.exists() for p in (prompt_path, cases_path)):
            continue

        prompt = prompt_path.read_text().strip()
        cases = yaml.safe_load(cases_path.read_text())

        for case in cases:
            params.append(
                pytest.param(
                    skill_dir.name,
                    case["name"],
                    case["query"],
                    case["schema"],
                    case["expected"],
                    prompt,
                    id=f"{skill_dir.name}-{case['name']}",
                )
            )

    return params


@pytest.mark.eval
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "skill_name,case_name,query,output_schema,expected,system_prompt",
    _discover_test_cases(),
)
async def test_doc_skill(
    provider_name: str,
    eval_runner: Callable[..., RunResult],
    skill_name: str,
    case_name: str,
    query: str,
    output_schema: dict,
    expected: dict,
    system_prompt: str,
) -> None:
    """Send a documentation query, validate schema, and compare expected values."""
    result = await eval_runner(
        query=query,
        system_prompt=system_prompt,
        output_schema=output_schema,
    )

    assert result.error is None, (
        f"{provider_name}/{skill_name}/{case_name} errored: {result.error}"
    )

    jsonschema.validate(result.raw, output_schema)

    for field, expected_value in expected.items():
        actual = result.raw.get(field)
        assert actual is not None, (
            f"{case_name}: field '{field}' missing from response. "
            f"Got: {json.dumps(result.raw, indent=2)[:500]}"
        )
        if isinstance(expected_value, list):
            assert sorted(actual) == sorted(expected_value), (
                f"{case_name}: field '{field}' expected {expected_value}, got {actual}"
            )
        else:
            assert actual == expected_value, (
                f"{case_name}: field '{field}' expected {expected_value}, got {actual}"
            )
