from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class TaskBase(BaseModel):
    title: str
    description: str


class TaskCreate(TaskBase):
    owner_id: int


class Task(TaskBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
