from fastapi import HTTPException, status
from datetime import timedelta
from database.connection import db_dependency
from auth.jwthandler import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from auth.users import get_password_hash, authenticate_user
from schemas.user import UserRegSchema, UserOutSchema
from schemas.token import Token
from database.models import Users


async def create_user(data: UserRegSchema, db: db_dependency):
    try:
        new_user = Users (
            username=data.username,
            password=get_password_hash(password=data.password),
            email=data.email,
            date_of_registration=data.date_of_registration
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This username is occupied by another person")
    return UserOutSchema(id_user=new_user.id_user, username=new_user.username)


async def login(username, password: str, db: db_dependency):
    user = authenticate_user(username=username, password=password, db=db)
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


