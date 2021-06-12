from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    age = Column(Integer)
    first_name = Column(String)
    patronymic = Column(String)
    surname = Column(String)
    credit_card = Column(String)
    telephone = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    @property
    def full_name(self):
        return f'{self.first_name} {self.patronymic} {self.surname}'