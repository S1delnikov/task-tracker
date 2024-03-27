from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from .settings import Base


# Таблица пользователей
class Users(Base):
    __tablename__ = 'users'

    id_user = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    email = Column(String, default="")
    password = Column(String)
    disabled = Column(String, default=False)
    date_of_registration = Column(DateTime)

# Таблица друзей пользователя
class Friends(Base):
    __tablename__ = 'friends'

    id_sender = Column(Integer, ForeignKey('users.id_user', ondelete="CASCADE"), primary_key=True)
    id_recipient = Column(Integer, ForeignKey('users.id_user', ondelete="CASCADE"), primary_key=True)
    relation_type = Column(String, default="")

# Таблица задач
class Tasks(Base):
    __tablename__ = 'tasks'

    id_task = Column(Integer, primary_key=True, index=True)
    title = Column(String, default="")
    description = Column(String, default="")
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    done = Column(Boolean, default=False)
    rank = Column(String, default="")
    category = Column(String, default="")
    id_project = Column(Integer, ForeignKey("projects.id_project", ondelete="CASCADE"), default=None)
    id_user = Column(Integer, ForeignKey("users.id_user", ondelete="CASCADE"))

# Таблица подзадач
class Subtasks(Base):
    __tablename__ = 'subtasks'

    id_subtask = Column(Integer, primary_key=True, index=True)
    title = Column(String, default="")
    description = Column(String, default="")
    done = Column(Boolean, default=False)
    id_task = Column(Integer, ForeignKey("tasks.id_task", ondelete="CASCADE"))

# Таблица проектов
class Projects(Base):
    __tablename__ = 'projects'

    id_project = Column(Integer, primary_key=True, index=True)
    name = Column(String, default="")
    description = Column(String, default="")

# Таблица-посредник между пользователями и проектами
class ProjectsUsers(Base):
    __tablename__ = 'projects_users'

    id_project = Column(Integer, ForeignKey("projects.id_project", ondelete="CASCADE"), primary_key=True)
    id_user = Column(Integer, ForeignKey("users.id_user", ondelete="CASCADE"), primary_key=True)
    role = Column(String, default="owner")

# Таблица сообщений пользователей
class Messages(Base):
    __tablename__ = 'messages'

    id_message = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    id_project = Column(Integer, ForeignKey("projects.id_project", ondelete="CASCADE"))
    id_user = Column(Integer, ForeignKey("users.id_user", ondelete="CASCADE"))

# Таблица с содержимым сообщений пользователя
class Contents(Base):
    __tablename__ = 'contents'

    id_content = Column(Integer, primary_key=True, index=True)
    text = Column(String, default="")
    image = Column(String, default="") # путь к изображению
    id_message = Column(Integer, ForeignKey("messages.id_message", ondelete="CASCADE"))

