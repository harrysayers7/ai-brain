# Lessons Learned

Things we've learned through experience, including failures, successes, and "aha" moments.

## What Belongs Here

- Post-mortems from failures
- Successful experiments
- Anti-patterns we've discovered
- "I wish I knew this earlier" moments
- Performance discoveries
- Security learnings

## Lesson Document Template

```markdown
---
title: [Lesson] What We Learned About X
type: knowledge
subtype: lesson
tags: [lesson, anti-pattern, area, technology]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
ship_factor: 8
deprecated: false
references:
  - knowledge/decisions/related-decision.md
---

# [Lesson] What We Learned About X

## The Lesson
One-sentence summary of what we learned.

## What Happened
- Context and setup
- What we tried
- What went wrong (or right)
- Impact (time lost, money saved, etc.)

## Root Cause
Why this happened (5 Whys analysis if applicable).

## What We Learned
- Key insights
- Patterns to recognize
- Early warning signs

## What To Do Instead
- Recommended approach
- Preventive measures
- Detection methods

## Applied To
Where we've applied this lesson:
- Project X: Saved 2 weeks
- Feature Y: Avoided the issue entirely

## Related Patterns
- Similar lessons
- Industry best practices
- External resources
```

## Categories

### Anti-Patterns
Things that seemed good but weren't:
- `premature-microservices.md`
- `over-abstracting-too-early.md`
- `optimizing-before-measuring.md`

### Success Patterns
Things that worked better than expected:
- `boring-tech-wins.md`
- `ship-daily-learn-faster.md`
- `customer-feedback-beats-planning.md`

### Post-Mortems
Learnings from incidents:
- `2024-01-database-outage.md`
- `slow-deploy-investigation.md`
- `memory-leak-lessons.md`

## How to Write a Good Lesson

1. **Be Specific**: Include numbers, dates, impact
2. **No Blame**: Focus on systems, not people
3. **Action-Oriented**: Always include "what to do instead"
4. **Measurable**: How do we know we've learned?
5. **Shareable**: Written so others can learn too

## Review Process

- **Immediately**: After any incident or surprise
- **Weekly**: Quick lessons from the week
- **Monthly**: Pattern recognition across lessons
- **Quarterly**: Update prevention strategies