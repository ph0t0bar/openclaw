const express = require('express');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');
const util = require('util');

const execAsync = util.promisify(exec);
const app = express();
const PORT = process.env.PORT || 3000;

// Config paths
const CONFIG_PATH = '/root/.openclaw/openclaw.json';
const BACKUP_DIR = '/root/.openclaw/config-backups';

// Simple auth token from env
const AUTH_TOKEN = process.env.CONFIG_UI_TOKEN || 'dev-token-change-in-production';

// Middleware
app.use(express.json());
app.use(express.static(path.join(__dirname)));

// Auth middleware
function requireAuth(req, res, next) {
  const token = req.headers.authorization?.replace('Bearer ', '') || req.query.token;
  if (token !== AUTH_TOKEN) {
    return res.status(401).json({ error: 'Unauthorized' });
  }
  next();
}

// Ensure backup dir exists
if (!fs.existsSync(BACKUP_DIR)) {
  fs.mkdirSync(BACKUP_DIR, { recursive: true });
}

// GET current config
app.get('/api/config', requireAuth, async (req, res) => {
  try {
    const config = JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
    
    // Return only the parts we expose in UI
    const exposed = {
      primary: config.agents?.defaults?.model?.primary || 'poe/kimi-k2.5',
      fallbacks: config.agents?.defaults?.model?.fallbacks || [],
      thinking: config.agents?.defaults?.thinkingDefault === 'on' || config.agents?.defaults?.thinkingDefault === true,
      lowThinking: config.agents?.defaults?.thinkingDefault === 'low',
      providers: Object.keys(config.models?.providers || {}),
      models: {}
    };
    
    // Extract model list from config
    for (const [provider, data] of Object.entries(config.models?.providers || {})) {
      exposed.models[provider] = data.models?.map(m => ({
        id: m.id,
        name: m.name,
        reasoning: m.reasoning,
        contextWindow: m.contextWindow
      })) || [];
    }
    
    res.json(exposed);
  } catch (error) {
    console.error('Error reading config:', error);
    res.status(500).json({ error: 'Failed to read config' });
  }
});

// POST update config
app.post('/api/config', requireAuth, async (req, res) => {
  try {
    const { primary, thinking, lowThinking } = req.body;
    
    // Read current config
    const config = JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
    
    // Create backup
    const backupPath = path.join(BACKUP_DIR, `openclaw-${Date.now()}.json`);
    fs.writeFileSync(backupPath, JSON.stringify(config, null, 2));
    
    // Update config
    if (!config.agents) config.agents = {};
    if (!config.agents.defaults) config.agents.defaults = {};
    if (!config.agents.defaults.model) config.agents.defaults.model = {};
    
    // Set primary model
    if (primary) {
      config.agents.defaults.model.primary = primary;
      
      // Update fallbacks based on provider
      const provider = primary.split('/')[0];
      const fallbacks = [];
      
      if (provider === 'poe') {
        fallbacks.push('openrouter/moonshotai/kimi-k2.5');
        fallbacks.push('anthropic/claude-opus-4-6');
      } else if (provider === 'openrouter') {
        fallbacks.push('poe/kimi-k2.5');
        fallbacks.push('anthropic/claude-opus-4-6');
      } else {
        fallbacks.push('poe/kimi-k2.5');
        fallbacks.push('openrouter/moonshotai/kimi-k2.5');
      }
      
      config.agents.defaults.model.fallbacks = fallbacks;
    }
    
    // Set thinking mode
    if (thinking !== undefined) {
      config.agents.defaults.thinkingDefault = thinking ? 'on' : (lowThinking ? 'low' : 'off');
    } else if (lowThinking !== undefined) {
      config.agents.defaults.thinkingDefault = lowThinking ? 'low' : 'off';
    }
    
    // Update meta
    if (!config.meta) config.meta = {};
    config.meta.lastTouchedAt = new Date().toISOString();
    config.meta.lastTouchedVersion = config.meta.lastTouchedVersion || '2026.3.13';
    
    // Write config
    fs.writeFileSync(CONFIG_PATH, JSON.stringify(config, null, 2));
    
    // Optionally trigger gateway reload (SIGUSR1)
    // This would need the gateway to handle it
    
    res.json({ 
      success: true, 
      message: 'Config updated',
      backup: backupPath,
      changes: { primary, thinking, lowThinking }
    });
    
  } catch (error) {
    console.error('Error updating config:', error);
    res.status(500).json({ error: 'Failed to update config: ' + error.message });
  }
});

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'ok', service: 'openclaw-config-ui' });
});

// Start server
app.listen(PORT, () => {
  console.log(`🦜 OpenClaw Config UI running on port ${PORT}`);
  console.log(`Config path: ${CONFIG_PATH}`);
  console.log(`Auth token: ${AUTH_TOKEN.substring(0, 8)}...`);
});