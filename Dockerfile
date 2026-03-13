FROM python:3.12-slim

WORKDIR /app

# 安装依赖
COPY pyproject.toml .
COPY src/ src/

RUN pip install --no-cache-dir .

# 暴露端口（Railway 会通过 PORT 环境变量指定实际端口）
EXPOSE 8000

# 启动 SSE 模式的 MCP 服务器
CMD ["python", "-m", "grok_search.sse_server"]
