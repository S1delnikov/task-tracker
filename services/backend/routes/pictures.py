from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from typing import Annotated
from database.connection import db_dependency
from schemas.user import UserInSchema
from auth.jwthandler import get_current_user
import crud.users.picture as crud

router = APIRouter()

@router.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    print(file)
    return {"file_size": len(file)}
    # return file

@router.post("/upload_profile_pic/")
async def create_upload_file(
    current_user: Annotated[UserInSchema, Depends(get_current_user)],
    file: UploadFile,
    db: db_dependency
):
    return await crud.save_profile_pic(id_user=current_user.id_user, file=file, db=db)


@router.get('/get_profile_pic')
async def get_profile_pic(
    current_user: Annotated[UserInSchema, Depends(get_current_user)],
    db: db_dependency
):
    return await crud.get_profile_pic(id_user=current_user.id_user, db=db)