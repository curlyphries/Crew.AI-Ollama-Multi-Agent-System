"""CLI entry point for running a Browserbase review."""

from __future__ import annotations

import argparse
import sys

from .agents.search_agent import SearchAgent
from .integrations.browserbase_client import BrowserbaseClient


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Review a URL using Browserbase")
    parser.add_argument("url", help="URL to review")
    parser.add_argument(
        "--api-key",
        help="Browserbase API key (defaults to BROWSERBASE_API_KEY env var)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    client = BrowserbaseClient(api_key=args.api_key)
    reviewer = SearchAgent(client=client)
    try:
        reviews = reviewer.review_url(args.url)
    except Exception as exc:  # pragma: no cover - entry point errors
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
    for perspective, review in reviews.items():
        print(f"\n[{perspective.upper()}]\n{review}\n")


if __name__ == "__main__":  # pragma: no cover - manual invocation
    main()
