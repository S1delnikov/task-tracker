from fastapi import HTTPException, status
from datetime import timedelta
from database.connection import db_dependency
from auth.jwthandler import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from auth.users import get_password_hash, authenticate_user
from schemas.user import UserInSchema
from schemas.task import TaskSolo, TaskProj
from schemas.token import Token
from database.models import Users, Tasks


async def create_task(
        data: TaskSolo, 
        id_user: int, 
        db: db_dependency):
    task = Tasks(
        title=data.title,
        description=data.description,
        start_date=data.start_date,
        end_date=data.end_date,
        status=data.status,
        rank=data.rank,
        id_user=id_user
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task