#!/usr/bin/env python3
"""Download documentation screenshots attached to OPM/ResInsight issues.

Looks for the newest issue comment starting with "### Documentation". Each
image in that comment whose alt text is a path such as
"plot-window/SummaryPlotCommonLegend.png" is saved to assets/images/<path>.
The text below an image is recorded as its caption, and an optional
"Page: <section>/<file>.md" line as the page to update. Images with other alt
text are ignored. See agents/update-from-resinsight.md for the convention.

Without issue numbers, all issues labelled both "Documentation" and
"PendingRelease" are processed. GITHUB_TOKEN is optional, but avoids the
unauthenticated API rate limit:

    PowerShell: $env:GITHUB_TOKEN = gh auth token
    bash:       export GITHUB_TOKEN=$(gh auth token)

pngquant and oxipng are used to compress downloaded PNG files when found on
PATH.

Usage:
    python fetch_issue_images.py [ISSUE ...] [--dry-run] [--manifest FILE]
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import requests

REPO = "OPM/ResInsight"
LABELS = "Documentation,PendingRelease"
API_URL = f"https://api.github.com/repos/{REPO}/issues"
HEADING = "### Documentation"

IMAGES_DIR = Path(__file__).resolve().parent.parent / "assets" / "images"

IMG_TAG = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
IMG_ATTR = re.compile(r'(\w+)\s*=\s*"([^"]*)"')
IMG_MARKDOWN = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)[^)]*\)")
PAGE_LINE = re.compile(r"^Page:\s*(\S+)\s*$", re.IGNORECASE)
TARGET_PATH = re.compile(r"^[A-Za-z0-9_-]+/[A-Za-z0-9_.-]+\.(png|jpg)$")


def get_session(token: str | None) -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
    )
    if token:
        session.headers["Authorization"] = f"Bearer {token}"
    return session


def get_all_pages(session: requests.Session, url: str, params: dict) -> list:
    items = []
    page = 1
    while True:
        response = session.get(url, params={**params, "per_page": 100, "page": page})
        response.raise_for_status()
        batch = response.json()
        if not batch:
            break
        items.extend(batch)
        page += 1
    return items


def find_labelled_issues(session: requests.Session) -> list[int]:
    issues = get_all_pages(session, API_URL, {"labels": LABELS, "state": "all"})
    return [issue["number"] for issue in issues if "pull_request" not in issue]


def find_documentation_comment(session: requests.Session, number: int) -> str | None:
    comments = get_all_pages(session, f"{API_URL}/{number}/comments", {})
    for comment in reversed(comments):
        body = comment.get("body") or ""
        if body.lstrip().startswith(HEADING):
            return body
    return None


def find_image(line: str) -> tuple[str, str] | None:
    """Return (alt, src) of the first image on the line."""
    tag = IMG_TAG.search(line)
    if tag:
        attrs = dict(IMG_ATTR.findall(tag.group(0)))
        if "src" in attrs:
            return attrs.get("alt", ""), attrs["src"]
    markdown = IMG_MARKDOWN.search(line)
    if markdown:
        return markdown.group(1), markdown.group(2)
    return None


def parse_comment(body: str) -> tuple[str | None, list[dict]]:
    """Return the page hint and the images, each with alt, src and caption."""
    page = None
    images = []
    current = None
    for line in body.splitlines()[1:]:
        stripped = line.strip()
        page_match = PAGE_LINE.match(stripped)
        if page_match:
            page = page_match.group(1)
            current = None
            continue
        image = find_image(stripped)
        if image:
            current = {"alt": image[0].strip(), "src": image[1], "caption": []}
            images.append(current)
        elif not stripped:
            # GitHub inserts a blank line after a pasted image, so only a
            # blank line after caption text ends the caption.
            if current is not None and current["caption"]:
                current = None
        elif current is not None:
            current["caption"].append(stripped)

    for image in images:
        image["caption"] = " ".join(image["caption"])
    return page, images


def validate_target(alt: str) -> str | None:
    """Return an error message if alt is not a usable target path."""
    if not TARGET_PATH.match(alt) or ".." in alt:
        return "expected <section>/<Name>.png or .jpg"
    if not (IMAGES_DIR / alt.split("/")[0]).is_dir():
        return f"unknown section folder '{alt.split('/')[0]}'"
    return None


def download(url: str, target: Path) -> None:
    # Plain session: the attachment URL redirects to signed storage that
    # rejects the GitHub API authorization header.
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    content_type = response.headers.get("Content-Type", "")
    if not content_type.startswith("image/"):
        raise ValueError(f"not an image ({content_type})")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(response.content)


def compress(target: Path) -> None:
    if target.suffix != ".png":
        return
    # pngquant exits with 98/99 when it keeps the original, which is fine.
    if shutil.which("pngquant"):
        subprocess.run(
            ["pngquant", "--quality", "80-95", "--skip-if-larger", "--force", "--ext", ".png", str(target)],
            check=False,
        )
    if shutil.which("oxipng"):
        subprocess.run(["oxipng", "-o", "4", "--strip", "safe", "--quiet", str(target)], check=False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("issues", nargs="*", type=int, help="Issue numbers. Default: all labelled issues.")
    parser.add_argument("--dry-run", action="store_true", help="List images without downloading them.")
    parser.add_argument("--manifest", default="issue-images.json", help="Output manifest file.")
    args = parser.parse_args()

    session = get_session(os.environ.get("GITHUB_TOKEN"))
    numbers = args.issues or find_labelled_issues(session)

    manifest = []
    errors = 0
    for number in numbers:
        body = find_documentation_comment(session, number)
        if body is None:
            print(f"#{number}: no '{HEADING}' comment")
            continue

        page, images = parse_comment(body)
        if page and not (IMAGES_DIR.parent.parent / "content" / page).is_file():
            print(f"#{number}: page '{page}' does not exist, treat as new page")
        for image in images:
            alt = image["alt"]
            if "/" not in alt:
                continue

            error = validate_target(alt)
            if error:
                print(f"#{number}: skipped '{alt}': {error}", file=sys.stderr)
                errors += 1
                continue

            target = IMAGES_DIR / alt
            status = "replaced" if target.exists() else "new"
            entry = {
                "issue": number,
                "path": f"assets/images/{alt}",
                "url": f"/images/{alt}",
                "status": status,
                "caption": image["caption"],
                "page": page,
                "source": image["src"],
            }

            if args.dry_run:
                print(f"#{number}: [dry-run] {status} {entry['path']}")
            else:
                try:
                    download(image["src"], target)
                except (requests.RequestException, ValueError) as e:
                    print(f"#{number}: failed '{alt}': {e}", file=sys.stderr)
                    errors += 1
                    continue
                compress(target)
                print(f"#{number}: {status} {entry['path']}")
            manifest.append(entry)

    print(f"\n{len(numbers)} issue(s) checked, {len(manifest)} image(s) found, {errors} error(s).")
    if not args.dry_run:
        Path(args.manifest).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote manifest to {args.manifest}.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
