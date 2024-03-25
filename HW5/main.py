from typing import Optional

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import User, UserWithId, users

app = FastAPI()
templates = Jinja2Templates(directory="templates")



def index_by_id(user_id):
    for i in range(len(users)):
        if users[i].user_id == user_id:
            return i
    return None


@app.get("/users/")
async def read_users():
    return users


@app.post("/users/")
async def create_user(user: User):
    users.append(user.add_id())
    return users


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def read_user(request: Request, user_id: Optional[int] = None):

    if user_id is not None:
        if index_by_id(user_id) is not None:
            founded_user = [users[index_by_id(user_id)]]
            return templates.TemplateResponse("user_details.html", {"request": request, "users": founded_user})
        else:
            return 'User not found'
    else:
        return templates.TemplateResponse("user_details.html", {"request": request, "users": users})


@app.put("/items/{user_id}")
async def update_user(user_id: int, new_user: User):
    if index_by_id(user_id) is not None:
        users[index_by_id(user_id)] = new_user.add_id(user_id)
        return users
    return {"message": "user not found"}


@app.delete("/items/{user_id}")
async def delete_user(user_id: int):
    if index_by_id(user_id) is not None:
        users.pop(index_by_id(user_id))
        return users
    return {"message": "user not found"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080)
