from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserRegister(UserBase):
    password: str


class UserInDB(UserBase):
    id: int
    hashed_password: str

    class Config:
        from_attributes = True


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


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
