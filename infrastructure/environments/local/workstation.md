---
created: '2025-09-16T15:05:15.620208'
modified: '2025-09-19T21:15:49.108804'
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
storage: 3.6TB (1.0TB available)
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
  - Visual Studio Code
  - Cursor
  - Claude Desktop
  
productivity:
  - Raycast
  
ai_tools:
  - Claude Desktop
  - Cursor AI
  
music_production:
  - Ableton Live 12 Suite (multiple versions installed)
  - Native Instruments
  - Spitfire Audio
  - Splice
  - Control Surface Studio
```

## Local Services
```yaml
databases:
  - Redis Server (port 6379) - Active
  - PostgreSQL 15 - Installed (data directory: /opt/homebrew/var/postgresql@15)
  
active_services:
  - Redis server (PID 815) - Running
  - Multiple Node.js MCP servers - Running
  - Docker Desktop 28.3.3 - Available
  - Development tools (VS Code, Cursor, Claude Desktop) - Active

service_status:
  redis: Active on localhost:6379
  postgresql: Installed (start with `brew services start postgresql@15`)
  docker: Available
  mcp_servers: Multiple running
```

## Access Information
```yaml
access_method: Direct local access
user: harrysayers
home_directory: /Users/harrysayers
status: Active
```

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

## Active Development Processes
```yaml
running_services:
  - Redis server (PID 815) - Port 6379
  - Multiple Node.js MCP servers
  - VS Code and Cursor processes
  - Various development helper processes

development_ready:
  - All development tools active
  - Redis server running and accessible
  - PostgreSQL installed and ready to start
  - Docker Desktop available
  - Multiple MCP servers running
  - Ready for local development and testing
```

## Deployment Notes
- Local development environment running on macOS workstation
- Redis server actively running and accessible
- PostgreSQL installed but not currently running (can be started with `brew services start postgresql@15`)
- Multiple development tools and MCP servers active
- Ready for local development and testing