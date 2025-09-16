---
created: '2025-09-16T15:05:15.643892'
modified: '2025-09-16T19:19:40.880556'
ship_factor: 5
subtype: shortcuts
tags: []
title: Instructions
type: general
version: 1
---

# ! Command Instructions for LLMs

When user types `!` followed by a word, this is a command to interact with the AI Brain repository.

## How to Handle ! Commands

1. **Recognize**: `!memz`, `!ship`, `!find`, etc.
2. **Action**: Create/update files in harrysayers7/ai-brain
3. **Location**: Add to appropriate folder based on command type
4. **Format**: Use frontmatter template from folder's README
5. **Update**: Modify INDEX.md to reflect changes

## Example
User: "!memz Docker fix worked"
→ Create: `knowledge/lessons/docker-fix.md` with proper frontmatter
→ Update: INDEX.md statistics and recent items