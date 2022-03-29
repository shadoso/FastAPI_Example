from pydantic import BaseModel, EmailStr
from SQL.types import Disability, Gender, Role, Exchange
from typing import Optional, Set, List
from uuid import UUID


class Login(BaseModel):
    username: str = "DefaultUser"
    password: str


class User(BaseModel):
    name: str
    surname: str
    gender: Gender

    class Config:
        orm_mode = True


class CreateUser(User):
    email: EmailStr
    username: str = "DefaultUser"
    password: str
    disabilities: Optional[Set[Disability]]

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    fullname: str
    role: Role

    class Config:
        orm_mode = True


class UserStatus(BaseModel):
    status: bool = False
    category: Exchange
    payment: float = 0.00

    class Config:
        orm_mode = True


class SecretShow(Login, ShowUser):
    uuid: UUID
    context: List[UserStatus]

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    uuid: UUID
    status: bool
    fullname: str
    role: Role
