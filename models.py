from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

# Модель пользователя
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)  # Хранение хешированного пароля

# Модель товара
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)  # Цена товара

# Модель заказа
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # Связь с пользователем
    product_id = Column(Integer, ForeignKey("products.id"))  # Связь с товаром
    date_ordered = Column(DateTime, default=datetime.datetime.utcnow)  # Дата заказа
    status = Column(String)  # Статус заказа (например, "в обработке", "доставлен")

    # Отношения с другими таблицами
    user = relationship("User")
    product = relationship("Product")
