# Demo Python FastAPI

A production-style FastAPI application using **uv** for dependency management.

````shell
# check
uv --version

uv init

uv add fastapi uvicorn
uv add pydantic-settings
uv add pytest pytest-asyncio

uv sync
````

## 🚀 Run locally

```bash

uvicorn app.main:app --reload
uv run uvicorn app.main:app --reload
```

## Test

```bash
uv run pytest tests/test_main.py
uv run pytest tests
```

## Access Swagger UI

http://127.0.0.1:8000/docs  
http://127.0.0.1:8000/openapi.json

## Dockerize

````shell
# ✓
docker build -t demo-python-fastapi .
docker run -d --name demo-python-api -p 8000:8000 demo-python-fastapi

````

## Jenkins file

````shell
TODO: make it work!!
tested on jenkins on docker.. failed
````