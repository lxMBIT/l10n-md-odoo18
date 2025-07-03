# Moldova e-invoice.md API Structure

## Overview
This document describes the integration API for Moldova's e-invoice.md, following the approach of l10n_it and l10n_lt modules.

## Endpoints
- **POST /api/einvoice/send**: Send an electronic invoice to e-invoice.md
- **GET /api/einvoice/status/{einvoice_md_id}**: Get the status of a sent invoice
- **GET /api/einvoice/download/{einvoice_md_id}**: Download the XML of a sent invoice

## Authentication
- OAuth2 or API Key (to be specified by e-invoice.md provider)

## Request/Response Examples
### Send Invoice
POST /api/einvoice/send
```json
{
  "invoice_number": "INV-2025-001",
  "partner_vat": "1002601000123",
  "date_invoice": "2025-07-03",
  "amount_total": 1234.56,
  "currency": "MDL",
  "xml_base64": "..."
}
```

### Status Response
```json
{
  "einvoice_md_id": "MD-1234567890",
  "status": "accepted",
  "message": "Invoice accepted by e-invoice.md"
}
```

### Download Response
Base64-encoded XML file.

## Error Handling
Standard HTTP error codes and JSON error messages.

