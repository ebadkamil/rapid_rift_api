from fastapi import APIRouter

from src.app.api.endpoints import login, product

api_router = APIRouter()
api_router.include_router(product.router, tags=["product"])
api_router.include_router(login.router, tags=["login"])
