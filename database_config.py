from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Base

# URL базы данных
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# Создание асинхронного движка базы данных
engine = create_async_engine(DATABASE_URL, echo=True)

# Создание асинхронной сессии базы данных
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

# Инициализация базы данных (создание таблиц)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Зависимость для получения сессии базы данных
async def get_db():
    async with SessionLocal() as session:
        yield session
        await session.commit()
