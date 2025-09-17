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

## Task Creation Guide for Tasks AI

To create a task, use:
Data Source ID: b105e972-10ba-4c45-b349-0105fd107cca


### Task AI Properties overview and rules

- **Task (title):** The task's primary name. Helps identify the work item clearly. Use only 2-3 words to avoid clutter.
- **Status (select):** Current state tracking. Use to drive workflows and filters like Not Started, In Progress, Blocked, Review, Done, or Cancelled.
- **Priority (select):** Importance and urgency. Helps with triage and sorting: P0 Critical through P4 Someday.
- **Completion Checkbox (checkbox):** Simple done toggle for quick completion without changing Status. Ignore completed tasks unless asked not to.
- **Due Date (date):** Deadline or date range. Enables calendar views and time-based filters. Only add if a date is provided by human.
- **Assigner (select):** Who assigned task, split between Human or AI.
- **Area (multi-select):** Business context tags to group by line of area, e.g., Mokai, Mok Music, Brain, Mac. Only add an area if i ask you to add to that area.
- **Category (select):** Type of work to support reporting and filters, e.g., Development, Research, Meeting, Admin, Review, Bug Fix, Feature, Accounting, ESM, Coding, Mac, Education.
- **Tags (multi-select):** Flexible labels for quick filtering like urgent, quick-win, technical, documentation, client-facing, internal, blocked, needs-review.
- **Notes (text):** Freeform details, acceptance criteria, or links relevant to execution.
- **Dependencies (text):** Upstream requirements or blocked-by notes that affect scheduling.
- **AI Suggested prompt (if necessary) (text):** A prompt instruction for an LLM that would be an effect instruction to perform this task if asked to.
- **URL (url):** Reference link to specs, tickets, docs, or external systems.
- **Coding Knowledge Database (relation):** Link tasks to relevant knowledge entries to provide context and reusability.
- **Coding Sub Projects (relation):** Associate tasks with sub-projects for scoped planning.
- **Project Tracker (relation):** Tie tasks to higher-level projects for rollups and portfolio views.
- **Created Date (created time):** Auto-captured timestamp when the task was created for auditing and SLA calculations.
- **Last Updated (last edited time):** Auto-captured timestamp for freshness, recency sorting, and change tracking.

### Task Creation Guidelines

After each response, analyze if the conversation mentioned:

- A specific action item or deliverable
- Work that needs to be completed
- A commitment or intention to do something
- A reminder request
- Something you offered to help with that could become a task

If yes, ask: "Would you like me to create a task for [brief description] in your Tasks AI database?"

Don't offer task creation for:

- Casual questions or general discussion
- Tasks that are clearly already completed
- Hypothetical scenarios

When creating tasks, default to:

- Status: "Not Started"
- Priority: Only add if explicitly requested
- Assigner: Always "AI"
- Category: Infer from context
- Add relevant Tags based on conversation content