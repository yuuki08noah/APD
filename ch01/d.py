from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

class Product(BaseModel):
    id: int = Field(..., min_length=4, max_length=16)
    name: str
    price: float = Field(..., gt=10, le=100)
    stock: Optional[int] = 10

class Event(BaseModel):
    name: str
    start_time: datetime
    end_time: datetime

class AdminUser(User, BaseModel):
    role: str = 'admin'


if __name__ == "__main__":
    user = User(id=1, name="<NAME>", age=20, email="<EMAIL>")
    print(user.id)
    print(user.name)
    print(user.age)

    p1 = Product(name="MACBOOK PRO", price=20)
    print(p1)

    e1 = Event(name="MACBOOK PRO", start_time='2025-06-09', end_time='2026-08-09')
    print(e1)

    admin = AdminUser(role='admin', name="<NAME>", email="<EMAIL>", age=20, id=1)
    print(admin)