from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import ValidationError
from sqlmodel import Session, inspect
from typing_extensions import Annotated

from src.app.core.config import settings
from src.app.db.connection import Connector
from src.app.models import TokenPayload, User

connector = Connector(settings.DBTYPE)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")


def get_session():
    with Session(connector.engine) as session:
        yield session


def get_inspector():
    yield connector.inspector


SessionDep = Annotated[Session, Depends(get_session)]
InsepectDep = Annotated[inspect, Depends(get_inspector)]
SecurityDep = Annotated[OAuth2PasswordBearer, Depends(oauth2_scheme)]


async def get_current_user(session: SessionDep, token: SecurityDep):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        print("PAY LOAD: ", payload)
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    user = session.get(User, token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]


def get_current_active_superuser(current_user: CurrentUser) -> User:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
