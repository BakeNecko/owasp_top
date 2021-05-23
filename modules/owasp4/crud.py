import re

from fastapi import HTTPException
from database import db
from sqlalchemy.exc import IntegrityError

import models
import schemas


def create_user(user: schemas.UserCreateSerializer, is_admin: bool = False):
    fake_hashed_password = user.password
    db_user = models.User(
        is_admin=is_admin,
        email=user.email,
        hashed_password=fake_hashed_password,
        age=user.age,
        first_name=user.first_name,
        patronymic=user.patronymic,
        surname=user.surname,
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=404, detail='Пользователь с таким email уже существует')
    return db_user
