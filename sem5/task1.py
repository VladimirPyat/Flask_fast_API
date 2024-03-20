from xmlrpc.client import boolean

import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
tasks=[]

class Item(BaseModel):
    user_id: int
    title: str
    description: Optional[str] = None
    status: boolean = True



@app.get("/")
async def read_root():
    return tasks



@app.post("/items/")
async def create_item(task: Item):
    tasks.append(task)
    return task



@app.put("/items/{item_id}")
async def update_item(item_id: int, task: Item):
    tasks[item_id]=task
    return task



@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"item_id": item_id}




if __name__ == "__main__":
    uvicorn.run("task1:app", port=8080)
