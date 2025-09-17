---
created: '2025-09-16T15:05:15.619879'
modified: '2025-09-17T16:12:32.909789'
ship_factor: 5
subtype: local
tags: []
title: Env Template
type: general
version: 1
---

# Environment Variables Template

Copy to `.env.local` and fill in values.

```bash
# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=development
DB_USER=dev
DB_PASSWORD=

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=

# APIs
OPENAI_API_KEY=
CLAUDE_API_KEY=
NOTION_API_KEY=
SUPABASE_URL=
SUPABASE_ANON_KEY=

# GitHub
GITHUB_TOKEN=
GITHUB_ORG=harrysayers7

# MCP Servers
MCP_NOTION_TOKEN=
MCP_GITHUB_TOKEN=
MCP_SLACK_TOKEN=

# Local Services
N8N_USER=admin
N8N_PASSWORD=

# Feature Flags
DEBUG=true
ENVIRONMENT=development
```

## Usage

1. Copy this template: `cp env-template.md .env.local`
2. Fill in actual values
3. Never commit `.env.local`
4. Load in your app:
   ```python
   from dotenv import load_dotenv
   load_dotenv('.env.local')
   ```