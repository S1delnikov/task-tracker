from pydantic import BaseModel


class ProjectInSchema(BaseModel):
    name: str
    description: str

    class Config:
        from_attributes = True


class ProjectOutSchema(BaseModel):
    id_project: int
    name: str
    description: str

    class Config:
        from_attributes = True


class ProjectUserOutSchema(BaseModel):
    id_project: int
    id_user: int
    role: str

    class Config:
        from_attributes = True