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
from auth import jwthandler
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from routes import users, tasks, subtasks, projects

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["https://task-2-vue.onrender.com"],
#     allow_credentials=True, 
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

models.Base.metadata.create_all(bind=engine)


app.include_router(users.router)
app.include_router(tasks.router)
app.include_router(subtasks.router)
app.include_router(projects.router)