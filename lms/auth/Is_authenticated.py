from typing import Any

import strawberry
from strawberry.permission import BasePermission
from strawberry.types import Info

from .verify_token import VerifyToken


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    async def has_permission(self, source: Any, info: Info, **kwargs) -> bool:
        request: Union[Request, WebSocket] = info.context.request
        if "Authorization" in request.headers:
            result = VerifyToken(request.headers['Authorization'][7:]).verify()
            if result.status == "error":
                return False
            if result.sub:
                return True
        return False
