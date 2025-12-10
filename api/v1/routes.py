# app/api/v1/routes.py
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello, World from FastAPI (modular)!"}


@router.get("/hello/{name}")
async def read_hello(name: str):
    return {"message": f"Hello, {name}! Welcome to our modular FastAPI app."}
