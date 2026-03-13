"""SSE transport entry-point for remote deployment (Railway / Fly.io / etc.)."""

import os
from grok_search.server import mcp


def main():
    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "0.0.0.0")
    print(f"Starting GrokSearch MCP server (SSE) on {host}:{port}")
    mcp.run(transport="sse", host=host, port=port)


if __name__ == "__main__":
    main()
