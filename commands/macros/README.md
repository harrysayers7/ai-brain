# Command Macros

Multi-step command sequences for complex operations.

## What Belongs Here

Macros combine multiple commands:
- Setup sequences
- Deployment chains
- Analysis workflows
- Batch operations
- Conditional flows

## Macro Format

```markdown
---
title: Macro Name
type: command
subtype: macro
tags: [macro, category]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
steps: 5
estimated_time: 2 minutes
requires_confirmation: true
---

# Macro Name

## Purpose
What this macro accomplishes.

## Syntax
```
!macro macro-name [params]
```

## Steps

1. **Step Name**
   - Command: `!command1 param`
   - Purpose: What this does
   - Validation: Success criteria

2. **Step Name**
   - Command: `!command2`
   - Condition: Only if step 1 succeeds
   - Rollback: How to undo

## Parameters
- param1: Description
- param2: Description (optional)

## Examples

### Basic Usage
```
User: !macro deploy-prod

Bot: 🔄 Executing macro: deploy-prod (5 steps)
    Step 1/5: Running tests... ✅
    Step 2/5: Building image... ✅
    Step 3/5: Pushing to registry... ✅
    Step 4/5: Deploying to k8s... ✅
    Step 5/5: Health check... ✅
    
    ✅ Macro completed successfully!
```

## Error Handling

If any step fails:
1. Stop execution
2. Run rollback steps
3. Report failure point
4. Suggest manual fixes
```

## Macro Categories

### Deployment Macros
- `deploy-prod.md` - Full production deploy
- `rollback.md` - Emergency rollback
- `canary-release.md` - Gradual rollout
- `hotfix.md` - Emergency patch

### Analysis Macros
- `full-audit.md` - Complete system audit
- `performance-check.md` - Perf analysis
- `security-scan.md` - Security review
- `cost-review.md` - Cost analysis

### Maintenance Macros
- `backup-all.md` - Full backup
- `cleanup.md` - System cleanup
- `update-deps.md` - Update dependencies
- `rotate-secrets.md` - Rotate credentials

### Setup Macros
- `onboard-dev.md` - Dev environment setup
- `create-project.md` - New project setup
- `configure-ci.md` - CI/CD setup
- `init-monitoring.md` - Monitoring setup

## Macro Execution

### Sequential
```yaml
steps:
  - !command1
  - !command2
  - !command3
```

### Conditional
```yaml
steps:
  - !command1
  - if: success
    then: !command2
    else: !rollback
```

### Parallel
```yaml
steps:
  - parallel:
    - !command1
    - !command2
  - !command3  # After both complete
```

### Loop
```yaml
steps:
  - foreach: [item1, item2, item3]
    do: !command {{item}}
```

## Creating Macros

### From History
```
Bot: I notice you run these commands together often:
     !test, !build, !deploy
     Create macro? [Y/n]
```

### From Definition
```
User: !macro create "my-flow" "!cmd1 && !cmd2 && !cmd3"
Bot: Macro created: !macro my-flow
```

## Safety Features

### Dry Run
```
!macro deploy-prod --dry-run

Shows what would happen without executing
```

### Confirmation
```
!macro dangerous-operation

Bot: ⚠️ This macro will:
     - Delete X
     - Modify Y
     - Restart Z
     Continue? [y/N]
```

### Rollback
```yaml
rollback:
  - step: 3
    command: !undo-deploy
  - step: 2
    command: !restore-backup
```

## Best Practices

1. **Atomic Steps**: Each step should be complete
2. **Idempotent**: Can run multiple times safely
3. **Rollback Plan**: Every step can be undone
4. **Validation**: Check success at each step
5. **Timeouts**: Set max execution time

## Monitoring

### Execution Tracking
```yaml
execution:
  id: macro-run-12345
  started: 2024-01-15T10:00:00Z
  completed: 2024-01-15T10:02:00Z
  status: success
  steps_completed: 5/5
  duration: 2m
```

### Success Metrics
- Success rate: 95%
- Average duration: 2m 30s
- Common failures: Step 3 (network)
- Last run: 2 hours ago