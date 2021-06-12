from typing import Optional

from pydantic import BaseModel


class CommentBody(BaseModel):
    rating: int = 1
    username: str
    comment: str


class SuccessResponse(BaseModel):
    res: str = 'success'
    status: int = 200

class ReviewModel(BaseModel):
    id: int
    rating: int
    username: str
    comment: str

    class Config:
        orm_mode = True


class UserSerializer(BaseModel):
    username: str
    id: int
    address: Optional[str]
    first_name: str
    patronymic: Optional[str]
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


class LoginRequest(BaseModel):
    username: str
    password: str

