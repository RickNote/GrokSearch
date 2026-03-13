"""Streamable-HTTP transport entry-point for remote deployment."""

import os
import fastmcp
import uvicorn
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Mount, Route

from grok_search.server import mcp


async def health(request: Request) -> Response:
    return Response("OK")


def main():
    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "0.0.0.0")
    print(f"FastMCP version: {fastmcp.__version__}")
    print(f"ENV CHECK - GROK_API_URL set: {bool(os.getenv('GROK_API_URL'))}")
    print(f"ENV CHECK - GROK_API_KEY set: {bool(os.getenv('GROK_API_KEY'))}")
    print(f"Starting GrokSearch MCP server (streamable-http) on {host}:{port}")

    mcp_app = mcp.http_app(path="/mcp")

    app = Starlette(
        routes=[
            Route("/", health),
            Route("/health", health),
            Mount("/", app=mcp_app),
        ]
    )

    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
