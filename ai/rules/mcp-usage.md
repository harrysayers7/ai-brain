---
created: '2025-09-17T16:12:32.929721'
modified: '2025-09-17T16:12:32.929722'
ship_factor: 5
subtype: rules
tags: []
title: Mcp Usage
type: general
version: 1
---

# MCP Usage Rules

## Core Principles

When using Model Context Protocol (MCP) servers, follow these behavioral rules synthesized from `tools/mcp-servers/` and `docs/guides/mcp-instructions/` directories.

## Pre-Flight Checks

### Before Using Any MCP Server
1. **Verify server is available** - Check if the MCP server is properly configured
2. **Validate API keys** - Ensure required API keys are set and valid
3. **Check server status** - Confirm the server is running and responsive
4. **Review documentation** - Reference the specific server documentation

### Context7 Specific Rules
- **Always resolve library ID first** - Use `resolve-library-id` before `get-library-docs`
- **Handle failures gracefully** - If library not found, suggest alternatives
- **Use appropriate token limits** - Balance context with response quality
- **Verify library compatibility** - Ensure library matches project requirements

### GitHub MCP Rules
- **Check repository access** - Verify permissions before operations
- **Use appropriate branch** - Work with correct branch for context
- **Handle rate limits** - Respect API rate limits and retry logic
- **Validate file paths** - Ensure file paths exist before operations

## Error Handling

### When MCP Operations Fail
1. **Check server logs** - Review error messages and status
2. **Verify configuration** - Ensure proper setup and API keys
3. **Test connectivity** - Confirm network and server availability
4. **Fallback gracefully** - Provide alternative approaches when possible

### Common Error Patterns
- **Authentication errors** - Check API keys and permissions
- **Rate limit errors** - Implement retry logic with backoff
- **Network errors** - Verify connectivity and server status
- **Data validation errors** - Check input parameters and formats

## Best Practices

### Server Selection
- **Choose appropriate server** - Match server to task requirements
- **Consider performance** - Use most efficient server for the task
- **Check capabilities** - Ensure server supports required operations
- **Verify reliability** - Prefer stable, well-maintained servers

### Data Management
- **Validate inputs** - Check parameters before sending requests
- **Handle responses** - Process and validate server responses
- **Manage state** - Maintain consistent state across operations
- **Cache when appropriate** - Store frequently accessed data

### Security Considerations
- **Protect API keys** - Never expose sensitive credentials
- **Validate inputs** - Sanitize user inputs before processing
- **Use secure connections** - Prefer HTTPS and secure protocols
- **Monitor usage** - Track server usage and performance

## Integration Guidelines

### With Development Workflows
- **Reference `systems/workflows/`** - Follow established development processes
- **Use `commands/`** - Leverage available command shortcuts
- **Check `infrastructure/`** - Verify environment compatibility
- **Update `docs/guides/`** - Document new patterns and procedures

### With Project Management
- **Use Task Master** - Integrate with project task management
- **Update Memory** - Store important decisions and patterns
- **Document changes** - Record MCP usage and configurations
- **Track performance** - Monitor server effectiveness and reliability

## Maintenance

### Regular Updates
- **Check server versions** - Keep MCP servers updated
- **Review configurations** - Ensure settings remain optimal
- **Test functionality** - Verify servers work as expected
- **Update documentation** - Keep guides current with changes

### Troubleshooting
- **Check logs** - Review server and application logs
- **Test connectivity** - Verify network and server status
- **Validate configuration** - Ensure proper setup
- **Consult documentation** - Reference server-specific guides

---

*These rules synthesize information from tools/mcp-servers/ and docs/guides/mcp-instructions/ directories to provide comprehensive MCP usage guidelines.*