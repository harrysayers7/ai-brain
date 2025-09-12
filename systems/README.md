# Systems

Operational systems including workflows, rules, and processes.

## Structure

- **workflows/** - Repeatable processes and automations
- **rules/** - Governance, constraints, and policies

## Purpose

Define how work gets done:
- Step-by-step processes
- Automation sequences
- Business rules and constraints
- Operational policies
- Quality gates and checkpoints

## System Document Template

```markdown
---
title: System Name
type: system
subtype: workflow|rule
tags: [relevant, tags]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
ship_factor: 1-10
active: true
---

# System Name

## Purpose
What this system accomplishes.

## Scope
- What it covers
- What it doesn't cover
- Edge cases

## Components
Key parts of the system.

## Integration Points
How it connects with other systems.

## Monitoring
How to know it's working.
```

## Best Practices

1. **Automation First**: If it can be automated, it should be
2. **Clear Triggers**: Define what starts/stops the system
3. **Error Handling**: Plan for failures
4. **Metrics**: Measure effectiveness
5. **Documentation**: Keep it current

## Review Schedule

- **Daily**: Check active workflows
- **Weekly**: Review automation effectiveness
- **Monthly**: Update based on issues
- **Quarterly**: Optimize and refactor