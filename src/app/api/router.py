from fastapi import APIRouter

from src.app.api.endpoints import product

api_router = APIRouter()
api_router.include_router(product.router, tags=["product"])
