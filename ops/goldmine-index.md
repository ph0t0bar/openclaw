# Goldmine Index - joey-backup/Ingestion/

## 0_VAULT Directory Catalog
**Cataloged:** 2026-03-17 03:52 UTC  
**Path:** `joey-backup/Ingestion/0_VAULT`  
**Purpose:** Core historical data archive - THE MOTHERLODE as referenced in TOOLS.md

### Structure Overview
- **Total items:** 4 directories
- **Purpose:** Historical content archive containing 2,422+ files from Joey's digital ecosystem

### Directory Structure

#### 📁 **BHA** 
- **Type:** Directory
- **Purpose:** 52 Notion database exports 
- **Contains:** Personas, System Prompts, Knowledge Base, Users, Messages, etc.
- **Significance:** Complete BrutallyHonest.ai business data export

#### 📁 **conversations**
- **Type:** Directory  
- **Purpose:** 2,070 ChatGPT conversations (Dec 2022 – Jul 2024)
- **Significance:** MASSIVE conversation history - nearly 2 years of AI interactions
- **Time Span:** December 2022 through July 2024

#### 📁 **Documents**
- **Type:** Directory
- **Purpose:** Document storage (contents unknown)
- **Status:** Needs further exploration

#### 📁 **_PROCESSED**
- **Type:** Directory
- **Purpose:** Processed/archived content (contents unknown)
- **Status:** Needs further exploration

### Research Value
This directory represents Joey's complete AI conversation history and business data - perfect for:
- Understanding Joey's evolution of AI thinking (2022-2024)
- Mining historical context for current projects
- Analyzing conversation patterns and preferences
- BHA business intelligence

### Next Steps for Full Catalog
1. ✅ 0_VAULT (completed)
2. 🔄 .claude/ - Brain state, mined patterns, persona architectures
3. 🔄 .agent/ - Eduardo agent workflows 
4. 🔄 Dated drops (20260107-20260312) - Recent drops/chats
5. 🔄 Root files - GOD_MODE_NOTION_FULL.md, SYSTEM_ARCHITECTURE.md, etc.

### Technical Notes
- **Source:** GitHub API via GITHUB_TOKEN
- **Repo:** ph0t0bar/joey-backup  
- **Auth:** Working GITHUB_TOKEN from .env.local
- **Access Method:** `curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/repos/ph0t0bar/joey-backup/contents/...`

*This catalog will be expanded with each research cycle.*