# Data Model Design

## Overview

The ESG ingestion platform is designed to collect, normalize, review, and validate emissions activity data from multiple enterprise systems such as SAP, utility providers, and travel systems.

The platform follows a layered ingestion approach:

1. Source System
2. Ingestion Batch
3. Raw Records
4. Normalized Activity Records

This structure helps maintain traceability between uploaded source files and normalized ESG activity data.

---

# Entities

## 1. SourceSystem

Stores information about the external system providing ESG data.

### Fields
- id
- name
- source_type
- created_at

### Purpose
Helps identify where uploaded ESG data originated from.

Examples:
- SAP
- Utility Provider
- Travel Vendor

---

## 2. IngestionBatch

Represents one uploaded CSV ingestion event.

### Fields
- id
- source_system
- file_name
- uploaded_at

### Purpose
Tracks uploaded files and groups raw records belonging to the same ingestion operation.

---

## 3. RawRecord

Stores original uploaded CSV row data before normalization.

### Fields
- id
- batch
- row_number
- raw_payload
- created_at

### Purpose
Preserves original source data for:
- auditing
- traceability
- debugging
- compliance review

---

## 4. NormalizedActivity

Stores cleaned and normalized ESG activity records.

### Fields
- id
- raw_record
- source_type
- scope
- activity_type
- quantity
- original_unit
- normalized_quantity
- normalized_unit
- emission_factor
- co2e
- status
- suspicious_reason
- created_at

### Purpose
Represents normalized emissions activity data used by ESG analysts.

---

# Relationships

## SourceSystem → IngestionBatch
One source system can have many ingestion batches.

## IngestionBatch → RawRecord
One ingestion batch can contain many raw records.

## RawRecord → NormalizedActivity
One raw record maps to one normalized activity record.

---

# Design Decisions

- Raw source data is preserved for audit traceability.
- Normalized records are stored separately from raw ingestion data.
- Suspicious records are flagged during ingestion.
- Status workflow supports analyst review and approvals.
- The architecture supports future integrations with additional ESG systems.

---

# Scalability Considerations

The design can be extended to support:
- large CSV uploads
- asynchronous processing
- multiple ESG scopes
- automated emissions factor calculation
- enterprise audit workflows