from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, inspect
from typing_extensions import Annotated

from src.app.core.config import settings
from src.app.db.connection import Connector

connector = Connector(settings.DBTYPE)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_session():
    with Session(connector.engine) as session:
        yield session


def get_inspector():
    yield connector.inspector


SessionDep = Annotated[Session, Depends(get_session)]
InsepectDep = Annotated[inspect, Depends(get_inspector)]
SecurityDep = Annotated[OAuth2PasswordBearer, Depends(oauth2_scheme)]
