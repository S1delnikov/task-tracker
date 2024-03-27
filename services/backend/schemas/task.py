from pydantic import BaseModel
from datetime import datetime

BaseModel.from_orm = True

class TaskSolo(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    done: bool = False
    # rank: str
    class Config:
        from_attributes=True

class TaskProj(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    done: bool = False
    rank: str
    category: str
    id_project: int
    id_user: int