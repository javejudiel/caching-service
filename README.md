Caching Service - FastAPI Microservice

Overview

# Caching Service

A small FastAPI microservice that generates deterministic payloads from two input lists, caches intermediate transformation results, and reuses payload identifiers for identical inputs.

This repository demonstrates API design, caching, persistence (SQLite), testing, and containerization.

## Features

- FastAPI REST API with OpenAPI docs
- Deterministic payload IDs for identical inputs
- Caching of transformed values to avoid repeated work
- SQLite persistence (lightweight, zero-config)
- Unit tests with pytest
- Docker image for easy deployment

## Quick Start

Prerequisites: Python 3.11 (recommended) or Docker.

Run with Docker (recommended):

```powershell
docker build -t caching-service .
docker run -p 8000:8000 caching-service
```

Open the API docs at: http://localhost:8000/docs

Run locally without Docker:

```powershell
py -3.11 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API

POST /payload
- Request body example:

```json
{
	"list_1": ["first string", "second string", "third string"],
	"list_2": ["other string", "another string", "last string"]
}
```

- Response:

```json
{ "id": "<payload_id>" }
```

GET /payload/{id}
- Response example:

```json
{ "output": "FIRST STRING, OTHER STRING, SECOND STRING, ANOTHER STRING, THIRD STRING, LAST STRING" }
```

Notes:
- The service uppercases and interleaves transformed strings from the two lists.
- If the same input pair is submitted again, the existing `id` is returned (identifier reuse).

## Project Structure

- app/
	- main.py — FastAPI app and routes
	- cache.py — caching helpers
	- crud.py — DB operations
	- database.py — DB setup
	- models.py — SQLModel models
	- schemas.py — Pydantic schemas
- tests/ — pytest test suite
- Dockerfile
- requirements.txt
- README.md

## Tests

Run tests from the project root:

```powershell
pytest
```

## Persistence

- SQLite is used by default for simplicity. When running in Docker, database files persist for the container lifetime unless you mount a host volume.

## Testing and Tradeoffs

- Unit and integration tests focus on API behavior and caching correctness.
- The transformer function is intentionally simple to simulate an external dependency.
- SQLite was chosen over PostgreSQL to reduce setup complexity for this assessment.

## AI Usage Disclosure

AI tools were used for:

- Clarifying FastAPI and SQLModel patterns
- Reviewing code structure and edge cases

All core logic, design decisions, and implementation were written and reviewed manually.
