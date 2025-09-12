# Knowledge Base

This directory contains all accumulated knowledge, decisions, and learnings.

## Structure

- **decisions/** - Architectural and technical decisions with rationale
- **lessons/** - Things we've learned (often the hard way)
- **references/** - Quick reference guides and cheat sheets

## Creating Knowledge Documents

All knowledge documents should answer:
- **What** was decided/learned?
- **Why** was this the choice?
- **When** should this apply?
- **How** do we implement it?

## Template

```markdown
---
title: Clear, Descriptive Title
type: knowledge
subtype: decision|lesson|reference
tags: [relevant, searchable, tags]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
ship_factor: 1-10
deprecated: false
---

# Title

## Summary
One-line summary for quick scanning.

## Context
Why this knowledge matters.

## Details
The actual knowledge content.

## Action Items
What to do with this knowledge.
```

## Ship Factor Guidelines

- **9-10**: Critical knowledge affecting current work
- **7-8**: Important for this week's deliverables
- **5-6**: Relevant for current sprint
- **3-4**: Good to know
- **1-2**: Archive/historical