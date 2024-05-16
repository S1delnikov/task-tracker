from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
IMAGES_USERS_DIR = BASE_DIR.joinpath('images/users')
IMAGES_PROJECTS_DIR = BASE_DIR.joinpath('images/projects')

DEFAULT_PROFILE_PIC = BASE_DIR.joinpath('images/users/default/default.jpeg')

IMAGES_USERS_SIZE = (300, 300)
ALLOWED_CONTENT_TYPE = ['image/jpg', 'image/jpeg', 'image/png', 'image/webp', 'image/gif']