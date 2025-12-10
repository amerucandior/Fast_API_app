# app/core/error_handlers.py
from fastapi import Request
from fastapi.responses import JSONResponse
from core.exceptions import ItemNotFoundError


async def item_not_found_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error": "ItemNotFound",
            "item_id": exc.item_id,
            "message": f"Item with id {exc.item_id} was not found",
        },
    )
