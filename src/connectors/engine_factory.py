
from src.connectors.constants import DbTypes
from sqlmodel import create_engine


class OracleEngine:
    def from_authentication_file(self, authentication):
        pass


class EngineFactory:
    _engines = {
        DbTypes.OARCLE: OracleEngine,
    }

    @classmethod
    def from_serialized_type(cls, db_type: DbTypes):
        if type in cls._engines:
            return cls._engines[db_type]

        raise NotImplementedError(f"Engine type {db_type} not implemented")