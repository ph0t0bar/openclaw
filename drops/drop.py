#!/usr/bin/env python3
"""
drop.py — Universal agent drop CLI.

Posts drops to the oPOErator hub API, which handles CDN upload + storage.
Works from anywhere: local machine, OpenClaw, CI, scripts.

Usage:
  python3 drop.py <file.md> [options]
  python3 drop.py --stdin --title "My drop" [options]
  echo "hello" | python3 drop.py --stdin --title "Quick note"

Examples:
  python3 drop.py checkpoint.md --from claude-code --type checkpoint
  python3 drop.py note.md --from openclaw --type context
  python3 drop.py --list
  python3 drop.py --list --from openclaw --since 2026-02-06
"""

import sys
import os
import json
import argparse
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

# Hub API config — override with env vars
HUB_URL = os.getenv("DROP_HUB_URL", "https://hub-production-f423.up.railway.app")
API_KEY = os.getenv("DROP_API_KEY") or os.getenv("INGEST_API_KEY", "")

# Try loading from local .env files if not set
if not API_KEY:
    for env_path in [
        Path("/Users/home/Library/Mobile Documents/com~apple~CloudDocs/Code/deploy_bridge/opoerator-hub/.env"),
        Path(".env"),
        Path(os.path.expanduser("~/.drop-env")),
    ]:
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                if line.startswith("INGEST_API_KEY="):
                    API_KEY = line.split("=", 1)[1].strip().strip("\"'")
                    break
            if API_KEY:
                break


def api_request(method, path, body=None, params=None):
    """Make an authenticated request to the hub API."""
    url = f"{HUB_URL}{path}"
    if params:
        qs = "&".join(f"{k}={v}" for k, v in params.items() if v is not None)
        if qs:
            url += f"?{qs}"

    data = json.dumps(body).encode() if body else None
    req = Request(url, data=data, method=method)
    req.add_header("Content-Type", "application/json")
    req.add_header("X-API-Key", API_KEY)

    try:
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except HTTPError as e:
        error_body = e.read().decode() if e.fp else str(e)
        print(f"API error ({e.code}): {error_body}", file=sys.stderr)
        sys.exit(1)


def extract_title(text):
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return None


def cmd_drop(args):
    """Create a drop."""
    if args.stdin:
        content = sys.stdin.read()
    else:
        path = Path(args.file)
        if not path.exists():
            print(f"File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        content = path.read_text()

    if not args.sender:
        args.sender = "claude-code"
    if not args.drop_type:
        args.drop_type = "context"
    title = args.title or extract_title(content) or (Path(args.file).stem if not args.stdin else "stdin-drop")

    result = api_request("POST", "/api/agent-drops", body={
        "from_agent": args.sender,
        "title": title,
        "content": content,
        "drop_type": args.drop_type,
        "tags": args.tags.split(",") if args.tags else [],
    })

    drop = result.get("drop", {})
    print(f"Dropped: {drop.get('id')}")
    print(f"  from: {drop.get('from')}")
    print(f"  type: {drop.get('type')}")
    if drop.get("cdn_url"):
        print(f"  cdn:  {drop['cdn_url']}")
    else:
        print(f"  cdn:  (upload failed, stored without CDN)")


def cmd_list(args):
    """List drops."""
    params = {}
    if args.sender:
        params["from_agent"] = args.sender
    if args.drop_type:
        params["drop_type"] = args.drop_type
    if args.since:
        params["since"] = args.since
    if args.limit:
        params["limit"] = str(args.limit)

    result = api_request("GET", "/api/agent-drops", params=params)
    drops = result.get("drops", [])

    if not drops:
        print("No drops found.")
        return

    print(f"{len(drops)} drop(s):\n")
    for d in drops:
        cdn = "cdn" if d.get("cdn_url") else "git"
        print(f"  [{d.get('type', '?'):10}] {d.get('id', '?')}")
        print(f"             from={d.get('from')} {cdn} {d.get('timestamp', '')[:19]}")
        if d.get("cdn_url"):
            print(f"             {d['cdn_url']}")
        print()


def cmd_read(args):
    """Read a specific drop."""
    result = api_request("GET", f"/api/agent-drops/{args.drop_id}")
    drop = result.get("drop", {})
    if drop.get("content"):
        print(drop["content"])
    else:
        print(json.dumps(drop, indent=2))


def main():
    parser = argparse.ArgumentParser(
        description="Universal agent drop CLI — posts to oPOErator hub",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    # Default: drop a file
    parser.add_argument("file", nargs="?", help="Markdown file to drop")
    parser.add_argument("--stdin", action="store_true", help="Read content from stdin")
    parser.add_argument("--from", dest="sender", default=None,
                        help="Who's dropping (default: claude-code for new drops)")
    parser.add_argument("--type", dest="drop_type", default=None,
                        help="Drop type: checkpoint, context, handoff, question (default: context for new drops)")
    parser.add_argument("--title", help="Override title (default: first # heading)")
    parser.add_argument("--tags", help="Comma-separated tags")

    # List mode
    parser.add_argument("--list", action="store_true", help="List drops instead of creating")
    parser.add_argument("--since", help="Filter: only drops after this ISO timestamp")
    parser.add_argument("--limit", type=int, default=20, help="Max results (default 20)")

    # Read mode
    parser.add_argument("--read", dest="drop_id", help="Read a specific drop by ID")

    args = parser.parse_args()

    if not API_KEY:
        print("No API key found. Set DROP_API_KEY or INGEST_API_KEY env var,", file=sys.stderr)
        print("or create a .env file with INGEST_API_KEY=...", file=sys.stderr)
        sys.exit(1)

    if args.drop_id:
        cmd_read(args)
    elif args.list:
        cmd_list(args)
    elif args.file or args.stdin:
        cmd_drop(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
