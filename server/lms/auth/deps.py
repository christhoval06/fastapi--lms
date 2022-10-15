from fastapi import Depends

from app.auth.jwt_bearer import JWTBearer

# from app.auth.password_bearer import get_current_user

jwt_token = JWTBearer()

# dependencies = [Depends(jwt_token), Depends(get_current_user)]
dependencies = [Depends(jwt_token)]
depends = Depends(jwt_token)
