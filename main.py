from typing import Union
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

items = [ 
  {"id": 1},
  {"id": 2},
  {"id": 3},
  {"id": 4}
]

class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None

@app.post("/items/")
async def post_item(item: Item = Body(embed=True)):
    results = {"item": item}
    return results

@app.put("/items/")
async def post_item(item: Item = Body(embed=True)):
    results = {"item": item}
    return results

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{id}")
async def read_item(id: int):
    return [item for item in items if item["id"] == id]

@app.get("/items/")
async def read_items(page: int = 1, page_size: int = 10):
    return items[page-1: page -1 + page_size]