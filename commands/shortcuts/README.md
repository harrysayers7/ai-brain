# Command Shortcuts

Quick commands for common LLM interactions.

## Command Template

```markdown
---
title: Command Name
type: command
subtype: shortcut
tags: [command, category]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
active: true
---

# !command

## Purpose
What this command does.

## Syntax
```
!command [required] <optional> {context}
```

## Parameters
- `required`: Description
- `<optional>`: Description (default: value)

## Action
1. What happens when executed
2. Files created/modified
3. Response format

## Examples

### Basic Usage
```
!command example
```

### With Parameters
```
!command example optional-value
```

## Aliases
- `!cmd` - Shorter version
- `!c` - Shortest version
```

## Categories

### Memory Commands
For saving patterns and learnings:
- `memz.md` - Save to memory
- `pattern.md` - Log workflow pattern
- `works.md` - Document success
- `repeat.md` - Save frequent request
- `tool.md` - Log tool combination
- `insight.md` - Capture insight
- `fail.md` - Document failure
- `til.md` - Today I learned

### Action Commands
For creating content:
- `ship.md` - High-priority task
- `decide.md` - Create decision
- `todo.md` - Add task
- `block.md` - Document blocker
- `fix.md` - Document solution

### Query Commands
For finding information:
- `find.md` - Search knowledge
- `recent.md` - Recent items
- `high.md` - High priority
- `stats.md` - Statistics

### Mode Commands
For changing behavior:
- `debug.md` - Debug mode
- `verbose.md` - Detailed output
- `brief.md` - Concise output
- `expert.md` - Expert mode

## Implementation

### Command Parser
```python
def parse_command(input):
    parts = input.split()
    command = parts[0][1:]  # Remove !
    params = parts[1:]
    
    # Load command definition
    cmd_file = f'commands/shortcuts/{command}.md'
    
    # Execute action
    return execute(command, params)
```

### Response Format
```yaml
command: !memz
status: success
action: created
file: knowledge/lessons/new-pattern.md
message: "Pattern saved to memory"
```