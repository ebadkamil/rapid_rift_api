from pydantic_settings import BaseSettings

from src.app.db.constants import DbTypes


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    ORACLE_SERVER: str = ""
    ORACLE_PORT: str = ""
    ORACLE_USER: str = ""
    ORACLE_PASSWORD: str = ""
    ORACLE_SERVICE: str = ""
    ORACLE_ENCODING: str = ""

    SQLITE_DATABASE_FILE_NAME: str = "database.db"

    DBTYPE: DbTypes = DbTypes.SQLITE
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()
print(settings.model_dump())
