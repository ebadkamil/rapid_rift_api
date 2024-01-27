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


settings = Settings()
print(settings.model_dump())
