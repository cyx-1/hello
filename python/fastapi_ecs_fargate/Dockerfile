# Line 1: Use official Python runtime as base image
FROM python:3.11-slim

# Line 4: Set working directory in container
WORKDIR /app

# Line 7: Install uv for fast Python package management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Line 10: Copy application file
COPY main_fastapi_ecs.py .

# Line 13: Install dependencies using uv
# uv will read inline script metadata from main_fastapi_ecs.py
RUN uv pip install --system fastapi>=0.115.0 uvicorn[standard]>=0.32.0

# Line 17: Expose port 8000 for the application
EXPOSE 8000

# Line 20: Create non-root user for security
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Line 24: Health check configuration for container health monitoring
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

# Line 28: Run the application
CMD ["uvicorn", "main_fastapi_ecs:app", "--host", "0.0.0.0", "--port", "8000"]
