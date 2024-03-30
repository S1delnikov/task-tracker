from typing import List
from fastapi import HTTPException, status
from datetime import timedelta
from database.connection import db_dependency
from auth.jwthandler import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from auth.users import get_password_hash, authenticate_user
from schemas.user import UserInSchema
from schemas.task import TaskSoloSchema, AllTaskSoloSchema, TaskProjSchema
from schemas.token import Token
from database.models import Users, Tasks
from errors.my_errors import TASK_NOT_EXIST_ERROR


async def create_task(
        data: TaskSoloSchema, 
        id_user: int, 
        db: db_dependency
):
    """Данный метод создаёт одиночную задачу для личного использования"""

    task = Tasks(
        title=data.title,
        description=data.description,
        start_date=data.start_date,
        end_date=data.end_date,
        done=data.done,
        # rank=data.rank,
        id_user=id_user
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


async def update_task(
        data: TaskSoloSchema,
        id_task: int,
        id_user: int,
        db: db_dependency
):
    """Данный метод обновляет данные одиночной задачи для личного пользования"""

    task = db.query(Tasks).filter(Tasks.id_task==id_task, Tasks.id_user==id_user).first()
    if not task:
        raise TASK_NOT_EXIST_ERROR
    
    task.title = data.title
    task.description = data.description
    task.start_date = data.start_date
    task.end_date = data.end_date
    task.done = data.done

    db.commit()
    db.refresh(task)
    return task


async def delete_task(
       id_task: int,
       id_user: int,
       db: db_dependency
):
    """Данный метод удаляет одиночную задачу для личного пользования"""

    task = db.query(Tasks).filter(Tasks.id_task==id_task, Tasks.id_user==id_user).first()
    if not task:
        raise TASK_NOT_EXIST_ERROR
    
    db.delete(task)
    db.commit()
    
    return {"message": "Task deleted successfully"}


async def get_task(
        id_task: int,
        id_user: int,
        db: db_dependency
):
    """Данный метод возвращает одиночную задачу пользователя"""

    task = db.query(Tasks).filter(Tasks.id_task==id_task, Tasks.id_user==id_user).first()
    if not task:
        raise TASK_NOT_EXIST_ERROR
    
    return AllTaskSoloSchema.model_validate(task)


async def get_tasks(id_user: int, db: db_dependency):
    """Данный метод возвращает все одиночные задачи пользователя"""

    tasks = db.query(Tasks).filter(Tasks.id_user==id_user).all()
    tasks = [AllTaskSoloSchema.model_validate(task) for task in tasks]
    return tasks