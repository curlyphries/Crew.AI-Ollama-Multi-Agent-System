"""Browserbase integration utilities.

This module provides a client wrapper for interacting with Browserbase.
It checks for the required dependency and exposes a simple API for
retrieving page content using the Browserbase service.
"""

from __future__ import annotations

import os
from dataclasses import dataclass


class BrowserbaseNotInstalledError(ImportError):
    """Raised when the browserbase package is missing."""


@dataclass
class BrowserbaseClient:
    """Client for interacting with Browserbase service."""

    api_key: str | None = None

    def __post_init__(self) -> None:
        if self.api_key is None:
            self.api_key = os.getenv("BROWSERBASE_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Browserbase API key must be provided via argument or BROWSERBASE_API_KEY env var"
            )

        try:
            import browserbase  # type: ignore
        except ImportError as exc:
            raise BrowserbaseNotInstalledError(
                "browserbase package is required. Install it with 'pip install browserbase'"
            ) from exc
        self._browserbase = browserbase

    def fetch_content(self, url: str) -> str:
        """Fetch page content for the given URL using Browserbase.

        Parameters
        ----------
        url: str
            Web address to fetch.

        Returns
        -------
        str
            Raw HTML contents of the page.
        """
        try:
            session = self._browserbase.Session(api_key=self.api_key)  # type: ignore[attr-defined]
            browser = session.new_browser()
            page = browser.new_page()
            page.goto(url)
            content = page.content()
            browser.close()
            session.close()
            return content
        except Exception as exc:  # pragma: no cover - runtime errors
            raise RuntimeError(f"Failed to fetch '{url}' via Browserbase: {exc}") from exc
