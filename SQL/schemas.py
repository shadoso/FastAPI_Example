from pydantic import BaseModel
from typing import Optional, Set
from SQL.types import Gender, Disability, Role


class Post(BaseModel):
    # uuid: UUID
    name: str
    surname: str
    # fullname: str = name + surname
    gender: Gender
    # role: Role
    # access: Optional[Set[Access]]
    # email: str = "defaultemail@ChimeraCore.com"
    # password: str
    # monetary: relationship("Monetary")
    disabilities: Optional[Set[Disability]]
    # created_date: datetime


class Login(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class ShowUser(Post):
    role: Role
    email: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    uuid: Optional[str]
    role: Optional[Role]
