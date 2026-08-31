#!/usr/bin/env python3
"""Remove the "PendingRelease" label from all issues in OPM/ResInsight.

Requires a GitHub personal access token with `repo` scope, provided via the
GITHUB_TOKEN environment variable. If you have the GitHub CLI (`gh`) installed
and authenticated, you can reuse its token instead of creating a new one:

    PowerShell: $env:GITHUB_TOKEN = gh auth token
    bash:       export GITHUB_TOKEN=$(gh auth token)

Usage:
    python remove_pending_release_label.py [--dry-run]
"""

import argparse
import os
import sys

import requests

REPO = "OPM/ResInsight"
LABEL = "PendingRelease"
API_URL = f"https://api.github.com/repos/{REPO}/issues"


def get_session(token: str) -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
    )
    return session


def find_issues_with_label(session: requests.Session, label: str):
    """Collect all open and closed issues (including PRs) that have the given label.

    Fetches all pages up front instead of yielding lazily, since removing the
    label while paginating shifts the result set and skips entries.
    """
    issues = []
    page = 1
    while True:
        response = session.get(
            API_URL,
            params={
                "labels": label,
                "state": "all",
                "per_page": 100,
                "page": page,
            },
        )
        response.raise_for_status()
        batch = response.json()
        if not batch:
            break
        issues.extend(batch)
        page += 1
    return issues


def remove_label(session: requests.Session, issue_number: int, label: str) -> None:
    url = f"{API_URL}/{issue_number}/labels/{label}"
    response = session.delete(url)
    response.raise_for_status()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List issues that would be modified without removing the label.",
    )
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable is not set.", file=sys.stderr)
        return 1

    session = get_session(token)

    count = 0
    for issue in find_issues_with_label(session, LABEL):
        number = issue["number"]
        title = issue["title"]
        count += 1
        if args.dry_run:
            print(f"[dry-run] Would remove '{LABEL}' from #{number}: {title}")
        else:
            remove_label(session, number, LABEL)
            print(f"Removed '{LABEL}' from #{number}: {title}")

    print(f"\nDone. {count} issue(s) processed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
