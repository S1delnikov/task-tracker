from fastapi import APIRouter, Depends
from typing import Annotated
from auth.jwthandler import get_current_user
from database.connection import db_dependency
from schemas.project import ProjectInSchema
from schemas.user import UserInSchema
import crud.projects.project as crud_proj


router = APIRouter()

@router.post('/create_proj')
async def create_proj(
    data: ProjectInSchema,
    current_user: Annotated[UserInSchema, Depends(get_current_user)],
    db: db_dependency
):
    return await crud_proj.create_proj(data=data, id_user=current_user.id_user, db=db)