# Technical Decisions

## Backend Framework

### Decision
Used Django + Django REST Framework for backend API development.

### Reason
- Fast API development
- Built-in admin support
- ORM support
- Easy CSV ingestion handling
- Strong ecosystem for enterprise applications

---

# Frontend Framework

### Decision
Used React with Vite.

### Reason
- Fast development experience
- Lightweight setup
- Easy API integration using Axios
- Modern UI rendering

---

# Database Choice

### Decision
Used SQLite for prototype implementation.

### Reason
- Simple setup
- No additional database configuration required
- Suitable for assignment prototype

Future production deployment can migrate to PostgreSQL.

---

# Data Processing

### Decision
Used Pandas for CSV parsing and validation.

### Reason
- Efficient CSV handling
- Easy row validation
- Supports scalable data transformation workflows

---

# Suspicious Record Detection

### Decision
Records with missing or zero quantity values are marked as suspicious.

### Reason
Helps ESG analysts identify incomplete or potentially invalid emissions records before approval.

---

# API Design

### Decision
REST APIs were designed for:
- CSV upload
- Activity retrieval
- Status updates

### Reason
Simple integration between frontend dashboard and backend services.

---

# UI Design

### Decision
Implemented analyst review dashboard with:
- KPI cards
- status badges
- suspicious row highlighting
- approve/reject actions

### Reason
Improves ESG analyst workflow and review efficiency.

---

# Git Version Control

### Decision
Used Git + GitHub repository management.

### Reason
- Proper version tracking
- Collaboration readiness
- Professional project delivery