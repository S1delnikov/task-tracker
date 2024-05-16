from fastapi import HTTPException, status, UploadFile, File
from fastapi.responses import FileResponse
from database.connection import db_dependency
from file_system.settings import BASE_DIR, IMAGES_USERS_DIR, ALLOWED_CONTENT_TYPE, DEFAULT_PROFILE_PIC
from file_system.methods import compress_image
from shutil import rmtree
from os import listdir
from errors.my_errors import FILE_IS_NOT_AN_IMAGE, IMAGE_TYPE_NOT_ALLOWED

async def save_profile_pic(
        id_user: int, 
        file: UploadFile,
        db: db_dependency
):
    try:
        if file.content_type in ALLOWED_CONTENT_TYPE:
            rmtree(f"{IMAGES_USERS_DIR}/{id_user}")
            IMAGES_USERS_DIR.joinpath(str(id_user)).mkdir()
            file.filename = f"{id_user}.{file.content_type.split('/')[1]}"
            dest_path = f"{IMAGES_USERS_DIR}/{id_user}/{file.filename}"
            with open(dest_path, 'wb+') as dest:
                dest.write(file.file.read())

            await compress_image(dest_path)

            return {'id_user': id_user, "filename": file}
        else: 
            raise IMAGE_TYPE_NOT_ALLOWED
    except:
        raise FILE_IS_NOT_AN_IMAGE


async def get_profile_pic(
        id_user: int,
        db: db_dependency
):
    try:
        dir = f"{IMAGES_USERS_DIR}/{id_user}/"
        content = listdir(dir)
        if len(content) == 0:
            return {"profile_pic": FileResponse(DEFAULT_PROFILE_PIC), "other_pic": FileResponse(f"{IMAGES_USERS_DIR}/antarctica3.jpg")}
        
        full_path = f"{dir}{content[0]}"
        return {'profile_pic': FileResponse(full_path)}
    except:
        ...