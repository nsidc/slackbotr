from typing import Any

from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt
from loguru import logger

# TODO: JWT_EXPIRY_MINUTES ?
from slackbotr.constants.auth import JWT_ALGORITHM, JWT_DATA, JWT_SECRET_KEY

# Learn more about JWT payload:
#    https://jwt.io/introduction
JWT_PAYLOAD = {
    # Subject:
    'sub': JWT_DATA,
    # Expiration (currently none):
    # 'exp': JWT_EXPIRY_MINUTES,
}


def generate_jwt() -> str:
    token = jwt.encode(
        JWT_PAYLOAD,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )
    return token


def validate_jwt(token: str) -> bool:
    # An invalid JWT string could cause the decode to raise
    try:
        if decode_jwt(token) == JWT_PAYLOAD:
            return True
    except Exception as e:
        logger.exception(e)
        return False

    return False


def decode_jwt(token: str) -> Any:
    contents = jwt.decode(
        token,
        JWT_SECRET_KEY,
        algorithms=[JWT_ALGORITHM],
    )
    return contents


class JWTBearer(HTTPBearer):
    def __init__(self):
        super().__init__(auto_error=True)

    async def __call__(self, request: Request) -> None:
        # The parent class extracts credentials from the header and does some simple
        # validation, like ensuring an 'Authorization: Bearer' header is passed.
        credentials: HTTPAuthorizationCredentials | None = await super().__call__(
            request
        )

        # If `auto_error` is `False`, the parent class could return `None` for
        # credentials.
        if not credentials:
            raise HTTPException(
                status_code=403,
                detail='No credentials provided.',
            )

        # Check that the credentials passed in are valid for this app
        if not validate_jwt(credentials.credentials):
            raise HTTPException(
                status_code=403,
                detail='Invalid or expired token.',
            )
