---
title: Document Success
type: command
subtype: shortcut
tags: [success, validation, confirmation]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
active: true
aliases: [!success, !win, !confirmed]
---

# !works - This Solution Worked

## Purpose
Confirm and document that a solution, approach, or fix was successful.

## Syntax
```
!works <rating> {notes}
```

## Parameters
- `<rating>`: Success level 1-10 (default: 8)
- `{notes}`: Additional context or caveats

## Action

1. **Mark Success**: Update related entries with validation
2. **Increase Priority**: Bump ship factor for proven solutions
3. **Create Reference**: Add to references if reusable
4. **Update Stats**: Track success rate

## Examples

### Simple Confirmation
```
User: That Docker fix worked perfectly!
User: !works

Bot: ✅ Marked solution as validated
    Updated: knowledge/lessons/docker-compose-fix.md
    Ship Factor: 7 → 9 (proven solution)
    Success Rate: 100% (1/1 uses)
```

### With Rating
```
User: !works 10 "Solved the problem completely, no side effects"

Bot: ✅ Solution validated with perfect score
    Created: knowledge/references/proven-solution-x.md
    Tagged: [validated, production-ready, high-confidence]
```

### Partial Success
```
User: !works 6 "Fixed main issue but needs optimization"

Bot: ⚠️ Partial success documented
    Note added about optimization needs
    Ship Factor: 6 (works but needs improvement)
```

## Side Effects

- Proven solutions get promoted to references
- Updates success metrics in INDEX.md
- May trigger creation of standard workflow
- Adds "validated" tag to original entry

## Tracking

```yaml
validation:
  status: confirmed
  rating: 8/10
  date: 2024-01-15
  uses: 1
  success_rate: 100%
  notes: "Additional context"
```

## Options

```
!works -prod     # Validated in production
!works -test     # Worked in test only
!works -partial  # Partial success
```