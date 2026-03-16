# AGENT-COMPANY-v3.md — The Full DropAnywhere Organization

**The Complete Agent-Native Company**  
**Based on:** 18 months of operational patterns + real company functions  
**Date:** 2026-03-15  
**Status:** Architecture v3.0 — Comprehensive  

---

## Executive Summary

A real company needs more than engineers. This defines a **complete organization** with 10 departments and 40 specialized agents.

**New Departments:**
- **Marketing** — Content, campaigns, social, SEO
- **Communications** — PR, press, partnerships, founder voice  
- **Intelligence** — Drop analysis, content mining, pattern recognition
- **Meta** — Organizational effectiveness, agent performance, system optimization

---

## The 10 Departments

| Dept | Focus | Key Agents |
|------|-------|------------|
| **Executive** | Strategy, orchestration | Claw |
| **Product** | What to build | DocBot, SpecBot, ResearchBot |
| **Engineering** | How to build | Dropper-Code, FrontEndBot, BHABot |
| **Operations** | Infrastructure | RailwayBot, DevOpsBot |
| **Revenue** | Money flow | StripeBot, PoeBot, GumroadBot |
| **Customer Success** | User health | UserHealthBot, SupportBot |
| **Marketing** | Voice, brand | ContentBot, SocialBot, SEOBot |
| **Communications** | Relations, PR | PRBot, FounderVoiceBot |
| **Intelligence** | Analysis, mining | DropMinerBot, ContentPitchBot |
| **Meta** | System optimization | OrgEffectivenessBot, LearningBot |

---

## Organization Chart (Visual)

```mermaid
flowchart TB
    subgraph EXEC["🎯 EXECUTIVE"]
        J["👤 Joey<br/>Human Founder"]
        C["🦜 Claw<br/>Chief of Staff<br/>✅ LIVE"]
    end

    subgraph DEPTS["📊 DEPARTMENTS"]
        subgraph PROD["📋 PRODUCT"]
            P1["DocBot<br/>🟡"]
            P2["SpecBot<br/>🟡"]
            P3["ResearchBot<br/>🟡"]
        end

        subgraph ENG["⚙️ ENGINEERING"]
            E1["Dropper-Code<br/>✅ LIVE"]
            E2["FrontEndBot<br/>🟡"]
            E3["BHABot<br/>🟡"]
            E4["APIBot<br/>🟡"]
            E5["RepoArch<br/>🟡"]
        end

        subgraph OPS["🔧 OPERATIONS"]
            O1["RailwayBot<br/>🟢 Initializing"]
            O2["DevOpsBot<br/>🟡"]
            O3["SecurityBot<br/>🟡"]
        end

        subgraph REV["💰 REVENUE"]
            R1["StripeBot<br/>🟡"]
            R2["PoeBot<br/>🟡"]
            R3["GumroadBot<br/>🟡"]
            R4["PricingBot<br/>🟡"]
        end

        subgraph CS["🤝 CUSTOMER SUCCESS"]
            CS1["UserHealthBot<br/>🟡"]
            CS2["SupportBot<br/>🟡"]
            CS3["OnboardBot<br/>🟡"]
        end

        subgraph MKT["📣 MARKETING"]
            M1["ContentBot<br/>🟡"]
            M2["SocialBot<br/>🟡"]
            M3["SEOBot<br/>🟡"]
            M4["CampaignBot<br/>🟡"]
            M5["VideoBot<br/>🟡"]
        end

        subgraph COMMS["📡 COMMUNICATIONS"]
            COM1["PRBot<br/>🟡"]
            COM2["PartnerBot<br/>🟡"]
            COM3["FounderVoiceBot<br/>🟡"]
            COM4["CommunityBot<br/>🟡"]
        end

        subgraph INTEL["🧠 INTELLIGENCE"]
            I1["⭐ DropMinerBot<br/>🟡"]
            I2["PatternBot<br/>🟡"]
            I3["ContentPitchBot<br/>🟡"]
            I4["InsightBot<br/>🟡"]
            I5["ConversationBot<br/>🟡"]
        end

        subgraph META["⚡ META"]
            ME1["OrgEffectivenessBot<br/>🟡"]
            ME2["EfficiencyBot<br/>🟡"]
            ME3["MetricsBot<br/>🟡"]
            ME4["LearningBot<br/>🟡"]
        end
    end

    %% Reporting lines
    J --> C
    C --> PROD
    C --> ENG
    C --> OPS
    C --> REV
    C --> CS
    C --> MKT
    C --> COMMS
    C --> INTEL
    C --> META

    %% Cross-functional flows
    I1 -.->|"mines for"| P1
    I1 -.->|"mines for"| M1
    I3 -.->|"pitches to"| C
    M1 -.->|"tone check"| COM3
    CS1 -.->|"alerts"| C
    ME1 -.->|"optimizes"| ENG
    ME1 -.->|"optimizes"| MKT

    %% Legend
    subgraph LEGEND["🔑 Legend"]
        L1["✅ LIVE"]
        L2["🟢 Initializing"]
        L3["🟡 Create"]
        L4["⭐ Critical Path"]
    end

    style EXEC fill:#e1f5e1,stroke:#4caf50,stroke-width:2px
    style J fill:#fff3cd,stroke:#ffc107,stroke-width:2px
    style C fill:#d4edda,stroke:#28a745,stroke-width:3px
    style I1 fill:#ffe6cc,stroke:#ff8c00,stroke-width:3px
    style E1 fill:#d4edda,stroke:#28a745,stroke-width:2px
    style INTEL fill:#f0e6ff,stroke:#9b59b6,stroke-width:2px
    style META fill:#fff0f5,stroke:#e91e63,stroke-width:2px
```

---

## Communication Flow Diagram

```mermaid
flowchart LR
    %% Inputs
    subgraph INPUTS["📥 INPUTS"]
        D1["Joey Drops"]
        D2["User Feedback"]
        D3["System Events"]
        D4["Market Signals"]
    end

    %% Central Hub
    C["🦜 Claw<br/>Chief of Staff"]

    %% Processing Departments
    subgraph PROCESS["⚙️ PROCESSING"]
        INTEL["🧠 Intelligence<br/>Analysis & Mining"]
        PROD["📋 Product<br/>What to Build"]
        ENG["⚙️ Engineering<br/>How to Build"]
    end

    %% Outputs
    subgraph OUTPUTS["📤 OUTPUTS"]
        CODE["Shipped Code"]
        CONTENT["Published Content"]
        REV["Revenue"]
        INSIGHT["Strategic Insights"]
    end

    %% Flow lines
    D1 --> INTEL
    D2 --> CS
    D3 --> OPS
    D4 --> INTEL

    INTEL -->|"Feature Ideas"| PROD
    INTEL -->|"Content Pitches"| MKT
    INTEL -->|"Insights"| C

    PROD -->|"Specs"| ENG
    ENG -->|"PRs"| CODE

    CS -->|"Health Alerts"| C
    MKT -->|"Campaigns"| CONTENT
    REV -->|"Metrics"| META

    C -.->|"Orchestrates"| PROCESS
    META -.->|"Optimizes"| PROCESS

    %% Styling
    style C fill:#d4edda,stroke:#28a745,stroke-width:3px
    style INTEL fill:#f0e6ff,stroke:#9b59b6,stroke-width:2px
    style PROCESS fill:#e3f2fd,stroke:#2196f3,stroke-width:2px
```

---

## NEW: Intelligence Department

### DropMinerBot ⭐
**Mission:** Continuously analyze Joey's drops

**Extracts:**
- Feature requests → Product queue
- Content gold → Marketing queue
- Strategic insights → Joey/Claw
- Emotional patterns → Private flags

### ContentPitchBot
**Mission:** Transform drops into content ideas

**Example:**
- **Drop:** "Over-engineering the digest pipeline"
- **Pitch:** "The Day I Deleted 400 Lines" 
- **Format:** LinkedIn thread on vulnerability

---

## NEW: Marketing Department

| Agent | Role |
|-------|------|
| ContentBot | Blog posts, threads |
| SocialBot | LinkedIn, Twitter/X |
| SEOBot | Keywords, rankings |
| VideoBot | Reels, shorts |

---

## NEW: Communications Department

| Agent | Role |
|-------|------|
| PRBot | Press outreach |
| FounderVoiceBot | Ghostwrites as Joey |
| PartnerBot | Integrations |

**FounderVoiceBot:** All public content routes through for tone check.

---

## NEW: Meta Department

| Agent | Role |
|-------|------|
| OrgEffectivenessBot | Analyze agent performance |
| LearningBot | Capture lessons learned |
| MetricsBot | KPI tracking |

---

## Full Roster: 40 Agents

| # | Agent | Dept | Status |
|---|-------|------|--------|
| 1 | Claw | Executive | ✅ LIVE |
| 2 | Dropper-Code | Engineering | ✅ LIVE |
| 3 | RailwayBot | Operations | 🟢 Initializing |
| 4-22 | [Original agents] | Various | 🟡 Create |
| 23 | **ContentBot** | Marketing | 🟡 Create |
| 24 | **SocialBot** | Marketing | 🟡 Create |
| 25 | **SEOBot** | Marketing | 🟡 Create |
| 26 | **CampaignBot** | Marketing | 🟡 Create |
| 27 | **VideoBot** | Marketing | 🟡 Create |
| 28 | **PRBot** | Communications | 🟡 Create |
| 29 | **PartnerBot** | Communications | 🟡 Create |
| 30 | **FounderVoiceBot** | Communications | 🟡 Create |
| 31 | **CommunityBot** | Communications | 🟡 Create |
| 32 | **DropMinerBot** ⭐ | Intelligence | 🟡 Create |
| 33 | **PatternBot** | Intelligence | 🟡 Create |
| 34 | **ContentPitchBot** | Intelligence | 🟡 Create |
| 35 | **InsightBot** | Intelligence | 🟡 Create |
| 36 | **ConversationBot** | Intelligence | 🟡 Create |
| 37 | **OrgEffectivenessBot** | Meta | 🟡 Create |
| 38 | **EfficiencyBot** | Meta | 🟡 Create |
| 39 | **MetricsBot** | Meta | 🟡 Create |
| 40 | **LearningBot** | Meta | 🟡 Create |

---

## Key Workflow: Drop to Published Content

```
Joey drops insight
    ↓
DropMinerBot → flags content-worthy
    ↓
ContentPitchBot generates 3 angles
    ↓
Pitches to Claw/Joey
    ↓
Joey approves
    ↓
ContentBot creates
    ↓
FounderVoiceBot tone-checks
    ↓
SocialBot posts + SEOBot optimizes
```

---

*This is a complete company. Not just engineering — marketing, PR, intelligence, meta-analysis.*

