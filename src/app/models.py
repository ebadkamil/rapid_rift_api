from datetime import datetime
from enum import Enum
from typing import Optional, Union

from pydantic import EmailStr
from sqlmodel import AutoString, Field, SQLModel


class Status(Enum):
    GREEN = "green"
    RED = "red"
    YELLOW = "yellow"


class Product_Type(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type_name: str


class Production_Line(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    line_number: int
    last_update_timestamp: datetime


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_number: str
    product_type_id: Optional[int] = Field(default=None, foreign_key="product_type.id")


class Mapping(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    line_id: Optional[int] = Field(default=None, foreign_key="production_line.id")
    order_id: Optional[int] = Field(default=None, foreign_key="order.id")


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, sa_type=AutoString)
    full_name: Union[str, None] = None
    is_active: bool = True
    is_superuser: bool = False


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str


class UserCreate(SQLModel):
    email: EmailStr
    password: str
    full_name: Union[str, None] = None


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(SQLModel):
    sub: Union[int, None] = None
