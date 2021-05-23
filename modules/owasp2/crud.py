import re

from fastapi import HTTPException
from database import db
from sqlalchemy.exc import IntegrityError

import models
import schemas


def create_user(user: schemas.UserCreateSerializer):
    fake_hashed_password = user.password
    password_re = r'^\d{6}$'  # 6 цифр
    if not re.match(password_re, fake_hashed_password):
        raise HTTPException(status_code=404, detail='Не верный пароль! Пароль должен состоять из 6(ти) цифр.')
    db_user = models.User(
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
