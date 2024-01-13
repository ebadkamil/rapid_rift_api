from datetime import datetime
from typing import Optional

from sqlmodel import Column, Enum, Field, SQLModel

from src.db_models.constants import Status


class Product_Type(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type_name: str


class Production_Line(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    line_number: int
    status: Status = Field(sa_column=Column(Enum(Status)))
    last_update_timestamp: datetime


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_number: str
    product_type_id: Optional[int] = Field(default=None, foreign_key="product_type.id")


class Mapping(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    line_id: Optional[int] = Field(default=None, foreign_key="production_line.id")
    order_id: Optional[int] = Field(default=None, foreign_key="order.id")


if __name__ == "__main__":
    pass
