"""Base class for all agents."""

from __future__ import annotations


class BaseAgent:
    """Define the core interface for agents."""

    def handle(self, task: str) -> str:
        raise NotImplementedError
