from typing import Optional

from pydantic import BaseModel, validator


class UserSerializer(BaseModel):
    username: str
    id: int
    address: Optional[str]
    first_name: str
    patronymic: Optional[str]
    credit_card: Optional[str]
    telephone: Optional[str]
    surname: Optional[str]
    is_admin: bool
    is_active: bool

    class Config:
        orm_mode = True


class UserCreateSerializer(BaseModel):
    username: str
    password: str
    address: Optional[str]
    first_name: str
    patronymic: Optional[str]
    surname: Optional[str]
    credit_card: Optional[str]
    telephone: Optional[str]


class LoginRequest(BaseModel):
    username: str
    password: str
