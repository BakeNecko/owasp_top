from typing import Optional

from pydantic import BaseModel


class UserSerializer(BaseModel):
    email: str
    id: int
    is_active: bool
    age: Optional[int]
    first_name: str
    patronymic: Optional[str]
    surname: Optional[str]

    class Config:
        orm_mode = True


class UserCreateSerializer(BaseModel):
    email: str
    password: str
    age: Optional[int]
    first_name: str
    patronymic: Optional[str]
    surname: Optional[str]
