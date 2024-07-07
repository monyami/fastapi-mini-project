from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app import models, schemas


async def get_user(db: AsyncSession, user_id: int):
    results = await db.execute(select(models.User).filter(models.User.id == user_id))
    return results.scalar()


async def get_user_by_username(db: AsyncSession, username: str):
    results = await db.execute(select(models.User).filter(models.User.username == username))
    return results.scalar()


async def get_user_by_email(db: AsyncSession, email: str):
    results = await db.execute(select(models.User).filter(models.User.email == email))
    return results.scalar()


async def get_users(db: AsyncSession, skip: int = 0, limit: int = 10):
    results = await db.execute(select(models.User).offset(skip).limit(limit))
    return results.scalars().all()


async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 10):
    results = await db.execute(select(models.User).offset(skip).limit(limit))
    return results.scalars().all()

async def get_tasks_by_username(db: AsyncSession, username: str):
    user = await get_user_by_username(db, username)
    if user:
        results = await db.execute(select(models.Task).filter(models.Task.owner_id == user.id))
        return results.scalars().all()


async def create_task(db: AsyncSession, task: schemas.TaskCreate):
    db_task = models.Task(title=task.title, description=task.description, owner_id=task.owner_id)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task
