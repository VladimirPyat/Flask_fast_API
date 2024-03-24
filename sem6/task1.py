from typing import List

import databases
from datetime import datetime
import sqlalchemy
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, SecretStr
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users",
                         metadata,
                         sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("username", sqlalchemy.String(32)),
                         sqlalchemy.Column("email", sqlalchemy.String(50)),
                         sqlalchemy.Column("password", sqlalchemy.String(32))
                         )

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()


class User(BaseModel):
    username: str = Field(title='Username', max_length=32)
    email: EmailStr = Field(title='Email', max_length=50)
    password: SecretStr = Field(title='Password', max_length=32)
    datetime: datetime


class UserWithId(User):
    user_id: int = Field(title='id')


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/users/', response_model=List[UserWithId])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=UserWithId)
async def get_user(user_id: int):
    query = users.select().where(users.c.user_id == user_id)
    return await database.fetch_one(query)


@app.post("/users/", response_model=UserWithId)
async def create_user(user: User):
    query = users.insert().values(username=user.username, email=user.email, password=user.password.get_secret_value())
    last_record_id = await database.execute(query)

    return {**user.model_dump(), "user_id": last_record_id}




@app.get('/temp/{number}')
async def temp_user(number):
    for i in range(number):
        query = users.insert().values(username=f'user_{i}', email=f'mail{i}@123.ru', password='1234')
        await database.execute(query)
        return ('ok')


if __name__ == '__main__':
    uvicorn.run('task1:app')
    temp_user()
