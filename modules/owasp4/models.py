from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from database import db

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
    first_name = Column(String)
    patronymic = Column(String)
    surname = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    @property
    def full_name(self):
        return f'{self.first_name} {self.patronymic} {self.surname}'

    @classmethod
    def get_user_by_id(cls, id_: int) -> 'User':
        return db.query(cls).get(id_)
