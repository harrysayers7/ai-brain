# Commands

Shortcut commands for fast LLM interaction and knowledge capture.

## Structure

- **shortcuts/** - Quick action commands
- **templates/** - Reusable prompt templates
- **macros/** - Multi-step command sequences

## Command Syntax

All commands start with `!` and can include parameters:
```
!command [required] <optional> {context}
```

## Quick Reference

### Memory & Learning
- `!memz` - Save this pattern to memory
- `!pattern` - Log this workflow pattern
- `!works` - This solution worked well
- `!repeat` - Save as frequently used template
- `!tool` - Log successful tool combination
- `!insight` - Important learning to remember
- `!fail` - Document what didn't work
- `!til` - Today I learned

### Action Commands
- `!ship` - Create high-priority decision
- `!decide` - Document a decision
- `!todo` - Add to task list
- `!block` - Document a blocker
- `!fix` - Document a solution
- `!debug` - Start debug mode
- `!explain` - Explain like I'm 5

### Navigation
- `!find` - Search knowledge base
- `!recent` - Show recent entries
- `!high` - Show high priority items
- `!deps` - Show deprecated items
- `!stats` - Show statistics

### Tool Commands
- `!dify` - Dify-specific command
- `!git` - Git workflow command
- `!api` - API integration command
- `!test` - Testing command
- `!deploy` - Deployment command

## Command Processing

When an LLM sees a command:
1. Parse command and parameters
2. Execute associated action
3. Create/update appropriate files
4. Confirm completion

## Creating Custom Commands

1. Add to `shortcuts/` with clear documentation
2. Define parameters and defaults
3. Include examples
4. Update this README

## Integration

### With Dify
```python
# Command processor for Dify
if message.startswith('!'):
    process_command(message)
```

### With Claude/GPT
```
System: You recognize ! commands and process them according to commands/shortcuts/
```

### With MCP Servers
```javascript
// Intercept commands
if (input[0] === '!') {
  return handleCommand(input);
}
```