---
title: Create High-Priority Task
type: command
subtype: shortcut
tags: [priority, ship, urgent]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
active: true
aliases: [!urgent, !now, !priority]
---

# !ship - Ship This Now

## Purpose
Create a high-priority decision or task that needs immediate attention.

## Syntax
```
!ship [what] <when> {why}
```

## Parameters
- `what`: Task or decision (required)
- `<when>`: Deadline (default: today)
- `{why}`: Urgency reason (from context)

## Action

1. **Create Entry**: High ship-factor item
2. **Set Priority**: Ship factor 9-10
3. **Add to Index**: Top of HIGH PRIORITY section
4. **Notify**: Alert if integrated

## Examples

### Urgent Fix
```
User: The API is rate limiting users, we need to fix this NOW
User: !ship "fix rate limiting"

Bot: 🚨 HIGH PRIORITY Created
    File: knowledge/decisions/fix-rate-limiting.md
    Ship Factor: 10
    Deadline: Today
    Status: Added to top of INDEX.md
```

### Scheduled Ship
```
User: !ship "migrate database" "friday" "maintenance window"

Bot: 🚀 Scheduled for shipping
    Ship Factor: 9
    Deadline: Friday
    Reason: Maintenance window
    Created workflow: systems/workflows/database-migration.md
```

## Generated Content

```markdown
---
title: [SHIP] Task Name
type: knowledge
subtype: decision
tags: [urgent, ship-now, high-priority]
ship_factor: 10
deadline: [date]
status: active
---

# 🚨 [SHIP] Task Name

## Urgent Because
[Reason for urgency]

## Decision/Action
[What needs to be done]

## Deadline
[When this must ship]

## Success Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## Blockers
- None identified | [List blockers]

## Resources Needed
- [What/who needed]
```

## Auto-Actions

- Adds to top of priority list
- Creates calendar reminder if deadline
- Suggests workflow if complex
- Links related decisions

## Options

```
!ship -block    # Has blockers
!ship -team     # Needs team
!ship -solo     # Can do alone
```