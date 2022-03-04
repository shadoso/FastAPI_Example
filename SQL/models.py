import sqlalchemy
from sqlalchemy.orm import relationship
from SQL.types import Gender, Role, Disability, Payment
from sqlalchemy.sql.functions import now
from sqlalchemy import Column, Numeric, String, Enum, ARRAY, DateTime, ForeignKey, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID
from SQL.session import Base

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
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    monetary = relationship("Monetary")
    #  Project need to be restructured
    #  Access
    disabilities = Column(ARRAY(Enum(Disability)), nullable=True)
    created_date = Column(DateTime(timezone=True), server_default=now())


class Monetary(Base):
    __tablename__ = 'monetary'

    user_fk = Column(UUID, ForeignKey(Users.uuid, ondelete="CASCADE"), primary_key=True)
    activity = Column(Boolean, default=False, nullable=False)
    payment = Column(Enum(Payment), nullable=False)
    exchange = Column(Numeric(precision=PRECISION, scale=SCALE), nullable=True)


# class Project(Base):
#     __tablename__ = 'project'
#
#     project_id = Column(Integer, primary_key=True, nullable=False)
#     author = Column(String, ForeignKey(Users.fullname, ondelete="CASCADE"))
#     author_email = Column(String, ForeignKey(Users.email, ondelete="CASCADE"))
#     title = Column(String, nullable=False)
#     content = Column(String, nullable=False)
#     approved = Column(Boolean, default=False, nullable=False)
#     created_date = Column(DateTime(timezone=True), server_default=now())
#
#
# class Classroom(Base):
#     __tablename__ = 'classroom'
#      Will receive (teacher, student or coordinator)uuid
#      Course will be a set, and student can only have 1
#      Class name will be a set, and student can only have 1
#      Activity from monetary
#     pass
