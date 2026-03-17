---
name: skill-creator-bot
description: Agent for creating, validating, and managing OpenClaw/Codex skills. Use when you need to create a new skill from scratch, list existing skills, or get information about skill structure. Part of the DropAnywhere Agency.
---

# Skill Creator Bot

An agent for the DropAnywhere Agency that creates and manages OpenClaw/Codex skills.

## When to Use

- Creating a new skill from scratch
- Listing available skills in the workspace
- Getting information about skill structure
- Validating skill names and structure
- Generating skill boilerplate

## Prerequisites

- OpenClaw workspace at `~/.openclaw/workspace`
- Write permissions to `skills/` directory

## Usage

### Create a New Skill
```bash
python3 ~/.openclaw/workspace/skills/skill-creator/scripts/skill_creator_bot.py create \
  --name my-skill \
  --description "What this skill does"
```

### List All Skills
```bash
python3 ~/.openclaw/workspace/skills/skill-creator/scripts/skill_creator_bot.py list
```

### Get Skill Info
```bash
python3 ~/.openclaw/workspace/skills/skill-creator/scripts/skill_creator_bot.py info --name poe-cdn-upload
```

### From Python
```python
from skills.skill_creator.scripts.skill_creator_bot import create_skill, list_skills

# Create a skill
path = create_skill(
    name="email-validator",
    description="Validate email addresses and check deliverability",
    when_to_use="Use when processing user email inputs",
    prerequisites="pip install email-validator",
    quick_start="python3 scripts/validate.py email@example.com",
    examples="# Validate single email\npython3 scripts/validate.py test@example.com",
    tips="- Check MX records for deliverability\n- Handle disposable email domains"
)

# List skills
skills = list_skills()
print(skills)  # ['poe-cdn-upload', 'skill-creator', ...]
```

## Skill Structure

Created skills follow this structure:
```
skills/{skill-name}/
├── SKILL.md              # Documentation and usage
└── scripts/              # Executable scripts
    └── (your scripts)
```

Optional directories:
- `references/` - Documentation loaded on demand
- `assets/` - Files used in output (templates, images)

## Skill Naming Conventions

- Lowercase letters, numbers, hyphens only
- Must start with a letter
- Examples: `poe-cdn-upload`, `email-validator`, `github-pr-manager`

## Tips

- Keep SKILL.md concise — context window is limited
- Include working examples in scripts/
- Test scripts before committing
- Update skills as workflows evolve
- Use references/ for large documentation

## Agency Context

This bot is part of the **DropAnywhere Agency**:
- **Department:** Meta / Engineering
- **Reports to:** Claw (Executive)
- **Collaborates with:** All department agents

Created: 2026-03-17
Version: 1.0
