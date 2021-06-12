from fastapi import HTTPException
from database import db
from sqlalchemy.exc import IntegrityError

from models import User
import schemas


def get_user(username: str = None):
    return db.query(User).filter(User.username == username).first()


def create_user(user: schemas.UserCreateSerializer, is_admin=False):
    fake_hashed_password = user.password
    db_user = User(
        username=user.username,
        hashed_password=fake_hashed_password,
        age=user.age,
        first_name=user.first_name,
        patronymic=user.patronymic,
        surname=user.surname,
        is_admin=is_admin,
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
