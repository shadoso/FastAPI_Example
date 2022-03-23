from pydantic import BaseModel
from SQL.types import Disability, Gender, Role, Payment
from typing import Optional, Set


class Post(BaseModel):
    # uuid: UUID
    name: str
    surname: str
    # fullname: Optional[str] = None
    gender: Gender
    # role: Role
    # access: Optional[Set[Access]]
    username: str = "defaultemail@ChimeraCore.com"
    password: str
    # monetary: relationship("Monetary")
    disabilities: Optional[Set[Disability]]
    # created_date: datetime


class Login(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class UserStatus(BaseModel):
    activity: bool
    archetype: Payment
    payment: float

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    fullname: str
    role: Role
    username: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    uuid: str
    fullname: str
    role: Role
