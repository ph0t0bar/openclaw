#!/usr/bin/env python3
"""
Search through joey-backup/Ingestion/ archive for conversations, insights, and patterns.
Part of goldmine-miner skill for extracting strategic value from 2,462+ archived files.
"""

import os
import sys
import json
import re
import argparse
from datetime import datetime
from typing import Dict, List, Any, Optional
import requests

def search_github_contents(query: str, path: str = "Ingestion", repo: str = "ph0t0bar/joey-backup") -> List[Dict]:
    """Search GitHub repository contents via API."""
    token = os.getenv('GH_TOKEN')
    if not token:
        raise ValueError("GH_TOKEN environment variable required")
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # GitHub search API for code/content
    search_url = f"https://api.github.com/search/code"
    params = {
        'q': f'{query} repo:{repo} path:{path}',
        'per_page': 100
    }
    
    try:
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        return response.json().get('items', [])
    except requests.exceptions.RequestException as e:
        print(f"GitHub API error: {e}")
        return []

def get_file_content(file_path: str, repo: str = "ph0t0bar/joey-backup") -> str:
    """Get content of a specific file from GitHub repository."""
    token = os.getenv('GH_TOKEN')
    if not token:
        raise ValueError("GH_TOKEN environment variable required")
        
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3.raw'
    }
    
    url = f"https://api.github.com/repos/{repo}/contents/{file_path}"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {file_path}: {e}")
        return ""

def list_directory_contents(path: str = "Ingestion", repo: str = "ph0t0bar/joey-backup") -> List[Dict]:
    """List contents of a directory in the repository."""
    token = os.getenv('GH_TOKEN')
    if not token:
        raise ValueError("GH_TOKEN environment variable required")
        
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error listing {path}: {e}")
        return []

def search_conversations(query: str, timeframe: Optional[str] = None, pattern: Optional[str] = None) -> Dict[str, Any]:
    """Search through conversation archive for specific topics/patterns."""
    
    print(f"🔍 Searching goldmine for: '{query}'")
    if timeframe:
        print(f"📅 Timeframe filter: {timeframe}")
    if pattern:
        print(f"🎯 Pattern filter: {pattern}")
    
    results = {
        "query": query,
        "timeframe": timeframe,
        "pattern": pattern,
        "conversations_found": 0,
        "files_searched": [],
        "key_insights": [],
        "strategic_files": [],
        "search_summary": ""
    }
    
    # Search in conversations directory first
    print("\n📂 Searching 0_VAULT/conversations/...")
    conversation_results = search_github_contents(query, "Ingestion/0_VAULT/conversations")
    
    # Search in BHA Notion exports
    print("📂 Searching 0_VAULT/BHA/...")
    bha_results = search_github_contents(query, "Ingestion/0_VAULT/BHA")
    
    # Search in Claude context files
    print("📂 Searching .claude/context/...")
    claude_results = search_github_contents(query, "Ingestion/.claude/context")
    
    # Search in recent dated folders
    print("📂 Searching recent dated folders...")
    dated_results = search_github_contents(query, "Ingestion/2026")
    
    all_results = conversation_results + bha_results + claude_results + dated_results
    
    print(f"📊 Found {len(all_results)} files matching query")
    
    # Process results
    for item in all_results:
        file_info = {
            "name": item["name"],
            "path": item["path"], 
            "url": item["html_url"],
            "repository": item["repository"]["full_name"]
        }
        
        # Apply timeframe filter if specified
        if timeframe:
            if timeframe not in item["path"]:
                continue
                
        results["files_searched"].append(file_info)
        
        # Extract insights from high-value files
        if any(keyword in item["name"].lower() for keyword in ["command_center", "system_architecture", "about_joey", "protocol"]):
            print(f"🎯 Strategic file found: {item['name']}")
            results["strategic_files"].append(file_info)
            
            # Try to get file content for insight extraction
            content = get_file_content(item["path"])
            if content and len(content) > 100:
                insight = {
                    "file": item["name"],
                    "path": item["path"],
                    "content_preview": content[:200] + "...",
                    "strategic_value": "HIGH",
                    "extract_recommended": True
                }
                results["key_insights"].append(insight)
    
    results["conversations_found"] = len(results["files_searched"])
    results["search_summary"] = f"Found {len(all_results)} files, {len(results['strategic_files'])} strategic files, {len(results['key_insights'])} insights extracted"
    
    return results

def search_by_pattern(pattern: str) -> Dict[str, Any]:
    """Search for specific patterns across the archive."""
    
    pattern_queries = {
        "transformation": "transform transformation protocol weekly catch narrative",
        "productivity": "inbox productivity workflow efficiency system",
        "features": "feature idea product roadmap user need",
        "strategy": "strategy business model revenue growth",
        "voice": "joey voice tone personality authentic",
        "insights": "insight discovery breakthrough realization",
        "protocol": "protocol system framework methodology process"
    }
    
    query = pattern_queries.get(pattern, pattern)
    return search_conversations(query, pattern=pattern)

def main():
    parser = argparse.ArgumentParser(description="Search joey-backup goldmine archive")
    parser.add_argument("--query", "-q", help="Search query")
    parser.add_argument("--topic", "-t", help="Topic to search for") 
    parser.add_argument("--pattern", "-p", help="Search by predefined pattern")
    parser.add_argument("--timeframe", "-tf", help="Timeframe filter (e.g., 2024, 2023-Q4)")
    parser.add_argument("--output", "-o", help="Output file for results")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--list-conversations", action="store_true", help="List all conversation files")
    
    args = parser.parse_args()
    
    # Validate GitHub token
    if not os.getenv('GH_TOKEN'):
        print("❌ Error: GH_TOKEN environment variable not set")
        print("Export your GitHub personal access token:")
        print("export GH_TOKEN='github_pat_....'")
        sys.exit(1)
    
    try:
        if args.list_conversations:
            print("📂 Listing conversation archive structure...")
            contents = list_directory_contents("Ingestion")
            for item in contents:
                if item["type"] == "dir":
                    print(f"📁 {item['name']}/")
                else:
                    print(f"📄 {item['name']}")
            return
            
        # Determine search approach
        if args.pattern:
            results = search_by_pattern(args.pattern)
        elif args.query or args.topic:
            query = args.query or args.topic
            results = search_conversations(query, args.timeframe, args.pattern)
        else:
            print("❌ Error: Specify --query, --topic, --pattern, or --list-conversations")
            parser.print_help()
            sys.exit(1)
        
        # Output results
        if args.json:
            output = json.dumps(results, indent=2)
        else:
            output = f"""
🔍 GOLDMINE SEARCH RESULTS
{'='*50}
Query: {results['query']}
Files Found: {results['conversations_found']}
Strategic Files: {len(results['strategic_files'])}

📊 SUMMARY:
{results['search_summary']}

🎯 STRATEGIC FILES:
"""
            for file in results['strategic_files']:
                output += f"  • {file['name']} ({file['path']})\n"
            
            output += f"\n💡 KEY INSIGHTS ({len(results['key_insights'])}):\n"
            for insight in results['key_insights']:
                output += f"  • {insight['file']}: {insight['content_preview']}\n"
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
            print(f"✅ Results saved to {args.output}")
        else:
            print(output)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()