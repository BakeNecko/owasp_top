from fastapi import HTTPException
from database import db
from sqlalchemy.exc import IntegrityError

import models
import schemas


def get_user(username: str = None):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(user: schemas.UserCreateSerializer, is_admin: bool = False):
    fake_hashed_password = user.password
    db_user = models.User(
        is_admin=is_admin,
        username=user.username,
        hashed_password=fake_hashed_password,
        address=user.address,
        first_name=user.first_name,
        patronymic=user.patronymic,
        surname=user.surname,
        telephone=user.telephone,
        credit_card=user.credit_card,
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=404, detail='Пользователь с таким username уже существует')
    return db_user


def get_all_users():
    return db.query(models.User.username).all()


def delete_user(username):
    db.query(models.User).filter(models.User.username == username).delete()
