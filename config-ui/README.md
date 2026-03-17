# OpenClaw Config UI

Mobile-friendly configuration interface for OpenClaw.

## Deploy to Railway

1. **Create new Railway project:**
   ```bash
   railway init
   ```

2. **Set environment variable:**
   ```bash
   railway variables set CONFIG_UI_TOKEN=your-secret-token-here
   ```

3. **Deploy:**
   ```bash
   railway up
   ```

## Usage

Visit: `https://your-service.railway.app/?token=YOUR_TOKEN`

The token will be saved to localStorage for subsequent visits.

## Features

- Quick preset switches (Fast/Balanced/Smart)
- Model selection with provider badges
- Thinking mode toggles
- Auto-backup on every save
- Mobile-optimized UI

## API Endpoints

- `GET /api/config` - Get current config (requires auth)
- `POST /api/config` - Update config (requires auth)
- `GET /health` - Health check

## Files

- `server.js` - Express API server
- `index.html` - Mobile UI (served statically)
- `package.json` - Dependencies