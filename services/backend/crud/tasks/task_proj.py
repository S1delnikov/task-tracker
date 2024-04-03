from database.connection import db_dependency
from schemas.task import TaskProjInSchema, TaskProjOutSchema
from database.models import Projects, ProjectsUsers, Tasks
from errors.my_errors import PROJECT_NOT_EXIST_ERROR


async  def create_task(
        data: TaskProjInSchema,
        id_project: int,
        id_user: int,
        db: db_dependency
):
    project = db.query(ProjectsUsers).filter(ProjectsUsers.id_project==id_project, ProjectsUsers.id_user==id_user).first()
    if not project:
        raise PROJECT_NOT_EXIST_ERROR
    del project
    
    task = Tasks(
        title=data.title,
        description=data.description,
        start_date=data.start_date,
        end_date=data.end_date,
        done=data.done,
        rank=data.rank,
        category=data.category,
        id_project=id_project,
        id_user=id_user
    )
    db.add(task)
    db.commit()
    db.refresh(task)

    return TaskProjOutSchema.model_validate(task)


async def update_task(
        
):
    ...


async def delete_task(
        
):
    ...


async def get_task(
        
):
    ...


async def get_tasks(
        
):
    ...