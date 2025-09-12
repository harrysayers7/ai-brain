# Notion Integration

Configuration and schemas for Notion workspace integration.

## Structure

- `databases.md` - Database schemas, IDs, and structures
- `api-config.md` - API configuration (reference only, no keys)
- `workflows.md` - Common Notion operations
- `templates.md` - Page and database templates

## Usage

Reference these files when:
- Creating Notion pages/databases via API
- Querying existing databases
- Setting up automations
- Maintaining consistency across Notion workspace

## Security Note

⚠️ Never store actual API keys here. Use:
```yaml
api_key:
  location: ENVIRONMENT_VARIABLE
  name: NOTION_API_KEY
```