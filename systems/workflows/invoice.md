{
    "title": "Invoice",
    "type": "system",
    "subtype": "workflows",
    "created": "2025-09-16T15:05:15.623100",
    "modified": "2025-09-16T19:19:40.868831",
    "version": 1,
    "ship_factor": 5,
    "tags": []
}


{
    "name": "ESM PO Processing - Main Pipeline",
    "nodes": [
      {
        "id": "gmail_trigger_1",
        "name": "Gmail PO Trigger - Xero",
        "type": "n8n-nodes-base.gmailTrigger",
        "position": [250, 200],
        "typeVersion": 2,
        "parameters": {
          "pollTimes": {
            "item": [
              {
                "mode": "everyMinute"
              }
            ]
          },
          "simple": false,
          "filters": {
            "q": "from:messaging-service@post.xero.com subject:\"Purchase Order PO-\" has:attachment -label:processed"
          }
        },
        "notes": "Triggers on Xero PO emails every minute. After processing, add 'processed' label to avoid reprocessing"
      },
      {
        "id": "gmail_trigger_2", 
        "name": "Gmail PO Trigger - Direct",
        "type": "n8n-nodes-base.gmailTrigger",
        "position": [250, 400],
        "typeVersion": 2,
        "parameters": {
          "pollTimes": {
            "item": [
              {
                "mode": "everyMinute"
              }
            ]
          },
          "simple": false,
          "filters": {
            "q": "(from:kate@electricsheepmusic.com OR from:glenn@electricsheepmusic.com) (subject:PO OR subject:\"purchase order\") has:attachment -label:processed"
          }
        },
        "notes": "Triggers on direct emails from Kate or Glenn"
      },
      {
        "id": "merge_triggers",
        "name": "Merge PO Sources",
        "type": "n8n-nodes-base.merge",
        "position": [450, 300],
        "typeVersion": 2,
        "parameters": {
          "mode": "combine",
          "combinationMode": "multiplex",
          "options": {}
        }
      },
      {
        "id": "extract_po_data",
        "name": "Extract & Validate PO Data",
        "type": "n8n-nodes-base.code",
        "position": [650, 300],
        "typeVersion": 1,
        "parameters": {
          "jsCode": `
  // Safely extract email data
  const emailData = $json;
  const subject = emailData.subject || '';
  const from = emailData.from?.value?.[0]?.address || emailData.from || '';
  const attachments = emailData.attachments || [];
  const messageId = emailData.id || emailData.messageId;
  
  // Find PDF attachment
  const pdfAttachment = attachments.find(att => {
    const filename = att.filename || att.name || '';
    return filename.toLowerCase().endsWith('.pdf');
  });
  
  if (!pdfAttachment) {
    return [{
      json: {
        error: true,
        errorType: 'NO_PDF',
        message: 'No PDF attachment found in PO email',
        emailId: messageId,
        subject: subject,
        from: from,
        timestamp: new Date().toISOString()
      }
    }];
  }
  
  // Extract PO number from subject or attachment
  let poNumber = null;
  let poNumberSource = null;
  
  // Try subject first - looking for PO-XXXX pattern
  const subjectMatch = subject.match(/PO[- ]?(\d{3,4})/i);
  if (subjectMatch) {
    poNumber = 'PO-' + subjectMatch[1].padStart(4, '0');
    poNumberSource = 'subject';
  }
  
  // If not in subject, try filename
  if (!poNumber) {
    const filenameMatch = pdfAttachment.filename?.match(/PO[- ]?(\d{3,4})/i);
    if (filenameMatch) {
      poNumber = 'PO-' + filenameMatch[1].padStart(4, '0');
      poNumberSource = 'filename';
    }
  }
  
  // Determine sender type
  const senderType = from.includes('xero.com') ? 'xero' : 'direct';
  const vendorEmail = senderType === 'xero' ? 'accounts@electricsheepmusic.com' : from;
  
  return [{
    json: {
      error: false,
      poNumber: poNumber || 'PO-UNKNOWN-' + Date.now(),
      poNumberSource: poNumberSource || 'generated',
      emailId: messageId,
      threadId: emailData.threadId,
      subject: subject,
      from: from,
      vendorEmail: vendorEmail,
      senderType: senderType,
      receivedAt: new Date().toISOString(),
      attachmentId: pdfAttachment.attachmentId || pdfAttachment.id,
      attachmentData: pdfAttachment.data,
      filename: pdfAttachment.filename || pdfAttachment.name,
      requiresManualPoNumber: !poNumber
    }
  }];`
        },
        "notes": "Extracts PO number and validates email structure"
      },
      {
        "id": "download_pdf",
        "name": "Download PDF Attachment",
        "type": "n8n-nodes-base.gmail",
        "position": [850, 300],
        "typeVersion": 2.1,
        "parameters": {
          "operation": "getAttachment",
          "messageId": "={{ $json.emailId }}",
          "attachmentId": "={{ $json.attachmentId }}"
        },
        "notes": "Downloads the actual PDF file from Gmail"
      },
      {
        "id": "parse_pdf",
        "name": "Parse PDF Content",
        "type": "n8n-nodes-base.extractFromFile",
        "position": [1050, 300],
        "typeVersion": 1,
        "parameters": {
          "operation": "text",
          "binaryPropertyName": "attachment",
          "options": {
            "pages": "all"
          }
        },
        "notes": "Extracts text from PDF using built-in OCR"
      },
      {
        "id": "extract_po_details",
        "name": "Extract PO Details from Text",
        "type": "n8n-nodes-base.code",
        "position": [1250, 300],
        "typeVersion": 1,
        "parameters": {
          "jsCode": `
  // Get the extracted text and previous data
  const text = $json.text || '';
  const poData = $input.first().json;
  
  // Clean up text for better parsing
  const cleanText = text.replace(/\\s+/g, ' ').trim();
  
  // Extract patterns specific to ESM POs
  const patterns = {
    poNumber: /PO[- ]?(\\d{3,4})/i,
    amount: /TOTAL\\s+AUD\\s+([\\d,]+\\.\\d{2})/i,
    vendorName: /Electric Sheep Music Pty Ltd/i,
    abn: /ABN\\s+(\\d{2}\\s\\d{3}\\s\\d{3}\\s\\d{3})/i,
    reference: /Reference\\s+([^\\n]+)/i,
    deliveryDate: /Delivery Date\\s+([^\\n]+)/i,
    description: /Description[\\s\\S]*?Quantity/i,
    demoFee: /composer fees?\\s+[\\d.]+\\s+([\\d,]+\\.\\d{2})/i
  };
  
  // Extract values
  const amount = cleanText.match(patterns.amount);
  const reference = cleanText.match(patterns.reference);
  const abn = cleanText.match(patterns.abn);
  
  // Parse line items - looking for the main service
  let lineItems = [];
  const descriptionSection = cleanText.match(/Description.*?Subtotal/is);
  if (descriptionSection) {
    const itemMatch = descriptionSection[0].match(/(\\w[\\w\\s]+?)\\s+(\\d+\\.\\d{2})\\s+([\\d,]+\\.\\d{2})\\s+GST\\s*Free\\s+([\\d,]+\\.\\d{2})/);
    if (itemMatch) {
      lineItems.push({
        description: itemMatch[1].trim(),
        quantity: parseFloat(itemMatch[2]),
        unitPrice: parseFloat(itemMatch[3].replace(/,/g, '')),
        amount: parseFloat(itemMatch[4].replace(/,/g, ''))
      });
    }
  }
  
  // Build extracted data object
  const extractedData = {
    poNumber: poData.poNumber,
    vendorName: 'Electric Sheep Music Pty Ltd',
    vendorEmail: poData.vendorEmail,
    abn: abn ? abn[1] : '35 614 711 358',
    reference: reference ? reference[1].trim() : null,
    totalAmount: amount ? parseFloat(amount[1].replace(/,/g, '')) : 0,
    currency: 'AUD',
    lineItems: lineItems.length > 0 ? lineItems : [{
      description: reference ? reference[1].trim() : 'Composer Services',
      quantity: 1,
      unitPrice: amount ? parseFloat(amount[1].replace(/,/g, '')) : 0,
      amount: amount ? parseFloat(amount[1].replace(/,/g, '')) : 0
    }],
    status: 'received',
    emailId: poData.emailId,
    threadId: poData.threadId,
    receivedAt: poData.receivedAt,
    rawTextSample: cleanText.substring(0, 500)
  };
  
  // Validate critical fields
  const errors = [];
  if (!extractedData.totalAmount || extractedData.totalAmount === 0) {
    errors.push('Could not extract amount from PDF');
  }
  if (!extractedData.reference) {
    errors.push('Could not extract reference/description');
  }
  
  return [{
    json: {
      ...extractedData,
      validationErrors: errors,
      requiresManualReview: errors.length > 0 || poData.requiresManualPoNumber,
      extractionSuccess: errors.length === 0
    }
  }];`
        },
        "notes": "Parses ESM-specific PO format from PDF text"
      },
      {
        "id": "check_duplicate",
        "name": "Check for Duplicate PO",
        "type": "n8n-nodes-base.supabase",
        "position": [1450, 300],
        "typeVersion": 1,
        "parameters": {
          "operation": "getAll",
          "tableId": "purchase_orders",
          "filterType": "string",
          "filterString": "po_number=eq.{{ $json.poNumber }}",
          "limit": 1
        },
        "notes": "Check if PO already exists in Supabase"
      },
      {
        "id": "check_duplicate_result",
        "name": "Is Duplicate?",
        "type": "n8n-nodes-base.if",
        "position": [1650, 300],
        "typeVersion": 1,
        "parameters": {
          "conditions": {
            "options": {
              "caseSensitive": true,
              "leftValue": "",
              "typeValidation": "loose"
            },
            "conditions": [
              {
                "leftValue": "={{ $json.length }}",
                "rightValue": 0,
                "operator": {
                  "type": "number",
                  "operation": "gt"
                }
              }
            ],
            "combinator": "and"
          }
        },
        "notes": "Routes to duplicate handler if PO exists"
      },
      {
        "id": "insert_supabase",
        "name": "Insert PO to Supabase",
        "type": "n8n-nodes-base.supabase",
        "position": [1850, 200],
        "typeVersion": 1,
        "parameters": {
          "operation": "create",
          "tableId": "purchase_orders",
          "sendBinary": false,
          "fieldsUi": {
            "fieldValues": [
              {
                "fieldName": "po_number",
                "fieldValue": "={{ $json.poNumber }}"
              },
              {
                "fieldName": "vendor_name",
                "fieldValue": "={{ $json.vendorName }}"
              },
              {
                "fieldName": "vendor_email",
                "fieldValue": "={{ $json.vendorEmail }}"
              },
              {
                "fieldName": "total_amount",
                "fieldValue": "={{ $json.totalAmount }}"
              },
              {
                "fieldName": "reference",
                "fieldValue": "={{ $json.reference }}"
              },
              {
                "fieldName": "status",
                "fieldValue": "received"
              },
              {
                "fieldName": "email_id",
                "fieldValue": "={{ $json.emailId }}"
              },
              {
                "fieldName": "thread_id",
                "fieldValue": "={{ $json.threadId }}"
              },
              {
                "fieldName": "received_at",
                "fieldValue": "={{ $json.receivedAt }}"
              },
              {
                "fieldName": "line_items",
                "fieldValue": "={{ JSON.stringify($json.lineItems) }}"
              },
              {
                "fieldName": "raw_text_sample",
                "fieldValue": "={{ $json.rawTextSample }}"
              }
            ]
          }
        },
        "notes": "Creates new PO record in Supabase"
      },
      {
        "id": "get_next_invoice_number",
        "name": "Get Next Invoice Number",
        "type": "n8n-nodes-base.code",
        "position": [2050, 200],
        "typeVersion": 1,
        "parameters": {
          "jsCode": `
  // You mentioned current invoice is 58, so next would be 59
  // In production, you'd query Notion or Supabase for the last invoice number
  
  const lastInvoiceNumber = 58; // This should be dynamically fetched
  const nextInvoiceNumber = lastInvoiceNumber + 1;
  
  return [{
    json: {
      ...$json,
      invoiceNumber: nextInvoiceNumber,
      invoiceNumberString: String(nextInvoiceNumber).padStart(3, '0')
    }
  }];`
        },
        "notes": "Generates next invoice number - update to fetch from Notion/Supabase"
      },
      {
        "id": "create_notion_project",
        "name": "Create/Update Notion Project",
        "type": "n8n-nodes-base.notion",
        "position": [2250, 200],
        "typeVersion": 2,
        "parameters": {
          "operation": "create",
          "databaseId": "1e64a17bb7f0807db0f3fe2cf5a6e3ac",
          "propertiesUi": {
            "propertyValues": [
              {
                "key": "Name|title",
                "title": "={{ $json.reference || 'PO ' + $json.poNumber }}"
              },
              {
                "key": "Status|status",
                "statusValue": "PO Received"
              },
              {
                "key": "PO #|rich_text",
                "textContent": "={{ $json.poNumber }}"
              },
              {
                "key": "Demo Fee|number",
                "numberValue": "={{ $json.totalAmount }}"
              },
              {
                "key": "date:Date Received:start|date",
                "date": "={{ $json.receivedAt.split('T')[0] }}",
                "includeTime": false
              },
              {
                "key": "Thread ID|rich_text",
                "textContent": "={{ $json.threadId }}"
              }
            ]
          }
        },
        "notes": "Creates project entry in ESM Projects database"
      },
      {
        "id": "generate_invoice_html",
        "name": "Generate Invoice HTML",
        "type": "n8n-nodes-base.code",
        "position": [2450, 200],
        "typeVersion": 1,
        "parameters": {
          "jsCode": `
  // Generate professional invoice HTML
  const po = $json;
  const invoiceDate = new Date().toISOString().split('T')[0];
  const dueDate = new Date(Date.now() + 30*24*60*60*1000).toISOString().split('T')[0]; // 30 days
  
  const invoiceHtml = \`
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="UTF-8">
    <style>
      @page { size: A4; margin: 20mm; }
      body { 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        color: #333;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
      }
      .header {
        display: flex;
        justify-content: space-between;
        align-items: start;
        border-bottom: 3px solid #333;
        padding-bottom: 20px;
        margin-bottom: 30px;
      }
      .logo-section h1 {
        margin: 0;
        font-size: 2.5em;
        font-weight: 300;
        letter-spacing: -1px;
      }
      .invoice-details {
        text-align: right;
      }
      .invoice-details h2 {
        margin: 0 0 10px 0;
        font-size: 1.8em;
        color: #666;
      }
      .invoice-details p {
        margin: 5px 0;
        font-size: 0.95em;
      }
      .parties {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 40px;
        margin: 30px 0;
      }
      .party h3 {
        color: #666;
        font-size: 0.9em;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 10px;
        font-weight: 600;
      }
      .party p {
        margin: 5px 0;
        font-size: 0.95em;
      }
      .items-table {
        width: 100%;
        border-collapse: collapse;
        margin: 30px 0;
      }
      .items-table th {
        background: #f8f9fa;
        padding: 12px;
        text-align: left;
        font-weight: 600;
        border-bottom: 2px solid #dee2e6;
        font-size: 0.9em;
        text-transform: uppercase;
        letter-spacing: 0.5px;
      }
      .items-table td {
        padding: 15px 12px;
        border-bottom: 1px solid #dee2e6;
      }
      .items-table .description {
        font-weight: 500;
      }
      .items-table .amount {
        text-align: right;
        font-family: 'Courier New', monospace;
      }
      .totals {
        margin-left: auto;
        width: 300px;
        margin-top: 30px;
      }
      .totals-row {
        display: flex;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px solid #eee;
      }
      .totals-row.total {
        border-bottom: none;
        border-top: 2px solid #333;
        margin-top: 10px;
        padding-top: 15px;
        font-size: 1.2em;
        font-weight: 600;
      }
      .payment-info {
        background: #f8f9fa;
        padding: 25px;
        border-radius: 8px;
        margin-top: 40px;
      }
      .payment-info h3 {
        margin-top: 0;
        color: #666;
        font-size: 1.1em;
      }
      .payment-details {
        display: grid;
        grid-template-columns: 120px 1fr;
        gap: 10px;
        margin-top: 15px;
      }
      .payment-details dt {
        font-weight: 600;
        color: #666;
      }
      .payment-details dd {
        margin: 0;
        font-family: 'Courier New', monospace;
      }
      .footer {
        text-align: center;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #dee2e6;
        color: #666;
        font-size: 0.9em;
      }
      .badge {
        display: inline-block;
        padding: 4px 8px;
        background: #28a745;
        color: white;
        border-radius: 4px;
        font-size: 0.8em;
        font-weight: 600;
        margin-left: 10px;
      }
    </style>
  </head>
  <body>
    <div class="header">
      <div class="logo-section">
        <h1>HARRISON SAYERS</h1>
        <p style="margin: 5px 0; color: #666;">Composer & Music Producer</p>
        <p style="margin: 5px 0; color: #666; font-size: 0.9em;">ABN: 89 184 087 850</p>
      </div>
      <div class="invoice-details">
        <h2>INVOICE</h2>
        <p><strong>Invoice #:</strong> \${po.invoiceNumber}</p>
        <p><strong>Date:</strong> \${invoiceDate}</p>
        <p><strong>Due Date:</strong> \${dueDate}</p>
        <p><strong>PO Ref:</strong> \${po.poNumber}</p>
      </div>
    </div>
  
    <div class="parties">
      <div class="party">
        <h3>From</h3>
        <p><strong>Harrison Sayers</strong></p>
        <p>Sydney, NSW</p>
        <p>Australia</p>
        <p>hello@harrisonsayers.com</p>
      </div>
      <div class="party">
        <h3>Bill To</h3>
        <p><strong>Electric Sheep Music Pty Ltd</strong></p>
        <p>Suite 306</p>
        <p>59 Great Buckingham St</p>
        <p>Redfern NSW 2016</p>
        <p>ABN: \${po.abn}</p>
      </div>
    </div>
  
    <table class="items-table">
      <thead>
        <tr>
          <th style="width: 50%;">Description</th>
          <th style="width: 15%; text-align: center;">Qty</th>
          <th style="width: 15%; text-align: right;">Rate</th>
          <th style="width: 20%; text-align: right;">Amount</th>
        </tr>
      </thead>
      <tbody>
        \${po.lineItems.map(item => \`
        <tr>
          <td class="description">
            \${item.description}
            <span class="badge">GST Free</span>
          </td>
          <td style="text-align: center;">\${item.quantity}</td>
          <td class="amount">$\${item.unitPrice.toFixed(2)}</td>
          <td class="amount">$\${item.amount.toFixed(2)}</td>
        </tr>
        \`).join('')}
      </tbody>
    </table>
  
    <div class="totals">
      <div class="totals-row">
        <span>Subtotal:</span>
        <span>$\${po.totalAmount.toFixed(2)}</span>
      </div>
      <div class="totals-row">
        <span>GST (0%):</span>
        <span>$0.00</span>
      </div>
      <div class="totals-row total">
        <span>Total AUD:</span>
        <span>$\${po.totalAmount.toFixed(2)}</span>
      </div>
    </div>
  
    <div class="payment-info">
      <h3>Payment Information</h3>
      <dl class="payment-details">
        <dt>Account Name:</dt>
        <dd>Harrison Sayers</dd>
        <dt>BSB:</dt>
        <dd>082 908</dd>
        <dt>Account No:</dt>
        <dd>143011567</dd>
        <dt>Payment Terms:</dt>
        <dd>Net 30 days</dd>
      </dl>
      <p style="margin-top: 20px; font-style: italic; color: #666;">
        Please include invoice number \${po.invoiceNumber} as payment reference.
      </p>
    </div>
  
    <div class="footer">
      <p>Thank you for your business!</p>
      <p style="font-size: 0.8em; margin-top: 10px;">
        This invoice was automatically generated from PO \${po.poNumber}
      </p>
    </div>
  </body>
  </html>
  \`;
  
  return [{
    json: {
      ...po,
      invoiceHtml,
      invoiceDate,
      dueDate,
      invoiceReady: true
    }
  }];`
        },
        "notes": "Generates professional invoice HTML for PDF conversion"
      },
      {
        "id": "convert_to_pdf",
        "name": "Convert HTML to PDF",
        "type": "n8n-nodes-base.html",
        "position": [2650, 200],
        "typeVersion": 1,
        "parameters": {
          "operation": "generatePDF",
          "html": "={{ $json.invoiceHtml }}",
          "options": {
            "format": "A4",
            "printBackground": true,
            "displayHeaderFooter": false,
            "margin": {
              "top": "20mm",
              "bottom": "20mm",
              "left": "15mm",
              "right": "15mm"
            }
          },
          "dataPropertyName": "invoicePdf"
        },
        "notes": "Converts HTML to PDF using n8n's built-in converter"
      },
      {
        "id": "create_notion_invoice",
        "name": "Create Invoice in Notion",
        "type": "n8n-nodes-base.notion",
        "position": [2850, 200],
        "typeVersion": 2,
        "parameters": {
          "operation": "create",
          "databaseId": "1ea4a17bb7f080689d6cd6eb8536147b",
          "propertiesUi": {
            "propertyValues": [
              {
                "key": "Job Name|title",
                "title": "={{ $json.reference || 'Invoice ' + $json.invoiceNumber }}"
              },
              {
                "key": "Status|status",
                "statusValue": "Draft"
              },
              {
                "key": "Paid|status",
                "statusValue": "Awaiting"
              },
              {
                "key": "userDefined:ID|number",
                "numberValue": "={{ $json.invoiceNumber }}"
              },
              {
                "key": "PO# Mapped|rich_text",
                "textContent": "={{ $json.poNumber.replace('PO-', '') }}"
              },
              {
                "key": "Total Amount|number",
                "numberValue": "={{ $json.totalAmount }}"
              },
              {
                "key": "ESM/PC|select",
                "selectValue": "Electric Sheep Music PTY LTD"
              },
              {
                "key": "date:Invoice Date:start|date",
                "date": "={{ $json.invoiceDate }}",
                "includeTime": false
              },
              {
                "key": "Send Invoice?|select",
                "selectValue": "Send Invoice"
              }
            ]
          }
        },
        "notes": "Creates invoice entry in ESM Invoices database"
      },
      {
        "id": "create_gmail_draft",
        "name": "Create Gmail Draft for Review",
        "type": "n8n-nodes-base.gmail",
        "position": [3050, 200],
        "typeVersion": 2.1,
        "parameters": {
          "operation": "draft",
          "to": "esmusic@dext.cc",
          "subject": "Invoice {{ $json.invoiceNumber }} - {{ $json.reference || $json.poNumber }}",
          "message": `Dear Electric Sheep Music,
  
  Please find attached Invoice #{{ $json.invoiceNumber }} for {{ $json.reference || 'services per PO ' + $json.poNumber }}.
  
  Amount Due: ${{ $json.totalAmount.toFixed(2) }} AUD
  Payment Terms: Net 30 days
  Due Date: {{ $json.dueDate }}
  
  Payment Details:
  Account Name: Harrison Sayers
  BSB: 082 908
  Account: 143011567
  
  Please include invoice number {{ $json.invoiceNumber }} as your payment reference.
  
  Thank you for your business.
  
  Best regards,
  Harrison Sayers`,
          "attachments": "invoicePdf",
          "options": {
            "replyTo": "hello@harrisonsayers.com"
          }
        },
        "notes": "Creates draft email with invoice attached for manual review"
      },
      {
        "id": "create_review_task",
        "name": "Create Review Task",
        "type": "n8n-nodes-base.notion",
        "position": [3250, 200],
        "typeVersion": 2,
        "parameters": {
          "operation": "create",
          "databaseId": "YOUR_TASKS_DATABASE_ID",
          "propertiesUi": {
            "propertyValues": [
              {
                "key": "Name|title",
                "title": "Review & Send Invoice {{ $json.invoiceNumber }}"
              },
              {
                "key": "Status|status",
                "statusValue": "To Do"
              },
              {
                "key": "Due Date|date",
                "date": "={{ new Date(Date.now() + 24*60*60*1000).toISOString().split('T')[0] }}",
                "includeTime": false
              }
            ]
          }
        },
        "notes": "Creates task in Notion to review invoice - UPDATE DATABASE ID"
      },
      {
        "id": "send_notification",
        "name": "Send Notification",
        "type": "n8n-nodes-base.emailSend",
        "position": [3450, 200],
        "typeVersion": 2.1,
        "parameters": {
          "fromEmail": "n8n@harrisonsayers.com",
          "toEmail": "hello@harrisonsayers.com",
          "subject": "📋 New Invoice Ready for Review - #{{ $json.invoiceNumber }}",
          "html": `
  <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
    <h2 style="color: #333;">New Invoice Ready for Review</h2>
    
    <div style="background: #f5f5f5; padding: 20px; border-radius: 8px; margin: 20px 0;">
      <p><strong>Invoice Number:</strong> {{ $json.invoiceNumber }}</p>
      <p><strong>PO Reference:</strong> {{ $json.poNumber }}</p>
      <p><strong>Client:</strong> Electric Sheep Music Pty Ltd</p>
      <p><strong>Amount:</strong> ${{ $json.totalAmount.toFixed(2) }} AUD</p>
      <p><strong>Description:</strong> {{ $json.reference || 'Composer Services' }}</p>
    </div>
    
    <h3>Next Steps:</h3>
    <ol>
      <li>Review the draft in Gmail</li>
      <li>Make any necessary edits</li>
      <li>Send to client when ready</li>
    </ol>
    
    <p style="margin-top: 30px;">
      <a href="https://mail.google.com/mail/u/0/#drafts" style="background: #4285f4; color: white; padding: 10px 20px; text-decoration: none; border-radius: 4px;">Open Gmail Drafts</a>
    </p>
  </div>`,
          "options": {
            "allowUnauthorizedCerts": true
          }
        },
        "notes": "Sends notification email about new invoice"
      },
      {
        "id": "label_processed",
        "name": "Add Processed Label",
        "type": "n8n-nodes-base.gmail",
        "position": [3650, 200],
        "typeVersion": 2.1,
        "parameters": {
          "operation": "addLabels",
          "messageId": "={{ $json.emailId }}",
          "labelIds": ["processed"]
        },
        "notes": "Marks email as processed to avoid reprocessing"
      },
      {
        "id": "handle_duplicate",
        "name": "Handle Duplicate PO",
        "type": "n8n-nodes-base.code",
        "position": [1850, 400],
        "typeVersion": 1,
        "parameters": {
          "jsCode": `
  // Log duplicate for monitoring
  console.log('Duplicate PO detected:', $json.poNumber);
  
  return [{
    json: {
      ...$json,
      isDuplicate: true,
      message: 'PO already exists in system',
      skipped: true
    }
  }];`
        },
        "notes": "Handles duplicate POs - could send notification if needed"
      }
    ],
    "connections": {
      "gmail_trigger_1": {
        "main": [[
          { "node": "merge_triggers", "type": "main", "index": 0 }
        ]]
      },
      "gmail_trigger_2": {
        "main": [[
          { "node": "merge_triggers", "type": "main", "index": 1 }
        ]]
      },
      "merge_triggers": {
        "main": [[
          { "node": "extract_po_data", "type": "main", "index": 0 }
        ]]
      },
      "extract_po_data": {
        "main": [[
          { "node": "download_pdf", "type": "main", "index": 0 }
        ]]
      },
      "download_pdf": {
        "main": [[
          { "node": "parse_pdf", "type": "main", "index": 0 }
        ]]
      },
      "parse_pdf": {
        "main": [[
          { "node": "extract_po_details", "type": "main", "index": 0 }
        ]]
      },
      "extract_po_details": {
        "main": [[
          { "node": "check_duplicate", "type": "main", "index": 0 }
        ]]
      },
      "check_duplicate": {
        "main": [[
          { "node": "check_duplicate_result", "type": "main", "index": 0 }
        ]]
      },
      "check_duplicate_result": {
        "main": [
          [{ "node": "insert_supabase", "type": "main", "index": 0 }],
          [{ "node": "handle_duplicate", "type": "main", "index": 0 }]
        ]
      },
      "insert_supabase": {
        "main": [[
          { "node": "get_next_invoice_number", "type": "main", "index": 0 }
        ]]
      },
      "get_next_invoice_number": {
        "main": [[
          { "node": "create_notion_project", "type": "main", "index": 0 }
        ]]
      },
      "create_notion_project": {
        "main": [[
          { "node": "generate_invoice_html", "type": "main", "index": 0 }
        ]]
      },
      "generate_invoice_html": {
        "main": [[
          { "node": "convert_to_pdf", "type": "main", "index": 0 }
        ]]
      },
      "convert_to_pdf": {
        "main": [[
          { "node": "create_notion_invoice", "type": "main", "index": 0 }
        ]]
      },
      "create_notion_invoice": {
        "main": [[
          { "node": "create_gmail_draft", "type": "main", "index": 0 }
        ]]
      },
      "create_gmail_draft": {
        "main": [[
          { "node": "create_review_task", "type": "main", "index": 0 }
        ]]
      },
      "create_review_task": {
        "main": [[
          { "node": "send_notification", "type": "main", "index": 0 }
        ]]
      },
      "send_notification": {
        "main": [[
          { "node": "label_processed", "type": "main", "index": 0 }
        ]]
      }
    },
    "settings": {
      "executionOrder": "v1",
      "saveDataErrorExecution": "all",
      "saveDataSuccessExecution": "all",
      "saveExecutionProgress": true,
      "saveManualExecutions": true,
      "callerPolicy": "workflowsFromSameOwner"
    }
  }