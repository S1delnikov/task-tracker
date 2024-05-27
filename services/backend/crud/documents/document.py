from database.connection import db_dependency
from database.models import Users, Documents, UsersDocuments
from schemas.document import DocumentSchema
from time import time
from shutil import rmtree
from os import remove
from file_system.settings import DOCUMENTS_DIR, TEMP_DIR, BASE_DIR
from file_system.methods import compress_file
from errors.my_errors import FILE_IS_NOT_EXIST, PERMISSION_DENIED_ERROR, USER_NOT_EXIST_ERROR, USER_IS_ALREADY_HAS_FILE
from fastapi import UploadFile


async def upload_document(
      id_user: int,
      document: UploadFile,
      db: db_dependency
):
      print(document.content_type)
      old_filename = document.filename
      temp_path = f"{TEMP_DIR}/{id_user}/{old_filename}"
      temp_dir = f"{TEMP_DIR}/{id_user}"
      document.filename = f"{time()}_{id_user}.zip"
      zip_path = f"{DOCUMENTS_DIR}/{id_user}/{document.filename}"
      with open(temp_path, 'wb+') as dest: ######
            dest.write(document.file.read())
      await compress_file(file_path=temp_path, zip_path=zip_path, filename=old_filename)

      rmtree(temp_dir)
      TEMP_DIR.joinpath(str(id_user)).mkdir()
    
      new_path = ""
      for node in zip_path.split('/')[-3:]:
            new_path += f"/{node}"

      print(new_path)
      document = Documents(
            name = old_filename,
            path = new_path
      )
      db.add(document)
      db.commit()
      db.refresh(document)

      user_document = UsersDocuments(
            id_user = id_user,
            id_document = document.id_document
      )
      db.add(user_document)
      db.commit()
      db.refresh(user_document)

      return {'document': DocumentSchema.model_validate(document), 'user_document': user_document}


async def delete_document(
      id_user: int,
      id_document: int,
      db: db_dependency
):
      row = db.query(UsersDocuments).filter(UsersDocuments.id_user==id_user, UsersDocuments.id_document==id_document).first()
      if not row:
            raise FILE_IS_NOT_EXIST
      if row.role != "owner":
            raise PERMISSION_DENIED_ERROR
      del row 

      document = db.query(Documents).filter(Documents.id_document==id_document).first()
      remove(str(BASE_DIR) + document.path)
      db.delete(document)
      db.commit()
      
      return DocumentSchema.model_validate(document)


async def share_document(
      id_user: int,
      id_document: int,
      id_new_user: int,
      db: db_dependency
):
      row = db.query(UsersDocuments).filter(UsersDocuments.id_user==id_user, UsersDocuments.id_document==id_document).first()
      if not row:
            raise FILE_IS_NOT_EXIST
      if row.role != "owner":
            raise PERMISSION_DENIED_ERROR
      del row 

      exist = db.query(UsersDocuments).filter(UsersDocuments.id_user==id_new_user, UsersDocuments.id_document==id_document).first()
      if exist:
            raise USER_IS_ALREADY_HAS_FILE

      new_user = db.query(Users).filter(Users.id_user==id_new_user).first()
      if not new_user:
            raise USER_NOT_EXIST_ERROR
      del new_user

      new__user_document = UsersDocuments(
            id_user = id_new_user,
            id_document = id_document,
            role = "editor"
      )
      db.add(new__user_document)
      db.commit()
      db.refresh(new__user_document)

      return new__user_document
