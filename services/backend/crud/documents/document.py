from database.connection import db_dependency
from database.models import Users, Documents, UsersDocuments
from schemas.document import DocumentSchema
from time import time
from shutil import rmtree
from os import listdir
from file_system.settings import DOCUMENTS_DIR, TEMP_DIR
from file_system.methods import compress_file
from fastapi import UploadFile


async def upload_file(
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
            name = "Документ",
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