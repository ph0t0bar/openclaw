#!/usr/bin/env python3
"""Generate images via Poe bots (e.g. @proproductphotos) and return CDN URLs.

Usage:
  python3 poe_image_gen.py "A floating water droplet, minimal, pastel" --bot proproductphotos
  python3 poe_image_gen.py "prompt" --bot BotName --api-key KEY
"""
import asyncio
import os
import sys
import json
import argparse

import fastapi_poe as fp


async def generate_image(prompt: str, bot_name: str = "proproductphotos", api_key: str = None) -> list[str]:
    """Send a prompt to a Poe image bot and extract image URLs from attachments."""
    if not api_key:
        api_key = os.getenv("POE_API_KEY", "")
    if not api_key:
        raise ValueError("POE_API_KEY not set")

    message = fp.ProtocolMessage(role="user", content=prompt)
    
    image_urls = []
    
    async for partial in fp.get_bot_response(
        messages=[message],
        bot_name=bot_name,
        api_key=api_key
    ):
        # Images come as attachment objects
        if hasattr(partial, 'attachment') and partial.attachment:
            att = partial.attachment
            if hasattr(att, 'url') and att.url:
                image_urls.append(att.url)
    
    return image_urls


async def generate_batch(prompts: list[dict], bot_name: str = "proproductphotos", api_key: str = None) -> dict:
    """Generate multiple images. Each prompt dict has 'name' and 'prompt' keys."""
    results = {}
    for item in prompts:
        name = item["name"]
        prompt = item["prompt"]
        print(f"Generating: {name}...", file=sys.stderr)
        urls = await generate_image(prompt, bot_name, api_key)
        results[name] = urls[0] if urls else None
        print(f"  -> {urls[0] if urls else 'FAILED'}", file=sys.stderr)
    return results


def main():
    parser = argparse.ArgumentParser(description="Generate images via Poe bots")
    parser.add_argument("prompt", nargs="?", help="Image generation prompt")
    parser.add_argument("--bot", default="proproductphotos", help="Bot name (default: proproductphotos)")
    parser.add_argument("--api-key", default=None, help="Poe API key (or set POE_API_KEY)")
    parser.add_argument("--batch", default=None, help="JSON file with batch prompts [{name, prompt}, ...]")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()
    
    if args.batch:
        with open(args.batch) as f:
            prompts = json.load(f)
        results = asyncio.run(generate_batch(prompts, args.bot, args.api_key))
        print(json.dumps(results, indent=2))
    elif args.prompt:
        urls = asyncio.run(generate_image(args.prompt, args.bot, args.api_key))
        if args.json:
            print(json.dumps({"urls": urls}, indent=2))
        else:
            for url in urls:
                print(url)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
