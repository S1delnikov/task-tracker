from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from sqlalchemy.orm import Session
from datetime import timedelta
from auth.users import authenticate_user
from auth.jwthandler import ACCESS_TOKEN_EXPIRE_MINUTES, oauth2_scheme, create_access_token
from auth.users import get_password_hash
from schemas.token import Token
from schemas.user import UserRegSchema
from database.connection import db_dependency
from database.models import Users
import crud.users.user as crud

router = APIRouter()

@router.get('/')
def home():
    return {'data': 'Hello, stranger'}


@router.post('/login')
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency
):
    return await crud.login(form_data.username, form_data.password, db)


@router.post('/register')
async def register(data: UserRegSchema, db: db_dependency):
    return await crud.create_user(data, db)

@router.get('/check')
def check(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}