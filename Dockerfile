FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY src/ src/

RUN pip install --no-cache-dir . && python -c "import fastmcp; print('fastmcp version:', fastmcp.__version__)"

EXPOSE 8000

CMD ["python", "-m", "grok_search.sse_server"]
