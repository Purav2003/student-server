from fastapi import Request
from fastapi.responses import JSONResponse, RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware
from utils.jwt import decode_access_token
import re

EXEMPT_PATHS = [
    re.compile(r"^/api/auth/login$"),
    re.compile(r"^/api/auth/signup$"),
    re.compile(r"^/docs"),         
    re.compile(r"^/openapi.json"),
]

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        if request.method == "OPTIONS":
            return await call_next(request)

        if any(pattern.match(path) for pattern in EXEMPT_PATHS):
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        print(f"Authorization header: {auth_header}")

        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"detail": "Authorization token missing"})

        token = auth_header.split(" ")[1]
        print(f"Decoding token: {token}")
        payload = decode_access_token(token)
        print(f"Decoded payload: {payload}")

        if not payload:
            return JSONResponse(status_code=401, content={"detail": "Invalid or expired token"})

        request.state.user = payload

        return await call_next(request)
