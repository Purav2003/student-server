from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from utils.jwt import decode_access_token
import re

EXEMPT_PATHS = [
    re.compile(r"^/api/auth/login$"),
    re.compile(r"^/api/auth/signup$"),
]

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        # Allow exempted paths (login/signup)
        for pattern in EXEMPT_PATHS:
            if pattern.match(path):
                return await call_next(request)

        # Get token from Authorization header
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"detail": "Authorization token missing"})

        token = auth_header.split(" ")[1]
        payload = decode_access_token(token)

        if not payload:
            return JSONResponse(status_code=401, content={"detail": "Invalid or expired token"})

        # You can attach user info to request state if needed
        request.state.user = payload

        return await call_next(request)
