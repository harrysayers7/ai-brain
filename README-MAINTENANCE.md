---
created: '2025-09-16T15:05:51.699059'
modified: '2025-09-17T16:14:24.422346'
ship_factor: 5
tags: []
title: Readme Maintenance
type: general
version: 1
---

# AI Brain Maintenance System - Quick Reference

## 🚀 Quick Start

```bash
# 1. Setup (one-time)
./setup.sh

# 2. Run maintenance
make update

# 3. Check status
make stats
```

## 📋 Common Commands

| Command | What it does |
|---------|-------------|
| `make update` | Full update cycle (index + frontmatter + validate) |
| `make validate` | Check all files for issues |
| `make stats` | Show repository statistics |
| `make sync-index` | Update INDEX.md with current structure |
| `make update-frontmatter` | Add/update frontmatter in all files |
| `make test` | Run all tests |
| `make help` | Show all available commands |

## 🔄 Git Integration

The system automatically runs maintenance tasks when you commit:

- **Pre-commit**: Validates files before allowing commit
- **Post-commit**: Updates INDEX.md, frontmatter, and changelog

## 🛠️ Manual Maintenance

```bash
# Using Python helper directly
source venv/bin/activate
python3 utils/brain_helper.py sync-index
python3 utils/brain_helper.py update-frontmatter
python3 utils/brain_helper.py validate

# Using Makefile
make update
make validate
make stats
```

## 📁 What Gets Updated

### INDEX.md
- Auto-generated from current file structure
- Organized by category (Knowledge, Tools, Systems, etc.)
- Links to all markdown files
- Updated on every commit

### Frontmatter
- Added to all markdown files missing it
- Updated with current timestamps
- Categorized by file location
- Ensures consistency across the knowledge base

### CHANGELOG.md
- Updated with commit messages
- Categorized by change type (Added, Fixed, Changed, etc.)
- Includes timestamps and commit hashes

## 🔍 Troubleshooting

### Dependencies Missing
```bash
source venv/bin/activate
pip install python-frontmatter pyyaml
```

### Git Hooks Not Working
```bash
chmod +x .git/hooks/*
```

### Validation Errors
```bash
make validate  # See specific errors
make format    # Fix formatting issues
```

### Reset Everything
```bash
make emergency-reset  # Reset to last commit
```

## 📊 Current Status

Run `make stats` to see:
- Total files in the knowledge base
- Files by category
- High priority items (ship_factor 8+)
- Deprecated items

## 🎯 Best Practices

1. **Run `make update` regularly** to keep files synchronized
2. **Use `make validate` before committing** to catch issues early
3. **Check `make stats`** to monitor repository health
4. **Use descriptive commit messages** for better changelog generation
5. **Keep frontmatter consistent** across all files

---

*This system keeps your AI Brain knowledge base organized and consistent automatically.*