from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserRegSchema(BaseModel):
    username: str
    email: str | None = None
    password: str
    date_of_registration: datetime = datetime.now()


class UserInSchema(BaseModel):
    id_user: int
    username: str
    password: str


class UserOutSchema(BaseModel):
    id_user: int
    username: str