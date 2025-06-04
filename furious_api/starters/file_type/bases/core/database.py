from typing import Any

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative, sessionmaker

from .config import settings

if settings.DB_MODE == "async":
    from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
    engine = create_async_engine(
        settings.DATABASE_URL,
        echo=True,
        pool_size=20,
        max_overflow=10
    )
    SessionLocal = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
else:
    from sqlalchemy import create_engine
    engine = create_engine(
        settings.DATABASE_URL,
        pool_size=20,
        max_overflow=10,
        pool_pre_ping=True
    )
    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )



# Modelo base para classes
@as_declarative()
class Base:
    id: Any
    __name__: str

    # Para gerar tabela com o nome da classe
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()



# Gerador de sessões
def get_db():
    if settings.DB_MODE == "async":
        from contextlib import asynccontextmanager
        @asynccontextmanager
        async def async_db():
            db = SessionLocal()
            try:
                yield db
            finally:
                await db.close()
        return async_db()
    else:
        from contextlib import contextmanager
        @contextmanager
        def sync_db():
            db = SessionLocal()
            try:
                yield db
            finally:
                db.close()
        return sync_db()
    

# Criação das tabelas
async def create_tables():         
    if settings.DB_MODE == "async":
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    else:
        Base.metadata.create_all(bind=engine)