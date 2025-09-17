---
created: '2025-09-16T15:05:15.650029'
modified: '2025-09-17T16:14:24.446345'
ship_factor: 5
subtype: claude-desktop
tags: []
title: Claude Instructions
type: tool
version: 1
---

# Claude Desktop Integration

## Repository Navigation
- Read `SYSTEM.md` for complete navigation rules
- Check `INDEX.md` for current high-priority items
- All content uses markdown with YAML frontmatter

## Command Recognition
Process commands starting with `!` using definitions in `commands/shortcuts/`

## File Operations
- CREATE: Add to appropriate folder with frontmatter (see templates in each folder's README)
- UPDATE: Increment version, update modified date
- DELETE: Never delete - set `deprecated: true` in frontmatter
- SEARCH: Use tags and ship_factor for filtering

## Priority System
Ship Factor 9-10 = Immediate action required
Ship Factor 7-8 = This week
Ship Factor 5-6 = This sprint

## Quick Commands
- `!memz [title]` - Save to knowledge base
- `!ship [task]` - Create high-priority item
- `!find [query]` - Search all content
- `!works` - Mark solution as validated