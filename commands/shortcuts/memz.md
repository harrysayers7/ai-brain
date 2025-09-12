---
title: Save to Memory
type: command
subtype: shortcut
tags: [memory, quick-save, pattern]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
active: true
aliases: [!mem, !m, !remember]
---

# !memz - Save to Memory

## Purpose
Quickly save a pattern, insight, or learning to long-term memory.

## Syntax
```
!memz [title] {content}
```

## Parameters
- `title`: Brief description (required)
- `{content}`: The actual content to save (uses context if not provided)

## Action

1. **Determine Type**: Analyze content to categorize
   - Pattern → `knowledge/lessons/`
   - Decision → `knowledge/decisions/`
   - Tool config → `tools/integrations/`
   - Workflow → `systems/workflows/`

2. **Create Entry**: Generate markdown file with:
   - Auto-generated filename from title
   - Appropriate frontmatter
   - Timestamp
   - Ship factor based on urgency

3. **Update Index**: Add to INDEX.md

4. **Confirm**: Return location and summary

## Examples

### Save Current Context
```
User: [explains complex solution]
User: !memz "Docker compose fix"

Bot: ✅ Saved to knowledge/lessons/docker-compose-fix.md
    Ship Factor: 7 (marked as useful pattern)
```

### Save with Content
```
User: !memz "API rate limit" "Use exponential backoff: 1, 2, 4, 8, 16 seconds"

Bot: ✅ Saved to knowledge/references/api-rate-limit.md
    Tagged: [api, rate-limiting, retry-strategy]
```

### Save Conversation Pattern
```
User: This workflow of test-first, then implement, then refactor really works!
User: !memz

Bot: ✅ Saved to knowledge/lessons/test-first-workflow.md
    Captured last interaction as successful pattern
```

## Auto-Processing

The command automatically:
- Extracts key points from context
- Generates appropriate tags
- Sets ship factor based on keywords
- Creates references to related entries
- Formats for both human and LLM reading

## Integration

### With Other Commands
- Often followed by `!find` to verify storage
- Can trigger `!pattern` if workflow detected
- May suggest `!repeat` if similar exists

### With Personas
When active persona affects storage:
- `skeptical-reviewer` → Adds "verify" tag
- `shipping-coach` → Sets high ship factor
- `learning-mode` → More detailed capture

## Storage Format

```markdown
---
title: [Generated from command]
type: knowledge
subtype: [auto-detected]
tags: [auto-generated]
created: [timestamp]
modified: [timestamp]
version: 1
ship_factor: [auto-scored]
source: !memz command
context_length: [number of previous messages included]
---

# [Title]

## Context
[Captured from conversation]

## Key Points
[Extracted automatically]

## Action Items
[Generated from content]
```

## Options

```
!memz -v          # Verbose output
!memz -q          # Quiet (just save)
!memz -high       # Force high priority
!memz -draft      # Save as draft
!memz -append     # Add to existing
```