from fastapi import APIRouter

router = APIRouter()


@router.get("/product_types/")
def read_product_types():
    return {"MESSAGE": "HELLO WORLD"}
