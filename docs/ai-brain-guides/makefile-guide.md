---
created: '2025-09-17T16:45:00.000000'
modified: '2025-09-18T06:32:12.386272'
ship_factor: 8
subtype: guide
tags:
- commands
- updates
- automation
- quick-reference
title: Update Commands Guide
type: guide
version: 1
---

# AI Brain Update Commands

Quick reference for keeping your AI Brain system updated.

## Main Commands

### `make update`
**Full system update** - Runs everything in the right order
- Updates frontmatter, INDEX.md, context files, SYSTEM.md
- Validates everything
- **What it does**: This now automatically syncs context files with their source directories
- **Use when**: Setting up or after major changes

### `make integrated-update` 
**Coordinated update** - Same as `make update` but more explicit
- Efficient shared analysis
- Only updates what's needed
- **Use when**: You want the full coordinated experience

### `make quick-update`
**Fast update** - Only recent changes
- Skips unnecessary work
- **Use when**: You just made small changes

## Individual Components

### `make sync-index`
Updates INDEX.md with current file structure

### `make update-system` 
Updates SYSTEM.md based on current codebase

### `make monitor-context`
Checks for context file changes and updates changelog

### `make sync-context`
Synchronizes context files with their source directories
- **What it does**: Automatically syncs context files with their source directories
- **Use when**: You want to update context files without running the full update process

### `make update-frontmatter`
Updates frontmatter in all markdown files

## Python Scripts

### `python3 scripts/context-sync.py --check`
**Check sync status** - Verifies if context synchronization is needed
- **What it does**: Check if sync is needed without actually performing the sync
- **Use when**: You want to verify if context files are up to date before running a full sync

## When to Use What

- **Daily work**: `make quick-update`
- **After adding files**: `make update`
- **After restructuring**: `make integrated-update`
- **Just context changes**: `make monitor-context`
- **Just documentation**: `make update-system`

## Setup

One-time setup:
```bash
./scripts/setup-auto-documentation.sh
```

That's it! The system handles the rest automatically.