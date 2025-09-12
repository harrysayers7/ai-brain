# Workflows

Repeatable processes and automation sequences.

## What Belongs Here

- Development workflows (CI/CD, review process)
- Operational workflows (deployment, monitoring)
- Business workflows (onboarding, reporting)
- Automation scripts and sequences
- Runbooks and playbooks

## Workflow Template

```markdown
---
title: [Workflow] X Process
type: system
subtype: workflow
tags: [workflow, area, frequency]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
ship_factor: 7
active: true
frequency: daily|weekly|monthly|on-demand
automation_level: manual|semi-auto|full-auto
---

# [Workflow] X Process

## Overview
What this workflow accomplishes.

## Triggers
- **Automatic**: [cron, event, condition]
- **Manual**: [command, button, request]
- **Hybrid**: [approval required]

## Prerequisites
- [ ] Condition 1 met
- [ ] Access to system Y
- [ ] Tool Z available
- [ ] Previous step X completed

## Steps

### 1. Step Name (Automated/Manual)
**Actor**: Human|System
**Duration**: ~X minutes

```bash
# Command or action
command --with-flags
```

**Validation**: How to verify success
**Rollback**: How to undo if needed

### 2. Step Name
[Repeat pattern]

## Decision Points

### Decision 1: [Condition]
- If A: Continue to Step 3
- If B: Go to Step 5
- If Error: Execute rollback

## Outputs
- Output 1: [description, location]
- Output 2: [description, location]
- Logs: [where to find them]
- Metrics: [what's measured]

## Error Handling

| Error | Likelihood | Impact | Response |
|-------|------------|--------|----------|
| X fails | Medium | High | Retry 3x then alert |
| Y timeout | Low | Medium | Increase timeout |
| Z missing | Low | Critical | Stop and alert |

## Rollback Procedure

1. Identify failure point
2. Execute rollback steps
3. Verify system state
4. Document incident

## Monitoring

- **Success Metrics**: [what indicates success]
- **SLAs**: [time/quality requirements]
- **Alerts**: [when to notify]
- **Dashboard**: [link to monitoring]

## Dependencies

- Upstream: [what must happen before]
- Downstream: [what this triggers]
- Systems: [what systems are involved]
- Teams: [who needs to know]

## Automation Opportunities

- [ ] Step 2 could be automated with script
- [ ] Decision point 1 could use ML
- [ ] Notification could be automatic

## Change Log

- v2: Automated step 3
- v1: Initial manual process
```

## Workflow Categories

### Development
- `code-review-process.md`
- `release-workflow.md`
- `hotfix-procedure.md`
- `feature-flag-rollout.md`

### Operations
- `deployment-pipeline.md`
- `incident-response.md`
- `backup-restore.md`
- `scaling-procedure.md`

### Business
- `customer-onboarding.md`
- `monthly-reporting.md`
- `invoice-processing.md`
- `support-escalation.md`

### Maintenance
- `database-cleanup.md`
- `log-rotation.md`
- `dependency-updates.md`
- `security-patching.md`

## Automation Levels

### Level 0: Manual
- Human executes all steps
- Documentation-driven
- Checklist-based

### Level 1: Assisted
- Scripts available
- Copy-paste commands
- Some validation automated

### Level 2: Semi-Automated
- One-click execution
- Human approval required
- Automatic validation

### Level 3: Fully Automated
- Triggered automatically
- No human intervention
- Self-healing on errors

## Best Practices

### DO:
✅ Include time estimates
✅ Document rollback procedures
✅ Specify actor for each step
✅ Include validation criteria
✅ Link to relevant tools/scripts

### DON'T:
❌ Skip error handling
❌ Assume knowledge
❌ Forget dependencies
❌ Ignore edge cases
❌ Leave out monitoring

## Testing Workflows

1. **Dry Run**: Execute without side effects
2. **Staging Test**: Run in test environment
3. **Canary**: Run on subset first
4. **Load Test**: Verify at scale
5. **Chaos Test**: Inject failures

## Metrics to Track

- **Execution Time**: How long it takes
- **Success Rate**: How often it works
- **Error Rate**: How often it fails
- **Manual Interventions**: How often humans needed
- **Cost**: Resources consumed