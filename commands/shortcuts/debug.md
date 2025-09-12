---
title: Enable Debug Mode
type: command
subtype: shortcut
tags: [debug, verbose, troubleshooting]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
active: true
aliases: [!verbose, !trace, !diag]
---

# !debug - Enable Debug Mode

## Purpose
Activate verbose debug output for troubleshooting.

## Syntax
```
!debug <on|off> <level>
```

## Parameters
- `<on|off>`: Toggle debug mode (default: on)
- `<level>`: Debug level 1-5 (default: 3)

## Action

1. **Enable Verbose Output**: Show detailed processing
2. **Log Everything**: Track all operations
3. **Show Internals**: Expose internal state
4. **Trace Execution**: Step-by-step flow

## Examples

### Enable Debug
```
User: !debug

Bot: 🐛 Debug Mode ENABLED (Level 3)
    - Verbose output: ON
    - Execution trace: ON
    - State inspection: ON
    - Performance timing: ON
    Say !debug off to disable
```

### Maximum Verbosity
```
User: !debug on 5

Bot: 🐛 Debug Mode MAXIMUM
    - Every operation logged
    - Full stack traces
    - Memory snapshots
    - Network requests detailed
    ⚠️ Output will be very verbose
```

### Disable Debug
```
User: !debug off

Bot: Debug mode disabled
    Returning to normal output
```

## Debug Levels

1. **Level 1**: Basic - Errors only
2. **Level 2**: Info - Key operations
3. **Level 3**: Debug - Detailed flow (default)
4. **Level 4**: Trace - All function calls
5. **Level 5**: Everything - Maximum verbosity

## Output Format

```
[DEBUG L3] Operation: search_knowledge
  Input: {query: "docker", type: null}
  Files searched: 47
  Matches found: 3
  Time: 123ms
  Memory: +2.3MB
  Result: [array of 3 items]
```

## Side Effects

- Slower responses (more processing)
- Larger output (more text)
- Exposes internal structure
- May reveal sensitive paths

## Auto-Disable

- After 30 minutes
- After 100 messages
- On any error
- On !debug off

## Options

```
!debug -time     # Show timing only
!debug -memory   # Show memory only
!debug -network  # Show API calls only
!debug -quiet    # Minimal debug
```