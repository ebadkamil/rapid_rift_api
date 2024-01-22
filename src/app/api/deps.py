from fastapi import Depends
from typing_extensions import Annotated

from src.app.core.config import settings
from src.app.db.connection import Connector

connector = Connector(settings.DBTYPE)


def get_session():
    with connector.session as session:
        yield session
