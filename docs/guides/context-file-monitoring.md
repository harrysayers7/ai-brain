---
created: '2025-09-17T16:30:00.000000'
modified: '2025-09-18T06:32:12.386821'
ship_factor: 9
subtype: guide
tags:
- automation
- monitoring
- context
- documentation
title: Context File Monitoring Automation
type: guide
version: 1
---

# Context File Monitoring Automation

This guide explains the automated system for tracking and documenting changes to context files in the AI Brain system.

## Overview

The context file monitoring system automatically tracks changes to:
- `ai/context/infrastructure.md`
- `ai/context/tech-stack.md`

When changes are detected, the system:
1. Updates the CHANGELOG.md with detailed change information
2. Creates a summary of the changes
3. Sends notifications (if configured)
4. Tracks file state for future comparisons

## Quick Start

### 1. Setup (One-time)
```bash
# Run the setup script
./scripts/setup-context-monitoring.sh
```

### 2. Manual Monitoring
```bash
# Check for changes
make monitor-context

# Watch for changes continuously
make watch-context

# Run full update cycle (includes context monitoring)
make update
```

### 3. Automatic Monitoring
The system automatically runs when:
- You commit changes (via git hooks)
- You run `make update`
- You run `make post-commit`

## Components

### 1. Context Monitor (`scripts/context-monitor.py`)
- Monitors file changes using MD5 hashing
- Tracks metadata (version, ship factor, size, etc.)
- Generates changelog entries
- Creates update summaries

### 2. Context Notifier (`scripts/context-notifier.py`)
- Sends notifications about changes
- Supports multiple notification methods
- Configurable notification preferences

### 3. Git Hooks (`scripts/git-hooks/post-commit-context`)
- Automatically runs on git commits
- Only processes commits that modify context files
- Integrates with existing git workflow

### 4. Makefile Integration
- `make monitor-context`: Check for changes
- `make watch-context`: Continuous monitoring
- `make update`: Full update cycle (includes monitoring)

## Configuration

### State Tracking
The system maintains state in `.context-monitor-state.json`:
```json
{
  "infrastructure": {
    "hash": "abc123...",
    "metadata": {
      "title": "Infrastructure Context",
      "version": 2,
      "ship_factor": 8,
      "size": 570,
      "lines": 11
    },
    "last_checked": "2025-09-17T16:30:00"
  }
}
```

### Notification Configuration
Configure notifications in `.context-notifier-config.json`:
```json
{
  "notifications": {
    "console": true,
    "file": true,
    "email": false,
    "webhook": false
  },
  "email": {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "username": "",
    "password": "",
    "from_email": "",
    "to_emails": []
  },
  "webhook": {
    "url": "",
    "headers": {},
    "timeout": 30
  }
}
```

## Notification Setup

### Console Notifications (Default)
Already enabled by default - shows changes in terminal.

### File Logging (Default)
Logs all changes to `context-updates.log`.

### Email Notifications
```bash
python3 scripts/context-notifier.py --setup-email
```

### Webhook Notifications
```bash
python3 scripts/context-notifier.py --setup-webhook
```

### Enable/Disable Notifications
```bash
# Enable specific notification type
python3 scripts/context-notifier.py --enable console
python3 scripts/context-notifier.py --enable file
python3 scripts/context-notifier.py --enable email
python3 scripts/context-notifier.py --enable webhook

# Disable specific notification type
python3 scripts/context-notifier.py --disable file
```

## Generated Files

### CHANGELOG.md
Automatically updated with context file changes:
```markdown
## Context Updates - 2025-09-17 16:29:05

### Infrastructure Context
- **File**: `ai/context/infrastructure.md`
- **Title**: Infrastructure Context
- **Version**: 1 → 2
- **Ship Factor**: 5 → 8
- **Size**: 0 → 570 bytes
- **Lines**: 1 → 11
- **Significant Changes**: version bump, ship factor change, significant content change
```

### CONTEXT-UPDATE-SUMMARY.md
Latest update summary:
```markdown
# Context Files Update Summary
*Generated: 2025-09-17 16:29:05*

## Infrastructure
- **File**: `ai/context/infrastructure.md`
- **Title**: Infrastructure Context
- **Version**: 2
- **Ship Factor**: 8
- **Size**: 570 bytes
- **Lines**: 11
```

### context-updates.log
Detailed log of all changes:
```
2025-09-17T16:29:05

🔔 Context Files Updated
📅 2025-09-17 16:29:05

📝 **Infrastructure**
   File: `ai/context/infrastructure.md`
   Title: Infrastructure Context
   Version: 2
   Ship Factor: 8
   Size: 570 bytes

--------------------------------------------------
```

## Usage Examples

### Daily Workflow
```bash
# 1. Make changes to context files
vim ai/context/infrastructure.md

# 2. Check what changed
make monitor-context

# 3. Commit changes (automatically triggers monitoring)
git add ai/context/infrastructure.md
git commit -m "Update infrastructure context"

# 4. View changelog
cat CHANGELOG.md | head -20
```

### Continuous Monitoring
```bash
# Start watching for changes
make watch-context

# In another terminal, make changes
echo "## New Section" >> ai/context/infrastructure.md

# Watch terminal will show changes automatically
```

### Manual Testing
```bash
# Test notification system
python3 scripts/context-notifier.py --test

# Force update state (useful for initial setup)
python3 scripts/context-monitor.py --force-update
```

## Troubleshooting

### Common Issues

#### 1. "Module not found" errors
```bash
# Make sure you're using the virtual environment
source venv/bin/activate
python3 scripts/context-monitor.py
```

#### 2. Git hooks not working
```bash
# Reinstall git hooks
cp scripts/git-hooks/post-commit-context .git/hooks/post-commit
chmod +x .git/hooks/post-commit
```

#### 3. Notifications not working
```bash
# Check configuration
cat .context-notifier-config.json

# Test notifications
python3 scripts/context-notifier.py --test
```

#### 4. State file issues
```bash
# Reset state (will re-detect all files)
python3 scripts/context-monitor.py --force-update
```

### Debug Mode
```bash
# Run with verbose output
python3 -u scripts/context-monitor.py 2>&1 | tee context-monitor.log
```

## Advanced Configuration

### Custom Context Files
To monitor additional files, edit `scripts/context-monitor.py`:
```python
self.context_files = {
    'infrastructure': self.root / 'ai' / 'context' / 'infrastructure.md',
    'tech-stack': self.root / 'ai' / 'context' / 'tech-stack.md',
    'custom-file': self.root / 'path' / 'to' / 'custom.md'  # Add this
}
```

### Custom Notification Templates
Edit `scripts/context-notifier.py` to customize notification formats.

### Integration with CI/CD
Add to your CI pipeline:
```yaml
- name: Monitor Context Files
  run: |
    source venv/bin/activate
    python3 scripts/context-monitor.py
```

## Best Practices

1. **Always use the virtual environment** when running scripts
2. **Commit context file changes** to trigger automatic monitoring
3. **Review generated changelog entries** before pushing
4. **Configure notifications** for important changes
5. **Keep state files in version control** (`.context-monitor-state.json`)
6. **Test the system** after making configuration changes

## Related Files

- `scripts/context-monitor.py` - Main monitoring script
- `scripts/context-notifier.py` - Notification system
- `scripts/setup-context-monitoring.sh` - Setup script
- `scripts/git-hooks/post-commit-context` - Git hook
- `Makefile` - Integration with build system
- `.context-monitor-state.json` - State tracking
- `.context-notifier-config.json` - Notification config
- `CHANGELOG.md` - Generated changelog
- `CONTEXT-UPDATE-SUMMARY.md` - Latest summary
- `context-updates.log` - Detailed log