from fastapi import Depends
from fastapi import APIRouter
from Utility import hashing
from uuid import uuid4
from SQL import schemas
from SQL.session import database
from SQL import models
from SQL.models import Role
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/ChimeraCore",
    tags=["Create"]
)

COLLEGE_EMAIL = "@ChimeraCore.com"


@router.post("/create/{role}")
async def create_user(
        post: schemas.Post, role: Role,
        code: str = str(uuid4())[::5],
        data: Session = Depends(database)
):

    hashed = hashing.hashed(code)
    unique = str(uuid4())[11::5]
    college_email = post.name + role.value + unique + COLLEGE_EMAIL
    user = role

    users = models.Users(**post.dict(), email=college_email, password=hashed, role=user)

    data.add(users)
    data.commit()
    data.refresh(users)

    return {f"{user.value}": users.email}
