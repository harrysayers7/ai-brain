---
created: '2025-09-17T16:12:32.908191'
modified: '2025-09-17T16:14:24.422116'
ship_factor: 5
tags: []
title: Maintenance
type: general
version: 1
---

# AI Brain Maintenance Guide

This document outlines maintenance procedures to keep the AI Brain system functioning properly.

## Automatic Maintenance

The system includes several automatic maintenance features:

### 1. INDEX.md Auto-Generation
- **Command**: `make sync-index`
- **Purpose**: Automatically generates INDEX.md from current directory structure
- **Trigger**: Run after any major directory restructuring
- **How it works**: The `brain_helper.py` script now **dynamically discovers** all top-level directories instead of using hardcoded lists

### 2. Frontmatter Updates
- **Command**: `make update-frontmatter`
- **Purpose**: Ensures all markdown files have proper frontmatter
- **Trigger**: Run when adding new files or changing structure

### 3. Validation
- **Command**: `make validate`
- **Purpose**: Checks for structural issues and missing required fields
- **Trigger**: Run before committing major changes

## When to Run Maintenance

### After Directory Changes
```bash
# After creating new top-level directories
make sync-index

# After moving files between directories
make sync-index

# After adding new files
make update-frontmatter
```

### Before Commits
```bash
# Full validation before committing
make validate
make sync-index
```

### Regular Maintenance
```bash
# Weekly maintenance
make format
make lint
make validate
```

## Critical Maintenance Rules

### 1. Never Hardcode Directory Names
- The `brain_helper.py` script now **dynamically discovers** directories
- This prevents the INDEX.md from becoming outdated when structure changes
- **If you modify `brain_helper.py`**: Always use dynamic discovery, never hardcode directory lists

### 2. Always Test After Structure Changes
- Run `make sync-index` after any directory restructuring
- Verify INDEX.md includes all expected files
- Check that new directories appear in the index

### 3. Keep Frontmatter Consistent
- All markdown files should have proper frontmatter
- Use `make update-frontmatter` to fix missing fields
- Follow the frontmatter template in `ai/rules/README.md`

## Troubleshooting

### INDEX.md Missing Files
1. Check if new directories are being discovered:
   ```bash
   python3 utils/brain_helper.py stats
   ```
2. Run sync-index:
   ```bash
   make sync-index
   ```
3. If still missing, check `brain_helper.py` for hardcoded exclusions

### Frontmatter Issues
1. Run frontmatter update:
   ```bash
   make update-frontmatter
   ```
2. Check for validation errors:
   ```bash
   make validate
   ```

### Structure Validation Failures
1. Check for missing required directories
2. Verify all markdown files have proper frontmatter
3. Run format and lint to fix common issues:
   ```bash
   make format
   make lint
   ```

## Prevention Measures

### 1. Dynamic Discovery
- The `sync_index()` function now uses `self.root.iterdir()` to discover directories
- No more hardcoded directory lists that become outdated
- Automatically adapts to new directory structures

### 2. Comprehensive Testing
- The `test()` function validates the entire system
- Run `make test` before major changes
- Ensures INDEX.md generation works correctly

### 3. Regular Validation
- Set up automated checks (if possible)
- Run maintenance commands regularly
- Monitor for structural drift

## Emergency Recovery

If the system becomes completely broken:

1. **Reset INDEX.md**:
   ```bash
   rm INDEX.md
   make sync-index
   ```

2. **Fix all frontmatter**:
   ```bash
   make update-frontmatter
   ```

3. **Validate and fix**:
   ```bash
   make validate
   make format
   make lint
   ```

4. **Full system test**:
   ```bash
   make test
   ```

## Notes

- The system is designed to be **self-maintaining** through dynamic discovery
- Manual intervention should only be needed for major structural changes
- Always test after making changes to `brain_helper.py`
- Keep this document updated when adding new maintenance procedures