"""Simple task orchestrator placeholder."""

from __future__ import annotations

from typing import List

from .agents.base_agent import BaseAgent


def run_tasks(agents: List[BaseAgent], task: str) -> List[str]:
    """Run a task across all agents and collect their responses."""
    results = []
    for agent in agents:
        try:
            results.append(agent.handle(task))
        except Exception as exc:  # pragma: no cover - runtime safety
            results.append(f"{agent.__class__.__name__} failed: {exc}")
    return results
