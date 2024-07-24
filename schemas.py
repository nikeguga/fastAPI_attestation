from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    status: str

class OrderResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    date_ordered: datetime
    status: str

    class Config:
        orm_mode = True
