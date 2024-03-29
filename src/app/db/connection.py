from sqlmodel import inspect

from src.app.db.constants import DbTypes
from src.app.db.engine_factory import EngineFactory


class Connector:
    def __init__(self, db_type: DbTypes) -> None:
        self._engine = EngineFactory.from_database_type(db_type)().get_engine()
        self._inspector = inspect(self._engine)

    def get_table_names(self):
        return self._inspector.get_table_names()

    @property
    def engine(self):
        return self._engine

    @property
    def inspector(self):
        return self._inspector
