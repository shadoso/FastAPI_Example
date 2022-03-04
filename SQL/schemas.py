from pydantic import BaseModel
from typing import Optional, Set
from SQL.types import Gender, Disability, Course


class Post(BaseModel):
    # uuid: Optional[UUID] = uuid4()
    name: str
    surname: str
    gender: Gender
    # role: Role
    # email: str = "defaultemail@ChimeraCore.com"
    # password: str
    disabilities: Optional[Set[Disability]]
    # created_date: datetime


class PostEmployee(Post):
    course: Optional[Set[Course]] = None

    # salary: float

    class Config:
        orm_mode = True


class PostStudent(Post):
    course: Course
    # monthly_payment: float

    class Config:
        orm_mode = True


class Login(BaseModel):
    email: str
    password: str
