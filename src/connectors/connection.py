from pathlib import Path

from sqlmodel import Session, inspect

from src.connectors.constants import DbTypes
from src.connectors.engine_factory import EngineFactory


class Connector:
    def __init__(self, db_type: DbTypes, authentication: Path) -> None:
        self._engine = EngineFactory.from_database_type(db_type)(
            authentication
        ).get_engine()

        self._inspector = inspect(self._engine)
        self.session = Session(self._engine)

    def get_table_names(self):
        return self._inspector.get_table_names()
