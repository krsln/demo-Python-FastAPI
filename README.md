# Demo Python FastAPI

A production-style FastAPI application using **uv** for dependency management.

## 🚀 Run locally

```bash
```

````shell
# check
uv --version

uv init

uv add fastapi uvicorn
uv add pydantic-settings
uv add pytest pytest-asyncio

uv sync

uv run pytest tests/test_main.py

uvicorn app.main:app --reload
uv run uvicorn app.main:app --reload
````

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


````