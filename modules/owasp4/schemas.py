from typing import Optional

from pydantic import BaseModel, validator
from jwt import check_admin_secret_key


class UserSerializer(BaseModel):
    email: str
    id: int
    age: Optional[int]
    first_name: str
    patronymic: Optional[str]
    surname: Optional[str]
    is_admin: bool
    is_active: bool

    class Config:
        orm_mode = True


class UserCreateSerializer(BaseModel):
    email: str
    password: str
    age: Optional[int]
    first_name: str
    patronymic: Optional[str]
    surname: Optional[str]


class AdminUserCreateSerializer(UserCreateSerializer):
    secret_admin_key: str

    @validator('secret_admin_key')
    def parse_sort(cls, secret_admin_key):
        return check_admin_secret_key(secret_admin_key)
