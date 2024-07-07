from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum

from app.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(1024), nullable=False)
    tasks = relationship("Task", back_populates="owner", cascade="all, delete-orphan")


class TaskPriority(PyEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(128), index=True, nullable=False)
    description = Column(String, index=True)
    priority = Column(Enum(TaskPriority), nullable=True)

    owner_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    owner = relationship("User", back_populates="tasks")
