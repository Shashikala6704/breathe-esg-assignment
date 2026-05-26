# Breathe ESG Data Ingestion Prototype

## Overview

This project is a prototype ESG data ingestion and analyst review platform built for the Breathe ESG assignment.

The system allows ESG analysts to:

- Upload ESG source CSV files
- Normalize activity data
- Detect suspicious records
- Review uploaded emissions activities
- Approve or reject records through a dashboard

---

# Features

## CSV Upload
Supports uploading ESG activity CSV files from:
- SAP Fuel / Procurement systems
- Utility electricity systems
- Corporate travel systems

---

# Data Processing

The backend:
- parses uploaded CSV files
- stores raw source records
- normalizes activity data
- flags suspicious records

---

# Suspicious Record Detection

Rows with:
- missing quantities
- zero values

are automatically marked as suspicious for analyst review.

---

# Analyst Dashboard

The React dashboard provides:
- KPI summary cards
- suspicious row highlighting
- approval workflow
- activity review table

---

# Tech Stack

## Backend
- Django
- Django REST Framework
- Pandas
- SQLite

## Frontend
- React
- Vite
- Axios

## Version Control
- Git
- GitHub

---

# Project Structure

```text
backend/
frontend/
sample_data/

MODEL.md
DECISIONS.md
TRADEOFFS.md
SOURCES.md
README.md


---

# Setup Instructions

## Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install django djangorestframework pandas django-cors-headers psycopg2-binary

python manage.py migrate

python manage.py runserver
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# API Endpoints

## Upload CSV

```text
POST /api/upload/
```

## Get Activities

```text
GET /api/activities/
```

## Update Activity Status

```text
POST /api/activities/<id>/status/
```

---

# Sample Data

Sample ESG CSV datasets are available in:

```text
sample_data/
```

Included datasets:
- sap_fuel_data.csv
- utility_electricity_data.csv
- travel_activity_data.csv

---

# Current Features

- CSV ingestion workflow
- ESG activity normalization
- Suspicious row detection
- Analyst review dashboard
- Approve / Reject workflow
- Search and filtering
- KPI summary cards
- GitHub version control

---

# Future Improvements

Potential future enhancements:
- async ingestion pipelines
- PostgreSQL production deployment
- authentication & authorization
- emissions factor engine
- AI anomaly detection
- enterprise ESG integrations
- charts and analytics

---

# Author

Shashikala6704