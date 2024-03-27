from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    first_name: str = Field(title='First_name', min_length=2, max_length=32)
    last_name: str = Field(title='Last_name', min_length=2, max_length=32)
    birthdate: date = Field(title='Birthdate')
    email: EmailStr = Field(title='Email', min_length=5, max_length=50)
    address: str = Field(title='Address', min_length=5, max_length=100)




class UserWithId(User):
    user_id: int = Field(title='id')