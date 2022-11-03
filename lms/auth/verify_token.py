from dataclasses import dataclass
from typing import Union

from lms.database import models
from lms.database.schemas import TokenPayload
from lms.utils.jwt import decode_access_token


@dataclass
class TokenDataError:
    status: str
    message: str


class VerifyToken:
    """Does all the token verification using PyJWT"""

    def __init__(self, token):
        self.token = token

    def verify(self) -> Union[TokenPayload, TokenDataError]:
        token_data = decode_access_token(self.token)
        if token_data is None:
            return TokenDataError(status="error", message="Invalid token or expired token")

        return token_data
