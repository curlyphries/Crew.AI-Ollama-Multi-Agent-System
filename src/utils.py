"""Utility helpers for the application."""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def configure_logging(level: int = logging.INFO) -> None:
    """Configure basic logging for the application."""
    logging.basicConfig(level=level)
