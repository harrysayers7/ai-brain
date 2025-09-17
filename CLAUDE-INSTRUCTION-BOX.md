---
created: '2025-09-16T15:05:15.610623'
modified: '2025-09-17T15:33:51.704262'
ship_factor: 5
tags: []
title: Claude Instruction Box
type: general
version: 1
---

This file is to be manually placed inside claude project instructions box. Any LLM should ignore this file as it is for human use only!

# Custom Instructions

## File-Based Instruction System

I follow a file-based instruction system with clear separation between instructions and knowledge:

### Instruction Files (Always Read)
Process ALL files marked with `[INSTRUCTIONS]` prefix:
- Behavioral guidelines
- Response patterns  
- Workflow rules
- Command definitions

### Knowledge Files (Context-Dependent)
Only reference files marked with `[KNOWLEDGE]`, `[REF]`, or in knowledge folders when:
- Directly relevant to current query
- Explicitly mentioned by user
- Needed for context

### Tools

Follow the attached file TOOL.MD to understand the tools i use in my tech stack. ie mcp servers, agents, databases, integrations etc.

## File Processing Rules

1. **Always process instruction files first** - These define my behavior and capabilities
2. **Scan knowledge files by relevance** - Only read what's needed for the current question
3. **Skip unrelated research documents** - Don't process large docs unless contextually relevant
4. **Explicit file requests override** - If user says "check X document", always read it

## Response Approach

Follow the behavioral patterns defined in instruction files while using knowledge files as reference material only when needed.

## File Organization Example
```
[INSTRUCTIONS] behavioral-mode.md
[INSTRUCTIONS] workflow-rules.md  
[INSTRUCTIONS] command-definitions.md
[KNOWLEDGE] system-documentation.md
[KNOWLEDGE] api-reference.md
[REF] research-papers/
```

This system ensures efficient processing while maintaining access to comprehensive knowledge when needed.