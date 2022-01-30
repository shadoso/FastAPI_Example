from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel
from typing import Optional, Set


class Gender(str, Enum):
    male = "Male"
    female = "Female"


class Role(str, Enum):
    admin = "Admin"
    coordinator = "Coordinator"
    teacher = "Teacher"
    student = "Student"
    guest = "Guest"


class Courses(str, Enum):
    cs = "Computer Science"
    ds = "Data Science"
    anth = "Anthropology"
    bioeng = "Bioengineering"
    ling = "Linguistics"
    psyc = "Psychology"


class Disability(str, Enum):
    mobility = "Mobility impairment"
    eyesight = "Eyesight impairment"
    hearing = "Hearing impairment"
    physical = "Physical impairment"
    cognitive = "Cognitive impairment"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    gender: Gender
    role: Role
    course: Set[Courses] = None
    disabilities: Optional[Set[Disability]] = None


class UpdateInfo(BaseModel):
    role: Role
    course: Set[Courses]
