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

router = APIRouter()

@router.get('/')
def home():
    return {'data': 'Hello, stranger'}


@router.post('/login')
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency
) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={ "sub": user.username }, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post('/register')
def register(data: UserRegSchema, db: db_dependency):
    new_user = Users(
        username = data.username,
        email = data.email,
        password = get_password_hash(data.password),
        date_of_registration = data.date_of_registration
    )
    try: 
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except:
        raise HTTPException(status_code=400, detail='This login is occupied by another person')
    return data

@router.get('/check')
def check(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}