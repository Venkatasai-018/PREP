from fastapi import FastAPI, Path
from pydantic import BaseModel, Field


app = FastAPI(title="Simple API", version="1.0.0")


class Item(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(ge=0, allow_inf_nan=False)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from FastAPI!"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/items/{item_id}")
def read_item(item_id: int = Path(ge=1)) -> dict[str, int]:
    return {"item_id": item_id}


@app.post("/items", response_model=Item)
def preview_item(item: Item) -> Item:
    return item