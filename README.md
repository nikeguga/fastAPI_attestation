# Интернет-магазин API

Это проект интернет-магазина с использованием FastAPI, SQLAlchemy и Pydantic. Проект предоставляет REST API для управления пользователями, товарами и заказами.

## Структура проекта

- `main.py`: Основной файл приложения FastAPI.
- `models.py`: Модели базы данных, определенные с использованием SQLAlchemy.
- `schemas.py`: Модели Pydantic для валидации данных и описания API.
- `crud.py`: Функции для выполнения операций CRUD.
- `database_config.py`: Настройки базы данных и создание сессий.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone <URL вашего репозитория>
   cd <название директории с проектом>
2. Создайте и активируйте виртуальное окружение:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate

3. Установите зависимости:  
   ```bash
   pip install -r requirements.txt
  
## Запуск  
Для запуска приложения используйте команду:  
  
uvicorn main:app --reload  
  
Приложение будет доступно по адресу http://127.0.0.1:8000.

## Использование
**Пользователи**  
Создание пользователя:  
POST /users/
Получение информации о пользователе:  
GET /users/{user_id}  
**Товары**  
Создание товара: POST /products/ 
Получение информации о товаре: GET /products/{product_id}  
**Заказы**  
Создание заказа: POST /orders/  
Получение информации о заказе: GET /orders/{order_id}

## Требования

* Python 3.7+
* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn

всё в requirements кроме python
