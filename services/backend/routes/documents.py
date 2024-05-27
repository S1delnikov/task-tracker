from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from typing import Annotated
from database.connection import db_dependency
from schemas.user import UserInSchema
from auth.jwthandler import get_current_user
import crud.documents.document as crud


router = APIRouter()


@router.post('/upload_document')
async def upload_document(
    current_user: Annotated[UserInSchema, Depends(get_current_user)],
    document: UploadFile,
    db: db_dependency
):
    return await crud.upload_document(id_user=current_user.id_user, document=document, db=db)


@router.delete('/delete_document/{id_document}')
async def delete_document(
    id_document,
    current_user: Annotated[UserInSchema, Depends(get_current_user)],
    db: db_dependency
):
    return await crud.delete_document(id_user=current_user.id_user, id_document=id_document, db=db)
