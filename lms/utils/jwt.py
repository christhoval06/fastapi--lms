from datetime import datetime, timedelta
from typing import Union, Any, Optional

from jose import jwt, JWTError
from pydantic import ValidationError

from lms.database.schemas import TokenPayload
from lms.settings import settings


def generate_jwt(data: Union[str, Any], secret_key: str, expires_delta: int = None) -> str:
    expires_delta = datetime.utcnow() + timedelta(minutes=expires_delta)

    to_encode = {"exp": expires_delta, "sub": str(data)}
    return str(jwt.encode(to_encode, secret_key, settings.ALGORITHM))


def create_access_token(subject: Union[str, Any]) -> str:
    return generate_jwt(subject, settings.JWT_SECRET_KEY, settings.ACCESS_TOKEN_EXPIRE_MIN)


def create_refresh_token(subject: Union[str, Any]) -> str:
    return generate_jwt(subject, settings.JWT_REFRESH_SECRET_KEY, settings.REFRESH_TOKEN_EXPIRE_MIN)


def verify_token(token: str) -> bool:
    is_token_valid: bool = False

    payload = decode_access_token(token)
    if payload:
        is_token_valid = True
    return is_token_valid


def decode_jwt(token: str, secret_key: str) -> Optional[TokenPayload]:
    try:
        payload = jwt.decode(token.encode(), secret_key, algorithms=[settings.ALGORITHM])
        token_data = TokenPayload(**payload)
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            return None

        return token_data
    except(JWTError, ValidationError):
        return None


def decode_access_token(token: str) -> Optional[TokenPayload]:
    return decode_jwt(token, settings.JWT_SECRET_KEY)


def decode_refresh_token(token: str) -> Optional[TokenPayload]:
    return decode_jwt(token, settings.JWT_REFRESH_SECRET_KEY)
