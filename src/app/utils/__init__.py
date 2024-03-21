from datetime import datetime, timedelta, timezone
from typing import Annotated, Union

from jose import JWTError, jwt

from src.app.core.config import settings


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(data)}
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt
