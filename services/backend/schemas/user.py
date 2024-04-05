from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserRegSchema(BaseModel):
    """Представление модели регистрирующегося пользователя\n
    username: str
    email: str | None = None
    password: str
    date_of_registration: datetime = datetime.now()\n

    class Config:
        from_attributes = True
    """
    username: str
    email: str | None = None
    password: str
    date_of_registration: datetime = datetime.now()

    class Config:
        from_attributes = True


class UserInSchema(BaseModel):
    """Представление модели входящих данных пользователя\n
    id_user: int
    username: str
    password: str\n

    class Config:
        from_attributes = True
    """
    id_user: int
    username: str
    password: str

    class Config:
        from_attributes = True


class UserOutSchema(BaseModel):
    """Представление модели исходящих данных пользователя\n
    id_user: int
    username: str\n

    class Config:
        from_attributes = True
    """
    id_user: int
    username: str

    class Config:
        from_attributes = True