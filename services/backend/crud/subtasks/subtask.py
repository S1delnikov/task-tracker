from fastapi import HTTPException, status
from schemas.subtask import SubtaskSchema
from database.models import Tasks, Subtasks
from database.connection import db_dependency


async def create_subtask(data: SubtaskSchema, id_task: int, db: db_dependency):
    task = db.query(Tasks).filter(Tasks.id_task==id_task).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Task doesn't exists."    
        )
    del task
    subtask = Subtasks (
        title = data.title,
        description = data.description,
        done = data.done,
        id_task = data.id_task
    )
    db.add(subtask)
    db.commit()
    db.refresh(subtask)
    
    return subtask