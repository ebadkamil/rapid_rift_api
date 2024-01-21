from typing import Annotated, List, Union

from fastapi import FastAPI, Query
from pydantic import BaseModel

from src.app.models import Product_Type


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


server = FastAPI()


@server.get("/")
async def root():
    return {"message": "Production Line Overview"}


# @server.get("/product_type/")
# async def get_product_types():
#     pass

# @server.get("/items/")
# async def read_items(q: Annotated[Union[list[str], None], Query()] = None):
#     query_items = {"q": q}
#     return query_items


# @server.get("/production/{line_number}")
# async def get_status(line_number: int):
#     return {"line_number": line_number}


# @server.get("/status/{status}")
# async def get_status(status: Status, start: Annotated[Union[List[str], None], Query()] = None, skip: Annotated[Union[int, None], Query(le=10)] = None):
#     return {"status": status, "start": start, "skip": skip}


# @server.put("/production_line/{line_number}")
# async def put_status(line_number: int, item: Product_Type):
#     return {"item": item}
