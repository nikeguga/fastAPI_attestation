from sqlalchemy.orm import Session
from models import User, Product, Order
from schemas import UserCreate, ProductCreate, OrderCreate
from passlib.context import CryptContext

# Настройка контекста для хеширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    """
    Возвращает хеш пароля.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    """
    Проверяет, соответствует ли введенный пароль хешу.
    """
    return pwd_context.verify(plain_password, hashed_password)

def create_user(db: Session, user: UserCreate):
    """
    Создает нового пользователя в базе данных.
    """
    hashed_password = get_password_hash(user.password)
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    """
    Возвращает пользователя по его ID.
    """
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    """
    Возвращает пользователя по его email.
    """
    return db.query(User).filter(User.email == email).first()

def create_product(db: Session, product: ProductCreate):
    """
    Создает новый товар в базе данных.
    """
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    """
    Возвращает товар по его ID.
    """
    return db.query(Product).filter(Product.id == product_id).first()

def create_order(db: Session, order: OrderCreate):
    """
    Создает новый заказ в базе данных.
    """
    db_order = Order(
        user_id=order.user_id,
        product_id=order.product_id,
        status=order.status
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    """
    Возвращает заказ по его ID.
    """
    return db.query(Order).filter(Order.id == order_id).first()
