from fastapi import HTTPException, status
from datetime import timedelta
from database.connection import db_dependency
from auth.jwthandler import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from auth.users import get_password_hash, authenticate_user
from schemas.user import UserRegSchema, UserOutSchema
from schemas.token import Token
from database.models import Users
from file_system.settings import IMAGES_USERS_DIR
from errors.my_errors import USERNAME_IS_OCCUPIED_ERROR, INCORRECT_UN_OR_PSWD_ERROR

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

        IMAGES_USERS_DIR.joinpath(str(new_user.id_user)).mkdir()
    except: 
        raise USERNAME_IS_OCCUPIED_ERROR
    return UserOutSchema(id_user=new_user.id_user, username=new_user.username)


async def login(username, password: str, db: db_dependency):
    user = authenticate_user(username=username, password=password, db=db)
    if not user:
        raise INCORRECT_UN_OR_PSWD_ERROR
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={ "sub": user.username }, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


