from PIL import Image
from fastapi import UploadFile
from .settings import IMAGES_USERS_SIZE

async def compress_image(path_to_img: str):
    img = Image.open(path_to_img)
    img.thumbnail(IMAGES_USERS_SIZE)
    # img.resize(IMAGES_USERS_SIZE, Image.ANTIALIAS)
    img.save(path_to_img)


