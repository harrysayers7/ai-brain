# Local Development Workstation

## System
```yaml
os: [macOS/Windows/Linux]
version: [VERSION]
arch: [arm64/x86_64]
hostname: [LOCAL_HOSTNAME]
```

## Hardware
```yaml
cpu: [CPU_MODEL]
ram: [AMOUNT]GB
storage: [SIZE]
gpu: [IF_APPLICABLE]
```

## Development Stack
```yaml
languages:
  - Python [VERSION]
  - Node.js [VERSION]
  - TypeScript [VERSION]
  
containerization:
  - Docker Desktop [VERSION]
  - Docker Compose [VERSION]
  
editors:
  - VS Code
  - Cursor
  - [OTHER]
  
ai_tools:
  - Claude Desktop
  - GitHub Copilot
  - [OTHER]
```

## Local Services
```yaml
databases:
  - PostgreSQL (Docker)
  - Redis (Docker)
  
services:
  - n8n (local)
  - Supabase (local)
  - [OTHER]
```

## Network
```yaml
vpn: [VPN_TOOL]
ports:
  - 3000: Frontend dev
  - 5000: API dev
  - 5432: PostgreSQL
  - 6379: Redis
  - 8080: Admin panels
  - [OTHER_PORTS]
```

## File Paths
```yaml
projects: ~/Projects/
configs: ~/.config/
ssh_keys: ~/.ssh/
env_files: [PROJECT]/.env.local
```