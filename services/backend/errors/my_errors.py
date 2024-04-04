from fastapi import HTTPException, status

USERNAME_IS_OCCUPIED_ERROR = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This username is occupied by another person.")
INCORRECT_UN_OR_PSWD_ERROR = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect username or password.",headers={"WWW-Authenticate": "Bearer"},)

TASK_NOT_EXIST_ERROR = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task doesn't exist.")
SUBTASK_NOT_EXIST_ERROR = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Subtask doesn't exist.")

PROJECT_NOT_EXIST_ERROR = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Project doesn't exist.")
PERMISSION_DENIED_ERROR = HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Permission denied.")