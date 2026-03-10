# NL SQL Benchmark API

Backend example project for natural language querying over a structured compensation benchmark dataset.

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Local Development

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
