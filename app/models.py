from sqlmodel import Field, SQLModel
from datetime import datetime


class JobBase(SQLModel):
    title: str
    description: str
    company: str
    location: str


class Job(JobBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=datetime.now(), nullable=False)


class JobCreate(JobBase):
    pass


class JobPublic(JobBase):
    id: int


class JobUpdate(SQLModel):
    title: str | None
    description: str | None
    company: str | None
    location: str | None
