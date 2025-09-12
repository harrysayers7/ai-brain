# MCP Servers Configuration

Model Context Protocol server configurations and connections.

## Active MCP Servers

### Available Servers
- filesystem - File system operations
- github - GitHub integration  
- google-drive - Google Drive access
- google-maps - Maps and location services
- notion - Notion workspace
- obsidian - Obsidian vault access
- postgres - PostgreSQL database
- sqlite - SQLite database
- slack - Slack workspace

## Server Configurations

Individual server configs in:
- `filesystem.md`
- `github.md`
- `notion.md`
- etc.

## Connection Instructions

See Claude Desktop MCP setup guide for adding servers to:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%/Claude/claude_desktop_config.json`

## Security

⚠️ Never store credentials here. Reference environment variables or secret managers only.