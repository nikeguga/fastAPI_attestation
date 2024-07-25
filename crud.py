from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import User, Product, Order
from schemas import UserCreate, ProductCreate, OrderCreate
from passlib.context import CryptContext

# Настройка контекста для хеширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Хеширование пароля
async def get_password_hash(password: str):
    return pwd_context.hash(password)

# Проверка пароля с использованием хеша
async def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Создание нового пользователя в базе данных
async def create_user(db: AsyncSession, user: UserCreate):
    hashed_password = await get_password_hash(user.password)
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

# Получение пользователя по ID
async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()

# Получение пользователя по email
async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalars().first()

# Создание нового товара в базе данных
async def create_product(db: AsyncSession, product: ProductCreate):
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price
    )
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

# Получение товара по ID
async def get_product(db: AsyncSession, product_id: int):
    result = await db.execute(select(Product).filter(Product.id == product_id))
    return result.scalars().first()

# Создание нового заказа в базе данных
async def create_order(db: AsyncSession, order: OrderCreate):
    db_order = Order(
        user_id=order.user_id,
        product_id=order.product_id,
        status=order.status
    )
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)
    return db_order

# Получение заказа по ID
async def get_order(db: AsyncSession, order_id: int):
    result = await db.execute(select(Order).filter(Order.id == order_id))
    return result.scalars().first()
