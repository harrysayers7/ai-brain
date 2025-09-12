# Operational Modes

Context-specific behavior modifications that adjust how the AI operates.

## What Belongs Here

Modes are behavioral overlays that modify AI operation:
- Debug mode (verbose, detailed)
- Production mode (concise, safe)
- Learning mode (explanatory, patient)
- Emergency mode (rapid, focused)
- Creative mode (exploratory, experimental)

## Mode Template

```markdown
---
title: [Mode] X Mode
type: behavior
subtype: mode
tags: [mode, context, operation]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
ship_factor: 6
active: true
priority: 1-10  # Higher overrides lower
---

# [Mode] X Mode

## Purpose
When and why to activate this mode.

## Modifications

### Output Format
- Length: [shorter/normal/detailed]
- Structure: [paragraph/bullet/code]
- Verbosity: [minimal/balanced/verbose]

### Processing Rules
- Speed vs Accuracy: [preference]
- Risk Tolerance: [conservative/balanced/aggressive]
- Assumption Making: [never/when-clear/freely]

### Behavioral Overrides
- Override 1: [what changes]
- Override 2: [what changes]
- Override 3: [what changes]

## Activation Conditions

### Automatic Triggers
- Time: [business hours/after hours/weekends]
- Context: [production/staging/development]
- User: [senior/junior/external]
- Urgency: [normal/high/critical]

### Manual Triggers
- Commands: `!debug`, `!verbose`, etc.
- Flags: `--mode=debug`
- Context: Explicit request

## Examples

### Normal Behavior
```
User: How do I fix this error?
AI: Try checking X, then Y.
```

### With This Mode
```
User: How do I fix this error?
AI: [Mode-modified response showing difference]
```

## Compatibility
- Combines with: [list of compatible modes]
- Overrides: [what this mode overrides]
- Overridden by: [what overrides this mode]

## Exit Conditions
- Time limit: [duration]
- Task completion: [criteria]
- Manual: [command to exit]
```

## Common Modes

### Development Modes
- `debug-mode.md` - Verbose logging, detailed errors
- `test-mode.md` - Mock data, safe operations
- `demo-mode.md` - Polished, curated responses

### Operational Modes
- `production-mode.md` - Safe, stable, monitored
- `maintenance-mode.md` - Limited features, careful
- `emergency-mode.md` - Rapid response, skip non-critical

### Interaction Modes
- `learning-mode.md` - Educational, patient, detailed
- `expert-mode.md` - Concise, technical, assume knowledge
- `discovery-mode.md` - Exploratory, creative, experimental

### Safety Modes
- `safe-mode.md` - Conservative, double-check everything
- `audit-mode.md` - Log everything, compliance focused
- `restricted-mode.md` - Limited capabilities, high security

## Mode Stacking

Modes can be combined with priority resolution:

```yaml
Active Modes:
1. emergency-mode (priority: 10) - Overrides all
2. production-mode (priority: 5) - Base behavior
3. audit-mode (priority: 3) - Adds logging

Result: Emergency behavior + audit logging
```

## Best Practices

1. **Clear Priorities**: Higher priority = stronger override
2. **Explicit Conflicts**: Document what can't combine
3. **Exit Strategies**: Always define how to deactivate
4. **Test Combinations**: Verify mode stacking works
5. **Document Changes**: Clear before/after examples

## Activation Patterns

### Time-Based
```yaml
schedule:
  - weekdays 9-5: production-mode
  - weekdays 5-9: maintenance-mode
  - weekends: development-mode
```

### Context-Based
```yaml
environment:
  production: [production-mode, audit-mode]
  staging: [test-mode, debug-mode]
  development: [debug-mode, learning-mode]
```

### User-Based
```yaml
user_level:
  senior: expert-mode
  junior: learning-mode
  external: safe-mode
```

## Monitoring

- Track mode activation frequency
- Log mode switch reasons
- Monitor mode effectiveness
- Review inappropriate activations