# app/api/v1/__init__.py
from fastapi import APIRouter
from api.v1.items import router as items_router

router = APIRouter()
router.include_router(items_router)
