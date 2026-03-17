---
name: poe-cdn-upload
description: Upload files to Poe CDN for use in emails, web pages, and other applications. Use when you need to host images, GIFs, SVGs, or other assets on a fast, reliable CDN. Requires POE_API_KEY environment variable.
---

# Poe CDN Upload Skill

Upload files to Poe's CDN (pfst.cf2.poecdn.net) for reliable hosting.

## When to Use

- Hosting email images/GIFs that need to work across all clients
- Serving static assets for web applications
- Creating shareable links for files
- Bypassing email client SVG restrictions by hosting externally

## Prerequisites

Set your Poe API key:
```bash
export POE_API_KEY="your-poe-api-key"
```

## Usage

### Single File
```bash
python3 ~/.openclaw/workspace/skills/poe-cdn-upload/scripts/poe_cdn_upload.py image.gif
```

### Multiple Files
```bash
python3 ~/.openclaw/workspace/skills/poe-cdn-upload/scripts/poe_cdn_upload.py file1.gif file2.png file3.svg
```

### From Python
```python
from skills.poe_cdn_upload.scripts.poe_cdn_upload import upload_to_cdn

url = upload_to_cdn("my-image.gif", api_key="your-key")
print(url)  # https://pfst.cf2.poecdn.net/base/image/...
```

## Output

Returns a CDN URL like:
```
https://pfst.cf2.poecdn.net/base/image/93148444dcf67e279c1747db14f4ab312b9f937e993947c11b39341a0e0d783b?w=160&h=6
```

## Tips

- CDN URLs are permanent and can be used immediately
- Poe CDN supports images, GIFs, SVGs, PDFs, and other file types
- Files are automatically optimized (width/height params in URL)
- No authentication required to access uploaded files
