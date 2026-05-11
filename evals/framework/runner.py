"""Eval runner — POSTs to /v1/agent/run."""

from __future__ import annotations

import asyncio
import random
import time
from dataclasses import dataclass, field
from typing import Any

import httpx

MAX_RETRIES = 5
RETRY_BACKOFF_BASE = 2.0


@dataclass
class RunResult:
    provider: str = ""
    success: bool = False
    summary: str = ""
    raw: dict[str, Any] = field(default_factory=dict)
    latency_seconds: float = 0.0
    error: str | None = None


async def run_query(
    server_url: str,
    query: str,
    system_prompt: str = "You are a helpful assistant.",
    output_schema: dict | None = None,
    timeout_ms: int | None = None,
) -> RunResult:
    """POST to /v1/agent/run — the primary eval entry point."""
    result = RunResult()
    start = time.monotonic()

    body: dict[str, Any] = {
        "query": query,
        "systemPrompt": system_prompt,
    }
    if output_schema:
        body["outputSchema"] = output_schema
    if timeout_ms is not None:
        body["timeout_ms"] = timeout_ms

    async with httpx.AsyncClient(timeout=300.0) as client:
        for attempt in range(MAX_RETRIES):
            try:
                resp = await client.post(f"{server_url}/v1/agent/run", json=body)
                if resp.status_code == 429:
                    wait = RETRY_BACKOFF_BASE ** (attempt + 1) * random.uniform(0.5, 1.0)
                    await asyncio.sleep(wait)
                    continue
                resp.raise_for_status()
                data = resp.json()

                result.success = data.get("success", False)
                result.summary = data.get("summary", "")
                result.raw = data
                break
            except Exception as e:
                result.error = str(e)
                break

    result.latency_seconds = time.monotonic() - start
    return result
