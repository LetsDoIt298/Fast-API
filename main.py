# uvicorn main:app --reload
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}


class Item(BaseModel):
    item: str

# List to store items
items = []

@app.post("/items")
def create_item(item: dict[str, str]): # This says json file/dictionary is sent. where key and value are in string.
    print(item)
    print(dict[str, str])
    items.append(item[item])
    return {"Items":items}  #{"Data":"Here is the data"}