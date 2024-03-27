from pydantic import BaseModel
from datetime import datetime


class TaskSoloSchema(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    done: bool = False
    # rank: str


class TaskProjSchema(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    done: bool = False
    rank: str
    category: str
    id_project: int
    id_user: int