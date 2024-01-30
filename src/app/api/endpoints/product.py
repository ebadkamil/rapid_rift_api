from fastapi import APIRouter

from src.app.api.deps import InsepectDep, SecurityDep, SessionDep

router = APIRouter()


@router.get("/tables")
def read_product_types(inspector: InsepectDep):
    return {f"Available tables": inspector.get_table_names()}


@router.get("/items")
def read_product_types():
    return {"Available tables": "Hello"}
