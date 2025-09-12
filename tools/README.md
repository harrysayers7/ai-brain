# Tools

External tool configurations and integrations.

## Structure

- **integrations/** - API configurations, tool settings, service connections

## Purpose

Document and configure all external tools:
- API configurations
- Service credentials (reference only, not actual secrets!)
- Integration mappings
- Tool-specific settings
- Webhook configurations
- Third-party service setups

## Tool Document Template

```markdown
---
title: Tool Name Configuration
type: tool
subtype: integration
tags: [tool-name, category, environment]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
ship_factor: 1-10
active: true
environment: development|staging|production|all
---

# Tool Name Configuration

## Overview
What this tool does and why we use it.

## Access
- URL: [endpoint]
- Dashboard: [admin panel]
- Docs: [documentation]

## Configuration
Non-sensitive configuration details.

## Integration Points
How it connects with our system.

## Monitoring
How to verify it's working.

## Troubleshooting
Common issues and solutions.
```

## Security Note

⚠️ **NEVER store actual credentials here!**

Use references to secret management:
```yaml
credentials:
  location: AWS_SECRETS_MANAGER
  key: prod/tool-name/api-key
  rotation: 90_days
```

## Review Schedule

- **On Change**: Update configuration
- **Monthly**: Verify active status
- **Quarterly**: Review necessity
- **Annually**: Audit all tools