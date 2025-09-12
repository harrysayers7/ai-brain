---
title: Capture Important Insight
type: command
subtype: shortcut
tags: [insight, learning, discovery]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
active: true
aliases: [!aha, !eureka, !learned]
---

# !insight - Important Learning to Remember

## Purpose
Capture significant insights, "aha moments", or important discoveries.

## Syntax
```
!insight [title] <impact> {details}
```

## Parameters
- `title`: Brief description (required)
- `<impact>`: Business/Technical/Team (default: technical)
- `{details}`: Full insight (from context)

## Action

1. **Capture Insight**: Save to knowledge/lessons/
2. **Assess Impact**: Rate importance and scope
3. **Connect Dots**: Link to related knowledge
4. **Share**: Flag for team review if high impact

## Examples

### Technical Insight
```
User: Just realized our bottleneck isn't the database, 
      it's the serialization between services!
User: !insight "serialization bottleneck"

Bot: 💡 Insight captured
    Saved: knowledge/lessons/serialization-bottleneck-insight.md
    Impact: High (performance)
    Action: Created investigation task
    Related: performance-optimization.md
```

### Business Insight
```
User: !insight "customer pattern" business "Users prefer quick wins over perfect features"

Bot: 💡 Business insight documented
    Ship Factor: 9 (affects product strategy)
    Notified: Product team
    Suggested: Update development priorities
```

## Insight Classification

### Technical
- Performance discoveries
- Architecture realizations
- Tool capabilities
- Integration opportunities

### Business
- User behavior patterns
- Market opportunities
- Cost optimizations
- Process improvements

### Team
- Collaboration improvements
- Communication patterns
- Skill gaps/strengths
- Workflow optimizations

## Generated Format

```markdown
---
title: [Insight Title]
type: knowledge
subtype: lesson
tags: [insight, impact-area, aha-moment]
impact: high|medium|low
actionable: true|false
---

# 💡 [Insight Title]

## The Insight
[Core realization]

## Why This Matters
[Impact analysis]

## Evidence
[What led to this insight]

## Actions
- [ ] Immediate action
- [ ] Investigation needed
- [ ] Process change

## Related Patterns
[Connections to other knowledge]
```

## Follow-up Actions

High-impact insights trigger:
- Team notification
- Task creation
- Priority adjustment
- Strategy review

## Options

```
!insight -team     # Share with team
!insight -task     # Create action items
!insight -brief    # Just capture, analyze later
```