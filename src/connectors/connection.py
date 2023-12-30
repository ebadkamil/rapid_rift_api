from pathlib import Path
from sqlmodel import Session

from src.connectors.engine_factory import EngineFactory
from src.connectors.constants import DbTypes


class Connector:
    def __init__(self, db_type: DbTypes, authentication: Path) -> None:
        self._engine = EngineFactory.from_database_type(db_type)(authentication).get_engine()
