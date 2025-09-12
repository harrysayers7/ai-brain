---
title: Search Knowledge Base
type: command
subtype: shortcut
tags: [search, query, find]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
active: true
aliases: [!search, !query, !lookup]
---

# !find - Search Knowledge Base

## Purpose
Quickly search through all knowledge base entries.

## Syntax
```
!find [query] <type> <tags>
```

## Parameters
- `query`: Search terms (required)
- `<type>`: Filter by type (optional)
- `<tags>`: Filter by tags (optional)

## Action

1. **Search All Files**: Full-text search
2. **Rank Results**: By relevance and ship factor
3. **Return Summary**: Top 5 matches
4. **Suggest Related**: Similar entries

## Examples

### Simple Search
```
User: !find "docker"

Bot: 🔍 Found 3 matches:
    1. [9] docker-compose-fix.md - Proven solution
    2. [7] docker-deployment.md - Workflow
    3. [5] docker-basics.md - Reference
```

### Filtered Search
```
User: !find "rate limit" tool

Bot: 🔍 Found in tools:
    1. tools/integrations/api-rate-limits.md
    2. tools/integrations/cloudflare-config.md
```

### Tag Search
```
User: !find "" "" api,urgent

Bot: 🔍 Found with tags [api, urgent]:
    1. [10] fix-api-outage.md
    2. [9] api-migration.md
```

## Search Scope

- All markdown files
- Frontmatter metadata
- Content body
- File paths
- Tags and references

## Results Format

```
[Ship Factor] filename.md - Brief description
  Path: full/path/to/file.md
  Tags: [tag1, tag2]
  Modified: date
  Preview: "First 100 chars..."
```

## Options

```
!find -all       # Show all results
!find -recent    # Last 7 days only
!find -high      # Ship factor 8+
!find -deprecated # Include deprecated
```