# FastAPI learning app

A minimal FastAPI project you can read, run, and tinker with while learning how FastAPI structures routers, schemas, services, and exception handlers.

## Quickstart

- Requirements: Python 3.11+ and `pip`.
- Create an environment: `python -m venv .venv && source .venv/bin/activate`
- Install dev deps: `pip install -U pip && pip install fastapi uvicorn[standard] httpx pytest`
- Run the app with reload: `uvicorn main:app --reload`
- Interactive docs: open http://127.0.0.1:8000/docs (Swagger UI) or `/redoc`.

## Project layout (what to read)

- `main.py` – creates the FastAPI app, mounts the v1 router, and registers the custom 404 handler.
- `api/v1/routes.py` – current public routes:
  - `GET /api/v1/` returns a hello world payload.
  - `GET /api/v1/hello/{name}` returns a personalized greeting.
- `api/v1/items.py` – example CRUD-style router using a Pydantic model (`schemas/items.py`) and a custom exception. Not wired into `main.py` yet; see “Enabling the items router” below if you want to expose it.
- `schemas/items.py` – Pydantic model with validation (min/max lengths, positive price, optional description).
- `services/items.py` – in-memory “service” layer showing where business logic could live.
- `core/exceptions.py` and `core/errorHandler.py` – custom exception plus a FastAPI exception handler that returns a JSON 404 payload.
- `tests/test_main.py` – pytest + httpx async client test for the root route.

## Hitting the running app

```bash
curl http://127.0.0.1:8000/api/v1/
# -> {"message": "Hello, World from FastAPI (modular)!"}

curl http://127.0.0.1:8000/api/v1/hello/you
# -> {"message": "Hello, you! Welcome to our modular FastAPI app."}
```

## Enabling the items router (optional exercise)

`api/v1/items.py` already defines:

- `POST /items/` to create an item with validation and auto-incremented `id`
- `GET /items/{item_id}` to fetch an item or raise `ItemNotFoundError`

To expose those endpoints, include the items router when registering v1 routes, e.g. replace the import in `main.py` with:

```python
from api.v1 import router as api_v1_router  # pulls in items via api/v1/__init__.py
```

Restart `uvicorn` and the items endpoints will appear under `/api/v1/items/...` in Swagger UI.

## Running tests

```bash
pytest
```

`tests/test_main.py` ensures the root route responds with the expected JSON.
