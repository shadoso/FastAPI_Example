from SQL.session import Base
from SQL.types import Access, Disability, Gender, Payment, Role
from sqlalchemy import ARRAY, Boolean, Column, DateTime, Enum, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now
import sqlalchemy

LENGTH_NAME = 25
LENGTH_SURNAME = 35
PRECISION = 8
SCALE = 2


class Users(Base):
    __tablename__ = 'users'

    uuid = Column(UUID, nullable=False, primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"))
    name = Column(String(length=LENGTH_NAME), nullable=False)
    surname = Column(String(length=LENGTH_SURNAME), nullable=False)
    fullname = Column(String, nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    role = Column(Enum(Role), nullable=False)
    access = Column(ARRAY(Enum(Access)), nullable=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    monetary = relationship("Monetary")
    disabilities = Column(ARRAY(Enum(Disability)), nullable=True)
    created_date = Column(DateTime(timezone=True), server_default=now())


class Monetary(Base):
    __tablename__ = 'monetary'

    user_fk = Column(UUID, ForeignKey(Users.uuid, ondelete="CASCADE"), primary_key=True)
    activity = Column(Boolean, default=False, nullable=False)
    archetype = Column(Enum(Payment), nullable=False)
    payment = Column(Numeric(precision=PRECISION, scale=SCALE), nullable=True)


# class Project(Base):
#     __tablename__ = 'project'
#
#     project_id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
#     author = Column(String, ForeignKey(Users.fullname, ondelete="CASCADE"))
#     title = Column(String, nullable=False)
#     content = Column(String, nullable=False)
#     approved = Column(Boolean, default=False, nullable=False)
#     owner = relationship("Users")
#     #  Create on update
#     created_date = Column(DateTime(timezone=True), server_default=now())

# class Classroom(Base):
#     __tablename__ = 'classroom'
#      Will receive (teacher, student or coordinator)uuid
#      Course will be a set, and student can only have 1
#      Class name will be a set, and student can only have 1
#      Activity from monetary
#     pass
