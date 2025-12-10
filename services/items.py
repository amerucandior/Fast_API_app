# app/services/items.py
from typing import List, Dict, Any
from core.exceptions import ItemNotFoundError

ITEMS_DB: List[Dict[str, Any]] = []


def list_items() -> List[Dict[str, Any]]:
    return ITEMS_DB


def get_item_by_id(item_id: int) -> Dict[str, Any]:
    for item in ITEMS_DB:
        if item["id"] == item_id:
            return item
    raise ItemNotFoundError(item_id)


def create_item(data: Dict[str, Any]) -> Dict[str, Any]:
    new_item = {**data, "id": len(ITEMS_DB) + 1}
    ITEMS_DB.append(new_item)
    return new_item
