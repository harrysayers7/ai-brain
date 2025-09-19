---
created: '2025-09-16T15:05:15.620208'
modified: '2025-09-19T21:15:49.188885'
ship_factor: 5
subtype: local
tags: []
title: Workstation
type: general
version: 2
---

# Local Development Workstation

## System
```yaml
os: macOS
version: 14.7.2 (Sonoma)
arch: arm64
hostname: Harrys-MacBook-Pro-2.local
```

## Hardware
```yaml
cpu: Apple M1 Max
ram: 32GB
storage: 3.6TB (1.1TB available)
gpu: Apple M1 Max GPU
```

## Development Stack
```yaml
languages:
  - Python 3.13.7
  - Node.js v24.7.0
  - TypeScript 4.9.5 (via Vercel)
  
containerization:
  - Docker Desktop 28.3.3
  - Docker Compose v2.39.2
  
editors:
  - VS Code
  - Cursor
  - Claude Desktop
  
productivity:
  - Raycast
  
ai_tools:
  - Claude Desktop
  - Cursor AI
  
music_production:
  - Ableton Live 12
  - Native Instruments
  - Spitfire Audio
  - Splice
  - Control Surface Studio
```

## Local Services
```yaml
databases:
  - PostgreSQL (Docker)
  - Redis (Docker)
  

## Network
```yaml
vpn: NordVPN
ports:
  - 3000: Frontend dev
  - 5000: API dev
  - 5432: PostgreSQL
  - 6379: Redis
  - 8080: Admin panels
  - 54322: Supabase local
```

## File Paths
```yaml
projects: ~/Brain/
configs: ~/.config/
ssh_keys: ~/.ssh/
env_files: ~/Brain/ai-brain/.env
mcp_config: ~/.mcp.json
```

## SSH Keys Available
- id_ed25519 (main key)
- github_actions_deploy
- chat_ai_deploy
- authorized_keys configured