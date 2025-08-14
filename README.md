# demo-python-fastapi

````shell
# check
uv --version

uv init

uv add fastapi uvicorn
uv add pydantic-settings

uv add pytest pytest-asyncio
uv add httpx

uv sync

uv run uvicorn main:app --reload
````

## Access Swagger UI

http://127.0.0.1:8000/docs
http://127.0.0.1:8000/openapi.json

## Dockerize

````shell
docker build -t demo-python-fastapi .
docker run -p 8000:8000 demo-python-fastapi
````

## Jenkinsfile

````shell
uv run pytest tests/test_main.py


````