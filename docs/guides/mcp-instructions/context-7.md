---
created: '2025-09-16T15:05:15.654856'
modified: '2025-09-17T17:15:05.747107'
ship_factor: 5
subtype: mcp-instructions
tags: []
title: Context 7
type: general
version: 1
---

## Context7 MCP Usage Instructions

### When to Use Context7
- Before implementing unfamiliar libraries/frameworks
- When encountering new APIs or methods
- For troubleshooting current issues
- Before suggesting alternatives

### Pre-Flight Checks
1. **Verify library exists** - Check if library is in Context7 database
2. **Check project dependencies** - Ensure library is actually installed
3. **Identify specific version** - Match Context7 docs to project version

### Intelligent Usage Pattern
1. **Resolve library ID first** - Use `resolve-library-id` with specific library name
2. **Handle failures gracefully** - If library not found, suggest alternatives or manual research
3. **Use targeted topics** - Start with specific topics, expand if needed
4. **Optimize token usage** - Start with 3000-5000 tokens, increase only if needed
5. **Validate against project** - Cross-reference with existing codebase patterns

### Error Handling
- **Library not found**: Suggest manual research or alternative libraries
- **Topic not found**: Try broader topics or related terms
- **Version mismatch**: Flag potential compatibility issues
- **Conflicting info**: Present both options with context

### Quality Assurance
- Always verify examples work with current project setup
- Flag any version-specific code that might not work
- Provide fallback options when Context7 info is insufficient
- Cross-reference with official documentation when possible