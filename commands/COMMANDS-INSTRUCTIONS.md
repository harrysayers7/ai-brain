---
created: '2025-09-16T15:05:15.616399'
modified: '2025-09-16T15:05:51.700734'
ship_factor: 5
subtype: COMMANDS-INSTRUCTIONS.md
tags: []
title: Commands Instructions
type: general
version: 1
---

# Command System Instructions

## How Commands Work

Commands start with `!` and trigger specific actions in the AI Brain repository.

## Basic Usage
```
!command [parameters]
```

## Command Structure
- `/shortcuts/` - Quick action commands (!memz, !ship, !find)
- `/templates/` - Reusable prompt templates 
- `/macros/` - Multi-step command sequences

## Processing Flow
1. User types command starting with `!`
2. Check command definition in appropriate folder
3. Execute defined action (create/update files)
4. Update INDEX.md if needed
5. Confirm completion

## Creating Commands
Add markdown file in appropriate folder with:
- Purpose
- Syntax
- Parameters
- Action to execute
- Examples

Commands auto-create entries with proper frontmatter and update indexes.