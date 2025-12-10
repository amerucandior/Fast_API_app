# app/schemas/items.py
from pydantic import BaseModel, Field
from typing import Optional


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0)
    description: Optional[str] = Field(None, max_length=200)
    in_stock: bool = True
