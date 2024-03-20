from typing import Optional     #не обязательные поля
from pydantic import BaseModel  #базовая модель для Items - данные для запросов


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


