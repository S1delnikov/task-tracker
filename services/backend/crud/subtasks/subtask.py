from fastapi import HTTPException, status
from schemas.subtask import SubtaskSchema
from database.models import Tasks, Subtasks, Users
from database.connection import db_dependency


async def create_subtask(data: SubtaskSchema, id_task: int, db: db_dependency):
    """Метод создания подзадачи. Работает для одиночных задач и проектных задач."""

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
        id_task = id_task
    )
    db.add(subtask)
    db.commit()
    db.refresh(subtask)
    
    return subtask


async def update_subtask(data: SubtaskSchema, id_subtask: int, id_user, db: db_dependency):
    """
    Метод обновления подзадачи. Работает для одиночных задач и проектных задач.
    
    SELECT subtasks.id_subtask, subtasks.title, subtasks.description, subtasks.done FROM subtasks\n
    JOIN tasks on tasks.id_task = subtasks.id_task\n
    JOIN users on tasks.id_user = users.id_user\n
    WHERE users.id_user = current_user.id_user AND subtasks.id_subtask = subtask_on_update.id_subtask;

    """
    
    subtask = \
        db.query(Subtasks) \
        .join(Tasks, Tasks.id_task==Subtasks.id_task) \
        .join(Users, Users.id_user==Tasks.id_user) \
        .filter(Users.id_user==id_user, Subtasks.id_subtask==id_subtask) \
        .first()
    
    if not subtask:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Subtask doesn't exists."    
        )
    
    subtask.title = data.title
    subtask.description = data.description
    subtask.done = data.done

    db.commit()
    db.refresh(subtask)

    return subtask


async def delete_subtask(id_subtask, id_user: int, db: db_dependency):
    subtask = \
        db.query(Subtasks) \
        .join(Tasks, Tasks.id_task==Subtasks.id_task) \
        .join(Users, Users.id_user==Tasks.id_user) \
        .filter(Users.id_user==id_user, Subtasks.id_subtask==id_subtask) \
        .first()
    
    if not subtask:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Subtask doesn't exists."
        )
    
    db.delete(subtask)
    db.commit()
    
    return {"message": "Subtask deleted successfully."}