#!/usr/bin/env python3
"""Upload files to Poe CDN using fastapi_poe"""
import sys
import os

# Try to import fastapi_poe
try:
    import fastapi_poe as fp
except ImportError:
    print("Installing fastapi_poe...")
    os.system("pip3 install fastapi_poe -q")
    import fastapi_poe as fp

def upload_to_cdn(file_path: str, api_key: str = None) -> str:
    """Upload a file to Poe CDN and return the URL"""
    if not api_key:
        api_key = os.getenv("POE_API_KEY", "")
    
    if not api_key:
        raise ValueError("POE_API_KEY not found in environment")
    
    with open(file_path, 'rb') as f:
        file_bytes = f.read()
    
    filename = os.path.basename(file_path)
    
    print(f"Uploading {filename} ({len(file_bytes)} bytes)...")
    attachment = fp.upload_file_sync(
        file=file_bytes,
        file_name=filename,
        api_key=api_key
    )
    
    print(f"✓ Uploaded: {attachment.url}")
    return attachment.url

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 poe_cdn_upload.py <file_path> [<file_path2> ...]")
        sys.exit(1)
    
    results = {}
    for path in sys.argv[1:]:
        if os.path.exists(path):
            try:
                url = upload_to_cdn(path)
                results[path] = url
            except Exception as e:
                print(f"✗ Failed {path}: {e}")
                results[path] = f"ERROR: {e}"
        else:
            print(f"✗ File not found: {path}")
    
    print("\n=== RESULTS ===")
    for path, url in results.items():
        print(f"{os.path.basename(path)}: {url}")
