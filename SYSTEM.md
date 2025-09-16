# AI Brain Navigation System

You have access to a knowledge base organized as markdown files. This document defines how to navigate and use this system.

## Structure Convention

- All files are markdown with YAML frontmatter
- Paths indicate type and purpose:
  - `knowledge/decisions/` = architectural and technical decisions
  - `knowledge/lessons/` = learned experiences and anti-patterns
  - `knowledge/references/` = quick reference guides and cheat sheets
  - `prompts/personas/` = AI personality definitions
  - `prompts/modes/` = operational modes (e.g., debug, production)
  - `systems/workflows/` = step-by-step processes
  - `systems/rules/` = governance and constraints
  - `tools/integrations/` = external tool configurations
- Newer files override older ones (check `modified` date in frontmatter)
- References use relative paths: `[link text](knowledge/decisions/example.md)`

## Reading Files

1. **Check INDEX.md first** for quick lookups and navigation
2. **Navigate by path**: `category/subcategory/filename.md`
3. **Parse frontmatter** for metadata (YAML between `---` markers)
4. **Use tags** for cross-references and semantic search
5. **Check deprecated status** before using any content

## CRUD Operations

### CREATE
- Add to appropriate folder based on content type
- Include complete frontmatter (see schema below)
- Update INDEX.md with reference to new file
- Use descriptive, kebab-case filenames

### READ
- Access directly by path
- Search by tags in frontmatter
- Use INDEX.md for categorized browsing
- Check `ship_factor` for implementation priority

### UPDATE
- Increment `version` in frontmatter
- Update `modified` timestamp
- Keep change history in content if significant
- Update INDEX.md if title or priority changes

### DELETE
- Set `deprecated: true` in frontmatter
- Add `deprecated_date` and `deprecated_reason`
- DO NOT remove files (maintain history)
- Update INDEX.md to show deprecation

## Frontmatter Schema

```yaml
title: Human-readable title (required)
type: knowledge|behavior|system|tool (required)
subtype: specific subcategory (required)
tags: [searchable, tags, here] (required)
created: ISO-8601 date (required)
modified: ISO-8601 date (required)
version: integer starting at 1 (required)
ship_factor: 1-10 scale (10 = ship immediately)
deprecated: boolean (default: false)
deprecated_date: ISO-8601 date (if deprecated)
deprecated_reason: explanation (if deprecated)
supersedes: path/to/previous/version.md
references: 
  - relative/path/to/related.md
  - another/related/file.md
```

## Priority Rules

1. **Ship Factor Scale**:
   - 9-10: Implement immediately, blocking issue
   - 7-8: High priority, implement this week
   - 5-6: Normal priority, implement this sprint
   - 3-4: Low priority, nice to have
   - 1-2: Future consideration, research only

2. **Deprecated Content**: 
   - Files with `deprecated: true` should be ignored
   - Check `supersedes` field for replacement

3. **Version Conflicts**:
   - Use highest version number when multiple exist
   - Check `modified` date as tiebreaker

## Quick Lookup Patterns

- **Recent decisions**: Sort by `modified` in `knowledge/decisions/`
- **High-priority items**: Search for `ship_factor: [8-10]`
- **Anti-patterns**: Check `knowledge/lessons/` with tag `anti-pattern`
- **Active workflows**: `systems/workflows/` where `deprecated: false`
- **Current tech stack**: `tools/integrations/` with tag `active`

## Naming Conventions

### File Names
- Use kebab-case: `why-we-chose-dify.md`
- Be descriptive but concise
- Include date for time-sensitive content: `2024-q1-roadmap.md`
- Avoid generic names: use `react-component-structure.md` not `structure.md`

### Folder Organization
- Keep hierarchy shallow (max 3 levels)
- Group by function, not by project
- Use plural for folder names: `decisions` not `decision`

## Content Guidelines

### Decision Documents
- Include: Context, Decision, Reasoning, Trade-offs, Upgrade triggers
- Tag with: technology names, architectural patterns
- Reference: related decisions, lessons learned

### Lesson Documents
- Include: What happened, What we learned, What to do instead
- Tag with: `lesson`, `anti-pattern` (if applicable)
- Reference: decisions that led to this lesson

### Workflow Documents
- Include: Prerequisites, Steps, Validation, Rollback procedure
- Tag with: frequency (`daily`, `weekly`), area (`deployment`, `review`)
- Reference: tools used, related workflows

## Integration Notes

### For Dify
- Point to this folder as knowledge base
- Use tags for retrieval filtering
- Ship factor becomes relevance score

### For MCP Servers
- Read SYSTEM.md first for context
- Use INDEX.md for navigation
- Parse frontmatter before content

### For Human Editors
- Edit with any text editor
- Compatible with Obsidian, VS Code, etc.
- Preview supported on GitHub

## Changelog Management

### Automatic Updates
- **On every git commit**: Update CHANGELOG.md with changes
- **Format**: Use [Keep a Changelog](https://keepachangelog.com/) format
- **Timestamp**: Include ISO-8601 timestamp for each entry
- **Categories**: Added, Changed, Deprecated, Removed, Fixed, Security

### Changelog Entry Template
```markdown
## [Unreleased]

### Added
- [Timestamp: YYYY-MM-DDTHH:MM:SSZ] Description of new feature

### Changed
- [Timestamp: YYYY-MM-DDTHH:MM:SSZ] Description of change

### Fixed
- [Timestamp: YYYY-MM-DDTHH:MM:SSZ] Description of bug fix
```

### Git Hook Integration
- Pre-commit hook: Validate changelog format
- Post-commit hook: Auto-update changelog with commit details
- Commit message parsing: Extract change type from conventional commits

## Maintenance Tasks

### Daily
- Update INDEX.md with new additions
- Check for deprecated items past expiry
- Verify changelog is updated with recent changes

### Weekly
- Review high ship factor items
- Archive completed decisions
- Update tool configurations
- Consolidate changelog entries

### Monthly
- Consolidate duplicate knowledge
- Update deprecated references
- Review and clean up tags
- Release new version and update changelog