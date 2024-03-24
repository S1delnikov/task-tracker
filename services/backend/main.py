from fastapi import FastAPI, APIRouter, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# import schemas
from typing import Annotated
# import models
from database.settings import engine, SessionLocal
from database import models
from sqlalchemy.orm import Session
from passlib.context import CryptContext
# import jwthandler
from auth import jwthandler
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["https://task-2-vue.onrender.com"],
#     allow_credentials=True, 
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/')
def home():
    return {'data': 'Hello, stranger'}


