#!/usr/bin/env python3
"""
Extract strategic insights and patterns from joey-backup goldmine archive.
Analyzes conversation clusters to identify transformation patterns, feature evolution, and strategic thinking.
"""

import os
import sys
import json
import re
import argparse
from datetime import datetime
from typing import Dict, List, Any, Optional
import requests

def extract_transformation_insights(content: str, source_file: str) -> List[Dict[str, Any]]:
    """Extract transformation-related insights from file content."""
    insights = []
    
    # Look for transformation patterns
    transformation_patterns = [
        r"transform(?:ation|ing|ed)?\s+(?:protocol|process|system|engine)",
        r"weekly\s+catch\s+(?:protocol|process|narrative)",
        r"(?:internal|external)\s+(?:reality|state)\s+(?:reflects?|mirror)",
        r"(?:container|structure)\s+creates?\s+freedom",
        r"drop\s+(?:it|everything)\.?\s+forget\s+(?:it|everything)",
        r"wake\s+up\s+(?:lighter|with\s+insights?)",
        r"(?:path|door)\s+(?:of\s+)?(?:least\s+)?resistance"
    ]
    
    for pattern in transformation_patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            # Extract surrounding context (±100 chars)
            start = max(0, match.start() - 100)
            end = min(len(content), match.end() + 100)
            context = content[start:end].strip()
            
            insight = {
                "type": "transformation",
                "pattern": match.group(),
                "context": context,
                "source_file": source_file,
                "relevance_score": 0.8,
                "strategic_value": "HIGH"
            }
            insights.append(insight)
    
    return insights

def extract_feature_insights(content: str, source_file: str) -> List[Dict[str, Any]]:
    """Extract feature-related insights from file content."""
    insights = []
    
    # Look for feature ideation patterns
    feature_patterns = [
        r"(?:feature|functionality|capability)\s+(?:idea|request|need)",
        r"user\s+(?:wants?|needs?|asks?\s+for)",
        r"(?:build|create|implement|add)\s+(?:a|an|the)?\s*(?:feature|function|tool)",
        r"(?:inbox|digest|vault|capture|drop)\s+(?:feature|improvement|enhancement)",
        r"multi[- ]?channel\s+(?:capture|ingestion|input)",
        r"daily\s+digest\s+(?:template|format|experience)",
        r"voice\s+(?:capture|input|recording|notes?)"
    ]
    
    for pattern in feature_patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            start = max(0, match.start() - 150)
            end = min(len(content), match.end() + 150)
            context = content[start:end].strip()
            
            insight = {
                "type": "feature",
                "pattern": match.group(),
                "context": context,
                "source_file": source_file,
                "relevance_score": 0.7,
                "strategic_value": "MEDIUM"
            }
            insights.append(insight)
    
    return insights

def extract_voice_insights(content: str, source_file: str) -> List[Dict[str, Any]]:
    """Extract Joey's voice patterns and authentic expressions."""
    insights = []
    
    # Look for Joey's distinctive voice patterns
    voice_patterns = [
        r"drop\s+it\.?\s+forget\s+it\.?\s+wake\s+up\s+lighter",
        r"the\s+(?:suffering|struggle|pain)\s+was\s+the\s+bug,?\s+not\s+the\s+feature",
        r"your\s+second\s+brain\s+has\s+no\s+inbox",
        r"(?:external|internal)\s+reality\s+(?:is\s+a\s+)?(?:reflection|mirror)",
        r"i\s+(?:finally\s+)?got\s+out\s+of\s+my\s+own\s+way",
        r"the\s+(?:inbox|container)\s+(?:was\s+never\s+)?(?:creates?\s+|was\s+)?(?:the\s+)?(?:problem|freedom)",
        r"felt\s+like\s+cheating",
        r"that\s+(?:makes\s+me|feels?)\s+(?:lighter|heavier)"
    ]
    
    for pattern in voice_patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            start = max(0, match.start() - 200)
            end = min(len(content), match.end() + 200)
            context = content[start:end].strip()
            
            insight = {
                "type": "voice",
                "pattern": match.group(),
                "context": context,
                "source_file": source_file,
                "relevance_score": 0.9,
                "strategic_value": "HIGH",
                "voice_element": "authentic_expression"
            }
            insights.append(insight)
    
    return insights

def extract_strategic_insights(content: str, source_file: str) -> List[Dict[str, Any]]:
    """Extract high-level strategic insights and business thinking."""
    insights = []
    
    # Look for strategic thinking patterns
    strategic_patterns = [
        r"(?:strategy|strategic)\s+(?:direction|insight|decision|pivot)",
        r"(?:business|product)\s+(?:model|vision|architecture|evolution)",
        r"(?:user|customer)\s+(?:journey|experience|retention|acquisition)",
        r"(?:revenue|monetization|growth)\s+(?:model|strategy|opportunity)",
        r"(?:competitive|market)\s+(?:advantage|differentiation|positioning)",
        r"(?:ai[- ]native|transformation|productivity)\s+(?:ecosystem|platform|approach)"
    ]
    
    for pattern in strategic_patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            start = max(0, match.start() - 200)
            end = min(len(content), match.end() + 200)
            context = content[start:end].strip()
            
            insight = {
                "type": "strategy",
                "pattern": match.group(),
                "context": context,
                "source_file": source_file,
                "relevance_score": 0.8,
                "strategic_value": "HIGH"
            }
            insights.append(insight)
    
    return insights

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

def extract_insights_from_file(file_path: str, pattern_types: List[str]) -> List[Dict[str, Any]]:
    """Extract insights from a single file based on specified pattern types."""
    print(f"🔍 Analyzing: {file_path}")
    
    content = get_file_content(file_path)
    if not content:
        print(f"⚠️  Could not fetch content from {file_path}")
        return []
    
    all_insights = []
    
    if "transformation" in pattern_types:
        insights = extract_transformation_insights(content, file_path)
        all_insights.extend(insights)
        print(f"  📊 Found {len(insights)} transformation insights")
    
    if "features" in pattern_types:
        insights = extract_feature_insights(content, file_path)
        all_insights.extend(insights)
        print(f"  📊 Found {len(insights)} feature insights")
        
    if "voice" in pattern_types:
        insights = extract_voice_insights(content, file_path)
        all_insights.extend(insights)
        print(f"  📊 Found {len(insights)} voice insights")
        
    if "strategy" in pattern_types:
        insights = extract_strategic_insights(content, file_path)
        all_insights.extend(insights)
        print(f"  📊 Found {len(insights)} strategic insights")
    
    return all_insights

def main():
    parser = argparse.ArgumentParser(description="Extract insights from goldmine archive")
    parser.add_argument("--pattern", "-p", required=True, 
                      choices=["transformation", "features", "voice", "strategy", "all"],
                      help="Type of pattern to extract")
    parser.add_argument("--source", "-s", help="Source path/file to analyze")
    parser.add_argument("--file", "-f", help="Specific file to analyze")
    parser.add_argument("--export-json", action="store_true", help="Export results as JSON")
    parser.add_argument("--output", "-o", help="Output file")
    parser.add_argument("--min-relevance", type=float, default=0.6, help="Minimum relevance score")
    
    args = parser.parse_args()
    
    # Validate GitHub token
    if not os.getenv('GH_TOKEN'):
        print("❌ Error: GH_TOKEN environment variable not set")
        print("Export your GitHub personal access token:")
        print("export GH_TOKEN='github_pat_....'")
        sys.exit(1)
    
    try:
        # Determine pattern types to extract
        if args.pattern == "all":
            pattern_types = ["transformation", "features", "voice", "strategy"]
        else:
            pattern_types = [args.pattern]
        
        print(f"🎯 Extracting patterns: {', '.join(pattern_types)}")
        
        # Determine files to analyze
        files_to_analyze = []
        
        if args.file:
            if not args.file.startswith("Ingestion/"):
                files_to_analyze = [f"Ingestion/{args.file}"]
            else:
                files_to_analyze = [args.file]
        elif args.source:
            # For now, analyze known strategic files
            strategic_files = [
                "Ingestion/COMMAND_CENTER.md",
                "Ingestion/SYSTEM_ARCHITECTURE.md", 
                "Ingestion/.claude/context/ABOUT_JOEY_HAMER.md",
                "Ingestion/_FROM-JOEY.md"
            ]
            files_to_analyze = strategic_files
        else:
            # Default to key strategic files
            files_to_analyze = [
                "Ingestion/COMMAND_CENTER.md",
                "Ingestion/SYSTEM_ARCHITECTURE.md",
                "Ingestion/.claude/context/ABOUT_JOEY_HAMER.md"
            ]
        
        print(f"📁 Analyzing {len(files_to_analyze)} files...")
        
        all_insights = []
        for file_path in files_to_analyze:
            insights = extract_insights_from_file(file_path, pattern_types)
            all_insights.extend(insights)
        
        # Filter by relevance score
        filtered_insights = [i for i in all_insights if i["relevance_score"] >= args.min_relevance]
        
        # Sort by relevance score (descending)
        filtered_insights.sort(key=lambda x: x["relevance_score"], reverse=True)
        
        print(f"\n📊 EXTRACTION COMPLETE")
        print(f"Total insights found: {len(all_insights)}")
        print(f"High-relevance insights: {len(filtered_insights)}")
        
        # Prepare output
        results = {
            "extraction_summary": {
                "patterns_extracted": pattern_types,
                "files_analyzed": len(files_to_analyze),
                "total_insights": len(all_insights),
                "high_relevance_insights": len(filtered_insights),
                "min_relevance_threshold": args.min_relevance
            },
            "files_analyzed": files_to_analyze,
            "insights": filtered_insights
        }
        
        # Output results
        if args.export_json:
            output = json.dumps(results, indent=2)
        else:
            output = f"""
🎯 INSIGHT EXTRACTION RESULTS
{'='*50}
Patterns: {', '.join(pattern_types)}
Files Analyzed: {len(files_to_analyze)}
High-Relevance Insights: {len(filtered_insights)}

💡 TOP INSIGHTS:
"""
            for i, insight in enumerate(filtered_insights[:10], 1):
                output += f"\n{i}. [{insight['type'].upper()}] {insight['pattern']}\n"
                output += f"   Source: {insight['source_file']}\n"
                output += f"   Score: {insight['relevance_score']:.2f}\n"
                output += f"   Context: {insight['context'][:100]}...\n"
        
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