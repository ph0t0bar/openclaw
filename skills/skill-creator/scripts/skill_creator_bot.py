#!/usr/bin/env python3
"""
Skill Creator Bot - Agent for the DropAnywhere Agency
Creates, validates, and manages OpenClaw/Codex skills
"""

import os
import sys
import re
from datetime import datetime
from pathlib import Path

SKILL_TEMPLATE = '''---
name: {skill_name}
description: {description}
---

# {skill_name_pretty}

{description}

## When to Use

{when_to_use}

## Prerequisites

{prerequisites}

## Usage

### Quick Start
```bash
{quick_start}
```

### Examples

{examples}

## Tips

{tips}
'''

def validate_skill_name(name: str) -> bool:
    """Validate skill name follows conventions"""
    # Lowercase, hyphens only, no special chars
    pattern = r'^[a-z][a-z0-9-]*$'
    return bool(re.match(pattern, name))

def create_skill(
    name: str,
    description: str,
    when_to_use: str = "",
    prerequisites: str = "None",
    quick_start: str = "",
    examples: str = "",
    tips: str = "",
    scripts: list = None
) -> str:
    """Create a new skill with proper structure"""
    
    if not validate_skill_name(name):
        raise ValueError(f"Invalid skill name: {name}. Use lowercase letters, numbers, hyphens only.")
    
    # Determine workspace path
    workspace = os.getenv("OPENCLAW_WORKSPACE", "/root/.openclaw/workspace")
    skill_path = Path(workspace) / "skills" / name
    
    # Create directories
    skill_path.mkdir(parents=True, exist_ok=True)
    (skill_path / "scripts").mkdir(exist_ok=True)
    
    # Generate SKILL.md
    skill_md = SKILL_TEMPLATE.format(
        skill_name=name,
        skill_name_pretty=name.replace('-', ' ').title(),
        description=description,
        when_to_use=when_to_use or f"Use this skill when you need to {description.lower()}",
        prerequisites=prerequisites,
        quick_start=quick_start or f"# See SKILL.md for usage",
        examples=examples or "# TODO: Add examples",
        tips=tips or "- Test the skill after creating\n- Update as workflows evolve"
    )
    
    # Write SKILL.md
    skill_file = skill_path / "SKILL.md"
    with open(skill_file, 'w') as f:
        f.write(skill_md)
    
    # Write scripts if provided
    if scripts:
        for script_name, script_content in scripts.items():
            script_path = skill_path / "scripts" / script_name
            with open(script_path, 'w') as f:
                f.write(script_content)
            # Make executable
            os.chmod(script_path, 0o755)
    
    return str(skill_path)

def list_skills() -> list:
    """List all available skills"""
    workspace = os.getenv("OPENCLAW_WORKSPACE", "/root/.openclaw/workspace")
    skills_dir = Path(workspace) / "skills"
    
    if not skills_dir.exists():
        return []
    
    skills = []
    for skill_dir in skills_dir.iterdir():
        if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
            skills.append(skill_dir.name)
    
    return sorted(skills)

def get_skill_info(skill_name: str) -> dict:
    """Get information about a skill"""
    workspace = os.getenv("OPENCLAW_WORKSPACE", "/root/.openclaw/workspace")
    skill_path = Path(workspace) / "skills" / skill_name
    
    if not skill_path.exists():
        return None
    
    info = {
        "name": skill_name,
        "path": str(skill_path),
        "has_scripts": (skill_path / "scripts").exists(),
        "has_references": (skill_path / "references").exists() if (skill_path / "references").exists() else False,
        "has_assets": (skill_path / "assets").exists() if (skill_path / "assets").exists() else False,
    }
    
    # Parse SKILL.md for description
    skill_md = skill_path / "SKILL.md"
    if skill_md.exists():
        content = skill_md.read_text()
        # Extract description from frontmatter
        desc_match = re.search(r'^description:\s*(.+)$', content, re.MULTILINE)
        if desc_match:
            info["description"] = desc_match.group(1)
    
    return info

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Skill Creator Bot")
    parser.add_argument("command", choices=["create", "list", "info"])
    parser.add_argument("--name", help="Skill name")
    parser.add_argument("--description", help="Skill description")
    
    args = parser.parse_args()
    
    if args.command == "list":
        skills = list_skills()
        print("Available skills:")
        for skill in skills:
            info = get_skill_info(skill)
            print(f"  - {skill}: {info.get('description', 'No description')}")
    
    elif args.command == "info" and args.name:
        info = get_skill_info(args.name)
        if info:
            print(f"Skill: {info['name']}")
            print(f"Path: {info['path']}")
            print(f"Description: {info.get('description', 'N/A')}")
            print(f"Scripts: {'Yes' if info['has_scripts'] else 'No'}")
        else:
            print(f"Skill not found: {args.name}")
    
    elif args.command == "create":
        if not args.name or not args.description:
            print("Usage: skill-creator create --name my-skill --description 'What it does'")
            sys.exit(1)
        
        try:
            path = create_skill(args.name, args.description)
            print(f"✅ Created skill: {path}")
            print(f"   Edit {path}/SKILL.md to add documentation")
        except ValueError as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
