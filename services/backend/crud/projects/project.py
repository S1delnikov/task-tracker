from database.connection import db_dependency
from schemas.project import ProjectInSchema, ProjectOutSchema, ProjectUserOutSchema
from database.models import Projects, ProjectsUsers, Users


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