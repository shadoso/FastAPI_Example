from PostgreSQL_Database import Base
from sqlalchemy import Column, Numeric, String, Enum, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from enum import Enum
from typing import Optional, List

LENGTH_NAME = 56
PRECISION = 2
SCALE = 8
EMAIL = """Name + Role + Unique + @ChimeraCore.com
Only users that are attached to college can have it"""


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


class User(Base):
    __tablename__ = "Users"

    uid: Column(UUID, nullable=False, primary_key=True)
    name: Column(String(length=LENGTH_NAME), nullable=False)
    email: Column(String, comment=EMAIL, nullable=True, unique=True)  # Check This
    gender: Column(Enum(Gender), nullable=False)
    role: Column(Enum(Role), nullable=False)
    course: Column(ARRAY(Enum(Courses)), nullable=True)
    salary: Column(Numeric(precision=PRECISION, scale=SCALE), nullable=True)
    monthly_payment: Column(Numeric(precision=PRECISION, scale=SCALE), nullable=True)
    scholarship: Column(Enum(Scholarship), nullable=True)
    disabilities: Column(ARRAY(Enum(Disability)), nullable=True)
