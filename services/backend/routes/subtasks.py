from fastapi import APIRouter, Depends
from typing import Annotated
from auth.jwthandler import get_current_user
from database.connection import db_dependency
from schemas.subtask import SubtaskCreateSchema
from schemas.user import UserInSchema
import crud.subtasks.subtask as crud


router = APIRouter()

@router.post('/create_subtask/{id_task}')
async def create_subtask(
    id_task,
    data: SubtaskCreateSchema,
    current_user: Annotated[UserInSchema, Depends(get_current_user)],
    db: db_dependency
):
    return await crud.create_subtask(data=data, id_task=id_task, db=db)