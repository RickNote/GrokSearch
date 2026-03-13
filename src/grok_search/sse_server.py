"""SSE transport entry-point for remote deployment (Railway / Fly.io / etc.)."""

import os
import fastmcp
from grok_search.server import mcp


def main():
    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "0.0.0.0")
    print(f"FastMCP version: {fastmcp.__version__}")
    print(f"ENV CHECK - GROK_API_URL set: {bool(os.getenv('GROK_API_URL'))}")
    print(f"ENV CHECK - GROK_API_KEY set: {bool(os.getenv('GROK_API_KEY'))}")
    print(f"ENV CHECK - GROK_MODEL: {os.getenv('GROK_MODEL', 'not set')}")
    print(f"Starting GrokSearch MCP server (SSE) on {host}:{port}")
    mcp.run(transport="sse", host=host, port=port)


if __name__ == "__main__":
    main()
