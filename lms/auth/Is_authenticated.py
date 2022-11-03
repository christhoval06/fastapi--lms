from typing import Any

import strawberry
from strawberry.permission import BasePermission
from strawberry.types import Info

from .verify_token import VerifyToken


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    async def has_permission(self, source: Any, info: Info, **kwargs) -> bool:
        request: Union[Request, WebSocket] = info.context.request
        print(request.headers)
        if "Authorization" in request.headers:
            print(request.headers['Authorization'])
            result = VerifyToken(request.headers['Authorization'][7:]).verify()
            if result == "error":
                print(result.message)
                return False
            if result.sub:
                print(result)
                return True
        return False
