"""In-memory store for agent context."""

from __future__ import annotations

from typing import Dict


class Memory:
    """Simple dictionary-backed memory."""

    def __init__(self) -> None:
        self._store: Dict[str, str] = {}

    def get(self, key: str) -> str | None:
        return self._store.get(key)

    def set(self, key: str, value: str) -> None:
        self._store[key] = value
