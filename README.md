# AI Brain - Second Brain Knowledge Base

> A human-readable, LLM-optimized knowledge management system using markdown and YAML frontmatter.

## 🎯 Purpose

This repository serves as a centralized knowledge base for AI-assisted development and decision-making. It's designed to be:

- **Human-readable**: Edit with any text editor
- **LLM-optimized**: Structured for AI consumption via CRUD operations
- **Git-friendly**: Track changes and collaborate
- **Tool-agnostic**: Works with Dify, Obsidian, VS Code, etc.

## 🚀 Quick Start

### For Humans

1. Browse `INDEX.md` for navigation
2. Read any `.md` file directly
3. Edit with your favorite markdown editor
4. Follow naming conventions in `SYSTEM.md`

### For LLMs

1. Read `SYSTEM.md` for complete instructions
2. Parse YAML frontmatter for metadata
3. Use `INDEX.md` for quick lookups
4. Implement CRUD operations as defined

### For Developers

```python
# Example: Reading a decision
import yaml
import frontmatter

with open('knowledge/decisions/example.md', 'r') as f:
    post = frontmatter.load(f)
    metadata = post.metadata  # YAML frontmatter
    content = post.content    # Markdown content
    
    if metadata.get('ship_factor', 0) >= 8:
        print(f"High priority: {metadata['title']}")
```

## 📁 Structure

```
ai-brain/
├── SYSTEM.md           # LLM instructions
├── INDEX.md            # Human navigation
├── README.md           # This file
│
├── knowledge/          # What we know
│   ├── decisions/      # Technical choices
│   ├── lessons/        # Learned experiences
│   └── references/     # Quick guides
│
├── prompts/            # How AI should act
│   ├── personas/       # Personality configs
│   └── modes/          # Operational modes
│
├── systems/            # How things work
│   ├── workflows/      # Processes
│   └── rules/          # Constraints
│
└── tools/              # External connections
    └── integrations/   # API configs
```

## 📝 Content Guidelines

### Frontmatter Requirements

Every markdown file MUST include:

```yaml
---
title: Descriptive title
type: knowledge|behavior|system|tool
subtype: specific category
tags: [relevant, tags]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
ship_factor: 1-10
---
```

### Ship Factor Scale

- **10**: 🔥 Critical - Do immediately
- **8-9**: 🚀 High - This week
- **5-7**: 📋 Normal - This sprint
- **3-4**: 📌 Low - Nice to have
- **1-2**: 💭 Research - Future consideration

## 🔄 Workflow

### Adding Content

1. Create `.md` file in appropriate folder
2. Add complete frontmatter
3. Write content following type guidelines
4. Update `INDEX.md`
5. Commit with descriptive message

### Deprecating Content

1. Set `deprecated: true` in frontmatter
2. Add `deprecated_reason`
3. Update `INDEX.md`
4. DO NOT delete the file

## 🔗 Integrations

### Dify
- Point knowledge base to this repository
- Use tags for filtering
- Ship factor for prioritization

### MCP Servers
- Parse `SYSTEM.md` for instructions
- Use frontmatter for metadata
- Navigate via `INDEX.md`

### Obsidian
- Open folder as vault
- Use graph view for references
- Edit with full markdown support

## 🛠️ Tools & Commands

### Quick Scripts

```bash
# Find high-priority items
grep -r "ship_factor: [89]\|ship_factor: 10" --include="*.md"

# List all decisions
ls knowledge/decisions/*.md

# Find deprecated items
grep -r "deprecated: true" --include="*.md"
```

### Python Helper

```python
# utils/brain_helper.py
import os
import frontmatter
from datetime import datetime

def create_decision(title, content, ship_factor=5):
    """Create a new decision document"""
    slug = title.lower().replace(' ', '-')
    path = f'knowledge/decisions/{slug}.md'
    
    doc = frontmatter.Post(content)
    doc['title'] = title
    doc['type'] = 'knowledge'
    doc['subtype'] = 'decision'
    doc['created'] = datetime.now().isoformat()
    doc['modified'] = datetime.now().isoformat()
    doc['version'] = 1
    doc['ship_factor'] = ship_factor
    doc['tags'] = []
    
    with open(path, 'w') as f:
        f.write(frontmatter.dumps(doc))
    
    return path
```

## 📊 Statistics

- **Total Files**: 0
- **Last Updated**: 2024-01-15
- **Primary Maintainer**: @harrysayers7

## 🤝 Contributing

1. Follow the structure defined in `SYSTEM.md`
2. Include complete frontmatter
3. Update `INDEX.md` when adding content
4. Use descriptive commit messages
5. Tag appropriately for discoverability

## 📜 License

This knowledge base is for internal use. Modify as needed for your use case.

## 🔍 Quick Links

- [System Instructions](SYSTEM.md)
- [Navigation Index](INDEX.md)
- [High Priority Items](INDEX.md#high-priority)
- [Recent Decisions](knowledge/decisions/)
- [Active Workflows](systems/workflows/)

---

*Built for humans and machines alike. Ship fast, learn faster.*