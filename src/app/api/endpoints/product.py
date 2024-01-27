from fastapi import APIRouter

from src.app.api.deps import InsepectDep, SessionDep

router = APIRouter()


@router.get("/tables")
def read_product_types(inspector: InsepectDep):
    return {"Available tables": inspector.get_table_names()}
