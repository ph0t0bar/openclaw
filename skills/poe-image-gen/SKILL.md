---
name: poe-image-gen
description: Generate images via Poe bots (like @proproductphotos) and get CDN-hosted URLs. Use when you need product photos, illustrations, or visual assets generated cheaply through Poe's image generation bots. Images are automatically hosted on Poe CDN.
---

# Poe Image Generation Skill

Generate images via any Poe image bot and get permanent CDN URLs back.

## When to Use

- Need product photos, illustrations, or visual assets for emails/templates
- Want cheap image generation through Poe's ecosystem (@proproductphotos etc.)
- Need CDN-hosted images that work in emails, web pages, docs

## Prerequisites

- `POE_API_KEY` environment variable set
- `fastapi_poe` Python package installed: `pip3 install fastapi_poe --break-system-packages`

## Usage

### Single Image
```bash
python3 ~/.openclaw/workspace/skills/poe-image-gen/scripts/poe_image_gen.py "A minimal water droplet icon, sage green, white background" --bot proproductphotos
```

### Batch Generation
Create a JSON file with prompts:
```json
[
  {"name": "hero", "prompt": "A glowing brain crystal on marble, sage green light"},
  {"name": "balance", "prompt": "Stacked zen stones, pastel colors, white background"}
]
```

```bash
python3 ~/.openclaw/workspace/skills/poe-image-gen/scripts/poe_image_gen.py --batch prompts.json --bot proproductphotos
```

### From Python
```python
import asyncio
from skills.poe_image_gen.scripts.poe_image_gen import generate_image, generate_batch

# Single
urls = asyncio.run(generate_image("A compass on white marble", bot_name="proproductphotos"))

# Batch
results = asyncio.run(generate_batch([
    {"name": "hero", "prompt": "..."},
    {"name": "icon", "prompt": "..."}
], bot_name="proproductphotos"))
```

## Output

Returns Poe CDN URLs like:
```
https://pfst.cf2.poecdn.net/base/image/1f6d01c844a6d3627212a4bcf433c9f58ee1dbe85b57cd10815b5a093ad33329?w=1024&h=768
```

## How It Works

1. Sends prompt to Poe bot via `fastapi_poe.get_bot_response()`
2. Bot generates image (takes ~10-20s per image)
3. Image returned as attachment with permanent CDN URL
4. No upload step needed — images are already hosted on Poe CDN

## Tips

- **@proproductphotos** is cheapest for product-style photography
- Images are 1024x768 JPEG by default
- CDN URLs are permanent, no auth needed to view
- Include "no text" in prompts to avoid watermarks/labels
- Mention specific colors (hex or names) for brand consistency
- Cost: uses Poe points from your balance

## Known Bots

| Bot | Style | Cost |
|-----|-------|------|
| proproductphotos | Product photography, clean studio shots | Low |
| DALL-E-3 | General purpose, creative | Medium |
| StableDiffusion | Artistic, varied styles | Low |
