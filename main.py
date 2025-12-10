# app/main.py
from fastapi import FastAPI
from api.v1.routes import router as api_v1_router
from fastapi import FastAPI
from core.exceptions import ItemNotFoundError
from core.errorHandler import item_not_found_handler


app = FastAPI(
    title="Hello API",
    version="1.0.0",
)

# Include your versioned router
app.include_router(api_v1_router, prefix="/api/v1")
app.add_exception_handler(ItemNotFoundError, item_not_found_handler)
