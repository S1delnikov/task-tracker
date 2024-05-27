from PIL import Image
from fastapi import UploadFile
from .settings import IMAGES_USERS_SIZE
import pyclamd
import clamav
import zipfile


async def compress_image(path_to_img: str):
    img = Image.open(path_to_img)
    img.thumbnail(IMAGES_USERS_SIZE)
    img.save(path_to_img)


async def compress_file(file_path, zip_path, filename):
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(filename=file_path, arcname=filename)  