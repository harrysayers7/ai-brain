---
title: Save Frequent Request
type: command
subtype: shortcut
tags: [template, frequent, reusable]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
active: true
aliases: [!freq, !template, !common]
---

# !repeat - Save Frequently Asked Template

## Purpose
Save a frequently asked question or request as a reusable template.

## Syntax
```
!repeat [name] <category> {template}
```

## Parameters
- `name`: Template identifier (required)
- `<category>`: Type of request (default: general)
- `{template}`: The request pattern (from context)

## Action

1. **Extract Pattern**: Identify the repeating request
2. **Create Template**: Save to `commands/templates/`
3. **Generate Shortcuts**: Create quick access command
4. **Track Usage**: Monitor frequency

## Examples

### Save Current Request
```
User: How do I check the status of all services in production?
User: !repeat "service-status"

Bot: ✅ Template saved: commands/templates/service-status.md
    Quick access: !tpl service-status
    Similar requests: 5 times this week
```

### Categorized Template
```
User: !repeat "daily-standup" meetings

Bot: ✅ Template created for meetings category
    Suggested automation: Create daily workflow
    Related templates: morning-check, team-sync
```

## Template Format

```markdown
---
title: [Template Name]
type: command
subtype: template
tags: [template, category, frequent]
frequency: [usage count]
last_used: [timestamp]
---

# [Template Name]

## Request Pattern
[The common request]

## Variables
- {{var1}}: Description
- {{var2}}: Description

## Standard Response
[Typical answer structure]

## Variations
- Variation 1: [context]
- Variation 2: [context]

## Quick Command
!tpl [name] var1=value var2=value
```

## Usage Tracking

- Counts how often requested
- Suggests optimization after 5 uses
- Proposes automation after 10 uses
- Creates workflow after 20 uses

## Auto-Suggestions

```
Bot: I notice you ask this often. Should I:
    1. Create a dashboard for this?
    2. Set up automated reports?
    3. Build a dedicated command?
```

## Options

```
!repeat -vars      # Include variables
!repeat -response  # Include standard response
!repeat -auto      # Auto-create command
```