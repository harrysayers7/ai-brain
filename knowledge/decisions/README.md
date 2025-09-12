# Decisions

Architectural and technical decisions that shape our system.

## What Belongs Here

- Technology choices (frameworks, libraries, services)
- Architectural patterns (monolith vs microservices, sync vs async)
- Development practices (testing strategy, deployment approach)
- Trade-off analyses (build vs buy, optimize vs simplify)

## Decision Document Template

```markdown
---
title: [Decision] Choose X Over Y
type: knowledge
subtype: decision
tags: [architecture, technology-name, area-affected]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
ship_factor: 7
deprecated: false
supersedes: previous-decision.md  # if replacing old decision
references:
  - knowledge/lessons/related-lesson.md
  - knowledge/references/tech-comparison.md
---

# [Decision] Choose X Over Y

## Decision
We will use X instead of Y for [specific purpose].

## Status
Accepted | Proposed | Deprecated | Superseded

## Context
- Current situation
- Problem we're solving
- Constraints (time, budget, team size)

## Options Considered

### Option 1: X (Chosen)
- Pros: Fast to implement, team knows it
- Cons: Less flexible
- Cost: $0
- Time: 1 week

### Option 2: Y
- Pros: More features
- Cons: 3-month learning curve
- Cost: $500/month
- Time: 3 months

## Decision Rationale
Why we chose X over Y.

## Consequences
- What becomes easier
- What becomes harder
- What we need to watch for

## Upgrade Triggers
Switch to Y when:
- User base > 100K
- Team size > 10
- Cost of X > $5K/month

## Review Date
2024-06-15 - Revisit this decision
```

## Examples

- `why-dify-over-custom-rag.md`
- `monolith-first-architecture.md`
- `typescript-over-javascript.md`
- `postgres-over-mongodb.md`

## Anti-Patterns to Avoid

❌ Making decisions without documenting them
❌ Not including upgrade triggers
❌ Missing trade-off analysis
❌ No review dates for major decisions

## Review Cadence

- **Monthly**: Review decisions with ship_factor >= 8
- **Quarterly**: Review all active decisions
- **Yearly**: Archive deprecated decisions