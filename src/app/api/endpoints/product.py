from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_product_types():
    return {"MESSAGE": "HELLO WORLD"}
