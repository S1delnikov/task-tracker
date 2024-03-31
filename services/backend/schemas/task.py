from pydantic import BaseModel
from datetime import datetime
from typing import List
from .subtask import SubtaskOutSchema

class TaskSoloInSchema(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    done: bool = False
    # rank: str
    class Config:
        from_attributes = True


class TaskSoloOutSchema(BaseModel):
    id_task: int
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    done: bool = False
    subtasks: List[SubtaskOutSchema] = None
    
    class Config:
        from_attributes = True


class TaskProjInSchema(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    done: bool = False
    rank: str
    category: str
    id_project: int
    id_user: int

    class Config:
        from_attributes = True