from typing import Dict, Tuple, List

from fastapi import Depends
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

from lms.auth.jwt_bearer import JWTBearer
from lms.database.models import Admin
# from app.auth.password_bearer import get_current_user
from .middleware.auth_middleware import FastAPIUser

jwt_token = JWTBearer()

# dependencies = [Depends(jwt_token), Depends(get_current_user)]
dependencies = [Depends(jwt_token)]
depends = Depends(jwt_token)


# The method you have to provide
async def verify_header(headers: Dict) -> Tuple[List[str], FastAPIUser]:
    auth = headers["Authorization"]
    try:
        scheme, credentials = auth.split()
        if scheme.lower() != 'bearer':
            return
        decoded = decode_access_token(credentials.credentials)
    except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
        raise AuthenticationError('Invalid token or expired token')

    user = await Admin.find_one(Admin.email == decoded.sub)
    if user is None:
        raise AuthenticationError('Could not find user')

    user = FastAPIUser(full_name=user.fullname, email=user.email, user_id=user.id)
    scopes = ["authenticated"]
    return scopes, user
