from fastapi import APIRouter, Depends
from typing import Annotated
from auth.jwthandler import get_current_user
from database.connection import db_dependency
from schemas.user import UserInSchema
from schemas.task import TaskSoloSchema, TaskProjSchema
import crud.tasks.task_solo as crud_solo
# import crud.tasks.task_proj as crud_proj

router = APIRouter()

@router.post('/create_task_solo')
async def create_task_solo(
    data: TaskSoloSchema,
    current_user: Annotated[UserInSchema, Depends(get_current_user)],
    db: db_dependency
):
    return await crud_solo.create_task(data=data, id_user=current_user.id_user, db=db)


@router.post('/update_task_solo/{id_task}')
async def update_task_solo(
    id_task,
    data: TaskSoloSchema,
    current_user: Annotated[UserInSchema, Depends(get_current_user)],
    db: db_dependency
):
    return await crud_solo.update_task(data=data, id_task=id_task, id_user=current_user.id_user, db=db)


@router.post('/delete_task_solo/{id_task}')
async def delete_task_solo(
    id_task,
    current_user: Annotated[UserInSchema, Depends(get_current_user)],
    db: db_dependency
):
    return await crud_solo.delete_task(id_task=id_task, id_user=current_user.id_user, db=db)