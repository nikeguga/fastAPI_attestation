from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from database_config import get_db, init_db
from models import Base
from schemas import UserCreate, UserResponse, ProductCreate, ProductResponse, OrderCreate, OrderResponse
import crud
import uvicorn

# Создание приложения FastAPI
app = FastAPI()

# Асинхронная инициализация базы данных при старте приложения
@app.on_event("startup")
async def on_startup():
    await init_db()

# Создание нового пользователя
@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    # Проверка, существует ли пользователь с данным email
    db_user = await crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # Создание пользователя
    return await crud.create_user(db=db, user=user)

# Получение информации о пользователе по ID
@app.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Создание нового товара
@app.post("/products/", response_model=ProductResponse)
async def create_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_product(db=db, product=product)

# Получение информации о товаре по ID
@app.get("/products/{product_id}", response_model=ProductResponse)
async def read_product(product_id: int, db: AsyncSession = Depends(get_db)):
    db_product = await crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# Создание нового заказа
@app.post("/orders/", response_model=OrderResponse)
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_order(db=db, order=order)

# Получение информации о заказе по ID
@app.get("/orders/{order_id}", response_model=OrderResponse)
async def read_order(order_id: int, db: AsyncSession = Depends(get_db)):
    db_order = await crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

# Запуск приложения
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
