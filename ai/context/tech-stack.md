---
created: '2025-09-16T15:05:15.615144'
modified: '2025-09-17T16:12:32.925507'
ship_factor: 5
subtype: context
tags: []
title: Tech Stack
type: general
version: 1
---

# Tech Stack Overview

This file contains an overview of my tech stack, what they do and where they are in my codebase.

- Whenever I say "my server", I'm referring to my Ubuntu server **134.199.159.190** (sayers-server)

## MCP Servers (6 active)

### Active MCP Servers
- **context-7**: Context and fact verification for AI responses
  - **Deployment**: Local - Claude desktop, Cursor, Claude Code
  - **Usage**: Verify current information before providing answers
  - **Status**: Active

- **docker**: Docker container management
  - **Deployment**: Local - Claude desktop, Cursor, Claude Code
  - **Status**: Active

- **github**: GitHub repository management
  - **Deployment**: Local - Claude desktop, Cursor, Claude Code
  - **Status**: Active

- **n8n**: Workflow automation platform
  - **Deployment**: Production Server (134.199.159.190:5678)
  - **Status**: Active

- **notion**: Notion workspace integration
  - **Deployment**: Local (Claude Desktop)
  - **Status**: Active

- **supabase**: Supabase database and backend services
  - **Deployment**: Production Server (134.199.159.190:3000)
  - **Status**: Active


- **taskmaster**: AI-optimized task management
  - **Deployment**: Local (Claude Desktop)
  - **Status**: Active

## Integrations

### Notion Integration
- **Purpose**: Notion workspace integration and database management
- **Deployment**: Cloud (Notion API)
- **Configuration**: MCP server on local Claude Desktop
- **Databases**:
  - Coding Knowledge Database: `3e82cc5a-57bd-4cb7-b85c-53b745fdc63c`
  - Tasks-AI: `bb278d48-954a-4c93-85b7-88bd4979f467`
  - Project Tracker: `a8ab8f91-6be9-4c61-b348-f08e46b22870`
  - Coding Sub Projects: `af935520-b760-4cda-848c-0f1808622ad9`
  - AI System Components & Agents: `7f90a1a3-dfae-47e8-ad0b-f0c18fc88cae`
  - Cursor Rules Database: `916aa2e8-d236-4ae5-9ab1-5f414667252c`
  - Up Bank: `1f94a17b-b7f0-805c-a532-e605479700ff`
- **Status**: Active

## Claude Desktop Integration

### Claude Desktop Tools
- **Purpose**: Claude Desktop integration and configuration
- **Deployment**: Local (macOS development machine)
- **Configuration**: MCP server configurations in Claude Desktop
- **Status**: Active

## Tool Configuration

### MCP Server Setup
All MCP servers are configured in Claude Desktop:
- **Config Location**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Status**: 6 servers active and operational

### Integration Dependencies
- **Notion databases** are interconnected through relation properties
- **MCP servers** provide tool access to AI assistants
- **Tools** coordinate through Claude Desktop and AI Brain system