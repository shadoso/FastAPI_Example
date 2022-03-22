from pydantic import BaseModel
from SQL.types import Disability, Gender, Role
from typing import Optional, Set


class Post(BaseModel):
    # uuid: UUID
    name: str
    surname: str
    fullname: str
    gender: Gender
    # role: Role
    # access: Optional[Set[Access]]
    email: str = "defaultemail@ChimeraCore.com"
    password: str
    # monetary: relationship("Monetary")
    disabilities: Optional[Set[Disability]]
    # created_date: datetime


class Login(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    role: Role
    email: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    uuid: str
    fullname: str
    role: Role
