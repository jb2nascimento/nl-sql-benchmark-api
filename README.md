# NL → SQL Compensation Benchmark API

A prototype backend service that converts natural language compensation
queries into structured benchmark lookups while enforcing guardrails to
prevent hallucinated or unreliable outputs.

The system demonstrates how a compensation platform could allow users to
query salary benchmarks using natural language while ensuring responses
are derived exclusively from validated structured datasets.

Use Case: AI-assisted developer tool for translating natural language questions into SQL queries for faster database exploration.

------------------------------------------------------------------------

# Problem

Compensation benchmarking platforms typically store structured salary
datasets but require users to manually configure multiple filters to
retrieve insights.

For example, a user may want to ask:

> What is the compensation range for Senior Backend Engineers in London?

Instead of manually selecting:

-   role title\
-   seniority level\
-   location\
-   percentile metrics

This project explores an alternative interaction model where users can
query compensation data using natural language.

The system converts natural language questions into structured queries
and retrieves benchmark results from a controlled dataset.

------------------------------------------------------------------------

# Solution Overview

The system processes queries through a structured pipeline designed to
maintain deterministic behavior and prevent hallucinated results.

Pipeline:

1.  Natural language question is received by the API\
2.  A deterministic parser extracts structured dimensions from the
    query\
3.  Guardrails validate whether the query contains sufficient
    information\
4.  A repository retrieves benchmark data from a structured dataset\
5.  The API returns a formatted benchmark response

------------------------------------------------------------------------

# Architecture

    User Question
          ↓
    FastAPI Endpoint
          ↓
    Query Parser
          ↓
    Structured Query (role, location, seniority, metric)
          ↓
    Guardrail Validation
          ↓
    Benchmark Repository
          ↓
    Formatted API Response

The repository layer is abstracted to allow replacing the current
in-memory dataset with a SQL-backed implementation such as PostgreSQL or
AWS RDS.

------------------------------------------------------------------------

# Example Request

POST `/query`

``` json
{
  "question": "Show P75 compensation for Staff Data Engineer in Berlin"
}
```

------------------------------------------------------------------------

# Example Response

``` json
{
  "summary": "P75 compensation benchmark for Staff Data Engineer in Berlin",
  "insufficient_data": false,
  "parsed_role_title": "Data Engineer",
  "parsed_seniority_level": "Staff",
  "parsed_location": "Berlin",
  "parsed_metric_requested": "p75",
  "benchmark": {
    "currency": "EUR",
    "p25_base_salary": 90000,
    "p50_base_salary": 105000,
    "p75_base_salary": 120000,
    "p90_base_salary": 135000,
    "data_points": 89
  },
  "notes": [
    "Based on 89 data points"
  ]
}
```

------------------------------------------------------------------------

# Project Structure

    app
     ├── api
     │   ├── routes
     │   └── schemas
     │
     ├── application
     │   ├── dto
     │   ├── ports
     │   └── use_cases
     │
     ├── domain
     │   ├── enums
     │   └── models
     │
     ├── infrastructure
     │   └── external
     │
     └── core
         ├── config
         └── logging

Architecture layers:

  Layer            Responsibility
  ---------------- ---------------------------------------------
  API              HTTP interface and request/response schemas
  Application      Use cases and business workflow
  Domain           Core business entities and enums
  Infrastructure   Data sources and external integrations
  Core             Configuration and logging

------------------------------------------------------------------------

# Running the Project

### Clone the repository

``` bash
git clone https://github.com/YOUR_USER/nl-sql-benchmark-api.git
cd nl-sql-benchmark-api
```

### Create a virtual environment

``` bash
python -m venv .venv
```

Activate it:

**Windows**

``` bash
.venv\Scripts\activate
```

**Mac/Linux**

``` bash
source .venv/bin/activate
```

### Install dependencies

``` bash
pip install -r requirements.txt
```

### Run the API

``` bash
uvicorn app.main:app --reload
```

### Open Swagger UI

    http://localhost:8000/docs


### Development

```bash
ruff check . --fix
black .
pytest
```

------------------------------------------------------------------------

# Guardrails

To ensure reliable outputs and prevent hallucinated results, the system
implements several safeguards:

-   Queries must contain required dimensions (role title and location)
-   If no matching benchmark record exists, the system returns an
    explicit `insufficient_data` response
-   Salary values are never generated or inferred
-   All responses originate exclusively from the structured dataset

These guardrails ensure that the system remains deterministic and
auditable.

------------------------------------------------------------------------

# Dataset

The prototype currently uses an **in-memory benchmark dataset**
containing sample compensation records.

This design allows validating the full query pipeline without requiring
a database.

The repository abstraction allows easily replacing the dataset with:

-   PostgreSQL
-   AWS RDS
-   Data warehouse sources
-   external compensation APIs

------------------------------------------------------------------------

# Future Improvements

Potential next steps include:

-   Replace the in-memory repository with a PostgreSQL-backed
    implementation
-   Add semantic parsing using an LLM for more flexible queries
-   Introduce confidence scoring for parsed query dimensions
-   Support fuzzy matching for role titles and locations
-   Add export functionality for PDF benchmark reports
-   Implement query caching and performance optimizations

------------------------------------------------------------------------

# Key Concepts Demonstrated

This prototype demonstrates several architectural patterns relevant for
AI-assisted data systems:

-   Natural Language → Structured Query conversion
-   Deterministic guardrails to prevent hallucinated data
-   Repository pattern for data abstraction
-   Layered architecture separating domain, application, and
    infrastructure
-   API-first design for integration with external frontends

------------------------------------------------------------------------

# License

MIT License
