# Tradeoffs

## SQLite vs PostgreSQL

### Chosen
SQLite

### Tradeoff
SQLite is simple and fast for prototype development but is not ideal for large-scale concurrent enterprise workloads.

### Why Accepted
The assignment focuses on prototype functionality rather than production-scale deployment.

---

# Synchronous CSV Processing

### Chosen
CSV processing occurs synchronously during upload.

### Tradeoff
Large files may increase API response time.

### Why Accepted
Simplifies implementation for prototype delivery.

Future versions can use:
- Celery
- background workers
- asynchronous ingestion pipelines

---

# Simple Suspicious Detection Logic

### Chosen
Suspicious records are detected using missing or zero quantity values.

### Tradeoff
Detection logic is basic and may not capture complex ESG anomalies.

### Why Accepted
Provides a clear demonstration of review workflow functionality.

Future improvements may include:
- AI anomaly detection
- threshold validation
- rule engines

---

# Static Emission Logic

### Chosen
Emission factor and CO2e calculations are currently placeholders.

### Tradeoff
The prototype focuses more on ingestion and review workflow than emissions calculation accuracy.

### Why Accepted
Keeps architecture modular while allowing future integration with official emissions factor libraries.

---

# Frontend State Management

### Chosen
Used React local state management.

### Tradeoff
May become difficult to manage in large enterprise dashboards.

### Why Accepted
The current application size is small and manageable.

Future versions can adopt:
- Redux
- Zustand
- React Query

---

# Authentication

### Chosen
No authentication implemented.

### Tradeoff
Not suitable for production ESG systems.

### Why Accepted
The assignment primarily evaluates ingestion architecture and review workflows.

Future versions can integrate:
- JWT authentication
- role-based access control
- SSO integration