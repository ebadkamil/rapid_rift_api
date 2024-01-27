from fastapi import Depends
from sqlmodel import Session, inspect
from typing_extensions import Annotated

from src.app.core.config import settings
from src.app.db.connection import Connector

connector = Connector(settings.DBTYPE)


def get_session():
    with Session(connector.engine) as session:
        yield session


def get_inspector():
    yield connector.inspector


SessionDep = Annotated[Session, Depends(get_session)]
InsepectDep = Annotated[inspect, Depends(get_inspector)]
