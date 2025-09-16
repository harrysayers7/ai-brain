# AI Brain Index

Last Updated: 2025-09-12

## Quick Navigation

### 🚀 High Priority (Ship Factor 8+)
*Items requiring immediate attention*

- No high priority items yet

### 📚 Knowledge Base

#### Recent Decisions
*Architectural and technical choices*

- No decisions yet (folder: `knowledge/decisions/`)

#### Lessons Learned
*What worked, what didn't, and why*

- No lessons yet (folder: `knowledge/lessons/`)

#### Reference Guides
*Quick lookups and cheat sheets*

- No references yet (folder: `knowledge/references/`)

### 🤖 Prompts

#### Active Configurations
*AI personality and interaction patterns*

- `prompts/claude-desktop/instructions.md` - Claude Desktop integration rules
- `prompts/modes/accountant.md` - Accountant persona mode
- `prompts/modes/vibe-coding.md` - Vibe coding assistant mode
- `prompts/personas/` - Empty, ready for personas

### ⚙️ Systems

#### Active Workflows
*Repeatable processes and automations*

- No workflows yet (folder: `systems/workflows/`)

#### Rules & Constraints
*Governance and guardrails*

- No rules defined yet (folder: `systems/rules/`)

### 🔧 Tools & Integrations

#### MCP Servers (17 configured)
*Model Context Protocol servers in `tools/mcp-servers/`*

- chrome-mcp, context-7, dify-mcp-connector, docker
- fastapi-mcp, fastmcp, filesystem, github
- google-drive, graphiti, mindsdb, n8n
- notion, playwright, slack, supabase, taskmaster

#### Integrations
*External tools and APIs*

- `tools/integrations/notion/` - Notion workspace configuration (databases.md, README.md)

### 🏗️ Infrastructure

#### Servers
- `infrastructure/servers/production.md` - 134.199.159.190 (sayers-server)

#### Local Environment
- `infrastructure/local/workstation.md` - Development machine specs
- `infrastructure/local/dev-tools.md` - Installed development tools
- `infrastructure/local/docker-compose.yml` - Local service stack
- `infrastructure/local/env-template.md` - Environment variables template

#### Empty Folders Ready for Content
- `infrastructure/databases/` - Database configurations
- `infrastructure/docker/` - Docker configurations
- `infrastructure/networking/` - Network configurations

### 📝 Commands

#### Command System
*Quick action shortcuts for LLMs*

- `commands/shortcuts/INSTRUCTIONS.md` - How to handle ! commands
- `commands/shortcuts/general-commands.md` - General command shortcuts
- `commands/shortcuts/mokai-commands.md` - Mokai-specific commands
- `commands/templates/` - Reusable prompt templates (with README)
- `commands/macros/` - Multi-step command sequences (with README)
- `commands/COMMANDS-INSTRUCTIONS.md` - Duplicate, needs cleanup

### 🛠️ Utils

#### Helper Scripts
- `utils/brain_helper.py` - Python utility for brain operations

### 📊 Statistics

- **Total Files**: ~50+ markdown files
- **Active Modes**: 2 (accountant, vibe-coding)
- **MCP Servers**: 17 configured
- **Infrastructure Envs**: 2 (production, local)
- **Command Categories**: 3 (shortcuts, templates, macros)
- **Python Utils**: 1 (brain_helper.py)

### 🏷️ Repository Structure

```
ai-brain/
├── .gitignore
├── README.md                   # Repository overview
├── SYSTEM.md                   # Complete navigation guide
├── INDEX.md                    # This file
│
├── knowledge/                  # What we know
│   ├── README.md
│   ├── decisions/             # Technical/architectural choices
│   ├── lessons/               # What worked/didn't work
│   └── references/            # Quick lookups
│
├── prompts/                    # How AI behaves
│   ├── README.md
│   ├── claude-desktop/        # Claude Desktop instructions
│   │   └── instructions.md
│   ├── modes/                 # Context-specific behaviors
│   │   ├── README.md
│   │   ├── accountant.md
│   │   └── vibe-coding.md
│   └── personas/              # AI personalities (empty)
│       └── README.md
│
├── systems/                    # How things work
│   ├── README.md
│   ├── workflows/             # Repeatable processes (empty)
│   │   └── README.md
│   └── rules/                 # Governance (empty)
│       └── README.md
│
├── tools/                      # External integrations
│   ├── README.md
│   ├── integrations/          # Service configurations
│   │   ├── README.md
│   │   └── notion/
│   │       ├── README.md
│   │       └── databases.md
│   ├── mcp-servers/           # MCP server configs
│   │   ├── README.md
│   │   └── [17 MCP server files]
│   └── infrastructure/        # Old location (moved to root)
│       └── .gitkeep
│
├── infrastructure/             # Where things run
│   ├── README.md
│   ├── servers/               # Production servers
│   │   └── production.md
│   ├── local/                 # Development environment
│   │   ├── README.md
│   │   ├── workstation.md
│   │   ├── dev-tools.md
│   │   ├── docker-compose.yml
│   │   └── env-template.md
│   ├── databases/             # DB configs (empty)
│   ├── docker/                # Docker configs (empty)
│   └── networking/            # Network configs (empty)
│
├── commands/                   # LLM command system
│   ├── README.md
│   ├── COMMANDS-INSTRUCTIONS.md  # Duplicate (needs removal)
│   ├── shortcuts/             # Quick ! commands
│   │   ├── README.md
│   │   ├── INSTRUCTIONS.md
│   │   ├── general-commands.md
│   │   └── mokai-commands.md
│   ├── templates/             # Reusable templates
│   │   └── README.md
│   └── macros/                # Multi-step sequences
│       └── README.md
│
└── utils/                      # Helper utilities
    └── brain_helper.py        # Python utility script
```

### ⚠️ Cleanup Needed

- Remove `commands/COMMANDS-INSTRUCTIONS.md` (duplicate)
- Remove `tools/infrastructure/.gitkeep` (moved to root)
- Various `.gitkeep` files can be removed once folders have content

### 📝 Recent Changes (2025-09-12)

- Added `prompts/claude-desktop/` for Claude Desktop integration
- Added `tools/mcp-servers/` with 17 MCP server configurations
- Created `infrastructure/` at root level (moved from tools)
- Added `commands/` system with shortcuts, templates, and macros
- Added `tools/integrations/notion/` for Notion configuration
- Created local development environment documentation

## Maintenance Notes

This index should be updated whenever:
- New content is added to any folder
- Files are moved or renamed
- Items are deprecated (mark with `deprecated: true` in frontmatter)
- Ship factors change significantly
- Monthly statistics review

## How to Use This Index

1. **For Quick Access**: Navigate directly to the folder/file you need
2. **For Priority Work**: Check High Priority section for ship factor 8+ items
3. **For Learning**: Browse `knowledge/lessons/` when populated
4. **For Commands**: Check `commands/shortcuts/INSTRUCTIONS.md` for ! command usage
5. **For Setup**: Use `infrastructure/local/` for dev environment setup