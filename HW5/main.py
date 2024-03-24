import uvicorn
from fastapi import FastAPI
from models import User, UserWithId, users



app = FastAPI()



def index_by_id(user_id):
    for i in range(len(users)):
        if users[i].user_id == user_id:
            return i
    return None


@app.get("/")
async def read_users():
    return users


@app.post("/users/")
async def create_user(user: User):
    users.append(user.add_id())
    return users


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

