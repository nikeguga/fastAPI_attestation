from pydantic import BaseModel, EmailStr
from datetime import datetime

# Базовая модель пользователя
class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

# Модель для создания нового пользователя
class UserCreate(UserBase):
    password: str  # Пароль в открытом виде, будет хеширован перед сохранением

# Модель для возврата информации о пользователе
class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True  # Включение поддержки ORM для преобразования данных

# Базовая модель товара
class ProductBase(BaseModel):
    name: str
    description: str
    price: float

# Модель для создания нового товара
class ProductCreate(ProductBase):
    pass

# Модель для возврата информации о товаре
class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True

# Базовая модель заказа
class OrderBase(BaseModel):
    user_id: int
    product_id: int
    status: str

# Модель для создания нового заказа
class OrderCreate(OrderBase):
    pass

# Модель для возврата информации о заказе
class OrderResponse(OrderBase):
    id: int
    date_ordered: datetime

    class Config:
        orm_mode = True
