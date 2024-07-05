from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv

from . import models

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
                                  )


class Base(DeclarativeBase):
    pass


async def get_db() -> AsyncSession:
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
