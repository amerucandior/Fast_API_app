# app/api/v1/items.py
from fastapi import APIRouter, HTTPException, status
from schemas.items import ItemCreate
from core.exceptions import ItemNotFoundError


router = APIRouter(prefix="/items", tags=["items"])

# Fake in-memory store for now
ITEMS_DB = []


@router.post("/", status_code=201)
async def create_item(item: ItemCreate):
    # item is already validated at this point
    stored_item = item.model_dump()
    stored_item["id"] = len(ITEMS_DB) + 1
    ITEMS_DB.append(stored_item)
    return stored_item


@router.get("/{item_id}")
async def get_item(item_id: int):
    for item in ITEMS_DB:
        if item["id"] == item_id:
            return item
    # No item found → raise a 404
    raise ItemNotFoundError(item_id=item_id)
