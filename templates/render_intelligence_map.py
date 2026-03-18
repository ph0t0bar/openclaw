#!/usr/bin/env python3
"""
render_intelligence_map.py

Takes Hub's _generate_intelligence_map_for_user() JSON output
and renders the v3 Intelligence Map email template with real data.

Usage:
    from render_intelligence_map import render_intel_map_email
    html = render_intel_map_email(map_data, user_data)

The map_data comes from: GET /api/intelligence/latest?user_id=XXX
The user_data comes from: the user's profile (name, email, preferences)
"""

import json
from datetime import datetime, timedelta
from typing import Optional


def render_intel_map_email(
    map_data: dict,
    user_name: str = "there",
    week_range: str = None,
    user_preferences: dict = None,
) -> str:
    """
    Render the Intelligence Map v3 email from Hub data.
    
    map_data: output from _generate_intelligence_map_for_user()
        {
            "nodes": [...],      # up to 30 nodes with type, label, description, metadata
            "links": [...],      # up to 40 links with source, target, relationship, weight
            "summary": {
                "mindset": str,
                "emotion": str,
                "domain_balance": {"work": 5, "health": 2, ...},
                "total_drops": int,
                "themes": [str, ...]
            }
        }
    
    user_preferences: optional dict to control which sections show
        {
            "show_projects": True,      # default: auto-detect from nodes
            "show_questions": True,     # default: auto-detect from nodes  
            "show_reminders": True,     # default: auto-detect from nodes
            "show_domains": True,       # default: True
            "show_emotions": True,      # default: True
        }
    """
    if not user_preferences:
        user_preferences = {}

    nodes = map_data.get("nodes", [])
    links = map_data.get("links", [])
    summary = map_data.get("summary", {})

    # --- Extract data from nodes by type ---
    projects = [n for n in nodes if n.get("type") in ("project", "active_project")]
    questions = [n for n in nodes if n.get("type") in ("question", "open_question")]
    actions = [n for n in nodes if n.get("type") in ("action", "task", "reminder")]
    ideas = [n for n in nodes if n.get("type") in ("idea", "key_idea", "insight", "concept")]
    
    # If no explicit types, try to infer from metadata
    if not projects and not questions and not actions and not ideas:
        for n in nodes:
            meta = n.get("metadata", {})
            drop_type = meta.get("drop_type", "") or n.get("type", "")
            if drop_type in ("task", "action", "reminder"):
                actions.append(n)
            elif drop_type in ("question",):
                questions.append(n)
            elif drop_type in ("idea", "reflection", "insight"):
                ideas.append(n)
            elif drop_type in ("project",):
                projects.append(n)
            else:
                ideas.append(n)  # default to ideas

    # --- Auto-detect which sections to show ---
    show_projects = user_preferences.get("show_projects", len(projects) > 0)
    show_questions = user_preferences.get("show_questions", len(questions) > 0)
    show_reminders = user_preferences.get("show_reminders", len(actions) > 0)
    show_domains = user_preferences.get("show_domains", bool(summary.get("domain_balance")))

    # --- Week range ---
    if not week_range:
        today = datetime.now()
        start = today - timedelta(days=today.weekday() + 1)  # last Sunday
        end = start + timedelta(days=6)
        week_range = f"{start.strftime('%B %d')} — {end.strftime('%d, %Y')}"

    # --- Stats ---
    total_drops = summary.get("total_drops", len(nodes))
    total_nodes = len(nodes)
    total_links = len(links)
    total_themes = len(summary.get("themes", []))

    # --- Mindset & Emotion ---
    mindset = summary.get("mindset", "neutral").capitalize()
    emotion_text = summary.get("emotion", "")
    
    # --- Domain balance ---
    domain_balance = summary.get("domain_balance", {})
    total_domain_drops = sum(domain_balance.values()) or 1
    
    DOMAIN_COLORS = {
        "work": ("#A8B5A0", "#8B9D83"),
        "health": ("#C4A484", "#a88c6c"),
        "relationships": ("#D4A5A5", "#c08e8e"),
        "personal": ("#D4A5A5", "#c08e8e"),
        "creativity": ("#C4A484", "#a88c6c"),
        "creative": ("#C4A484", "#a88c6c"),
        "rest": ("#8B8680", "#6e6a65"),
        "other": ("#E8DFD5", "#ccc5ba"),
    }

    STATUS_COLORS = {
        "in progress": "#A8B5A0",
        "active": "#A8B5A0",
        "stalled": "#C4A484",
        "emerging": "rgba(196,164,132,0.3)",
        "high": "#D4A5A5",
        "medium": "#C4A484",
        "low": "#E8DFD5",
        "tomorrow": "#D4A5A5",
        "this week": "#C4A484",
        "someday": "#E8DFD5",
    }

    # --- Build HTML sections ---
    
    # PULSE STATS
    stats_html = f"""
<div style="background:white;border-radius:16px;padding:20px;margin-bottom:16px;box-shadow:0 1px 4px rgba(0,0,0,0.04),0 4px 12px rgba(0,0,0,0.03);">
  <table style="width:100%;border-collapse:collapse;">
    <tr>
      <td style="text-align:center;padding:8px;">
        <p style="margin:0;font-size:32px;color:#2D2A26;font-weight:700;">{total_drops}</p>
        <p style="margin:4px 0 0;font-size:10px;color:#8B8680;letter-spacing:1.5px;font-weight:600;">DROPS</p>
      </td>
      <td style="text-align:center;padding:8px;">
        <p style="margin:0;font-size:32px;color:#2D2A26;font-weight:700;">{total_nodes}</p>
        <p style="margin:4px 0 0;font-size:10px;color:#8B8680;letter-spacing:1.5px;font-weight:600;">NODES</p>
      </td>
      <td style="text-align:center;padding:8px;">
        <p style="margin:0;font-size:32px;color:#2D2A26;font-weight:700;">{total_links}</p>
        <p style="margin:4px 0 0;font-size:10px;color:#8B8680;letter-spacing:1.5px;font-weight:600;">LINKS</p>
      </td>
      <td style="text-align:center;padding:8px;">
        <p style="margin:0;font-size:32px;color:#2D2A26;font-weight:700;">{total_themes}</p>
        <p style="margin:4px 0 0;font-size:10px;color:#8B8680;letter-spacing:1.5px;font-weight:600;">THEMES</p>
      </td>
    </tr>
  </table>
</div>"""

    # MINDSET + EMOTION
    mindset_html = f"""
<table style="width:100%;border-collapse:separate;border-spacing:8px 0;margin-bottom:8px;">
  <tr>
    <td style="width:50%;vertical-align:top;">
      <div style="background:white;border-radius:16px;padding:20px;box-shadow:0 1px 4px rgba(0,0,0,0.04),0 4px 12px rgba(0,0,0,0.03);">
        <p style="margin:0 0 8px;font-size:10px;color:#A8B5A0;letter-spacing:1.5px;font-weight:600;">MINDSET</p>
        <p style="margin:0;font-size:22px;color:#2D2A26;font-weight:700;">{mindset}</p>
      </div>
    </td>
    <td style="width:50%;vertical-align:top;">
      <div style="background:white;border-radius:16px;padding:20px;box-shadow:0 1px 4px rgba(0,0,0,0.04),0 4px 12px rgba(0,0,0,0.03);">
        <p style="margin:0 0 8px;font-size:10px;color:#A8B5A0;letter-spacing:1.5px;font-weight:600;">EMOTION</p>
        <p style="margin:0;font-size:13px;color:#2D2A26;line-height:1.6;">{_escape(emotion_text[:120])}</p>
      </div>
    </td>
  </tr>
</table>"""

    # AI SYNTHESIS (from the first "summary" or "insight" type node, or from emotion field)
    synthesis_text = ""
    synthesis_nodes = [n for n in nodes if n.get("type") in ("summary", "synthesis", "insight")]
    if synthesis_nodes:
        synthesis_text = synthesis_nodes[0].get("description", "")
    if not synthesis_text and emotion_text and len(emotion_text) > 50:
        synthesis_text = emotion_text
    if not synthesis_text:
        # Build from themes
        themes = summary.get("themes", [])
        if themes:
            synthesis_text = f"This week your mind kept returning to: {', '.join(themes[:3])}. The connections between these themes tell a story worth paying attention to."

    synthesis_html = ""
    if synthesis_text:
        synthesis_html = f"""
<div style="background:white;border-radius:16px;padding:28px;margin-bottom:16px;box-shadow:0 1px 4px rgba(0,0,0,0.04),0 4px 12px rgba(0,0,0,0.03);">
  <div style="border-left:3px solid #A8B5A0;padding-left:20px;">
    <p style="margin:0;font-size:15px;color:#2D2A26;line-height:1.75;">{_escape(synthesis_text)}</p>
  </div>
</div>"""

    # PROJECTS (optional)
    projects_html = ""
    if show_projects and projects:
        items = ""
        for p in projects[:5]:
            meta = p.get("metadata", {})
            status = meta.get("status", "active")
            color = STATUS_COLORS.get(status, "#A8B5A0")
            label = _escape(p.get("label", "Untitled"))
            desc = _escape(p.get("description", "")[:200])
            is_text_status = status in ("emerging",)
            text_color = "white" if not is_text_status else "#8B8680"
            items += f"""
  <div style="background:#FAF8F5;border-radius:12px;padding:16px;margin-bottom:10px;">
    <div style="margin-bottom:8px;">
      <span style="font-size:14px;color:#2D2A26;font-weight:600;">{label}</span>
      <span style="float:right;font-size:10px;padding:3px 10px;border-radius:12px;background:{color};color:{text_color};font-weight:600;">{_escape(status)}</span>
    </div>
    <p style="margin:0;font-size:13px;color:#8B8680;line-height:1.6;">{desc}</p>
  </div>"""

        projects_html = f"""
<div style="background:white;border-radius:16px;padding:24px;margin-bottom:16px;box-shadow:0 1px 4px rgba(0,0,0,0.04),0 4px 12px rgba(0,0,0,0.03);">
  <div style="display:flex;align-items:center;margin-bottom:20px;">
    <div style="width:28px;height:28px;border-radius:8px;background:linear-gradient(135deg,#A8B5A0,#8B9D83);text-align:center;line-height:28px;font-size:14px;margin-right:10px;color:white;">&#9670;</div>
    <h2 style="margin:0;font-size:15px;color:#2D2A26;font-weight:700;">Active Projects</h2>
    <span style="margin-left:auto;font-size:11px;color:#8B8680;background:#FAF8F5;padding:3px 10px;border-radius:12px;font-weight:600;">{len(projects)}</span>
  </div>
  {items}
</div>"""

    # OPEN QUESTIONS (optional)
    questions_html = ""
    if show_questions and questions:
        items = ""
        for q in questions[:5]:
            meta = q.get("metadata", {})
            priority = meta.get("priority", "normal")
            color = STATUS_COLORS.get(priority, "#C4A484")
            label = _escape(q.get("label", "Untitled"))
            desc = _escape(q.get("description", "")[:200])
            items += f"""
  <div style="background:#FAF8F5;border-radius:12px;padding:16px;margin-bottom:10px;">
    <div style="margin-bottom:8px;">
      <span style="font-size:14px;color:#2D2A26;font-weight:600;">{label}</span>
      <span style="float:right;font-size:10px;padding:3px 10px;border-radius:12px;background:{color};color:white;font-weight:600;">{_escape(priority)}</span>
    </div>
    <p style="margin:0;font-size:13px;color:#8B8680;line-height:1.6;">{desc}</p>
  </div>"""

        questions_html = f"""
<div style="background:white;border-radius:16px;padding:24px;margin-bottom:16px;box-shadow:0 1px 4px rgba(0,0,0,0.04),0 4px 12px rgba(0,0,0,0.03);">
  <div style="display:flex;align-items:center;margin-bottom:20px;">
    <div style="width:28px;height:28px;border-radius:8px;background:linear-gradient(135deg,#D4A5A5,#c08e8e);text-align:center;line-height:28px;font-size:14px;margin-right:10px;color:white;">?</div>
    <h2 style="margin:0;font-size:15px;color:#2D2A26;font-weight:700;">Open Questions</h2>
    <span style="margin-left:auto;font-size:11px;color:#8B8680;background:#FAF8F5;padding:3px 10px;border-radius:12px;font-weight:600;">{len(questions)}</span>
  </div>
  {items}
</div>"""

    # REMINDERS (optional)
    reminders_html = ""
    if show_reminders and actions:
        rows = ""
        for a in actions[:6]:
            meta = a.get("metadata", {})
            label = _escape(a.get("label", a.get("description", "")[:60]))
            due = meta.get("due_date", "")
            if due:
                urgency = "tomorrow"
            else:
                urgency = "this week"
            color = STATUS_COLORS.get(urgency, "#C4A484")
            rows += f"""
    <tr>
      <td style="padding:12px 0;color:#2D2A26;border-bottom:1px solid #FAF8F5;">{label}</td>
      <td style="padding:12px 0;text-align:right;border-bottom:1px solid #FAF8F5;"><span style="font-size:10px;padding:3px 10px;border-radius:12px;background:{color};color:white;font-weight:600;">{_escape(urgency)}</span></td>
    </tr>"""

        reminders_html = f"""
<div style="background:white;border-radius:16px;padding:24px;margin-bottom:16px;box-shadow:0 1px 4px rgba(0,0,0,0.04),0 4px 12px rgba(0,0,0,0.03);">
  <div style="display:flex;align-items:center;margin-bottom:20px;">
    <div style="width:28px;height:28px;border-radius:8px;background:linear-gradient(135deg,#C4A484,#a88c6c);text-align:center;line-height:28px;font-size:14px;margin-right:10px;color:white;">!</div>
    <h2 style="margin:0;font-size:15px;color:#2D2A26;font-weight:700;">Reminders</h2>
    <span style="margin-left:auto;font-size:11px;color:#8B8680;background:#FAF8F5;padding:3px 10px;border-radius:12px;font-weight:600;">{len(actions)}</span>
  </div>
  <table style="width:100%;border-collapse:collapse;font-size:13px;">
    {rows}
  </table>
</div>"""

    # KEY IDEAS (always shown)
    ideas_html = ""
    if ideas:
        items = ""
        colors = ["#A8B5A0", "#C4A484", "#E8DFD5"]
        for i, idea in enumerate(ideas[:5]):
            color = colors[i % len(colors)]
            label = _escape(idea.get("label", idea.get("description", "")[:80]))
            conf = idea.get("confidence", 0.5)
            strength = "strong" if conf > 0.7 else "emerging" if conf > 0.4 else "speculative"
            items += f"""
  <div style="border-left:3px solid {color};padding:14px 18px;margin-bottom:10px;background:#FAF8F5;border-radius:0 12px 12px 0;">
    <p style="margin:0 0 4px;font-size:14px;color:#2D2A26;font-weight:600;">{label}</p>
    <p style="margin:0;font-size:11px;color:#8B8680;"><span style="color:{color};font-weight:600;">{strength}</span></p>
  </div>"""

        ideas_html = f"""
<div style="background:white;border-radius:16px;padding:24px;margin-bottom:16px;box-shadow:0 1px 4px rgba(0,0,0,0.04),0 4px 12px rgba(0,0,0,0.03);">
  <div style="display:flex;align-items:center;margin-bottom:20px;">
    <div style="width:28px;height:28px;border-radius:8px;background:linear-gradient(135deg,#A8B5A0,#C4A484);text-align:center;line-height:28px;font-size:14px;margin-right:10px;color:white;">&#10024;</div>
    <h2 style="margin:0;font-size:15px;color:#2D2A26;font-weight:700;">Key Ideas</h2>
    <span style="margin-left:auto;font-size:11px;color:#8B8680;background:#FAF8F5;padding:3px 10px;border-radius:12px;font-weight:600;">{len(ideas)}</span>
  </div>
  {items}
</div>"""

    # CONNECTIONS (always shown — the magic)
    connections_html = ""
    if links:
        # Build node lookup
        node_map = {n.get("id"): n for n in nodes}
        items = ""
        for link in links[:5]:
            src = node_map.get(link.get("source"), {})
            tgt = node_map.get(link.get("target"), {})
            src_label = _escape(src.get("label", link.get("source", "?")))
            tgt_label = _escape(tgt.get("label", link.get("target", "?")))
            relationship = _escape(link.get("relationship", "connects to"))
            weight = link.get("weight", 0.5)
            weight_pct = int(weight * 100)
            items += f"""
  <div style="background:#FAF8F5;border-radius:12px;padding:16px 18px;margin-bottom:10px;">
    <p style="margin:0 0 6px;font-size:13px;font-weight:600;"><span style="color:#A8B5A0;">{src_label}</span> <span style="color:#8B8680;font-weight:normal;">&#8594;</span> <span style="color:#A8B5A0;">{tgt_label}</span></p>
    <p style="margin:0;font-size:13px;color:#2D2A26;line-height:1.6;">{_escape(relationship)}</p>
    <p style="margin:8px 0 0;font-size:10px;color:#8B8680;">strength <span style="display:inline-block;width:40px;height:4px;border-radius:2px;background:#E8DFD5;vertical-align:middle;margin:0 4px;"><span style="display:block;width:{weight_pct}%;height:100%;border-radius:2px;background:#A8B5A0;"></span></span> {weight:.2f}</p>
  </div>"""

        connections_html = f"""
<div style="background:white;border-radius:16px;padding:24px;margin-bottom:16px;box-shadow:0 1px 4px rgba(0,0,0,0.04),0 4px 12px rgba(0,0,0,0.03);">
  <p style="margin:0 0 4px;font-size:15px;color:#2D2A26;font-weight:700;">Connections</p>
  <p style="margin:0 0 18px;font-size:12px;color:#8B8680;">Threads your conscious mind might have missed</p>
  {items}
</div>"""

    # DOMAIN BALANCE (optional)
    domains_html = ""
    if show_domains and domain_balance:
        rows = ""
        for domain, count in sorted(domain_balance.items(), key=lambda x: -x[1]):
            pct = int((count / total_domain_drops) * 100)
            colors = DOMAIN_COLORS.get(domain, DOMAIN_COLORS["other"])
            rows += f"""
    <tr>
      <td style="padding:6px 0;color:#2D2A26;font-weight:600;width:100px;">{_escape(domain.capitalize())}</td>
      <td style="padding:6px 0;">
        <div style="background:#FAF8F5;border-radius:6px;height:10px;width:100%;overflow:hidden;">
          <div style="background:linear-gradient(90deg,{colors[0]},{colors[1]});border-radius:6px;height:10px;width:{pct}%;"></div>
        </div>
      </td>
      <td style="padding:6px 0 6px 12px;color:{colors[0]};text-align:right;width:44px;font-weight:700;">{pct}%</td>
    </tr>"""

        domains_html = f"""
<div style="background:white;border-radius:16px;padding:24px;margin-bottom:16px;box-shadow:0 1px 4px rgba(0,0,0,0.04),0 4px 12px rgba(0,0,0,0.03);">
  <p style="margin:0 0 16px;font-size:15px;color:#2D2A26;font-weight:700;">Life Domain Balance</p>
  <table style="width:100%;border-collapse:collapse;font-size:13px;">
    {rows}
  </table>
</div>"""

    # SUGGESTED FOCUS (always shown — the closer)
    themes = summary.get("themes", [])
    focus_text = ""
    if themes:
        focus_text = f"Your drops keep returning to: <strong>{_escape(themes[0])}</strong>. That's not random — that's signal. Lean into it this week."
    else:
        focus_text = "Keep dropping. The more you share, the sharper the map gets. Patterns emerge from volume."

    focus_html = f"""
<div style="background:linear-gradient(135deg,#A8B5A0,#8B9D83);border-radius:16px;padding:28px;margin-bottom:28px;box-shadow:0 1px 4px rgba(0,0,0,0.04),0 8px 24px rgba(168,181,160,0.2);">
  <p style="margin:0 0 12px;font-size:10px;color:rgba(255,255,255,0.7);letter-spacing:2px;font-weight:600;">SUGGESTED FOCUS</p>
  <p style="margin:0;font-size:15px;color:white;line-height:1.75;">{focus_text}</p>
</div>"""

    # --- Assemble full email ---
    hero_img = "https://pfst.cf2.poecdn.net/base/image/b27a9917de793f580f83b2ae680b82c4bae81faa6db949d9af42b6231563c94f?w=1024&h=768"
    logo_img = "https://pfst.cf2.poecdn.net/base/image/c2569ac4f8a476caba1d0f3bf31600e24aeab531c7806755da3f42564969efbb?pmaid=587987696"
    cta_orb = "https://pfst.cf2.poecdn.net/base/image/c40c806b6522bce2a2fc8e2739b69f82eacea261eb38351ec35cd9127651d64e?w=1200&h=1200"

    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#FAF8F5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;-webkit-font-smoothing:antialiased;">
<div style="max-width:600px;margin:0 auto;padding:40px 24px;">

<!-- Preheader -->
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;">{total_drops} drops. {total_themes} themes. {total_links} connections you probably didn't see coming.&#847;&zwnj;&nbsp;</div>

<!-- HERO IMAGE -->
<div style="text-align:center;margin-bottom:0;">
  <img src="{hero_img}" width="280" alt="Your world, distilled" style="display:block;width:280px;max-width:50%;height:auto;border-radius:16px;border:0;margin:0 auto;" />
</div>

<!-- HEADER -->
<div style="text-align:center;margin-bottom:36px;padding:20px 20px 28px;">
  <img src="{logo_img}" width="36" height="36" alt="DropAnywhere" style="display:inline-block;border:0;margin-bottom:8px;" />
  <p style="margin:0 0 4px;font-size:14px;color:#2D2A26;font-weight:600;letter-spacing:0.5px;">DropAnywhere</p>
  <p style="margin:0;font-size:11px;color:#A8B5A0;letter-spacing:3px;text-transform:uppercase;font-weight:600;">Your Weekly</p>
  <h1 style="margin:6px 0 0;font-size:28px;color:#2D2A26;font-weight:700;letter-spacing:-0.5px;">Intelligence Map</h1>
  <p style="margin:8px 0 0;font-size:13px;color:#8B8680;">{_escape(week_range)}</p>
</div>

{stats_html}
{mindset_html}
{synthesis_html}
{projects_html}
{questions_html}
{reminders_html}
{ideas_html}
{connections_html}
{domains_html}
{focus_html}

<!-- CTA -->
<div style="text-align:center;margin:32px 0;">
  <img src="{cta_orb}" width="48" height="48" alt="" style="border:0;display:inline-block;margin-bottom:12px;" />
  <p style="margin:0 0 16px;font-size:14px;color:#8B8680;">Something on your mind right now?</p>
  <a href="mailto:drop@drop-anywhere.com?subject=drop&body=" style="display:inline-block;background:#2D2A26;color:white;padding:14px 40px;border-radius:12px;text-decoration:none;font-size:15px;font-weight:600;letter-spacing:0.3px;">Drop a thought</a>
  <p style="margin:12px 0 0;font-size:12px;color:#8B8680;">Just reply to this email or send to drop@drop-anywhere.com</p>
</div>

<!-- FOOTER -->
<div style="text-align:center;padding-top:28px;border-top:1px solid #E8DFD5;">
  <p style="margin:0;font-size:14px;color:#C4A484;font-style:italic;">Drop it. Forget it. Wake up lighter.</p>
  <p style="margin:10px 0 0;font-size:20px;">&#x1F99C;</p>
  <p style="margin:14px 0 0;font-size:12px;color:#8B8680;">
    <a href="mailto:hello@drop-anywhere.com" style="color:#8B8680;text-decoration:none;">hello@drop-anywhere.com</a>
  </p>
  <p style="margin:10px 0 0;font-size:11px;color:#8B8680;line-height:2;">
    DropAnywhere &middot; Chicago, IL<br>
    <a href="{{{{unsubscribe_url}}}}" style="color:#8B8680;text-decoration:underline;">Unsubscribe</a> &middot;
    <a href="mailto:drop@drop-anywhere.com?subject=weekly" style="color:#8B8680;text-decoration:underline;">Switch to weekly</a> &middot;
    <a href="mailto:drop@drop-anywhere.com?subject=daily" style="color:#8B8680;text-decoration:underline;">Switch to daily</a> &middot;
    <a href="https://drop-anywhere.com/privacy" style="color:#8B8680;text-decoration:underline;">Privacy Policy</a>
  </p>
</div>

</div>
</body>
</html>"""

    return html


def _escape(text: str) -> str:
    """HTML escape."""
    if not text:
        return ""
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


# --- CLI: render from live Hub data ---
if __name__ == "__main__":
    import os
    import urllib.request

    hub_url = os.getenv("HUB_URL", "https://hub-production-f423.up.railway.app")
    api_key = os.getenv("HUB_API_KEY", os.getenv("INGEST_API_KEY", ""))
    user_id = os.getenv("USER_ID", "b419d8ad5d23513f")  # Joey default

    # Fetch latest intelligence map
    req = urllib.request.Request(
        f"{hub_url}/api/intelligence/latest?user_id={user_id}",
        headers={"X-API-Key": api_key},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            map_data = data.get("map", data)
    except Exception as e:
        print(f"Error fetching intel map: {e}")
        print("Using empty map data for template preview")
        map_data = {"nodes": [], "links": [], "summary": {"total_drops": 0, "themes": []}}

    html = render_intel_map_email(map_data, user_name="Joey")
    
    # Write to file
    out_path = os.path.join(os.path.dirname(__file__), "intelligence-map-rendered.html")
    with open(out_path, "w") as f:
        f.write(html)
    print(f"Rendered to {out_path}")
