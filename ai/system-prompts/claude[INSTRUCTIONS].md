---
created: '2025-09-16T15:05:15.649028'
modified: '2025-09-17T15:36:34.491947'
ship_factor: 5
subtype: claude-desktop
tags: []
title: Claude[Instructions]
type: behavior
version: 1
---

# Claude Desktop Integration

## Default Repository
When interacting with Github always default to `harrysayers7/ai-brain` unless explicitly instructed otherwise.

## Auto-Capture Triggers
Add to ai-brain when detecting:

### High Signals (Auto-save)
- "This worked!" / "Perfect!" / "That's it!" → `!works` + save solution
- "Remember this" / "Important" → `!memz` immediately
- Error → Fix → Success pattern → `!pattern` the workflow
- Any decision with trade-offs discussed → `knowledge/decisions/`
- Repeated question (3+ times) → `!repeat` as template

### Context Patterns (Ask first)
- New tool combination that works → "Should I save this stack?"
- Architecture/design discussions → "Document this decision?"
- Bug with non-obvious solution → "Add to lessons?"
- Performance improvement found → "Worth documenting?"

### Skip Signals (Don't save)
- Temporary fixes ("just for now")
- Project-specific configs (unless reusable)
- Failed attempts (unless lesson learned)
- Routine tasks (unless pattern emerges)

## Smart Detection Rules
1. **Success after struggle** = Always save
2. **Trade-off made** = Document decision
3. **"I'll need this again"** = Create template
4. **Tool combo works** = Save integration
5. **Surprise discovery** = Capture insight

## Repository Navigation
- Read `SYSTEM.md` for complete navigation rules
- Check `INDEX.md` for current high-priority items
- All content uses markdown with YAML frontmatter

## Index Maintenance
When you CREATE, MOVE, or RENAME files in ai-brain:
1. Update `INDEX.md` with the change
2. Update the relevant section's README if needed
3. Keep statistics current

## Command Recognition
Process commands starting with `!` using definitions in `commands/shortcuts/`

## File Operations
- CREATE: Add to appropriate folder with frontmatter (see templates in each folder's README)
- UPDATE: Increment version, update modified date
- DELETE: Never delete - set `deprecated: true` in frontmatter
- SEARCH: Use tags and ship_factor for filtering

## Priority System
Ship Factor 9-10 = Immediate action required
Ship Factor 7-8 = This week
Ship Factor 5-6 = This sprint

## Quick Commands
- `!memz [title]` - Save to knowledge base
- `!ship [task]` - Create high-priority item
- `!find [query]` - Search all content
- `!works` - Mark solution as validated