# Command Templates

Reusable prompt templates for common requests.

## What Belongs Here

Templates for frequently used:
- Prompts and queries
- Report formats
- Analysis patterns
- Review checklists
- Standard responses

## Template Format

```markdown
---
title: Template Name
type: command
subtype: template
tags: [template, category]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
frequency: daily|weekly|monthly|on-demand
variables:
  - name: var1
    type: string
    default: value
    required: true
  - name: var2
    type: number
    default: 5
    required: false
---

# Template Name

## Purpose
What this template is for.

## Usage
```
!tpl template-name var1="value" var2=10
```

## Template

[The actual template with {{variables}}]

## Examples

### Example 1
Input: !tpl template-name var1="test"
Output: [Processed template]

### Example 2
Input: !tpl template-name var1="prod" var2=20
Output: [Processed template]

## Variations

### Variation Name
[Alternative template structure]
```

## Template Categories

### Analysis Templates
- `code-review.md` - Standard code review
- `performance-analysis.md` - Performance check
- `security-audit.md` - Security review
- `cost-analysis.md` - Cost breakdown

### Report Templates
- `daily-standup.md` - Standup format
- `weekly-summary.md` - Week review
- `incident-report.md` - Incident template
- `project-status.md` - Status update

### Query Templates
- `system-status.md` - Check all services
- `user-metrics.md` - User analytics
- `error-investigation.md` - Error lookup
- `deployment-check.md` - Deploy validation

### Decision Templates
- `tech-choice.md` - Technology decision
- `architecture-review.md` - Architecture choice
- `buy-vs-build.md` - Make or buy
- `priority-matrix.md` - Priority decision

## Using Templates

### Quick Access
```bash
# List all templates
!tpl list

# Use template
!tpl template-name var1=value

# Preview template
!tpl preview template-name
```

### With Variables
```bash
# Positional
!tpl daily-standup "John" "3 tasks" "No blockers"

# Named
!tpl daily-standup name="John" completed="3 tasks" blockers="None"

# Mixed
!tpl daily-standup "John" blockers="Waiting on API"
```

## Template Processing

1. Load template file
2. Parse variables
3. Validate required fields
4. Replace {{variables}}
5. Return processed text

## Creating Templates

### From Repeated Request
```
User: [Asks same question multiple times]
Bot: I notice you ask this often. Should I create a template?
User: Yes
Bot: Created template: !tpl your-question
```

### From Command
```
User: !repeat "daily-check" "How are services {{env}}?"
Bot: Template created: !tpl daily-check env="prod"
```

## Best Practices

1. **Clear Variables**: Use descriptive names
2. **Defaults**: Provide sensible defaults
3. **Validation**: Check required fields
4. **Examples**: Include 2-3 examples
5. **Variations**: Document alternatives

## Advanced Features

### Conditional Sections
```
{{#if premium}}
  Include premium features
{{/if}}
```

### Loops
```
{{#each items}}
  - {{this.name}}: {{this.value}}
{{/each}}
```

### Computed Values
```
{{multiply quantity price}}
{{formatDate date "YYYY-MM-DD"}}
```