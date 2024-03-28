from pydantic import BaseModel


class SubtaskCreateSchema(BaseModel):
    title: str
    description: str
    done: bool = False
