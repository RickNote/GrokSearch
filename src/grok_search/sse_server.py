"""SSE transport with Bearer token auth for remote deployment."""

import os
import uvicorn
from starlette.applications import Starlette
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Mount, Route

from grok_search.server import mcp


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path in ("/", "/health"):
            return await call_next(request)

        auth_token = os.getenv("MCP_AUTH_TOKEN", "")
        if not auth_token:
            return await call_next(request)

        auth_header = request.headers.get("Authorization", "")
        if auth_header != f"Bearer {auth_token}":
            return JSONResponse(status_code=401, content={"error": "Unauthorized"})

        return await call_next(request)


async def health(request: Request) -> Response:
    return Response("OK")


def main():
    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "0.0.0.0")

    print(f"Starting GrokSearch MCP server (SSE + Auth) on {host}:{port}")

    # sse_app() 在 FastMCP 2.x 中可用，SSE 端点位于 /sse
    sse = mcp.sse_app()

    app = Starlette(
        routes=[
            Route("/", health),
            Route("/health", health),
            Mount("/", app=sse),
        ]
    )
    app.add_middleware(AuthMiddleware)

    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
