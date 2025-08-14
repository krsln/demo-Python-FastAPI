# Use slim python image
FROM python:3.12-slim AS base

# Install uv
RUN pip install --no-cache-dir uv

WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install deps exactly as in uv.lock
RUN uv sync --frozen --no-dev

# Copy app code
COPY app ./app

# Expose port
EXPOSE 8000

# Run app
CMD [".venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
