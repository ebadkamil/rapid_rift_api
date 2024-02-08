from fastapi import APIRouter

from src.app.api.endpoints import login, product, users

api_router = APIRouter()
api_router.include_router(product.router, tags=["product"])
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, tags=["users"])
