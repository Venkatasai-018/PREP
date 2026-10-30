# Simple FastAPI API

A small Python API with interactive documentation and a Docker image. No React frontend or database is required.

## Run With Docker

Install Docker (Docker Desktop on Windows) and ensure it is running. From the project directory:

```sh
docker build -t simple-fastapi .
docker run --rm -p 8000:8000 --name simple-fastapi simple-fastapi
```

Open http://localhost:8000/docs to try the endpoints, or http://localhost:8000/ for the greeting. Press Ctrl+C to stop the container.

## Run From a Clone

After publishing this project to your Git repository, replace the placeholder URL below with that repository's URL:

```sh
git clone <your-repository-url> simple-fastapi
cd simple-fastapi
docker build -t simple-fastapi .
docker run --rm -p 8000:8000 --name simple-fastapi simple-fastapi
```

Git cloning happens on the host. The Dockerfile builds the checked-out code, so it does not need repository credentials.

## Run Locally

Use Python 3.12. On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

On macOS/Linux, use `.venv/bin/python` instead of `.\.venv\Scripts\python.exe`.

## Endpoints

| Method | Path | Behavior |
| --- | --- | --- |
| GET | `/` | Returns a greeting |
| GET | `/health` | Returns `{"status":"ok"}` |
| GET | `/items/{item_id}` | Returns a positive integer item ID; does not look up stored data |
| POST | `/items` | Validates and echoes an item; does not save it |

Example JSON body for `POST /items`:

```json
{"name": "Notebook", "price": 12.5}
```

Invalid inputs return HTTP 422. Swagger UI is at `/docs`; the OpenAPI schema is at `/openapi.json`.

## Tests

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m unittest -v test_api
```

This is an unauthenticated demonstration API. Add authentication and review dependencies before exposing it publicly.