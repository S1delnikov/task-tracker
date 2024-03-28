from pydantic import BaseModel


class SubtaskSchema(BaseModel):
    title: str
    description: str
    done: bool = False
    id_task: int
