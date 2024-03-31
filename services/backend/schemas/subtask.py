from pydantic import BaseModel


class SubtaskSchema(BaseModel):
    title: str
    description: str
    done: bool = False

    class Config:
        from_attributes = True


class SubtaskOutSchema(BaseModel):
    id_subtask: int
    title: str
    description: str
    done: bool = False

    class Config:
        from_attributes = True
