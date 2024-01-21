from fastapi import FastAPI

from src.app.api.router import api_router
from src.app.core.config import settings

app = FastAPI(
    title="Rapid-Rift-API",
)


app.include_router(api_router, prefix=settings.API_V1_STR)
