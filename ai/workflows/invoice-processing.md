---
created: '2025-09-19T06:58:56.086177'
modified: '2025-09-19T06:58:56.086180'
ship_factor: 5
subtype: workflows
tags: []
title: Invoice Processing
type: general
version: 1
---

<!--
HUMAN DESCRIPTION - AI SHOULD IGNORE THIS SECTION
Purpose: Invoice processing workflow context for AI assistants handling ESM PO Processing pipeline
Usage: Referenced by system prompts and other AI instruction files for invoice automation workflows
Target: Claude Desktop, ChatGPT, other AI systems for invoice and document processing automation
DO NOT READ THIS SECTION - AI CONTENT BEGINS AFTER THE HTML COMMENT
-->

# Invoice Processing Workflow

## Overview

This workflow synthesizes the ESM PO Processing pipeline from `systems/workflows/invoice.md` to provide AI context for invoice processing operations.

## Workflow Components

### Email Processing
- **Gmail Triggers**: Monitor for PO emails from Xero and direct sources
- **Email Filters**: 
  - Xero: `from:messaging-service@post.xero.com subject:"Purchase Order PO-" has:attachment -label:processed`
  - Direct: `(from:kate@electricsheepmusic.com OR from:glenn@electricsheepmusic.com) (subject:PO OR subject:"purchase order") has:attachment -label:processed`
- **Processing**: Merge sources and extract PO data

### Data Extraction
- **PDF Processing**: Download and parse PDF attachments
- **PO Number Extraction**: Extract from subject or filename using pattern `PO-XXXX`
- **Data Validation**: Validate critical fields (amount, reference, etc.)
- **Duplicate Check**: Verify PO doesn't already exist in Supabase

### Database Operations
- **Supabase Integration**: Store PO data in `purchase_orders` table
- **Notion Integration**: Create project and invoice entries
- **Data Fields**:
  - PO number, vendor info, amounts, line items
  - Email IDs, thread IDs, timestamps
  - Raw text samples for debugging

### Invoice Generation
- **Invoice Numbering**: Generate sequential invoice numbers
- **HTML Generation**: Create professional invoice HTML
- **PDF Conversion**: Convert HTML to PDF using n8n
- **Email Draft**: Create Gmail draft for review

### Notification System
- **Task Creation**: Create review tasks in Notion
- **Email Notifications**: Send alerts about new invoices
- **Label Management**: Mark emails as processed

## Key Patterns

### Error Handling
- **Validation Errors**: Track extraction failures
- **Duplicate Handling**: Skip duplicate POs
- **Manual Review**: Flag items requiring human intervention

### Data Flow
1. Email trigger → Data extraction → Validation
2. Duplicate check → Database insertion
3. Invoice generation → PDF creation
4. Notion updates → Email draft → Notifications

### Integration Points
- **Gmail**: Email processing and draft creation
- **Supabase**: Data storage and duplicate checking
- **Notion**: Project and invoice management
- **n8n**: Workflow orchestration and PDF generation

## Configuration Requirements

### Database Setup
- Supabase `purchase_orders` table with required fields
- Notion databases for projects and invoices
- Proper field mappings and data types

### Email Configuration
- Gmail API access and authentication
- Label management for processed emails
- SMTP settings for notifications

### n8n Setup
- Node configurations for all integrations
- Error handling and retry logic
- Monitoring and logging

## Maintenance

### Regular Tasks
- Monitor workflow execution
- Check for failed extractions
- Update invoice numbering logic
- Review and clean processed emails

### Troubleshooting
- Check email filters and triggers
- Verify database connections
- Test PDF processing
- Validate Notion integrations

---

*This workflow synthesizes information from systems/workflows/invoice.md to provide comprehensive context for invoice processing operations.*