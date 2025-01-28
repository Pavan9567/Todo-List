from pydantic import BaseModel

class ToDoBase(BaseModel):
    title: str
    description: str
    completed: bool = False

class ToDoCreate(ToDoBase):
    pass

class ToDoResponse(ToDoBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
