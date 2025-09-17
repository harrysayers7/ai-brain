---
created: '2025-09-17T16:12:32.929948'
modified: '2025-09-17T17:15:05.744916'
ship_factor: 5
subtype: templates
tags: []
title: Code Generation
type: general
version: 1
---

# Code Generation Template

## Template Structure

This template synthesizes code generation patterns from `tools/`, `infrastructure/`, and `systems/workflows/` directories.

## Pre-Development Checklist

### Research Phase
- **Use Context7**: Look up library documentation and examples
- **Check GitHub**: Review similar implementations and best practices
- **Reference Infrastructure**: Verify environment compatibility
- **Consult Guides**: Follow setup instructions from `docs/guides/`

### Planning Phase
- **Define Requirements**: Clear specification of what needs to be built
- **Choose Tools**: Select appropriate libraries and frameworks
- **Plan Architecture**: Design system structure and data flow
- **Consider Integration**: Ensure compatibility with existing systems

## Code Generation Process

### 1. Setup and Configuration
```markdown
## Environment Setup
- Reference: `infrastructure/local/` for development setup
- Use environment templates from `infrastructure/local/env-template.md`
- Configure development tools per `infrastructure/local/dev-tools.md`
- Set up workstation per `infrastructure/local/workstation.md`
```

### 2. Implementation Standards
```markdown
## Code Quality
- Write clean, well-documented code
- Follow established patterns and conventions
- Include comprehensive error handling
- Write tests for all functionality
- Use proper version control practices
```

### 3. Integration Guidelines
```markdown
## System Integration
- Use MCP servers from `tools/mcp-servers/` directory
- Follow workflows from `systems/workflows/` directory
- Reference commands from `commands/` directory
- Apply infrastructure knowledge from `infrastructure/` directory
```

## Common Patterns

### MCP Server Integration
- **Context7**: Library documentation and examples
- **GitHub**: Repository operations and code examples
- **Memory**: Persistent knowledge storage
- **Supabase**: Database operations
- **Task Master**: Project management integration

### Error Handling
- **Validation**: Check inputs and parameters
- **Graceful Degradation**: Provide fallback options
- **Logging**: Record errors and debugging information
- **User Feedback**: Clear error messages and guidance

### Testing Strategy
- **Unit Tests**: Test individual components
- **Integration Tests**: Test system interactions
- **End-to-End Tests**: Test complete workflows
- **Performance Tests**: Verify system performance

## Documentation Requirements

### Code Documentation
- **Inline Comments**: Explain complex logic
- **Function Documentation**: Describe purpose and parameters
- **API Documentation**: Document external interfaces
- **Usage Examples**: Provide practical examples

### System Documentation
- **Setup Instructions**: How to configure and run
- **Configuration Guide**: Environment and parameter settings
- **Troubleshooting**: Common issues and solutions
- **Maintenance**: Ongoing care and updates

## Quality Assurance

### Code Review Checklist
- **Functionality**: Does it work as intended?
- **Performance**: Is it efficient and scalable?
- **Security**: Are there any vulnerabilities?
- **Maintainability**: Is it easy to understand and modify?

### Testing Checklist
- **Coverage**: Are all code paths tested?
- **Edge Cases**: Are boundary conditions handled?
- **Error Conditions**: Are failures handled gracefully?
- **Integration**: Do all components work together?

---

*This template synthesizes information from tools/, infrastructure/, and systems/ directories to provide comprehensive code generation guidance.*