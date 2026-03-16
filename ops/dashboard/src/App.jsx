import React, { useState, useEffect, useRef } from 'react'

const GATEWAY_URL = window.location.hostname === 'localhost' 
  ? 'https://openclaw-gateway-production-54a0.up.railway.app'
  : window.location.origin

const DEPARTMENTS = [
  { name: 'Executive', icon: '🎯', color: '#22c55e', agents: [
    { name: 'Claw', model: 'Opus', cadence: 'always', role: 'Co-CEO' },
    { name: 'Chief of Staff', model: 'Opus', cadence: '20m', role: 'Gap Finder' },
  ]},
  { name: 'Product', icon: '📋', color: '#3b82f6', agents: [
    { name: 'DocBot', model: 'Kimi', cadence: '20m', role: 'Tech Writer' },
    { name: 'SpecBot', model: 'Kimi', cadence: '30m', role: 'Requirements' },
  ]},
  { name: 'Engineering', icon: '⚙️', color: '#8b5cf6', agents: [
    { name: 'DC Manager', model: 'Kimi', cadence: '30m', role: 'DevOps Lead' },
    { name: 'FrontEndBot', model: 'Kimi', cadence: '30m', role: 'DA Frontend' },
    { name: 'BHABot', model: 'Kimi', cadence: '30m', role: 'BHA Stack' },
    { name: 'RailwayBot', model: 'Kimi', cadence: '20m', role: 'Infra' },
  ]},
  { name: 'Operations', icon: '🔒', color: '#f59e0b', agents: [
    { name: 'Kimi Patrol', model: 'Kimi', cadence: '5m', role: 'Fast Ops' },
    { name: 'Sentry', model: 'Sonnet', cadence: '15m', role: 'Security' },
  ]},
  { name: 'Revenue', icon: '💰', color: '#10b981', agents: [
    { name: 'StripeBot', model: 'Kimi', cadence: '30m', role: 'Payments' },
    { name: 'PoeBot', model: 'Kimi', cadence: '30m', role: 'Bot Growth' },
  ]},
  { name: 'Customer Success', icon: '🤝', color: '#ec4899', agents: [
    { name: 'UserHealthBot', model: 'Kimi', cadence: '20m', role: 'User Health' },
    { name: 'OnboardBot', model: 'Kimi', cadence: '30m', role: 'Onboarding' },
  ]},
  { name: 'Marketing', icon: '📣', color: '#f97316', agents: [
    { name: 'ContentBot', model: 'Sonnet', cadence: '20m', role: 'Creator' },
    { name: 'SocialBot', model: 'Kimi', cadence: '30m', role: 'Social' },
    { name: 'SEOBot', model: 'Kimi', cadence: '30m', role: 'Search' },
  ]},
  { name: 'Communications', icon: '📡', color: '#06b6d4', agents: [
    { name: 'FounderVoice', model: 'Sonnet', cadence: '30m', role: 'Voice Guard' },
  ]},
  { name: 'Intelligence', icon: '🧠', color: '#a855f7', agents: [
    { name: 'Researcher', model: 'Sonnet', cadence: '10m', role: 'Intel Engine' },
    { name: 'Wire', model: 'Kimi', cadence: '15m', role: 'News Feed' },
    { name: 'ContentPitch', model: 'Kimi', cadence: '30m', role: 'Pitches' },
    { name: 'PatternBot', model: 'Kimi', cadence: '30m', role: 'Patterns' },
  ]},
  { name: 'Meta', icon: '⚡', color: '#ef4444', agents: [
    { name: 'Opus Strategy', model: 'Opus', cadence: '15m', role: 'Quality Gate' },
    { name: 'Meta', model: 'Sonnet', cadence: '20m', role: 'Grader' },
    { name: 'Governance', model: 'Sonnet', cadence: '30m', role: 'Constitution' },
    { name: 'Archivist', model: 'Kimi', cadence: '20m', role: 'Backup' },
    { name: 'LearningBot', model: 'Kimi', cadence: '30m', role: 'Lessons' },
  ]},
]

const PIPELINE = ['Drop/Idea','Wire/Research','ContentPitch','Spec','Task','Dropper-Code','PR Review','Ship','Docs','Backup']

const modelColor = m => m === 'Opus' ? '#f59e0b' : m === 'Sonnet' ? '#3b82f6' : '#22c55e'

function StatusDot({ status = 'pending' }) {
  const colors = { green: '#22c55e', yellow: '#eab308', red: '#ef4444', pending: '#444' }
  return <div style={{ width: 7, height: 7, borderRadius: '50%', background: colors[status] || '#444', boxShadow: status === 'green' ? '0 0 6px #22c55e44' : status === 'red' ? '0 0 6px #ef444444' : 'none', flexShrink: 0 }} />
}

function DeptCard({ dept }) {
  const [expanded, setExpanded] = useState(true)
  return (
    <div style={{ background: '#12121a', border: '1px solid #1e1e2e', borderRadius: 10, padding: 12, borderLeft: `3px solid ${dept.color}` }}>
      <div onClick={() => setExpanded(!expanded)} style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', marginBottom: expanded ? 8 : 0 }}>
        <span style={{ fontSize: 14 }}>{dept.icon}</span>
        <span style={{ fontSize: 12, fontWeight: 600, color: '#ccc', flex: 1 }}>{dept.name}</span>
        <span style={{ fontSize: 9, color: '#555' }}>{dept.agents.length}</span>
        <span style={{ fontSize: 10, color: '#444' }}>{expanded ? '▼' : '▶'}</span>
      </div>
      {expanded && dept.agents.map((a, i) => (
        <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 6, padding: '4px 6px', borderRadius: 5, fontSize: 10, marginBottom: 2 }}>
          <StatusDot status={a.status || 'pending'} />
          <span style={{ color: '#aaa', flex: 1 }}>{a.name}</span>
          <span style={{ color: '#666', fontSize: 8 }}>{a.role}</span>
          <span style={{ color: modelColor(a.model), fontSize: 8, fontWeight: 600 }}>{a.model}</span>
          <span style={{ color: '#444', fontSize: 8, fontFamily: 'monospace' }}>{a.cadence}</span>
        </div>
      ))}
    </div>
  )
}

function Chat() {
  const [open, setOpen] = useState(false)
  const [msgs, setMsgs] = useState([{ from: 'claw', text: 'Hey Joey. Dashboard is live. Ask me anything about the org.' }])
  const [input, setInput] = useState('')
  const bottom = useRef()
  
  useEffect(() => { bottom.current?.scrollIntoView({ behavior: 'smooth' }) }, [msgs])
  
  const send = () => {
    if (!input.trim()) return
    setMsgs(p => [...p, { from: 'joey', text: input }])
    setInput('')
    // TODO: Wire to OpenClaw webhook/API
    setTimeout(() => {
      setMsgs(p => [...p, { from: 'claw', text: '🦜 (connect this to the gateway webhook to get live responses from me!)' }])
    }, 1000)
  }
  
  if (!open) return (
    <div onClick={() => setOpen(true)} style={{ position: 'fixed', bottom: 20, right: 20, width: 48, height: 48, borderRadius: '50%', background: '#22c55e', display: 'flex', alignItems: 'center', justifyContent: 'center', cursor: 'pointer', boxShadow: '0 4px 20px #22c55e44', fontSize: 22 }}>
      🦜
    </div>
  )
  
  return (
    <div style={{ position: 'fixed', bottom: 20, right: 20, width: 340, height: 420, background: '#12121a', border: '1px solid #2a2a3e', borderRadius: 12, display: 'flex', flexDirection: 'column', boxShadow: '0 8px 40px #00000088' }}>
      <div style={{ padding: '10px 14px', borderBottom: '1px solid #1e1e2e', display: 'flex', alignItems: 'center', gap: 8 }}>
        <span>🦜</span>
        <span style={{ fontSize: 12, fontWeight: 600, color: '#ccc', flex: 1 }}>Chat with Claw</span>
        <span onClick={() => setOpen(false)} style={{ cursor: 'pointer', color: '#555', fontSize: 16 }}>×</span>
      </div>
      <div style={{ flex: 1, overflow: 'auto', padding: 10 }}>
        {msgs.map((m, i) => (
          <div key={i} style={{ marginBottom: 8, textAlign: m.from === 'joey' ? 'right' : 'left' }}>
            <div style={{ display: 'inline-block', maxWidth: '80%', padding: '6px 10px', borderRadius: 8, fontSize: 11, background: m.from === 'joey' ? '#22c55e22' : '#1e1e2e', color: m.from === 'joey' ? '#22c55e' : '#aaa' }}>
              {m.text}
            </div>
          </div>
        ))}
        <div ref={bottom} />
      </div>
      <div style={{ padding: 8, borderTop: '1px solid #1e1e2e', display: 'flex', gap: 6 }}>
        <input value={input} onChange={e => setInput(e.target.value)} onKeyDown={e => e.key === 'Enter' && send()} placeholder="Message Claw..." style={{ flex: 1, background: '#1a1a2a', border: '1px solid #2a2a3e', borderRadius: 6, padding: '6px 10px', color: '#ccc', fontSize: 11, outline: 'none' }} />
        <button onClick={send} style={{ background: '#22c55e', border: 'none', borderRadius: 6, padding: '6px 12px', color: '#000', fontSize: 11, fontWeight: 600, cursor: 'pointer' }}>→</button>
      </div>
    </div>
  )
}

export default function App() {
  const [now, setNow] = useState(new Date())
  useEffect(() => { const t = setInterval(() => setNow(new Date()), 30000); return () => clearInterval(t) }, [])
  
  const totalAgents = DEPARTMENTS.reduce((s, d) => s + d.agents.length, 0)
  
  return (
    <div style={{ fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro', system-ui, sans-serif", background: '#0a0a0f', color: '#e0e0e0', minHeight: '100vh', padding: 20 }}>
      <h1 style={{ fontSize: 18, color: '#fff', marginBottom: 2 }}>🦜 DropAnywhere Agent Company</h1>
      <p style={{ fontSize: 10, color: '#555', marginBottom: 16 }}>Live Dashboard — {now.toISOString().slice(0,16)} UTC</p>
      
      {/* Stats */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(100px, 1fr))', gap: 8, marginBottom: 16 }}>
        {[
          { value: totalAgents, label: 'AGENTS', color: '#22c55e' },
          { value: 10, label: 'DEPTS', color: '#fff' },
          { value: '~1.5K', label: 'CYCLES/DAY', color: '#22c55e' },
          { value: '3', label: 'MODELS', color: '#fff' },
          { value: '8d', label: 'TO LAUNCH', color: '#eab308' },
        ].map((s, i) => (
          <div key={i} style={{ background: '#12121a', border: '1px solid #1e1e2e', borderRadius: 8, padding: 8, textAlign: 'center' }}>
            <div style={{ fontSize: 20, fontWeight: 700, color: s.color }}>{s.value}</div>
            <div style={{ fontSize: 8, color: '#555' }}>{s.label}</div>
          </div>
        ))}
      </div>
      
      {/* Model Legend */}
      <div style={{ display: 'flex', gap: 12, marginBottom: 12, fontSize: 9 }}>
        <span><span style={{ color: '#f59e0b' }}>●</span> Opus (strategy)</span>
        <span><span style={{ color: '#3b82f6' }}>●</span> Sonnet (build)</span>
        <span><span style={{ color: '#22c55e' }}>●</span> Kimi (fast ops)</span>
      </div>
      
      {/* Org Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: 8, marginBottom: 16 }}>
        {DEPARTMENTS.map((d, i) => <DeptCard key={i} dept={d} />)}
      </div>
      
      {/* Pipeline */}
      <div style={{ fontSize: 12, fontWeight: 600, color: '#666', marginBottom: 6 }}>🔄 Value Pipeline</div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 3, flexWrap: 'wrap', background: '#12121a', border: '1px solid #1e1e2e', borderRadius: 8, padding: 10, marginBottom: 16 }}>
        {PIPELINE.map((p, i) => (
          <React.Fragment key={i}>
            <span style={{ color: '#22c55e', background: '#0f1f0f', padding: '3px 7px', borderRadius: 4, fontSize: 9, border: '1px solid #22c55e22' }}>{p}</span>
            {i < PIPELINE.length - 1 && <span style={{ color: '#333', fontSize: 9 }}>→</span>}
          </React.Fragment>
        ))}
      </div>
      
      {/* DCS Protocol */}
      <div style={{ fontSize: 12, fontWeight: 600, color: '#666', marginBottom: 6 }}>⏱ DCS Timeout Tiers</div>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 8, marginBottom: 16 }}>
        {[
          { model: 'Kimi K2.5', timeout: '120s', count: 18, color: '#22c55e', desc: 'Fast ops, monitoring' },
          { model: 'Sonnet', timeout: '240s', count: 5, color: '#3b82f6', desc: 'Research, build, content' },
          { model: 'Opus', timeout: '300-420s', count: 2, color: '#f59e0b', desc: 'Strategy, gap finding' },
        ].map((t, i) => (
          <div key={i} style={{ background: '#12121a', border: `1px solid ${t.color}22`, borderRadius: 8, padding: 10 }}>
            <div style={{ fontSize: 14, fontWeight: 700, color: t.color }}>{t.model}</div>
            <div style={{ fontSize: 10, color: '#888', marginTop: 2 }}>{t.count} agents · {t.timeout}</div>
            <div style={{ fontSize: 9, color: '#555', marginTop: 2 }}>{t.desc}</div>
          </div>
        ))}
      </div>
      
      {/* Permissions */}
      <div style={{ fontSize: 12, fontWeight: 600, color: '#666', marginBottom: 6 }}>🛡 Data Classification</div>
      <div style={{ display: 'flex', gap: 6, marginBottom: 16, fontSize: 9, flexWrap: 'wrap' }}>
        <span style={{ background: '#2a0a0a', color: '#ef4444', padding: '3px 8px', borderRadius: 4 }}>🔴 RESTRICTED — Claw only</span>
        <span style={{ background: '#2a1a0a', color: '#f59e0b', padding: '3px 8px', borderRadius: 4 }}>🟠 CONFIDENTIAL — Role-specific</span>
        <span style={{ background: '#1a1a0a', color: '#eab308', padding: '3px 8px', borderRadius: 4 }}>🟡 INTERNAL — All agents</span>
        <span style={{ background: '#0a1a0a', color: '#22c55e', padding: '3px 8px', borderRadius: 4 }}>🟢 PUBLIC — Publishable</span>
      </div>
      
      {/* Chat */}
      <Chat />
    </div>
  )
}
