from fastapi import FastAPI

from typing import Optional

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def root(item: Item):
    return {"item_id": item.name}

@app.get("/")
async def root():
    return {"message": "Hello World"}