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
    com_sci = "Computer Science"
    dat_sci = "Data Science"
    ant = "Anthropology"
    bio_eng = "Bioengineering"
    ling = "Linguistics"
    psych = "Psychology"


class Access(Enum):
    classroom = "Classroom"
    hall = "Lecture Hall"
    server = "Server Room"
    computer = "Computer Lab"
    bio_eng = "Bioengineering Lab"
    library = "Library Hall"


class Disability(Enum):
    mobility = "Mobility Impairment"
    eyesight = "Eyesight Impairment"
    hearing = "Hearing Impairment"
    physical = "Physical Impairment"
    cognitive = "Cognitive Impairment"


class Payment(Enum):
    salary = "Salary"
    tuition = "College Tuition"
    lecture = "Lecture Fee"
