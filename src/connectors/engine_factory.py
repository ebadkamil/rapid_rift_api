from pathlib import Path
from typing import Dict, Optional

import sqlmodel
from yaml import safe_load

from src.connectors.constants import DbTypes


def read_config(filepath: Path) -> Dict[str, str]:
    try:
        with open(filepath, "r") as file:
            setup_yaml = safe_load(file)
    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"{filepath} is not a valid DB config filepath, {error}"
        )
    return setup_yaml


class BaseEngine:
    def __init__(self, authentication, local_db: Optional[bool] = False):
        self._config = read_config(authentication)
        if not local_db:
            self.user = self._config["user"]
            self.passd = self._config["password"]
            self.host = self._config["host"]
            self.port = self._config["port"]
            self.service = self._config["service"]
            self.encoding = self._config["encoding"]

    def get_engine(self):
        raise NotImplementedError(f"Engine not implemented")


class OracleEngine(BaseEngine):
    def __init__(self, authentication):
        super().__init__(authentication)

    def get_engine(self):
        return sqlmodel.create_engine(
            f"oracle+cx_oracle://{self.user}:{self.passd}@{self.host}:{self.port}/?service_name={self.service}&{self.encoding}"
        )


class SqliteEngine(BaseEngine):
    def __init__(self, authentication, local_db=True):
        super().__init__(authentication, local_db=local_db)

    def get_engine(self):
        return sqlmodel.create_engine(
            f"sqlite:///{self._config['database_file_name']}", echo=True
        )


class EngineFactory:
    _engines = {
        DbTypes.ORACLE: OracleEngine,
        DbTypes.SQLITE: SqliteEngine,
    }

    @classmethod
    def from_database_type(cls, db_type: DbTypes):
        if db_type in cls._engines:
            return cls._engines[db_type]

        raise NotImplementedError(f"Engine type {db_type} not implemented")
