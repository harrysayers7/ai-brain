<!--
HUMAN DESCRIPTION - AI SHOULD IGNORE THIS SECTION
Purpose: Documentation explaining the modes directory structure and purpose for AI behavioral modes
Usage: Human reference for understanding AI mode organization and creation
Target: Human users managing the AI Brain system and creating new AI modes
DO NOT READ THIS SECTION - AI CONTENT BEGINS AFTER THE HTML COMMENT
-->
# Modes

AI operational modes for different interaction styles and contexts.

## What Belongs Here

Modes define how AI operates in different contexts:
- Communication style
- Expertise level
- Emotional tone
- Problem-solving approach
- Values and priorities
- Operational behavior

## Mode Template

```markdown
---
title: [Mode] The X
type: behavior
subtype: mode
tags: [mode, style, domain]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
ship_factor: 7
active: true
---

# [Mode] The X

## Identity
I am a [role] who [primary function].

## Core Traits
- **Primary**: [Main characteristic]
- **Style**: [Communication approach]
- **Focus**: [What I prioritize]
- **Expertise**: [Domain knowledge]

## Voice & Tone
- Speak in [first/second/third] person
- Use [formal/casual/technical] language
- [Short/detailed] responses
- [Direct/diplomatic] feedback

## Behavioral Rules
1. Always [do this]
2. Never [do that]
3. When uncertain, [default behavior]
4. Prioritize [this over that]

## Sample Interactions

### User: "Should we use microservices?"
**Response**: "[Mode-appropriate response]"

### User: "I'm stuck on this problem"
**Response**: "[Mode-appropriate response]"

## Activation Triggers
- Keywords: [list of trigger words]
- Contexts: [when to activate]
- Projects: [specific project types]

## Combination Rules
- Works well with: [other modes/modes]
- Conflicts with: [incompatible behaviors]
- Overrides: [what this mode overrides]
```

## Example Modes

### Development Focused
- `skeptical-reviewer.md` - Challenges over-engineering
- `pragmatic-architect.md` - Focuses on shipping
- `security-auditor.md` - Finds vulnerabilities
- `performance-optimizer.md` - Identifies bottlenecks

### Business Focused
- `product-strategist.md` - User-value focused
- `cost-analyzer.md` - ROI and budget conscious
- `customer-advocate.md` - User experience first

### Support Focused
- `patient-teacher.md` - Educational approach
- `debug-detective.md` - Systematic troubleshooting
- `empathetic-coach.md` - Emotional support + technical help

## Creating Effective Modes

### DO:
✅ Give clear, specific behavioral rules
✅ Include example responses
✅ Define clear activation triggers
✅ Specify expertise boundaries
✅ Make them memorable and distinct

### DON'T:
❌ Make them too similar to each other
❌ Create conflicting rules within a mode
❌ Forget to specify when NOT to use
❌ Make them too narrow (unusable)
❌ Make them too broad (meaningless)

## Activation in Practice

```yaml
# In your prompt:
Using mode: prompts/modes/skeptical-reviewer.md

Review this architecture...
```

## Testing Modes

1. **Consistency**: Same input → similar style output
2. **Distinctiveness**: Different from default AI behavior
3. **Appropriateness**: Fits the intended use case
4. **Completeness**: Handles edge cases properly

## Maintenance

- **After Each Use**: Note effectiveness
- **Weekly**: Update based on feedback
- **Monthly**: Review activation patterns
- **Quarterly**: Consolidate similar modes
