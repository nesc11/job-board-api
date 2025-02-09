from enum import Enum

from sqlmodel import Field, SQLModel
from pydantic import EmailStr
from datetime import datetime


# Users
class RoleEnum(str, Enum):
    recruiter = "recruiter"
    candidate = "candidate"


class UserBase(SQLModel):
    first_name: str = Field(min_length=3, max_length=50)
    last_name: str = Field(min_length=3, max_length=50)
    email: EmailStr = Field(min_length=3, max_length=50)
    role: RoleEnum


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    hashed_password: str = Field(nullable=False)


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=32)


class UserPublic(UserBase):
    id: int


# Jobs
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
