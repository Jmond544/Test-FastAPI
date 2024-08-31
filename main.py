from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Request - Response model
class Item(BaseModel):
    text: str
    is_done: bool = False

items = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int) -> Item:
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    del items[item_id]
    return items