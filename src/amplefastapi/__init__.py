import time
from datetime import datetime

import httpagentparser
import httpx
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp


class AmpleMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, project_id: str):
        super().__init__(app)
        self.project_id = project_id

    async def record_stats(
        self,
        request_time: float,
        response_time: float,
        request_details: dict,
        response_status_code: int,
    ):

        async with httpx.AsyncClient(
            base_url="https://ample-analytics.ew.r.appspot.com"
        ) as client:
            data = {
                "project_id": self.project_id,
                "request_time": datetime.utcfromtimestamp(request_time).isoformat(),
                "response_time": datetime.utcfromtimestamp(response_time).isoformat(),
                "metadata": {
                    "request_details": request_details,
                    "status_code": response_status_code,
                },
            }
            await client.post(url="/analytics", json=data)

    async def dispatch(self, request: Request, call_next):
        request_time = time.time()
        response: Response = await call_next(request)
        response_time = time.time()
        platform, user_agent = httpagentparser.simple_detect(
            request.headers.get("user-agent")
        )
        request_details = {
            "method": request.method,
            "origin": request.client.host,
            "user_agent": user_agent,
            "platform": platform,
            "endpoint": request.url.path,
        }
        await self.record_stats(
            request_time,
            response_time,
            request_details,
            response.status_code,
        )
        return response
