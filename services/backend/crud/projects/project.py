from database.connection import db_dependency
from schemas.project import ProjectInSchema, ProjectOutSchema, ProjectUserOutSchema
from schemas.user import UserOutSchema
from database.models import Projects, ProjectsUsers, Users
from errors.my_errors import (
    PROJECT_NOT_EXIST_ERROR, 
    PERMISSION_DENIED_ERROR, 
    USER_NOT_EXIST_ERROR, 
    USER_IS_NOT_A_MEMBER,
    SUICIDE_IS_NOT_A_WAY_OUT
)


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


async def delete_proj(
        id_project: int,
        id_user: int,
        db: db_dependency
):
    """Метод удаления проекта."""
    project = db.query(ProjectsUsers).filter(ProjectsUsers.id_project==id_project, ProjectsUsers.id_user==id_user).first()
    if not project:
        raise PROJECT_NOT_EXIST_ERROR
    if project.role != "owner":
        raise PERMISSION_DENIED_ERROR
    
    project = db.query(Projects).filter(Projects.id_project==id_project).first()

    db.delete(project)
    db.commit()

    return {"message": "Project deleted successfully."}


async def add_member(
        id_project: int,
        id_user: int,
        id_new_user: int,
        db: db_dependency,
        role: str = "editor",
):
    """Метод добавления сторонних пользователей в проект."""
    project = db.query(ProjectsUsers).filter(ProjectsUsers.id_project==id_project, ProjectsUsers.id_user==id_user).first()
    if not project:
        raise PROJECT_NOT_EXIST_ERROR
    if project.role != "owner":
        raise PERMISSION_DENIED_ERROR
    del project

    new_user = db.query(Users).filter(Users.id_user==id_new_user).first()
    if not new_user:
        raise USER_NOT_EXIST_ERROR
    del new_user

    new_member = ProjectsUsers(
        id_project = id_project,
        id_user = id_new_user,
        role = role
    )
    try:
        db.add(new_member)
        db.commit()
    except:
        return {"message": "This user is already a member of the project."}

    return {"new_project_member": ProjectUserOutSchema.model_validate(new_member)}


async def delete_member(
        id_project: int,
        id_member_on_delete: int,
        id_user: int,
        db: db_dependency
):
    project = db.query(ProjectsUsers).filter(ProjectsUsers.id_project==id_project, ProjectsUsers.id_user==id_user).first()
    if not project:
        raise PROJECT_NOT_EXIST_ERROR
    if project.role != "owner":
        raise PERMISSION_DENIED_ERROR
    del project
    
    member_on_delete = db.query(ProjectsUsers).filter(ProjectsUsers.id_project==id_project, ProjectsUsers.id_user==id_member_on_delete).first()
    if not member_on_delete:
        raise USER_IS_NOT_A_MEMBER
    if member_on_delete.id_user == id_user:
        raise SUICIDE_IS_NOT_A_WAY_OUT
    db.delete(member_on_delete)
    db.commit()

    return {"deleted_member": ProjectUserOutSchema.model_validate(member_on_delete)}


async def get_member(
        id_project: int,
        id_user: int,
        db: db_dependency
):
    project = db.query(Projects).filter(Projects.id_project==id_project).first()
    if not project:
        raise PROJECT_NOT_EXIST_ERROR
    del project
    user = db.query(Users).join(ProjectsUsers, ProjectsUsers.id_user==id_user).filter(ProjectsUsers.id_project==id_project).first()
    if not user:
        raise USER_IS_NOT_A_MEMBER
    
    return UserOutSchema.model_validate(user)


async def get_members(
        id_project: int,
        db: db_dependency
):
    project = db.query(Projects).filter(Projects.id_project==id_project).first()
    if not project:
        raise PROJECT_NOT_EXIST_ERROR
    del project

    members = db.query(Users).join(ProjectsUsers, ProjectsUsers.id_user==Users.id_user).filter(ProjectsUsers.id_project==id_project).all()
    members = [UserOutSchema.model_validate(member) for member in members]

    return members