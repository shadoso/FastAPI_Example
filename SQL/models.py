import sqlalchemy

from SQL.types import Gender, Role, Access, Disability, Course, Scholarship, LifeTime
from uuid import uuid4
from sqlalchemy.sql.functions import now
from sqlalchemy import Column, Numeric, String, Enum, ARRAY, DateTime
from sqlalchemy.dialects.postgresql import UUID
from SQL.session import Base


LENGTH_NAME = 23
LENGTH_SURNAME = 35
PASSWORD_LENGTH = 56
PRECISION = 8
SCALE = 2


class Employee(Base):
    __tablename__ = 'employee'

    uuid = Column(UUID, nullable=False, primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    name = Column(String(length=LENGTH_NAME), nullable=False)
    surname = Column(String(length=LENGTH_SURNAME), nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    role = Column(Enum(Role), nullable=False)
    email = Column(String, nullable=False)
    password = Column(String(length=PASSWORD_LENGTH), nullable=False)
    disabilities = Column(ARRAY(Enum(Disability)), nullable=True)
    created_date = Column(DateTime(timezone=True), server_default=now())

    # course = Column(ARRAY(Enum(Course)), nullable=True)
    # salary = Column(Numeric(precision=PRECISION, scale=SCALE), nullable=False)


class Student(Base):
    __tablename__ = 'student'

    uuid = Column(UUID, nullable=False, primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    name = Column(String(length=LENGTH_NAME), nullable=False)
    surname = Column(String(length=LENGTH_SURNAME), nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    role = Column(Enum(Role), nullable=False, default=Role.student)
    email = Column(String, nullable=False)
    password = Column(String(length=PASSWORD_LENGTH), nullable=False)
    disabilities = Column(ARRAY(Enum(Disability)), nullable=True)
    created_date = Column(DateTime(timezone=True), server_default=now())

    # course = Column(Enum(Course), nullable=True)
    # monthly_payment = Column(Numeric(precision=PRECISION, scale=SCALE), nullable=True)
    # scholarship = Column(Enum(Scholarship), nullable=True)


class Guest(Base):
    __tablename__ = 'guest'

    uuid = Column(UUID, nullable=False, primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    name = Column(String(length=LENGTH_NAME), nullable=False)
    surname = Column(String(length=LENGTH_SURNAME), nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    role = Column(Enum(Role), nullable=False, default=Role.guest)
    email = Column(String, nullable=False)
    password = Column(String(length=PASSWORD_LENGTH), nullable=False)
    disabilities = Column(ARRAY(Enum(Disability)), nullable=True)
    created_date = Column(DateTime(timezone=True), server_default=now())

    # description = Column(String, nullable=True)
    # access = Column(ARRAY(Enum(Access)), nullable=True)
    # life_time = Column(Enum(LifeTime), nullable=True)
