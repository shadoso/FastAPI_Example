from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel
from typing import Optional, List


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


class Scholarship(float, Enum):
    full = 1.00
    half = 0.50
    quarter = 0.25


class Disability(str, Enum):
    mobility = "Mobility impairment"
    eyesight = "Eyesight impairment"
    hearing = "Hearing impairment"
    physical = "Physical impairment"
    cognitive = "Cognitive impairment"


class User(BaseModel):
    uid: Optional[UUID] = uuid4()
    name: str
    gender: Gender
    role: Role
    course: Optional[List[Courses]] = None
    salary: Optional[float] = None
    monthly_payment: Optional[float] = None
    scholarship: Optional[Scholarship] = None
    disabilities: Optional[List[Disability]] = None


class UpdateInfo(BaseModel):
    role: Role
    course: List[Courses]
    salary: Optional[float] = None
    monthly_payment: Optional[float] = None
    scholarship: Optional[Scholarship] = None
