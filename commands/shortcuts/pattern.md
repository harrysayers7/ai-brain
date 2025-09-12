---
title: Log Workflow Pattern
type: command
subtype: shortcut
tags: [workflow, pattern, automation]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
active: true
aliases: [!pat, !workflow, !wf]
---

# !pattern - Log Workflow Pattern

## Purpose
Capture a successful workflow or process pattern for reuse.

## Syntax
```
!pattern [name] <category> {steps}
```

## Parameters
- `name`: Pattern identifier (required)
- `<category>`: Type of pattern (default: general)
- `{steps}`: Workflow steps (extracted from context)

## Action

1. **Extract Workflow**: Identify steps from conversation
2. **Create Workflow Doc**: Save to `systems/workflows/`
3. **Generate Automation**: Suggest automation opportunities
4. **Link Related**: Connect to similar patterns

## Examples

### Capture Current Workflow
```
User: First I check logs, then identify the error pattern, 
      then search Stack Overflow, then test the fix
User: !pattern "debug-process"

Bot: ✅ Workflow saved to systems/workflows/debug-process.md
    Steps identified: 4
    Automation potential: Medium (steps 1-2 can be automated)
```

### Categorized Pattern
```
User: !pattern "pr-review" development

Bot: ✅ Saved to systems/workflows/pr-review.md
    Category: development
    Linked to: code-review-process.md
```

## Auto-Generated Content

```markdown
---
title: [Pattern Name]
type: system
subtype: workflow
tags: [pattern, category, auto-generated]
created: [timestamp]
frequency: on-demand
automation_level: manual
---

# [Pattern Name]

## Trigger
[Extracted from context]

## Steps
1. [First identified step]
2. [Second identified step]
...

## Validation
- [ ] [Success criteria]

## Automation Opportunities
- Step X could be scripted
- Step Y could use tool Z
```

## Pattern Recognition

Automatically detects:
- Sequential steps (then, after, next)
- Conditions (if, when, unless)
- Loops (repeat, until, while)
- Parallel tasks (meanwhile, simultaneously)

## Integration

### Suggests Follow-ups
- `!tool` - If tools mentioned
- `!works` - To confirm success
- `!repeat` - If frequently used

## Options

```
!pattern -detail    # Capture more context
!pattern -simple    # Basic steps only
!pattern -auto      # Suggest automation
```