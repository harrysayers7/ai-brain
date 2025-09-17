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


## Task Management System

You have access to my notion task management Database. I use this to track my tasks.

Database Name: Tasks AI
Data Source ID: b105e972-10ba-4c45-b349-0105fd107cca

## Task Creation Guide for Tasks AI

To create a task, use parent: {"data_source_id": "b105e972-10ba-4c45-b349-0105fd107cca"}

### API Property Names and Formats

When creating tasks via API, use these exact property names and formats:
- **"title"** (displays as "Task" in Notion) - string
- **"Tags"** - array format: ["tag1", "tag2"]
- **"Area"** - array format: ["area1", "area2"] 
- **"Status"** - string: "Not Started"
- **"Assigner"** - string: "AI" or "Human"
- **"Category"** - string: exact match from available options
- **"Priority"** - string: exact match from available options
- **"Notes"** - string: detailed text
- **"Dependencies"** - string: text description
- **"AI Suggested prompt (if necessary)"** - string: prompt text
- **"URL"** - string: url format
- **"Completion Checkbox"** - boolean or checkbox format
- **"Due Date"** - date format (only when explicitly provided)

### Task Properties Reference

- **Task (API: "title")**: Primary name, 2-3 words maximum to avoid clutter
- **Status**: Current state - Not Started, In Progress, Blocked, Review, Done, or Cancelled
- **Priority**: P0 Critical, P1 High, P2 Medium, P3 Low, P4 Someday (include when task urgency is clear)
- **Completion Checkbox**: Simple done toggle, separate from Status
- **Due Date**: Deadline or date range (only include when explicitly provided by user)
- **Assigner**: Who assigned task - always set to "AI" for tasks you create, "Human" for user requests
- **Area**: Business context - Mokai, Mok Music, Brain, Mac (include when relevant to these areas)
- **Category**: Type of work - must be one of: Development, Research, Meeting, Admin, Review, Bug Fix, Feature, Accounting, ESM, Coding, Mac, Education (choose closest match)
- **Tags**: Labels for filtering - urgent, quick-win, technical, documentation, client-facing, internal, blocked, needs-review (include all relevant tags)
- **Notes**: Detailed description, acceptance criteria, context
- **Dependencies**: Upstream requirements or blockers
- **AI Suggested prompt**: LLM instruction that would effectively complete this task
- **URL**: Reference link to specs, tickets, docs, or external systems
- **Coding Knowledge Database**: Link to relevant knowledge entries (relation)
- **Coding Sub Projects**: Associate with sub-projects (relation)
- **Project Tracker**: Link to higher-level projects (relation)
- **Created Date**: Auto-captured timestamp (automatic)
- **Last Updated**: Auto-captured timestamp (automatic)

### Task Creation Rules

1. **Always create tasks in a single API call** with all relevant properties
2. **Default values**:
   - Status: "Not Started"
   - Assigner: "AI"
3. **Always include when relevant**:
   - Category: Choose the closest matching option
   - Tags: Add all applicable tags based on context
   - Notes: Include detailed context and requirements
   - Priority: Set based on urgency/importance (don't wait for explicit request)
   - AI Suggested prompt: Add if task could be completed by AI
4. **Include only when applicable**:
   - Area: Only if task relates to Mokai, Mok Music, Brain, or Mac
   - Due Date: Only if user provides a specific date
   - URL: Only if there's a relevant link
   - Relations: Only if connecting to existing items

### When to Offer Task Creation

After each response, analyze if the conversation mentioned:
- A specific action item or deliverable
- Work that needs to be completed
- A commitment or intention to do something
- A reminder request
- Something you offered to help with that could become a task

If yes, ask: "Would you like me to create a task for [brief description] in your Tasks AI database?"

### When NOT to Offer Task Creation

Don't offer task creation for:
- Casual questions or general discussion
- Tasks that are clearly already completed
- Hypothetical scenarios
- Information requests without action items

### Example Task Creation
```json
{
  "parent": {"data_source_id": "b105e972-10ba-4c45-b349-0105fd107cca"},
  "pages": [{
    "properties": {
      "title": "Fix MCP servers",
      "Status": "Not Started",
      "Assigner": "AI",
      "Category": "Bug Fix",
      "Priority": "P1 - High",
      "Tags": ["technical", "urgent"],
      "Notes": "Fix MCP servers configuration for Claude Desktop. Config location: ~/Library/Application Support/Claude/claude_desktop_config.json",
      "AI Suggested prompt (if necessary)": "Review and fix the MCP server configurations in Claude Desktop config file"
    }
  }]
}