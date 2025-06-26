"""Agent that queries a local Ollama model."""

from __future__ import annotations

from dataclasses import dataclass

from .base_agent import BaseAgent


@dataclass
class OllamaAgent(BaseAgent):
    """Simple agent that returns a canned response."""

    model_name: str = "llama2"

    def handle(self, task: str) -> str:
        # Placeholder for local model interaction
        return f"[{self.model_name}] Response to: {task}"
