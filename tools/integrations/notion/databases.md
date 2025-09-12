# Notion Databases

Database schemas and IDs for API interaction.

## Main Databases

### Second Brain Knowledge Base
```yaml
name: Second Brain
id: [DATABASE_ID_HERE]
url: https://notion.so/...
type: knowledge_base
schema:
  title:
    type: title
    required: true
  tags:
    type: multi_select
    options: [coding, architecture, decision, learning]
  ship_factor:
    type: number
    min: 1
    max: 10
  status:
    type: select
    options: [active, archived, deprecated]
  created:
    type: date
  modified:
    type: date
```

### Projects Tracker
```yaml
name: Projects
id: [DATABASE_ID_HERE]
url: https://notion.so/...
type: project_management
schema:
  name:
    type: title
  status:
    type: select
    options: [planning, active, on-hold, completed]
  priority:
    type: select
    options: [high, medium, low]
  deadline:
    type: date
  owner:
    type: person
```

## API Operations

### Query Database
```javascript
// Example query structure
{
  database_id: "[DATABASE_ID]",
  filter: {
    property: "ship_factor",
    number: {
      greater_than_or_equal_to: 8
    }
  },
  sorts: [{
    property: "modified",
    direction: "descending"
  }]
}
```

## Common Filters

- High priority: `ship_factor >= 8`
- Active items: `status = "active"`
- Recent: `modified > last_7_days`
- Tagged: `tags contains "architecture"`