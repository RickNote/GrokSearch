FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY src/ src/

# 先安装所有依赖，再强制锁定 fastmcp 到本地一致的版本
RUN pip install --no-cache-dir . && \
    pip install --no-cache-dir --force-reinstall "fastmcp==2.12.5"

EXPOSE 8000

CMD ["python", "-m", "grok_search.sse_server"]
