import sqlmodel

from src.app.core.config import settings
from src.app.db.constants import DbTypes


class BaseEngine:
    def __init__(self):
        self.config = settings.model_dump()
        if not self.validate_config():
            raise ValueError(f"Missing or invalid configurations: {self.config}")

    def get_engine(self):
        raise NotImplementedError("Engine not implemented")

    def validate_config(self):
        return True


class OracleEngine(BaseEngine):
    def get_engine(self):
        return sqlmodel.create_engine(
            f"oracle+cx_oracle://{self.config['ORACLE_USER']}:{self.config['ORACLE_PASSWORD']}@{self.config['ORACLE_SERVER']}:{self.config['ORACLE_PORT']}/?service_name={self.config['ORACLE_SERVICE']}&{self.config['ORACLE_ENCODING']}"
        )

    def validate_config(self):
        required_configurations = [
            "ORACLE_USER",
            "ORACLE_PASSWORD",
            "ORACLE_SERVER",
            "ORACLE_PORT",
            "ORACLE_SERVICE",
            "ORACLE_ENCODING",
        ]
        return all([var in self.config for var in required_configurations])


class SqliteEngine(BaseEngine):
    def get_engine(self):
        return sqlmodel.create_engine(
            f"sqlite:///{self.config['SQLITE_DATABASE_FILE_NAME']}", echo=True
        )

    def validate_config(self):
        return "SQLITE_DATABASE_FILE_NAME" in self.config


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
