from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    ORACLE_SERVER: str = ""
    ORACLE_PORT: str = ""
    ORACLE_USER: str = ""
    ORACLE_PASSWORD: str = ""
    ORACLE_SERVICE: str = ""
    ORACLE_ENCODING: str = ""

    SQLITE_DATABASE_FILE_NAME: str = ""


settings = Settings()
