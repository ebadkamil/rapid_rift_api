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
    def __init__(self, authentication):
        self.config = read_config(authentication)
        if not self.validate_config():
            raise ValueError(f"Missing or invalid configurations: {self.config}")

    def get_engine(self):
        raise NotImplementedError(f"Engine not implemented")

    def validate_config(self):
        return True


class OracleEngine(BaseEngine):
    def __init__(self, authentication):
        super().__init__(authentication)

    def get_engine(self):
        return sqlmodel.create_engine(
            f"oracle+cx_oracle://{self.config['user']}:{self.config['password']}@{self.config['host']}:{self.config['port']}/?service_name={self.config['service']}&{self.config['encoding']}"
        )

    def validate_config(self):
        required_configurations = [
            "user",
            "password",
            "host",
            "port",
            "service",
            "encoding",
        ]
        return all([var in self.config for var in required_configurations])


class SqliteEngine(BaseEngine):
    def __init__(self, authentication):
        super().__init__(authentication)

    def get_engine(self):
        return sqlmodel.create_engine(
            f"sqlite:///{self.config['database_file_name']}", echo=True
        )

    def validate_config(self):
        return "database_file_name" in self.config


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
