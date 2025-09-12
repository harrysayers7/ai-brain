---
title: Log Tool Combination
type: command
subtype: shortcut
tags: [tools, integration, stack]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
active: true
aliases: [!stack, !combo, !integration]
---

# !tool - Log Successful Tool Combination

## Purpose
Document a successful combination of tools or integrations that work well together.

## Syntax
```
!tool [tools] <purpose> {config}
```

## Parameters
- `tools`: Tool names separated by + (required)
- `<purpose>`: What this combination achieves
- `{config}`: Configuration details (from context)

## Action

1. **Document Stack**: Create integration reference
2. **Save Config**: Store working configuration
3. **Link Tools**: Update individual tool docs
4. **Create Recipe**: Generate setup guide

## Examples

### Simple Tool Combo
```
User: Dify + Supabase + n8n works perfectly for this!
User: !tool

Bot: ✅ Tool combination saved
    Created: tools/integrations/dify-supabase-n8n-stack.md
    Purpose: [extracted from context]
    Config: [captured from discussion]
```

### With Purpose
```
User: !tool "claude+github+mcp" "AI-powered code review"

Bot: ✅ Integration documented
    File: tools/integrations/ai-code-review-stack.md
    Components: 3 tools
    Setup guide: Generated
    Related workflows: code-review-process.md
```

### With Configuration
```
User: !tool "postgres+redis" "caching layer" "redis for session, pg for persistent"

Bot: ✅ Stack configuration saved
    Includes: Connection settings, use cases, performance notes
```

## Generated Documentation

```markdown
---
title: [Tool1 + Tool2 + Tool3] Stack
type: tool
subtype: integration
tags: [stack, tools, purpose]
---

# [Combined Tool Name] Stack

## Components
- Tool 1: [Role]
- Tool 2: [Role]
- Tool 3: [Role]

## Purpose
[What this combination achieves]

## Configuration
[Working config extracted]

## Setup Steps
1. Configure Tool 1
2. Connect Tool 2
3. Integrate Tool 3

## Validation
- [ ] Connection test
- [ ] Data flow verified
- [ ] Performance acceptable

## Benefits
- [Why this combo works]

## Trade-offs
- [Limitations or concerns]
```

## Integration Tracking

- Links to individual tool configs
- Tracks version compatibility
- Documents breaking changes
- Suggests alternatives

## Options

```
!tool -config    # Include detailed config
!tool -minimal   # Just tool names
!tool -recipe    # Generate setup guide
```