from datetime import datetime, timedelta
from typing import Union, Any, Optional

from jose import jwt, JWTError
from pydantic import ValidationError

from app.config.config import settings
from app.database.schemas import TokenPayload


def generate_jwt(data: Union[str, Any], secret_key: str, expires_delta: int = None) -> str:
    expires_delta = datetime.utcnow() + timedelta(minutes=expires_delta)

    to_encode = {"exp": expires_delta, "sub": str(data)}
    return str(jwt.encode(to_encode, secret_key, settings.algorithm))

def create_access_token(subject: Union[str, Any]) -> str:
    return generate_jwt(subject, settings.jwt_secret_key, settings.access_token_expire_minutes)


def create_refresh_token(subject: Union[str, Any]) -> str:
    return generate_jwt(subject, settings.jwt_refresh_secret_key, settings.refresh_token_expires_minutes)


def verify_token(token: str) -> bool:
    is_token_valid: bool = False

    payload = decode_access_token(token)
    if payload:
        is_token_valid = True
    return is_token_valid


def decode_jwt(token: str, secret_key: str) -> Optional[TokenPayload]:
    try:
        payload = jwt.decode(token.encode(), secret_key, algorithms=[settings.algorithm])
        token_data = TokenPayload(**payload)
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            return None

        return token_data
    except(JWTError, ValidationError):
        return None


def decode_access_token(token: str) -> Optional[TokenPayload]:
    return decode_jwt(token, settings.jwt_secret_key)


def decode_refresh_token(token: str) -> Optional[TokenPayload]:
    return decode_jwt(token, settings.jwt_refresh_secret_key)
