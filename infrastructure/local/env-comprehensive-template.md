---
created: '2025-09-16T19:19:40.867385'
modified: '2025-09-16T19:20:17.742022'
ship_factor: 5
subtype: local
tags: []
title: Env Comprehensive Template
type: general
version: 1
---

# Comprehensive Environment Variables Template

Copy this to `.env` and fill in your actual values.

```bash
# =============================================================================
# AI-BRAIN ENVIRONMENT VARIABLES TEMPLATE
# =============================================================================
# Copy this file to .env and fill in your actual values
# Never commit .env files to version control
# =============================================================================

# =============================================================================
# CORE AI SERVICES
# =============================================================================

# OpenAI
OPENAI_API_KEY=sk-your-openai-api-key-here
OPENAI_ORG_ID=org-your-org-id-here
OPENAI_MODEL=gpt-4o

# Anthropic Claude
ANTHROPIC_API_KEY=sk-ant-your-claude-api-key-here
CLAUDE_MODEL=claude-3-5-sonnet-20241022

# Google AI
GOOGLE_AI_API_KEY=your-google-ai-api-key-here
GOOGLE_AI_MODEL=gemini-pro

# Azure OpenAI (if using)
AZURE_OPENAI_API_KEY=your-azure-openai-key-here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name

# Perplexity AI
PERPLEXITY_API_KEY=pplx-your-perplexity-api-key-here

# =============================================================================
# DATABASE SERVICES
# =============================================================================

# PostgreSQL
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ai_brain
DB_USER=dev
DB_PASSWORD=your-db-password-here
DATABASE_URL=postgresql://dev:your-db-password-here@localhost:5432/ai_brain

# Supabase
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-supabase-anon-key-here
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key-here
SUPABASE_JWT_SECRET=your-supabase-jwt-secret-here

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=your-redis-password-here
REDIS_URL=redis://localhost:6379

# MindsDB
MINDSDB_API_KEY=your-mindsdb-api-key-here
MINDSDB_HOST=cloud.mindsdb.com
MINDSDB_PORT=47334

# =============================================================================
# MCP SERVERS & INTEGRATIONS
# =============================================================================

# Notion
NOTION_API_KEY=secret_your-notion-api-key-here
NOTION_VERSION=2022-06-28

# GitHub
GITHUB_TOKEN=ghp_your-github-token-here
GITHUB_ORG=harrysayers7
GITHUB_USER=harrysayers7

# Slack
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token-here
SLACK_APP_TOKEN=xapp-your-slack-app-token-here
SLACK_SIGNING_SECRET=your-slack-signing-secret-here

# Context7
CONTEXT7_API_KEY=your-context7-api-key-here
CONTEXT7_BASE_URL=https://api.context7.ai

# Dify
DIFY_API_KEY=app-your-dify-api-key-here
DIFY_BASE_URL=https://api.dify.ai
DIFY_WORKFLOW_ID=your-workflow-id-here

# Graphiti (Memory System)
GRAPHITI_API_KEY=your-graphiti-api-key-here
GRAPHITI_BASE_URL=https://api.graphiti.ai

# TaskMaster
TASKMASTER_API_KEY=your-taskmaster-api-key-here
TASKMASTER_BASE_URL=https://api.taskmaster.ai

# =============================================================================
# WORKFLOW AUTOMATION
# =============================================================================

# N8N
N8N_USER=admin
N8N_PASSWORD=your-n8n-password-here
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=your-n8n-password-here
N8N_WEBHOOK_URL=http://localhost:5678/webhook

# Trigger.dev
TRIGGER_API_KEY=tr_dev_your-trigger-api-key-here
TRIGGER_ENDPOINT_ID=your-endpoint-id-here

# =============================================================================
# BROWSER AUTOMATION
# =============================================================================

# Playwright
PLAYWRIGHT_BROWSER=chromium
PLAYWRIGHT_HEADLESS=true
PLAYWRIGHT_TIMEOUT=30000

# Chrome MCP
CHROME_MCP_ENABLED=true
CHROME_MCP_PORT=9222

# =============================================================================
# DEVELOPMENT & DEPLOYMENT
# =============================================================================

# Environment
NODE_ENV=development
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=debug

# Ports
PORT=3000
API_PORT=8000
N8N_PORT=5678
REDIS_PORT=6379
POSTGRES_PORT=5432

# URLs
FRONTEND_URL=http://localhost:3000
API_URL=http://localhost:8000
WEBHOOK_URL=https://your-domain.com/webhook

# =============================================================================
# SECURITY & AUTHENTICATION
# =============================================================================

# JWT
JWT_SECRET=your-super-secret-jwt-key-here
JWT_EXPIRES_IN=7d

# Encryption
ENCRYPTION_KEY=your-32-character-encryption-key-here

# CORS
CORS_ORIGIN=http://localhost:3000,http://localhost:8000

# =============================================================================
# MONITORING & ANALYTICS
# =============================================================================

# Sentry
SENTRY_DSN=https://your-sentry-dsn-here

# DataDog
DATADOG_API_KEY=your-datadog-api-key-here
DATADOG_APP_KEY=your-datadog-app-key-here

# =============================================================================
# EXTERNAL SERVICES
# =============================================================================

# Email (SendGrid)
SENDGRID_API_KEY=SG.your-sendgrid-api-key-here
FROM_EMAIL=noreply@yourdomain.com

# SMS (Twilio)
TWILIO_ACCOUNT_SID=your-twilio-account-sid-here
TWILIO_AUTH_TOKEN=your-twilio-auth-token-here
TWILIO_PHONE_NUMBER=+1234567890

# File Storage (AWS S3)
AWS_ACCESS_KEY_ID=your-aws-access-key-here
AWS_SECRET_ACCESS_KEY=your-aws-secret-key-here
AWS_REGION=us-east-1
S3_BUCKET_NAME=your-s3-bucket-name-here

# =============================================================================
# FEATURE FLAGS
# =============================================================================

# AI Features
ENABLE_AI_CHAT=true
ENABLE_AI_ANALYSIS=true
ENABLE_AI_GENERATION=true
ENABLE_MEMORY_SYSTEM=true

# Integrations
ENABLE_NOTION_INTEGRATION=true
ENABLE_GITHUB_INTEGRATION=true
ENABLE_SLACK_INTEGRATION=true
ENABLE_N8N_WORKFLOWS=true

# Development
ENABLE_DEBUG_LOGGING=true
ENABLE_API_DOCS=true
ENABLE_METRICS=true

# =============================================================================
# RATE LIMITING
# =============================================================================

# API Rate Limits
API_RATE_LIMIT=1000
API_RATE_WINDOW=3600
AI_RATE_LIMIT=100
AI_RATE_WINDOW=3600

# =============================================================================
# CACHING
# =============================================================================

# Cache Settings
CACHE_TTL=3600
CACHE_MAX_SIZE=1000
ENABLE_REDIS_CACHE=true

# =============================================================================
# BACKUP & RECOVERY
# =============================================================================

# Backup Settings
BACKUP_ENABLED=true
BACKUP_SCHEDULE=0 2 * * *
BACKUP_RETENTION_DAYS=30
BACKUP_S3_BUCKET=your-backup-bucket-here

# =============================================================================
# DEVELOPMENT OVERRIDES
# =============================================================================

# Override for local development
LOCAL_DEVELOPMENT=true
SKIP_AUTH=false
MOCK_EXTERNAL_APIS=false
USE_LOCAL_DB=true

# =============================================================================
# NOTES
# =============================================================================
# 
# 1. Replace all placeholder values with your actual API keys and credentials
# 2. Never commit this file or any .env files to version control
# 3. Use a secrets manager for production environments
# 4. Rotate API keys regularly according to your security policy
# 5. Some services may require additional configuration beyond environment variables
# 6. Check individual service documentation for required scopes and permissions
#
# =============================================================================
```

## Usage Instructions

1. **Copy the template**: Copy the code block above to a new `.env` file in your project root
2. **Fill in values**: Replace all placeholder values with your actual API keys and credentials
3. **Security**: Never commit `.env` files to version control
4. **Production**: Use a secrets manager for production environments

## Service Categories

### Core AI Services
- OpenAI (GPT models)
- Anthropic Claude
- Google AI (Gemini)
- Azure OpenAI
- Perplexity AI

### Database Services
- PostgreSQL (local development)
- Supabase (cloud database)
- Redis (caching)
- MindsDB (ML database)

### MCP Servers & Integrations
- Notion (workspace management)
- GitHub (repository management)
- Slack (communication)
- Context7 (fact verification)
- Dify (workflow automation)
- Graphiti (memory system)
- TaskMaster (task management)

### Workflow Automation
- N8N (workflow automation)
- Trigger.dev (background jobs)

### Browser Automation
- Playwright (browser automation)
- Chrome MCP (browser control)

### Development & Deployment
- Environment configuration
- Port settings
- URL configuration

### Security & Authentication
- JWT configuration
- Encryption keys
- CORS settings

### Monitoring & Analytics
- Sentry (error tracking)
- DataDog (monitoring)

### External Services
- SendGrid (email)
- Twilio (SMS)
- AWS S3 (file storage)

### Feature Flags
- AI feature toggles
- Integration toggles
- Development settings

### Rate Limiting & Caching
- API rate limits
- Cache configuration

### Backup & Recovery
- Backup settings
- Retention policies

