---
created: '2025-09-16T15:05:15.614529'
modified: '2025-09-16T19:19:40.863262'
ship_factor: 5
tags: []
title: Maintenance
type: general
version: 1
---

# AI Brain Maintenance System

This document describes the automated maintenance system for the AI Brain knowledge base.

## Overview

The AI Brain maintenance system provides automated tools to keep your knowledge base organized, validated, and up-to-date. It includes:

- **Makefile**: Easy-to-use commands for maintenance tasks
- **Git Hooks**: Automatic updates on commit
- **Python Helper**: Core functionality for file management
- **Validation**: Ensures consistency and structure

## Quick Start

### 1. Initial Setup

```bash
# Run the setup script
./setup.sh

# Or manually install dependencies
pip3 install python-frontmatter pyyaml
make install
```

### 2. Basic Usage

```bash
# Run full update cycle
make update

# Validate all files
make validate

# Show help
make help
```

## Makefile Commands

### Core Commands

| Command | Description |
|---------|-------------|
| `make help` | Show all available commands |
| `make install` | Install dependencies and setup |
| `make update` | Run complete update cycle |
| `make validate` | Validate all files and structure |
| `make test` | Run tests and checks |

### Maintenance Commands

| Command | Description |
|---------|-------------|
| `make sync-index` | Update INDEX.md with current structure |
| `make update-frontmatter` | Update frontmatter in all files |
| `make format` | Format all markdown files |
| `make lint` | Lint files for issues |
| `make clean` | Clean temporary files |

### Development Commands

| Command | Description |
|---------|-------------|
| `make stats` | Show repository statistics |
| `make docs` | Generate documentation |
| `make backup` | Create backup of current state |
| `make watch` | Watch for changes and auto-update |

### Git Integration

| Command | Description |
|---------|-------------|
| `make pre-commit` | Run pre-commit checks |
| `make post-commit` | Run post-commit updates |

## Git Hooks

### Pre-Commit Hook

Runs automatically before each commit:
- Validates file structure
- Checks frontmatter consistency
- Runs linting checks
- Prevents commits with validation errors

### Post-Commit Hook

Runs automatically after each commit:
- Updates CHANGELOG.md
- Syncs INDEX.md with current structure
- Updates frontmatter in all files
- Validates changes

## Python Helper

The `utils/brain_helper.py` script provides core functionality:

### CLI Usage

```bash
# Sync index
python3 utils/brain_helper.py sync-index

# Update frontmatter
python3 utils/brain_helper.py update-frontmatter

# Validate files
python3 utils/brain_helper.py validate

# Run tests
python3 utils/brain_helper.py test

# Format files
python3 utils/brain_helper.py format

# Lint files
python3 utils/brain_helper.py lint

# Generate docs
python3 utils/brain_helper.py generate-docs
```

### Python API

```python
from utils.brain_helper import BrainHelper

# Initialize
brain = BrainHelper()

# Sync index
brain.sync_index()

# Update frontmatter
brain.update_frontmatter()

# Validate
if brain.validate():
    print("All files valid")

# Get statistics
stats = brain.get_statistics()
print(f"Total files: {stats['total_files']}")
```

## File Structure

```
ai-brain/
├── Makefile                 # Main maintenance commands
├── setup.sh                # Initial setup script
├── MAINTENANCE.md          # This documentation
├── scripts/                # Maintenance scripts
│   ├── update-index.sh
│   ├── update-frontmatter.sh
│   └── validate-files.sh
├── utils/
│   └── brain_helper.py     # Core Python helper
└── .git/hooks/             # Git hooks
    ├── pre-commit          # Pre-commit validation
    └── post-commit         # Post-commit updates
```

## Configuration

### Frontmatter Requirements

All markdown files should include:

```yaml
---
title: Document Title
type: knowledge|behavior|system|tool|general
subtype: specific category
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
ship_factor: 1-10
tags: [tag1, tag2]
---
```

### Directory Structure

The system expects these directories:
- `knowledge/` - Knowledge base content
- `prompts/` - AI behavior configurations
- `systems/` - System documentation
- `tools/` - Tool configurations
- `infrastructure/` - Infrastructure docs
- `commands/` - Command documentation
- `instructions/` - Instruction sets

## Troubleshooting

### Common Issues

1. **Python dependencies missing**
   ```bash
   pip3 install python-frontmatter pyyaml
   ```

2. **Git hooks not working**
   ```bash
   chmod +x .git/hooks/*
   ```

3. **Validation errors**
   ```bash
   make validate  # See specific errors
   make format    # Fix formatting issues
   ```

4. **INDEX.md not updating**
   ```bash
   make sync-index
   ```

### Debug Mode

Run individual components to debug:

```bash
# Test Python helper
python3 utils/brain_helper.py test

# Test specific functions
python3 utils/brain_helper.py validate
python3 utils/brain_helper.py sync-index

# Test git hooks manually
.git/hooks/pre-commit
.git/hooks/post-commit
```

## Customization

### Adding New File Types

1. Update `brain_helper.py` validation rules
2. Add to directory structure in `ensure_structure()`
3. Update INDEX.md generation logic

### Custom Validation Rules

Modify the `validate()` method in `brain_helper.py`:

```python
def validate(self):
    # Add your custom validation logic
    # Return True if valid, False if errors found
    pass
```

### Custom Update Scripts

Add new scripts to `scripts/` directory and update the Makefile:

```makefile
custom-task: ## Custom task description
	@echo "Running custom task..."
	@./scripts/custom-script.sh
```

## Best Practices

1. **Run `make update` regularly** to keep files synchronized
2. **Use `make validate` before committing** to catch issues early
3. **Check `make stats`** to monitor repository health
4. **Use descriptive commit messages** for better changelog generation
5. **Keep frontmatter consistent** across all files

## Integration with Other Tools

### VS Code

Add to your workspace settings:

```json
{
    "files.associations": {
        "*.md": "markdown"
    },
    "markdown.preview.breaks": true
}
```

### Obsidian

1. Open the ai-brain directory as a vault
2. Use the graph view to see relationships
3. Edit files with full markdown support

### Dify

1. Point your knowledge base to this repository
2. Use tags for filtering content
3. Use ship_factor for prioritization

## Contributing

When adding new features:

1. Update the Makefile with new commands
2. Add corresponding Python methods to `brain_helper.py`
3. Update this documentation
4. Test with `make test`
5. Update the changelog

## Support

For issues or questions:

1. Check the troubleshooting section
2. Run `make test` to identify problems
3. Check git hook logs for errors
4. Review the Python helper documentation

---

*This maintenance system is designed to keep your AI Brain knowledge base organized and consistent automatically.*