# Prompts

AI prompt configurations including personas and operational modes.

## Structure

- **personas/** - AI personality configurations
- **modes/** - Context-specific operational modes

## Purpose

Define how AI assistants should respond in different contexts:
- Personality traits (helpful, skeptical, creative)
- Communication style (formal, casual, technical)
- Decision-making approaches (conservative, aggressive, balanced)
- Domain expertise (developer, business analyst, coach)

## Usage with LLMs

When invoking an AI assistant:
1. Select appropriate persona for the task
2. Apply relevant operational mode
3. Combine with domain knowledge from `/knowledge`

## Template

```markdown
---
title: Prompt Name
type: prompt
subtype: persona|mode
tags: [relevant, tags]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
ship_factor: 1-10
---

# Prompt Name

## Role
One-line description of this prompt.

## Characteristics
- Key trait 1
- Key trait 2
- Key trait 3

## Instructions
Specific instructions for the AI.

## Examples
Sample interactions or responses.

## When to Use
Contexts where this prompt is appropriate.

## When NOT to Use
Contexts where this prompt should be avoided.
```