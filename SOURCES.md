# Data Source Research

## 1. SAP Fuel and Procurement Data

### Researched Format
CSV export representing SAP flat-file style exports.

### Research Notes
Typical SAP exports contain:
- plant codes
- fuel categories
- inconsistent units
- vendor information
- procurement quantities

### Sample Data Included
- Diesel
- Petrol
- Natural Gas
- Coal
- Vendor names
- Plant identifiers

### Real-World Challenges
- inconsistent units
- missing quantities
- multilingual headers
- ERP export inconsistencies

---

# 2. Utility Electricity Data

### Researched Format
CSV utility portal export.

### Research Notes
Typical utility exports contain:
- billing periods
- meter identifiers
- electricity usage (kWh)
- tariffs
- cost information

### Sample Data Included
- office facilities
- industrial plants
- meter IDs
- electricity usage
- tariff categories

### Real-World Challenges
- billing periods not aligned with calendar months
- missing meter readings
- inconsistent tariff structures

---

# 3. Corporate Travel Data

### Researched Format
Travel platform style CSV export inspired by Concur/Navan systems.

### Research Notes
Corporate travel systems usually provide:
- employee IDs
- travel mode
- airport codes
- trip classes
- distances

### Sample Data Included
- flight travel
- hotel stays
- taxi trips
- airport codes
- business/economy classes

### Real-World Challenges
- missing distance data
- inconsistent airport naming
- multiple emissions methodologies

---

# Ingestion Approach

## Selected Method
CSV file upload through frontend dashboard.

### Reason
CSV upload is:
- realistic
- simple to demo
- commonly used in enterprise ESG onboarding workflows

---

# Future Improvements

Potential future enhancements:
- direct SAP API integrations
- utility portal APIs
- Concur/Navan OAuth integrations
- automated emissions factor calculations
- asynchronous ingestion pipelines