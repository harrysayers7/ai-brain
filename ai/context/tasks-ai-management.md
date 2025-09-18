---
created: '2025-09-18T06:32:12.377360'
modified: '2025-09-18T06:32:12.377367'
ship_factor: 5
subtype: context
tags: []
title: Tasks Ai Management
type: general
version: 1
---



# Task Management System

You have access to my Notion task management Database. I use this to track my tasks.

**Database Name**: Tasks AI  
**Database ID**: bb278d48-954a-4c93-85b7-88bd4979f467  
**Data Source ID**: b105e972-10ba-4c45-b349-0105fd107cca

## Task Creation Process

### API Property Names and Data Formats

**CRITICAL DATA FORMAT REQUIREMENTS:**
- **Multi-select fields** (Tags, Area) MUST be JSON strings: `"[\"value1\", \"value2\"]"`
- **Select fields** (Status, Priority, etc.) use simple strings: `"Not Started"`
- **Property names** are case-sensitive and must match exactly

#### Required Property Names:
- **"Task"** - string (task title)
- **"Tags"** - JSON string: `"[\"technical\", \"internal\"]"`
- **"Area"** - JSON string: `"[\"Brain\"]"`
- **"Status"** - string: `"Not Started"`
- **"Assigner"** - string: `"AI"` or `"Human"`
- **"Category"** - string: exact match from allowed options
- **"Priority"** - string: exact match from allowed options
- **"Notes"** - string: detailed text
- **"Dependencies"** - string: text description
- **"AI Suggested prompt (if necessary)"** - string: prompt text
- **"userDefined:URL"** - string: url format
- **"Completion Checkbox"** - string: `"__YES__"` or `"__NO__"`
- **"date:Due Date:start"** - string: ISO date format (only when explicitly provided)

### Allowed Values (Use Only These)

#### Tags (Multi-select - JSON string format):
`"urgent"`, `"quick-win"`, `"technical"`, `"documentation"`, `"client-facing"`, `"internal"`, `"blocked"`, `"needs-review"`

#### Area (Multi-select - JSON string format):
`"Mokai"`, `"Mok Music"`, `"Brain"`, `"Mac"`

#### Status (Select):
`"Not Started"`, `"In Progress"`, `"Blocked"`, `"Review"`, `"Done"`, `"Cancelled"`

#### Priority (Select):
`"P0 - Critical"`, `"P1 - High"`, `"P2 - Medium"`, `"P3 - Low"`, `"P4 - Someday"`

#### Category (Select):
`"Development"`, `"Research"`, `"Meeting"`, `"Admin"`, `"Review"`, `"Bug Fix"`, `"Feature"`, `"Accounting"`, `"ESM"`, `"Coding"`, `"Mac"`, `"Education"`

#### Assigner (Select):
`"AI"`, `"Human"`

## Task Creation Template

```json
{
  "parent": {"data_source_id": "b105e972-10ba-4c45-b349-0105fd107cca"},
  "pages": [{
    "properties": {
      "Task": "Fix MCP servers",
      "Status": "Not Started",
      "Assigner": "AI",
      "Category": "Bug Fix",
      "Priority": "P1 - High",
      "Tags": "[\"technical\", \"urgent\"]",
      "Area": "[\"Brain\"]",
      "Notes": "Fix MCP servers configuration for Claude Desktop.",
      "Dependencies": "Access to Claude Desktop configuration file",
      "AI Suggested prompt (if necessary)": "Review and fix the MCP server configurations"
    }
  }]
}
```

## Task Creation Rules

1. **Use documented schema above** (no API fetch needed unless errors occur)
2. **Required defaults**:
   - Status: "Not Started"
   - Assigner: "AI"
3. **Always include when relevant**:
   - Category: Choose closest match
   - Tags: Add relevant tags from allowed list
   - Notes: Detailed context and requirements
   - Priority: Based on urgency/importance
4. **Include only when applicable**:
   - Area: Only for Mokai, Mok Music, Brain, or Mac
   - Due Date: Only if user provides specific date
   - URL: Only if there's a relevant link

## Error Prevention Checklist

- [ ] Used "Task" property name (not "title")
- [ ] Formatted Tags as JSON string: `"[\"tag1\", \"tag2\"]"`
- [ ] Formatted Area as JSON string: `"[\"Brain\"]"`
- [ ] Verified all values exist in allowed options above
- [ ] Used correct data source ID: `"b105e972-10ba-4c45-b349-0105fd107cca"`

**If validation errors occur**: Fetch schema to check for updates using database ID `bb278d48-954a-4c93-85b7-88bd4979f467`

## When to Offer Task Creation

After responses, check if conversation mentioned:
- Specific action items or deliverables
- Work that needs completion
- Commitments or intentions
- Reminder requests
- Offered assistance that could become tasks

If yes, ask: "Would you like me to create a task for [brief description] in your Tasks AI database?"

## When NOT to Offer Task Creation

Don't offer for:
- Casual questions or general discussion
- Completed tasks
- Hypothetical scenarios
- Information requests without action items