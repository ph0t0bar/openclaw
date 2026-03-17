# SPEC-Intelligence-Map-Generator

> Auto-generate visual knowledge maps from user drops. Make the invisible visible.

**Status:** Skeleton  
**Priority:** P1 (Pre-launch)  
**Owner:** TBD  
**Created:** 2026-03-17 by SpecBot  

---

## 1. Problem Statement

Users accumulate hundreds of drops but can't see patterns, connections, or the "shape" of their thinking. Mem.ai wins with auto-organization. DropAnywhere needs intelligence that emerges from accumulated data.

### User Pain Points
- "I've dropped 200 things but don't know what I have"
- Can't see connections between drops across time/topics
- No visual representation of their "second brain"
- Manual tagging/organization is friction

---

## 2. Vision

**The Intelligence Map** is an auto-generated, always-available visualization of a user's knowledge graph. It surfaces:
- Topic clusters (what you think about most)
- Concept connections (how ideas link)
- Temporal patterns (how thinking evolves)
- Knowledge gaps (what's missing)

### Core Philosophy
> "The map is not the territory, but it shows you where you've been."

---

## 3. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Map Generation Rate | 100% of users with 20+ drops | Automated |
| User Engagement | 30% view map weekly | Analytics |
| Insight Discovery | 5+ "aha" moments per user/month | Survey/NPS |
| Time to First Map | < 5 minutes after 20th drop | Performance |

---

## 4. Technical Architecture

### 4.1 Data Pipeline
```
Drops → Embedding → Clustering → Graph Construction → Visualization
```

### 4.2 Components

| Component | Purpose | Tech Options |
|-----------|---------|--------------|
| Embedding Engine | Vector representation of drops | OpenAI Ada-002, Gemini Embedding |
| Clustering Engine | Group similar drops | HDBSCAN, K-means |
| Graph Builder | Connect related concepts | NetworkX, Force-directed layout |
| Viz Renderer | Generate visual map | D3.js, Cytoscape.js, Canvas API |
| Update Trigger | Regenerate on new drops | Event-driven, debounced (5min) |

### 4.3 Data Model

```python
class IntelligenceMap:
    user_id: str
    version: int  # Incremental updates
    generated_at: datetime
    
    # Clusters
    clusters: List[TopicCluster]
    
    # Connections
    edges: List[ConceptEdge]
    
    # Metadata
    total_drops: int
    coverage_percent: float  # % of drops clustered
    
class TopicCluster:
    id: str
    label: str  # AI-generated name
    drop_ids: List[str]
    centroid: Vector
    coherence_score: float  # Cluster quality
    created_at: datetime
    
class ConceptEdge:
    source_cluster: str
    target_cluster: str
    strength: float  # 0-1 similarity
    shared_concepts: List[str]
```

---

## 5. User Experience

### 5.1 Trigger Conditions
- **Minimum drops:** 20 (configurable)
- **Auto-generate:** After every 10 new drops
- **Manual refresh:** Always available

### 5.2 Visualization Modes

| Mode | Purpose | View |
|------|---------|------|
| **Constellation** | Default - force-directed graph | Nodes = topics, edges = connections |
| **Timeline** | See evolution over time | X-axis = time, Y-axis = topic depth |
| **Focus** | Deep dive on one cluster | Expanded view with related drops |
| **Compare** | Before/after or topic A vs B | Split view |

### 5.3 Interaction Design
- Click cluster → See representative drops
- Click edge → See connecting drops
- Drag to explore
- Zoom for detail
- Search to locate

### 5.4 Entry Points
- Digest footer: "View your Intelligence Map"
- Vault: Tab alongside Search/Drops
- Weekly email: "Your mind this week" thumbnail
- Onboarding milestone: "You've created enough to map!"

---

## 6. AI Prompts

### 6.1 Cluster Naming
```
Given these drops [samples], generate a concise 2-4 word label 
that captures the common theme. Be specific, not generic.

Examples:
- "Product Launch Planning" (not "Work")
- "Parenting Philosophy" (not "Family")
- "Revenue Optimization" (not "Business")
```

### 6.2 Connection Description
```
These two clusters share these concepts: [concepts].
Describe the relationship in 10 words or less.
```

### 6.3 Insight Generation
```
Analyze this user's intelligence map:
- Top 3 clusters by size
- Strongest cross-cluster connections
- Temporal trends

Generate 3 insights that would surprise and delight the user.
```

---

## 7. Implementation Phases

### Phase 1: MVP (2 weeks)
- [ ] Basic embedding + clustering pipeline
- [ ] Simple D3.js force-directed graph
- [ ] Static map generation on demand
- [ ] Single visualization mode (Constellation)

### Phase 2: Polish (1 week)
- [ ] Auto-regeneration triggers
- [ ] Cluster naming with AI
- [ ] Click-to-explore interactions
- [ ] Entry points in digest + vault

### Phase 3: Intelligence (2 weeks)
- [ ] Timeline view
- [ ] Insight generation
- [ ] Weekly map evolution email
- [ ] Compare/contrast modes

---

## 8. Open Questions

1. **Performance:** How to handle users with 1000+ drops? Incremental updates?
2. **Privacy:** Any concerns with AI analyzing drop content for clustering?
3. **Storage:** Vector storage strategy - Postgres pgvector vs dedicated service?
4. **Caching:** Map generation is expensive - cache strategy?
5. **Mobile:** How to render complex graphs on small screens?

---

## 9. Related Work

- **Mem.ai:** Auto-organizing knowledge (competitive benchmark)
- **Roam Research:** Graph-based note-taking (UX inspiration)
- **Obsidian Graph View:** Local knowledge visualization (interaction patterns)
- **DropAnywhere Digest:** Existing content for clustering

---

## 10. Files to Create

```
hub/services/intelligence_map/
├── __init__.py
├── embedder.py          # Drop → Vector
├── clusterer.py         # Vectors → Clusters
├── graph_builder.py     # Clusters + Edges → Graph
├── generator.py         # Orchestration
└── prompts.py           # AI prompts

frontend/app/vault/intelligence-map/
├── page.tsx             # Main map view
├── components/
│   ├── ConstellationGraph.tsx
│   ├── TimelineView.tsx
│   ├── ClusterCard.tsx
│   └── InsightPanel.tsx
└── hooks/
    └── useIntelligenceMap.ts
```

---

*Next step: Review with Joey, prioritize against pre-launch roadmap, assign owner.*
