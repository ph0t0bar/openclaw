#!/usr/bin/env python3
"""
drop.py — Write a drop, upload to Poe CDN, update manifest.

Usage:
  python3 drop.py <file.md> [--from claude-code|openclaw] [--type checkpoint|context|handoff] [--push]

Examples:
  python3 drop.py checkpoint.md --from claude-code --type checkpoint
  python3 drop.py note.md --from openclaw --type context --push
  python3 drop.py handoff.md                  # defaults: claude-code, context
"""

import sys
import os
import json
import asyncio
from pathlib import Path
from datetime import datetime, timezone

# Resolve paths — works from repo root or drops/ dir
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DROPS_DIR = SCRIPT_DIR
MANIFEST = DROPS_DIR / "manifest.json"

# Poe CDN client — try multiple known locations
CODE_ROOT = Path("/Users/home/Library/Mobile Documents/com~apple~CloudDocs/Code")
for candidate in [CODE_ROOT / "tools", REPO_ROOT]:
    if (candidate / "poe_client.py").exists():
        sys.path.insert(0, str(candidate))
        break


def load_manifest():
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text())
    return {"drops": []}


def save_manifest(data):
    MANIFEST.write_text(json.dumps(data, indent=2) + "\n")


def extract_title(md_text):
    """Pull the first # heading as the title."""
    for line in md_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return None


async def upload_to_cdn(file_path):
    """Upload file to Poe CDN, return URL or None."""
    try:
        from poe_client import SovereignPoeClient
        client = SovereignPoeClient()
        result = await client.upload_to_cdn(file_path=str(file_path))
        return result["url"]
    except Exception as e:
        print(f"  CDN upload failed ({e}), continuing with git-only drop")
        return None


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Write a drop, upload to CDN, update manifest")
    parser.add_argument("file", help="Markdown file to drop")
    parser.add_argument("--from", dest="sender", default="claude-code",
                        choices=["claude-code", "openclaw"],
                        help="Who's dropping (default: claude-code)")
    parser.add_argument("--type", dest="drop_type", default="context",
                        choices=["checkpoint", "context", "handoff", "question"],
                        help="Drop type (default: context)")
    parser.add_argument("--push", action="store_true",
                        help="Git add, commit, and push after dropping")
    parser.add_argument("--no-cdn", action="store_true",
                        help="Skip CDN upload (git-only drop)")
    args = parser.parse_args()

    source = Path(args.file).resolve()
    if not source.exists():
        print(f"File not found: {args.file}")
        sys.exit(1)

    content = source.read_text()
    title = extract_title(content) or source.stem

    # Copy to the right from-* directory
    dest_dir = DROPS_DIR / f"from-{args.sender}"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / source.name
    dest.write_text(content)
    print(f"  Dropped: {dest.relative_to(REPO_ROOT)}")

    # Upload to CDN
    cdn_url = None
    if not args.no_cdn:
        cdn_url = asyncio.run(upload_to_cdn(source))
        if cdn_url:
            print(f"  CDN: {cdn_url}")

    # Update manifest
    drop_id = source.stem
    manifest = load_manifest()

    # Replace if same ID exists, otherwise append
    manifest["drops"] = [d for d in manifest["drops"] if d["id"] != drop_id]
    manifest["drops"].append({
        "id": drop_id,
        "from": args.sender,
        "title": title,
        "file": f"from-{args.sender}/{source.name}",
        "cdn_url": cdn_url,
        "type": args.drop_type,
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    })
    save_manifest(manifest)
    print(f"  Manifest: updated ({len(manifest['drops'])} drops)")

    # Git push if requested
    if args.push:
        os.chdir(REPO_ROOT)
        os.system(f'git add drops/')
        os.system(f'git commit -m "drop: {title}"')
        os.system(f'git push origin main')
        print(f"  Pushed to origin/main")

    print(f"\nDrop complete: {drop_id}")
    if cdn_url:
        print(f"CDN URL: {cdn_url}")


if __name__ == "__main__":
    main()
