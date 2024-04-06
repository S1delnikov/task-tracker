from database.connection import db_dependency
from schemas.project import ProjectInSchema, ProjectOutSchema, ProjectUserOutSchema
from database.models import Projects, ProjectsUsers, Users
from errors.my_errors import PROJECT_NOT_EXIST_ERROR, PERMISSION_DENIED_ERROR


async def create_proj(
        data: ProjectInSchema,
        id_user: int,
        db: db_dependency
):
    """Метод создания проекта."""
    project = Projects(
        name = data.name,
        description = data.description
    )
    db.add(project)
    db.commit()
    db.refresh(project)

    link_project_and_user = ProjectsUsers(
        id_project = project.id_project,
        id_user = id_user
    )
    db.add(link_project_and_user)
    db.commit()
    db.refresh(link_project_and_user)

    return  {
        "project": ProjectOutSchema.model_validate(project),
        "link_project_and_user": ProjectUserOutSchema.model_validate(link_project_and_user)
        }
    # return proj


async def update_proj(
        data: ProjectInSchema,
        id_project: int,
        id_user: int,
        db: db_dependency
):
    """Метод обновления проекта."""
    project = db.query(ProjectsUsers).filter(ProjectsUsers.id_project==id_project, ProjectsUsers.id_user==id_user).first()
    if not project:
        raise PROJECT_NOT_EXIST_ERROR
    if project.role != "owner" and project.role != "editor":
        raise PERMISSION_DENIED_ERROR
    
    project = db.query(Projects).filter(Projects.id_project==id_project).first()
    project.name = data.name
    project.description = data.description
    
    db.commit()
    db.refresh(project)

    return ProjectOutSchema.model_validate(project)