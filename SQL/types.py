from enum import Enum


class Gender(Enum):
    male = "Male"
    female = "Female"


class Role(Enum):
    admin = "Admin"
    coordinator = "Coordinator"
    staff = "Staff"
    teacher = "Teacher"
    student = "Student"
    guest = "Guest"


class Course(Enum):
    cs = "Computer Science"
    ds = "Data Science"
    anth = "Anthropology"
    bioeng = "Bioengineering"
    ling = "Linguistics"
    psyc = "Psychology"


class Scholarship(Enum):
    full = 1.00
    half = 0.50
    quarter = 0.25
    none = 0.00


class Access(Enum):
    classroom = "Classroom"
    lecture = "Lecture"
    cafeteria = "Cafeteria"


class Disability(Enum):
    mobility = "Mobility impairment"
    eyesight = "Eyesight impairment"
    hearing = "Hearing impairment"
    physical = "Physical impairment"
    cognitive = "Cognitive impairment"


class LifeTime(Enum):
    daylong = "Daylong"
    monthlong = "Monthlong"
    yearlong = "Yearlong"
    permanent = "Permanent"
